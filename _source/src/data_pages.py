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
    return f"TokenSave (2026). {MULTI_TITLE} [Data set]. {BASE}{MULTI_PATH}"


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
      <p>Free to use, quote and republish with attribution under <a href="{LICENSE}">CC BY 4.0</a>. Please link to this page.</p>
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
