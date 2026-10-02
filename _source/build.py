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
from blog_meta import BLOG, BLOG_DATE, PRO, MISTRAL_FR, PROMPT_PL, GUIDES, CC_COST, CC_LIMITS, CC_SAVE, CMP, GPT6, API_CMP, TPW, COUNT
CC = (CC_COST, CC_LIMITS, CC_SAVE)
MULTI = (CC_COST, CC_LIMITS, CC_SAVE, CMP, GPT6, API_CMP, TPW, COUNT)
PRO_BY_TAG = {b["tag"]: b for b in PRO}
from i18n_view import MORE_LANGS
from i18n_plans_all import PL, PNAV, PMETA
from i18n_agents_all import AG, AGNAV, AGMETA
import i18n_guides as GI
for _t in GI.CTX:
    S[_t]["a4"] = GI.a4(_t)
S["en"]["a4"] = ("Yes: across 41 languages, the same prompt uses from 1.03× (Simplified Chinese) to 2.44× (Punjabi) the tokens of English "
                 "on GPT's o200k tokenizer. Sending the prompt in English avoids most of that: the Save tokens button translates it on your "
                 "device (desktop Chrome / Edge) and asks for the reply in your language.")
LLM = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "llm_prices.json"), encoding="utf-8"))

# ---------------------------------------------------------------- settings
BASE = "https://tokensave.app"
LASTMOD = "2026-10-02"
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
JS_FILES = ["common.js", "token.js", "video.js", "image.js", "plans.js", "agents.js"]
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
for tag in PL:
    NAV[tag]["navPlans"] = PNAV[tag]
    META.setdefault("plans", {})[tag] = PMETA[tag]
for tag in AG:
    NAV[tag]["navAgents"] = AGNAV[tag]
    META.setdefault("agents", {})[tag] = AGMETA[tag]

TOOLS = [
    dict(key="token", nav="navToken", body="token_body.html", strings=S, script="token.js",
         file="index.html", page="", og="og-token.jpg",
         runtime=["note", "exact", "based", "est", "waste", "efficient", "great", "moderate", "high",
                  "share", "tSaved", "tAlready", "tNothing", "tCopied", "tCleared",
                  "overhead", "overheadTip", "chatErr", "chatInfo",
                  "toEn", "undo", "tDownloading", "tTranslating", "tTranslated", "tNoSupport", "tLangNA", "tFail", "tRestored", "saveTok", "stepSpaces", "stepEn", "stepShort", "tSavedAll", "monthSaved",
                  "viewTokMore", "viewTokWait", "tShareCopied", "tShareLong", "ctxFits", "ctxOver"]),
    dict(key="video", nav="navVideo", body="video_body.html", strings=V, script="video.js",
         file="video.html", page="video", og="og-video.jpg",
         runtime=["na", "noAudio", "cheapest", "srcOfficial", "srcRunway", "audioIncl", "clipNote"]),
    dict(key="image", nav="navImage", body="image_body.html", strings=IMG, script="image.js",
         file="image.html", page="image", og="og-image.jpg",
         runtime=["na", "cheapest", "srcOfficial", "srcRunway"]),
    dict(key="plans", nav="navPlans", body="plans_body.html", strings=PL, script="plans.js",
         file="plans.html", page="plans", og="og-token.jpg",
         runtime=["apiLabel", "perMonth", "cheaperApi", "cheaperPlan", "breakEven", "langNote"]),
    dict(key="agents", nav="navAgents", body="agents_body.html", strings=AG, script="agents.js",
         file="agents.html", page="agents", og="og-token.jpg",
         runtime=["apiLabel", "perMonth", "perTask", "apiCheaper", "planCheaper"]),
]

# English-only site pages (not in the tool menu)
PAGES = [
    dict(file="about.html", path="/about", body="about_body.html",
         title="About TokenSave",
         desc="Free, private AI calculators for tokens, video and image costs in 41 languages."),
    dict(file="languages.html", path="/languages", body=None,
         title="All 41 languages | TokenSave",
         desc="TokenSave in 41 languages, grouped by region, with how many GPT tokens each needs vs English."),
    dict(file="privacy.html", path="/privacy", body="privacy_body.html",
         title="Privacy Policy | TokenSave",
         desc="How TokenSave handles data: text stays in your browser, analytics and ads."),
    dict(file="contact.html", path="/contact", body="contact_body.html",
         title="Contact | TokenSave",
         desc="Contact TokenSave: report a wrong price, a missing model or a translation fix."),
    dict(file="terms.html", path="/terms", body="terms_body.html",
         title="Terms of Use | TokenSave",
         desc="Terms of use for TokenSave's free AI cost calculators."),
    dict(file="blog/index.html", path="/blog/", body=None,
         title="Blog: AI tokens, prices and costs | TokenSave",
         desc="Guides to AI tokens, API prices, video and image costs, and how to spend less."),
    dict(file="404.html", path=None, body="404_body.html",
         title="Page not found | TokenSave", desc="This page does not exist."),
]

NAV_ON = "px-2.5 py-1 rounded-md font-semibold tab-active"
NAV_OFF = "px-2.5 py-1 rounded-md font-semibold text-zinc-400 hover:text-zinc-100 hover:bg-zinc-800"
ARIA = ' aria-current="page"'
VIEW_IN = {(slug or "en"): SITE[tag]["viewIn"] for slug, tag, *_ in LANGS}

# Language menu: the 12 biggest languages, the current one if it is not among them, then "More languages…" (/languages).
# data-all keeps every language's URL so the browser-language suggestion still works for all 41.
TOP_LANGS = ["", "zh-cn", "es", "hi", "ar", "pt", "fr", "de", "ja", "ru", "ko", "id"]

def lang_menu(cur_slug, tag, url_of):
    native = {sl: nat for sl, _, nat, _, _ in LANGS}
    order = ([cur_slug] if cur_slug not in TOP_LANGS else []) + TOP_LANGS
    opt = lambda sl: (f'          <option value="{url_of(sl)}" data-code="{sl or "en"}"'
                      f'{" selected" if sl == cur_slug else ""}>{esc(native[sl])}</option>')
    all_urls = {(sl or "en"): url_of(sl) for sl, *_ in LANGS}
    return "\n".join([*(opt(sl) for sl in order),
                      '          <option disabled>──────────</option>',
                      f'          <option value="/languages">🌐 {esc(MORE_LANGS[tag])}</option>']), esc(json.dumps(all_urls))

# /languages: every language, grouped by region, with its measured token ratio vs English
REGIONS = [
    ("🌏", "East Asia", ["ko", "ja", "zh-CN", "zh-TW"]),
    ("🌏", "Southeast Asia", ["id", "vi", "th", "fil"]),
    ("🌏", "South Asia", ["hi", "bn", "ur", "mr", "gu", "kn", "ml", "ta", "te", "pa"]),
    ("🌍", "Middle East", ["ar", "fa", "he", "tr"]),
    ("🌎", "Western Europe & the Americas", ["en", "es", "pt", "fr", "de", "it", "nl"]),
    ("🌍", "Northern Europe", ["sv", "da", "no", "fi"]),
    ("🌍", "Central & Eastern Europe", ["ru", "uk", "pl", "cs", "sk", "hu", "ro", "el"]),
]

def languages_html():
    data = json.load(open(os.path.join(ROOT, "blog_data", "langdata.json"), encoding="utf-8"))
    info = {tag: (slug, nat, d) for slug, tag, nat, _, d in LANGS}
    blog = {b["tag"]: b["path"] for b in BLOG}
    assert sorted(t for *_, ts in REGIONS for t in ts) == sorted(info), "REGIONS must list every language once"
    tone = lambda r: "text-emerald-300" if r < 1.2 else "text-amber-300" if r < 1.6 else "text-rose-300"
    parts = []
    for icon, name, tags in REGIONS:
        cards = []
        for t in tags:
            slug, nat, d = info[t]
            r = data[t]["ro"]
            art = f'<a href="{blog[t]}" class="text-[11px] text-zinc-500 hover:text-violet-300">Details →</a>' if t in blog else ""
            cards.append(
                f'<li class="flex items-center justify-between gap-3 bg-zinc-950/60 border border-zinc-800 rounded-xl px-3 py-2.5 hover:border-violet-500/50">'
                f'<a href="{path_for(slug, TOOLS[0])}" class="min-w-0" lang="{t}" dir="{d}"><span class="block font-semibold text-zinc-100 truncate">{esc(nat)}</span>'
                f'<span class="block text-[11px] text-zinc-500" dir="ltr" lang="en">{esc(data[t]["name"])}</span></a>'
                f'<span class="ltr text-end shrink-0"><span class="block text-sm font-bold tabular-nums {tone(r)}">{r:.2f}×</span>{art}</span></li>')
        parts.append(f'      <h2 class="mt-8 text-sm font-bold uppercase tracking-wider text-zinc-400">{icon} {name}</h2>\n'
                     f'      <ul class="mt-3 grid grid-cols-1 sm:grid-cols-2 gap-2">\n        ' + "\n        ".join(cards) + "\n      </ul>")
    return ('    <section class="max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-5 sm:p-8">\n'
            '      <h1 class="text-2xl sm:text-3xl font-extrabold text-white">All 41 languages</h1>\n'
            '      <p class="mt-3 text-sm text-zinc-400">Pick your language to open the token counter in it. The number is how many GPT tokens '
            'the same text needs compared with English (o200k tokenizer, GPT-4o and later). Tap “Details” to read how it was measured.</p>\n'
            + "\n".join(parts) + '\n    </section>')

_LD = json.load(open(os.path.join(ROOT, "blog_data", "langdata.json"), encoding="utf-8"))
LANG_RATIOS = sorted(([tag, nat, _LD[tag]["ro"]] for _, tag, nat, _, _ in LANGS), key=lambda x: x[2])

def blog_index_html():
    en = GUIDES + [b for G in (PRO, BLOG, *MULTI) for b in G if b["tag"] == "en"]
    en.sort(key=lambda b: b.get("date", BLOG_DATE), reverse=True)
    cards = "\n".join(
        f'      <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{b["path"]}" class="block no-underline" style="text-decoration:none">'
        f'<span class="block font-semibold text-zinc-100">{esc(b["title"])}</span>'
        f'<span class="block mt-1 text-sm text-zinc-400">{esc(b["desc"])}</span></a></li>' for b in en)
    native = {tag: nat for _, tag, nat, _, _ in LANGS}
    other = [b for G in (BLOG, PRO, MISTRAL_FR, PROMPT_PL, *MULTI) for b in G if b["tag"] != "en"]
    other.sort(key=lambda b: native[b["tag"]])
    links = "\n".join(f'        <li><a href="{b["path"]}" lang="{b["tag"]}">{esc(native[b["tag"]])}: {esc(b["title"])}</a></li>' for b in other)
    return ('    <section class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">\n'
            '      <h1 class="text-3xl font-extrabold text-white">Blog</h1>\n'
            '      <p class="mt-3">Plain-English guides to what AI really costs: tokens, API prices, subscriptions, video and image generation, and practical ways to spend less.</p>\n'
            '      <ul class="not-prose mt-6 grid gap-3" style="list-style:none;padding:0">\n' + cards + '\n      </ul>\n'
            '      <h2>In other languages</h2>\n      <ul>\n' + links + '\n      </ul>\n    </section>')

def guide_links(tag, key):
    """Articles in the page language to link under the tool guide."""
    arts = {"token": [b for G in (BLOG, MISTRAL_FR, PROMPT_PL, GPT6, API_CMP, TPW, COUNT) for b in G if b["tag"] == tag],
            "plans": [b for G in (PRO, CMP) for b in G if b["tag"] == tag],
            "agents": [b for G in CC for b in G if b["tag"] == tag]}.get(key, [])
    return [(b["path"], b["title"]) for b in arts]

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
            options, lang_all = lang_menu(slug, tag, lambda sl: path_for(sl, tool))
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
            if tool["key"] == "agents":
                runtime["prices"] = {k: {"in": v["in"], "out": v["out"]} for k, v in LLM["models"].items()}
            if tool["key"] == "plans":
                runtime["prices"] = {k: {"in": v["in"], "out": v["out"]} for k, v in LLM["models"].items()}
                runtime["pageTag"] = tag
                runtime["langs"] = LANG_RATIOS
            if tool["key"] == "token":
                runtime["prices"] = {k: {"in": v["in"], "out": v["out"], "ctx": v.get("ctx")} for k, v in LLM["models"].items()}
            runtime["viewIn"] = VIEW_IN
            values = {k: esc(v) for k, v in s.items()}
            values.update({k: esc(v) for k, v in SITE[tag].items()})
            values.update(
                htmlLang=tag, dir=direction, url=url, ogLocale=og, ogImage=f"{BASE}/{tool['og']}",
                homeUrl=path_for(slug, TOOLS[0]), hreflang=hreflang, langOptions=options, langAll=lang_all, toolNav=nav,
                ver=ver, adsHead=extras, faq=faq_html(s),
                guide=(open(os.path.join(SRC, "guides", *([tag] if tag in ("ko", "ja") else []), tool["key"] + ".html"), encoding="utf-8").read() if tag in ("en", "ko", "ja")
                       else GI.guide(tag, tool["key"], guide_links(tag, tool["key"])) if tag in GI.CTX else ""), moreLink=more_link(tag, s.get("more", "")),
                proLink=(f'<a href="{PRO_BY_TAG[tag]["path"]}" class="text-violet-300 hover:text-violet-200 underline">{esc(PRO_BY_TAG[tag]["title"])} →</a>' if tag in PRO_BY_TAG else ""),
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
    en_opts, en_all = lang_menu("", "en", lambda sl: path_for(sl, TOOLS[0]))
    for pg in PAGES:
        body = languages_html() if pg["path"] == "/languages" else blog_index_html() if pg["path"] == "/blog/" else open(os.path.join(SRC, pg["body"]), encoding="utf-8").read()
        url = BASE + (pg["path"] or "/404")
        values = dict(
            htmlLang="en", dir="ltr", url=url, ogLocale="en_US", ogImage=f"{BASE}/og-token.jpg",
            title=esc(pg["title"]), desc=esc(pg["desc"]), lang=esc(S["en"]["lang"]),
            homeUrl="/", hreflang="", langOptions=en_opts, langAll=en_all, toolNav=en_nav, ver=ver, adsHead=extras, faq="", guide="",
            f1="", f2="", fAbout=esc(SITE["en"]["fAbout"]), fPrivacy=esc(SITE["en"]["fPrivacy"]),
            ldjson=js({"@context": "https://schema.org", "@type": "WebPage", "name": pg["title"], "url": url}),
            tjson=js({"static": True}),
            scriptTag=f'<script type="module" src="/common.js?v={ver}"></script>',
        )
        out = render(base, body, values)
        if pg["path"] is None:  # 404: keep out of the index, absolute canonical removed
            out = out.replace(f'  <link rel="canonical" href="{url}" />\n', '  <meta name="robots" content="noindex" />\n')
        os.makedirs(os.path.dirname(os.path.join(DIST, pg["file"])), exist_ok=True)
        open(os.path.join(DIST, pg["file"]), "w", encoding="utf-8").write(out)


    # Articles (/<slug>/blog/...): each group is one article in several languages, linked with hreflang
    plans_tool = next(t for t in TOOLS if t["key"] == "plans")
    tool_by_key = {t["key"]: t for t in TOOLS}
    og_by_key = {"video": "og-video.jpg", "image": "og-image.jpg"}
    for GROUP, gimg, gtool in [(BLOG, "blog-language-tax-chart-v4.png", TOOLS[0]), (PRO, "blog-chatgpt-pro-tiers.png", plans_tool), (MISTRAL_FR, "blog-mistral-francais.png", TOOLS[0]), (PROMPT_PL, "blog-prompt-polski.png", TOOLS[0])] + [
            ([g], og_by_key.get(g["tool"], "og-token.jpg"), tool_by_key[g["tool"]]) for g in GUIDES] + [
            (G, "og-token.jpg", tool_by_key["agents"]) for G in CC] + [(CMP, "og-token.jpg", plans_tool), (GPT6, "og-token.jpg", TOOLS[0]), (API_CMP, "og-token.jpg", TOOLS[0]), (TPW, "og-token.jpg", TOOLS[0]), (COUNT, "og-token.jpg", TOOLS[0])]:
      blog_en = next((b for b in GROUP if b["tag"] == "en"), None)
      blog_alts = "\n".join(f'  <link rel="alternate" hreflang="{b["tag"]}" href="{BASE}{b["path"]}" />' for b in GROUP) + (
          f'\n  <link rel="alternate" hreflang="x-default" href="{BASE}{blog_en["path"]}" />' if blog_en else "")
      tag_slug = {tag: slug for slug, tag, *_ in LANGS}
      tag_og = {tag: og for slug, tag, _, og, _ in LANGS}
      tag_dir = {tag: d for slug, tag, _, _, d in LANGS}
      for b in GROUP:
          tag, slug = b["tag"], tag_slug[b["tag"]]
          prefix = f"/{slug}/blog/" if slug else "/blog/"
          assert b["path"].startswith(prefix) and len(b["desc"]) <= 160, (b["path"], len(b["desc"]))
          bdate = b.get("date", BLOG_DATE)
          url = BASE + b["path"]
          tool_home = path_for(slug, TOOLS[0])
          cta_url = path_for(slug, gtool)
          article = open(os.path.join(SRC, "blog", b.get("src", tag) + ".html"), encoding="utf-8").read()
          body = f"""    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
        <h1 class="text-2xl sm:text-3xl font-extrabold text-white leading-snug">{esc(b["title"])}</h1>
        <p class="mt-2 text-xs text-zinc-500">{esc(b["byline"])}</p>
  {article}
        <div class="not-prose mt-8 rounded-xl border border-violet-500/30 bg-violet-500/10 p-5 text-center">
          <p class="text-zinc-200">{esc(b["cta"])}</p>
          <a href="{cta_url}" class="mt-3 inline-block tab-active rounded-lg px-4 py-2 font-semibold no-underline" style="text-decoration:none">{esc(b["ctaBtn"])} →</a>
        </div>
      </article>"""
          nav = "\n".join(f'          <a href="{path_for(slug, t)}" class="{NAV_OFF}">{esc(NAV[tag][t["nav"]])}</a>' for t in TOOLS)
          opts, opts_all = lang_menu(slug, tag, lambda sl: path_for(sl, TOOLS[0]))
          ld = {"@context": "https://schema.org", "@graph": [
              {"@type": "BlogPosting", "headline": b["title"], "description": b["desc"], "inLanguage": tag,
               "url": url, "mainEntityOfPage": url, "datePublished": bdate, "dateModified": bdate,
               "image": f"{BASE}/{gimg}",
               "author": {"@type": "Person", "name": "Jonhisking"},
               "publisher": {"@type": "Organization", "name": "TokenSave", "url": BASE + "/"}},
              {"@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": BASE + tool_home},
                  {"@type": "ListItem", "position": 2, "name": b["title"], "item": url}]}]}
          values = dict(
              htmlLang=tag, dir=tag_dir[tag], url=url, ogLocale=tag_og[tag], ogImage=f"{BASE}/{gimg}",
              title=esc(b["title"] + " | TokenSave"), desc=esc(b["desc"]), lang=esc(S[tag]["lang"]),
              homeUrl=tool_home, hreflang=blog_alts, langOptions=opts, langAll=opts_all, toolNav=nav, ver=ver, adsHead=extras, faq="", guide="",
              f1="", f2="", fAbout=esc(SITE[tag]["fAbout"]), fPrivacy=esc(SITE[tag]["fPrivacy"]),
              ldjson=js(ld), tjson=js({"static": True}),
              scriptTag=f'<script type="module" src="/common.js?v={ver}"></script>',
          )
          folder = os.path.join(DIST, slug, "blog") if slug else os.path.join(DIST, "blog")
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
    for GROUP in (BLOG, PRO, MISTRAL_FR, PROMPT_PL, *MULTI, *([g] for g in GUIDES)):
      b_alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{b["tag"]}" href="{BASE}{b["path"]}"/>' for b in GROUP)
      b_en = next((b for b in GROUP if b["tag"] == "en"), None)
      if b_en:
          b_alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{b_en["path"]}"/>'
      for b in GROUP:
        entries.append(f"\n  <url>\n    <loc>{BASE}{b['path']}</loc>\n    <lastmod>{b.get('date', BLOG_DATE)}</lastmod>{b_alts}\n  </url>")
    open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
        + "".join(entries) + "\n</urlset>\n"
    )
    print("built", count, "tool pages +", len(PAGES), "site pages +", len(BLOG) + len(PRO) + len(MISTRAL_FR) + len(PROMPT_PL) + len(GUIDES) + sum(map(len, MULTI)), "articles ->", DIST)

if __name__ == "__main__":
    build()
