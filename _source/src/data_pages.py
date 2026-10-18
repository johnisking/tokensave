"""/data/ pages: TokenSave's own measurements as citable datasets (table, CSV/JSON download,
method, limitations, suggested citation, embed code, schema.org Dataset).
Goal: other writers can quote a number and link the source in one step (2026-10-16 citation strategy)."""
import csv, io, json, os
from html import escape as esc

BASE = "https://tokensave.app"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LICENSE = "https://creativecommons.org/licenses/by/4.0/"

LANG_PATH = "/data/token-cost-by-language"
LANG_MEASURED = "2026-09-30"
LANG_VERIFIED = "2026-10-16"
LANG_CHART = "/blog-language-tax-chart-v5.png"
LANG_DOI = "10.5281/zenodo.23427148"  # concept DOI (always resolves to the latest Zenodo version)
LANG_MIRRORS = [("Zenodo", "https://zenodo.org/records/23427149"),
                ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/token-cost-by-language"),
                ("Kaggle", "https://www.kaggle.com/datasets/johnisking/token-cost-by-language-41-languages-gpt")]
LANG_TITLE = "Token cost by language: 41 languages measured on GPT tokenizers"
LANG_DESC = ("Dataset: the same prompt in 41 languages counted with OpenAI's o200k_base and cl100k_base tokenizers. "
             "From +3% (Simplified Chinese) to +144% (Punjabi) more tokens than English. Free CSV, CC BY 4.0.")


def _lang_rows():
    d = json.load(open(os.path.join(ROOT, "blog_data", "langdata.json"), encoding="utf-8"))
    en = d["en"]
    rows = []
    for code, v in d.items():
        if code.startswith("_"):
            continue
        rows.append(dict(code=code, name=v["name"], o=v["o"], c=v["c"],
                         po=round((v["o"] / en["o"] - 1) * 100), pc=round((v["c"] / en["c"] - 1) * 100),
                         prompt=v["prompt"]))
    rows.sort(key=lambda r: (r["o"], r["c"], r["name"]))
    return rows


def _nm(n):
    """'Chinese (Simplified)' -> 'Simplified Chinese' for running text."""
    return f"{n.split(' (')[1].rstrip(')')} {n.split(' (')[0]}" if " (" in n else n


def _pct(p):
    return "±0%" if p == 0 else f"+{p}%" if p > 0 else f"{p}%"


def write_files(dist):
    """CSV and JSON downloads next to the page."""
    _write_lang_files(dist)
    write_multi_files(dist)
    write_fmt_files(dist)
    write_img_files(dist)
    write_code_files(dist)
    write_pdf_files(dist)
    write_eff_files(dist)
    write_agt_files(dist)
    write_ags_files(dist)
    write_agl_files(dist)
    write_amd_files(dist)
    write_tl_files(dist)


def _write_lang_files(dist):
    rows = _lang_rows()
    os.makedirs(os.path.join(dist, "data"), exist_ok=True)
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["language_code", "language", "o200k_tokens", "o200k_vs_english_pct", "cl100k_tokens", "cl100k_vs_english_pct", "prompt"])
    for r in rows:
        w.writerow([r["code"], r["name"], r["o"], r["po"], r["c"], r["pc"], r["prompt"]])
    open(os.path.join(dist, "data", "token-cost-by-language.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=LANG_TITLE, url=BASE + LANG_PATH, license="CC BY 4.0", measured=LANG_MEASURED, verified=LANG_VERIFIED,
                tokenizers=["o200k_base (GPT-4o and later)", "cl100k_base (GPT-4, GPT-3.5)"],
                citation=citation_text(), rows=[{k: r[k] for k in ("code", "name", "o", "po", "c", "pc", "prompt")} for r in rows])
    open(os.path.join(dist, "data", "token-cost-by-language.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def citation_text():
    return f"TokenSave (2026). {LANG_TITLE} [Data set]. Zenodo. https://doi.org/{LANG_DOI}"


def lang_ld():
    rows = _lang_rows()
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "Dataset", "name": LANG_TITLE, "description": LANG_DESC, "url": BASE + LANG_PATH,
         "identifier": f"https://doi.org/{LANG_DOI}", "sameAs": [u for _, u in LANG_MIRRORS],
         "license": LICENSE, "isAccessibleForFree": True,
         "creator": {"@type": "Organization", "name": "TokenSave", "url": BASE + "/"},
         "datePublished": LANG_MEASURED, "dateModified": LANG_VERIFIED,
         "keywords": ["tokenizer", "tokens per language", "LLM cost", "o200k_base", "cl100k_base", "multilingual"],
         "variableMeasured": ["tokens (o200k_base)", "tokens (cl100k_base)", "difference vs English (%)"],
         "measurementTechnique": "Same customer-support prompt translated into 41 languages, counted with tiktoken",
         "spatialCoverage": f"{len(rows)} languages",
         "image": BASE + LANG_CHART,
         "distribution": [
             {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": BASE + "/data/token-cost-by-language.csv"},
             {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": BASE + "/data/token-cost-by-language.json"}]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Data", "item": BASE + "/data/"},
            {"@type": "ListItem", "position": 3, "name": LANG_TITLE, "item": BASE + LANG_PATH}]}]}


COPY_JS = ("<script>document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',()=>{"
           "const t=document.getElementById(b.dataset.copy);const v=t.value!==undefined?t.value:t.textContent;"
           "const done=()=>{const o=b.textContent;b.textContent='Copied';setTimeout(()=>b.textContent=o,1500)};"
           "(navigator.clipboard?navigator.clipboard.writeText(v).then(done):Promise.reject()).catch(()=>{"
           "const r=document.createRange();r.selectNodeContents(t);const s=getSelection();s.removeAllRanges();s.addRange(r)})}))</script>")

BTN = ('class="not-prose text-xs font-semibold rounded-md border border-violet-500/40 bg-violet-500/10 '
       'px-2.5 py-1 text-violet-200 hover:bg-violet-500/20"')


def lang_html():
    rows = _lang_rows()
    en = next(r for r in rows if r["code"] == "en")
    hi = rows[-1]
    lo = [r for r in rows if r["code"] != "en"][0]
    by = {r["code"]: r for r in rows}
    trs = "\n".join(
        f'          <tr><td>{esc(r["name"])}</td><td class="text-right tabular-nums">{r["o"]}</td>'
        f'<td class="text-right tabular-nums">{_pct(r["po"])}</td><td class="text-right tabular-nums">{r["c"]}</td>'
        f'<td class="text-right tabular-nums">{_pct(r["pc"])}</td></tr>' for r in rows)
    embed = (f'<a href="{BASE}{LANG_PATH}"><img src="{BASE}{LANG_CHART}" '
             f'alt="Extra GPT tokens per language vs English, 41 languages (TokenSave)" width="1200" loading="lazy"></a>\n'
             f'<p>Source: <a href="{BASE}{LANG_PATH}">TokenSave, token cost by language</a> (CC BY 4.0)</p>')
    return f'''    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <p class="not-prose text-xs font-semibold uppercase tracking-wider text-violet-300"><a href="/data/" class="no-underline" style="text-decoration:none">TokenSave Data</a> · Dataset</p>
      <h1 class="text-3xl font-extrabold text-white">How many more tokens each language needs than English</h1>
      <p class="mt-3 text-lg text-zinc-200"><strong>The same prompt needs {en["o"]} GPT tokens in English and {lo["o"]}–{hi["o"]} tokens in {len(rows) - 1} other languages: from {_pct(lo["po"])} ({esc(_nm(lo["name"]))}) to {_pct(hi["po"])} ({esc(_nm(hi["name"]))}).</strong> Korean needs {_pct(by["ko"]["po"])}, Japanese {_pct(by["ja"]["po"])}, Spanish {_pct(by["es"]["po"])} and German {_pct(by["de"]["po"])}.</p>
      <p class="text-sm text-zinc-400">Tokenizer: o200k_base (GPT-4o and later), with cl100k_base (GPT-4, GPT-3.5) for comparison · Measured {LANG_MEASURED} · Counts re-verified {LANG_VERIFIED} · License <a href="{LICENSE}">CC BY 4.0</a></p>
      <p class="text-sm text-zinc-400">DOI <a href="https://doi.org/{LANG_DOI}">{LANG_DOI}</a> · Also on {" · ".join(f'<a href="{u}">{n}</a>' for n, u in LANG_MIRRORS[1:])}</p>
      <div class="not-prose flex flex-wrap gap-2 my-4">
        <a href="/data/token-cost-by-language.csv" {BTN} style="text-decoration:none">⬇ CSV</a>
        <a href="/data/token-cost-by-language.json" {BTN} style="text-decoration:none">⬇ JSON</a>
        <a href="#cite" {BTN} style="text-decoration:none">How to cite</a>
      </div>
      <img src="{LANG_CHART}" alt="Extra GPT tokens per language compared with English, 41 languages" width="1200" loading="lazy">
      <h2>Why it matters</h2>
      <p>API prices are per token, so a language that needs {_pct(by["ko"]["po"])} more tokens pays about {_pct(by["ko"]["po"])} more for the same request. Usage limits on ChatGPT, Claude and Gemini plans are also counted in tokens, so the same gap shows up as messages running out sooner. If the model answers in the same language, the output costs more too, and output tokens are usually priced 300–400% higher than input.</p>
      <h2>All {len(rows)} languages</h2>
      <div class="overflow-x-auto">
        <table>
          <thead><tr><th>Language</th><th class="text-right">o200k tokens</th><th class="text-right">vs English</th><th class="text-right">cl100k tokens</th><th class="text-right">vs English</th></tr></thead>
          <tbody>
{trs}
          </tbody>
        </table>
      </div>
      <p class="text-sm text-zinc-400">The newer o200k tokenizer narrowed the gap for most languages; the older cl100k column shows how much. For example, Korean went from {_pct(by["ko"]["pc"])} to {_pct(by["ko"]["po"])} and Hindi from {_pct(by["hi"]["pc"])} to {_pct(by["hi"]["po"])}.</p>
      <h2>Method</h2>
      <ul>
        <li>One everyday English prompt: <em>“{esc(en["prompt"])}”</em></li>
        <li>Translated into each language (machine translation as a first draft, then checked) and counted with OpenAI's <a href="https://github.com/openai/tiktoken">tiktoken</a> using <code>o200k_base</code> and <code>cl100k_base</code>.</li>
        <li>“vs English” = tokens in the language ÷ English tokens − 1, rounded to whole percent. Every translated prompt is in the CSV, so the counts can be reproduced.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>One prompt. With other text the ratios move by roughly ±10–20 percentage points; the ranking is more stable than the exact numbers.</li>
        <li>OpenAI tokenizers only. Claude and Gemini use their own tokenizers, so their gaps differ (see <a href="/ko/blog/claude-hangugeo-token">our Claude Korean test</a>).</li>
        <li>Input text only. It does not measure how long the model's answer would be in each language.</li>
      </ul>
      <h2 id="cite">How to cite</h2>
      <p>Free to use, quote and republish with attribution under <a href="{LICENSE}">CC BY 4.0</a>. Please link to this page or the DOI.</p>
      <div class="not-prose bg-zinc-950/70 border border-zinc-800 rounded-xl p-4">
        <p id="cite-text" class="text-sm text-zinc-200 break-words">{esc(citation_text())}</p>
        <div class="mt-3"><button type="button" data-copy="cite-text" {BTN}>Copy citation</button></div>
      </div>
      <h3>Embed the chart</h3>
      <div class="not-prose">
        <textarea id="embed-code" readonly rows="4" class="w-full text-xs font-mono bg-zinc-950/70 border border-zinc-800 rounded-xl p-3 text-zinc-300">{esc(embed)}</textarea>
        <div class="mt-2"><button type="button" data-copy="embed-code" {BTN}>Copy embed code</button></div>
      </div>
      <h2>Related</h2>
      <ul>
        <li><a href="/blog/token-cost-by-language">Full write-up: why some languages cost more and how to save</a></li>
        <li><a href="/languages">Per-language articles (41 languages)</a></li>
        <li><a href="/">Count tokens for your own text</a> · <a href="/tokens-to-words">Tokens to words converter</a></li>
      </ul>
      <p class="text-sm text-zinc-400">Questions or corrections: <a href="mailto:contact@jonhisking.com">contact@jonhisking.com</a></p>
    </article>
{COPY_JS}'''


def hub_html():
    return f'''    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <h1 class="text-3xl font-extrabold text-white">TokenSave Data</h1>
      <p class="mt-3">Measurements we ran ourselves on AI tokens and costs, published as open datasets. Each page has the headline numbers, the full table, a CSV download, the method and its limits, and a ready-made citation. Everything is free to reuse under <a href="{LICENSE}">CC BY 4.0</a> with a link back.</p>
      <ul class="not-prose mt-6 space-y-3">
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{LANG_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(LANG_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">The same prompt in 41 languages: +3% to +144% more GPT tokens than English. CSV · updated {LANG_VERIFIED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{MULTI_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(MULTI_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">The same prompt on Claude 5.5, Claude Haiku 4.5, Gemini and GPT: Korean needs 89 Claude tokens vs 49 on GPT. CSV · measured {MULTI_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{FMT_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(FMT_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">The same table in 8 formats on 4 tokenizers: CSV needs about two thirds fewer tokens than indented JSON. CSV · measured {FMT_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{IMG_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(IMG_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">One image at 10 resolutions on Claude, Gemini and GPT: Gemini charges a flat ~1,100 tokens, GPT-6 Astra up to 14,364. CSV · measured {IMG_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{CODE_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(CODE_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">The same two programs in 10 programming languages: C needs 90% more GPT tokens than Python. CSV · measured {CODE_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{PDF_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(PDF_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">PDF pages on Claude and Gemini vs pasting the text: Gemini charges a flat 560 tokens per page. CSV · measured {PDF_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{EFF_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(EFF_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">One coding task at every Claude effort level: $0.56 at medium, $5.25 at max. CSV · measured {EFF_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{AGT_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(AGT_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">Startup tokens, MCP tool overhead and the same coding task: Codex used about half the tokens of Claude Code. CSV · measured {AGT_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{AGS_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(AGS_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">Four kinds of question with web search on: tokens, searches, time and the sites seen and cited. CSV · measured {AGS_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{AGL_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(AGL_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">Claude Code and Codex in 5 languages: English searches for AI topics, local-language searches for Seoul, Tokyo, Madrid and Kyiv. CSV · measured {AGL_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{AMD_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(AMD_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">A 50 KB CLAUDE.md adds about 16,000 tokens to every request; Codex reads only the first 32 KiB of AGENTS.md. CSV · measured {AMD_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{TL_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(TL_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">The same coding task in 5 prompt languages: almost the same tokens, but the game and its comments follow your language. CSV · measured {TL_MEASURED}</span></a></li>
      </ul>
      <p class="mt-6 text-sm text-zinc-400">More datasets are on the way. Using our data in an article or paper? We'd love to hear about it: <a href="mailto:contact@jonhisking.com">contact@jonhisking.com</a></p>
    </article>'''


HUB_TITLE = "TokenSave Data: open AI token and cost measurements"
HUB_DESC = "Datasets from TokenSave's own measurements of AI tokens and costs, with CSV downloads and citations (CC BY 4.0)."


def hub_ld():
    return {"@context": "https://schema.org", "@type": "CollectionPage", "name": HUB_TITLE, "url": BASE + "/data/", "description": HUB_DESC}


# ---- Dataset 2: same prompt, 41 languages, Claude / Gemini / GPT tokenizers (measured 2026-10-17) ----
MULTI_PATH = "/data/token-cost-by-language-claude-gemini"
MULTI_MEASURED = "2026-10-17"
MULTI_CHART = "/token-cost-claude-gemini-gpt-chart.png"
MULTI_DOI = "10.5281/zenodo.23428350"  # concept DOI
MULTI_MIRRORS = [("Zenodo", "https://zenodo.org/records/23428351"),
                 ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/token-cost-by-language-claude-gemini"),
                 ("Kaggle", "https://www.kaggle.com/datasets/johnisking/token-cost-by-language-claude-gemini-gpt"),
                 ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/claude-gemini")]
MULTI_TITLE = "Token cost by language on Claude, Gemini and GPT: 41 languages measured"
MULTI_DESC = ("Dataset: the same prompt in 41 languages counted on Claude Opus/Sonnet 5.5, Claude Haiku 4.5, Gemini 3.x and GPT (o200k). "
              "Korean needs 89 Claude tokens vs 49 on GPT and 48 on Gemini. Free CSV, CC BY 4.0.")
MULTI_COLS = [("claude55", "Claude Opus/Sonnet 5.5"), ("claude45", "Claude Haiku 4.5"), ("gemini", "Gemini 3.x"), ("gpt", "GPT o200k")]


def _multi_rows():
    rows = json.load(open(os.path.join(ROOT, "blog_data", "langmulti", "combined.json"), encoding="utf-8"))
    prompts = {r["code"]: r["prompt"] for r in _lang_rows()}
    for r in rows:
        r["prompt"] = prompts[r["code"]]
    rows.sort(key=lambda r: (r["claude55"], r["gemini"], r["name"]))
    return rows


def multi_citation():
    return f"TokenSave (2026). {MULTI_TITLE} [Data set]. Zenodo. https://doi.org/{MULTI_DOI}"


def write_multi_files(dist):
    rows = _multi_rows()
    buf = io.StringIO()
    w = csv.writer(buf)
    hdr = ["language_code", "language"]
    for k, _ in MULTI_COLS:
        hdr += [f"{k}_tokens", f"{k}_vs_english_pct"]
    w.writerow(hdr + ["prompt"])
    for r in rows:
        line = [r["code"], r["name"]]
        for k, _ in MULTI_COLS:
            line += [r[k], r[k + "_pct"]]
        w.writerow(line + [r["prompt"]])
    open(os.path.join(dist, "data", "token-cost-by-language-claude-gemini.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=MULTI_TITLE, url=BASE + MULTI_PATH, license="CC BY 4.0", measured=MULTI_MEASURED,
                tokenizers={"claude55": "Claude Opus 5.5 / Sonnet 5.5 (identical counts)", "claude45": "Claude Haiku 4.5",
                            "gemini": "Gemini 3.8 Flash / 3.1 Pro (identical counts)", "gpt": "OpenAI o200k_base (GPT-4o and later)"},
                citation=multi_citation(), rows=[{k: r[k] for k in r} for r in rows])
    open(os.path.join(dist, "data", "token-cost-by-language-claude-gemini.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def multi_ld():
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "Dataset", "name": MULTI_TITLE, "description": MULTI_DESC, "url": BASE + MULTI_PATH,
         "identifier": f"https://doi.org/{MULTI_DOI}", "sameAs": [u for _, u in MULTI_MIRRORS],
         "license": LICENSE, "isAccessibleForFree": True,
         "creator": {"@type": "Organization", "name": "TokenSave", "url": BASE + "/"},
         "datePublished": MULTI_MEASURED,
         "keywords": ["tokenizer", "Claude tokenizer", "Gemini tokenizer", "tokens per language", "LLM cost", "multilingual"],
         "variableMeasured": ["tokens (Claude 5.5)", "tokens (Claude Haiku 4.5)", "tokens (Gemini 3.x)", "tokens (o200k_base)", "difference vs English (%)"],
         "measurementTechnique": "Same prompt in 41 languages; Claude counts from Claude Code usage minus a one-character baseline, Gemini from the Google AI Studio token counter, GPT with tiktoken",
         "isBasedOn": BASE + LANG_PATH, "image": BASE + MULTI_CHART,
         "distribution": [
             {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": BASE + "/data/token-cost-by-language-claude-gemini.csv"},
             {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": BASE + "/data/token-cost-by-language-claude-gemini.json"}]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Data", "item": BASE + "/data/"},
            {"@type": "ListItem", "position": 3, "name": MULTI_TITLE, "item": BASE + MULTI_PATH}]}]}


def multi_html():
    rows = _multi_rows()
    by = {r["code"]: r for r in rows}
    en = by["en"]
    import statistics as st
    med = {k: round(st.median([r[k + "_pct"] for r in rows if r["code"] != "en"])) for k, _ in MULTI_COLS}
    kn, ko, hi = by["kn"], by["ko"], by["hi"]
    head = "".join(f'<th class="text-right">{esc(n)}</th>' for _, n in MULTI_COLS)
    trs = "\n".join(
        f'          <tr><td>{esc(r["name"])}</td>' + "".join(
            f'<td class="text-right tabular-nums">{r[k]} <span class="text-zinc-500">({_pct(r[k + "_pct"])})</span></td>' for k, _ in MULTI_COLS) + "</tr>"
        for r in rows)
    embed = (f'<a href="{BASE}{MULTI_PATH}"><img src="{BASE}{MULTI_CHART}" '
             f'alt="Extra tokens vs English on Claude, Gemini and GPT, 41 languages (TokenSave)" width="1200" loading="lazy"></a>\n'
             f'<p>Source: <a href="{BASE}{MULTI_PATH}">TokenSave, token cost by language on Claude, Gemini and GPT</a> (CC BY 4.0)</p>')
    return f'''    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <p class="not-prose text-xs font-semibold uppercase tracking-wider text-violet-300"><a href="/data/" class="no-underline" style="text-decoration:none">TokenSave Data</a> · Dataset</p>
      <h1 class="text-3xl font-extrabold text-white">How many tokens each language needs on Claude, Gemini and GPT</h1>
      <p class="mt-3 text-lg text-zinc-200"><strong>The same Korean prompt needs {ko["claude55"]} tokens on Claude Opus/Sonnet 5.5, {ko["gpt"]} on GPT and {ko["gemini"]} on Gemini.</strong> Across 40 non-English languages, the median extra cost versus English is {_pct(med["gemini"])} on Gemini, {_pct(med["gpt"])} on GPT and {_pct(med["claude55"])} on Claude 5.5. The widest gap is Kannada: {_pct(kn["claude55_pct"])} on Claude 5.5 against {_pct(kn["gemini_pct"])} on Gemini.</p>
      <p class="text-sm text-zinc-400">Measured {MULTI_MEASURED} · 41 languages · 4 tokenizers · License <a href="{LICENSE}">CC BY 4.0</a> · Companion to <a href="{LANG_PATH}">the GPT-only dataset</a></p>
      <p class="text-sm text-zinc-400">DOI <a href="https://doi.org/{MULTI_DOI}">{MULTI_DOI}</a> · Also on {" · ".join(f'<a href="{u}">{n}</a>' for n, u in MULTI_MIRRORS[1:])}</p>
      <div class="not-prose flex flex-wrap gap-2 my-4">
        <a href="/data/token-cost-by-language-claude-gemini.csv" {BTN} style="text-decoration:none">⬇ CSV</a>
        <a href="/data/token-cost-by-language-claude-gemini.json" {BTN} style="text-decoration:none">⬇ JSON</a>
        <a href="#cite" {BTN} style="text-decoration:none">How to cite</a>
      </div>
      <img src="{MULTI_CHART}" alt="Extra tokens versus English for the same prompt on Claude 5.5, GPT and Gemini, 41 languages" width="1200" loading="lazy">
      <h2>Key findings</h2>
      <ul>
        <li><strong>English itself costs more on Claude 5.5.</strong> The English prompt is {en["claude55"]} tokens on Claude Opus/Sonnet 5.5, {en["claude45"]} on Claude Haiku 4.5, and {en["gpt"]} on both GPT and Gemini.</li>
        <li><strong>Claude's newer tokenizer changed Latin-script text only.</strong> Compared with Haiku 4.5, Claude 5.5 needs {round((en["claude55"] / en["claude45"] - 1) * 100)}% more tokens for English and more for every other Latin-script language, while Korean, Japanese, Chinese, Cyrillic, Arabic, Hebrew, Greek, Thai and the Indic languages have exactly the same counts. That is why the gap versus English looks smaller on Claude 5.5 (Korean {_pct(ko["claude55_pct"])}) than on Haiku 4.5 (Korean {_pct(ko["claude45_pct"])}).</li>
        <li><strong>Indic languages are the costliest on Claude.</strong> Hindi is {_pct(hi["claude55_pct"])} on Claude 5.5 against {_pct(hi["gpt_pct"])} on GPT and {_pct(hi["gemini_pct"])} on Gemini.</li>
        <li><strong>Gemini has the smallest gap overall.</strong> Simplified Chinese costs the same as English on Gemini ({_pct(by["zh-CN"]["gemini_pct"])}).</li>
        <li><strong>Models from the same family share counts.</strong> Claude Opus 5.5 and Sonnet 5.5 gave identical counts for all 41 languages; Gemini 3.8 Flash and 3.1 Pro matched on every language we re-checked.</li>
      </ul>
      <h2>All 41 languages</h2>
      <p class="text-sm text-zinc-400">Tokens for the same prompt, with the difference versus English in brackets. Sorted by Claude 5.5.</p>
      <div class="overflow-x-auto">
        <table>
          <thead><tr><th>Language</th>{head}</tr></thead>
          <tbody>
{trs}
          </tbody>
        </table>
      </div>
      <h2>Method</h2>
      <ul>
        <li>Same prompt and translations as <a href="{LANG_PATH}">our GPT dataset</a>: <em>“{esc(en["prompt"])}”</em> in 41 languages. Every translated prompt is in the CSV.</li>
        <li><strong>Claude:</strong> each prompt was sent through Claude Code (<code>claude -p</code>) with a fixed one-line system prompt, and the input tokens it reported (uncached + cache read + cache write) were reduced by the same run with a one-character message. Re-running with a different system prompt, a different baseline character and a different order gave identical counts.</li>
        <li><strong>Gemini:</strong> the prompt token counter in Google AI Studio, which adds one start token (“a” shows 2, “a a a” shows 4); we subtracted it. Measured on Gemini 3.8 Flash and re-checked on Gemini 3.1 Pro.</li>
        <li><strong>GPT:</strong> OpenAI's <a href="https://github.com/openai/tiktoken">tiktoken</a> with <code>o200k_base</code>.</li>
        <li>“vs English” = tokens in the language ÷ English tokens on the same tokenizer − 1, rounded to a whole percent.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>One prompt. With other text the ratios move by roughly ±10–20 percentage points; the ranking is more stable than the exact numbers.</li>
        <li>Claude counts come from usage reports rather than a dedicated count endpoint, so each value can be off by about ±2 tokens (under 5 percentage points against English).</li>
        <li>Input text only; output length is not measured. Prices differ by model, so more tokens does not always mean a higher bill. Use the <a href="/">token calculator</a> to compare costs.</li>
      </ul>
      <h2 id="cite">How to cite</h2>
      <p>Free to use, quote and republish with attribution under <a href="{LICENSE}">CC BY 4.0</a>. Please link to this page or the DOI.</p>
      <div class="not-prose bg-zinc-950/70 border border-zinc-800 rounded-xl p-4">
        <p id="cite-text" class="text-sm text-zinc-200 break-words">{esc(multi_citation())}</p>
        <div class="mt-3"><button type="button" data-copy="cite-text" {BTN}>Copy citation</button></div>
      </div>
      <h3>Embed the chart</h3>
      <div class="not-prose">
        <textarea id="embed-code" readonly rows="4" class="w-full text-xs font-mono bg-zinc-950/70 border border-zinc-800 rounded-xl p-3 text-zinc-300">{esc(embed)}</textarea>
        <div class="mt-2"><button type="button" data-copy="embed-code" {BTN}>Copy embed code</button></div>
      </div>
      <h2>Related</h2>
      <ul>
        <li><a href="{LANG_PATH}">GPT-only dataset with the older cl100k tokenizer</a></li>
        <li><a href="/ko/blog/claude-hangugeo-token">Our Claude Korean test (input and output, in Korean)</a></li>
        <li><a href="/">Count tokens for your own text</a></li>
      </ul>
      <p class="text-sm text-zinc-400">Questions or corrections: <a href="mailto:contact@jonhisking.com">contact@jonhisking.com</a></p>
    </article>
{COPY_JS}'''


# ---- Dataset 3: same data in 8 formats (JSON, YAML, XML, CSV, TSV, Markdown, TOON) on 4 tokenizers (measured 2026-10-17) ----
FMT_PATH = "/data/token-cost-by-format"
FMT_MEASURED = "2026-10-17"
FMT_CHART = "/token-cost-by-format-chart.png"
FMT_DOI = "10.5281/zenodo.23435788"  # concept DOI
FMT_MIRRORS = [("Zenodo", "https://zenodo.org/records/23435789"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/token-cost-by-format"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/token-cost-by-data-format-json-csv-toon"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/format")]
FMT_TITLE = "Token cost by data format: JSON vs YAML vs CSV vs TOON on Claude, Gemini and GPT"
FMT_DESC = ("Dataset: the same 20-row product table in 8 formats (JSON, minified JSON, YAML, XML, CSV, TSV, Markdown table, TOON) "
            "counted on Claude 5.5, Claude Haiku 4.5, Gemini and GPT. CSV uses about two thirds fewer tokens than indented JSON. Free CSV, CC BY 4.0.")
FMT_NAMES = {"json_pretty": "JSON (indented)", "json_minified": "JSON (minified)", "yaml": "YAML", "xml": "XML", "csv": "CSV",
             "tsv": "TSV", "markdown_table": "Markdown table", "toon": "TOON"}


def _fmt_rows():
    rows = json.load(open(os.path.join(ROOT, "blog_data", "fmtdata", "combined.json"), encoding="utf-8"))
    rows.sort(key=lambda r: (r["gpt"], r["claude55"]))
    return rows


def _fmt_samples():
    return json.load(open(os.path.join(ROOT, "blog_data", "fmtdata", "formats.json"), encoding="utf-8"))


def fmt_citation():
    return f"TokenSave (2026). {FMT_TITLE} [Data set]. Zenodo. https://doi.org/{FMT_DOI}"


def write_fmt_files(dist):
    rows = _fmt_rows()
    buf = io.StringIO()
    w = csv.writer(buf)
    cols = [k for k, _ in MULTI_COLS]
    w.writerow(["format", "characters"] + sum([[f"{k}_tokens", f"{k}_vs_indented_json_pct"] for k in cols], []))
    for r in rows:
        w.writerow([r["format"], r["chars"]] + sum([[r[k], r[k + "_vs_json"]] for k in cols], []))
    open(os.path.join(dist, "data", "token-cost-by-format.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=FMT_TITLE, url=BASE + FMT_PATH, license="CC BY 4.0", measured=FMT_MEASURED,
                data="20 products x 7 fields (id, name, category, price, in_stock, rating, tags)",
                tokenizers={"claude55": "Claude Opus 5.5 / Sonnet 5.5 (identical counts)", "claude45": "Claude Haiku 4.5",
                            "gemini": "Gemini 3.8 Flash", "gpt": "OpenAI o200k_base (GPT-4o and later)"},
                citation=fmt_citation(), rows=rows, inputs=_fmt_samples())
    open(os.path.join(dist, "data", "token-cost-by-format.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def fmt_ld():
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "Dataset", "name": FMT_TITLE, "description": FMT_DESC, "url": BASE + FMT_PATH,
         "identifier": f"https://doi.org/{FMT_DOI}", "sameAs": [u for _, u in FMT_MIRRORS],
         "license": LICENSE, "isAccessibleForFree": True,
         "creator": {"@type": "Organization", "name": "TokenSave", "url": BASE + "/"},
         "datePublished": FMT_MEASURED,
         "keywords": ["JSON vs CSV tokens", "TOON", "YAML tokens", "prompt format", "LLM cost", "tokenizer", "Claude", "Gemini"],
         "variableMeasured": ["tokens (Claude 5.5)", "tokens (Claude Haiku 4.5)", "tokens (Gemini 3.x)", "tokens (o200k_base)", "difference vs indented JSON (%)"],
         "measurementTechnique": "Same 20-row table serialised in 8 formats; Claude counts from Claude Code usage minus a one-character baseline, Gemini from the Google AI Studio token counter, GPT with tiktoken",
         "image": BASE + FMT_CHART,
         "distribution": [
             {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": BASE + "/data/token-cost-by-format.csv"},
             {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": BASE + "/data/token-cost-by-format.json"}]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Data", "item": BASE + "/data/"},
            {"@type": "ListItem", "position": 3, "name": FMT_TITLE, "item": BASE + FMT_PATH}]}]}


def fmt_html():
    rows = _fmt_rows()
    by = {r["format"]: r for r in rows}
    s = _fmt_samples()
    jp, jm, cs, to, xm = by["json_pretty"], by["json_minified"], by["csv"], by["toon"], by["xml"]
    head = "".join(f'<th class="text-right">{esc(n)}</th>' for _, n in MULTI_COLS)
    trs = "\n".join(
        f'          <tr><td>{esc(FMT_NAMES[r["format"]])}</td>' + "".join(
            f'<td class="text-right tabular-nums">{r[k]:,} <span class="text-zinc-500">({_pct(r[k + "_vs_json"])})</span></td>' for k, _ in MULTI_COLS) + "</tr>"
        for r in rows)
    def first_lines(txt, n):
        return esc("\n".join(txt.splitlines()[:n]) + "\n…")
    vs_gpt = {k: round((by[k]["claude55"] / by[k]["gpt"] - 1) * 100) for k in by}
    embed = (f'<a href="{BASE}{FMT_PATH}"><img src="{BASE}{FMT_CHART}" '
             f'alt="Tokens for the same data in 8 formats on Claude, Gemini and GPT (TokenSave)" width="1200" loading="lazy"></a>\n'
             f'<p>Source: <a href="{BASE}{FMT_PATH}">TokenSave, token cost by data format</a> (CC BY 4.0)</p>')
    return f'''    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <p class="not-prose text-xs font-semibold uppercase tracking-wider text-violet-300"><a href="/data/" class="no-underline" style="text-decoration:none">TokenSave Data</a> · Dataset</p>
      <h1 class="text-3xl font-extrabold text-white">JSON vs YAML vs CSV vs TOON: how many tokens each format costs</h1>
      <p class="mt-3 text-lg text-zinc-200"><strong>The same 20-product table costs {jp["gpt"]:,} GPT tokens as indented JSON and {cs["gpt"]:,} as CSV ({abs(cs["gpt_vs_json"])}% fewer).</strong> CSV was the cheapest format on every tokenizer we tested (Claude, Gemini, GPT), and the newer TOON format came close but did not beat it. XML was the most expensive.</p>
      <p class="text-sm text-zinc-400">Measured {FMT_MEASURED} · 8 formats · 4 tokenizers · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{MULTI_PATH}">token cost by language</a></p>
      <p class="text-sm text-zinc-400">DOI <a href="https://doi.org/{FMT_DOI}">{FMT_DOI}</a> · Also on {" · ".join(f'<a href="{u}">{n}</a>' for n, u in FMT_MIRRORS[1:])}</p>
      <div class="not-prose flex flex-wrap gap-2 my-4">
        <a href="/data/token-cost-by-format.csv" {BTN} style="text-decoration:none">⬇ CSV</a>
        <a href="/data/token-cost-by-format.json" {BTN} style="text-decoration:none">⬇ JSON (with all 8 inputs)</a>
        <a href="#cite" {BTN} style="text-decoration:none">How to cite</a>
      </div>
      <img src="{FMT_CHART}" alt="Tokens for the same 20-row table in 8 formats on Claude, Gemini and GPT" width="1200" loading="lazy">
      <h2>Key findings</h2>
      <ul>
        <li><strong>CSV and TSV are the cheapest.</strong> Switching from indented JSON to CSV cuts tokens by {abs(cs["gpt_vs_json"])}% on GPT, {abs(cs["claude55_vs_json"])}% on Claude 5.5 and {abs(cs["gemini_vs_json"])}% on Gemini.</li>
        <li><strong>TOON is close to CSV, not below it.</strong> The token-oriented format needs {round((to["gpt"] / cs["gpt"] - 1) * 100)}% more tokens than CSV on GPT and {round((to["claude55"] / cs["claude55"] - 1) * 100)}% more on Claude 5.5, while still using about two thirds fewer than indented JSON.</li>
        <li><strong>Minifying JSON helps less on Claude.</strong> Removing whitespace saves {abs(jm["gemini_vs_json"])}% on Gemini and {abs(jm["gpt_vs_json"])}% on GPT but only {abs(jm["claude55_vs_json"])}% on Claude 5.5. Minified JSON is the format where Claude 5.5 needs the most extra tokens over GPT ({_pct(vs_gpt["json_minified"])}).</li>
        <li><strong>Claude 5.5 uses more tokens for every format.</strong> Compared with GPT it needs {min(vs_gpt.values())}% to {max(vs_gpt.values())}% more for the same data, and more than Claude Haiku 4.5 as well. The jump over Haiku 4.5 is largest for minified JSON ({_pct(round((jm["claude55"] / jm["claude45"] - 1) * 100))}), where punctuation is packed with no spaces, matching our finding that Claude's newer tokenizer changed how Latin-script text is split.</li>
        <li><strong>XML is the most expensive.</strong> It needs {_pct(xm["gpt_vs_json"])} versus indented JSON on GPT.</li>
      </ul>
      <h2>All 8 formats</h2>
      <p class="text-sm text-zinc-400">Tokens for the same table, with the difference versus indented JSON on the same tokenizer in brackets.</p>
      <div class="overflow-x-auto">
        <table>
          <thead><tr><th>Format</th>{head}</tr></thead>
          <tbody>
{trs}
          </tbody>
        </table>
      </div>
      <h2>What the inputs look like</h2>
      <p>All eight files hold the same 20 products with 7 fields each (id, name, category, price, in stock, rating, tags). The full inputs are in the JSON download.</p>
      <div class="not-prose grid gap-3 sm:grid-cols-3 text-xs">
        <div><p class="text-zinc-400 mb-1">CSV</p><pre class="bg-zinc-950/70 border border-zinc-800 rounded-xl p-3 overflow-x-auto text-zinc-300">{first_lines(s["csv"], 3)}</pre></div>
        <div><p class="text-zinc-400 mb-1">TOON</p><pre class="bg-zinc-950/70 border border-zinc-800 rounded-xl p-3 overflow-x-auto text-zinc-300">{first_lines(s["toon"], 3)}</pre></div>
        <div><p class="text-zinc-400 mb-1">JSON (indented)</p><pre class="bg-zinc-950/70 border border-zinc-800 rounded-xl p-3 overflow-x-auto text-zinc-300">{first_lines(s["json_pretty"], 6)}</pre></div>
      </div>
      <h2>Method</h2>
      <ul>
        <li>One table of 20 products × 7 fields, written out in 8 formats: indented JSON (2 spaces), minified JSON, YAML, XML, CSV, TSV, a Markdown table and TOON (tabular form, tags joined with |).</li>
        <li><strong>Claude:</strong> each file sent through Claude Code (<code>claude -p</code>) with a fixed one-line system prompt; reported input tokens minus the same run with a one-character message. Opus 5.5 and Sonnet 5.5 gave identical counts.</li>
        <li><strong>Gemini:</strong> Google AI Studio prompt token counter on Gemini 3.8 Flash, minus its one start token. XML, CSV and indented JSON were measured a second time with a stricter reading of the counter; CSV and JSON matched, and the XML value shown is from the second run.</li>
        <li><strong>GPT:</strong> <a href="https://github.com/openai/tiktoken">tiktoken</a> with <code>o200k_base</code>.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>One flat table. Deeply nested data does not fit CSV well, and there JSON or YAML may be the practical choice.</li>
        <li>Token count is not the only factor: models may read some formats more reliably than others. This dataset measures cost only.</li>
        <li>Claude values can be off by about ±2 tokens; with tables of 400+ tokens that is under 1%.</li>
      </ul>
      <h2 id="cite">How to cite</h2>
      <p>Free to use, quote and republish with attribution under <a href="{LICENSE}">CC BY 4.0</a>. Please link to this page.</p>
      <div class="not-prose bg-zinc-950/70 border border-zinc-800 rounded-xl p-4">
        <p id="cite-text" class="text-sm text-zinc-200 break-words">{esc(fmt_citation())}</p>
        <div class="mt-3"><button type="button" data-copy="cite-text" {BTN}>Copy citation</button></div>
      </div>
      <h3>Embed the chart</h3>
      <div class="not-prose">
        <textarea id="embed-code" readonly rows="4" class="w-full text-xs font-mono bg-zinc-950/70 border border-zinc-800 rounded-xl p-3 text-zinc-300">{esc(embed)}</textarea>
        <div class="mt-2"><button type="button" data-copy="embed-code" {BTN}>Copy embed code</button></div>
      </div>
      <h2>Related</h2>
      <ul>
        <li><a href="{MULTI_PATH}">Token cost by language on Claude, Gemini and GPT</a></li>
        <li><a href="/">Count tokens for your own data</a></li>
      </ul>
      <p class="text-sm text-zinc-400">Questions or corrections: <a href="mailto:contact@jonhisking.com">contact@jonhisking.com</a></p>
    </article>
{COPY_JS}'''


# ---- Dataset 4: input tokens for one image by resolution on Claude, Gemini and GPT (measured 2026-10-18) ----
IMG_PATH = "/data/image-token-cost"
IMG_MEASURED = "2026-10-18"
IMG_CHART = "/image-token-cost-chart.png"
IMG_DOI = "10.5281/zenodo.23443906"  # concept DOI
IMG_MIRRORS = [("Zenodo", "https://zenodo.org/records/23443907"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/image-token-cost"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/image-token-cost-by-resolution-claudegeminigpt"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/image")]
IMG_TITLE = "Image input token cost by resolution: Claude vs Gemini vs GPT"
IMG_DESC = ("Dataset: input tokens for one image at 10 resolutions (256×256 to a 12 MP photo) on Claude Opus/Sonnet 5.5, Claude Haiku 4.5, "
            "Gemini 3.x and GPT. Gemini charges a flat ~1,100 tokens; a 12 MP photo costs 14,364 tokens on GPT-6 Astra by default. Free CSV, CC BY 4.0.")
IMG_COLS = [("claude55", "Claude Opus/Sonnet 5.5"), ("claude45", "Claude Haiku 4.5"), ("gemini", "Gemini 3.x"),
            ("gpt6_auto", "GPT-6 Astra (default)"), ("gpt6_high", "GPT-6 Astra (detail: high)"), ("gpt55_auto", "GPT-5.5 (default)")]
IMG_LABEL = {"256x256": "256×256", "512x512": "512×512", "768x768": "768×768", "1024x1024": "1024×1024",
             "1280x720": "1280×720 (720p)", "1920x1080": "1920×1080 (1080p)", "1080x1920": "1080×1920 (phone screen)",
             "2560x1440": "2560×1440 (1440p)", "3840x2160": "3840×2160 (4K)", "4032x3024": "4032×3024 (12 MP photo)"}


def _img_rows():
    return json.load(open(os.path.join(ROOT, "blog_data", "imgdata", "combined.json"), encoding="utf-8"))


def img_citation():
    return f"TokenSave (2026). {IMG_TITLE} [Data set]. Zenodo. https://doi.org/{IMG_DOI}"


def write_img_files(dist):
    rows = _img_rows()
    buf = io.StringIO()
    w = csv.writer(buf)
    cols = [k for k, _ in IMG_COLS]
    w.writerow(["size", "width", "height", "megapixels"] + [f"{k}_tokens" for k in cols])
    for r in rows:
        w.writerow([r["size"], r["width"], r["height"], r["megapixels"]] + [r[k] for k in cols])
    open(os.path.join(dist, "data", "image-token-cost.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=IMG_TITLE, url=BASE + IMG_PATH, license="CC BY 4.0", measured=IMG_MEASURED,
                columns={"claude55": "Claude Opus 5.5 / Sonnet 5.5, measured (identical counts)",
                         "claude45": "Claude Haiku 4.5, measured",
                         "gemini": "Gemini 3.8 Flash, measured in Google AI Studio (default media resolution)",
                         "gpt6_auto": "gpt-6-astra, detail auto/original, computed with OpenAI's published patch formula",
                         "gpt6_high": "gpt-6-astra, detail high (2,500-patch budget), computed",
                         "gpt55_auto": "gpt-5.5, detail auto/original (10,000-patch budget), computed"},
                citation=img_citation(), rows=rows)
    open(os.path.join(dist, "data", "image-token-cost.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def img_ld():
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "Dataset", "name": IMG_TITLE, "description": IMG_DESC, "url": BASE + IMG_PATH,
         "identifier": f"https://doi.org/{IMG_DOI}", "sameAs": [u for _, u in IMG_MIRRORS],
         "license": LICENSE, "isAccessibleForFree": True,
         "creator": {"@type": "Organization", "name": "TokenSave", "url": BASE + "/"},
         "datePublished": IMG_MEASURED,
         "keywords": ["image tokens", "vision tokens", "image input cost", "Claude vision", "Gemini image tokens", "GPT image tokens", "LLM cost"],
         "variableMeasured": ["image input tokens (Claude 5.5)", "image input tokens (Claude Haiku 4.5)", "image input tokens (Gemini 3.x)", "image input tokens (GPT-6 Astra, GPT-5.5)"],
         "measurementTechnique": "Same synthetic PNG at 10 resolutions; Claude from Claude Code usage minus a text-only baseline, Gemini from the Google AI Studio per-image token count, GPT from OpenAI's published patch formula",
         "image": BASE + IMG_CHART,
         "distribution": [
             {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": BASE + "/data/image-token-cost.csv"},
             {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": BASE + "/data/image-token-cost.json"}]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Data", "item": BASE + "/data/"},
            {"@type": "ListItem", "position": 3, "name": IMG_TITLE, "item": BASE + IMG_PATH}]}]}


def img_html():
    rows = _img_rows()
    by = {r["size"]: r for r in rows}
    sq, small, fhd, photo = by["1024x1024"], by["256x256"], by["1920x1080"], by["4032x3024"]
    gem_lo, gem_hi = min(r["gemini"] for r in rows), max(r["gemini"] for r in rows)
    pct = lambda a, b: round((a / b - 1) * 100)
    head = "".join(f'<th class="text-right">{esc(n)}</th>' for _, n in IMG_COLS)
    trs = "\n".join(
        f'          <tr><td>{esc(IMG_LABEL[r["size"]])}</td>' + "".join(
            f'<td class="text-right tabular-nums">{r[k]:,}</td>' for k, _ in IMG_COLS) + "</tr>"
        for r in rows)
    embed = (f'<a href="{BASE}{IMG_PATH}"><img src="{BASE}{IMG_CHART}" '
             f'alt="Input tokens for one image at different resolutions on Claude, Gemini and GPT (TokenSave)" width="1200" loading="lazy"></a>\n'
             f'<p>Source: <a href="{BASE}{IMG_PATH}">TokenSave, image input token cost</a> (CC BY 4.0)</p>')
    return f'''    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <p class="not-prose text-xs font-semibold uppercase tracking-wider text-violet-300"><a href="/data/" class="no-underline" style="text-decoration:none">TokenSave Data</a> · Dataset</p>
      <h1 class="text-3xl font-extrabold text-white">How many tokens does an image cost? Claude vs Gemini vs GPT</h1>
      <p class="mt-3 text-lg text-zinc-200"><strong>A 12-megapixel phone photo costs {photo["gemini"]:,} input tokens on Gemini, {photo["claude55"]:,} on Claude 5.5 and {photo["gpt6_auto"]:,} on GPT-6 Astra with default settings.</strong> Gemini charges about the same for every image, so it is the cheapest for large pictures and the most expensive for small ones.</p>
      <p class="text-sm text-zinc-400">Measured {IMG_MEASURED} · 10 resolutions · 6 model settings · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{MULTI_PATH}">token cost by language</a>, <a href="{FMT_PATH}">by data format</a></p>
      <p class="text-sm text-zinc-400">DOI <a href="https://doi.org/{IMG_DOI}">{IMG_DOI}</a> · Also on {" · ".join(f'<a href="{u}">{n}</a>' for n, u in IMG_MIRRORS[1:])}</p>
      <div class="not-prose flex flex-wrap gap-2 my-4">
        <a href="/data/image-token-cost.csv" {BTN} style="text-decoration:none">⬇ CSV</a>
        <a href="/data/image-token-cost.json" {BTN} style="text-decoration:none">⬇ JSON</a>
        <a href="#cite" {BTN} style="text-decoration:none">How to cite</a>
      </div>
      <img src="{IMG_CHART}" alt="Input tokens for one image at 8 resolutions on Claude 5.5, Claude Haiku 4.5, GPT-6 Astra and Gemini" width="1200" loading="lazy">
      <h2>Key findings</h2>
      <ul>
        <li><strong>Gemini charges a flat rate.</strong> Every image we sent cost {gem_lo:,} to {gem_hi:,} tokens on Gemini 3.x, from a 256×256 icon to a 12 MP photo. The small icon costs {small["gemini"]:,} tokens there against {small["gpt6_auto"]:,} on GPT-6 Astra, but the photo costs {abs(pct(photo["gemini"], photo["gpt6_auto"]))}% less than on GPT-6 Astra.</li>
        <li><strong>GPT-6 Astra does not shrink images by default.</strong> Its default detail level keeps the original size, so cost grows with every pixel: {photo["gpt6_auto"]:,} tokens for a 12 MP photo. Setting <code>detail: "high"</code> caps it at {photo["gpt6_high"]:,} tokens ({pct(photo["gpt6_high"], photo["gpt6_auto"])}%).</li>
        <li><strong>Claude 5.5 keeps more detail than Haiku 4.5, and charges for it.</strong> Up to about 1 megapixel the two cost almost the same ({sq["claude55"]:,} vs {sq["claude45"]:,} tokens at 1024×1024). Above that Haiku 4.5 levels off near {photo["claude45"]:,} tokens, while Claude 5.5 needs {pct(fhd["claude55"], fhd["claude45"])}% more for a 1080p screenshot and {pct(photo["claude55"], photo["claude45"])}% more for a 12 MP photo.</li>
        <li><strong>Resizing before you send saves money on Claude and GPT.</strong> A 1024×1024 image costs {sq["claude55"]:,} tokens on Claude 5.5 and {sq["gpt6_auto"]:,} on GPT-6 Astra; shrinking a 12 MP photo to that size cuts its cost by {abs(pct(sq["claude55"], photo["claude55"]))}% on Claude 5.5 and {abs(pct(sq["gpt6_auto"], photo["gpt6_auto"]))}% on GPT-6 Astra. On Gemini resizing changes almost nothing.</li>
      </ul>
      <h2>All resolutions</h2>
      <p class="text-sm text-zinc-400">Input tokens for one image. Claude and Gemini are measured; GPT columns are computed with OpenAI's published formula.</p>
      <div class="overflow-x-auto">
        <table>
          <thead><tr><th>Image size</th>{head}</tr></thead>
          <tbody>
{trs}
          </tbody>
        </table>
      </div>
      <h2>Method</h2>
      <ul>
        <li>One synthetic PNG (colour gradient with shapes) rendered at 10 sizes, from 256×256 to 4032×3024. A second image with different content was measured at three sizes on Claude 5.5 and Gemini and gave identical counts, so the counts depend on size, not content.</li>
        <li><strong>Claude:</strong> each image sent through Claude Code (<code>claude -p</code>, stream-json input) with a fixed one-line system prompt and a one-character text message; reported input tokens minus the same run without the image. Opus 5.5 and Sonnet 5.5 gave identical counts. The figures include the small per-image overhead of a message.</li>
        <li><strong>Gemini:</strong> per-image token count shown by Google AI Studio for Gemini 3.8 Flash at the default media resolution.</li>
        <li><strong>GPT:</strong> computed with the 32×32-pixel patch formula and model limits in OpenAI's <a href="https://developers.openai.com/api/docs/guides/images-vision">vision guide</a> (patch count × 1.2). Our implementation reproduces the guide's three worked examples exactly. Not measured through the API.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>Input tokens only. The price per token differs by model, so equal token counts do not mean equal cost.</li>
        <li>Default settings. Gemini's media resolution and GPT's <code>detail</code> option change the counts; we show GPT-6 Astra both ways.</li>
        <li>Claude counts are from Claude Code; the API may differ by a few tokens of message overhead.</li>
      </ul>
      <h2 id="cite">How to cite</h2>
      <p>Free to use, quote and republish with attribution under <a href="{LICENSE}">CC BY 4.0</a>. Please link to this page.</p>
      <div class="not-prose bg-zinc-950/70 border border-zinc-800 rounded-xl p-4">
        <p id="cite-text" class="text-sm text-zinc-200 break-words">{esc(img_citation())}</p>
        <div class="mt-3"><button type="button" data-copy="cite-text" {BTN}>Copy citation</button></div>
      </div>
      <h3>Embed the chart</h3>
      <div class="not-prose">
        <textarea id="embed-code" readonly rows="4" class="w-full text-xs font-mono bg-zinc-950/70 border border-zinc-800 rounded-xl p-3 text-zinc-300">{esc(embed)}</textarea>
        <div class="mt-2"><button type="button" data-copy="embed-code" {BTN}>Copy embed code</button></div>
      </div>
      <h2>Related</h2>
      <ul>
        <li><a href="{MULTI_PATH}">Token cost by language on Claude, Gemini and GPT</a></li>
        <li><a href="{FMT_PATH}">Token cost by data format (JSON vs CSV vs TOON)</a></li>
        <li><a href="/">Count tokens for your own text</a></li>
      </ul>
      <p class="text-sm text-zinc-400">Questions or corrections: <a href="mailto:contact@jonhisking.com">contact@jonhisking.com</a></p>
    </article>
{COPY_JS}'''


def _dataset_ld(title, desc, path, measured, keywords, measured_vars, technique, chart, files, doi=None, mirrors=None):
    ds = {"@type": "Dataset", "name": title, "description": desc, "url": BASE + path,
         "license": LICENSE, "isAccessibleForFree": True,
         "creator": {"@type": "Organization", "name": "TokenSave", "url": BASE + "/"},
         "datePublished": measured, "keywords": keywords, "variableMeasured": measured_vars,
         "measurementTechnique": technique, "image": BASE + chart,
         "distribution": [{"@type": "DataDownload", "encodingFormat": t, "contentUrl": BASE + "/data/" + f} for f, t in files]}
    if doi:
        ds["identifier"] = f"https://doi.org/{doi}"
        ds["sameAs"] = [u for _, u in (mirrors or [])]
    return {"@context": "https://schema.org", "@graph": [ds,
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "TokenSave", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Data", "item": BASE + "/data/"},
            {"@type": "ListItem", "position": 3, "name": title, "item": BASE + path}]}]}


def _page_tail(citation, embed, related):
    rel = "\n".join(f'        <li><a href="{u}">{esc(t)}</a></li>' for u, t in related)
    return f'''      <h2 id="cite">How to cite</h2>
      <p>Free to use, quote and republish with attribution under <a href="{LICENSE}">CC BY 4.0</a>. Please link to this page.</p>
      <div class="not-prose bg-zinc-950/70 border border-zinc-800 rounded-xl p-4">
        <p id="cite-text" class="text-sm text-zinc-200 break-words">{esc(citation)}</p>
        <div class="mt-3"><button type="button" data-copy="cite-text" {BTN}>Copy citation</button></div>
      </div>
      <h3>Embed the chart</h3>
      <div class="not-prose">
        <textarea id="embed-code" readonly rows="4" class="w-full text-xs font-mono bg-zinc-950/70 border border-zinc-800 rounded-xl p-3 text-zinc-300">{esc(embed)}</textarea>
        <div class="mt-2"><button type="button" data-copy="embed-code" {BTN}>Copy embed code</button></div>
      </div>
      <h2>Related</h2>
      <ul>
{rel}
      </ul>
      <p class="text-sm text-zinc-400">Questions or corrections: <a href="mailto:contact@jonhisking.com">contact@jonhisking.com</a></p>
    </article>
{COPY_JS}'''


def _embed(path, chart, alt, label):
    return (f'<a href="{BASE}{path}"><img src="{BASE}{chart}" alt="{alt} (TokenSave)" width="1200" loading="lazy"></a>\n'
            f'<p>Source: <a href="{BASE}{path}">TokenSave, {label}</a> (CC BY 4.0)</p>')


def _doi_line(doi, mirrors):
    links = " · ".join('<a href="%s">%s</a>' % (u, n) for n, u in mirrors[1:])
    return '<p class="text-sm text-zinc-400">DOI <a href="https://doi.org/%s">%s</a> · Also on %s</p>' % (doi, doi, links)


def _head(title_h1, lead, meta, downloads, chart, chart_alt, doi=None, mirrors=None):
    doi_html = ("\n      " + _doi_line(doi, mirrors)) if doi else ""
    btns = "\n".join(f'        <a href="/data/{f}" {BTN} style="text-decoration:none">⬇ {lab}</a>' for f, lab in downloads)
    return f'''    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <p class="not-prose text-xs font-semibold uppercase tracking-wider text-violet-300"><a href="/data/" class="no-underline" style="text-decoration:none">TokenSave Data</a> · Dataset</p>
      <h1 class="text-3xl font-extrabold text-white">{title_h1}</h1>
      <p class="mt-3 text-lg text-zinc-200">{lead}</p>
      <p class="text-sm text-zinc-400">{meta}</p>{doi_html}
      <div class="not-prose flex flex-wrap gap-2 my-4">
{btns}
        <a href="#cite" {BTN} style="text-decoration:none">How to cite</a>
      </div>
      <img src="{chart}" alt="{chart_alt}" width="1200" loading="lazy">
'''


def _table(head_cells, rows_html):
    head = "".join(head_cells)
    return f'''      <div class="overflow-x-auto">
        <table>
          <thead><tr>{head}</tr></thead>
          <tbody>
{rows_html}
          </tbody>
        </table>
      </div>
'''


# ---- Dataset 5: same programs in 10 programming languages (measured 2026-10-18) ----
CODE_PATH = "/data/token-cost-by-programming-language"
CODE_MEASURED = "2026-10-18"
CODE_CHART = "/token-cost-by-programming-language-chart.png"
CODE_DOI = "10.5281/zenodo.23446563"  # concept DOI
CODE_MIRRORS = [("Zenodo", "https://zenodo.org/records/23446564"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/token-cost-by-programming-language"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/token-cost-by-programming-language"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/code")]
CODE_TITLE = "Token cost by programming language: the same programs in 10 languages on Claude, Gemini and GPT"
CODE_DESC = ("Dataset: two programs (an inventory class and Dijkstra's shortest path) written in Python, JavaScript, TypeScript, Java, Go, Rust, C++, C, PHP and Ruby "
             "with identical output, counted on Claude 5.5, Claude Haiku 4.5, Gemini and GPT. C needs 90% more GPT tokens than Python. Free CSV, CC BY 4.0.")
CODE_COLS = [("claude55", "Claude Opus/Sonnet 5.5"), ("claude45", "Claude Haiku 4.5"), ("gemini", "Gemini 3.x"), ("gpt", "GPT o200k")]


def _code_rows():
    return json.load(open(os.path.join(ROOT, "blog_data", "codedata", "combined.json"), encoding="utf-8"))


def _code_files():
    return json.load(open(os.path.join(ROOT, "blog_data", "codedata", "files.json"), encoding="utf-8"))


def code_citation():
    return f"TokenSave (2026). {CODE_TITLE} [Data set]. Zenodo. https://doi.org/{CODE_DOI}"


def write_code_files(dist):
    rows = _code_rows()
    buf = io.StringIO()
    w = csv.writer(buf)
    cols = [k for k, _ in CODE_COLS]
    w.writerow(["language", "program", "characters", "lines"] + [f"{k}_tokens" for k in cols])
    for r in rows:
        for p in ["inventory", "dijkstra", "total"]:
            src = r[p] if p != "total" else r
            w.writerow([r["name"], p, src["chars"], src["lines"]] + [src[k] for k in cols])
    open(os.path.join(dist, "data", "token-cost-by-programming-language.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=CODE_TITLE, url=BASE + CODE_PATH, license="CC BY 4.0", measured=CODE_MEASURED,
                programs={"inventory": "Inventory class: add, restock, sell, low-stock list, total value, formatted report",
                          "dijkstra": "Dijkstra's shortest path on a 6-node graph with path reconstruction"},
                tokenizers={"claude55": "Claude Opus 5.5 / Sonnet 5.5 (identical counts)", "claude45": "Claude Haiku 4.5",
                            "gemini": "Gemini 3.8 Flash", "gpt": "OpenAI o200k_base (GPT-4o and later)"},
                citation=code_citation(), rows=rows, sources=_code_files())
    open(os.path.join(dist, "data", "token-cost-by-programming-language.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def code_ld():
    return _dataset_ld(CODE_TITLE, CODE_DESC, CODE_PATH, CODE_MEASURED,
                       ["programming language tokens", "code tokens", "Python vs Java tokens", "LLM coding cost", "tokenizer", "Claude", "Gemini", "GPT"],
                       ["tokens (Claude 5.5)", "tokens (Claude Haiku 4.5)", "tokens (Gemini 3.x)", "tokens (o200k_base)", "difference vs Python (%)"],
                       "Same two programs in 10 languages with identical output; Claude from Claude Code usage minus a one-character baseline, Gemini from the Google AI Studio token counter, GPT with tiktoken",
                       CODE_CHART, [("token-cost-by-programming-language.csv", "text/csv"), ("token-cost-by-programming-language.json", "application/json")], doi=CODE_DOI, mirrors=CODE_MIRRORS)


def code_html():
    rows = _code_rows()
    by = {r["language"]: r for r in rows}
    py, c, go, js, ts, java = by["python"], by["c"], by["go"], by["javascript"], by["typescript"], by["java"]
    vs = [r["claude55_vs_gpt"] for r in rows]
    gem_vs_gpt = [round((r["gemini"] / r["gpt"] - 1) * 100) for r in rows]
    most_chars = max(rows, key=lambda r: r["chars"])
    trs = "\n".join(
        f'          <tr><td>{esc(r["name"])}</td><td class="text-right tabular-nums">{r["lines"]}</td>' + "".join(
            f'<td class="text-right tabular-nums">{r[k]:,} <span class="text-zinc-500">({_pct(r[k + "_vs_python"])})</span></td>' for k, _ in CODE_COLS) + "</tr>"
        for r in rows)
    head = ['<th>Language</th>', '<th class="text-right">Lines</th>'] + [f'<th class="text-right">{esc(n)}</th>' for _, n in CODE_COLS]
    return _head("Python vs Java vs Go vs C: how many tokens the same code costs",
                 f'<strong>The same two programs cost {py["gpt"]:,} GPT tokens in Python and {c["gpt"]:,} in C ({_pct(c["gpt_vs_python"])}).</strong> Python and Ruby were the cheapest languages on every tokenizer we tested; Go and C were the most expensive. Claude 5.5 needed {min(vs)}% to {max(vs)}% more tokens than GPT for the same code.',
                 f'Measured {CODE_MEASURED} · 10 languages · 2 programs · 4 tokenizers · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{FMT_PATH}">token cost by data format</a>',
                 [("token-cost-by-programming-language.csv", "CSV"), ("token-cost-by-programming-language.json", "JSON (with all 20 source files)")],
                 CODE_CHART, "Tokens for the same two programs in 10 programming languages on Claude, Gemini and GPT", doi=CODE_DOI, mirrors=CODE_MIRRORS) + f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Python and Ruby are the cheapest.</strong> Both programs together cost {py["gpt"]:,} GPT tokens in Python and {by["ruby"]["gpt"]:,} in Ruby. JavaScript needs {_pct(js["gpt_vs_python"])}, Java {_pct(java["gpt_vs_python"])}, Go {_pct(go["gpt_vs_python"])} and C {_pct(c["gpt_vs_python"])}.</li>
        <li><strong>The ranking holds on every tokenizer.</strong> Python and Ruby stay at the top and Go and C at the bottom on Claude 5.5, Claude Haiku 4.5, Gemini and GPT alike.</li>
        <li><strong>Claude 5.5 costs {min(vs)}% to {max(vs)}% more than GPT for the same code.</strong> The gap is largest for {esc(max(rows, key=lambda r: r["claude55_vs_gpt"])["name"])} ({_pct(max(vs))}). Gemini sits between them at {min(gem_vs_gpt)}% to {max(gem_vs_gpt)}% more than GPT.</li>
        <li><strong>Types add tokens.</strong> TypeScript needs {round((ts["gpt"] / js["gpt"] - 1) * 100)}% more GPT tokens than the same JavaScript.</li>
        <li><strong>File size is a rough guide only.</strong> {esc(most_chars["name"])} has the most characters ({most_chars["chars"]:,}), but Go and C need more tokens. Characters and lines do not map neatly onto tokens.</li>
      </ul>
      <h2>All 10 languages</h2>
      <p class="text-sm text-zinc-400">Tokens for both programs together, with the difference versus Python on the same tokenizer in brackets. Per-program counts are in the CSV.</p>
{_table(head, trs)}      <h2>Method</h2>
      <ul>
        <li>Two programs written in each language: an inventory class (add, restock, sell, a low-stock list, total value and a formatted report) and Dijkstra's shortest path on a 6-node graph with path reconstruction. Every version was compiled or run and printed exactly the same output as the Python version.</li>
        <li>Code is idiomatic for each language with no comments: for example Java uses <code>PriorityQueue</code>, Go uses <code>container/heap</code>, and C uses a simple array scan instead of a heap. All 20 source files are in the JSON download.</li>
        <li><strong>Claude:</strong> each file sent through Claude Code (<code>claude -p</code>) with a fixed one-line system prompt; reported input tokens minus the same run with a one-character message. Opus 5.5 and Sonnet 5.5 gave identical counts, and a re-run gave identical counts.</li>
        <li><strong>Gemini:</strong> Google AI Studio prompt token counter on Gemini 3.8 Flash, minus its one start token. Four files were measured twice with identical results.</li>
        <li><strong>GPT:</strong> <a href="https://github.com/openai/tiktoken">tiktoken</a> with <code>o200k_base</code>.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>Two small programs. Real projects with comments, long names or heavy boilerplate can shift the numbers; the ranking is more stable than the exact percentages.</li>
        <li>Style matters: the same language written more tersely or more verbosely will cost a different number of tokens.</li>
        <li>Input tokens only; it does not measure how well each model writes or understands each language.</li>
      </ul>
''' + _page_tail(code_citation(), _embed(CODE_PATH, CODE_CHART, "Tokens for the same code in 10 programming languages on Claude, Gemini and GPT", "token cost by programming language"),
                 [(FMT_PATH, "Token cost by data format (JSON vs CSV vs TOON)"), (MULTI_PATH, "Token cost by language on Claude, Gemini and GPT"), ("/", "Count tokens for your own code")])


# ---- Dataset 6: PDF pages vs pasted text (measured 2026-10-18) ----
PDF_PATH = "/data/pdf-token-cost"
PDF_MEASURED = "2026-10-18"
PDF_CHART = "/pdf-token-cost-chart.png"
PDF_DOI = "10.5281/zenodo.23446565"  # concept DOI
PDF_MIRRORS = [("Zenodo", "https://zenodo.org/records/23447869"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/pdf-token-cost"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/pdf-token-cost-per-page-claude-vs-gemini"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/pdf")]
PDF_TITLE = "PDF token cost per page: Claude vs Gemini, and PDF vs pasted text"
PDF_DESC = ("Dataset: input tokens for PDF pages (text, table and scanned) on Claude Opus/Sonnet 5.5, Claude Haiku 4.5 and Gemini, compared with pasting the same content as text. "
            "Gemini charges a flat 560 tokens per page; a text page costs 2,347 tokens as a PDF on Claude 5.5 but 728 pasted. Also: the same files read from disk by Codex and Cursor. Free CSV, CC BY 4.0.")


def _pdf_rows():
    return json.load(open(os.path.join(ROOT, "blog_data", "pdfdata", "combined.json"), encoding="utf-8"))


def pdf_citation():
    return f"TokenSave (2026). {PDF_TITLE} [Data set]. Zenodo. https://doi.org/{PDF_DOI}"


def _pdf_agents():
    return json.load(open(os.path.join(ROOT, "blog_data", "pdfdata", "agents", "combined.json"), encoding="utf-8"))


def write_pdf_files(dist):
    rows = _pdf_rows()
    ag = _pdf_agents()
    abuf = io.StringIO()
    aw = csv.writer(abuf)
    aw.writerow(["input", "label", "codex_avg_input_tokens", "codex_run1", "codex_run2", "codex_result", "cursor_avg_input_tokens", "cursor_run1", "cursor_run2", "cursor_result"])
    for r in ag["rows"]:
        aw.writerow([r["input"], r["label"], r["codex_avg"], r["codex_runs"][0], r["codex_runs"][1], r["codex_result"],
                     r["cursor_avg"], r["cursor_runs"][0], r["cursor_runs"][1], r["cursor_result"]])
    open(os.path.join(dist, "data", "pdf-token-cost-agents.csv"), "w", encoding="utf-8", newline="").write(abuf.getvalue())
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["input", "label", "kind", "pages", "claude55_tokens", "claude45_tokens", "gemini_tokens", "gpt_tokens", "claude55_per_page", "claude45_per_page", "gemini_per_page"])
    for r in rows:
        w.writerow([r["input"], r["label"], r["kind"], r["pages"], r["claude55"], r["claude45"], r["gemini"], "" if r["gpt"] is None else r["gpt"],
                    r["claude55_per_page"], r["claude45_per_page"], r["gemini_per_page"]])
    open(os.path.join(dist, "data", "pdf-token-cost.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    plain = json.load(open(os.path.join(ROOT, "blog_data", "pdfdata", "plain.json"), encoding="utf-8"))
    meta = dict(title=PDF_TITLE, url=BASE + PDF_PATH, license="CC BY 4.0", measured=PDF_MEASURED,
                tokenizers={"claude55": "Claude Opus 5.5 / Sonnet 5.5 (identical counts)", "claude45": "Claude Haiku 4.5",
                            "gemini": "Gemini 3.8 Flash (AI Studio)", "gpt": "OpenAI o200k_base, pasted text only"},
                citation=pdf_citation(), rows=rows, pasted_text=plain, coding_agents=ag)
    open(os.path.join(dist, "data", "pdf-token-cost.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def pdf_ld():
    return _dataset_ld(PDF_TITLE, PDF_DESC, PDF_PATH, PDF_MEASURED,
                       ["PDF tokens", "tokens per page", "Claude PDF", "Gemini PDF", "document input cost", "LLM cost"],
                       ["tokens per PDF page (Claude 5.5)", "tokens per PDF page (Claude Haiku 4.5)", "tokens per PDF page (Gemini 3.x)", "tokens for the same content as text"],
                       "A4 PDFs (text, table, scanned image; 1, 5 and 10 pages) sent to Claude Code as document blocks and uploaded to Google AI Studio; the same content pasted as text for comparison",
                       PDF_CHART, [("pdf-token-cost.csv", "text/csv"), ("pdf-token-cost-agents.csv", "text/csv"), ("pdf-token-cost.json", "application/json")], doi=PDF_DOI, mirrors=PDF_MIRRORS)


def pdf_html():
    by = {r["input"]: r for r in _pdf_rows()}
    t1, t10, tab, scan, ptxt, ptab = by["text_1p"], by["text_10p"], by["table_1p"], by["scan_1p"], by["text_page_plain"], by["table_plain"]
    pct = lambda a, b: round((a / b - 1) * 100)
    cols = [("claude55", "Claude Opus/Sonnet 5.5"), ("claude45", "Claude Haiku 4.5"), ("gemini", "Gemini 3.x"), ("gpt", "GPT o200k")]
    trs = "\n".join(
        f'          <tr><td>{esc(r["label"])}</td>' + "".join(
            f'<td class="text-right tabular-nums">{"–" if r[k] is None else format(r[k], ",")}</td>' for k, _ in cols) + "</tr>"
        for r in _pdf_rows())
    head = ['<th>Input</th>'] + [f'<th class="text-right">{esc(n)}</th>' for _, n in cols]
    agd = _pdf_agents()
    agb = agd["baseline"]
    ag = {r["input"]: r for r in agd["rows"]}
    note = lambda res: "" if res == "read correctly" else (' <span class="text-zinc-500">(' + ("failed" if res.startswith("failed") else "wrong answer" if res.startswith("wrong") else "1 of 2 runs failed") + ")</span>")
    atrs = "\n".join(
        f'          <tr><td>{esc(r["label"])}</td><td class="text-right tabular-nums">{r["codex_avg"]:,}{note(r["codex_result"])}</td><td class="text-right tabular-nums">{r["cursor_avg"]:,}{note(r["cursor_result"])}</td></tr>'
        for r in agd["rows"])
    ahead = ['<th>File</th>', '<th class="text-right">Codex (gpt-6-luna)</th>', '<th class="text-right">Cursor (free, Auto)</th>']
    return _head("How many tokens is a PDF page? Claude vs Gemini vs Codex vs Cursor",
                 f'<strong>One page of text costs {t1["claude55"]:,} tokens as a PDF on Claude 5.5 but {ptxt["claude55"]:,} when the same text is pasted ({_pct(pct(t1["claude55"], ptxt["claude55"]))}).</strong> Gemini charges a flat {t10["gemini_per_page"]} tokens per PDF page whatever is on it, so the same page costs {abs(pct(t1["gemini"], t1["claude55"]))}% less there.',
                 f'Measured {PDF_MEASURED} · text, table and scanned pages · 1 to 10 pages · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{IMG_PATH}">image token cost</a>',
                 [("pdf-token-cost.csv", "CSV"), ("pdf-token-cost-agents.csv", "CSV (Codex, Cursor)"), ("pdf-token-cost.json", "JSON")],
                 PDF_CHART, "Input tokens for one page as a PDF or as pasted text on Claude, Gemini and GPT", doi=PDF_DOI, mirrors=PDF_MIRRORS) + f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Claude reads every PDF page twice: as text and as an image.</strong> A text page costs {t1["claude55"]:,} tokens on Claude 5.5. A scanned page with no text layer costs {scan["claude55"]:,}, which is the image part alone; the rest is the extracted text.</li>
        <li><strong>Pasting text is much cheaper on Claude.</strong> The same page pasted as text costs {ptxt["claude55"]:,} tokens on Claude 5.5, {abs(pct(ptxt["claude55"], t1["claude55"]))}% less than the PDF. If you only need the words, copy them out.</li>
        <li><strong>Gemini charges a flat rate per page.</strong> Text, table and scanned pages all cost {t1["gemini"]:,} tokens, and 10 pages cost {t10["gemini"]:,}, so about {t10["gemini_per_page"]} per page.</li>
        <li><strong>On Gemini a PDF can beat pasting.</strong> Our table page costs {tab["gemini"]:,} tokens as a PDF but {ptab["gemini"]:,} pasted as CSV ({abs(pct(tab["gemini"], ptab["gemini"]))}% less as a PDF). For dense pages Gemini's flat rate is cheaper than the text itself.</li>
        <li><strong>Cost grows in a straight line with pages.</strong> 10 text pages cost {t10["claude55"]:,} tokens on Claude 5.5 (about {t10["claude55_per_page"]:,} per page) and {t10["claude45"]:,} on Claude Haiku 4.5.</li>
        <li><strong>Coding agents spend more on working out how to open a PDF than on the PDF itself.</strong> Asked to summarize a one-page PDF from disk, Codex used {ag["text_1p"]["codex_avg"]:,} input tokens and Cursor {ag["text_1p"]["cursor_avg"]:,}, against {ag["text_page_plain"]["codex_avg"]:,} and {ag["text_page_plain"]["cursor_avg"]:,} for the same text as a .txt file ({_pct(pct(ag["text_1p"]["codex_avg"], ag["text_page_plain"]["codex_avg"]))} and {_pct(pct(ag["text_1p"]["cursor_avg"], ag["text_page_plain"]["cursor_avg"]))}). Ten pages cost about the same as one.</li>
        <li><strong>Scanned PDFs broke both agents.</strong> Codex used {ag["scan_1p"]["codex_avg"]:,} tokens on average and then said it could not read the page. Cursor answered both times with a summary of content that is not in the file.</li>
      </ul>
      <h2>All inputs</h2>
      <p class="text-sm text-zinc-400">Input tokens. GPT is shown for pasted text only (see method).</p>
{_table(head, trs)}      <h2>Coding agents: Codex and Cursor</h2>
      <p>Same files, read from disk by a coding agent with the prompt &ldquo;Read the file … and summarize its full contents in one sentence.&rdquo; Each file sat alone in an empty folder; two runs per file. Numbers are total input tokens for the whole agent session, including cached tokens and the agent&rsquo;s own instructions, so they are not comparable with the Claude and Gemini counts above. With no file at all the same setup used {agb["codex"]:,} (Codex) and {agb["cursor"]:,} (Cursor) tokens.</p>
{_table(ahead, atrs)}      <ul>
        <li><strong>How they read PDFs:</strong> neither agent looked at the pages as images. Codex loaded a PDF skill, tried Python libraries that were not installed, then extracted the text with <code>pdftotext</code>. Cursor read a PDF skill file and then used its built-in file reader, which returns the text layer.</li>
        <li><strong>Codex varies a lot between runs.</strong> The same 10-page PDF took {ag["text_10p"]["codex_runs"][0]:,} tokens once and {ag["text_10p"]["codex_runs"][1]:,} the next time, depending on how many tools it tried first. Cursor&rsquo;s two runs were within 2% of each other on every text and table PDF.</li>
        <li><strong>The scanned page has no text layer.</strong> Codex could not find an OCR tool and said so. Cursor&rsquo;s file reader returned an empty page, its shell commands were not approved in print mode, and it still answered with invented text (once a &ldquo;handwritten note&rdquo;, once a sentence about a crow); the page is the same garden text as the other files.</li>
      </ul>
      <h2>Method</h2>
      <ul>
        <li>A4 PDFs made with ReportLab: one page of English prose (about 420 words), the same page repeated to 5 and 10 pages, a page with a 35-row table, and a scanned version of the text page (rendered at 150 dpi and placed as an image with no text layer).</li>
        <li><strong>Claude:</strong> each PDF sent through Claude Code (<code>claude -p</code>, stream-json input) as a document block with a one-character message; input tokens minus the same run without the PDF. Opus 5.5 and Sonnet 5.5 gave identical counts.</li>
        <li><strong>Gemini:</strong> per-file token count shown by Google AI Studio for Gemini 3.8 Flash after uploading each PDF. Pasted text was measured with the prompt counter minus its one start token.</li>
        <li><strong>GPT:</strong> OpenAI bills PDF input as extracted text plus an image of each page, which we could not reproduce without the API, so GPT appears only for pasted text (tiktoken, <code>o200k_base</code>).</li>
        <li><strong>Codex:</strong> Codex CLI 0.162 on Windows, ChatGPT plan login, model gpt-6-luna at low reasoning effort, <code>codex exec --json -s read-only</code>; input tokens from the final usage report.</li>
        <li><strong>Cursor:</strong> Cursor Agent CLI on Windows, free Hobby plan, model Auto, <code>cursor-agent -p --output-format stream-json</code> with default permissions; input plus cache-read tokens from the result event.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>One page design. Pages with more text, small fonts or many images will cost more on Claude; Gemini's per-page rate should stay flat.</li>
        <li>Default settings; Gemini's media resolution option changes its per-page count.</li>
        <li>Input tokens only; the price per token differs by model.</li>
        <li>Codex and Cursor: two runs per file on one machine with the tools that happened to be installed; an agent with an OCR tool or shell access would behave differently.</li>
      </ul>
''' + _page_tail(pdf_citation(), _embed(PDF_PATH, PDF_CHART, "Input tokens for one PDF page on Claude and Gemini, and the same page pasted as text", "PDF token cost per page"),
                 [(IMG_PATH, "Image input token cost by resolution"), (FMT_PATH, "Token cost by data format"), ("/", "Count tokens for your own text")])


# ---- Dataset 7: Claude effort levels (measured 2026-10-09) ----
EFF_PATH = "/data/claude-effort-cost"
EFF_MEASURED = "2026-10-09"
EFF_CHART = "/claude-effort-cost-chart.png"
EFF_DOI = "10.5281/zenodo.23446567"  # concept DOI
EFF_MIRRORS = [("Zenodo", "https://zenodo.org/records/23446568"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/claude-effort-cost"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/claude-effort-levels-tokens-time-and-cost"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/effort")]
EFF_TITLE = "Claude effort levels: tokens, time and cost for the same coding task"
EFF_DESC = ("Dataset: the same coding prompt run in Claude Code at every effort level of Claude Opus 5.5 (low to max) and at medium and high on Sonnet 5.5, "
            "with time, output tokens, total tokens, API-equivalent cost and lines of code. Max used 160,033 output tokens and $5.25 against 6,299 and $0.56 at medium. Free CSV, CC BY 4.0.")


def _eff():
    return json.load(open(os.path.join(ROOT, "blog_data", "effortdata", "combined.json"), encoding="utf-8"))


def eff_citation():
    return f"TokenSave (2026). {EFF_TITLE} [Data set]. Zenodo. https://doi.org/{EFF_DOI}"


def write_eff_files(dist):
    d = _eff()
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["model", "effort", "seconds", "output_tokens", "total_tokens", "cost_usd", "code_lines"])
    for r in d["rows"]:
        w.writerow([r["model"], r["effort"], r["seconds"], r["output_tokens"], r["total_tokens"], f'{r["cost_usd"]:.2f}', r["code_lines"]])
    open(os.path.join(dist, "data", "claude-effort-cost.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=EFF_TITLE, url=BASE + EFF_PATH, license="CC BY 4.0", measured=EFF_MEASURED, tool=d["tool"], prompt=d["prompt"],
                citation=eff_citation(), rows=d["rows"])
    open(os.path.join(dist, "data", "claude-effort-cost.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def eff_ld():
    return _dataset_ld(EFF_TITLE, EFF_DESC, EFF_PATH, EFF_MEASURED,
                       ["Claude effort", "reasoning effort", "thinking tokens", "Claude Opus 5.5 cost", "Claude Code cost", "LLM cost"],
                       ["time (seconds)", "output tokens", "total tokens", "cost (USD, API prices)", "lines of code"],
                       "Same prompt run once per effort level in Claude Code; tokens and cost from ccusage at API prices, time from start and end timestamps",
                       EFF_CHART, [("claude-effort-cost.csv", "text/csv"), ("claude-effort-cost.json", "application/json")], doi=EFF_DOI, mirrors=EFF_MIRRORS)


def _dur(s):
    return f"{s} s" if s < 60 else f"{s // 60} min {s % 60} s"


def eff_html():
    d = _eff()
    by = {(r["model_name"], r["effort"]): r for r in d["rows"]}
    lo, me, hi, xh, mx = (by[("Opus 5.5", k)] for k in ["low", "medium", "high", "xhigh", "max"])
    sme, shi = by[("Sonnet 5.5", "medium")], by[("Sonnet 5.5", "high")]
    pct = lambda a, b: round((a / b - 1) * 100)
    trs = "\n".join(
        f'          <tr><td>{esc(r["model_name"])} · {esc(r["effort"])}</td><td class="text-right tabular-nums">{_dur(r["seconds"])}</td>'
        f'<td class="text-right tabular-nums">{r["output_tokens"]:,}</td><td class="text-right tabular-nums">{r["total_tokens"]:,}</td>'
        f'<td class="text-right tabular-nums">${r["cost_usd"]:.2f}</td><td class="text-right tabular-nums">{r["code_lines"]:,}</td></tr>'
        for r in d["rows"])
    head = ['<th>Model · effort</th>', '<th class="text-right">Time</th>', '<th class="text-right">Output tokens</th>', '<th class="text-right">Total tokens</th>', '<th class="text-right">Cost</th>', '<th class="text-right">Lines of code</th>']
    return _head("Claude effort levels: what low, medium, high, xhigh and max cost",
                 f'<strong>The same coding task used {me["output_tokens"]:,} output tokens and ${me["cost_usd"]:.2f} at medium effort on Claude Opus 5.5, and {mx["output_tokens"]:,} tokens and ${mx["cost_usd"]:.2f} at max.</strong> High cost only {pct(hi["cost_usd"], me["cost_usd"])}% more than medium; the jump starts at xhigh.',
                 f'Measured {EFF_MEASURED} · Opus 5.5 at 5 levels, Sonnet 5.5 at 2 · License <a href="{LICENSE}">CC BY 4.0</a> · Write-up: <a href="/blog/claude-opus-5-5-effort">Claude Opus 5.5 effort levels tested</a>',
                 [("claude-effort-cost.csv", "CSV"), ("claude-effort-cost.json", "JSON")],
                 EFF_CHART, "Output tokens and cost for the same task at each Claude effort level", doi=EFF_DOI, mirrors=EFF_MIRRORS) + f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Low and medium are close.</strong> Low cost {abs(pct(lo["cost_usd"], me["cost_usd"]))}% less than medium (${lo["cost_usd"]:.2f} vs ${me["cost_usd"]:.2f}) and took {_dur(lo["seconds"])} instead of {_dur(me["seconds"])}, but built the plainest result.</li>
        <li><strong>High is the best value step.</strong> Output tokens rose {pct(hi["output_tokens"], me["output_tokens"])}% ({me["output_tokens"]:,} to {hi["output_tokens"]:,}) but cost only {pct(hi["cost_usd"], me["cost_usd"])}% more, because most of each request is input that does not change.</li>
        <li><strong>Costs jump from xhigh.</strong> xhigh cost {pct(xh["cost_usd"], me["cost_usd"])}% more than medium and max {pct(mx["cost_usd"], me["cost_usd"])}% more. Max used {mx["output_tokens"]:,} output tokens against {me["output_tokens"]:,} at medium and took {_dur(mx["seconds"])}.</li>
        <li><strong>Sonnet 5.5 is cheaper per run, not just per token.</strong> At the same effort it used {abs(pct(sme["output_tokens"], me["output_tokens"]))}% fewer output tokens than Opus 5.5 and cost {abs(pct(sme["cost_usd"], me["cost_usd"]))}% less at medium and {abs(pct(shi["cost_usd"], hi["cost_usd"]))}% less at high.</li>
      </ul>
      <h2>All runs</h2>
{_table(head, trs)}      <h2>Method</h2>
      <ul>
        <li>Prompt, word for word: “{esc(d["prompt"])}”</li>
        <li>Run once per effort level in Claude Code (<code>claude -p --effort …</code>), each in its own empty folder.</li>
        <li>Tokens and cost from <a href="https://github.com/ryoppippi/ccusage">ccusage</a> at API prices; time from start and end timestamps; lines counted in the finished <code>index.html</code>.</li>
        <li>All seven games ran without errors and had every requested feature; screenshots and a review of each are in the <a href="/blog/claude-opus-5-5-effort">write-up</a>.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>One run per level and one task. Runs vary, especially at high effort levels; treat the numbers as an order of magnitude, not a fixed price.</li>
        <li>Costs are API-equivalent. On a Pro or Max plan the same runs use up your usage limit instead of money.</li>
        <li>Max effort tried to run an automated test that needed permission, which added time.</li>
      </ul>
''' + _page_tail(eff_citation(), _embed(EFF_PATH, EFF_CHART, "Output tokens and cost for the same task at each Claude effort level", "Claude effort levels"),
                 [("/blog/claude-opus-5-5-effort", "Claude Opus 5.5 effort levels tested (full write-up)"), ("/blog/claude-sonnet-5-5-vs-opus-5-5", "Sonnet 5.5 vs Opus 5.5"), ("/agents", "Coding agent cost calculator")])


# ---- Dataset 8: Claude Code vs Codex — startup tokens, MCP tools, same coding task (measured 2026-10-18) ----
AGT_PATH = "/data/claude-code-vs-codex-tokens"
AGT_MEASURED = "2026-10-18"
AGT_CHART = "/claude-code-vs-codex-tokens-chart.png"
AGT_DOI = "10.5281/zenodo.23448342"  # concept DOI
AGT_MIRRORS = [("Zenodo", "https://zenodo.org/records/23448343"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/claude-code-vs-codex-tokens"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/claude-code-vs-codex-startup-and-task-tokens"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/agents")]
AGT_TITLE = "Claude Code vs Codex: startup tokens, MCP tools and the same coding task"
AGT_DESC = ("Dataset: input tokens Claude Code and Codex use before any work (a one-word reply), what adding 1 to 30 MCP tools adds, and tokens, time and output "
            "for the same browser-game task at medium effort. Free CSV, CC BY 4.0.")
AGT_TOOLS = [("claude_code", "Claude Code (Opus 5.5)"), ("codex", "Codex (gpt-6-luna)")]


def _agt():
    d = json.load(open(os.path.join(ROOT, "blog_data", "agentbase", "combined.json"), encoding="utf-8"))
    keep = {k for k, _ in AGT_TOOLS}
    d["rows"] = [r for r in d["rows"] if r["tool"] in keep]
    return d


def _agt_task_avg(d):
    out = {}
    for k, _ in AGT_TOOLS:
        rs = [r for r in d["task"]["rows"] if r["tool"] == k]
        avg = lambda f: round(sum(r[f] for r in rs) / len(rs))
        out[k] = dict(input=avg("input_tokens"), output=avg("output_tokens"), seconds=avg("seconds"), lines=avg("file_lines"),
                      cost=(round(sum(r["api_cost_usd"] for r in rs) / len(rs), 2) if rs[0]["api_cost_usd"] is not None else None), runs=rs)
    return out


def agt_citation():
    return f"TokenSave (2026). {AGT_TITLE} [Data set]. Zenodo. https://doi.org/{AGT_DOI}"


def write_agt_files(dist):
    d = _agt()
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["test", "tool", "model", "mcp_tools", "run", "input_tokens", "cached_input_tokens", "output_tokens", "seconds", "api_cost_usd", "file_lines"])
    for r in d["rows"]:
        for i, v in enumerate([r["run1"], r["run2"]], 1):
            w.writerow(["startup", r["tool"], r["model"], r["mcp_tools"], i, v, "", "", "", "", ""])
    for r in d["task"]["rows"]:
        w.writerow(["same_task", r["tool"], r["model"], 0, r["run"], r["input_tokens"], r["cached_input_tokens"], r["output_tokens"], r["seconds"],
                    "" if r["api_cost_usd"] is None else f'{r["api_cost_usd"]:.2f}', r["file_lines"]])
    open(os.path.join(dist, "data", "claude-code-vs-codex-tokens.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=AGT_TITLE, url=BASE + AGT_PATH, license="CC BY 4.0", measured=AGT_MEASURED, citation=agt_citation(),
                startup=dict(prompt=d["prompt"], mcp_server=d["mcp_server"], full_definition_tokens_o200k=d["full_definition_tokens_o200k"],
                             codex_tool_use_check=d["codex_tool_use_check"], rows=d["rows"]),
                same_task=d["task"])
    open(os.path.join(dist, "data", "claude-code-vs-codex-tokens.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def agt_ld():
    return _dataset_ld(AGT_TITLE, AGT_DESC, AGT_PATH, AGT_MEASURED,
                       ["Claude Code vs Codex", "coding agent tokens", "MCP token overhead", "system prompt tokens", "Claude Code cost", "Codex cost"],
                       ["input tokens for a one-word reply", "input tokens added per MCP tool", "input tokens for the same task", "output tokens", "time (seconds)"],
                       "Claude Code and Codex CLI run on the same Windows machine; startup with 0, 1, 10 and 30 tools from a self-written MCP server; the same browser-game prompt at medium effort, two runs each",
                       AGT_CHART, [("claude-code-vs-codex-tokens.csv", "text/csv"), ("claude-code-vs-codex-tokens.json", "application/json")], doi=AGT_DOI, mirrors=AGT_MIRRORS)


def agt_html():
    d = _agt()
    base = {(r["tool"], r["mcp_tools"]): r for r in d["rows"]}
    t = _agt_task_avg(d)
    cc, cx = t["claude_code"], t["codex"]
    pct = lambda a, b: round((a / b - 1) * 100)
    b_cc, b_cx = base[("claude_code", 0)]["avg"], base[("codex", 0)]["avg"]
    full30 = d["full_definition_tokens_o200k"]["30"]
    strs = "\n".join(
        f'          <tr><td>{n} MCP tool{"s" if n != 1 else ""}</td>' + "".join(
            f'<td class="text-right tabular-nums">{base[(k, n)]["avg"]:,}' + ("" if n == 0 else f' <span class="text-zinc-500">(+{base[(k, n)]["added_vs_no_mcp"]:,})</span>') + "</td>" for k, _ in AGT_TOOLS) + "</tr>"
        for n in [0, 1, 10, 30])
    shead = ['<th>Setup</th>'] + [f'<th class="text-right">{esc(n)}</th>' for _, n in AGT_TOOLS]
    ttrs = "\n".join(
        f'          <tr><td>{esc(dict(AGT_TOOLS)[r["tool"]])} · run {r["run"]}</td><td class="text-right tabular-nums">{r["input_tokens"]:,}</td><td class="text-right tabular-nums">{r["output_tokens"]:,}</td>'
        f'<td class="text-right tabular-nums">{r["seconds"]} s</td><td class="text-right tabular-nums">{r["file_lines"]:,}</td><td class="text-right tabular-nums">{"–" if r["api_cost_usd"] is None else "$" + format(r["api_cost_usd"], ".2f")}</td></tr>'
        for r in d["task"]["rows"])
    thead = ['<th>Run</th>', '<th class="text-right">Input tokens</th>', '<th class="text-right">Output tokens</th>', '<th class="text-right">Time</th>', '<th class="text-right">Lines in index.html</th>', '<th class="text-right">API cost</th>']
    return _head("Claude Code vs Codex: how many tokens they use before and during work",
                 f'<strong>Before doing anything, Claude Code sends {b_cc:,} input tokens and Codex {b_cx:,}.</strong> On the same browser-game task Codex used {abs(pct(cx["input"], cc["input"]))}% fewer input tokens and {abs(pct(cx["output"], cc["output"]))}% fewer output tokens than Claude Code. Adding 30 MCP tools barely changed either.',
                 f'Measured {AGT_MEASURED} · Claude Code 2.1 and Codex CLI 0.162 · 2 runs each · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{EFF_PATH}">Claude effort levels</a>',
                 [("claude-code-vs-codex-tokens.csv", "CSV"), ("claude-code-vs-codex-tokens.json", "JSON")],
                 AGT_CHART, "Startup input tokens and the same coding task on Claude Code and Codex", doi=AGT_DOI, mirrors=AGT_MIRRORS) + f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Claude Code starts {pct(b_cc, b_cx)}% heavier.</strong> A one-word reply costs {b_cc:,} input tokens in Claude Code and {b_cx:,} in Codex. That fixed amount is sent again with every request, so it adds up over a session even though most of it is cached.</li>
        <li><strong>Adding MCP tools barely changed startup tokens.</strong> The full definitions of our 30 test tools are {full30:,} tokens, but adding them raised Claude Code by only {base[("claude_code", 30)]["added_vs_no_mcp"]:,} tokens (about {round(base[("claude_code", 30)]["added_vs_no_mcp"] / 30)} per tool) and Codex by 0. Both now load a tool&rsquo;s details only when it is needed.</li>
        <li><strong>Using the tools is what costs.</strong> Asked to list the 10 tracker tools and call one, Codex used {d["codex_tool_use_check"]["input_tokens"]:,} input tokens, {pct(d["codex_tool_use_check"]["input_tokens"], b_cx)}% more than its plain startup.</li>
        <li><strong>Same task, about half the tokens on Codex.</strong> The browser game took Claude Code {cc["input"]:,} input and {cc["output"]:,} output tokens on average ({cc["seconds"]} s, ${cc["cost"]:.2f} at API prices) and Codex {cx["input"]:,} input and {cx["output"]:,} output tokens ({cx["seconds"]} s). All four games worked.</li>
        <li><strong>Claude Code wrote more code.</strong> Its games averaged {cc["lines"]} lines against {cx["lines"]} for Codex, which wrote denser code with fewer line breaks; both had every requested feature.</li>
      </ul>
      <h2>Startup tokens and MCP tools</h2>
      <p class="text-sm text-zinc-400">Input tokens for the prompt &ldquo;{esc(d["prompt"])}&rdquo;, average of two runs; in brackets, the increase over no MCP server.</p>
{_table(shead, strs)}      <h2>The same coding task</h2>
      <p class="text-sm text-zinc-400">Prompt, word for word: &ldquo;{esc(d["task"]["prompt"])}&rdquo;</p>
{_table(thead, ttrs)}      <h2>Method</h2>
      <ul>
        <li>Both tools on the same Windows laptop, each run in its own empty folder.</li>
        <li><strong>Claude Code 2.1.295</strong> with its default model (Opus 5.5) on a Max plan: <code>claude -p --output-format json</code>, MCP servers only from <code>--mcp-config</code> with <code>--strict-mcp-config</code>; the task at <code>--effort medium</code> with <code>--permission-mode acceptEdits</code>. Input tokens are input + cache creation + cache read; the cost is Claude Code&rsquo;s own API-price figure.</li>
        <li><strong>Codex CLI 0.162</strong> with its default model (gpt-6-luna) on a ChatGPT plan: <code>codex exec --json</code>, reasoning effort low for the startup test and medium for the task; the MCP server added with <code>-c mcp_servers.…</code>. Input tokens include cached tokens. No price is shown because Codex reports none on a ChatGPT plan.</li>
        <li><strong>MCP test server:</strong> a small stdio server we wrote that exposes 1, 10 or 30 tracker tools (create, update, list issue and so on), each with a one-sentence description and a five-field input schema.</li>
        <li>Each finished game was opened in a headless browser: no errors, and two levels, a score and three lives on screen.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>Two runs per setting and one task. Claude Code&rsquo;s two task runs differed by {abs(pct(cc["runs"][0]["input_tokens"], cc["runs"][1]["input_tokens"]))}% in input tokens.</li>
        <li>Default models differ (Opus 5.5 vs gpt-6-luna), and the price per token differs too, so fewer tokens does not automatically mean cheaper.</li>
        <li>Startup tokens include each tool&rsquo;s installed skills and plugins on this machine; a fresh install may start lower.</li>
        <li>Cursor will be added when its free-plan limit resets.</li>
      </ul>
''' + _page_tail(agt_citation(), _embed(AGT_PATH, AGT_CHART, "Startup input tokens and the same coding task on Claude Code and Codex", "Claude Code vs Codex tokens"),
                 [(EFF_PATH, "Claude effort levels: tokens, time and cost"), (PDF_PATH, "PDF token cost, including Codex and Cursor"), ("/claude-code-usage", "Check your own Claude Code and Codex usage")])


# ---- Dataset 9: web search in Claude Code and Codex (measured 2026-10-18) ----
AGS_PATH = "/data/ai-agent-web-search-tokens"
AGS_MEASURED = "2026-10-18"
AGS_CHART = "/ai-agent-web-search-tokens-chart.png"
AGS_DOI = "10.5281/zenodo.23449842"  # concept DOI
AGS_MIRRORS = [("Zenodo", "https://zenodo.org/records/23449843"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/ai-agent-web-search-tokens"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/ai-web-search-tokens-claude-code-vs-codex"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/search")]
AGS_TITLE = "Web search in Claude Code and Codex: tokens, searches and sources per question"
AGS_DESC = ("Dataset: four kinds of question asked with web search on in Claude Code and Codex, two runs each: input and output tokens, number of searches and page opens, "
            "time, the sites seen in results and the sites cited in the answer, plus the same questions with no tools. Free CSV, CC BY 4.0.")
AGS_TOOLS = [("claude_code", "Claude Code (Opus 5.5)"), ("codex", "Codex (gpt-6-luna)")]
AGS_QS = ["q1_fact", "q2_news", "q3_compare", "q4_geo"]


def _ags():
    return json.load(open(os.path.join(ROOT, "blog_data", "agentsearch", "combined.json"), encoding="utf-8"))


def _ags_avg(d, tool, q, search):
    rs = [r for r in d["rows"] if r["tool"] == tool and r["question"] == q and r["search"].startswith(search)]
    a = lambda f: round(sum(r[f] for r in rs) / len(rs))
    seen = {}
    for r in rs:
        for i, dm in enumerate(r["domains_seen_top"]):
            seen[dm] = seen.get(dm, 0) + (8 - i)
    cited = sorted({c for r in rs for c in r["domains_cited"]})
    return dict(input=a("input_tokens"), output=a("output_tokens"), helper=a("helper_model_input_tokens"), searches=sum(r["searches"] for r in rs) / len(rs),
                opens=sum(r["page_opens"] for r in rs) / len(rs), seconds=a("seconds"), seen_n=a("domains_seen_count"),
                seen_top=[k for k, _ in sorted(seen.items(), key=lambda kv: -kv[1])[:3]], cited=cited, runs=rs)


def ags_citation():
    return f"TokenSave (2026). {AGS_TITLE} [Data set]. Zenodo. https://doi.org/{AGS_DOI}"


def write_ags_files(dist):
    d = _ags()
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["tool", "question", "question_type", "search", "run", "input_tokens", "output_tokens", "helper_model_input_tokens", "searches", "page_opens", "seconds",
                "domains_seen_count", "domains_seen_top", "domains_cited"])
    for r in d["rows"]:
        w.writerow([r["tool"], r["question"], r["question_type"], r["search"], r["run"], r["input_tokens"], r["output_tokens"], r["helper_model_input_tokens"],
                    r["searches"], r["page_opens"], r["seconds"], r["domains_seen_count"], " ".join(r["domains_seen_top"]), " ".join(r["domains_cited"])])
    open(os.path.join(dist, "data", "ai-agent-web-search-tokens.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=AGS_TITLE, url=BASE + AGS_PATH, license="CC BY 4.0", measured=AGS_MEASURED, citation=ags_citation(), questions=d["questions"], rows=d["rows"])
    open(os.path.join(dist, "data", "ai-agent-web-search-tokens.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def ags_ld():
    return _dataset_ld(AGS_TITLE, AGS_DESC, AGS_PATH, AGS_MEASURED,
                       ["AI web search tokens", "Claude Code web search", "Codex web search", "search cost", "AI citations", "GEO"],
                       ["input tokens per question", "output tokens", "web searches", "page opens", "time (seconds)", "domains seen", "domains cited"],
                       "Claude Code and Codex CLI on the same Windows machine at medium effort; four English questions, web search on and all tools off, two runs each",
                       AGS_CHART, [("ai-agent-web-search-tokens.csv", "text/csv"), ("ai-agent-web-search-tokens.json", "application/json")], doi=AGS_DOI, mirrors=AGS_MIRRORS)


def ags_html():
    d = _ags()
    qs = d["questions"]
    A = {(t, q, s): _ags_avg(d, t, q, s) for t, _ in AGS_TOOLS for q in AGS_QS for s in ["on", "off"]}
    pct = lambda a, b: round((a / b - 1) * 100)
    fmt1 = lambda x: f"{x:g}"
    cc1, cx1 = A[("claude_code", "q1_fact", "on")], A[("codex", "q1_fact", "on")]
    cx_up = [pct(A[("codex", q, "on")]["input"], A[("codex", q, "off")]["input"]) for q in AGS_QS]
    cc_all = [A[("claude_code", q, "on")]["input"] for q in AGS_QS]
    cx_all = [A[("codex", q, "on")]["input"] for q in AGS_QS]
    helper_share = [round(A[("claude_code", q, "on")]["helper"] / A[("claude_code", q, "on")]["input"] * 100) for q in AGS_QS]
    trs = "\n".join(
        f'          <tr><td>{esc(qs[q]["type"])}</td><td>{esc(dict(AGS_TOOLS)[t])}</td>'
        f'<td class="text-right tabular-nums">{A[(t, q, "on")]["input"]:,}</td><td class="text-right tabular-nums">{A[(t, q, "on")]["output"]:,}</td>'
        f'<td class="text-right tabular-nums">{fmt1(A[(t, q, "on")]["searches"])} / {fmt1(A[(t, q, "on")]["opens"])}</td>'
        f'<td class="text-right tabular-nums">{A[(t, q, "on")]["seconds"]} s</td><td class="text-right tabular-nums">{A[(t, q, "off")]["input"]:,}</td></tr>'
        for q in AGS_QS for t, _ in AGS_TOOLS)
    head = ['<th>Question</th>', '<th>Tool</th>', '<th class="text-right">Input tokens</th>', '<th class="text-right">Output tokens</th>',
            '<th class="text-right">Searches / page opens</th>', '<th class="text-right">Time</th>', '<th class="text-right">Input, no tools</th>']
    srs = "\n".join(
        f'          <tr><td>{esc(qs[q]["type"])}<br><span class="text-zinc-500">{esc(dict(AGS_TOOLS)[t].split(" (")[0])}</span></td><td class="text-right tabular-nums">{A[(t, q, "on")]["seen_n"]}</td>'
        f'<td style="white-space:normal;min-width:10rem">{esc(", ".join(A[(t, q, "on")]["seen_top"]))}</td><td style="white-space:normal;min-width:10rem">{esc(", ".join(A[(t, q, "on")]["cited"]))}</td></tr>'
        for q in AGS_QS for t, _ in AGS_TOOLS)
    shead = ['<th>Question · tool</th>', '<th class="text-right">Sites seen</th>', '<th>Most seen in results</th>', '<th>Cited in the answer</th>']
    qlist = "\n".join(f'        <li><strong>{esc(qs[q]["type"])}:</strong> &ldquo;{esc(qs[q]["prompt"])}&rdquo;</li>' for q in AGS_QS)
    return _head("How many tokens does an AI web search cost? Claude Code vs Codex",
                 f'<strong>With web search on, a one-line fact question cost {cc1["input"]:,} input tokens in Claude Code and {cx1["input"]:,} in Codex.</strong> Across four kinds of question Claude Code used {min(cc_all):,} to {max(cc_all):,} input tokens and Codex {min(cx_all):,} to {max(cx_all):,}.',
                 f'Measured {AGS_MEASURED} · 4 questions · search on, 2 runs each · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{AGT_PATH}">Claude Code vs Codex startup tokens</a>',
                 [("ai-agent-web-search-tokens.csv", "CSV"), ("ai-agent-web-search-tokens.json", "JSON")],
                 AGS_CHART, "Input tokens per question with web search on, Claude Code vs Codex", doi=AGS_DOI, mirrors=AGS_MIRRORS) + f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Search is the expensive part of an answer.</strong> With every tool off, the same questions cost Codex {min(A[("codex", q, "off")]["input"] for q in AGS_QS):,} to {max(A[("codex", q, "off")]["input"] for q in AGS_QS):,} input tokens; turning search on added {min(cx_up)}% to {max(cx_up)}%.</li>
        <li><strong>Claude Code runs a second model for the web.</strong> During searches and page reads a smaller Claude model (Haiku) processed the results; that helper accounted for {min(helper_share)}% to {max(helper_share)}% of Claude Code&rsquo;s input tokens.</li>
        <li><strong>Research-style questions cost the most.</strong> The tokenizer question took Claude Code {A[("claude_code", "q4_geo", "on")]["input"]:,} input tokens on average with {fmt1(A[("claude_code", "q4_geo", "on")]["searches"])} searches and {fmt1(A[("claude_code", "q4_geo", "on")]["opens"])} page opens.</li>
        <li><strong>Different tools look at different web.</strong> For the news question Codex&rsquo;s results were led by {esc(A[("codex", "q2_news", "on")]["seen_top"][0])} and Claude Code&rsquo;s by {esc(A[("claude_code", "q2_news", "on")]["seen_top"][0])}, and the two cited almost no sources in common. For prices both cited only the official pages.</li>
        <li><strong>Without search both tools declined the news question</strong> instead of guessing. On the price question Claude Code said it was answering from memory; Codex named the pricing page as its source although it had not opened it.</li>
        <li><strong>Turning search off is not simple.</strong> With only the search tool blocked, Claude Code fetched pages with shell commands and Codex used other built-in tools to reach the web; we had to switch off every tool for the no-search runs.</li>
      </ul>
      <h2>Tokens and searches per question</h2>
      <p class="text-sm text-zinc-400">Averages of two runs with web search on. The last column is the same question with all tools switched off, for reference.</p>
{_table(head, trs)}      <h2>Sites seen and cited</h2>
      <p class="text-sm text-zinc-400">Unique sites in the search results and fetched pages (average per run), the sites that came up most, and every site cited in the final answers.</p>
{_table(shead, srs)}      <h2>Questions</h2>
      <ul>
{qlist}
      </ul>
      <h2>Method</h2>
      <ul>
        <li>Both tools on the same Windows laptop, effort medium, each run in its own empty folder, prompts sent through standard input.</li>
        <li><strong>Claude Code 2.1.295</strong> (Opus 5.5, Max plan): <code>claude -p --output-format stream-json --verbose --allowedTools WebSearch WebFetch</code> with no MCP servers. Input tokens are summed over every model in the run, including the helper model that reads fetched pages.</li>
        <li><strong>Codex CLI 0.162</strong> (gpt-6-luna, ChatGPT plan): <code>codex --search exec --json</code>. Searches and page opens are the web-search items in the log.</li>
        <li><strong>No tools:</strong> Claude Code with <code>--tools ""</code>; Codex with <code>-c web_search="disabled"</code> and apps, plugins, in-app browser and skill search disabled.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>Four English questions, two runs each, on one day; search results change over time, and runs varied (Claude Code&rsquo;s two research runs differed by {abs(pct(A[("claude_code", "q4_geo", "on")]["runs"][0]["input_tokens"], A[("claude_code", "q4_geo", "on")]["runs"][1]["input_tokens"]))}%).</li>
        <li>Default models and per-token prices differ, and most Claude Code input is cached, so token counts are not costs.</li>
        <li>&ldquo;No tools&rdquo; removes Claude Code&rsquo;s built-in tool definitions as well as search, so it is a lower bound, not the cost of search alone.</li>
        <li>English questions only; the same questions in Korean, Japanese, Spanish and Ukrainian are in <a href="{AGL_PATH}">Claude web search by language</a>. Cursor will be added later.</li>
      </ul>
''' + _page_tail(ags_citation(), _embed(AGS_PATH, AGS_CHART, "Input tokens per question with web search on, Claude Code vs Codex", "AI web search tokens"),
                 [(AGT_PATH, "Claude Code vs Codex: startup tokens and the same coding task"), (PDF_PATH, "PDF token cost per page"), ("/claude-code-usage", "Check your own Claude Code and Codex usage")])


# ---- Dataset 10: AI web search by question language (measured 2026-10-18; v2 adds Codex and local topics) ----
AGL_PATH = "/data/claude-web-search-by-language"
AGL_MEASURED = "2026-10-18"
AGL_CHART = "/claude-web-search-by-language-chart.png"
AGL_DOI = "10.5281/zenodo.23451506"  # concept DOI
AGL_MIRRORS = [("Zenodo", "https://zenodo.org/records/23452537"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/claude-web-search-by-language"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/claude-web-search-by-language"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/search-language")]
AGL_TITLE = "AI web search by language: what Claude Code and Codex search for, and cite, in 5 languages"
AGL_DESC = ("Dataset: Claude Code and Codex answering the same questions in English, Korean, Japanese, Spanish and Ukrainian with web search on, "
            "plus local-topic questions about Seoul, Tokyo, Madrid and Kyiv asked in the local language and in English: the language of every search query, "
            "every cited link and its language, the answer language, tokens, searches and time. Free CSV, CC BY 4.0.")
AGL_LANGS = [("en", "English"), ("ko", "Korean"), ("ja", "Japanese"), ("es", "Spanish"), ("uk", "Ukrainian")]
AGL_QS = ["q1_fact", "q2_news", "q3_compare", "q4_geo"]
AGL_LQS = ["l1_fare", "l2_news", "l3_food"]
AGL_COUNTRIES = [("ko", "South Korea", "Seoul"), ("ja", "Japan", "Tokyo"), ("es", "Spain", "Madrid"), ("uk", "Ukraine", "Kyiv")]


def _agl():
    return json.load(open(os.path.join(ROOT, "blog_data", "agentsearchlang", "combined.json"), encoding="utf-8"))


def agl_citation():
    return f"TokenSave (2026). {AGL_TITLE} [Data set]. Zenodo. https://doi.org/{AGL_DOI}"


AGL_COLS = ["tool", "topic", "ask_language", "topic_country", "question", "question_type", "run", "input_tokens", "output_tokens", "search_queries_count",
            "queries_in_english", "queries_in_ask_language", "queries_in_topic_language", "page_opens", "seconds", "cited_links", "cited_in_ask_language",
            "cited_in_topic_language", "cited_english", "cited_other_language", "answer_language"]


def write_agl_files(dist):
    d = _agl()
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(AGL_COLS + ["search_queries", "domains_cited"])
    for r in d["rows"]:
        w.writerow([("" if r[c] is None else r[c]) for c in AGL_COLS] + [" | ".join(r["search_queries"]), " ".join(r["domains_cited"])])
    open(os.path.join(dist, "data", "claude-web-search-by-language.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=AGL_TITLE, url=BASE + AGL_PATH, license="CC BY 4.0", measured=AGL_MEASURED, version=2, citation=agl_citation(), tools=d["tools"],
                question_types=d["question_types"], prompts=d["prompts"], rows=d["rows"])
    open(os.path.join(dist, "data", "claude-web-search-by-language.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def agl_ld():
    return _dataset_ld(AGL_TITLE, AGL_DESC, AGL_PATH, AGL_MEASURED,
                       ["AI web search", "Claude Code", "Codex", "multilingual search", "search query language", "AI citations", "Korean", "Japanese", "Spanish", "Ukrainian", "GEO"],
                       ["search query language", "links cited", "language of cited pages", "answer language", "input tokens", "output tokens", "page opens", "time (seconds)"],
                       "Claude Code (Opus 5.5) and Codex CLI (gpt-6-luna) at medium effort with web search on; AI-topic questions in five languages and local-topic questions about four capitals, two runs each",
                       AGL_CHART, [("claude-web-search-by-language.csv", "text/csv"), ("claude-web-search-by-language.json", "application/json")], doi=AGL_DOI, mirrors=AGL_MIRRORS)


def agl_html():
    d = _agl()
    R = d["rows"]
    T = lambda rs, f: sum((r[f] or 0) for r in rs)
    avg = lambda rs, f: round(sum(r[f] for r in rs) / len(rs))
    pc = lambda a, b: round(a / b * 100)
    sel = lambda **k: [r for r in R if all(r[a] == b for a, b in k.items())]
    ai_cc = [r for r in sel(topic="ai", tool="claude_code") if r["ask_language"] != "en"]
    ai_cx = [r for r in sel(topic="ai", tool="codex") if r["ask_language"] != "en"]
    loc_l = [r for r in sel(topic="local") if r["ask_language"] != "en"]
    loc_e = sel(topic="local", ask_language="en")
    lang = dict(AGL_LANGS)
    one = [r for r in sel(topic="ai", tool="claude_code", question="q1_fact") if r["search_queries_count"] == 1]
    one_en = [r["input_tokens"] for r in one if r["ask_language"] == "en"][0]
    one_other = [r["input_tokens"] for r in one if r["ask_language"] != "en"]
    ukn = sel(topic="local", ask_language="uk", question="l2_news")
    es_fare_en = sel(topic="local", ask_language="en", topic_country="Spain", question="l1_fare")
    tool_avg = lambda t: [avg(sel(topic="ai", tool=t, ask_language=l), "input_tokens") for l, _ in AGL_LANGS]

    def r1(l, n, t):
        rs = sel(topic="ai", tool=t, ask_language=l)
        return (f'          <tr><td>{n}</td><td>{"Claude Code" if t == "claude_code" else "Codex"}</td>'
                f'<td class="text-right tabular-nums">{T(rs, "queries_in_english")} / {T(rs, "search_queries_count")}</td>'
                f'<td class="text-right tabular-nums">{T(rs, "cited_in_ask_language")} / {T(rs, "cited_links")}</td>'
                f'<td class="text-right tabular-nums">{sum(1 for r in rs if r["answer_language"] == l)} / {len(rs)}</td>'
                f'<td class="text-right tabular-nums">{avg(rs, "input_tokens"):,}</td><td class="text-right tabular-nums">{avg(rs, "seconds")} s</td></tr>')
    trs1 = "\n".join(r1(l, n, t) for l, n in AGL_LANGS for t in ["claude_code", "codex"])
    head1 = ['<th>Question language</th>', '<th>Tool</th>', '<th class="text-right">Queries in English</th>', '<th class="text-right">Cited links in the question&rsquo;s language</th>',
             '<th class="text-right">Answers in the question&rsquo;s language</th>', '<th class="text-right">Input tokens (avg)</th>', '<th class="text-right">Time (avg)</th>']

    def r2(code, country, asked):
        rs = [r for r in sel(topic="local", topic_country=country) if (r["ask_language"] == "en") == (asked == "en")]
        return (f'          <tr><td>{country}</td><td>{"English" if asked == "en" else lang[code]}</td>'
                f'<td class="text-right tabular-nums">{T(rs, "queries_in_topic_language")} / {T(rs, "search_queries_count")}</td>'
                f'<td class="text-right tabular-nums">{T(rs, "cited_in_topic_language")} / {T(rs, "cited_links")}</td>'
                f'<td class="text-right tabular-nums">{T(rs, "cited_english")}</td>'
                f'<td class="text-right tabular-nums">{avg(rs, "input_tokens"):,}</td></tr>')
    trs2 = "\n".join(r2(c, n, a) for c, n, _ in AGL_COUNTRIES for a in ["local", "en"])
    head2 = ['<th>Topic country</th>', '<th>Asked in</th>', '<th class="text-right">Queries in the country&rsquo;s language</th>', '<th class="text-right">Cited links in the country&rsquo;s language</th>',
             '<th class="text-right">Cited English pages</th>', '<th class="text-right">Input tokens (avg)</th>']

    ex = [("Claude Code · AI research question asked in Korean", sel(topic="ai", tool="claude_code", ask_language="ko", question="q4_geo")),
          ("Codex · AI price question asked in Japanese", sel(topic="ai", tool="codex", ask_language="ja", question="q1_fact")),
          ("Claude Code · Madrid metro fare asked in English", es_fare_en),
          ("Claude Code · Korean news asked in English", sel(topic="local", ask_language="en", topic_country="South Korea", question="l2_news")),
          ("Claude Code · Kyiv borscht asked in English", sel(topic="local", ask_language="en", topic_country="Ukraine", question="l3_food"))]
    trs3 = "\n".join(f'          <tr><td>{esc(a)}</td><td style="white-space:normal;min-width:14rem">' + "<br>".join(esc(q) for q in rs[0]["search_queries"]) + '</td></tr>' for a, rs in ex)
    head3 = ['<th>Run (first of two)</th>', '<th>Search queries</th>']
    plist = "\n".join(f'        <li><strong>{n}:</strong> ' + " · ".join(f"&ldquo;{esc(d['prompts']['ai'][l][q])}&rdquo;" for q in AGL_QS) + '</li>' for l, n in AGL_LANGS)
    llist = "\n".join(f'        <li><strong>{country}, in {lang[c]}:</strong> ' + " · ".join(f"&ldquo;{esc(d['prompts']['local'][c][q])}&rdquo;" for q in AGL_LQS)
                      + '<br><strong>In English:</strong> ' + " · ".join(f"&ldquo;{esc(d['prompts']['local']['en-' + c][q])}&rdquo;" for q in AGL_LQS) + '</li>' for c, country, _ in AGL_COUNTRIES)
    ai_en_pct = pc(T(ai_cc, "queries_in_english") + T(ai_cx, "queries_in_english"), T(ai_cc, "search_queries_count") + T(ai_cx, "search_queries_count"))
    lead = (f'<strong>Asked about AI in Korean, Japanese, Spanish or Ukrainian, Claude Code and Codex ran {T(ai_cc, "queries_in_english") + T(ai_cx, "queries_in_english")} of their {T(ai_cc, "search_queries_count") + T(ai_cx, "search_queries_count")} searches in English and cited no pages in the question&rsquo;s language. '
            f'Asked about Seoul, Tokyo, Madrid or Kyiv in the local language, Claude Code searched in that language {pc(T(loc_l, "queries_in_topic_language"), T(loc_l, "search_queries_count"))}% of the time.</strong> '
            'Every answer came back in the language of the question.')
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>For a global topic, both agents search in English.</strong> Asked about AI products in Korean, Japanese, Spanish or Ukrainian, Claude Code wrote {T(ai_cc, "queries_in_english")} of its {T(ai_cc, "search_queries_count")} search queries in English and Codex all {T(ai_cx, "search_queries_count")} of its. For the price question every language produced the same English query.</li>
        <li><strong>So the sources stay English.</strong> None of the {T(ai_cc, "cited_links")} links Claude Code cited and none of the {T(ai_cx, "cited_links")} Codex cited in those answers was a page in the question&rsquo;s language.</li>
        <li><strong>For a local topic, the search follows the country.</strong> Asked in the local language about metro fares, the week&rsquo;s news and restaurants in Seoul, Tokyo, Madrid and Kyiv, Claude Code searched in that language {T(loc_l, "queries_in_topic_language")} of {T(loc_l, "search_queries_count")} times, and {T(loc_l, "cited_in_topic_language")} of the {T(loc_l, "cited_links")} links it cited were local-language pages.</li>
        <li><strong>Even an English question about a local topic pulls in local sources.</strong> Asked the same local questions in English, Claude Code still ran {T(loc_e, "queries_in_topic_language")} of {T(loc_e, "search_queries_count")} searches in the country&rsquo;s language; for the Madrid metro fare every query was in Spanish. {T(loc_e, "cited_in_topic_language")} of {T(loc_e, "cited_links")} cited links were local-language pages.</li>
        <li><strong>Ukrainian news was the exception.</strong> Asked in Ukrainian for the week&rsquo;s news in Ukraine, Claude Code cited English-language outlets (NPR, Al Jazeera, CNN) for {T(ukn, "cited_english")} of {T(ukn, "cited_links")} links.</li>
        <li><strong>The answer always comes back in your language.</strong> All {len(R)} answers were written in the language of the question.</li>
        <li><strong>Language barely changes the token count.</strong> With one identical search, the price question cost Claude Code {one_en:,} input tokens in English and {min(one_other):,} to {max(one_other):,} in the other languages. Per answer, Codex averaged {min(tool_avg("codex")):,} to {max(tool_avg("codex")):,} input tokens by language and Claude Code {min(tool_avg("claude_code")):,} to {max(tool_avg("claude_code")):,}.</li>
      </ul>
      <h2>AI topic: search language and sources by question language</h2>
      <p class="text-sm text-zinc-400">Four questions about AI products, two runs each. Totals over the eight runs; tokens and time are averages per answer.</p>
{_table(head1, trs1)}      <h2>Local topics: Seoul, Tokyo, Madrid and Kyiv</h2>
      <p class="text-sm text-zinc-400">Claude Code only. Three questions per country (metro fare, the week&rsquo;s news, restaurants), asked in the local language and in English, two runs each.</p>
{_table(head2, trs2)}      <h2>What the agents actually searched for</h2>
{_table(head3, trs3)}      <h2>Questions</h2>
      <p class="text-sm text-zinc-400">AI topic: the same four questions as the <a href="{AGS_PATH}">Claude Code vs Codex web search dataset</a>, translated by meaning.</p>
      <ul>
{plist}
      </ul>
      <p class="text-sm text-zinc-400">Local topics:</p>
      <ul>
{llist}
      </ul>
      <h2>Method</h2>
      <ul>
        <li>Both tools on one Windows laptop, effort medium, each run in its own empty folder, prompt sent through standard input.</li>
        <li><strong>Claude Code 2.1.295</strong> (Opus 5.5, Max plan): <code>claude -p --output-format stream-json --verbose --allowedTools WebSearch WebFetch</code> with no MCP servers.</li>
        <li><strong>Codex CLI 0.162</strong> (gpt-6-luna, ChatGPT plan): <code>codex --search exec --json</code>. Codex can send several queries in one search step; every query is counted.</li>
        <li>The English AI-topic runs of both tools are the runs of the <a href="{AGS_PATH}">web search dataset</a>, measured the same day with the same settings.</li>
        <li>Query language: the script of each query (Hangul, Japanese, Cyrillic) or, for Latin script, Spanish versus English words. Cited links: every URL in the final answer; the language of each cited page was checked by hand from its address and title.</li>
        <li>Input tokens are summed over every model in the run, including cache reads and Claude Code&rsquo;s helper model.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>Two tools, two runs per question, on one day; search results and the models&rsquo; choices change over time.</li>
        <li>Local topics were measured on Claude Code only, for four countries and three kinds of question.</li>
        <li>The AI research question asks about Korean in every language, which may favour Korean sources for the Korean run.</li>
      </ul>
'''
    return (_head("Does AI search in your language? Claude Code and Codex in 5 languages", lead,
                  f'Measured {AGL_MEASURED} · version 2 · {len(R)} runs · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{AGS_PATH}">AI web search tokens, Claude Code vs Codex</a>',
                  [("claude-web-search-by-language.csv", "CSV"), ("claude-web-search-by-language.json", "JSON")],
                  AGL_CHART, "Share of search queries and cited links in English versus the local language, by topic and tool", doi=AGL_DOI, mirrors=AGL_MIRRORS)
            + body + _page_tail(agl_citation(), _embed(AGL_PATH, AGL_CHART, "Share of AI agent search queries and cited links in English versus the local language", "AI web search by language"),
                                [(AGS_PATH, "AI web search tokens: Claude Code vs Codex"), (LANG_PATH, "Token cost by language"), ("/claude-code-usage", "Check your own Claude Code usage")]))


# ---- Dataset 11: CLAUDE.md and AGENTS.md size vs tokens (measured 2026-10-18) ----
AMD_PATH = "/data/claude-md-agents-md-size"
AMD_MEASURED = "2026-10-18"
AMD_CHART = "/claude-md-agents-md-size-chart.png"
AMD_DOI = "10.5281/zenodo.23453217"  # concept DOI
AMD_MIRRORS = [("Zenodo", "https://zenodo.org/records/23453218"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/claude-md-agents-md-size"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/claude-md-and-agents-md-size-token-cost"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/agent-instructions")]
AMD_TITLE = "CLAUDE.md and AGENTS.md size: what instruction files cost in Claude Code and Codex"
AMD_DESC = ("Dataset: Claude Code and Codex run with CLAUDE.md / AGENTS.md files of 0, 1, 5, 10, 25 and 50 KB: input tokens, cache reads and cost per request over two turns, "
            "plus a test of whether an instruction at the end of a 50 KB file is followed. Free CSV, CC BY 4.0.")
AMD_SIZES = [0, 1, 5, 10, 25, 50]


def _amd():
    return json.load(open(os.path.join(ROOT, "blog_data", "agentmd", "combined.json"), encoding="utf-8"))


def amd_citation():
    if AMD_DOI:
        return f"TokenSave (2026). {AMD_TITLE} [Data set]. Zenodo. https://doi.org/{AMD_DOI}"
    return f"TokenSave (2026). {AMD_TITLE} [Data set]. {BASE}{AMD_PATH}"


AMD_COLS = ["tool", "file", "file_kb", "file_bytes", "run", "turn", "input_tokens", "cache_write_tokens", "cache_read_tokens", "output_tokens", "cost_usd", "answer"]


def write_amd_files(dist):
    d = _amd()
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(AMD_COLS)
    for r in d["rows"]:
        w.writerow([("" if r[c] is None else r[c]) for c in AMD_COLS])
    open(os.path.join(dist, "data", "claude-md-agents-md-size.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=AMD_TITLE, url=BASE + AMD_PATH, license="CC BY 4.0", measured=AMD_MEASURED, citation=amd_citation(), tools=d["tools"], prompts=d["prompts"],
                sentinel_question=d["sentinel_question"], sentinel_line=d["sentinel_line"], rows=d["rows"], sentinel=d["sentinel"],
                generator_script=open(os.path.join(ROOT, "blog_data", "agentmd", "gen.js"), encoding="utf-8").read())
    open(os.path.join(dist, "data", "claude-md-agents-md-size.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def amd_ld():
    return _dataset_ld(AMD_TITLE, AMD_DESC, AMD_PATH, AMD_MEASURED,
                       ["CLAUDE.md", "AGENTS.md", "Claude Code", "Codex", "context tokens", "prompt caching", "instruction file size", "project_doc_max_bytes"],
                       ["input tokens per request", "cache read tokens", "cost per request (USD)", "instruction followed (yes/no)"],
                       "Claude Code (Opus 5.5) and Codex CLI (gpt-6-luna) at medium effort on one Windows laptop; generated project guides of 0 to 50 KB; two turns per session, two runs each",
                       AMD_CHART, [("claude-md-agents-md-size.csv", "text/csv"), ("claude-md-agents-md-size.json", "application/json")], doi=AMD_DOI, mirrors=AMD_MIRRORS)


def amd_html():
    d = _amd()
    R = d["rows"]
    g = lambda tool, kb, turn, f: [r[f] for r in R if r["tool"] == tool and r["file_kb"] == kb and r["turn"] == turn and r["run"] == 1][0]
    base_c, base_x = g("claude_code", 0, 1, "input_tokens"), g("codex", 0, 1, "input_tokens")
    add_c = {kb: g("claude_code", kb, 1, "input_tokens") - base_c for kb in AMD_SIZES}
    add_x = {kb: g("codex", kb, 1, "input_tokens") - base_x for kb in AMD_SIZES}
    nbytes = {kb: g("claude_code", kb, 1, "file_bytes") for kb in AMD_SIZES}
    cost1 = {kb: g("claude_code", kb, 1, "cost_usd") for kb in AMD_SIZES}
    cost2 = {kb: g("claude_code", kb, 2, "cost_usd") for kb in AMD_SIZES}
    pct = lambda a, b: round((a / b - 1) * 100)
    per_kb = round(add_c[50] / (nbytes[50] / 1024))
    S = d["sentinel"]
    found = lambda tool, pos: sum(1 for s in S if s["tool"] == tool and s["position"] == pos and s["found"])
    tot = lambda tool, pos: sum(1 for s in S if s["tool"] == tool and s["position"] == pos)
    trs = "\n".join(
        f'          <tr><td class="tabular-nums">{"none" if kb == 0 else f"{nbytes[kb]:,} bytes ({kb} KB)"}</td>'
        f'<td class="text-right tabular-nums">{g("claude_code", kb, 1, "input_tokens"):,}</td><td class="text-right tabular-nums">+{add_c[kb]:,}</td>'
        f'<td class="text-right tabular-nums">${cost1[kb]:.3f}</td><td class="text-right tabular-nums">${cost2[kb]:.3f}</td>'
        f'<td class="text-right tabular-nums">{g("codex", kb, 1, "input_tokens"):,}</td><td class="text-right tabular-nums">+{add_x[kb]:,}</td></tr>' for kb in AMD_SIZES)
    head = ['<th>Instruction file</th>', '<th class="text-right">Claude Code input, turn 1</th>', '<th class="text-right">Added by file</th>',
            '<th class="text-right">Claude cost, turn 1</th>', '<th class="text-right">Claude cost, turn 2</th>', '<th class="text-right">Codex input, turn 1</th>', '<th class="text-right">Added by file</th>']
    trs2 = "\n".join(f'          <tr><td>{t}</td><td>{p}</td><td class="text-right tabular-nums">{found(k, pp)} / {tot(k, pp)}</td></tr>'
                     for k, t in [("claude_code", "Claude Code (CLAUDE.md)"), ("codex", "Codex (AGENTS.md)")] for pp, p in [("start", "Start of the file"), ("end", "End of the file")])
    head2 = ['<th>Tool</th>', '<th>Where the line was placed in a 50 KB file</th>', '<th class="text-right">Runs that knew the codename</th>']
    lead = (f'<strong>A 50 KB CLAUDE.md added {add_c[50]:,} input tokens to every Claude Code request. Codex read only the first 32 KiB of a 50 KB AGENTS.md and silently ignored an instruction placed at the end.</strong> '
            f'Claude Code&rsquo;s prompt cache absorbs most of the cost after the first turn.')
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Every kilobyte of CLAUDE.md costs about {per_kb} input tokens on every request.</strong> With no instruction file, a one-word reply cost Claude Code {base_c:,} input tokens; a 10 KB CLAUDE.md added {add_c[10]:,}, a 25 KB file {add_c[25]:,} and a 50 KB file {add_c[50]:,} (+{pct(base_c + add_c[50], base_c)}%).</li>
        <li><strong>Codex stops reading AGENTS.md at 32 KiB.</strong> A 25 KB AGENTS.md added {add_x[25]:,} tokens, but doubling it to 50 KB added only {add_x[50] - add_x[25]:,} more. We put the line &ldquo;the release codename is BLUE-HERON-47&rdquo; at the end of a 50 KB AGENTS.md: Codex answered &ldquo;NONE&rdquo; in {tot("codex", "end") - found("codex", "end")} of {tot("codex", "end")} runs, while the same line at the start of the file was found {found("codex", "start")} of {tot("codex", "start")} times. Codex documents this limit (<code>project_doc_max_bytes</code>, 32 KiB by default) but its output in our runs gave no warning that the file was cut.</li>
        <li><strong>Claude Code read the whole file.</strong> It found the codename at the start and at the end of the 50 KB CLAUDE.md in all {found("claude_code", "start") + found("claude_code", "end")} runs. Claude Code shows a performance warning for CLAUDE.md files over 40,000 characters but still loads them.</li>
        <li><strong>The cache makes the first turn the expensive one.</strong> At API list prices reported by Claude Code, the first request cost ${cost1[0]:.3f} with no file and ${cost1[50]:.3f} with the 50 KB file (+{pct(cost1[50], cost1[0])}%). On the second turn the file was read from the cache and the cost was ${cost2[0]:.3f} against ${cost2[50]:.3f} (+{pct(cost2[50], cost2[0])}%).</li>
        <li><strong>The same text costs Claude more tokens.</strong> The 25 KB file added {add_c[25]:,} tokens in Claude Code and {add_x[25]:,} in Codex, {pct(add_c[25], add_x[25])}% more, in line with Claude&rsquo;s tokenizer needing more tokens for the same English text.</li>
      </ul>
      <h2>Input tokens and cost by instruction file size</h2>
      <p class="text-sm text-zinc-400">Prompt: &ldquo;Reply with the single word OK.&rdquo;, then &ldquo;Reply with the single word OK again.&rdquo; in the same session. Both runs gave identical token counts. Cost is the API list-price figure Claude Code reports (the runs used a Max plan); Codex does not report cost.</p>
{_table(head, trs)}      <h2>Is an instruction at the end of a big file followed?</h2>
      <p class="text-sm text-zinc-400">A line &ldquo;The release codename for this project is BLUE-HERON-47.&rdquo; was added at the start or at the end of the 50 KB file, and each tool was asked for the codename without being allowed to open any files.</p>
{_table(head2, trs2)}      <h2>Method</h2>
      <ul>
        <li>The instruction files are a realistic project guide for a TypeScript monorepo (commands, then conventions for 60 modules), generated by a script so that the 1, 5, 10, 25 and 50 KB files are prefixes of the same text. The generator script is included in the JSON download.</li>
        <li>The same file was saved as <code>CLAUDE.md</code> for Claude Code and <code>AGENTS.md</code> for Codex in an otherwise empty folder.</li>
        <li><strong>Claude Code 2.1.295</strong> (Opus 5.5, effort medium): <code>claude -p</code> and then <code>claude -c -p</code> with <code>--output-format json</code> and no MCP servers. Input tokens are uncached input plus cache writes plus cache reads.</li>
        <li><strong>Codex CLI 0.162</strong> (gpt-6-luna, effort medium): <code>codex exec --json</code> and then <code>codex exec resume --last</code>. Codex reports session totals, so turn 2 is the difference from turn 1.</li>
        <li>Each configuration was run twice on 2026-10-18 on the same Windows laptop. The baseline includes each tool&rsquo;s global settings on that machine, so only the added tokens should be compared.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>One kind of instruction text, English only; other languages need more tokens per kilobyte.</li>
        <li>Sizes between 25 and 50 KB were not measured, so the exact point where Codex stops reading is taken from its documentation.</li>
        <li>The cost figures are list-price estimates from Claude Code; subscription plans are not billed per token.</li>
      </ul>
'''
    return (_head("How much does a big CLAUDE.md or AGENTS.md cost? Claude Code vs Codex", lead,
                  f'Measured {AMD_MEASURED} · 6 file sizes · 2 tools · 2 runs · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{AGT_PATH}">Claude Code vs Codex startup tokens</a>',
                  [("claude-md-agents-md-size.csv", "CSV"), ("claude-md-agents-md-size.json", "JSON")],
                  AMD_CHART, "Extra input tokens per request for CLAUDE.md and AGENTS.md files from 0 to 50 KB", doi=AMD_DOI, mirrors=AMD_MIRRORS)
            + body + _page_tail(amd_citation(), _embed(AMD_PATH, AMD_CHART, "Extra input tokens per request for CLAUDE.md and AGENTS.md files", "CLAUDE.md and AGENTS.md size"),
                                [(AGT_PATH, "Claude Code vs Codex: startup tokens and the same coding task"), (EFF_PATH, "Claude effort levels: tokens, time and cost"), ("/claude-code-usage", "Check your own Claude Code usage")]))


# ---- Dataset 12: the same coding task prompted in 5 languages (measured 2026-10-18) ----
TL_PATH = "/data/ai-coding-prompt-language"
TL_MEASURED = "2026-10-18"
TL_CHART = "/ai-coding-prompt-language-chart.png"
TL_DOI = None
TL_MIRRORS = None
TL_TITLE = "Coding in your own language: does the prompt language change what Claude Code and Codex cost?"
TL_DESC = ("Dataset: the same brick-breaker task given to Claude Code and Codex in English, Korean, Japanese, Spanish and Ukrainian, two runs each: "
           "input and output tokens, time, cost, whether the game ran, and the language of the game text and code comments. Free CSV, CC BY 4.0.")
TL_LANGS = [("en", "English"), ("ko", "Korean"), ("ja", "Japanese"), ("es", "Spanish"), ("uk", "Ukrainian")]


def _tl():
    return json.load(open(os.path.join(ROOT, "blog_data", "tasklang", "combined.json"), encoding="utf-8"))


def tl_citation():
    if TL_DOI:
        return f"TokenSave (2026). {TL_TITLE} [Data set]. Zenodo. https://doi.org/{TL_DOI}"
    return f"TokenSave (2026). {TL_TITLE} [Data set]. {BASE}{TL_PATH}"


TL_COLS = ["tool", "prompt_language", "run", "input_tokens", "cached_input_tokens", "output_tokens", "seconds", "api_cost_usd", "agent_turns",
           "file_chars", "file_lines", "works", "ui_language", "reply_language", "non_ascii_letters_in_script"]


def write_tl_files(dist):
    d = _tl()
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(TL_COLS)
    for r in d["rows"]:
        w.writerow([("" if r.get(c) is None else r.get(c)) for c in TL_COLS])
    open(os.path.join(dist, "data", "ai-coding-prompt-language.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=TL_TITLE, url=BASE + TL_PATH, license="CC BY 4.0", measured=TL_MEASURED, citation=tl_citation(), tools=d["tools"], prompts=d["prompts"], note=d["note"], rows=d["rows"])
    open(os.path.join(dist, "data", "ai-coding-prompt-language.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def tl_ld():
    return _dataset_ld(TL_TITLE, TL_DESC, TL_PATH, TL_MEASURED,
                       ["Claude Code", "Codex", "prompt language", "language tax", "Korean", "Japanese", "Spanish", "Ukrainian", "AI coding cost"],
                       ["input tokens", "output tokens", "time (seconds)", "API cost (USD)", "game works (yes/no)", "UI language", "code comment language"],
                       "Claude Code (Opus 5.5) and Codex CLI (gpt-6-luna) at medium effort on one Windows laptop; one coding task in five prompt languages, two runs each",
                       TL_CHART, [("ai-coding-prompt-language.csv", "text/csv"), ("ai-coding-prompt-language.json", "application/json")], doi=TL_DOI, mirrors=TL_MIRRORS)


def tl_html():
    d = _tl()
    R = d["rows"]
    sel = lambda t, l=None: [r for r in R if r["tool"] == t and (l is None or r["prompt_language"] == l)]
    avg = lambda rs, f: round(sum(r[f] for r in rs) / len(rs))
    rng = lambda rs, f: (min(r[f] for r in rs), max(r[f] for r in rs))
    non_en = lambda t: [r for r in sel(t) if r["prompt_language"] != "en"]
    cc_in, cx_in = rng(non_en("claude_code"), "input_tokens"), rng(non_en("codex"), "input_tokens")
    cc_out, cx_out = rng(non_en("claude_code"), "output_tokens"), rng(non_en("codex"), "output_tokens")
    en_cc = sel("claude_code", "en")
    en_two = [r for r in en_cc if r["agent_turns"] == 2][0]
    en_three = [r for r in en_cc if r["agent_turns"] == 3][0]
    works = sum(1 for r in R if r["works"])
    ui_ok = sum(1 for r in R if r["prompt_language"] != "en" and r["ui_language"] == r["prompt_language"])
    n_non_en = sum(1 for r in R if r["prompt_language"] != "en")
    cc_cost = rng(non_en("claude_code"), "api_cost_usd")
    lang = dict(TL_LANGS)
    def row(l, t):
        rs = sel(t, l)
        ins = " / ".join("{:,}".format(r["input_tokens"]) for r in rs)
        outs = " / ".join("{:,}".format(r["output_tokens"]) for r in rs)
        costs = " / ".join(("$%.2f" % r["api_cost_usd"]) if r["api_cost_usd"] is not None else "–" for r in rs)
        tname = "Claude Code" if t == "claude_code" else "Codex"
        return (f'          <tr><td>{lang[l]}</td><td>{tname}</td><td class="text-right tabular-nums">{ins}</td><td class="text-right tabular-nums">{outs}</td>'
                f'<td class="text-right tabular-nums">{avg(rs, "seconds")} s</td><td class="text-right tabular-nums">{costs}</td>'
                f'<td class="text-right tabular-nums">{sum(1 for r in rs if r["works"])} / {len(rs)}</td><td>{lang[rs[0]["ui_language"]]}</td></tr>')
    trs = "\n".join(row(l, t) for l, _ in TL_LANGS for t in ["claude_code", "codex"])
    head = ['<th>Prompt language</th>', '<th>Tool</th>', '<th class="text-right">Input tokens (run 1 / 2)</th>', '<th class="text-right">Output tokens (run 1 / 2)</th>',
            '<th class="text-right">Time (avg)</th>', '<th class="text-right">API cost (run 1 / 2)</th>', '<th class="text-right">Game works</th>', '<th>Game text language</th>']
    plist = "\n".join('        <li><strong>%s:</strong> &ldquo;%s&rdquo;</li>' % (n, esc(d["prompts"][l])) for l, n in TL_LANGS)
    lead = (f'<strong>Asking Claude Code or Codex to build the same game in Korean, Japanese, Spanish or Ukrainian cost about the same as asking in English: '
            f'{cc_in[0]:,} to {cc_in[1]:,} input tokens in Claude Code and {cx_in[0]:,} to {cx_in[1]:,} in Codex.</strong> '
            'What changed was the game itself: its on-screen text, and Claude Code&rsquo;s code comments, followed the language of the prompt.')
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>The prompt language barely moves the bill for agentic coding.</strong> With Korean, Japanese, Spanish and Ukrainian prompts, Claude Code used {cc_in[0]:,} to {cc_in[1]:,} input tokens per task against {en_two["input_tokens"]:,} for a comparable English run, and Codex {cx_in[0]:,} to {cx_in[1]:,} against {min(r["input_tokens"] for r in sel("codex", "en")):,} to {max(r["input_tokens"] for r in sel("codex", "en")):,}. The prompt is about a hundred tokens; the agent&rsquo;s own instructions, tools and the code it writes make up the rest.</li>
        <li><strong>Output did not grow either.</strong> Claude Code wrote {cc_out[0]:,} to {cc_out[1]:,} output tokens with non-English prompts and Codex {cx_out[0]:,} to {cx_out[1]:,}, close to the English runs ({min(r["output_tokens"] for r in en_cc):,} to {max(r["output_tokens"] for r in en_cc):,} and {min(r["output_tokens"] for r in sel("codex", "en")):,} to {max(r["output_tokens"] for r in sel("codex", "en")):,}), with no language consistently higher. At the API list prices Claude Code reports, a task cost ${cc_cost[0]:.2f} to ${cc_cost[1]:.2f} in any language.</li>
        <li><strong>The run matters more than the language.</strong> One English Claude Code run took an extra agent step and used {en_three["input_tokens"]:,} input tokens, more than any non-English run.</li>
        <li><strong>The game speaks your language.</strong> In all {n_non_en} non-English runs the game&rsquo;s on-screen text (score, lives, level, messages) was written in the prompt&rsquo;s language ({ui_ok} of {n_non_en}). Claude Code also wrote its code comments in that language in every run, and in one Spanish run named variables in Spanish (<code>paleta</code>, <code>ladrillos</code>); Codex wrote almost no comments (3 in 8 runs).</li>
        <li><strong>Every game worked.</strong> All {works} of {len(R)} games loaded and responded to keyboard and mouse in a headless browser without script errors.</li>
        <li><strong>The language tax is a chat problem.</strong> In plain chat, the same answer in Korean or Japanese needs far more tokens than in English (see <a href="{LANG_PATH}">token cost by language</a>). In an agentic coding task that difference is lost in the agent&rsquo;s fixed overhead and the English-like code it writes.</li>
      </ul>
      <h2>Tokens, time and cost by prompt language</h2>
      <p class="text-sm text-zinc-400">Both runs are shown for tokens and cost. Codex does not report cost. &ldquo;Game text language&rdquo; is the language of the on-screen text in the generated game.</p>
{_table(head, trs)}      <h2>Prompts</h2>
      <ul>
{plist}
      </ul>
      <h2>Method</h2>
      <ul>
        <li>Both tools on one Windows laptop, effort medium, each run in its own empty folder, prompt sent through standard input.</li>
        <li><strong>Claude Code 2.1.295</strong> (Opus 5.5): <code>claude -p --permission-mode acceptEdits --output-format json</code>, no MCP servers. Input tokens are summed over every model in the run, including cache reads.</li>
        <li><strong>Codex CLI 0.162</strong> (gpt-6-luna): <code>codex exec --json -s workspace-write</code>; tokens from the <code>turn.completed</code> events.</li>
        <li>The English runs are the same-task runs of the <a href="{AGT_PATH}">Claude Code vs Codex dataset</a>, measured the same day with the same settings.</li>
        <li>&ldquo;Game works&rdquo;: the file loaded in headless Chromium with a canvas, took mouse clicks and arrow keys for two seconds and threw no script errors. The game text language was read from the generated HTML.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>One small task and two runs per language and tool; bigger projects with more conversation may show a larger language effect.</li>
        <li>Only the first prompt was in another language; a long back-and-forth in Korean or Japanese would add more non-English text to the context.</li>
        <li>The cost figures are list-price estimates; subscription plans are not billed per token.</li>
      </ul>
'''
    return (_head("Does the prompt language change what AI coding costs? Claude Code and Codex in 5 languages", lead,
                  f'Measured {TL_MEASURED} · 5 languages · 2 tools · 2 runs · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{AGT_PATH}">Claude Code vs Codex: the same coding task</a>',
                  [("ai-coding-prompt-language.csv", "CSV"), ("ai-coding-prompt-language.json", "JSON")],
                  TL_CHART, "Input tokens for the same coding task prompted in English, Korean, Japanese, Spanish and Ukrainian", doi=TL_DOI, mirrors=TL_MIRRORS)
            + body + _page_tail(tl_citation(), _embed(TL_PATH, TL_CHART, "Input tokens for the same coding task in 5 prompt languages", "AI coding prompt language"),
                                [(AGT_PATH, "Claude Code vs Codex: startup tokens and the same coding task"), (LANG_PATH, "Token cost by language"), (AGL_PATH, "Does AI search in your language?")]))
