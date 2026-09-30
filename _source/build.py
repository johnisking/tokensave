#!/usr/bin/env python3
"""Build the static multi-language, multi-tool site for tokensave.app.

src/base.html (shared layout) + src/<page>_body.html + src/i18n*.py + src/*.js + src/styles.css  ->  dist/
  dist/index.html, video.html, image.html           English tools (/, /video, /image)
  dist/<slug>/index.html, video.html, image.html    other languages (/<slug>/, /<slug>/video, /<slug>/image)
  dist/about.html, privacy.html, 404.html           English site pages
  dist/styles.css (Tailwind, compiled), *.js, static files, CNAME, robots.txt, sitemap.xml, ads.txt

Run:  python3 build.py      (needs Node for Tailwind: the first run installs it into tw/node_modules)
"""
import html, json, os, shutil, hashlib, subprocess, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
from i18n import LANGS, S
from i18n_video import NAV, V
from i18n_image import I
from i18n_site import SITE
from seo_meta import META
from blog_meta import BLOG, BLOG_DATE
LLM = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "llm_prices.json"), encoding="utf-8"))

# ---------------------------------------------------------------- settings
BASE = "https://tokensave.app"
LASTMOD = "2026-09-30"
# Google AdSense publisher id, e.g. "ca-pub-1234567890123456". Empty = no ad code on the pages.
ADSENSE_PUB = "ca-pub-6520495092767533"
# Search engine ownership tags (content value only). Empty = not added.
VERIFY = {
    "google-site-verification": "",
    "naver-site-verification": "131662d11b92d5ad870f190a7d06d1d96c50a225",
    "msvalidate.01": "575FA911DCD5006EA2DA8F4A4EE835AA",
    "seznam-wmt": "m6Gmw0zFrG6YmBXyMKJZ9VEh6991V35s",
}

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, DIST, TW = os.path.join(ROOT, "src"), os.path.join(ROOT, "dist"), os.path.join(ROOT, "tw")
JS_FILES = ["common.js", "token.js", "video.js", "image.js"]
DEV_POST = "https://dev.to/jaehyun_cho_0dff271e0d2e5/i-sent-the-same-prompt-in-27-languages-czech-costs-2x-english-chinese-costs-the-same-420m"
BLOG_BY_TAG = {b["tag"]: b for b in BLOG}
MORE_CLS = "inline-block whitespace-nowrap font-semibold text-amber-300 underline underline-offset-2 decoration-amber-400/40 hover:text-white"

def more_link(tag, label):
    b = BLOG_BY_TAG.get(tag)
    if b:
        return f'<a href="{b["path"]}" class="{MORE_CLS}">{esc(label)} →</a>'
    return f'<a href="{DEV_POST}" target="_blank" rel="noopener" class="{MORE_CLS}">{esc(label)} ↗</a>'

# Image page reuses shared labels from the video page strings
SHARED = ["badge", "res", "model", "total", "na", "cheapest", "srcOfficial", "srcRunway", "f2"]
IMG = {tag: {**{k: V[tag][k] for k in SHARED}, **{k: v for k, v in I[tag].items() if k != "navImage"}} for tag in I}
for tag in I:
    NAV[tag]["navImage"] = I[tag]["navImage"]

TOOLS = [
    dict(key="token", nav="navToken", body="token_body.html", strings=S, script="token.js",
         file="index.html", page="", og="og-token.jpg",
         runtime=["note", "exact", "based", "est", "waste", "efficient", "great", "moderate", "high",
                  "share", "tSaved", "tAlready", "tNothing", "tCopied", "tCleared",
                  "overhead", "overheadTip", "chatErr", "chatInfo",
                  "toEn", "undo", "tDownloading", "tTranslating", "tTranslated", "tNoSupport", "tLangNA", "tFail", "tRestored", "saveTok", "stepSpaces", "stepEn", "stepShort", "tSavedAll", "monthSaved"]),
    dict(key="video", nav="navVideo", body="video_body.html", strings=V, script="video.js",
         file="video.html", page="video", og="og-video.jpg",
         runtime=["na", "noAudio", "cheapest", "srcOfficial", "srcRunway", "audioIncl", "clipNote"]),
    dict(key="image", nav="navImage", body="image_body.html", strings=IMG, script="image.js",
         file="image.html", page="image", og="og-image.jpg",
         runtime=["na", "cheapest", "srcOfficial", "srcRunway"]),
]

# English-only site pages (not in the tool menu)
PAGES = [
    dict(file="about.html", path="/about", body="about_body.html",
         title="About TokenSave",
         desc="Free, private AI calculators for tokens, video and image costs in 27 languages."),
    dict(file="privacy.html", path="/privacy", body="privacy_body.html",
         title="Privacy Policy | TokenSave",
         desc="How TokenSave handles data: text stays in your browser, cookieless analytics, ads."),
    dict(file="404.html", path=None, body="404_body.html",
         title="Page not found | TokenSave", desc="This page does not exist."),
]

NAV_ON = "px-2.5 py-1 rounded-md font-semibold tab-active"
NAV_OFF = "px-2.5 py-1 rounded-md font-semibold text-zinc-400 hover:text-zinc-100 hover:bg-zinc-800"
ARIA = ' aria-current="page"'
VIEW_IN = {(slug or "en"): SITE[tag]["viewIn"] for slug, tag, *_ in LANGS}

def path_for(slug, tool):
    return (f"/{slug}/" if slug else "/") + tool["page"]

def url_for(slug, tool):
    return BASE + path_for(slug, tool)

def js(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")

def esc(v):
    return html.escape(v, quote=True)

def head_extras():
    out = [f'  <meta name="{k}" content="{esc(v)}" />' for k, v in VERIFY.items() if v]
    if ADSENSE_PUB:
        out.append(f'  <meta name="google-adsense-account" content="{ADSENSE_PUB}" />')
        out.append(f'  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_PUB}" crossorigin="anonymous"></script>')
    return "\n".join(out)

def faq_html(s):
    qs = [(s[f"q{i}"], s[f"a{i}"]) for i in (1, 2, 3, 4) if f"q{i}" in s]
    if not qs:
        return ""
    cards = "\n".join(
        f'''      <div class="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-5">
        <h2 class="font-semibold mb-1.5">{esc(q)}</h2>
        <p class="text-zinc-400">{esc(a)}</p>
      </div>''' for q, a in qs)
    cols = "sm:grid-cols-2 lg:grid-cols-4" if len(qs) == 4 else "sm:grid-cols-3"
    return f'    <section class="mt-12 grid {cols} gap-4 text-sm">\n{cards}\n    </section>'

def compile_css():
    if not os.path.isdir(os.path.join(TW, "node_modules")):
        subprocess.run(["npm", "install", "--silent"], cwd=TW, check=True)
    subprocess.run(["npx", "tailwindcss", "-c", "tailwind.config.js", "-i", "../src/styles.css",
                    "-o", os.path.join(DIST, "styles.css"), "--minify"], cwd=TW, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def render(base, body, values):
    out = base.replace("{{body}}", body)
    for k, v in values.items():
        out = out.replace("{{" + k + "}}", v)
    assert "{{" not in out, f"unfilled placeholder: {out[out.index('{{'):][:40]}"
    return out

def build():
    base = open(os.path.join(SRC, "base.html"), encoding="utf-8").read()
    shutil.rmtree(DIST, ignore_errors=True)
    os.makedirs(DIST)
    compile_css()

    h = hashlib.sha1()
    for f in JS_FILES:
        h.update(open(os.path.join(SRC, f), "rb").read())
    h.update(open(os.path.join(DIST, "styles.css"), "rb").read())
    ver = h.hexdigest()[:8]
    extras = head_extras()

    for tool in TOOLS:
        en = tool["strings"]["en"]
        for _, tag, *_ in LANGS:
            missing = [k for k in en if k not in tool["strings"][tag]]
            assert not missing, f"{tool['key']} {tag} missing keys: {missing}"
            assert tag in NAV and tag in SITE, f"NAV/SITE missing {tag}"

    count = 0
    for tool in TOOLS:
        body = open(os.path.join(SRC, tool["body"]), encoding="utf-8").read()
        hreflang = "\n".join(
            f'  <link rel="alternate" hreflang="{tag}" href="{url_for(slug, tool)}" />' for slug, tag, *_ in LANGS
        ) + f'\n  <link rel="alternate" hreflang="x-default" href="{url_for("", tool)}" />'

        for slug, tag, native, og, direction in LANGS:
            s = dict(tool["strings"][tag])
            s.setdefault("lang", S[tag]["lang"])
            s["title"], s["desc"] = META[tool["key"]][tag]
            assert len(s["title"]) <= 40 and len(s["desc"]) <= 80, f"meta too long: {tool['key']} {tag}"
            options = "\n".join(
                f'          <option value="{path_for(sl, tool)}" data-code="{sl or "en"}"{" selected" if sl == slug else ""}>{esc(nat)}</option>'
                for sl, _, nat, _, _ in LANGS
            )
            nav = "\n".join(
                f'          <a href="{path_for(slug, t)}" class="{NAV_ON if t is tool else NAV_OFF}"'
                f'{ARIA if t is tool else ""}>{esc(NAV[tag][t["nav"]])}</a>'
                for t in TOOLS
            )
            url = url_for(slug, tool)
            graph = [
                {"@type": "WebApplication", "name": s["h1"], "url": url, "inLanguage": tag,
                 "applicationCategory": "DeveloperApplication", "operatingSystem": "Any",
                 "isAccessibleForFree": True, "description": s["desc"],
                 "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                 "publisher": {"@type": "Organization", "name": "TokenSave", "url": BASE + "/"}},
                {"@type": "FAQPage", "inLanguage": tag, "mainEntity": [
                    {"@type": "Question", "name": s[f"q{i}"],
                     "acceptedAnswer": {"@type": "Answer", "text": s[f"a{i}"]}} for i in (1, 2, 3, 4) if f"q{i}" in s]},
            ]
            if tool["page"]:
                graph.append({"@type": "BreadcrumbList", "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": url_for(slug, TOOLS[0])},
                    {"@type": "ListItem", "position": 2, "name": s["h1"], "item": url}]})
            runtime = {k: s[k] for k in tool["runtime"]}
            if tool["key"] == "token":
                runtime["prices"] = {k: {"in": v["in"], "out": v["out"]} for k, v in LLM["models"].items()}
            runtime["viewIn"] = VIEW_IN
            values = {k: esc(v) for k, v in s.items()}
            values.update({k: esc(v) for k, v in SITE[tag].items()})
            values.update(
                htmlLang=tag, dir=direction, url=url, ogLocale=og, ogImage=f"{BASE}/{tool['og']}",
                homeUrl=path_for(slug, TOOLS[0]), hreflang=hreflang, langOptions=options, toolNav=nav,
                ver=ver, adsHead=extras, faq=faq_html(s), moreLink=more_link(tag, s.get("more", "")),
                ldjson=js({"@context": "https://schema.org", "@graph": graph}),
                tjson=js(runtime),
                scriptTag=f'<script type="module" src="/{tool["script"]}?v={ver}"></script>',
            )
            folder = os.path.join(DIST, slug) if slug else DIST
            os.makedirs(folder, exist_ok=True)
            open(os.path.join(folder, tool["file"]), "w", encoding="utf-8").write(render(base, body, values))
            count += 1

    # English site pages
    en_nav = "\n".join(f'          <a href="{path_for("", t)}" class="{NAV_OFF}">{esc(NAV["en"][t["nav"]])}</a>' for t in TOOLS)
    en_opts = "\n".join(
        f'          <option value="{path_for(sl, TOOLS[0])}" data-code="{sl or "en"}"{" selected" if not sl else ""}>{esc(nat)}</option>'
        for sl, _, nat, _, _ in LANGS)
    for pg in PAGES:
        body = open(os.path.join(SRC, pg["body"]), encoding="utf-8").read()
        url = BASE + (pg["path"] or "/404")
        values = dict(
            htmlLang="en", dir="ltr", url=url, ogLocale="en_US", ogImage=f"{BASE}/og-token.jpg",
            title=esc(pg["title"]), desc=esc(pg["desc"]), lang=esc(S["en"]["lang"]),
            homeUrl="/", hreflang="", langOptions=en_opts, toolNav=en_nav, ver=ver, adsHead=extras, faq="",
            f1="", f2="", fAbout=esc(SITE["en"]["fAbout"]), fPrivacy=esc(SITE["en"]["fPrivacy"]),
            ldjson=js({"@context": "https://schema.org", "@type": "WebPage", "name": pg["title"], "url": url}),
            tjson=js({"static": True}),
            scriptTag=f'<script type="module" src="/common.js?v={ver}"></script>',
        )
        out = render(base, body, values)
        if pg["path"] is None:  # 404: keep out of the index, absolute canonical removed
            out = out.replace(f'  <link rel="canonical" href="{url}" />\n', '  <meta name="robots" content="noindex" />\n')
        open(os.path.join(DIST, pg["file"]), "w", encoding="utf-8").write(out)


    # Language-specific articles (/<slug>/blog/...)
    blog_alts = "\n".join(f'  <link rel="alternate" hreflang="{b["tag"]}" href="{BASE}{b["path"]}" />' for b in BLOG)
    tag_slug = {tag: slug for slug, tag, *_ in LANGS}
    tag_og = {tag: og for slug, tag, _, og, _ in LANGS}
    for b in BLOG:
        tag, slug = b["tag"], tag_slug[b["tag"]]
        assert b["path"].startswith(f"/{slug}/blog/") and len(b["desc"]) <= 120, b["path"]
        url = BASE + b["path"]
        tool_home = path_for(slug, TOOLS[0])
        article = open(os.path.join(SRC, "blog", tag + ".html"), encoding="utf-8").read()
        body = f"""    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <h1 class="text-2xl sm:text-3xl font-extrabold text-white leading-snug">{esc(b["title"])}</h1>
      <p class="mt-2 text-xs text-zinc-500">{esc(b["byline"])}</p>
{article}
      <div class="not-prose mt-8 rounded-xl border border-violet-500/30 bg-violet-500/10 p-5 text-center">
        <p class="text-zinc-200">{esc(b["cta"])}</p>
        <a href="{tool_home}" class="mt-3 inline-block tab-active rounded-lg px-4 py-2 font-semibold no-underline" style="text-decoration:none">{esc(b["ctaBtn"])} →</a>
      </div>
    </article>"""
        nav = "\n".join(f'          <a href="{path_for(slug, t)}" class="{NAV_OFF}">{esc(NAV[tag][t["nav"]])}</a>' for t in TOOLS)
        opts = "\n".join(
            f'          <option value="{path_for(sl, TOOLS[0])}" data-code="{sl or "en"}"{" selected" if sl == slug else ""}>{esc(nat)}</option>'
            for sl, _, nat, _, _ in LANGS)
        ld = {"@context": "https://schema.org", "@graph": [
            {"@type": "BlogPosting", "headline": b["title"], "description": b["desc"], "inLanguage": tag,
             "url": url, "mainEntityOfPage": url, "datePublished": BLOG_DATE, "dateModified": BLOG_DATE,
             "image": f"{BASE}/blog-language-tax-chart-v2.png",
             "author": {"@type": "Person", "name": "Jonhisking"},
             "publisher": {"@type": "Organization", "name": "TokenSave", "url": BASE + "/"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": BASE + tool_home},
                {"@type": "ListItem", "position": 2, "name": b["title"], "item": url}]}]}
        values = dict(
            htmlLang=tag, dir="ltr", url=url, ogLocale=tag_og[tag], ogImage=f"{BASE}/blog-language-tax-chart-v2.png",
            title=esc(b["title"] + " | TokenSave"), desc=esc(b["desc"]), lang=esc(S[tag]["lang"]),
            homeUrl=tool_home, hreflang=blog_alts, langOptions=opts, toolNav=nav, ver=ver, adsHead=extras, faq="",
            f1="", f2="", fAbout=esc(SITE[tag]["fAbout"]), fPrivacy=esc(SITE[tag]["fPrivacy"]),
            ldjson=js(ld), tjson=js({"static": True}),
            scriptTag=f'<script type="module" src="/common.js?v={ver}"></script>',
        )
        folder = os.path.join(DIST, slug, "blog")
        os.makedirs(folder, exist_ok=True)
        open(os.path.join(folder, b["path"].rsplit("/", 1)[1] + ".html"), "w", encoding="utf-8").write(render(base, body, values))

    for f in JS_FILES:
        shutil.copy(os.path.join(SRC, f), os.path.join(DIST, f))
    for f in os.listdir(os.path.join(SRC, "static")):
        shutil.copy(os.path.join(SRC, "static", f), os.path.join(DIST, f))
    open(os.path.join(DIST, "CNAME"), "w").write("tokensave.app\n")
    open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nUser-agent: Yeti\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    if ADSENSE_PUB:
        open(os.path.join(DIST, "ads.txt"), "w").write(
            f"google.com, {ADSENSE_PUB.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")

    # Sitemap with hreflang alternates for every tool page
    entries = []
    for tool in TOOLS:
        alts = "".join(
            f'\n    <xhtml:link rel="alternate" hreflang="{tag}" href="{url_for(sl, tool)}"/>' for sl, tag, *_ in LANGS
        ) + f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{url_for("", tool)}"/>'
        for slug, *_ in LANGS:
            entries.append(f"\n  <url>\n    <loc>{url_for(slug, tool)}</loc>\n    <lastmod>{LASTMOD}</lastmod>{alts}\n  </url>")
    for pg in PAGES:
        if pg["path"]:
            entries.append(f"\n  <url>\n    <loc>{BASE}{pg['path']}</loc>\n    <lastmod>{LASTMOD}</lastmod>\n  </url>")
    b_alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{b["tag"]}" href="{BASE}{b["path"]}"/>' for b in BLOG)
    for b in BLOG:
        entries.append(f"\n  <url>\n    <loc>{BASE}{b['path']}</loc>\n    <lastmod>{BLOG_DATE}</lastmod>{b_alts}\n  </url>")
    open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
        + "".join(entries) + "\n</urlset>\n"
    )
    print("built", count, "tool pages +", len(PAGES), "site pages +", len(BLOG), "articles ->", DIST)

if __name__ == "__main__":
    build()
