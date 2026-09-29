#!/usr/bin/env python3
"""Build the static multi-language, multi-tool site for tokensave.app.

src/base.html (shared layout) + src/<tool>_body.html + src/i18n*.py + src/*.js  ->  dist/
  dist/index.html, video.html, image.html   English
  dist/<slug>/index.html, video.html, image.html  other languages (served at /<slug>/, /<slug>/video, /<slug>/image)
  dist/common.js, token.js, video.js, CNAME, robots.txt, sitemap.xml
"""
import html, json, os, shutil, hashlib, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
from i18n import LANGS, S
from i18n_video import NAV, V
from i18n_image import I

# Image page reuses shared labels from the video page strings
SHARED = ["badge", "res", "model", "total", "na", "cheapest", "srcOfficial", "srcRunway", "f2"]
IMG = {tag: {**{k: V[tag][k] for k in SHARED}, **{k: v for k, v in I[tag].items() if k != "navImage"}} for tag in I}
for tag in I:
    NAV[tag]["navImage"] = I[tag]["navImage"]

BASE = "https://tokensave.app"
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, DIST = os.path.join(ROOT, "src"), os.path.join(ROOT, "dist")
JS_FILES = ["common.js", "token.js", "video.js", "image.js"]

TOOLS = [
    # key, nav label key, body file, strings, script, file name, page path, runtime keys
    dict(key="token", nav="navToken", body="token_body.html", strings=S, script="token.js",
         file="index.html", page="",
         runtime=["note", "exact", "based", "est", "waste", "efficient", "great", "moderate", "high",
                  "share", "tSaved", "tAlready", "tNothing", "tCopied", "tCleared"]),
    dict(key="video", nav="navVideo", body="video_body.html", strings=V, script="video.js",
         file="video.html", page="video",
         runtime=["na", "noAudio", "cheapest", "srcOfficial", "srcRunway", "audioIncl", "clipNote"]),
    dict(key="image", nav="navImage", body="image_body.html", strings=IMG, script="image.js",
         file="image.html", page="image",
         runtime=["na", "cheapest", "srcOfficial", "srcRunway"]),
]

def path_for(slug, tool):
    prefix = f"/{slug}/" if slug else "/"
    return prefix + tool["page"]

def url_for(slug, tool):
    return BASE + path_for(slug, tool)

# English pages only: send first-time visitors to their browser language (never overrides a saved choice).
REDIRECT = """  <script>
  (function () {
    try {
      var saved = localStorage.getItem('ts_lang');
      var MAP = %s;
      if (saved) { if (saved !== 'en' && MAP[saved]) location.replace(MAP[saved]); return; }
      var l = ((navigator.languages && navigator.languages[0]) || navigator.language || '').toLowerCase();
      var base = l.split('-')[0], key = null;
      if (base === 'zh') key = /-(tw|hk|mo|hant)/.test(l) ? 'zh-tw' : 'zh-cn';
      else if (MAP[base]) key = base;
      if (key) location.replace(MAP[key]);
    } catch (e) {}
  })();
  </script>"""

NAV_ON = "px-2.5 py-1 rounded-md font-semibold tab-active"
ARIA = ' aria-current="page"'
NAV_OFF = "px-2.5 py-1 rounded-md font-semibold text-zinc-400 hover:text-zinc-100 hover:bg-zinc-800"

def js(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")

def build():
    base = open(os.path.join(SRC, "base.html"), encoding="utf-8").read()
    h = hashlib.sha1()
    for f in JS_FILES:
        h.update(open(os.path.join(SRC, f), "rb").read())
    ver = h.hexdigest()[:8]

    shutil.rmtree(DIST, ignore_errors=True)
    os.makedirs(DIST)

    for tool in TOOLS:
        strings, en = tool["strings"], tool["strings"]["en"]
        for _, tag, *_ in LANGS:
            missing = [k for k in en if k not in strings[tag]]
            assert not missing, f"{tool['key']} {tag} missing keys: {missing}"
            assert tag in NAV, f"NAV missing {tag}"

    count = 0
    for tool in TOOLS:
        body = open(os.path.join(SRC, tool["body"]), encoding="utf-8").read()
        hreflang = "\n".join(
            f'  <link rel="alternate" hreflang="{tag}" href="{url_for(slug, tool)}" />' for slug, tag, *_ in LANGS
        ) + f'\n  <link rel="alternate" hreflang="x-default" href="{url_for("", tool)}" />'
        redirect_map = {slug: path_for(slug, tool) for slug, *_ in LANGS if slug}

        for slug, tag, native, og, direction in LANGS:
            s = dict(tool["strings"][tag])
            s.setdefault("lang", S[tag]["lang"])
            options = "\n".join(
                f'          <option value="{path_for(sl, tool)}" data-code="{sl or "en"}"{" selected" if sl == slug else ""}>{html.escape(nat)}</option>'
                for sl, _, nat, _, _ in LANGS
            )
            nav = "\n".join(
                f'          <a href="{path_for(slug, t)}" class="{NAV_ON if t is tool else NAV_OFF}"'
                f'{ARIA if t is tool else ""}>{html.escape(NAV[tag][t["nav"]])}</a>'
                for t in TOOLS
            )
            ld = {
                "@context": "https://schema.org", "@type": "WebApplication",
                "name": f"TokenSave – {s['h1']}", "url": url_for(slug, tool), "inLanguage": tag,
                "applicationCategory": "DeveloperApplication", "operatingSystem": "Any",
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                "description": s["desc"],
            }
            values = {k: html.escape(v, quote=True) for k, v in s.items()}
            values.update(
                htmlLang=tag, dir=direction, url=url_for(slug, tool), ogLocale=og,
                homeUrl=path_for(slug, TOOLS[0]), hreflang=hreflang, langOptions=options, toolNav=nav,
                script=tool["script"], ver=ver, ldjson=js(ld),
                tjson=js({k: s[k] for k in tool["runtime"]}),
                redirect=(REDIRECT % json.dumps(redirect_map)) if slug == "" else "",
            )
            out = base.replace("{{body}}", body)
            for k, v in values.items():
                out = out.replace("{{" + k + "}}", v)
            assert "{{" not in out, f"unfilled placeholder in {tool['key']} {tag}: {out[out.index('{{'):][:40]}"
            folder = os.path.join(DIST, slug) if slug else DIST
            os.makedirs(folder, exist_ok=True)
            open(os.path.join(folder, tool["file"]), "w", encoding="utf-8").write(out)
            count += 1

    for f in JS_FILES:
        shutil.copy(os.path.join(SRC, f), os.path.join(DIST, f))
    open(os.path.join(DIST, "CNAME"), "w").write("tokensave.app\n")
    open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")

    urls = "".join(
        f"\n  <url><loc>{url_for(slug, tool)}</loc><lastmod>2026-09-30</lastmod></url>"
        for tool in TOOLS for slug, *_ in LANGS
    )
    open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{urls}\n</urlset>\n"
    )
    print("built", count, "pages ->", DIST)

if __name__ == "__main__":
    build()
