#!/usr/bin/env python3
"""Build the static multi-language, multi-tool site for tokensave.app.

src/base.html (shared layout) + src/<page>_body.html + src/i18n*.py + src/*.js + src/styles.css  ->  dist/
  dist/index.html, video.html, image.html           English tools (/, /video, /image)
  dist/<slug>/index.html, video.html, image.html    other languages (/<slug>/, /<slug>/video, /<slug>/image)
  dist/about.html, privacy.html, 404.html           English site pages
  dist/styles.css (Tailwind, compiled), *.js, static files, CNAME, robots.txt, sitemap.xml, ads.txt

Run:  python3 build.py      (needs Node for Tailwind: the first run installs it into tw/node_modules)
"""
import html, json, os, re, shutil, hashlib, subprocess, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))
from i18n import LANGS, S
from i18n_video import NAV, V
from i18n_image import I
from i18n_site import SITE
from seo_meta import META
from blog_meta import BLOG, BLOG_DATE, PRO, MISTRAL_FR, PROMPT_PL, GUIDES, CC_COST, CC_LIMITS, CC_SAVE, CMP, GPT6, API_CMP, TPW, COUNT, CHLIM, CXLIM, CMAX, AISITE, GEM4, RANK, GAME, GAME_HOWTO
CC = (CC_COST, CC_LIMITS, CC_SAVE, CXLIM, CMAX)
MULTI = (CC_COST, CC_LIMITS, CC_SAVE, CMP, GPT6, API_CMP, TPW, COUNT, CHLIM, CXLIM, CMAX, AISITE, GEM4, RANK, GAME, GAME_HOWTO)
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
JS_FILES = ["common.js", "token.js", "video.js", "image.js", "plans.js", "agents.js", "gamecost.js"]
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
            '      <p><a href="/compare/">Model vs model API cost comparisons →</a></p>\n'
            '      <ul class="not-prose mt-6 grid gap-3" style="list-style:none;padding:0">\n' + cards + '\n      </ul>\n'
            '      <h2>In other languages</h2>\n      <ul>\n' + links + '\n      </ul>\n    </section>')

def guide_links(tag, key):
    """Articles in the page language to link under the tool guide."""
    arts = {"token": [b for G in (BLOG, MISTRAL_FR, PROMPT_PL, RANK, GEM4, GPT6, API_CMP, TPW, COUNT, AISITE) for b in G if b["tag"] == tag],
            "plans": [b for G in (PRO, CMP, CHLIM) for b in G if b["tag"] == tag],
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

RANK_NAV = {"en": "AI Ranking", "ko": "AI 순위", "ja": "AIランキング", "zh-CN": "AI排行", "zh-TW": "AI排行", "es": "Ranking IA",
    "pt": "Ranking IA", "fr": "Classement IA", "de": "KI-Ranking", "it": "Classifica IA", "ru": "Рейтинг ИИ", "uk": "Рейтинг ШІ",
    "tr": "YZ Sıralaması", "ar": "تصنيف AI", "fa": "رتبه‌بندی AI", "hi": "AI रैंकिंग", "id": "Peringkat AI", "vi": "Xếp hạng AI",
    "th": "อันดับ AI", "pl": "Ranking AI", "nl": "AI-ranglijst", "bn": "AI র‍্যাঙ্কিং", "ur": "AI درجہ بندی", "fil": "Ranggo ng AI",
    "cs": "Žebříček AI", "sv": "AI-ranking", "he": "דירוג AI", "el": "Κατάταξη AI", "ro": "Clasament AI", "hu": "MI-rangsor",
    "da": "AI-rangliste", "fi": "AI-ranking", "no": "KI-rangering", "sk": "Rebríček AI", "mr": "AI क्रमवारी", "gu": "AI રેન્કિંગ",
    "kn": "AI ಶ್ರೇಯಾಂಕ", "ml": "AI റാങ്കിംഗ്", "ta": "AI தரவரிசை", "te": "AI ర్యాంకింగ్", "pa": "AI ਰੈਂਕਿੰਗ"}

GC_NAV = {"en": "Game cost", "ko": "게임 제작비", "ja": "ゲーム制作費"}
from gamecost_i18n import NAV as _GCN, EXTRA as _GCX
GC_NAV.update(_GCN)
GC_HREF = {"ko": "/ko/ai-game-cost-calculator", "ja": "/ja/ai-game-cost-calculator", **{t_: f"/{s_}/ai-game-cost-calculator" for t_, (s_, _) in _GCX.items()}}

FEEDBACK = {"en": "Ideas or a bug? Email", "ko": "개선 제안·오류 제보", "ja": "改善のご提案・不具合のご報告", "zh-CN": "改进建议・问题反馈", "zh-TW": "改進建議・問題回報",
    "es": "¿Ideas o errores? Escríbenos", "pt": "Sugestões ou erros? Escreva para", "fr": "Une idée ou un bug ? Écrivez à", "de": "Ideen oder Fehler? Schreib an",
    "it": "Idee o errori? Scrivi a", "ru": "Идеи или ошибки? Пишите на", "uk": "Ідеї чи помилки? Пишіть на", "tr": "Öneri veya hata? Yazın",
    "ar": "اقتراح أو خطأ؟ راسلنا", "fa": "پیشنهاد یا خطا؟ ایمیل بزنید", "hi": "सुझाव या गड़बड़ी? ईमेल करें", "id": "Ada saran atau bug? Email",
    "vi": "Góp ý hoặc báo lỗi", "th": "ข้อเสนอแนะหรือแจ้งปัญหา", "pl": "Pomysł lub błąd? Napisz na", "nl": "Idee of fout? Mail naar",
    "bn": "পরামর্শ বা ত্রুটি? ইমেল করুন", "ur": "تجویز یا خرابی؟ ای میل کریں", "fil": "May mungkahi o bug? Mag-email sa", "cs": "Nápad nebo chyba? Napište na",
    "sv": "Idéer eller fel? Mejla", "he": "רעיון או באג? כתבו אל", "el": "Ιδέες ή σφάλματα; Γράψτε στο", "ro": "Idei sau erori? Scrie la",
    "hu": "Ötlet vagy hiba? Írj ide", "da": "Idéer eller fejl? Skriv til", "fi": "Ideoita tai virheitä? Kirjoita", "no": "Idéer eller feil? Skriv til",
    "sk": "Nápad alebo chyba? Napíšte na", "mr": "सूचना किंवा त्रुटी? ईमेल करा", "gu": "સૂચન કે ભૂલ? ઇમેઇલ કરો", "kn": "ಸಲಹೆ ಅಥವಾ ದೋಷ? ಇಮೇಲ್ ಮಾಡಿ",
    "ml": "നിർദേശമോ പിശകോ? ഇമെയിൽ ചെയ്യൂ", "ta": "யோசனை அல்லது பிழை? மின்னஞ்சல்", "te": "సూచన లేదా లోపం? ఇమెయిల్ చేయండి", "pa": "ਸੁਝਾਅ ਜਾਂ ਗਲਤੀ? ਈਮੇਲ ਕਰੋ"}

# Search-result titles: shorter versions for pages whose full headline would be cut off (~60 chars)
SHORT_TITLES = {
    "/el/blog/tokens-ellinika-gpt": "Ελληνικά στο GPT: πόσα tokens θέλουν σε σχέση με τα αγγλικά",
    "/pa/blog/punjabi-tokens-gpt": "GPT ਵਿੱਚ ਪੰਜਾਬੀ ਟੋਕਨ: ਅੰਗਰੇਜ਼ੀ ਨਾਲ ਤੁਲਨਾ",
    "/fr/blog/souverainete-ia-tokens": "Souveraineté de l'IA : l'impact sur vos prompts",
    "/blog/llm-api-pricing-comparison": "LLM API Pricing Compared: 22 Models (GPT-6, Claude, Gemini)",
    "/fr/blog/compteur-de-tokens-pourquoi": "Pourquoi utiliser un compteur de tokens ? 5 raisons",
    "/pl/blog/jak-skrocic-prompt-po-polsku": "Jak pisać tańsze prompty po polsku? 7 wersji zmierzone",
    "/blog/write-shorter-prompts": "Write Shorter Prompts Without Losing Quality (Measured)",
    "/blog/rag-vs-long-context-cost": "RAG vs Long Context: Cost of Asking About Big Documents",
    "/blog/how-many-tokens-does-code-use": "How Many Tokens Does Code Use? Indentation & Comments",
    "/blog/chatgpt-usage-limits": "ChatGPT Usage Limits in 2026: Caps and Reset Times",
    "/uk/blog/tokeny-ukrainska-gpt": "Українська в GPT: скільки токенів порівняно з англійською",
    "/compare/performance": "AI Model Capability vs Price: Best LLM for the Money",
    "/fr/blog/mistral-chatgpt-cout-prompt-francais": "Mistral ou ChatGPT : le coût d'un prompt en français",
    "/fil/blog/token-filipino-gpt": "Filipino sa GPT: ilang token kumpara sa English",
    "/blog/codex-usage-limits": "Codex Usage Limits: 5-Hour Window, Weekly Cap, Resets",
}

def render(base, body, values):
    _u = values.get("url", "").replace(BASE, "")
    if "title" in values:
        if _u in SHORT_TITLES:
            values = dict(values, title=esc(SHORT_TITLES[_u]))
        elif values["title"].endswith(" | TokenSave") and len(html.unescape(values["title"])) > 62:
            values = dict(values, title=values["title"][: -len(" | TokenSave")])
    lab_fb = FEEDBACK.get(values.get("htmlLang", "en"), FEEDBACK["en"])
    values = dict(values, feedback=f'✉️ {esc(lab_fb)} → <a href="mailto:contact@jonhisking.com" class="text-zinc-400 hover:text-zinc-200 select-all">contact@jonhisking.com</a>')
    if "toolNav" in values:  # every page's top menu gets the capability/price ranking
        here = values.get("url", "").endswith("/compare/performance")
        lab = RANK_NAV.get(values.get("htmlLang", "en"), RANK_NAV["en"])
        href = {"ko": "/ko/compare/performance", "ja": "/ja/compare/performance"}.get(values.get("htmlLang"), "/compare/performance")
        values = dict(values, toolNav=values["toolNav"] + f'\n          <a href="{href}" class="{NAV_ON if here else NAV_OFF}"'
                      + (' aria-current="page"' if here else '') + f'>📊 {esc(lab)}</a>')
    if "toolNav" in values and values.get("htmlLang") in GC_NAV:
        gl = values["htmlLang"]
        here = values.get("url", "").endswith("ai-game-cost-calculator")
        href = GC_HREF.get(gl, "/ai-game-cost-calculator")
        values = dict(values, toolNav=values["toolNav"] + f'\n          <a href="{href}" class="{NAV_ON if here else NAV_OFF}"'
                      + (' aria-current="page"' if here else '') + f'>🎮 {esc(GC_NAV[gl])}</a>')
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

    import variants as VAR
    VAR_ALTS = "\n".join(f'  <link rel="alternate" hreflang="{l}" href="{BASE}{p}" />' for l, p in VAR.PATHS.items()) + \
        f'\n  <link rel="alternate" hreflang="x-default" href="{BASE}{VAR.PATHS["en"]}" />'
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
            if tool["key"] == "token" and tag in VAR.PATHS and "</section>" in values["guide"]:
                lk = {"en": "Using Claude? Open the <a href=\"{p}\">Claude token counter</a> with Opus, Sonnet and Haiku preselected.",
                      "ko": "Claude를 쓰시나요? Opus·Sonnet·Haiku가 바로 선택된 <a href=\"{p}\">Claude 토큰 계산기</a>를 열어 보세요.",
                      "ja": "Claude をお使いですか？ Opus・Sonnet・Haiku が最初から選ばれた<a href=\"{p}\">Claude トークンカウンター</a>をどうぞ。"}[tag].format(p=VAR.PATHS[tag])
                values["guide"] = values["guide"].replace("</section>", f"      <p>{lk}</p>\n    </section>", 1)
            folder = os.path.join(DIST, slug) if slug else DIST
            os.makedirs(folder, exist_ok=True)
            open(os.path.join(folder, tool["file"]), "w", encoding="utf-8").write(render(base, body, values))
            count += 1
            if tool["key"] == "token" and tag in VAR.PATHS:  # Claude token counter landing page
                vt = VAR.TXT[tag]
                vguide, vfaq = VAR.guide_and_faq(tag, LLM)
                vurl = BASE + VAR.PATHS[tag]
                vs = dict(s, title=vt["title"], desc=vt["desc"], h1=vt["h1"], sub=vt["sub"])
                for i in (1, 2, 3, 4):
                    vs.pop(f"q{i}", None); vs.pop(f"a{i}", None)
                for i, (q_, a_) in enumerate(vfaq, 1):
                    vs[f"q{i}"], vs[f"a{i}"] = q_, a_
                vgraph = [dict(graph[0], name=vt["h1"], url=vurl, description=vt["desc"]),
                          {"@type": "FAQPage", "inLanguage": tag, "mainEntity": [{"@type": "Question", "name": q_, "acceptedAnswer": {"@type": "Answer", "text": a_}} for q_, a_ in vfaq]},
                          {"@type": "BreadcrumbList", "itemListElement": [
                              {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": url_for(slug, TOOLS[0])},
                              {"@type": "ListItem", "position": 2, "name": vt["h1"], "item": vurl}]}]
                vvalues = dict(values)
                vvalues.update({k: esc(v) for k, v in vs.items()})
                vvalues.update(url=vurl, hreflang=VAR_ALTS, guide=vguide, faq=faq_html(vs),
                               ldjson=js({"@context": "https://schema.org", "@graph": vgraph}),
                               tjson=js(dict(runtime, defaultProvider="claude", defaultModel="claude-sonnet-5-5")))
                vfile = os.path.join(DIST, VAR.PATHS[tag].lstrip("/") + ".html")
                os.makedirs(os.path.dirname(vfile), exist_ok=True)
                open(vfile, "w", encoding="utf-8").write(render(base, body, vvalues))

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


    # Model-vs-model comparison pages (/compare/...), English only, prices from llm_prices.json
    import compare as CMPG
    cmp_pages, cmp_hub = CMPG.build_all(LLM)
    import charts as CH
    import perf as PERF
    PERF_LANGS = ["en", "ko", "ja"]
    PERF_ALTS = "\n".join(f'  <link rel="alternate" hreflang="{l}" href="{BASE}{PERF.PATH[l]}" />' for l in PERF_LANGS) + \
        f'\n  <link rel="alternate" hreflang="x-default" href="{BASE}{PERF.PATH["en"]}" />'
    IMAGES = {}  # page path -> [(image url, caption)] for the image sitemap
    def write_img(src, svg):
        fp = os.path.join(DIST, src.lstrip("/"))
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, "w", encoding="utf-8").write(svg)
    for cp in cmp_pages:
        write_img(*cp["chart"])
        IMAGES[cp["path"]] = [(BASE + cp["chart"][0], cp["image_caption"])]
        for src_, svg_, cap_ in cp.get("extra_images", []):
            write_img(src_, svg_)
            IMAGES[cp["path"]].append((BASE + src_, cap_))
    for cp in [cmp_hub] + cmp_pages:
        url = BASE + cp["path"]
        ld = {"@context": "https://schema.org", "@graph": [
            {"@type": "WebPage", "name": cp["title"], "url": url, "description": cp["desc"], "dateModified": LLM.get("checked", LASTMOD),
             **({"primaryImageOfPage": {"@type": "ImageObject", "url": BASE + cp["chart"][0], "caption": cp["image_caption"]}} if "chart" in cp else {})},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": BASE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Compare", "item": BASE + "/compare/"},
                *([{"@type": "ListItem", "position": 3, "name": cp["title"], "item": url}] if cp is not cmp_hub else [])]}]
            + ([cp["faq_ld"]] if "faq_ld" in cp else [])}
        values = dict(
            htmlLang="en", dir="ltr", url=url, ogLocale="en_US", ogImage=f"{BASE}/og-token.jpg",
            title=esc(cp["title"] if cp is cmp_hub else cp["title"] + " | TokenSave"), desc=esc(cp["desc"]), lang=esc(S["en"]["lang"]),
            homeUrl="/", hreflang=PERF_ALTS if cp["path"] == "/compare/performance" else "", langOptions=en_opts, langAll=en_all, toolNav=en_nav, ver=ver, adsHead=extras, faq="", guide="",
            f1="", f2="", fAbout=esc(SITE["en"]["fAbout"]), fPrivacy=esc(SITE["en"]["fPrivacy"]),
            ldjson=js(ld), tjson=js({"static": True}),
            scriptTag=f'<script type="module" src="/common.js?v={ver}"></script>',
        )
        fpath = os.path.join(DIST, "compare", "index.html") if cp is cmp_hub else os.path.join(DIST, cp["path"].lstrip("/") + ".html")
        os.makedirs(os.path.dirname(fpath), exist_ok=True)
        open(fpath, "w", encoding="utf-8").write(render(base, cp["body"], values))

    # Localized capability vs price pages (/ko/compare/performance, /ja/compare/performance)
    tag_slug_ = {tag: slug for slug, tag, *_ in LANGS}
    tag_og_ = {tag: og for slug, tag, _, og, _ in LANGS}
    for pl in PERF_LANGS[1:]:
        pp, _ = PERF.build_page(CMPG.load_models(LLM), LLM, pl)
        write_img(*pp["chart"])
        IMAGES[pp["path"]] = [(BASE + pp["chart"][0], pp["image_caption"])]
        for src_, svg_, cap_ in pp["extra_images"]:
            write_img(src_, svg_); IMAGES[pp["path"]].append((BASE + src_, cap_))
        slug = tag_slug_[pl]
        url = BASE + pp["path"]
        nav = "\n".join(f'          <a href="{path_for(slug, t)}" class="{NAV_OFF}">{esc(NAV[pl][t["nav"]])}</a>' for t in TOOLS)
        opts, opts_all = lang_menu(slug, pl, lambda sl: path_for(sl, TOOLS[0]))
        ld = {"@context": "https://schema.org", "@graph": [
            {"@type": "WebPage", "name": pp["title"], "url": url, "description": pp["desc"], "inLanguage": pl, "dateModified": LLM.get("checked", LASTMOD),
             "primaryImageOfPage": {"@type": "ImageObject", "url": BASE + pp["chart"][0], "caption": pp["image_caption"]}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": BASE + path_for(slug, TOOLS[0])},
                {"@type": "ListItem", "position": 2, "name": pp["title"], "item": url}]}, pp["faq_ld"]]}
        values = dict(
            htmlLang=pl, dir="ltr", url=url, ogLocale=tag_og_[pl], ogImage=f"{BASE}/og-token.jpg",
            title=esc(pp["title"] + " | TokenSave"), desc=esc(pp["desc"]), lang=esc(S[pl]["lang"]),
            homeUrl=path_for(slug, TOOLS[0]), hreflang=PERF_ALTS, langOptions=opts, langAll=opts_all, toolNav=nav, ver=ver, adsHead=extras,
            faq="", guide="", f1="", f2="", fAbout=esc(SITE[pl]["fAbout"]), fPrivacy=esc(SITE[pl]["fPrivacy"]),
            ldjson=js(ld), tjson=js({"static": True}), scriptTag=f'<script type="module" src="/common.js?v={ver}"></script>',
        )
        fp = os.path.join(DIST, pp["path"].lstrip("/") + ".html")
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, "w", encoding="utf-8").write(render(base, pp["body"], values))

    # AI game cost estimator (/ai-game-cost-calculator + ko/ja)
    import gamecost as GC
    GC_ALTS = "\n".join(f'  <link rel="alternate" hreflang="{l}" href="{BASE}{p}" />' for l, p in GC.PATH.items()) + \
        f'\n  <link rel="alternate" hreflang="x-default" href="{BASE}{GC.PATH["en"]}" />'
    gc_prices = {k: {"in": v["in"], "out": v["out"]} for k, v in LLM["models"].items()}
    for gl in GC.PATH:
        gp = GC.build_page(gl, LLM)
        slug = tag_slug_[gl]
        url = BASE + gp["path"]
        nav = "\n".join(f'          <a href="{path_for(slug, t)}" class="{NAV_OFF}">{esc(NAV[gl][t["nav"]])}</a>' for t in TOOLS)
        opts, opts_all = lang_menu(slug, gl, lambda sl: path_for(sl, TOOLS[0]))
        ld = {"@context": "https://schema.org", "@graph": [
            {"@type": "WebApplication", "name": gp["h1"], "url": url, "inLanguage": gl, "applicationCategory": "DeveloperApplication",
             "operatingSystem": "Any", "isAccessibleForFree": True, "description": gp["desc"], "dateModified": GC.CHECKED,
             "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
             "publisher": {"@type": "Organization", "name": "TokenSave", "url": BASE + "/"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": BASE + path_for(slug, TOOLS[0])},
                {"@type": "ListItem", "position": 2, "name": gp["h1"], "item": url}]}, gp["faq_ld"]]}
        values = dict(
            htmlLang=gl, dir="ltr", url=url, ogLocale=tag_og_[gl], ogImage=f"{BASE}/og-token.jpg",
            title=esc(gp["title"]), desc=esc(gp["desc"]), lang=esc(S[gl]["lang"]),
            homeUrl=path_for(slug, TOOLS[0]), hreflang=GC_ALTS, langOptions=opts, langAll=opts_all, toolNav=nav, ver=ver, adsHead=extras,
            faq="", guide="", f1="", f2="", fAbout=esc(SITE[gl]["fAbout"]), fPrivacy=esc(SITE[gl]["fPrivacy"]),
            ldjson=js(ld), tjson=js({"static": True, "gc": gp["gc"], "prices": gc_prices, "modelNames": gp["models"]}),
            scriptTag=f'<script type="module" src="/common.js?v={ver}"></script>\n  <script type="module" src="/gamecost.js?v={ver}"></script>',
        )
        fp = os.path.join(DIST, gp["path"].lstrip("/") + ".html")
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, "w", encoding="utf-8").write(render(base, gp["body"], values))

    # Price chart for the API-pricing articles (one chart per highlight set, localized alt/caption)
    _cm = CMPG.load_models(LLM)
    _ids = ["claude-fable-5-1", "gpt-6-astra", "claude-opus-5-5", "gemini-4-argon", "gemini-3-1-pro", "gpt-6-sol",
            "claude-sonnet-5-5", "grok-4-7", "deepseek-v4-pro", "kimi-k3", "claude-haiku-4-5", "gemini-3-8-flash",
            "gpt-6-luna", "deepseek-v4-flash"]
    _pm = sorted((_cm[i] for i in _ids if i in _cm), key=lambda m: (-m["out"], -m["inp"]))
    PRICE_CAP = {
        "en": ("Bar chart of API prices per 1M tokens, input and output, for {n} AI models{hl}", "API price per 1M tokens{hl} vs other major models (USD, checked {d})."),
        "ko": ("주요 AI 모델 {n}개의 100만 토큰당 입력·출력 API 가격 막대그래프{hl}", "100만 토큰당 API 가격{hl} (달러, {d} 기준)"),
        "ja": ("主要AIモデル{n}種の100万トークンあたり入力・出力API料金の棒グラフ{hl}", "100万トークンあたりのAPI料金{hl}（ドル、{d}時点）"),
        "es": ("Gráfico de barras del precio de la API por 1M de tokens, entrada y salida, de {n} modelos de IA{hl}", "Precio de la API por 1M de tokens{hl} (USD, revisado el {d})."),
    }
    PRICE_HL = {
        "gem4": (["gemini-4-argon"], "/img/gemini-4-argon-api-price-chart.svg",
                 {"en": " (Gemini 4 Argon highlighted)", "ko": ": 제미나이 4 아르곤 강조", "ja": "：Gemini 4 Argon を強調", "es": " (Gemini 4 Argon resaltado)"}),
        "gpt6": (["gpt-6-astra", "gpt-6-sol", "gpt-6-luna"], "/img/gpt-6-api-price-chart.svg",
                 {"en": " (GPT-6 Astra, Sol and Luna highlighted)", "ko": ": GPT-6 Astra·Sol·Luna 강조", "ja": "：GPT-6 Astra・Sol・Luna を強調", "es": " (GPT-6 resaltado)"}),
        "api": ([], "/img/llm-api-price-chart.svg", {}),
    }
    PRICE_SVG = {}
    for key, (hl, src, _) in PRICE_HL.items():
        PRICE_SVG[key] = CH.price_chart(_pm, set(hl), LLM.get("checked", ""))
        write_img(src, PRICE_SVG[key])
    def price_fig(key, tag):
        hl, src, names = PRICE_HL[key]
        alt, cap = PRICE_CAP.get(tag, PRICE_CAP["en"])
        h = names.get(tag, names.get("en", ""))
        w_, h_ = CH.size_of(PRICE_SVG[key])
        return CH.figure(src, alt.format(n=len(_pm), hl=h), cap.format(hl=h, d=LLM.get("checked", "")), w_, h_), (BASE + src, cap.format(hl=h, d=LLM.get("checked", "")))
    PRICE_GROUP = {id(GEM4): "gem4", id(GPT6): "gpt6", id(API_CMP): "api"}

    # Related articles: every article links to up to 5 newer/other articles in the same language
    ALL_ART = [b for G in (BLOG, PRO, MISTRAL_FR, PROMPT_PL, *MULTI) for b in G] + list(GUIDES)
    REL_H = {"en": "More articles", "ko": "다른 글", "ja": "関連記事", "es": "Más artículos", "fr": "Autres articles",
             "pl": "Więcej artykułów", "de": "Weitere Artikel", "pt": "Mais artigos", "it": "Altri articoli",
             "uk": "Інші статті", "ru": "Другие статьи", "zh-CN": "更多文章", "zh-TW": "更多文章"}
    def related_html(b):
        ring = sorted((x for x in ALL_ART if x["tag"] == b["tag"]), key=lambda x: (x.get("date", BLOG_DATE), x["path"]), reverse=True)
        if len(ring) < 2:
            return ""
        i = next(k for k, x in enumerate(ring) if x["path"] == b["path"])
        # the newest two, plus the next ones around the ring, so every article gets inbound links
        pick = [x for x in ring[:2] if x["path"] != b["path"]]
        for k in range(1, len(ring)):
            x = ring[(i + k) % len(ring)]
            if len(pick) >= 5: break
            if x["path"] != b["path"] and x not in pick: pick.append(x)
        items = "".join(f'<li><a href="{x["path"]}">{esc(x["title"])}</a></li>' for x in pick)
        return f'\n        <h2>{esc(REL_H.get(b["tag"], "More articles"))}</h2>\n        <ul>{items}</ul>'

    # Articles (/<slug>/blog/...): each group is one article in several languages, linked with hreflang
    plans_tool = next(t for t in TOOLS if t["key"] == "plans")
    tool_by_key = {t["key"]: t for t in TOOLS}
    og_by_key = {"video": "og-video.jpg", "image": "og-image.jpg"}
    for GROUP, gimg, gtool in [(BLOG, "blog-language-tax-chart-v4.png", TOOLS[0]), (PRO, "blog-chatgpt-pro-tiers.png", plans_tool), (MISTRAL_FR, "blog-mistral-francais.png", TOOLS[0]), (PROMPT_PL, "blog-prompt-polski.png", TOOLS[0])] + [
            ([g], og_by_key.get(g["tool"], "og-token.jpg"), tool_by_key[g["tool"]]) for g in GUIDES] + [
            (G, "og-token.jpg", tool_by_key["agents"]) for G in CC] + [(CMP, "og-token.jpg", plans_tool), (GPT6, "og-token.jpg", TOOLS[0]), (GEM4, "og-token.jpg", TOOLS[0]), (RANK, "og-token.jpg", TOOLS[0]), (API_CMP, "og-token.jpg", TOOLS[0]), (TPW, "og-token.jpg", TOOLS[0]), (COUNT, "og-token.jpg", TOOLS[0]), (CHLIM, "og-token.jpg", plans_tool), (AISITE, "og-token.jpg", TOOLS[0]), (GAME, "og-token.jpg", {"page": "ai-game-cost-calculator"}), (GAME_HOWTO, "og-token.jpg", {"page": "ai-game-cost-calculator"})]:
      blog_en = next((b for b in GROUP if b["tag"] == "en"), None)
      def _alts_for(me):  # hreflang: one URL per language, and a same-language sibling is never this page's alternate
          grp = [x for x in GROUP if x["tag"] != me["tag"] or x is me]
          xd = blog_en if blog_en in grp else None
          return "\n".join(f'  <link rel="alternate" hreflang="{x["tag"]}" href="{BASE}{x["path"]}" />' for x in grp) + (
              f'\n  <link rel="alternate" hreflang="x-default" href="{BASE}{xd["path"]}" />' if xd else "")
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
          def _fix_chart(m):  # charts generated into /img: real size, full width
              fp = os.path.join(DIST, m.group(2).lstrip("/"))
              if not os.path.exists(fp):
                  return m.group(0)
              w_, h_ = CH.size_of(open(fp, encoding="utf-8").read())
              tag_ = re.sub(r'width="\d+" height="\d+"', f'width="{w_}" height="{h_}"', m.group(0))
              return tag_.replace("<img ", '<img class="chart" ', 1)
          article = re.sub(r'<img[^>]*?alt="([^"]*)"[^>]*?src="(/img/[^"]+\.svg)"[^>]*>', _fix_chart, article)
          for _alt, _src in re.findall(r'<img[^>]*?alt="([^"]*)"[^>]*?src="(/[^"]+)"', article):
              IMAGES.setdefault(b["path"], []).append((BASE + _src, _alt))
          if id(GROUP) in PRICE_GROUP:
              fig, img = price_fig(PRICE_GROUP[id(GROUP)], tag)
              cut = article.find("<h2")
              article = article[:cut] + fig + "\n" + article[cut:] if cut >= 0 else article + fig
              IMAGES.setdefault(b["path"], []).append(img)
          body = f"""    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
        <h1 class="text-2xl sm:text-3xl font-extrabold text-white leading-snug" style="overflow-wrap:anywhere">{esc(b["title"])}</h1>
        <p class="mt-2 text-xs text-zinc-500">{esc(b["byline"])}</p>
  {article}{related_html(b)}
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
              homeUrl=tool_home, hreflang=_alts_for(b), langOptions=opts, langAll=opts_all, toolNav=nav, ver=ver, adsHead=extras, faq="", guide="",
              f1="", f2="", fAbout=esc(SITE[tag]["fAbout"]), fPrivacy=esc(SITE[tag]["fPrivacy"]),
              ldjson=js(ld), tjson=js({"static": True}),
              scriptTag=f'<script type="module" src="/common.js?v={ver}"></script>',
          )
          folder = os.path.join(DIST, slug, "blog") if slug else os.path.join(DIST, "blog")
          os.makedirs(folder, exist_ok=True)
          open(os.path.join(folder, b["path"].rsplit("/", 1)[1] + ".html"), "w", encoding="utf-8").write(render(base, body, values))

    # Directory badges, English home page footer only (listing verification)
    BADGES = ('<p class="pt-3 flex flex-wrap items-center justify-center gap-3"><a href="https://verifieddr.com/website/tokensave-app" target="_blank">'
              '<img src="https://verifieddr.com/badge/tokensave-app.svg?metric=truedr" alt="Verified DR - Verified Domain Rating for tokensave.app" '
              'width="220" height="68" loading="lazy" /></a>'
              '<a href="https://easylaunch.dev/ai/tokensave" target="_blank" rel="noopener">'
              '<img src="https://easylaunch.dev/badge/easylaunch-badge-dark.svg" alt="Featured on EasyLaunch" width="188" height="56" loading="lazy" /></a>'
              '<a href="https://uno.directory" target="_blank" rel="noopener">'
              '<img src="https://uno.directory/uno-directory.svg" alt="Listed on Uno Directory" width="120" height="30" loading="lazy" /></a>'
              '<a href="https://findly.tools/tokensave?utm_source=tokensave" target="_blank" rel="noopener noreferrer">'
              '<img src="https://findly.tools/badges/findly-tools-badge-dark.svg" alt="Featured on Findly.tools" width="175" height="55" loading="lazy" /></a>'
              '<a href="https://neeed.directory/products/tokensave?utm_source=tokensave" target="_blank">'
              '<img src="https://neeed.directory/badges/neeed-badge-dark.svg" alt="Featured on neeed.directory" width="139" height="20" loading="lazy" /></a></p>')
    _home = os.path.join(DIST, "index.html")
    _h = open(_home, encoding="utf-8").read()
    assert _h.count("    </footer>") == 1
    open(_home, "w", encoding="utf-8").write(_h.replace("    </footer>", "      " + BADGES + "\n    </footer>"))

    for f in JS_FILES:
        shutil.copy(os.path.join(SRC, f), os.path.join(DIST, f))
    for f in os.listdir(os.path.join(SRC, "static")):
        shutil.copy(os.path.join(SRC, "static", f), os.path.join(DIST, f))
    open(os.path.join(DIST, "CNAME"), "w").write("tokensave.app\n")
    # AI training crawlers bring no visitors (and no ad views), so they are blocked; search/answer bots that link back stay allowed
    TRAIN_BOTS = ["GPTBot", "ClaudeBot", "anthropic-ai", "CCBot", "Google-Extended", "Applebot-Extended", "Bytespider", "meta-externalagent", "cohere-training-data-crawler"]
    open(os.path.join(DIST, "robots.txt"), "w").write("User-agent: *\nAllow: /\n\nUser-agent: Yeti\nAllow: /\n\n" + "".join(f"User-agent: {b_}\nDisallow: /\n\n" for b_ in TRAIN_BOTS) + f"Sitemap: {BASE}/sitemap.xml\n")
    if ADSENSE_PUB:
        open(os.path.join(DIST, "ads.txt"), "w").write(
            f"google.com, {ADSENSE_PUB.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")

    def img_tags(p):
        return "".join(f"\n    <image:image>\n      <image:loc>{u}</image:loc>\n    </image:image>" for u, _ in IMAGES.get(p, []))

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
      b_en = next((b for b in GROUP if b["tag"] == "en"), None)
      for b in GROUP:
        grp = [x for x in GROUP if x["tag"] != b["tag"] or x is b]  # same-language siblings are separate articles, not alternates
        b_alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{x["tag"]}" href="{BASE}{x["path"]}"/>' for x in grp)
        if b_en and b_en in grp:
            b_alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{b_en["path"]}"/>'
        entries.append(f"\n  <url>\n    <loc>{BASE}{b['path']}</loc>\n    <lastmod>{b.get('date', BLOG_DATE)}</lastmod>{b_alts}{img_tags(b['path'])}\n  </url>")
    perf_x = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{BASE}{PERF.PATH[l]}"/>' for l in PERF_LANGS)
    for cp in [cmp_hub] + cmp_pages:
        alts_ = perf_x if cp["path"] == "/compare/performance" else ""
        entries.append(f"\n  <url>\n    <loc>{BASE}{cp['path']}</loc>\n    <lastmod>{LLM.get('checked', LASTMOD)}</lastmod>{alts_}{img_tags(cp['path'])}\n  </url>")
    var_x = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{BASE}{p}"/>' for l, p in VAR.PATHS.items())
    for p_ in VAR.PATHS.values():
        entries.append(f"\n  <url>\n    <loc>{BASE}{p_}</loc>\n    <lastmod>{LLM.get('checked', LASTMOD)}</lastmod>{var_x}\n  </url>")
    for pl in PERF_LANGS[1:]:
        entries.append(f"\n  <url>\n    <loc>{BASE}{PERF.PATH[pl]}</loc>\n    <lastmod>{LLM.get('checked', LASTMOD)}</lastmod>{perf_x}{img_tags(PERF.PATH[pl])}\n  </url>")
    gc_x = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{BASE}{p}"/>' for l, p in GC.PATH.items()) + \
        f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{GC.PATH["en"]}"/>'
    for p_ in GC.PATH.values():
        entries.append(f"\n  <url>\n    <loc>{BASE}{p_}</loc>\n    <lastmod>{GC.CHECKED}</lastmod>{gc_x}\n  </url>")
    open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">'
        + "".join(entries) + "\n</urlset>\n"
    )
    print("built", count, "tool pages +", len(PAGES), "site pages +", len(BLOG) + len(PRO) + len(MISTRAL_FR) + len(PROMPT_PL) + len(GUIDES) + sum(map(len, MULTI)), "articles +", len(cmp_pages) + 1, "compare pages ->", DIST)

if __name__ == "__main__":
    build()
