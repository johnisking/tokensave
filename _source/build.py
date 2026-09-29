#!/usr/bin/env python3
"""Build static language pages for tokensave.app.

src/template.html + src/i18n.py + src/app.js  ->  dist/
  dist/index.html      English (home)
  dist/<slug>.html     one page per language, served by GitHub Pages at /<slug>
  dist/app.js, CNAME, robots.txt, sitemap.xml
"""
import html, json, os, shutil, hashlib, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from i18n import LANGS, S

BASE = "https://tokensave.app"
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, DIST = os.path.join(ROOT, "src"), os.path.join(ROOT, "dist")
RUNTIME_KEYS = ["note", "exact", "based", "est", "waste", "efficient", "great", "moderate", "high",
                "share", "tSaved", "tAlready", "tNothing", "tCopied", "tCleared"]

def url_for(slug):
    return f"{BASE}/{slug}" if slug else f"{BASE}/"

def path_for(slug):
    return f"/{slug}" if slug else "/"

# Home page only: send first-time visitors to their browser language (never overrides a saved choice).
REDIRECT = """  <script>
  (function () {
    try {
      var p = location.pathname;
      if (p !== '/' && p !== '/index.html') return;
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

def build():
    template = open(os.path.join(SRC, "template.html"), encoding="utf-8").read()
    app_js = open(os.path.join(SRC, "app.js"), encoding="utf-8").read()
    ver = hashlib.sha1(app_js.encode()).hexdigest()[:8]

    shutil.rmtree(DIST, ignore_errors=True)
    os.makedirs(DIST)

    en = S["en"]
    for _, tag, *_ in LANGS:
        missing = [k for k in en if k not in S[tag]]
        assert not missing, f"{tag} missing keys: {missing}"

    hreflang = "\n".join(
        f'  <link rel="alternate" hreflang="{tag}" href="{url_for(slug)}" />' for slug, tag, *_ in LANGS
    ) + f'\n  <link rel="alternate" hreflang="x-default" href="{url_for("")}" />'

    redirect_map = {(slug or "en"): path_for(slug) for slug, *_ in LANGS if slug}

    for slug, tag, native, og, direction in LANGS:
        s = S[tag]
        options = "\n".join(
            f'          <option value="{path_for(sl)}" data-code="{sl or "en"}"{" selected" if sl == slug else ""}>{html.escape(nat)}</option>'
            for sl, _, nat, _, _ in LANGS
        )
        ld = {
            "@context": "https://schema.org", "@type": "WebApplication",
            "name": f"TokenSave – {s['h1']}", "url": url_for(slug), "inLanguage": tag,
            "applicationCategory": "DeveloperApplication", "operatingSystem": "Any",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            "description": s["desc"],
        }
        values = {k: html.escape(v, quote=True) for k, v in s.items()}
        values.update(
            htmlLang=tag, dir=direction, url=url_for(slug), ogLocale=og, homeUrl=path_for(slug),
            hreflang=hreflang, langOptions=options, ver=ver,
            ldjson=json.dumps(ld, ensure_ascii=False).replace("</", "<\\/"),
            tjson=json.dumps({k: s[k] for k in RUNTIME_KEYS}, ensure_ascii=False).replace("</", "<\\/"),
            redirect=(REDIRECT % json.dumps(redirect_map)) if slug == "" else "",
        )
        out = template
        for k, v in values.items():
            out = out.replace("{{" + k + "}}", v)
        leftover = [m for m in ("{{",) if m in out]
        assert not leftover, f"unfilled placeholder in {tag}"
        name = "index.html" if slug == "" else f"{slug}.html"
        open(os.path.join(DIST, name), "w", encoding="utf-8").write(out)

    shutil.copy(os.path.join(SRC, "app.js"), os.path.join(DIST, "app.js"))
    open(os.path.join(DIST, "CNAME"), "w").write("tokensave.app\n")
    open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")

    # Language alternates are declared with hreflang in each page's <head>, so the sitemap just lists URLs.
    urls = "".join(
        f"\n  <url><loc>{url_for(slug)}</loc><lastmod>2026-09-30</lastmod></url>" for slug, *_ in LANGS
    )
    open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{urls}\n</urlset>\n"
    )
    print("built", len(LANGS), "pages ->", DIST)

if __name__ == "__main__":
    build()
