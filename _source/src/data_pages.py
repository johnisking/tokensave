"""/data/ pages: TokenSave's own measurements as citable datasets (table, CSV/JSON download,
method, limitations, suggested citation, embed code, schema.org Dataset).
Goal: other writers can quote a number and link the source in one step (2026-10-16 citation strategy)."""
import csv, io, json, os, statistics
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
    write_har_files(dist)
    write_lti_files(dist)
    write_vib_files(dist)
    write_lng_files(dist)
    write_pol_files(dist)
    write_cof_files(dist)
    write_tai_files(dist)
    write_ccv_files(dist)
    write_bmc_files(dist)
    write_blm_files(dist)
    write_agy_files(dist)
    write_lgo_files(dist)


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
      <a href="{LTI_PATH}" class="not-prose block mt-6 border border-violet-500/40 bg-violet-500/10 rounded-xl p-4" style="text-decoration:none">
        <span class="block text-xs font-semibold uppercase tracking-wider text-violet-300">Index · v{LTI_VERSION}</span>
        <span class="block mt-1 font-semibold text-zinc-100">TokenSave Language Tax Index</span>
        <span class="block mt-1 text-sm text-zinc-300">How many more tokens your language needs than English, per model. Updated when new models ship.</span></a>
      <h2>Latest measurements</h2>
      <ul class="not-prose space-y-1.5 text-sm text-zinc-300">
{"".join(f'        <li class="flex gap-3"><span class="shrink-0 tabular-nums text-zinc-500">{d}</span><a href="{p}" class="hover:text-violet-300">{esc(t)}</a></li>' + chr(10) for d, p, t in CHANGELOG[:6])}      </ul>
      <h2>All datasets</h2>
      <ul class="not-prose mt-4 space-y-3">
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
          <span class="block mt-1 text-sm text-zinc-400">One coding task at every Claude effort level, 3 runs each: $0.26 at medium, $5.33 at max on Opus 5.5. CSV · measured {EFF_MEASURED_NEW}</span></a></li>
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
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{HAR_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(HAR_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">One coding task under 7 Claude Code settings: the harness is 90% of the input, a subagent costs +128%, unused plugins still add tokens. CSV · measured {HAR_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{VIB_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(VIB_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">Three browser games by Claude Haiku, Sonnet and Opus 5.5: all 45 passed play tests, Haiku cost about 95% less. CSV · measured {VIB_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{LNG_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(LNG_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">30 change requests three ways: a new session per request cost 129% more than one long chat. CSV · measured {LNG_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{POL_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(POL_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">Greetings and thanks double the prompt in Korean, Japanese and English, but add only a few percent to the cost. CSV · measured {POL_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{COF_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(COF_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">Pauses of up to 55 minutes cost nothing extra; after 65 minutes the cache was gone and the next message cost about 500% more. CSV · measured {COF_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{TAI_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(TAI_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">Six documents as text and as pxpipe images on four Claude models: 64% to 81% fewer input tokens, but ids outside the factsheet were read 0 of 80 times. CSV · measured {TAI_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{CCV_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(CCV_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">The prompt &ldquo;a&rdquo; on Claude Code versions from July 2025 to today: the baseline rose 86% to May 2026, then fell back to half that by October. CSV · measured {CCV_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{BMC_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(BMC_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">Playwright MCP and Chrome DevTools MCP in Claude Code, 94 runs: everyday tasks stay small, but one full snapshot of a long page is over 200,000 tokens; our tokensave-mcp-diet proxy cuts it 99%. CSV · measured {BMC_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{BLM_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(BLM_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">MCP for Blender in Claude Code, 72 runs: everyday tasks $0.16 to $0.23, a racing scene with a chase camera about $0.47; a long property dump $0.87, or $0.17 through tokensave-mcp-diet. CSV · measured {BLM_MEASURED}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{AGY_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(AGY_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">Google's Antigravity CLI (the Gemini CLI replacement) against Claude Code and Codex, 52 runs: the same Opus 5.5 read 71% to 89% fewer input tokens in Antigravity for the same game, and all 20 games worked. CSV · measured {AGY_MEASURED_SHOW}</span></a></li>
        <li class="border border-zinc-800 rounded-xl p-4 hover:border-violet-500/50"><a href="{LGO_PATH}" class="block no-underline" style="text-decoration:none">
          <span class="block font-semibold text-zinc-100">{esc(LGO_TITLE)}</span>
          <span class="block mt-1 text-sm text-zinc-400">100 runs of one coding task in Claude Code, Codex and Antigravity CLI, prompted in five languages: Claude Opus 5.5 spent about 60% more output tokens per character of code than Gemini or GPT. CSV · measured {LGO_MEASURED}</span></a></li>
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
MULTI_COLS = [("claude55", "Claude 5.5 (Opus, Sonnet, Haiku)"), ("claude45", "Claude Haiku 4.5"), ("gemini", "Gemini 3.x"), ("gpt", "GPT o200k")]


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
                tokenizers={"claude55": "Claude Opus 5.5 / Sonnet 5.5 / Haiku 5.5 (identical counts; Haiku 5.5 added 2026-10-20)", "claude45": "Claude Haiku 4.5",
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
EFF_MIRRORS = [("Zenodo", "https://zenodo.org/records/23589126"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/claude-effort-cost"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/claude-effort-levels-tokens-time-and-cost"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/effort")]
EFF_TITLE = "Claude effort levels: tokens, time and cost for the same coding task"
EFF_UPDATED = "2026-10-21"
EFF_MEASURED_NEW = "2026-10-23"
EFF_DESC = ("Dataset: the same coding prompt run in Claude Code 2.1.295 at every effort level of Claude Opus 5.5 and Haiku 5.5 and at medium and high on Sonnet 5.5, 3 runs each, "
            "with time, output tokens, total tokens, API-equivalent cost and lines of code. Opus cost $0.26 at medium and $5.33 at max on average; low to xhigh cost 40% to 64% less than our first run on an earlier version. Free CSV, CC BY 4.0.")


def _eff():
    return json.load(open(os.path.join(ROOT, "blog_data", "effortdata", "combined.json"), encoding="utf-8"))


def eff_citation():
    return f"TokenSave (2026). {EFF_TITLE} [Data set]. Zenodo. https://doi.org/{EFF_DOI}"


def write_eff_files(dist):
    d = _eff()
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["model", "effort", "run", "seconds", "output_tokens", "total_tokens", "cost_usd", "code_lines"])
    for r in d["rows"]:
        w.writerow([r["model"], r["effort"], r.get("run", 1), r["seconds"], r["output_tokens"], r["total_tokens"], _usd(r["cost_usd"]).lstrip("$"), r["code_lines"]])
    open(os.path.join(dist, "data", "claude-effort-cost.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=EFF_TITLE, url=BASE + EFF_PATH, license="CC BY 4.0", measured=f"{EFF_MEASURED} and {EFF_UPDATED} to {EFF_MEASURED_NEW}", tool=d["tool"], prompt=d["prompt"],
                citation=eff_citation(), rows=d["rows"])
    open(os.path.join(dist, "data", "claude-effort-cost.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def eff_ld():
    return _dataset_ld(EFF_TITLE, EFF_DESC, EFF_PATH, EFF_MEASURED,
                       ["Claude effort", "reasoning effort", "thinking tokens", "Claude Opus 5.5 cost", "Claude Code cost", "LLM cost"],
                       ["time (seconds)", "output tokens", "total tokens", "cost (USD, API prices)", "lines of code"],
                       "Same prompt run three times per effort level in Claude Code 2.1.295; tokens and cost from Claude Code's own usage report at list prices, time wall-clock; every game played by a script in a headless browser",
                       EFF_CHART, [("claude-effort-cost.csv", "text/csv"), ("claude-effort-cost.json", "application/json")], doi=EFF_DOI, mirrors=EFF_MIRRORS)


def _usd(v):
    return f"${v:.2f}" if v >= 0.1 else f"${v:.4f}"


def _haiku_eff(d):
    out = []
    for lv in ["low", "medium", "high", "xhigh", "max"]:
        rs = [r for r in d["rows"] if r["model_name"] == "Haiku 5.5" and r["effort"] == lv]
        if not rs: continue
        m = lambda f: statistics.mean(r[f] for r in rs)
        out.append(dict(effort=lv, n=len(rs), cost=m("cost_usd"), out=round(m("output_tokens")), seconds=round(m("seconds")),
                        turns=m("turns"), lines=round(m("code_lines")), ok=sum(r["plays_ok"] for r in rs)))
    return out


def _dur(s):
    return f"{s} s" if s < 60 else f"{s // 60} min {s % 60} s"


def _eff_avg(d, model, measured="2026-10-23"):
    out = {}
    for lv in ["low", "medium", "high", "xhigh", "max"]:
        rs = [r for r in d["rows"] if r["model_name"] == model and r["effort"] == lv and r.get("measured") == measured]
        if not rs: continue
        m = lambda f: statistics.mean(r[f] for r in rs)
        out[lv] = dict(effort=lv, n=len(rs), cost_usd=m("cost_usd"), output_tokens=round(m("output_tokens")), total_tokens=round(m("total_tokens")),
                       seconds=round(m("seconds")), code_lines=round(m("code_lines")), turns=m("turns") if all("turns" in r for r in rs) else None,
                       ok=sum(bool(r.get("plays_ok")) for r in rs))
    return out


def eff_html():
    d = _eff()
    O, SN = _eff_avg(d, "Opus 5.5"), _eff_avg(d, "Sonnet 5.5")
    old = {(r["model_name"], r["effort"]): r for r in d["rows"] if r.get("measured") == "2026-10-09"}
    lo, me, hi, xh, mx = (O[k] for k in ["low", "medium", "high", "xhigh", "max"])
    sme, shi = SN["medium"], SN["high"]
    H = {x["effort"]: x for x in _haiku_eff(d)}
    pct = lambda a, b: round((a / b - 1) * 100)
    new_ok = sum(x["ok"] for x in O.values()) + sum(x["ok"] for x in SN.values()); new_n = sum(x["n"] for x in O.values()) + sum(x["n"] for x in SN.values())
    hmax_vs_lo = pct(H["max"]["cost"], lo["cost_usd"])
    hmax_txt = (f'Even so, Haiku at max cost {abs(hmax_vs_lo)}% less than Opus 5.5 at low.' if hmax_vs_lo < 0
                else f'At max, Haiku cost {hmax_vs_lo}% more than Opus 5.5 at low, so its low to xhigh levels are where it saves money.')
    avg_rows = []
    for name, A in (("Opus 5.5", O), ("Sonnet 5.5", SN)):
        for x in A.values():
            avg_rows.append(f'          <tr><td>{name} · {x["effort"]}</td><td class="text-right tabular-nums">{_usd(x["cost_usd"])}</td><td class="text-right tabular-nums">{x["output_tokens"]:,}</td>'
                            f'<td class="text-right tabular-nums">{x["total_tokens"]:,}</td><td class="text-right tabular-nums">{_dur(x["seconds"])}</td><td class="text-right tabular-nums">{x["code_lines"]}</td>'
                            f'<td class="text-right tabular-nums">{x["ok"]}/{x["n"]}</td></tr>')
    cmp_rows = []
    for name, A in (("Opus 5.5", O), ("Sonnet 5.5", SN)):
        for x in A.values():
            o = old.get((name, x["effort"]))
            if not o: continue
            cmp_rows.append(f'          <tr><td>{name} · {x["effort"]}</td><td class="text-right tabular-nums">{_usd(o["cost_usd"])}</td><td class="text-right tabular-nums">{_usd(x["cost_usd"])}</td>'
                            f'<td class="text-right tabular-nums">{"+" if pct(x["cost_usd"], o["cost_usd"]) >= 0 else "&minus;"}{abs(pct(x["cost_usd"], o["cost_usd"]))}%</td>'
                            f'<td class="text-right tabular-nums">{o["total_tokens"]:,}</td><td class="text-right tabular-nums">{x["total_tokens"]:,}</td></tr>')
    trs = "\n".join(
        f'          <tr><td>{esc(r["model_name"])} · {esc(r["effort"])}{" · run " + str(r["run"]) if "run" in r else ""}</td><td>{esc(r.get("measured", EFF_UPDATED))}</td><td class="text-right tabular-nums">{_dur(r["seconds"])}</td>'
        f'<td class="text-right tabular-nums">{r["output_tokens"]:,}</td><td class="text-right tabular-nums">{r["total_tokens"]:,}</td>'
        f'<td class="text-right tabular-nums">{_usd(r["cost_usd"])}</td><td class="text-right tabular-nums">{r["code_lines"]:,}</td></tr>'
        for r in d["rows"])
    head = ['<th>Model · effort</th>', '<th>Measured</th>', '<th class="text-right">Time</th>', '<th class="text-right">Output tokens</th>', '<th class="text-right">Total tokens</th>', '<th class="text-right">Cost</th>', '<th class="text-right">Lines of code</th>']
    return _head("Claude effort levels: what low, medium, high, xhigh and max cost",
                 f'<strong>The same coding task cost ${me["cost_usd"]:.2f} on average at medium effort on Claude Opus 5.5 and ${mx["cost_usd"]:.2f} at max ({mx["output_tokens"]:,} output tokens against {me["output_tokens"]:,}).</strong> High cost {pct(hi["cost_usd"], me["cost_usd"])}% more than medium; the jump starts at xhigh. '
                 f'Three runs per level in Claude Code 2.1.295; low to xhigh now cost 40% to 64% less than in our first measurement on an earlier version.',
                 f'Opus and Sonnet measured {EFF_MEASURED_NEW} (3 runs per level; first run {EFF_MEASURED}), Haiku 5.5 {EFF_UPDATED} · Opus 5.5 and Haiku 5.5 at 5 levels, Sonnet 5.5 at 2 · License <a href="{LICENSE}">CC BY 4.0</a> · Write-up: <a href="/blog/claude-opus-5-5-effort">Claude Opus 5.5 effort levels tested</a>',
                 [("claude-effort-cost.csv", "CSV"), ("claude-effort-cost.json", "JSON")],
                 EFF_CHART, "Output tokens and cost for the same task at each Claude effort level", doi=EFF_DOI, mirrors=EFF_MIRRORS) + f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Low and medium are close.</strong> Low cost {abs(pct(lo["cost_usd"], me["cost_usd"]))}% less than medium (${lo["cost_usd"]:.2f} vs ${me["cost_usd"]:.2f}) and took {_dur(lo["seconds"])} instead of {_dur(me["seconds"])}, but built the plainest games ({lo["code_lines"]} lines on average against {me["code_lines"]}).</li>
        <li><strong>High is the best value step.</strong> Output tokens rose {pct(hi["output_tokens"], me["output_tokens"])}% ({me["output_tokens"]:,} to {hi["output_tokens"]:,}) but cost only {pct(hi["cost_usd"], me["cost_usd"])}% more, because most of each request is input that does not change.</li>
        <li><strong>Costs jump from xhigh.</strong> xhigh cost {pct(xh["cost_usd"], me["cost_usd"])}% more than medium and max {pct(mx["cost_usd"], me["cost_usd"])}% more. Max used {mx["output_tokens"]:,} output tokens on average and took {_dur(mx["seconds"])}.</li>
        <li><strong>Sonnet 5.5 is cheaper per run, not just per token.</strong> At the same effort it used {abs(pct(sme["output_tokens"], me["output_tokens"]))}% fewer output tokens than Opus 5.5 and cost {abs(pct(sme["cost_usd"], me["cost_usd"]))}% less at medium and {abs(pct(shi["cost_usd"], hi["cost_usd"]))}% less at high.</li>
        <li><strong>Newer Claude Code, lower bills.</strong> Our first Opus and Sonnet runs (2026-10-09, one per level, an earlier Claude Code version, measured with ccusage) cost much more at every level except max; the table below compares them. The fresh runs also carried no MCP servers, which keeps each request smaller.</li>
        <li><strong>Every game worked.</strong> All {new_ok} of {new_n} new Opus and Sonnet games kept score, reached level 2 and counted three lives down to zero in a scripted headless-browser play.</li>
        <li><strong>Haiku 5.5 at every level, three runs each.</strong> Average cost went from {_usd(H["low"]["cost"])} at low to {_usd(H["xhigh"]["cost"])} at xhigh, then {_usd(H["max"]["cost"])} at max ({pct(H["max"]["cost"], H["xhigh"]["cost"])}% more than xhigh). At max Haiku wrote its own test script and ran it, which took {H["max"]["turns"]:.0f} turns instead of {H["xhigh"]["turns"]:.0f}; each turn re-reads the conversation. {hmax_txt}</li>
        <li><strong>Every Haiku game passed at every level</strong> ({sum(x["ok"] for x in H.values())} of {sum(x["n"] for x in H.values())}). Higher effort wrote longer code ({H["low"]["lines"]} lines on average at low, {H["max"]["lines"]} at max), not more working games.</li>
      </ul>
      <h2>Opus 5.5 and Sonnet 5.5 by effort level (average of 3 runs, {EFF_MEASURED_NEW})</h2>
{_table(['<th>Model · effort</th>', '<th class="text-right">Cost</th>', '<th class="text-right">Output tokens</th>', '<th class="text-right">Total tokens</th>', '<th class="text-right">Time</th>', '<th class="text-right">Lines</th>', '<th class="text-right">Games passed</th>'], chr(10).join(avg_rows))}
      <h2>Compared with our first measurement</h2>
      <p class="text-sm text-zinc-400">First run {EFF_MEASURED} (one per level, an earlier Claude Code version, cost from ccusage) against the average of three runs on {EFF_MEASURED_NEW} (Claude Code 2.1.295, no MCP servers, cost from Claude Code&rsquo;s own report). Same prompt.</p>
{_table(['<th>Model · effort</th>', f'<th class="text-right">Cost {EFF_MEASURED}</th>', f'<th class="text-right">Cost {EFF_MEASURED_NEW}</th>', '<th class="text-right">Change</th>', '<th class="text-right">Total tokens then</th>', '<th class="text-right">Total tokens now</th>'], chr(10).join(cmp_rows))}
      <h2>Haiku 5.5 by effort level (average of 3 runs)</h2>
{_table(['<th>Effort</th>', '<th class="text-right">Cost</th>', '<th class="text-right">Output tokens</th>', '<th class="text-right">Time</th>', '<th class="text-right">Turns</th>', '<th class="text-right">Lines</th>', '<th class="text-right">Games passed</th>'], chr(10).join(
        f'          <tr><td>{x["effort"]}</td><td class="text-right tabular-nums">{_usd(x["cost"])}</td><td class="text-right tabular-nums">{x["out"]:,}</td><td class="text-right tabular-nums">{_dur(x["seconds"])}</td><td class="text-right tabular-nums">{x["turns"]:.1f}</td><td class="text-right tabular-nums">{x["lines"]}</td><td class="text-right tabular-nums">{x["ok"]}/{x["n"]}</td></tr>' for x in H.values()))}
      <h2>All runs</h2>
{_table(head, trs)}      <h2>Method</h2>
      <ul>
        <li>Prompt, word for word: &ldquo;{esc(d["prompt"])}&rdquo;</li>
        <li>Opus 5.5 and Sonnet 5.5 ({EFF_MEASURED_NEW}): Claude Code 2.1.295 on Windows 11, <code>claude -p --model &hellip; --effort &hellip; --permission-mode acceptEdits --output-format stream-json --strict-mcp-config</code> with an empty MCP config, each run in its own empty folder, three runs per level. Tokens and cost from Claude Code&rsquo;s own usage report at list prices; time is wall-clock.</li>
        <li>First measurement ({EFF_MEASURED}): one run per level on an earlier Claude Code version with default settings; tokens and cost from <a href="https://github.com/ryoppippi/ccusage">ccusage</a> at API prices. Kept for comparison.</li>
        <li>Haiku 5.5 ({EFF_UPDATED}): Claude Code 2.1.295, same settings as above, three runs per level.</li>
        <li>Every game was played by a script in headless Chromium to check the score, level 2 and three lives. One Opus max game drew its score label and value separately, which the script could not read; reading the game&rsquo;s own score variable showed it rising. Scripts are in the GitHub mirror.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>Three runs per level and one task. Runs vary, especially at xhigh and max; treat the numbers as an order of magnitude, not a fixed price.</li>
        <li>Costs are API-equivalent. On a Pro or Max plan the same runs use up your usage limit instead of money.</li>
        <li>The first and the new measurement differ in Claude Code version, MCP setup and how cost was read, so the comparison shows how much the bill moved, not why.</li>
      </ul>
''' + _page_tail(eff_citation(), _embed(EFF_PATH, EFF_CHART, "Output tokens and cost for the same task at each Claude effort level", "Claude effort levels"),
                 [("/blog/claude-opus-5-5-effort", "Claude Opus 5.5 effort levels tested (full write-up)"), ("/blog/claude-sonnet-5-5-vs-opus-5-5", "Sonnet 5.5 vs Opus 5.5"), ("/agents", "Coding agent cost calculator")])


# ---- Dataset 8: Claude Code vs Codex — startup tokens, MCP tools, same coding task (measured 2026-10-18) ----
AGT_PATH = "/data/claude-code-vs-codex-tokens"
AGT_MEASURED = "2026-10-18"
AGT_MEASURED_SHOW = "2026-10-18 and 2026-10-22"
AGT_CHART = "/claude-code-vs-codex-tokens-chart.png"
AGT_DOI = "10.5281/zenodo.23448342"  # concept DOI
AGT_MIRRORS = [("Zenodo", "https://zenodo.org/records/23589129"),
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
        for i, v in enumerate(r.get("runs") or [r["run1"], r["run2"]], 1):
            w.writerow(["startup", r["tool"], r["model"], r["mcp_tools"], i, v, "", "", "", "", ""])
    for r in d["task"]["rows"]:
        w.writerow(["same_task", r["tool"], r["model"], 0, r["run"], r["input_tokens"], r["cached_input_tokens"], r["output_tokens"], r["seconds"],
                    "" if r["api_cost_usd"] is None else f'{r["api_cost_usd"]:.2f}', r["file_lines"]])
    open(os.path.join(dist, "data", "claude-code-vs-codex-tokens.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=AGT_TITLE, url=BASE + AGT_PATH, license="CC BY 4.0", measured=AGT_MEASURED_SHOW, citation=agt_citation(),
                startup=dict(prompt=d["prompt"], mcp_server=d["mcp_server"], full_definition_tokens_o200k=d["full_definition_tokens_o200k"],
                             codex_tool_use_check=d["codex_tool_use_check"], rows=d["rows"]),
                same_task=d["task"])
    open(os.path.join(dist, "data", "claude-code-vs-codex-tokens.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def agt_ld():
    return _dataset_ld(AGT_TITLE, AGT_DESC, AGT_PATH, AGT_MEASURED,
                       ["Claude Code vs Codex", "coding agent tokens", "MCP token overhead", "system prompt tokens", "Claude Code cost", "Codex cost"],
                       ["input tokens for a one-word reply", "input tokens added per MCP tool", "input tokens for the same task", "output tokens", "time (seconds)"],
                       "Claude Code and Codex CLI run on the same Windows machine; startup with 0, 1, 10 and 30 tools from a self-written MCP server (4 runs each); the same browser-game prompt at medium effort (5 runs each)",
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
            f'<td class="text-right tabular-nums">{base[(k, n)]["avg"]:,}' + ("" if n == 0 else f' <span class="text-zinc-500">({base[(k, n)]["added_vs_no_mcp"]:+,})</span>') + "</td>" for k, _ in AGT_TOOLS) + "</tr>"
        for n in [0, 1, 10, 30])
    shead = ['<th>Setup</th>'] + [f'<th class="text-right">{esc(n)}</th>' for _, n in AGT_TOOLS]
    ttrs = "\n".join(
        f'          <tr><td>{esc(dict(AGT_TOOLS)[r["tool"]])} · run {r["run"]}</td><td class="text-right tabular-nums">{r["input_tokens"]:,}</td><td class="text-right tabular-nums">{r["output_tokens"]:,}</td>'
        f'<td class="text-right tabular-nums">{r["seconds"]} s</td><td class="text-right tabular-nums">{r["file_lines"]:,}</td><td class="text-right tabular-nums">{"–" if r["api_cost_usd"] is None else "$" + format(r["api_cost_usd"], ".2f")}</td></tr>'
        for r in d["task"]["rows"])
    thead = ['<th>Run</th>', '<th class="text-right">Input tokens</th>', '<th class="text-right">Output tokens</th>', '<th class="text-right">Time</th>', '<th class="text-right">Lines in index.html</th>', '<th class="text-right">API cost</th>']
    return _head("Claude Code vs Codex: how many tokens they use before and during work",
                 f'<strong>Before doing anything, Claude Code sends {b_cc:,} input tokens and Codex {b_cx:,}.</strong> On the same browser-game task Codex used {abs(pct(cx["input"], cc["input"]))}% fewer input tokens and {abs(pct(cx["output"], cc["output"]))}% fewer output tokens than Claude Code. Adding 30 MCP tools barely changed either.',
                 f'Measured {AGT_MEASURED_SHOW} · Claude Code 2.1.295 and Codex CLI 0.162 · 4 startup and 5 task runs per tool · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{EFF_PATH}">Claude effort levels</a>',
                 [("claude-code-vs-codex-tokens.csv", "CSV"), ("claude-code-vs-codex-tokens.json", "JSON")],
                 AGT_CHART, "Startup input tokens and the same coding task on Claude Code and Codex", doi=AGT_DOI, mirrors=AGT_MIRRORS) + f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Claude Code starts {pct(b_cc, b_cx)}% heavier.</strong> A one-word reply costs {b_cc:,} input tokens in Claude Code and {b_cx:,} in Codex. That fixed amount is sent again with every request, so it adds up over a session even though most of it is cached.</li>
        <li><strong>Adding MCP tools barely changed startup tokens.</strong> The full definitions of our 30 test tools are {full30:,} tokens, but adding them raised Claude Code by only {base[("claude_code", 30)]["added_vs_no_mcp"]:,} tokens (about {round(base[("claude_code", 30)]["added_vs_no_mcp"] / 30)} per tool) and Codex by {('nothing measurable' if abs(base[('codex', 30)]['added_vs_no_mcp']) < 200 else format(base[('codex', 30)]['added_vs_no_mcp'], ','))}. Both now load a tool&rsquo;s details only when it is needed.</li>
        <li><strong>Using the tools is what costs.</strong> Asked to list the 10 tracker tools and call one, Codex used {d["codex_tool_use_check"]["input_tokens"]:,} input tokens, {pct(d["codex_tool_use_check"]["input_tokens"], b_cx)}% more than its plain startup.</li>
        <li><strong>Same task, about half the tokens on Codex.</strong> The browser game took Claude Code {cc["input"]:,} input and {cc["output"]:,} output tokens on average ({cc["seconds"]} s, ${cc["cost"]:.2f} at API prices) and Codex {cx["input"]:,} input and {cx["output"]:,} output tokens ({cx["seconds"]} s). All {len(cc["runs"]) + len(cx["runs"])} games worked.</li>
        <li><strong>Claude Code wrote more code.</strong> Its games averaged {cc["lines"]} lines against {cx["lines"]} for Codex, which wrote denser code with fewer line breaks; both had every requested feature.</li>
      </ul>
      <h2>Startup tokens and MCP tools</h2>
      <p class="text-sm text-zinc-400">Input tokens for the prompt &ldquo;{esc(d["prompt"])}&rdquo;, average of four runs (two on 2026-10-18, two on 2026-10-22, same versions); in brackets, the change against no MCP server. One Codex run without MCP read 15,018 tokens; all its other startup runs read 14,618 or 14,678.</p>
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
        <li>Four startup runs and five task runs per tool, on two days with the same versions, and one task. Claude Code&rsquo;s task runs ranged from {min(r["input_tokens"] for r in cc["runs"]):,} to {max(r["input_tokens"] for r in cc["runs"]):,} input tokens, Codex&rsquo;s from {min(r["input_tokens"] for r in cx["runs"]):,} to {max(r["input_tokens"] for r in cx["runs"]):,}.</li>
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
AGL_MEASURED = "2026-10-19"
AGL_CHART = "/claude-web-search-by-language-chart.png"
AGL_DOI = "10.5281/zenodo.23451506"  # concept DOI
AGL_MIRRORS = [("Zenodo", "https://zenodo.org/records/23462652"),
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
    meta = dict(title=AGL_TITLE, url=BASE + AGL_PATH, license="CC BY 4.0", measured="2026-10-18 and 2026-10-19", version=3, citation=agl_citation(), tools=d["tools"],
                question_types=d["question_types"], prompts=d["prompts"], rows=d["rows"])
    open(os.path.join(dist, "data", "claude-web-search-by-language.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def agl_ld():
    return _dataset_ld(AGL_TITLE, AGL_DESC, AGL_PATH, AGL_MEASURED,
                       ["AI web search", "Claude Code", "Codex", "multilingual search", "search query language", "AI citations", "Korean", "Japanese", "Spanish", "Ukrainian", "GEO"],
                       ["search query language", "links cited", "language of cited pages", "answer language", "input tokens", "output tokens", "page opens", "time (seconds)"],
                       "Claude Code (Opus 5.5) and Codex CLI (gpt-6-luna) at medium effort with web search on; AI-topic questions in five languages (two runs each) and local-topic questions about four capitals in the local language and in English (five runs each)",
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
    loc_l = [r for r in sel(topic="local", tool="claude_code") if r["ask_language"] != "en"]
    loc_e = sel(topic="local", tool="claude_code", ask_language="en")
    xloc_l = [r for r in sel(topic="local", tool="codex") if r["ask_language"] != "en"]
    xloc_e = sel(topic="local", tool="codex", ask_language="en")
    xja_e = sel(topic="local", tool="codex", ask_language="en", topic_country="Japan")
    xukn = sel(topic="local", tool="codex", ask_language="uk", question="l2_news")
    xes_c = sel(topic="local", tool="claude_code", ask_language="en", topic_country="Spain")
    xes_x = sel(topic="local", tool="codex", ask_language="en", topic_country="Spain")
    nloc = len(sel(topic="local", tool="claude_code", ask_language="ko", question="l1_fare"))
    lang = dict(AGL_LANGS)
    one = [r for r in sel(topic="ai", tool="claude_code", question="q1_fact") if r["search_queries_count"] == 1]
    one_en = [r["input_tokens"] for r in one if r["ask_language"] == "en"][0]
    one_other = [r["input_tokens"] for r in one if r["ask_language"] != "en"]
    ukn = sel(topic="local", tool="claude_code", ask_language="uk", question="l2_news")
    es_fare_en = sel(topic="local", tool="claude_code", ask_language="en", topic_country="Spain", question="l1_fare")
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

    def r2(code, country, asked, t):
        rs = [r for r in sel(topic="local", topic_country=country, tool=t) if (r["ask_language"] == "en") == (asked == "en")]
        return (f'          <tr><td>{country}</td><td>{"English" if asked == "en" else lang[code]}</td><td>{"Claude Code" if t == "claude_code" else "Codex"}</td>'
                f'<td class="text-right tabular-nums">{T(rs, "queries_in_topic_language")} / {T(rs, "search_queries_count")}</td>'
                f'<td class="text-right tabular-nums">{T(rs, "cited_in_topic_language")} / {T(rs, "cited_links")}</td>'
                f'<td class="text-right tabular-nums">{T(rs, "cited_english")}</td>'
                f'<td class="text-right tabular-nums">{avg(rs, "input_tokens"):,}</td></tr>')
    trs2 = "\n".join(r2(c, n, a, t) for c, n, _ in AGL_COUNTRIES for a in ["local", "en"] for t in ["claude_code", "codex"])
    head2 = ['<th>Topic country</th>', '<th>Asked in</th>', '<th>Tool</th>', '<th class="text-right">Queries in the country&rsquo;s language</th>', '<th class="text-right">Cited links in the country&rsquo;s language</th>',
             '<th class="text-right">Cited English pages</th>', '<th class="text-right">Input tokens (avg)</th>']

    ex = [("Claude Code · AI research question asked in Korean", sel(topic="ai", tool="claude_code", ask_language="ko", question="q4_geo")),
          ("Codex · AI price question asked in Japanese", sel(topic="ai", tool="codex", ask_language="ja", question="q1_fact")),
          ("Claude Code · Madrid metro fare asked in English", es_fare_en),
          ("Claude Code · Korean news asked in English", sel(topic="local", tool="claude_code", ask_language="en", topic_country="South Korea", question="l2_news")),
          ("Claude Code · Kyiv borscht asked in English", sel(topic="local", tool="claude_code", ask_language="en", topic_country="Ukraine", question="l3_food")),
          ("Codex · Tokyo ramen asked in Japanese (run 2; run 1 did not search)", sel(topic="local", tool="codex", ask_language="ja", topic_country="Japan", question="l3_food", run=2))]
    trs3 = "\n".join(f'          <tr><td>{esc(a)}</td><td style="white-space:normal;min-width:14rem">' + "<br>".join(esc(q) for q in rs[0]["search_queries"]) + '</td></tr>' for a, rs in ex)
    head3 = ['<th>Run (first run unless noted)</th>', '<th>Search queries</th>']
    plist = "\n".join(f'        <li><strong>{n}:</strong> ' + " · ".join(f"&ldquo;{esc(d['prompts']['ai'][l][q])}&rdquo;" for q in AGL_QS) + '</li>' for l, n in AGL_LANGS)
    llist = "\n".join(f'        <li><strong>{country}, in {lang[c]}:</strong> ' + " · ".join(f"&ldquo;{esc(d['prompts']['local'][c][q])}&rdquo;" for q in AGL_LQS)
                      + '<br><strong>In English:</strong> ' + " · ".join(f"&ldquo;{esc(d['prompts']['local']['en-' + c][q])}&rdquo;" for q in AGL_LQS) + '</li>' for c, country, _ in AGL_COUNTRIES)
    ai_en_pct = pc(T(ai_cc, "queries_in_english") + T(ai_cx, "queries_in_english"), T(ai_cc, "search_queries_count") + T(ai_cx, "search_queries_count"))
    lead = (f'<strong>Asked about AI in Korean, Japanese, Spanish or Ukrainian, Claude Code and Codex ran {T(ai_cc, "queries_in_english") + T(ai_cx, "queries_in_english")} of their {T(ai_cc, "search_queries_count") + T(ai_cx, "search_queries_count")} searches in English and cited no pages in the question&rsquo;s language. '
            f'Asked about Seoul, Tokyo, Madrid or Kyiv in the local language, Claude Code searched in that language {pc(T(loc_l, "queries_in_topic_language"), T(loc_l, "search_queries_count"))}% of the time and Codex {pc(T(xloc_l, "queries_in_topic_language"), T(xloc_l, "search_queries_count"))}%.</strong> '
            'Every answer came back in the language of the question.')
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>For a global topic, both agents search in English.</strong> Asked about AI products in Korean, Japanese, Spanish or Ukrainian, Claude Code wrote {T(ai_cc, "queries_in_english")} of its {T(ai_cc, "search_queries_count")} search queries in English and Codex all {T(ai_cx, "search_queries_count")} of its. For the price question every language produced the same English query.</li>
        <li><strong>So the sources stay English.</strong> None of the {T(ai_cc, "cited_links")} links Claude Code cited and none of the {T(ai_cx, "cited_links")} Codex cited in those answers was a page in the question&rsquo;s language.</li>
        <li><strong>For a local topic, Claude Code&rsquo;s search follows the country.</strong> Asked in the local language about metro fares, the week&rsquo;s news and restaurants in Seoul, Tokyo, Madrid and Kyiv ({nloc} runs per question), Claude Code searched in that language {T(loc_l, "queries_in_topic_language")} of {T(loc_l, "search_queries_count")} times, and {T(loc_l, "cited_in_topic_language")} of the {T(loc_l, "cited_links")} links it cited were local-language pages.</li>
        <li><strong>Even an English question about a local topic pulls in local sources.</strong> Asked the same local questions in English, Claude Code still ran {T(loc_e, "queries_in_topic_language")} of {T(loc_e, "search_queries_count")} searches in the country&rsquo;s language; for the Madrid metro fare every query was in Spanish. {T(loc_e, "cited_in_topic_language")} of {T(loc_e, "cited_links")} cited links were local-language pages.</li>
        <li><strong>Codex switches far less.</strong> Asked the same local questions in the local language, Codex searched in that language {T(xloc_l, "queries_in_topic_language")} of {T(xloc_l, "search_queries_count")} times ({pc(T(xloc_l, "queries_in_topic_language"), T(xloc_l, "search_queries_count"))}%) and {T(xloc_l, "cited_in_topic_language")} of its {T(xloc_l, "cited_links")} cited links were local-language pages. Asked in English it searched in the country&rsquo;s language {T(xloc_e, "queries_in_topic_language")} of {T(xloc_e, "search_queries_count")} times; for Japan, {T(xja_e, "queries_in_topic_language")} of {T(xja_e, "search_queries_count")}. Madrid was the exception for both tools: asked in English, Claude Code still cited Spanish pages for {T(xes_c, "cited_in_topic_language")} of {T(xes_c, "cited_links")} links and Codex for {T(xes_x, "cited_in_topic_language")} of {T(xes_x, "cited_links")}.</li>
        <li><strong>Ukrainian news was the exception.</strong> Asked in Ukrainian for the week&rsquo;s news in Ukraine, Claude Code cited English-language outlets (NPR, Al Jazeera, CNN) for {T(ukn, "cited_english")} of {T(ukn, "cited_links")} links; {T(xukn, "cited_english")} of the {T(xukn, "cited_links")} links Codex cited were English-language pages.</li>
        <li><strong>The answer always comes back in your language.</strong> All {len(R)} answers were written in the language of the question.</li>
        <li><strong>Language barely changes the token count.</strong> With one identical search, the price question cost Claude Code {one_en:,} input tokens in English and {min(one_other):,} to {max(one_other):,} in the other languages. Per answer, Codex averaged {min(tool_avg("codex")):,} to {max(tool_avg("codex")):,} input tokens by language and Claude Code {min(tool_avg("claude_code")):,} to {max(tool_avg("claude_code")):,}.</li>
      </ul>
      <h2>AI topic: search language and sources by question language</h2>
      <p class="text-sm text-zinc-400">Four questions about AI products, two runs each. Totals over the eight runs; tokens and time are averages per answer.</p>
{_table(head1, trs1)}      <h2>Local topics: Seoul, Tokyo, Madrid and Kyiv</h2>
      <p class="text-sm text-zinc-400">Three questions per country (metro fare, the week&rsquo;s news, restaurants), asked in the local language and in English, {nloc} runs each per tool. Totals over the runs.</p>
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
        <li>AI-topic runs and local-topic runs 1 and 2 of Claude Code were measured on 2026-10-18; local-topic runs 3 to 5 of Claude Code and all local-topic runs of Codex on 2026-10-19 with the same versions and settings. The news question asks about &ldquo;the past 7 days&rdquo;, so later runs saw a different week&rsquo;s news.</li>
        <li>Query language: the script of each query (Hangul, Japanese, Cyrillic) or, for Latin script, Spanish versus English words. Cited links: every URL in the final answer; the language of each cited page was checked by hand from its address and title.</li>
        <li>Input tokens are summed over every model in the run, including cache reads and Claude Code&rsquo;s helper model.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>Two runs per AI-topic question and five per local-topic question, over two days; search results and the models&rsquo; choices change over time.</li>
        <li>Four countries and three kinds of local question; the language of each cited page was classified by hand.</li>
        <li>The AI research question asks about Korean in every language, which may favour Korean sources for the Korean run.</li>
      </ul>
'''
    return (_head("Does AI search in your language? Claude Code and Codex in 5 languages", lead,
                  f'Measured 2026-10-18 and {AGL_MEASURED} · version 3 · {len(R)} runs · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{AGS_PATH}">AI web search tokens, Claude Code vs Codex</a>',
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


# ---- Dataset 12: the same coding task prompted in 5 languages (measured 2026-10-18, runs 3-5 added 2026-10-19) ----
TL_PATH = "/data/ai-coding-prompt-language"
TL_MEASURED = "2026-10-19"
TL_CHART = "/ai-coding-prompt-language-chart.png"
TL_DOI = "10.5281/zenodo.23454308"  # concept DOI
TL_MIRRORS = [("Zenodo", "https://zenodo.org/records/23460530"),
              ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/ai-coding-prompt-language"),
              ("Kaggle", "https://www.kaggle.com/datasets/johnisking/coding-prompt-language-claude-code-vs-codex"),
              ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/coding-prompt-language")]
TL_TITLE = "Coding in your own language: does the prompt language change what Claude Code and Codex cost?"
TL_DESC = ("Dataset: the same brick-breaker task given to Claude Code and Codex in English, Korean, Japanese, Spanish and Ukrainian, five runs each: "
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
                       "Claude Code (Opus 5.5) and Codex CLI (gpt-6-luna) at medium effort on one Windows laptop; one coding task in five prompt languages, five runs each",
                       TL_CHART, [("ai-coding-prompt-language.csv", "text/csv"), ("ai-coding-prompt-language.json", "application/json")], doi=TL_DOI, mirrors=TL_MIRRORS)


def tl_html():
    d = _tl()
    R = d["rows"]
    sel = lambda t, l=None: [r for r in R if r["tool"] == t and (l is None or r["prompt_language"] == l)]
    med = lambda rs, f: statistics.median(r[f] for r in rs)
    nruns = len(sel("claude_code", "en"))
    langs_non_en = [l for l, _ in TL_LANGS if l != "en"]
    def med_rng(t, f):
        ms = [med(sel(t, l), f) for l in langs_non_en]
        return min(ms), max(ms), med(sel(t, "en"), f)
    cc_in, cx_in = med_rng("claude_code", "input_tokens"), med_rng("codex", "input_tokens")
    cc_out, cx_out = med_rng("claude_code", "output_tokens"), med_rng("codex", "output_tokens")
    pct = lambda a, b: (a / b - 1) * 100
    spread = max(abs(pct(v, m[2])) for m in (cc_in, cx_in) for v in m[:2])
    en_cc = sel("claude_code", "en")
    extra = [r for r in en_cc if r["agent_turns"] and r["agent_turns"] > 2]
    non_en_cc = [r for r in sel("claude_code") if r["prompt_language"] != "en"]
    non_en_extra = sum(1 for r in non_en_cc if r["agent_turns"] and r["agent_turns"] > 2)
    cx_en = sel("codex", "en")
    cx_out_run = max(cx_en, key=lambda r: r["input_tokens"])
    works = sum(1 for r in R if r["works"])
    broken = [r for r in R if not r["works"]]
    ui_ok = sum(1 for r in R if r["prompt_language"] != "en" and r["ui_language"] == r["prompt_language"])
    n_non_en = sum(1 for r in R if r["prompt_language"] != "en")
    costs = [r["api_cost_usd"] for r in sel("claude_code")]
    lang = dict(TL_LANGS)
    tname = lambda t: "Claude Code" if t == "claude_code" else "Codex"

    def row(l, t):
        rs = sel(t, l)
        cs = [r["api_cost_usd"] for r in rs if r["api_cost_usd"] is not None]
        cost = ("$%.2f to $%.2f" % (min(cs), max(cs))) if cs else "&ndash;"
        uis = sorted(set(lang[r["ui_language"]] for r in rs))
        return ('          <tr><td>%s</td><td>%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s to %s</td>'
                '<td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%d s</td><td class="text-right tabular-nums">%s</td>'
                '<td class="text-right tabular-nums">%d / %d</td><td>%s</td></tr>') % (
            lang[l], tname(t), "{:,}".format(round(med(rs, "input_tokens"))),
            "{:,}".format(min(r["input_tokens"] for r in rs)), "{:,}".format(max(r["input_tokens"] for r in rs)),
            "{:,}".format(round(med(rs, "output_tokens"))), round(med(rs, "seconds")), cost,
            sum(1 for r in rs if r["works"]), len(rs), ", ".join(uis))
    trs = "\n".join(row(l, t) for l, _ in TL_LANGS for t in ["claude_code", "codex"])
    head = ['<th>Prompt language</th>', '<th>Tool</th>', '<th class="text-right">Input tokens (median)</th>', '<th class="text-right">Input tokens (range)</th>',
            '<th class="text-right">Output tokens (median)</th>', '<th class="text-right">Time (median)</th>', '<th class="text-right">API cost (range)</th>',
            '<th class="text-right">Game works</th>', '<th>Game text language</th>']
    plist = "\n".join('        <li><strong>%s:</strong> &ldquo;%s&rdquo;</li>' % (n, esc(d["prompts"][l])) for l, n in TL_LANGS)
    f = lambda v: "{:,}".format(round(v))
    broken_txt = ""
    if broken:
        b = broken[0]
        broken_txt = (" The exception was a %s run with the %s prompt, which crashed on a canvas error (a particle effect drew a circle with a negative radius)."
                      % (tname(b["tool"]), lang[b["prompt_language"]]))
    lead = ('<strong>Asking Claude Code or Codex to build the same game in Korean, Japanese, Spanish or Ukrainian cost about the same as asking in English: '
            'over %d runs per language, the median input tokens per task stayed within %.1f%% of the English median in both tools.</strong> '
            'What changed was the game itself: its on-screen text, and Claude Code&rsquo;s code comments, followed the language of the prompt.') % (nruns, spread)
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>The prompt language barely moves the bill for agentic coding.</strong> The median Claude Code task used {f(cc_in[2])} input tokens with the English prompt and {f(cc_in[0])} to {f(cc_in[1])} with the Korean, Japanese, Spanish and Ukrainian prompts. In Codex the medians were {f(cx_in[2])} and {f(cx_in[0])} to {f(cx_in[1])}. The prompt itself is about a hundred tokens; the agent&rsquo;s own instructions, tools and the code it writes make up the rest.</li>
        <li><strong>Output did not grow either.</strong> Median output was {f(cc_out[2])} tokens in English and {f(cc_out[0])} to {f(cc_out[1])} in the other languages for Claude Code, and {f(cx_out[2])} against {f(cx_out[0])} to {f(cx_out[1])} for Codex, inside the run-to-run spread. At the API list prices Claude Code reports, a task cost ${min(costs):.2f} to ${max(costs):.2f} in any language.</li>
        <li><strong>The run matters more than the language.</strong> The most expensive runs were English ones: {len(extra)} of {len(en_cc)} English Claude Code runs took an extra agent step and used {f(min(r["input_tokens"] for r in extra))} to {f(max(r["input_tokens"] for r in extra))} input tokens, and one English Codex run made an extra model call and used {f(cx_out_run["input_tokens"])}. None of the {len(non_en_cc)} non-English Claude Code runs took the extra step{"" if non_en_extra == 0 else " (" + str(non_en_extra) + " did)"}; with five runs per language this looks like chance rather than an effect of English.</li>
        <li><strong>The game speaks your language.</strong> In all {n_non_en} non-English runs the game&rsquo;s on-screen text (score, lives, level, messages) was written in the prompt&rsquo;s language ({ui_ok} of {n_non_en}). Claude Code also wrote its code comments in that language in all 20 of its non-English runs, and in 3 of the 5 Spanish runs named its variables and functions in Spanish (<code>paleta</code>, <code>ladrillos</code>, <code>dibujarBola</code>). Codex wrote 4 comments in its 20 non-English runs, all in English.</li>
        <li><strong>Almost every game worked.</strong> {works} of {len(R)} games loaded and responded to keyboard and mouse in a headless browser without script errors.{broken_txt}</li>
        <li><strong>The language tax is a chat problem.</strong> In plain chat, the same answer in Korean or Japanese needs far more tokens than in English (see <a href="{LANG_PATH}">token cost by language</a>). In an agentic coding task that difference is lost in the agent&rsquo;s fixed overhead and the English-like code it writes.</li>
      </ul>
      <h2>Tokens, time and cost by prompt language</h2>
      <p class="text-sm text-zinc-400">{nruns} runs per language and tool. Codex does not report cost. &ldquo;Game text language&rdquo; is the language of the on-screen text in the generated game. Every run is in the CSV.</p>
{_table(head, trs)}      <h2>Prompts</h2>
      <ul>
{plist}
      </ul>
      <h2>Method</h2>
      <ul>
        <li>Both tools on one Windows laptop, effort medium, each run in its own empty folder, prompt sent through standard input.</li>
        <li><strong>Claude Code 2.1.295</strong> (Opus 5.5): <code>claude -p --permission-mode acceptEdits --output-format json</code>, no MCP servers. Input tokens are summed over every model in the run, including cache reads.</li>
        <li><strong>Codex CLI 0.162</strong> (gpt-6-luna): <code>codex exec --json -s workspace-write</code>; tokens from the <code>turn.completed</code> events.</li>
        <li>Runs 1 and 2 were measured on 2026-10-18 (the English ones are the same-task runs of the <a href="{AGT_PATH}">Claude Code vs Codex dataset</a>); runs 3 to 5 for all five languages were added on 2026-10-19 with the same versions and settings, cycling through the five languages in turn.</li>
        <li>&ldquo;Game works&rdquo;: the file loaded in headless Chromium with a canvas, took mouse clicks and arrow keys for about two seconds and threw no script errors. The game text language was read from the generated HTML. The scripts that rebuild the table from the raw logs and run this check are in the GitHub mirror.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>One small task and five runs per language and tool; bigger projects with more conversation may show a larger language effect.</li>
        <li>Only the first prompt was in another language; a long back-and-forth in Korean or Japanese would add more non-English text to the context.</li>
        <li>The cost figures are list-price estimates; subscription plans are not billed per token.</li>
      </ul>
'''
    return (_head("Does the prompt language change what AI coding costs? Claude Code and Codex in 5 languages", lead,
                  f'Measured 2026-10-18 and {TL_MEASURED} · 5 languages · 2 tools · {nruns} runs each · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{AGT_PATH}">Claude Code vs Codex: the same coding task</a>',
                  [("ai-coding-prompt-language.csv", "CSV"), ("ai-coding-prompt-language.json", "JSON")],
                  TL_CHART, "Median input tokens for the same coding task prompted in English, Korean, Japanese, Spanish and Ukrainian, 5 runs each", doi=TL_DOI, mirrors=TL_MIRRORS)
            + body + _page_tail(tl_citation(), _embed(TL_PATH, TL_CHART, "Input tokens for the same coding task in 5 prompt languages", "AI coding prompt language"),
                                [(AGT_PATH, "Claude Code vs Codex: startup tokens and the same coding task"), (LANG_PATH, "Token cost by language"), (AGL_PATH, "Does AI search in your language?")]))


HAR_PATH = "/data/claude-code-harness-cost"
HAR_MEASURED = "2026-10-19"
HAR_CHART = "/claude-code-harness-cost-chart.png"
HAR_DOI = "10.5281/zenodo.23465633"  # concept DOI
HAR_MIRRORS = [("Zenodo", "https://zenodo.org/records/23465634"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/claude-code-harness-cost"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/claude-code-harness-cost-plugins-subagents"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/harness")]
HAR_TITLE = "What the Claude Code harness costs: plugins, subagents, plan mode, skills and hooks on the same task"
HAR_DESC = ("Dataset: the same coding task run five times each under seven Claude Code settings (default, safe mode, a minimal harness, a subagent, "
            "plan mode, a project skill and a hook): input and output tokens, cache reads, API cost, time and tool calls. Free CSV, CC BY 4.0.")
HAR_CONDS = [("default", "Default"), ("safemode", "Safe mode (no personal plugins)"), ("minimal", "Minimal harness (1-line system prompt, Write and Read)"),
             ("hook", "+ PostToolUse hook"), ("skill", "+ one project skill"), ("plan", "Plan mode, then build"), ("subagent", "Delegated to a subagent")]
HAR_COLS = ["condition", "run", "input_tokens", "cache_read_tokens", "output_tokens", "api_cost_usd", "seconds", "tool_calls", "subagent_tool_calls",
            "used_subagent", "used_skill", "file_chars", "works", "tools", "subagent_tools"]


def _har():
    return json.load(open(os.path.join(ROOT, "blog_data", "harness", "combined.json"), encoding="utf-8"))


def har_citation():
    if HAR_DOI:
        return f"TokenSave (2026). {HAR_TITLE} [Data set]. Zenodo. https://doi.org/{HAR_DOI}"
    return f"TokenSave (2026). {HAR_TITLE} [Data set]. {BASE}{HAR_PATH}"


def write_har_files(dist):
    d = _har()
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(HAR_COLS)
    for r in d["rows"]:
        w.writerow([json.dumps(r[c], sort_keys=True) if isinstance(r.get(c), dict) else ("" if r.get(c) is None else r.get(c)) for c in HAR_COLS])
    open(os.path.join(dist, "data", "claude-code-harness-cost.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=HAR_TITLE, url=BASE + HAR_PATH, license="CC BY 4.0", measured=HAR_MEASURED, citation=har_citation(), tool=d["tool"],
                conditions=d["conditions"], prompt=d["prompt"], subagent_prompt=d["subagent_prompt"], rows=d["rows"])
    open(os.path.join(dist, "data", "claude-code-harness-cost.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def har_ld():
    return _dataset_ld(HAR_TITLE, HAR_DESC, HAR_PATH, HAR_MEASURED,
                       ["Claude Code", "harness", "plugins", "subagent", "plan mode", "skills", "hooks", "safe mode", "system prompt", "AI coding cost"],
                       ["input tokens", "cache read tokens", "output tokens", "API cost (USD)", "time (seconds)", "tool calls", "game works (yes/no)"],
                       "Claude Code 2.1.295 (Opus 5.5) at medium effort on one Windows laptop; one coding task under seven harness settings, five runs each",
                       HAR_CHART, [("claude-code-harness-cost.csv", "text/csv"), ("claude-code-harness-cost.json", "application/json")], doi=HAR_DOI, mirrors=HAR_MIRRORS)


def har_html():
    d = _har()
    R = d["rows"]
    rs = lambda c: [r for r in R if r["condition"] == c]
    med = lambda c, k: statistics.median(r[k] for r in rs(c))
    f = lambda v: "{:,}".format(round(v))
    pct = lambda c, k: round((med(c, k) / med("default", k) - 1) * 100)
    sp = lambda c, k: ("+%d%%" if pct(c, k) >= 0 else "&minus;%d%%") % abs(pct(c, k))
    ap = lambda c, k: "%d%%" % abs(pct(c, k))
    n = len(rs("default"))
    works = sum(1 for r in R if r["works"])

    def row(c, name):
        x = rs(c)
        return ('          <tr><td>%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td>'
                '<td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">$%.2f</td><td class="text-right tabular-nums">%s</td>'
                '<td class="text-right tabular-nums">%d s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%d / %d</td></tr>') % (
            esc(name), f(med(c, "input_tokens")), "&ndash;" if c == "default" else sp(c, "input_tokens"), f(med(c, "cache_read_tokens")),
            f(med(c, "output_tokens")), med(c, "api_cost_usd"), "&ndash;" if c == "default" else sp(c, "api_cost_usd"),
            round(med(c, "seconds")), f(med(c, "file_chars")), sum(1 for r in x if r["works"]), len(x))
    trs = "\n".join(row(c, nm) for c, nm in HAR_CONDS)
    head = ['<th>Setting</th>', '<th class="text-right">Input tokens (median)</th>', '<th class="text-right">vs default</th>',
            '<th class="text-right">of which cache reads</th>', '<th class="text-right">Output tokens</th>', '<th class="text-right">API cost (median)</th>',
            '<th class="text-right">vs default</th>', '<th class="text-right">Time</th>', '<th class="text-right">Game size (chars)</th>', '<th class="text-right">Game works</th>']
    sub_s = round((med("subagent", "seconds") / med("default", "seconds") - 1) * 100)
    lead = ('<strong>Most of what Claude Code sends to the model is its own harness, not your task.</strong> '
            f'The same small coding task used a median {f(med("default", "input_tokens"))} input tokens in a default setup and {f(med("minimal", "input_tokens"))} '
            f'with a one-line system prompt and two tools ({sp("minimal", "input_tokens")}); every game still worked. '
            f'Delegating the task to a subagent cost {ap("subagent", "api_cost_usd")} more, and installed plugins added cost even when none was used.')
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>The harness is about 90% of the input.</strong> With Claude Code&rsquo;s system prompt and tool descriptions replaced by one sentence and two tools (Write and Read), the median run used {f(med("minimal", "input_tokens"))} input tokens instead of {f(med("default", "input_tokens"))} ({sp("minimal", "input_tokens")}) and cost ${med("minimal", "api_cost_usd"):.2f} instead of ${med("default", "api_cost_usd"):.2f} ({sp("minimal", "api_cost_usd")}). All {n} games worked. The games were also shorter (median {f(med("minimal", "file_chars"))} characters against {f(med("default", "file_chars"))}), so part of the saving is output.</li>
        <li><strong>Installed plugins cost tokens even when unused.</strong> This laptop has 35 plugins installed, which list 376 skills and 19 agents to the model. <code>--safe-mode</code> loaded 3 plugins, 19 skills and 5 agents, with the same 27 tools. No run used a plugin, yet safe mode cut the median input by {ap("safemode", "input_tokens")} ({f(med("default", "input_tokens") - med("safemode", "input_tokens"))} tokens per task) and the cost by {ap("safemode", "api_cost_usd")}. Here too the games came out shorter ({f(med("safemode", "file_chars"))} characters, {f(med("safemode", "output_tokens"))} output tokens against {f(med("default", "output_tokens"))}), so not all of the cost drop is input.</li>
        <li><strong>A subagent is the most expensive way to do a small task.</strong> Asked to delegate the work with the Agent tool, Claude Code did so in all {n} runs. The median run used {f(med("subagent", "input_tokens"))} input tokens ({sp("subagent", "input_tokens")}), cost ${med("subagent", "api_cost_usd"):.2f} ({sp("subagent", "api_cost_usd")}) and took {round(med("subagent", "seconds"))} seconds instead of {round(med("default", "seconds"))} (+{sub_s}%). The subagent starts with its own copy of the harness and checked its work with several shell commands.</li>
        <li><strong>Plan mode roughly tripled the input but added a quarter to the cost.</strong> Planning first and then building (two calls, the second continuing the session) used {f(med("plan", "input_tokens"))} input tokens ({sp("plan", "input_tokens")}) and cost ${med("plan", "api_cost_usd"):.2f} ({sp("plan", "api_cost_usd")}). Most of the extra input was read back from the prompt cache, which is billed at a fraction of the normal price.</li>
        <li><strong>A skill or a hook doubles the token count but barely moves the bill.</strong> One project skill (a 1.9 KB <code>SKILL.md</code>, used in all {n} runs) raised input to {f(med("skill", "input_tokens"))} ({sp("skill", "input_tokens")}) but cost only {sp("skill", "api_cost_usd")}; a PostToolUse hook that sends a reminder after each file write raised input {sp("hook", "input_tokens")} and cost {sp("hook", "api_cost_usd")}. Each adds model turns, and every turn re-reads the whole context, but nearly all of it from the cache.</li>
        <li><strong>Every game worked.</strong> {works} of {len(R)} games loaded and responded to keyboard and mouse in a headless browser without script errors, so none of these settings bought or lost correctness on a task this small.</li>
      </ul>
      <h2>Tokens, cost and time by setting</h2>
      <p class="text-sm text-zinc-400">Median of {n} runs per setting. Input tokens include cache reads and cache writes. Cost is the API list-price estimate Claude Code reports; subscription plans are not billed per token. Every run is in the CSV.</p>
{_table(head, trs)}      <h2>What this means for our other Claude Code datasets</h2>
      <p>Our earlier Claude Code measurements, such as the <a href="{AGT_PATH}">35,771 input tokens for a one-word reply</a>, were made on this same laptop with the same 35 plugins installed. Comparisons inside each dataset (file sizes, languages, effort levels) are unaffected, but the absolute Claude Code numbers include the cost of those plugins, so a clean installation will start lower.</p>
      <h2>The settings</h2>
      <ul>
        <li><strong>Default:</strong> <code>claude -p --effort medium --output-format stream-json --verbose --permission-mode acceptEdits</code> with an empty MCP config (<code>--strict-mcp-config</code>). The task prompt: &ldquo;{esc(d["prompt"])}&rdquo;</li>
        <li><strong>Safe mode:</strong> the same plus <code>--safe-mode</code>, which leaves out personal plugins, skills, hooks and CLAUDE.md.</li>
        <li><strong>Minimal harness:</strong> <code>--system-prompt "You are a coding agent. Use your tools to complete the user's task." --tools Write,Read</code>.</li>
        <li><strong>Subagent:</strong> the default command with one more sentence in the prompt: &ldquo;Delegate the implementation to a subagent with the Agent tool.&rdquo;</li>
        <li><strong>Plan mode:</strong> the prompt with <code>--permission-mode plan</code>, then <code>claude -c</code> in the same folder with &ldquo;Go ahead and implement your plan.&rdquo;. The tokens and cost of both calls are added together.</li>
        <li><strong>Skill:</strong> a 1.9 KB project skill, <code>.claude/skills/html-canvas-games/SKILL.md</code>, with conventions for single-file canvas games, placed in the working folder.</li>
        <li><strong>Hook:</strong> a PostToolUse hook on Write and Edit that returns a reminder to check the requirements before finishing.</li>
      </ul>
      <h2>Method</h2>
      <ul>
        <li>Claude Code 2.1.295 with Opus 5.5 on one Windows laptop, effort medium, no MCP servers, each run in its own empty folder, the prompt sent through standard input. The seven settings were run in turn, five rounds, on {HAR_MEASURED}.</li>
        <li>Tokens and cost come from the <code>modelUsage</code> and <code>total_cost_usd</code> fields of the final <code>result</code> event; the numbers of tools, skills, plugins and agents from the <code>system/init</code> event.</li>
        <li>&ldquo;Game works&rdquo;: the file loaded in headless Chromium with a canvas, took mouse clicks and arrow keys for about two seconds and threw no script errors.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>One small task and five runs per setting; on larger tasks a skill, a plan or a subagent may save rework that this task never needed.</li>
        <li>The plugin overhead depends on what is installed; 35 plugins is a heavy setup, and fewer plugins will cost less.</li>
        <li>The minimal harness has no shell, search or edit tools, so it is a measure of overhead, not a recommended setup.</li>
      </ul>
'''
    return (_head("What the Claude Code harness costs: plugins, subagents, plan mode, skills and hooks", lead,
                  f'Measured {HAR_MEASURED} · Claude Code (Opus 5.5) · 7 settings · {n} runs each · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{AGT_PATH}">Claude Code vs Codex: startup tokens</a>',
                  [("claude-code-harness-cost.csv", "CSV"), ("claude-code-harness-cost.json", "JSON")],
                  HAR_CHART, "Median input tokens and API cost for the same coding task under seven Claude Code settings, 5 runs each", doi=HAR_DOI, mirrors=HAR_MIRRORS)
            + body + _page_tail(har_citation(), _embed(HAR_PATH, HAR_CHART, "Claude Code harness cost by setting", "Claude Code harness cost"),
                                [(AGT_PATH, "Claude Code vs Codex: startup tokens and the same coding task"), (AMD_PATH, "CLAUDE.md and AGENTS.md size"), (EFF_PATH, "Claude effort levels: tokens, time and cost")]))


# ---- TokenSave Language Tax Index (derived from datasets 1 and 2; versioned, re-measured when new models ship) ----
LTI_PATH = "/data/language-tax-index"
LTI_VERSION = "1.2"
LTI_DATE = "2026-10-21"
LTI_CHART = "/language-tax-index-chart.png"
LTI_TITLE = "TokenSave Language Tax Index: extra tokens per language on Claude, Gemini and GPT"
LTI_DESC = ("How many more tokens the same text needs in 40 languages than in English, per model. "
            "Version 1.2 (October 2026): median +41% on Gemini 3.x and Gemini 4 Argon, +52% on GPT, +88% on Claude 5.5 (Opus, Sonnet and Haiku 5.5). Updated when new models ship. CSV, CC BY 4.0.")
# (key, label, family, current) - the legacy GPT-4 tokenizer stays as history
LTI_MODELS = [("gemini", "Gemini 3.x", "Google", True), ("gpt", "GPT (o200k, GPT-4o and later)", "OpenAI", True),
              ("claude55", "Claude 5.5 (Opus, Sonnet, Haiku)", "Anthropic", True), ("claude45", "Claude Haiku 4.5", "Anthropic", True),
              ("cl100k", "GPT-4 / GPT-3.5 (cl100k, legacy)", "OpenAI", False)]
# New models are added by dropping blog_data/lti_models/<key>.json (made by blog_data/lti_add_model.py); see seo/new-model-routine.md.
def _lti_extra():
    d = os.path.join(ROOT, "blog_data", "lti_models")
    out = []
    for f in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if f.endswith(".json"):
            out.append(json.load(open(os.path.join(d, f), encoding="utf-8")))
    return out


LTI_EXTRA = _lti_extra()
LTI_MODELS = LTI_MODELS[:-1] + [(m["key"], m["label"], m["family"], True) for m in LTI_EXTRA] + LTI_MODELS[-1:]
# Version history: (version, date, what changed). Add a row every time the index is re-measured.
LTI_HISTORY = [("1.2", "2026-10-21", "Added Gemini 4 Argon, measured on all 41 prompts in Google AI Studio: a new tokenizer. Its median tax equals Gemini 3.x (+41%), but East Asian languages got cheaper (Korean 48 to 41 tokens, Japanese 46 to 42) and most Indian languages more expensive (Kannada 58 to 72, Hindi 41 to 48, Tamil 52 to 63). English is unchanged at 34."),
               ("1.1", "2026-10-20", "Added Claude Haiku 5.5 (released 2026-10-07), measured on all 41 prompts: identical counts to Opus and Sonnet 5.5 in every language, so it joins the Claude 5.5 column. Versus Haiku 4.5, English needs 34% more tokens (35 to 47) while Korean, Japanese, Chinese, Hindi, Russian and Ukrainian are unchanged."),
               ("1.0", "2026-10-19", "First release: 41 languages × 4 current tokenizers plus the legacy GPT-4 tokenizer, from our 2026-09-30 and 2026-10-17 measurements.")]
# Models released after the last measurement, queued for the next version.
LTI_PENDING = []


def _lti_rows():
    multi = {r["code"]: r for r in json.load(open(os.path.join(ROOT, "blog_data", "langmulti", "combined.json"), encoding="utf-8"))}
    legacy = {r["code"]: r for r in _lang_rows()}
    en_c = legacy["en"]["c"]
    rows = []
    for code, r in multi.items():
        row = dict(code=code, name=r["name"])
        for k in ("gemini", "gpt", "claude55", "claude45"):
            row[k] = r[k]
            row[k + "_tax"] = r[k + "_pct"]
        for m in LTI_EXTRA:
            row[m["key"]] = m["counts"][code]
            row[m["key"] + "_tax"] = round((m["counts"][code] / m["counts"]["en"] - 1) * 100)
        row["cl100k"] = legacy[code]["c"]
        row["cl100k_tax"] = round((legacy[code]["c"] / en_c - 1) * 100)
        rows.append(row)
    rows.sort(key=lambda r: (r["gpt_tax"], r["name"]))
    return rows


def _lti_summary(rows):
    out = {}
    for k, label, fam, cur in LTI_MODELS:
        vals = [(r[k + "_tax"], r["name"]) for r in rows if r["code"] != "en"]
        out[k] = dict(label=label, family=fam, current=cur, median=round(statistics.median(v for v, _ in vals)),
                      low=min(vals), high=max(vals), en=next(r[k] for r in rows if r["code"] == "en"))
    return out


def lti_citation():
    return f"TokenSave (2026). TokenSave Language Tax Index, version {LTI_VERSION} ({LTI_DATE}). {BASE}{LTI_PATH}"


def write_lti_files(dist):
    rows = _lti_rows()
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["language_code", "language"] + [f"{k}_tax_pct" for k, *_ in LTI_MODELS] + [f"{k}_tokens" for k, *_ in LTI_MODELS])
    for r in rows:
        w.writerow([r["code"], r["name"]] + [r[k + "_tax"] for k, *_ in LTI_MODELS] + [r[k] for k, *_ in LTI_MODELS])
    open(os.path.join(dist, "data", "language-tax-index.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=LTI_TITLE, version=LTI_VERSION, date=LTI_DATE, url=BASE + LTI_PATH, license="CC BY 4.0",
                definition="tax = tokens for the language / tokens for English on the same tokenizer - 1, in percent",
                models={k: label for k, label, *_ in LTI_MODELS}, summary=_lti_summary(rows),
                history=[dict(version=v, date=d, note=n) for v, d, n in LTI_HISTORY], pending=LTI_PENDING,
                sources=[BASE + LANG_PATH, BASE + MULTI_PATH, f"https://doi.org/{LANG_DOI}", f"https://doi.org/{MULTI_DOI}"],
                citation=lti_citation(), rows=rows)
    open(os.path.join(dist, "data", "language-tax-index.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def lti_ld():
    ld = _dataset_ld(LTI_TITLE, LTI_DESC, LTI_PATH, LTI_DATE,
                     ["language tax", "tokens per language", "tokenizer", "multilingual LLM cost", "Claude", "Gemini", "GPT"],
                     ["extra tokens versus English (%)"],
                     "Derived index: tokens for the same prompt in each language divided by English tokens on the same tokenizer, minus one",
                     LTI_CHART, [("language-tax-index.csv", "text/csv"), ("language-tax-index.json", "application/json")])
    ds = ld["@graph"][0]
    ds["version"] = LTI_VERSION
    ds["isBasedOn"] = [f"https://doi.org/{LANG_DOI}", f"https://doi.org/{MULTI_DOI}"]
    return ld


def lti_html():
    rows = _lti_rows()
    sm = _lti_summary(rows)
    by = {r["code"]: r for r in rows}
    cur = [m for m in LTI_MODELS if m[3]]
    cards = "\n".join(
        f'''        <div class="border border-zinc-800 rounded-xl p-4 bg-zinc-950/40">
          <span class="block text-xs text-zinc-400">{esc(sm[k]["label"])}</span>
          <span class="block text-3xl font-extrabold tabular-nums" style="color:#fff">{_pct(sm[k]["median"])}</span>
          <span class="block text-xs text-zinc-400">median of 40 languages · {esc(sm[k]["low"][1])} {_pct(sm[k]["low"][0])} to {esc(sm[k]["high"][1])} {_pct(sm[k]["high"][0])}</span>
        </div>''' for k, *_ in cur)
    head = "".join(f'<th class="text-right">{esc(label)}</th>' for _, label, *_ in LTI_MODELS)
    trs = "\n".join(
        f'          <tr><td>{esc(r["name"])}</td>' + "".join(
            f'<td class="text-right tabular-nums">{"–" if r["code"] == "en" else _pct(r[k + "_tax"])}</td>' for k, *_ in LTI_MODELS) + "</tr>"
        for r in rows)
    hist = "\n".join(f"        <li><strong>v{v}</strong> · {d} · {esc(n)}</li>" for v, d, n in LTI_HISTORY)
    pend = ", ".join(esc(p) for p in LTI_PENDING) or "none"
    ko, uk, hi = by["ko"], by["uk"], by["hi"]
    embed = _embed(LTI_PATH, LTI_CHART, "TokenSave Language Tax Index: median extra tokens versus English by model", f"Language Tax Index v{LTI_VERSION}")
    return f'''    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <p class="not-prose text-xs font-semibold uppercase tracking-wider text-violet-300"><a href="/data/" class="no-underline" style="text-decoration:none">TokenSave Data</a> · Index · v{LTI_VERSION}</p>
      <h1 class="text-3xl font-extrabold text-white">TokenSave Language Tax Index</h1>
      <p class="mt-3 text-lg text-zinc-200"><strong>The “language tax” is how many more tokens the same text needs in your language than in English.</strong> On today's models the median across 40 languages is {_pct(sm["gemini_4_argon"]["median"])} on Gemini (3.x and 4 Argon alike), {_pct(sm["gpt"]["median"])} on GPT and {_pct(sm["claude55"]["median"])} on Claude 5.5 (Opus, Sonnet and Haiku). API prices, context windows and token-based limits all scale with it.</p>
      <p class="text-sm text-zinc-400">Version {LTI_VERSION} · {LTI_DATE} · 41 languages · {len(cur)} current tokenizers + 1 legacy · License <a href="{LICENSE}">CC BY 4.0</a> · Re-measured when new models ship</p>
      <div class="not-prose flex flex-wrap gap-2 my-4">
        <a href="/data/language-tax-index.csv" {BTN} style="text-decoration:none">⬇ CSV</a>
        <a href="/data/language-tax-index.json" {BTN} style="text-decoration:none">⬇ JSON</a>
        <a href="#cite" {BTN} style="text-decoration:none">How to cite</a>
      </div>
      <div class="not-prose grid grid-cols-1 sm:grid-cols-2 gap-3 my-4">
{cards}
      </div>
      <img src="{LTI_CHART}" alt="TokenSave Language Tax Index: median extra tokens versus English by model, with the range across 40 languages" width="1200" loading="lazy">
      <h2>What the index shows</h2>
      <ul>
        <li><strong>Every model taxes non-English text, but by very different amounts.</strong> Gemini has the smallest median tax, Claude the largest. Korean is {_pct(ko["gemini_4_argon_tax"])} on Gemini 4 Argon, {_pct(ko["gpt_tax"])} on GPT and {_pct(ko["claude55_tax"])} on Claude 5.5; Ukrainian {_pct(uk["gemini_4_argon_tax"])}, {_pct(uk["gpt_tax"])} and {_pct(uk["claude55_tax"])}.</li>
        <li><strong>The tax has fallen over time.</strong> On the legacy GPT-4 tokenizer (cl100k) the median was {_pct(sm["cl100k"]["median"])}; on the current o200k tokenizer it is {_pct(sm["gpt"]["median"])}. Hindi went from {_pct(hi["cl100k_tax"])} to {_pct(hi["gpt_tax"])}.</li>
        <li><strong>A lower tax is not always a cheaper model.</strong> The index compares each language with English on the same model. Claude 5.5 also needs more tokens for English itself ({sm["claude55"]["en"]} for our prompt, against {sm["gpt"]["en"]} on GPT and {sm["gemini"]["en"]} on Gemini), and prices per token differ. Use the <a href="/">token calculator</a> to compare real costs.</li>
        <li><strong>New in v1.2: Gemini 4 Argon moved the tax between languages.</strong> Its median is the same as Gemini 3.x ({_pct(sm["gemini_4_argon"]["median"])}) and English is unchanged at {by["en"]["gemini_4_argon"]} tokens, but {sum(r["gemini_4_argon"] < r["gemini"] for r in rows)} of 41 prompts got cheaper and {sum(r["gemini_4_argon"] > r["gemini"] for r in rows)} more expensive. Korean fell from {by["ko"]["gemini"]} to {by["ko"]["gemini_4_argon"]} tokens ({_pct(round((by["ko"]["gemini_4_argon"] / by["ko"]["gemini"] - 1) * 100))}) and Japanese from {by["ja"]["gemini"]} to {by["ja"]["gemini_4_argon"]} ({_pct(round((by["ja"]["gemini_4_argon"] / by["ja"]["gemini"] - 1) * 100))}), while Kannada rose from {by["kn"]["gemini"]} to {by["kn"]["gemini_4_argon"]} ({_pct(round((by["kn"]["gemini_4_argon"] / by["kn"]["gemini"] - 1) * 100))}), Hindi from {by["hi"]["gemini"]} to {by["hi"]["gemini_4_argon"]} ({_pct(round((by["hi"]["gemini_4_argon"] / by["hi"]["gemini"] - 1) * 100))}) and Tamil from {by["ta"]["gemini"]} to {by["ta"]["gemini_4_argon"]} ({_pct(round((by["ta"]["gemini_4_argon"] / by["ta"]["gemini"] - 1) * 100))}).</li>
        <li><strong>New in v1.1: Haiku 5.5 has a smaller tax than Haiku 4.5, because English got more expensive.</strong> Haiku 5.5 counts exactly like Opus and Sonnet 5.5 in all 41 languages. Its median tax is {_pct(sm["claude55"]["median"])} against {_pct(sm["claude45"]["median"])} on Haiku 4.5, but no language got cheaper: English rose from {by["en"]["claude45"]} to {by["en"]["claude55"]} tokens ({_pct(round((by["en"]["claude55"] / by["en"]["claude45"] - 1) * 100))}), Spanish {_pct(round((by["es"]["claude55"] / by["es"]["claude45"] - 1) * 100))} and German {_pct(round((by["de"]["claude55"] / by["de"]["claude45"] - 1) * 100))}, while Korean ({by["ko"]["claude55"]}), Japanese, Chinese, Hindi, Russian and Ukrainian stayed exactly the same. Across all 41 prompts Haiku 5.5 uses {round((sum(r["claude55"] for r in rows) / sum(r["claude45"] for r in rows) - 1) * 100)}% more tokens. At list prices ($0.10 vs $1 per million input tokens) it is still far cheaper per prompt.</li>
        <li><strong>It matters most for chat, documents and API work, much less for coding agents.</strong> In our coding test the prompt language moved input tokens by about 1%, because the agent's own instructions dwarf the prompt (<a href="/data/ai-coding-prompt-language">data</a>).</li>
      </ul>
      <h2>The index, all 41 languages</h2>
      <p class="text-sm text-zinc-400">Extra tokens versus English on the same tokenizer. Sorted by GPT.</p>
{_table(['<th>Language</th>', head], trs)}
      <h2>Method</h2>
      <ul>
        <li><strong>Definition:</strong> tax = tokens for the language ÷ tokens for English on the same tokenizer − 1, rounded to a whole percent. The headline number is the median over the 40 non-English languages.</li>
        <li><strong>Text:</strong> one everyday instruction (summarize a customer email and suggest a reply) translated into 41 languages. The prompts and raw counts are in the two source datasets: <a href="{LANG_PATH}">GPT tokenizers</a> (DOI <a href="https://doi.org/{LANG_DOI}">{LANG_DOI}</a>) and <a href="{MULTI_PATH}">Claude, Gemini and GPT</a> (DOI <a href="https://doi.org/{MULTI_DOI}">{MULTI_DOI}</a>).</li>
        <li><strong>Counting:</strong> GPT with tiktoken; Claude from Claude Code usage reports minus a one-character baseline; Gemini with the Google AI Studio token counter. Models that share a tokenizer share a column (Claude Opus, Sonnet and Haiku 5.5 gave identical counts in all 41 languages, as did Gemini 3.8 Flash and 3.1 Pro). Gemini 4 Argon was counted in the same AI Studio counter, which adds a fixed 31 tokens on that model (the one-letter text &ldquo;a&rdquo; shows 32); we subtract it.</li>
      </ul>
      <h2>Update policy and version history</h2>
      <p>We re-measure the same 41 prompts when a model with a new tokenizer ships, add or replace its column, and publish a new version here with the date. Earlier versions stay in the history, so changes over time can be cited.</p>
      <ul>
{hist}
      </ul>
      <p class="text-sm text-zinc-400">Queued for the next version: {pend}.</p>
      <h2>Limitations</h2>
      <ul>
        <li>The index rests on one prompt. On other text the per-language numbers move by roughly ±10–20 percentage points; the ranking of models and languages is more stable. Adding more texts is planned for a later version.</li>
        <li>Input tokens only. Output in another language can cost more again, and prices per token differ by model.</li>
        <li>Claude counts come from usage reports and can be off by about ±2 tokens.</li>
      </ul>
{_page_tail(lti_citation(), embed, [(LANG_PATH, "Source data: GPT tokenizers, 41 languages"), (MULTI_PATH, "Source data: Claude, Gemini and GPT, 41 languages"), ("/data/ai-coding-prompt-language", "Does prompt language change coding cost?"), ("/", "Count tokens for your own text")])}'''


# ---- Measurement log: newest first, shown on the data hub and the English home page ----
CHANGELOG = [
    ("2026-10-23", "/data/output-tokens-per-character-by-model", "Same code, about 60% more output tokens: Claude vs GPT vs Gemini in four coding tools and five languages"),
    ("2026-10-22", "/data/antigravity-cli-vs-claude-code-vs-codex", "Antigravity CLI vs Claude Code vs Codex: the same Opus 5.5 read 68% to 88% fewer tokens in Antigravity"),
    ("2026-10-22", "/data/blender-mcp-token-cost", "Blender MCP token cost: everyday tasks $0.16 to $0.23, a racing scene $0.47, and the one case a diet fixes"),
    ("2026-10-22", "/data/browser-mcp-token-cost", "Browser MCP token cost: one long-page snapshot is over 200,000 tokens, and a snapshot diet that cuts it 99%"),
    ("2026-10-21", EFF_PATH, "Claude effort levels: Haiku 5.5 added, 15 games, max about ten times the cost of xhigh"),
    ("2026-10-21", LTI_PATH, "Language Tax Index v1.2: Gemini 4 Argon in 41 languages, Korean 15% cheaper, Kannada 24% dearer than Gemini 3.x"),
    ("2026-10-21", "/data/claude-code-baseline-tokens-by-version", "Claude Code baseline tokens by version: +86% in ten months, then back to half the peak"),
    ("2026-10-21", "/data/text-as-image-token-cost", "Text as images (pxpipe) on Claude: 64% to 81% fewer tokens, but exact ids often lost"),
    ("2026-10-20", "/data/ai-coffee-break-cache-cost", "The coffee-break tax: the next Claude Code message after a 0 to 65 minute pause"),
    ("2026-10-20", "/data/vibe-coding-by-claude-model", "Vibe coding with Claude Haiku, Sonnet and Opus 5.5: 45 games, cost and play tests"),
    ("2026-10-20", "/data/long-chat-vs-new-chat-cost", "Long chat or new chat: 30 requests in one session, with /compact, and in fresh sessions"),
    ("2026-10-20", "/data/ai-politeness-token-cost", "Does being polite to AI cost more? Korean, Japanese and English"),
    ("2026-10-20", LTI_PATH, "Language Tax Index v1.1: Claude Haiku 5.5 measured in 41 languages"),
    ("2026-10-19", LTI_PATH, "Language Tax Index v1.0: extra tokens per language for every current model"),
    ("2026-10-19", "/data/claude-code-harness-cost", "Claude Code harness cost: plugins, subagents, plan mode, skills and hooks (35 runs)"),
    ("2026-10-19", "/data/ai-coding-prompt-language", "Coding in 5 prompt languages: re-run to 5 runs per language"),
    ("2026-10-19", "/data/claude-web-search-by-language", "AI web search by language: 320 runs, local topics added for Codex"),
    ("2026-10-18", "/data/claude-md-agents-md-size", "CLAUDE.md and AGENTS.md size: what instruction files cost"),
    ("2026-10-18", "/data/ai-agent-web-search-tokens", "Web search tokens in Claude Code and Codex"),
    ("2026-10-18", "/data/claude-code-vs-codex-tokens", "Claude Code vs Codex: startup tokens, MCP tools, the same task"),
    ("2026-10-18", "/data/pdf-token-cost", "PDF tokens per page, now with Codex and Cursor reading from disk"),
    ("2026-10-18", "/data/image-token-cost", "Image tokens by resolution on Claude, Gemini and GPT"),
    ("2026-10-17", "/data/token-cost-by-format", "JSON vs YAML vs CSV vs TOON on four tokenizers"),
    ("2026-10-17", "/data/token-cost-by-language-claude-gemini", "41 languages on Claude, Gemini and GPT"),
]


def latest_html(limit=5):
    items = "\n".join(
        f'        <li class="flex gap-3"><span class="shrink-0 tabular-nums text-zinc-500">{d}</span><a href="{p}" class="hover:text-violet-300">{esc(t)}</a></li>'
        for d, p, t in CHANGELOG[:limit])
    return f'''    <section class="mt-10 pt-6 border-t border-zinc-800">
      <div class="flex items-baseline justify-between gap-3 mb-3">
        <h2 class="text-sm font-semibold text-zinc-200">Latest measurements</h2>
        <a href="/data/" class="text-xs text-violet-300 hover:text-violet-200">All open data →</a>
      </div>
      <ul class="space-y-1.5 text-sm text-zinc-300">
{items}
      </ul>
    </section>
'''


# ---- Dataset 14: vibe coding with Claude Haiku, Sonnet and Opus 5.5 (measured 2026-10-20) ----
VIB_PATH = "/data/vibe-coding-by-claude-model"
VIB_MEASURED = "2026-10-20"
VIB_CHART = "/vibe-coding-by-claude-model-chart.png"
VIB_DOI = "10.5281/zenodo.23489448"  # concept DOI
VIB_MIRRORS = [("Zenodo", "https://zenodo.org/records/23536989"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/vibe-coding-by-claude-model"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/vibe-coding-claude-haiku-vs-sonnet-vs-opus-5-5"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/vibe-coding")]
VIB_TITLE = "Vibe coding with Claude Haiku, Sonnet and Opus 5.5: cost, time and whether the game works"
VIB_DESC = ("Dataset: three browser games (brick-breaker, 2048, Sudoku) built by Claude Code with Haiku 5.5, Sonnet 5.5 and Opus 5.5, five runs each: "
            "tokens, API cost, time and automated play tests. All 45 games passed; Haiku 5.5 cost about 95% less than Opus 5.5. Free CSV, CC BY 4.0.")
VIB_TASKS = [("brick", "Brick-breaker"), ("2048", "2048"), ("sudoku", "Sudoku")]
VIB_MODELS = [("claude-haiku-5-5", "Haiku 5.5"), ("claude-sonnet-5-5", "Sonnet 5.5"), ("claude-opus-5-5", "Opus 5.5")]
VIB_COLS = ["task", "model", "run", "input_tokens", "cache_read_tokens", "output_tokens", "api_cost_usd", "seconds", "turns", "tool_calls",
            "file_bytes", "works", "check_points", "rule_moves_ok", "rule_moves_bad", "puzzles_unique"]


def _vib():
    return json.load(open(os.path.join(ROOT, "blog_data", "vibe", "combined.json"), encoding="utf-8"))


def vib_citation():
    if VIB_DOI:
        return f"TokenSave (2026). {VIB_TITLE} [Data set]. Zenodo. https://doi.org/{VIB_DOI}"
    return f"TokenSave (2026). {VIB_TITLE} [Data set]. {BASE}{VIB_PATH}"


def write_vib_files(dist):
    d = _vib()
    buf = io.StringIO(); w = csv.writer(buf); w.writerow(VIB_COLS)
    for r in d["rows"]:
        w.writerow(["" if r.get(c) is None else r.get(c) for c in VIB_COLS])
    open(os.path.join(dist, "data", "vibe-coding-by-claude-model.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=VIB_TITLE, url=BASE + VIB_PATH, license="CC BY 4.0", measured=VIB_MEASURED, citation=vib_citation(), tool=d["tool"],
                prompts=d["prompts"], rows=d["rows"])
    open(os.path.join(dist, "data", "vibe-coding-by-claude-model.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def vib_ld():
    return _dataset_ld(VIB_TITLE, VIB_DESC, VIB_PATH, VIB_MEASURED,
                       ["vibe coding", "Claude Haiku 5.5", "Claude Sonnet 5.5", "Claude Opus 5.5", "Claude Code", "AI coding cost", "browser game", "2048", "Sudoku"],
                       ["input tokens", "output tokens", "API cost (USD)", "time (seconds)", "automated play test (pass/fail)"],
                       "Claude Code 2.1.295 at medium effort on one Windows laptop; three single-file browser games, three models, five runs each; games checked in headless Chromium",
                       VIB_CHART, [("vibe-coding-by-claude-model.csv", "text/csv"), ("vibe-coding-by-claude-model.json", "application/json")], doi=VIB_DOI, mirrors=VIB_MIRRORS)


def vib_html():
    d = _vib(); R = d["rows"]
    rs = lambda t, m: [r for r in R if r["task"] == t and r["model"] == m]
    med = lambda t, m, k: statistics.median(r[k] for r in rs(t, m))
    allm = lambda m, k: statistics.median(r[k] for r in R if r["model"] == m)
    f = lambda v: "{:,}".format(round(v))
    n = len(rs("brick", "claude-opus-5-5")); works = sum(1 for r in R if r["works"])
    save = lambda t: round((1 - med(t, "claude-haiku-5-5", "api_cost_usd") / med(t, "claude-opus-5-5", "api_cost_usd")) * 100)
    saves = [save(t) for t, _ in VIB_TASKS]
    trs = "\n".join(
        '          <tr><td>%s</td><td>%s</td><td class="text-right tabular-nums">$%.3f</td><td class="text-right tabular-nums">%d s</td>'
        '<td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%d / %d</td></tr>' % (
            tn, mn, med(t, m, "api_cost_usd"), round(med(t, m, "seconds")), f(med(t, m, "input_tokens")), f(med(t, m, "output_tokens")),
            f(med(t, m, "file_bytes")), sum(1 for r in rs(t, m) if r["works"]), len(rs(t, m)))
        for t, tn in VIB_TASKS for m, mn in VIB_MODELS)
    head = ['<th>Game</th>', '<th>Model</th>', '<th class="text-right">API cost</th>', '<th class="text-right">Time</th>', '<th class="text-right">Input tokens</th>',
            '<th class="text-right">Output tokens</th>', '<th class="text-right">File size (bytes)</th>', '<th class="text-right">Passed</th>']
    H, S, O = "claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5"
    lead = ('<strong>Claude Haiku 5.5 built every game we asked for, for about 5% of what Opus 5.5 cost.</strong> '
            f'Three browser games, three models, {n} runs each: all {works} of {len(R)} games passed automated play tests, including a strict check of the 2048 rules and of Sudoku puzzles with exactly one solution. '
            f'Haiku was the cheapest by far (median ${allm(H, "api_cost_usd"):.3f} per game against ${allm(O, "api_cost_usd"):.2f} on Opus) but the slowest; Sonnet 5.5 was the fastest.')
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>All {works} games passed.</strong> Every brick-breaker loaded and took keyboard and mouse input without errors. Every 2048 got 30 out of 30 moves exactly right (slide, merge once, one new 2 or 4). Every Sudoku generated three puzzles that each had exactly one solution, checked with a solver, and its Check and Solve buttons worked. On games of this size the cheapest model did not lose correctness.</li>
        <li><strong>Haiku 5.5 cost {min(saves)}&ndash;{max(saves)}% less than Opus 5.5.</strong> Median API cost per game: Haiku ${allm(H, "api_cost_usd"):.3f}, Sonnet ${allm(S, "api_cost_usd"):.2f}, Opus ${allm(O, "api_cost_usd"):.2f}. Haiku 5.5's list price is $0.10 / $0.50 per million input / output tokens against $4 / $20 for Opus 5.5.</li>
        <li><strong>Haiku was the slowest and the wordiest.</strong> It wrote a median {f(allm(H, "output_tokens"))} output tokens per game against {f(allm(S, "output_tokens"))} on Sonnet and {f(allm(O, "output_tokens"))} on Opus, and often took more model turns, so it needed a median {round(allm(H, "seconds"))} seconds against {round(allm(S, "seconds"))} on Sonnet and {round(allm(O, "seconds"))} on Opus.</li>
        <li><strong>Sonnet 5.5 was the fastest in every game</strong> and cost about half as much as Opus.</li>
        <li><strong>On a subscription the cost gap shows up as usage limits.</strong> Plans are not billed per token, but cheaper models use less of the plan's allowance, so the same Pro or Max plan stretches much further on Haiku for this kind of task.</li>
      </ul>
      <h2>Cost, time and result by game and model</h2>
      <p class="text-sm text-zinc-400">Median of {n} runs. Cost is the API list-price estimate Claude Code reports. Input tokens include cache reads and writes. Every run is in the CSV.</p>
{_table(head, trs)}      <h2>The tasks</h2>
      <ul>
''' + "".join(f'        <li><strong>{esc(tn)}:</strong> &ldquo;{esc(d["prompts"][t])}&rdquo;</li>\n' for t, tn in VIB_TASKS) + f'''      </ul>
      <h2>How the games were checked</h2>
      <ul>
        <li><strong>Brick-breaker:</strong> loads in headless Chromium with a canvas, takes clicks and arrow keys for about two seconds, no script errors (the same check as our earlier coding datasets). This first check did not verify the three things the prompt asked for, so a deeper check was added on 2026-10-21 (below).</li>
        <li><strong>Brick-breaker, deeper check (2026-10-21):</strong> the same 15 archived games, not regenerated or edited. A scripted player follows the ball with the mouse on a fast-forwarded clock (the ball is found by observing the canvas drawing calls). <strong>Score went up in 15 of 15, every game reached its second level (15 of 15), and the game's own lives value started at 3 and dropped by one per lost ball to game over in 15 of 15.</strong> In 9 games the lives value sits inside a closure, so it was read from a temporary test copy with one added line that exposes it; the archived files are unchanged. The first version of this check pressed the serve key before reading the lives value; in one game (Opus 5.5, run 5) that key also restarted the game from its Game Over screen, so the zero was not recorded (3, 2, 1, 3). The revised check reads the value before any key press and passes a game only if it records exactly 3, 2, 1, 0: all 15 pass. A separate trace of that game, with a screenshot of its Game Over screen, is in the same folder. Script and per-game results: <a href="https://github.com/johnisking/token-cost-by-language/tree/main/vibe-coding">check_brick_deep.py and brick_deep.json</a>. This question came from the editors of <a href="https://letsdatascience.com/news/tokensave-tells-lds-what-45-claude-coding-runs-reveal-0d3335f3">Let's Data Science</a>, who reviewed the dataset.</li>
        <li><strong>2048:</strong> two or three starting tiles of 2 or 4; arrow keys move tiles; tiles keep appearing; the score goes up; New Game resets the board; then 30 more moves where the board after each move must equal the expected slide-and-merge result plus exactly one new 2 or 4. A deliberately broken copy (merging into a wrong number) failed 22 of 30 moves.</li>
        <li><strong>Sudoku:</strong> 81 inputs; three generated puzzles that are valid and have exactly one solution (counted by a backtracking solver); a wrong digit is marked by Check; Solve fills a valid grid that matches the givens; New Puzzle changes the givens. A broken copy that skipped the uniqueness test failed.</li>
      </ul>
      <h2>Method</h2>
      <ul>
        <li>Claude Code 2.1.295 on one Windows laptop, <code>claude -p --effort medium --permission-mode acceptEdits --model &lt;model&gt;</code>, no MCP servers, each run in its own empty folder. Brick-breaker and 2048 ran in rounds of all three models; Sudoku ran in a parallel loop on the same day, {VIB_MEASURED}.</li>
        <li>Tokens and cost from the <code>modelUsage</code> and <code>total_cost_usd</code> fields of the final <code>result</code> event. Time is wall-clock time for the whole run.</li>
        <li>The raw logs, the games and the checking script are in the GitHub repository and the downloads.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>Three small, well-known games. On larger codebases or less familiar problems the models may differ in correctness, and a cheaper model that needs more fixes can end up costing more.</li>
        <li>Automated tests check the rules a script can see; they do not judge how fun or polished a game is.</li>
        <li>Five runs per game and model; time depends on server load on the day.</li>
      </ul>
'''
    return (_head("Vibe coding with Claude Haiku, Sonnet and Opus 5.5", lead,
                  f'Measured {VIB_MEASURED} · Claude Code · 3 games × 3 models × {n} runs · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{HAR_PATH}">Claude Code harness cost</a>',
                  [("vibe-coding-by-claude-model.csv", "CSV"), ("vibe-coding-by-claude-model.json", "JSON")],
                  VIB_CHART, "Median API cost and time per game for Claude Haiku, Sonnet and Opus 5.5", doi=VIB_DOI, mirrors=VIB_MIRRORS)
            + body + _page_tail(vib_citation(), _embed(VIB_PATH, VIB_CHART, "Vibe coding cost by Claude model", "Vibe coding with Claude Haiku, Sonnet and Opus 5.5"),
                                [(HAR_PATH, "What the Claude Code harness costs"), (EFF_PATH, "Claude effort levels: tokens, time and cost"), ("/agents", "Coding agent cost calculator")]))


# ---- Dataset 15: long conversation vs /compact vs a new session per request (measured 2026-10-20) ----
LNG_PATH = "/data/long-chat-vs-new-chat-cost"
LNG_MEASURED = "2026-10-20"
LNG_CHART = "/long-chat-vs-new-chat-cost-chart.png"
LNG_DOI = "10.5281/zenodo.23489464"  # concept DOI
LNG_MIRRORS = [("Zenodo", "https://zenodo.org/records/23489465"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/long-chat-vs-new-chat-cost"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/long-chat-vs-new-chat-claude-code-cost"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/long-chat")]
LNG_TITLE = "Long chat or new chat? What 30 requests cost in one Claude Code session, with /compact, and in fresh sessions"
LNG_DESC = ("Dataset: 30 change requests on one browser game in Claude Code (Opus 5.5), sent in one session, in one session with /compact after request 15, "
            "and as a new session for every request, two runs each: tokens, cache writes and reads, API cost and time per request. Free CSV, CC BY 4.0.")
LNG_VARS = [("claude_one", "One session"), ("claude_compact", "One session, /compact after 15"), ("claude_fresh", "New session per request")]
LNG_COLS = ["variant", "rep", "request", "input_tokens", "cache_write_tokens", "cache_read_tokens", "uncached_input_tokens", "output_tokens", "cost_usd",
            "model_calls", "seconds", "text"]


def _lng():
    return json.load(open(os.path.join(ROOT, "blog_data", "longchat", "combined.json"), encoding="utf-8"))


def lng_citation():
    if LNG_DOI:
        return f"TokenSave (2026). {LNG_TITLE} [Data set]. Zenodo. https://doi.org/{LNG_DOI}"
    return f"TokenSave (2026). {LNG_TITLE} [Data set]. {BASE}{LNG_PATH}"


def lng_totals(d=None):
    d = d or _lng()
    out = {}
    for v, _ in LNG_VARS:
        for rep in (1, 2):
            x = [r for r in d["rows"] if r["variant"] == v and r["rep"] == rep]
            c = sum(r["cost_usd"] for r in x) + sum(c["cost_usd"] for c in d["compactions"] if c["variant"] == v and c["rep"] == rep)
            out[(v, rep)] = dict(cost=c, inp=sum(r["input_tokens"] for r in x), cw=sum(r["cache_write_tokens"] for r in x),
                                 calls=sum(r["model_calls"] for r in x), sec=sum(r["seconds"] for r in x))
    return out


def write_lng_files(dist):
    d = _lng()
    buf = io.StringIO(); w = csv.writer(buf); w.writerow(LNG_COLS)
    for r in d["rows"]:
        w.writerow([r.get(c) for c in LNG_COLS])
    open(os.path.join(dist, "data", "long-chat-vs-new-chat-cost.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=LNG_TITLE, url=BASE + LNG_PATH, license="CC BY 4.0", measured=LNG_MEASURED, citation=lng_citation(), tool=d["tool"],
                requests=d["requests"], fresh_prefix=d["fresh_prefix"], compactions=d["compactions"], rows=d["rows"])
    open(os.path.join(dist, "data", "long-chat-vs-new-chat-cost.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def lng_ld():
    return _dataset_ld(LNG_TITLE, LNG_DESC, LNG_PATH, LNG_MEASURED,
                       ["Claude Code", "long conversation", "context", "/compact", "new session", "prompt caching", "AI coding cost", "vibe coding"],
                       ["input tokens", "cache write tokens", "cache read tokens", "output tokens", "API cost (USD)", "time (seconds)"],
                       "Claude Code 2.1.295 (Opus 5.5) at medium effort on one Windows laptop; 30 change requests on one game under three conversation strategies, two runs each",
                       LNG_CHART, [("long-chat-vs-new-chat-cost.csv", "text/csv"), ("long-chat-vs-new-chat-cost.json", "application/json")], doi=LNG_DOI, mirrors=LNG_MIRRORS)


def lng_html():
    d = _lng(); R = d["rows"]; T = lng_totals(d)
    f = lambda v: "{:,}".format(round(v))
    avg = lambda v, k: (T[(v, 1)][k] + T[(v, 2)][k]) / 2
    one, cmp_, fr = avg("claude_one", "cost"), avg("claude_compact", "cost"), avg("claude_fresh", "cost")
    per = lambda v, a, b: statistics.mean(r["cost_usd"] for r in R if r["variant"] == v and a <= r["request"] <= b)
    calls = lambda v: statistics.mean(r["model_calls"] for r in R if r["variant"] == v and r["request"] > 1)
    cw = lambda v: statistics.mean(r["cache_write_tokens"] for r in R if r["variant"] == v and r["request"] > 1)
    comp = d["compactions"]
    trs = "\n".join(
        '          <tr><td>%s</td><td class="text-right tabular-nums">$%.2f · $%.2f</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">$%.3f</td>'
        '<td class="text-right tabular-nums">$%.3f</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%d min</td></tr>' % (
            nm, T[(v, 1)]["cost"], T[(v, 2)]["cost"], "&ndash;" if v == "claude_one" else _pct(round((avg(v, "cost") / one - 1) * 100)),
            per(v, 2, 5), per(v, 26, 30), f(avg(v, "inp")), round(avg(v, "sec") / 60))
        for v, nm in LNG_VARS)
    head = ['<th>Strategy</th>', '<th class="text-right">Total API cost, run 1 · run 2</th>', '<th class="text-right">vs one session</th>',
            '<th class="text-right">Per request, 2&ndash;5</th>', '<th class="text-right">Per request, 26&ndash;30</th>', '<th class="text-right">Input tokens (total)</th>',
            '<th class="text-right">Time</th>']
    lead = ('<strong>Starting a new chat for every request cost 129% more than staying in one long chat.</strong> '
            f'We sent the same 30 change requests to one browser game in Claude Code three ways. One long session cost ${one:.2f} on average, '
            f'one session with <code>/compact</code> halfway ${cmp_:.2f} ({_pct(round((cmp_ / one - 1) * 100))}), and a fresh session for every request ${fr:.2f} ({_pct(round((fr / one - 1) * 100))}).')
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>A new session per request was the most expensive strategy, by far.</strong> Total API cost: one session ${T[("claude_one", 1)]["cost"]:.2f} and ${T[("claude_one", 2)]["cost"]:.2f}; a new session each time ${T[("claude_fresh", 1)]["cost"]:.2f} and ${T[("claude_fresh", 2)]["cost"]:.2f}. Both runs agree.</li>
        <li><strong>Why: a fresh session has to find its way back in.</strong> Without the conversation, Claude Code re-read the game file and rebuilt its prompt cache on every request: a mean of {calls("claude_fresh"):.1f} model calls and {f(cw("claude_fresh"))} newly cached tokens per request, against {calls("claude_one"):.1f} calls and {f(cw("claude_one"))} in the long session. A one-hour cache write costs 100% more than normal input; a cache read costs 95% less.</li>
        <li><strong>A long chat does get more expensive per message.</strong> In one session, requests 2&ndash;5 cost ${per("claude_one", 2, 5):.3f} each on average and requests 26&ndash;30 cost ${per("claude_one", 26, 30):.3f}, {_pct(round((per("claude_one", 26, 30) / per("claude_one", 2, 5) - 1) * 100))}, because every message re-reads a longer history and the game kept growing. Even then, a late message in the long chat was cheaper than a late message in a fresh session (${per("claude_fresh", 26, 30):.3f}).</li>
        <li><strong><code>/compact</code> did not save money here.</strong> Compacting after request 15 cost ${comp[0]["cost_usd"]:.2f} and ${comp[1]["cost_usd"]:.2f} itself, and the next request had to rebuild the cache, so the total came out {_pct(round((cmp_ / one - 1) * 100))} against the uncompacted session. Over 30 requests the shorter history never paid that back.</li>
        <li><strong>All six final games worked</strong> after 30 rounds of changes, whichever strategy was used.</li>
      </ul>
      <h2>Results by strategy</h2>
      <p class="text-sm text-zinc-400">Two runs each. Per-request costs are means over both runs. For one-session strategies Claude Code reports session totals, so each request is the difference from the previous one; the cost of the <code>/compact</code> call is counted in the total. Cost is the API list-price estimate (Opus 5.5).</p>
{_table(head, trs)}      <h2>What to take from it</h2>
      <ul>
        <li>For a run of related changes to the same project, keep going in the same session; that is what the prompt cache is built for.</li>
        <li>Start a new session when you switch to unrelated work, not between every small change.</li>
        <li>Save <code>/compact</code> for when the context is close to full or the history is confusing the model. It is not a cost-saving step on its own.</li>
        <li>Pauses matter too: the cache only lasts so long, which is the subject of our <a href="/data/ai-coffee-break-cache-cost">coffee-break measurement</a>.</li>
      </ul>
      <h2>Method</h2>
      <ul>
        <li>Claude Code 2.1.295 with Opus 5.5 on one Windows laptop, <code>claude -p --effort medium --permission-mode acceptEdits</code>, no MCP servers. Request 1 builds a brick-breaker game; requests 2&ndash;30 change it (ball colour, levels, sound, touch controls, a clean-up at the end). The full list is in the JSON download.</li>
        <li><strong>One session:</strong> requests 2&ndash;30 sent with <code>--resume</code> to the first session. <strong>/compact:</strong> the same, with <code>/compact</code> sent after request 15. <strong>New session:</strong> each request in a new session in the same folder, prefixed with &ldquo;{esc(d["fresh_prefix"].strip())}&rdquo;.</li>
        <li>All three strategies ran at the same time, twice, on {LNG_MEASURED}. Tokens and cost from the <code>result</code> event of each call.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>One project of about 30&ndash;40 KB and requests that mostly touch the same file. A long session that wanders across unrelated work, or one that reaches the context limit and auto-compacts, may behave differently.</li>
        <li>Claude Code only. Other tools cache differently.</li>
        <li>On a subscription the bill does not change, but the same difference applies to how fast you reach the usage limit.</li>
      </ul>
'''
    return (_head("Long chat or new chat? What 30 requests cost in Claude Code", lead,
                  f'Measured {LNG_MEASURED} · Claude Code (Opus 5.5) · 30 requests × 3 strategies × 2 runs · License <a href="{LICENSE}">CC BY 4.0</a>',
                  [("long-chat-vs-new-chat-cost.csv", "CSV"), ("long-chat-vs-new-chat-cost.json", "JSON")],
                  LNG_CHART, "Cost per request over 30 requests in one session, with /compact, and in a new session each time", doi=LNG_DOI, mirrors=LNG_MIRRORS)
            + body + _page_tail(lng_citation(), _embed(LNG_PATH, LNG_CHART, "Cost per request: long chat vs new chat", "Long chat or new chat?"),
                                [(HAR_PATH, "What the Claude Code harness costs"), (AMD_PATH, "CLAUDE.md and AGENTS.md size"), ("/blog/claude-code-save-tokens", "How to save tokens in Claude Code")]))


# ---- Dataset 16: politeness tax (measured 2026-10-20) ----
POL_PATH = "/data/ai-politeness-token-cost"
POL_MEASURED = "2026-10-20"
POL_CHART = "/ai-politeness-token-cost-chart.png"
POL_DOI = "10.5281/zenodo.23489481"  # concept DOI
POL_MIRRORS = [("Zenodo", "https://zenodo.org/records/23489482"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/ai-politeness-token-cost"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/politeness-and-ai-token-cost-ko-ja-en"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/politeness")]
POL_TITLE = "Does being polite to AI cost more? Plain, polite and very polite prompts in Korean, Japanese and English"
POL_DESC = ("Dataset: 10 everyday requests in Korean, Japanese and English at four politeness levels, sent to Claude Opus 5.5 and Haiku 5.5: "
            "prompt tokens (Claude and GPT), answer tokens and cost. Polite padding more than doubles the prompt, but the most polite version cost only 0-4% more in total. Free CSV, CC BY 4.0.")
POL_LANGS = [("ko", "Korean"), ("ja", "Japanese"), ("en", "English")]
POL_COLS = ["model", "rep", "language", "request", "level", "level_name", "prompt_tokens", "gpt_o200k_tokens", "gpt_cl100k_tokens", "output_tokens",
            "answer_chars", "cost_usd", "seconds", "prompt"]


def _pol():
    return json.load(open(os.path.join(ROOT, "blog_data", "honorific", "combined.json"), encoding="utf-8"))


def pol_citation():
    if POL_DOI:
        return f"TokenSave (2026). {POL_TITLE} [Data set]. Zenodo. https://doi.org/{POL_DOI}"
    return f"TokenSave (2026). {POL_TITLE} [Data set]. {BASE}{POL_PATH}"


def write_pol_files(dist):
    d = _pol()
    buf = io.StringIO(); w = csv.writer(buf); w.writerow(POL_COLS)
    for r in d["rows"]:
        w.writerow([r.get(c) for c in POL_COLS])
    open(os.path.join(dist, "data", "ai-politeness-token-cost.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=POL_TITLE, url=BASE + POL_PATH, license="CC BY 4.0", measured=POL_MEASURED, citation=pol_citation(), tool=d["tool"],
                levels=d["levels"], cost_note=d["cost_note"], rows=d["rows"])
    open(os.path.join(dist, "data", "ai-politeness-token-cost.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def pol_ld():
    return _dataset_ld(POL_TITLE, POL_DESC, POL_PATH, POL_MEASURED,
                       ["politeness", "please and thank you", "honorifics", "Korean", "Japanese", "keigo", "prompt tokens", "AI cost", "Claude"],
                       ["prompt tokens (Claude, GPT o200k, GPT cl100k)", "output tokens", "answer length (characters)", "API cost (USD)"],
                       "Claude Code 2.1.295 as a plain chat (no tools) with Opus 5.5 (two runs) and Haiku 5.5 (one run); GPT counts with js-tiktoken",
                       POL_CHART, [("ai-politeness-token-cost.csv", "text/csv"), ("ai-politeness-token-cost.json", "application/json")], doi=POL_DOI, mirrors=POL_MIRRORS)


def pol_sums(d=None):
    d = d or _pol(); R = d["rows"]
    out = {}
    for L, _ in POL_LANGS:
        for model in ("claude-opus-5-5", "claude-haiku-5-5"):
            x = [r for r in R if r["language"] == L and r["model"] == model]
            reps = len({r["rep"] for r in x})
            out[(L, model)] = [dict(prompt=sum(r["prompt_tokens"] for r in x if r["level"] == lv) / reps,
                                    gpt=sum(r["gpt_o200k_tokens"] for r in x if r["level"] == lv) / reps,
                                    out=sum(r["output_tokens"] for r in x if r["level"] == lv) / reps,
                                    cost=sum(r["cost_usd"] for r in x if r["level"] == lv) / reps) for lv in range(4)]
    return out


def pol_html():
    d = _pol(); S = pol_sums(d); O = "claude-opus-5-5"; H = "claude-haiku-5-5"
    f = lambda v: "{:,}".format(round(v))
    pc = lambda a, b: _pct(round((a / b - 1) * 100))
    lv = d["levels"]
    trs = []
    for L, ln in POL_LANGS:
        s = S[(L, O)]
        for i in range(4):
            trs.append('          <tr><td>%s</td><td>%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td>'
                       '<td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td></tr>' % (
                           ln if i == 0 else "", esc(lv[L][i]), f(s[i]["prompt"]), "&ndash;" if i == 0 else pc(s[i]["prompt"], s[0]["prompt"]),
                           f(s[i]["out"]), "&ndash;" if i == 0 else pc(s[i]["out"], s[0]["out"]), "$%.3f" % s[i]["cost"], "&ndash;" if i == 0 else pc(s[i]["cost"], s[0]["cost"])))
    head = ['<th>Language</th>', '<th>Level</th>', '<th class="text-right">Prompt tokens (10 requests)</th>', '<th class="text-right">vs plain</th>',
            '<th class="text-right">Answer tokens</th>', '<th class="text-right">vs plain</th>', '<th class="text-right">Cost (Opus 5.5)</th>', '<th class="text-right">vs plain</th>']
    top = {L: S[(L, O)][3]["prompt"] / S[(L, O)][0]["prompt"] - 1 for L, _ in POL_LANGS}
    cost3 = {L: S[(L, O)][3]["cost"] / S[(L, O)][0]["cost"] - 1 for L, _ in POL_LANGS}
    gpt3 = {L: S[(L, O)][3]["gpt"] / S[(L, O)][0]["gpt"] - 1 for L, _ in POL_LANGS}
    ch = [S[(L, O)][i]["out"] / S[(L, O)][0]["out"] - 1 for L, _ in POL_LANGS for i in range(1, 4)]
    mid_max = max(S[(L, O)][i]["out"] / S[(L, O)][0]["out"] - 1 for L in ("ja", "en") for i in (1, 2))
    trs_html = "\n".join(trs)
    share = statistics.mean((S[(L, O)][3]["prompt"] - S[(L, O)][0]["prompt"]) * 4 / (S[(L, O)][0]["cost"] * 1e6) * 100 for L, _ in POL_LANGS)
    lead = ('<strong>Being polite to AI more than doubles the length of your prompt, but adds only a few percent to what the message costs.</strong> '
            f'Greetings, apologies and thanks raised the prompt by {round(top["ko"] * 100)}% in Korean, {round(top["ja"] * 100)}% in Japanese and {round(top["en"] * 100)}% in English on Claude, '
            'yet the most polite version cost only 0&ndash;4% more in total, because the answer, which is most of the cost, did not get longer.')
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Polite padding adds a lot of prompt tokens.</strong> The most polite version of each request (greeting + apology + thanks) needed {round(top["ko"] * 100)}% more Claude tokens than the plain version in Korean, {round(top["ja"] * 100)}% more in Japanese and {round(top["en"] * 100)}% more in English (GPT o200k: {round(gpt3["ko"] * 100)}%, {round(gpt3["ja"] * 100)}% and {round(gpt3["en"] * 100)}%). Changing only the verb ending (&ldquo;해 줘&rdquo; to &ldquo;해 주세요&rdquo;, &ldquo;して&rdquo; to &ldquo;してください&rdquo;, adding &ldquo;please&rdquo;) added just 3&ndash;5%.</li>
        <li><strong>The answers did not grow with politeness.</strong> For the most polite version, answers were about as long as for the plain one (Korean {pc(S[("ko", O)][3]["out"], S[("ko", O)][0]["out"])}, Japanese {pc(S[("ja", O)][3]["out"], S[("ja", O)][0]["out"])}, English {pc(S[("en", O)][3]["out"], S[("en", O)][0]["out"])}). The two middle levels (&ldquo;please&rdquo;, &ldquo;Could you please &hellip;?&rdquo;, &ldquo;ご提案いただけますでしょうか&rdquo;) did get longer answers in Japanese and English (up to {_pct(round(mid_max * 100))}), but Korean was mixed and the same prompts varied by up to 19% between two runs, so this is a hint rather than a rule.</li>
        <li><strong>The polite words themselves cost little.</strong> Answers are much longer than prompts (for plain Korean on Opus 5.5, 6,464 answer tokens against 303 prompt tokens over 10 requests) and output tokens cost 400% more than input, so the extra prompt tokens of the most polite version are worth about {share:.1f}% of a message's cost on Opus 5.5. Measured totals for the most polite level against plain: Korean {_pct(round(cost3["ko"] * 100))}, Japanese {_pct(round(cost3["ja"] * 100))}, English {_pct(round(cost3["en"] * 100))}. Most of any difference in cost comes from how long the answer is, not from the courtesy phrases.</li>
        <li><strong>Where it does add up: text that is sent again and again.</strong> A system prompt, a template or a CLAUDE.md is resent with every request, so greetings and courtesy phrases there cost on every call. In a one-off chat message they barely register.</li>
      </ul>
      <h2>Results on Claude Opus 5.5</h2>
      <p class="text-sm text-zinc-400">Sum of 10 requests per level, mean of two runs. Prompt tokens exclude the fixed system prompt. Cost = prompt and answer tokens at API list prices ($4 / $20 per million). Haiku 5.5 results and every single request are in the CSV.</p>
{_table(head, trs_html)}      <h2>The four levels</h2>
      <ul>
        <li><strong>Korean:</strong> 반말 (&ldquo;추천해 줘&rdquo;), 해요체 (&ldquo;추천해 주세요&rdquo;), formal (&ldquo;추천해 주시겠습니까?&rdquo;), formal with &ldquo;안녕하세요! 바쁘신데 죄송하지만 &hellip; 감사합니다&rdquo;.</li>
        <li><strong>Japanese:</strong> 普通体 (&ldquo;考えて&rdquo;), です・ます (&ldquo;考えてください&rdquo;), 敬語 (&ldquo;ご提案いただけますでしょうか&rdquo;), 敬語 with &ldquo;お疲れ様です。お忙しいところ恐縮ですが &hellip; よろしくお願いいたします&rdquo;.</li>
        <li><strong>English:</strong> plain (&ldquo;Suggest&rdquo;), &ldquo;Please suggest&rdquo;, &ldquo;Could you please &hellip;? Thank you.&rdquo;, and &ldquo;Hi! Sorry to bother you, but could you please &hellip;? Thanks so much!&rdquo;.</li>
      </ul>
      <h2>Method</h2>
      <ul>
        <li>10 everyday requests (email subject lines, a Python question, a date plan, a translation, a template, Excel help, blog titles, a self-introduction, a spelling fix, work-from-home tips), each written at four politeness levels in three languages: 120 prompts. All prompts are in the downloads.</li>
        <li>Each prompt sent once per run to Claude Code 2.1.295 as a plain chat: <code>claude -p --system-prompt "You are a helpful assistant." --tools ""</code>, no MCP servers. Opus 5.5 twice, Haiku 5.5 once, on {POL_MEASURED}. Prompt tokens = the run's input tokens minus a one-character baseline run.</li>
        <li>GPT token counts with js-tiktoken (o200k_base and cl100k_base).</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>One-turn chats. In a long conversation every earlier message is sent again, so polite phrases in it are paid for repeatedly, though they stay small next to the answers.</li>
        <li>Answer length varies a lot from run to run; two runs on Opus and one on Haiku cannot rule out a small effect of politeness on the answers.</li>
        <li>We do not measure whether politeness changes answer quality.</li>
      </ul>
'''
    return (_head("Does being polite to AI cost more?", lead,
                  f'Measured {POL_MEASURED} · Claude Opus 5.5 and Haiku 5.5 · 3 languages × 10 requests × 4 levels · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{LTI_PATH}">Language Tax Index</a>',
                  [("ai-politeness-token-cost.csv", "CSV"), ("ai-politeness-token-cost.json", "JSON")],
                  POL_CHART, "Prompt tokens and total cost by politeness level in Korean, Japanese and English", doi=POL_DOI, mirrors=POL_MIRRORS)
            + body + _page_tail(pol_citation(), _embed(POL_PATH, POL_CHART, "Politeness and AI token cost", "Does being polite to AI cost more?"),
                                [(LTI_PATH, "Language Tax Index"), (LANG_PATH, "Token cost by language"), (AMD_PATH, "CLAUDE.md and AGENTS.md size")]))


# ---- Dataset 17: coffee-break tax: the next message after a pause (measured 2026-10-20) ----
COF_PATH = "/data/ai-coffee-break-cache-cost"
COF_MEASURED = "2026-10-20"
COF_CHART = "/ai-coffee-break-cache-cost-chart.png"
COF_DOI = "10.5281/zenodo.23489501"  # concept DOI
COF_MIRRORS = [("Zenodo", "https://zenodo.org/records/23489502"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/ai-coffee-break-cache-cost"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/coffee-break-tax-claude-code-prompt-cache"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/coffee-break")]
COF_TITLE = "The coffee-break tax: what your next Claude Code message costs after a 0 to 65 minute pause"
COF_DESC = ("Dataset: Claude Code (Opus 5.5) builds a game, waits 0, 4, 6, 15, 30, 55 or 65 minutes, then gets a small change request in the same session: "
            "cache reads and writes and the cost of that next message. Up to 55 minutes nothing changed; after 65 minutes the cache was gone and the message cost about 500% more. Free CSV, CC BY 4.0.")
COF_COLS = ["wait_min", "rep", "actual_gap_s", "turn1_cost_usd", "turn2_cost_usd", "turn2_first_call_cache_read", "turn2_first_call_cache_write",
            "turn2_first_call_cache_write_1h", "turn2_first_call_cache_write_5m", "turn2_cache_write_total", "turn2_cache_read_total", "turn2_model_calls", "cache_hit"]


def _cof():
    return json.load(open(os.path.join(ROOT, "blog_data", "coffee", "combined.json"), encoding="utf-8"))


def cof_citation():
    if COF_DOI:
        return f"TokenSave (2026). {COF_TITLE} [Data set]. Zenodo. https://doi.org/{COF_DOI}"
    return f"TokenSave (2026). {COF_TITLE} [Data set]. {BASE}{COF_PATH}"


def write_cof_files(dist):
    d = _cof()
    buf = io.StringIO(); w = csv.writer(buf); w.writerow(COF_COLS)
    for r in d["rows"]:
        w.writerow([r.get(c) for c in COF_COLS])
    open(os.path.join(dist, "data", "ai-coffee-break-cache-cost.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=COF_TITLE, url=BASE + COF_PATH, license="CC BY 4.0", measured=COF_MEASURED, citation=cof_citation(), tool=d["tool"],
                turn1_prompt=d["turn1_prompt"], turn2_prompt=d["turn2_prompt"], rows=d["rows"])
    open(os.path.join(dist, "data", "ai-coffee-break-cache-cost.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def cof_ld():
    return _dataset_ld(COF_TITLE, COF_DESC, COF_PATH, COF_MEASURED,
                       ["prompt caching", "cache TTL", "Claude Code", "coffee break", "AI coding cost", "session", "resume"],
                       ["pause length (minutes)", "cache read tokens", "cache write tokens", "API cost of the next message (USD)"],
                       "Claude Code 2.1.295 (Opus 5.5) at medium effort on one Windows laptop; one session per pause length, all started together",
                       COF_CHART, [("ai-coffee-break-cache-cost.csv", "text/csv"), ("ai-coffee-break-cache-cost.json", "application/json")], doi=COF_DOI, mirrors=COF_MIRRORS)


def cof_waits(d=None):
    d = d or _cof(); R = d["rows"]
    waits = sorted({r["wait_min"] for r in R})
    return {w: [r for r in R if r["wait_min"] == w] for w in waits}


def cof_html():
    d = _cof(); W = cof_waits(d); R = d["rows"]
    f = lambda v: "{:,}".format(round(v))
    reps = len({r["rep"] for r in R})
    mc = lambda w: statistics.mean(r["turn2_cost_usd"] for r in W[w])
    warm = [w for w in W if w < 60]; cold = [w for w in W if w > 60]
    warm_cost = statistics.mean(r["turn2_cost_usd"] for w in warm for r in W[w])
    cold_cost = statistics.mean(r["turn2_cost_usd"] for w in cold for r in W[w])
    cold_write = statistics.mean(r["turn2_first_call_cache_write"] for w in cold for r in W[w])
    warm_read = statistics.mean(r["turn2_first_call_cache_read"] for w in warm for r in W[w])
    trs = "\n".join(
        '          <tr><td class="tabular-nums">%d min</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">$%.3f</td><td>%s</td></tr>' % (
            w, f(statistics.mean(r["turn2_first_call_cache_read"] for r in W[w])), f(statistics.mean(r["turn2_first_call_cache_write"] for r in W[w])),
            mc(w), "still cached" if all(r["cache_hit"] for r in W[w]) else "cache expired, rebuilt")
        for w in W)
    head = ['<th>Pause</th>', '<th class="text-right">Read from cache</th>', '<th class="text-right">Written to cache</th>',
            '<th class="text-right">Cost of the next message</th>', '<th>Cache</th>']
    ratio = cold_cost / warm_cost
    lead = ('<strong>Take a break of up to an hour and your next Claude Code message costs the same. Take longer, and it costs %d%% more.</strong> '
            'In our runs Claude Code kept the conversation in Anthropic&rsquo;s prompt cache for one hour. After pauses of 0 to 55 minutes the next message read %s tokens from the cache and cost $%.3f; '
            'after 65 minutes the cache had expired, %s tokens had to be written again, and the same message cost $%.3f.') % (round((ratio - 1) * 100), f(warm_read), warm_cost, f(cold_write), cold_cost)
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Nothing changed for an hour.</strong> After pauses of {", ".join(str(w) for w in warm)} minutes, the first model call of the next message read about {f(warm_read)} tokens from the cache and wrote only a few hundred new ones. The message cost ${warm_cost:.3f} on average whether we waited 0 minutes or 55.</li>
        <li><strong>After 65 minutes the cache was gone.</strong> The first call had to write {f(cold_write)} tokens to the cache again, at 100% more than the normal input price, and the message cost ${cold_cost:.3f} ({_pct(round((ratio - 1) * 100))}).</li>
        <li><strong>The cache lifetime was one hour.</strong> Every cache write in these runs was a one-hour write (<code>ephemeral_1h</code> in the usage report), not the five-minute default of the Anthropic API. That is why the 6- and 15-minute pauses, which would have missed a five-minute cache, cost nothing extra.</li>
        <li><strong>The bigger the project, the bigger the tax.</strong> Here the context was a small game of about 40,000 tokens. The cost of a cold start grows with everything in the conversation, so after a long session (our <a href="/data/long-chat-vs-new-chat-cost">long-chat measurement</a> reached 200,000 tokens of context and more) an expired cache costs far more.</li>
      </ul>
      <h2>The next message after each pause</h2>
      <p class="text-sm text-zinc-400">First model call of the next message: tokens read from and written to the prompt cache. Cost is the API list-price estimate for the whole message (Opus 5.5). {"Mean of %d runs." % reps if reps > 1 else "One run per pause; a second round is planned."} Every run is in the CSV.</p>
{_table(head, trs)}      <h2>What to take from it</h2>
      <ul>
        <li>Short breaks are free. Lunch is not: if you come back after more than an hour, the first message pays to rebuild the cache.</li>
        <li>If you know you will be away for longer, it can be cheaper to start a fresh, small session for the next task than to resume a huge one.</li>
        <li>On a subscription this shows up as usage-limit consumption rather than a bill.</li>
      </ul>
      <h2>Method</h2>
      <ul>
        <li>Claude Code 2.1.295 with Opus 5.5 on one Windows laptop, signed in with a subscription, <code>claude -p --effort medium --permission-mode acceptEdits</code>, no MCP servers. Turn 1: &ldquo;{esc(d["turn1_prompt"])}&rdquo;. After the pause, turn 2 with <code>--resume</code>: &ldquo;{esc(d["turn2_prompt"])}&rdquo;.</li>
        <li>One session per pause length, all started within a minute of each other on {COF_MEASURED}, so the sessions overlapped in time. Cache reads and writes come from the <code>usage</code> of each model call in the stream-json log; cost from <code>total_cost_usd</code>.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>The cache lifetime is set by Claude Code and Anthropic and may differ by login type, version or settings; with an API key and a five-minute cache the break-even pause would be much shorter.</li>
        <li>Because the sessions ran at the same time, part of the shared system prompt may have stayed cached through the other sessions: after 65 minutes about {f(statistics.mean(r["turn2_first_call_cache_read"] for w in cold for r in W[w]))} tokens were still read from the cache. A lone session may pay a little more.</li>
        <li>Codex runs were started too but stalled on file writes when many ran in parallel, so they are left out.</li>
      </ul>
'''
    return (_head("The coffee-break tax: your next Claude Code message after a pause", lead,
                  f'Measured {COF_MEASURED} · Claude Code (Opus 5.5) · pauses of {", ".join(str(w) for w in W)} minutes · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="/data/long-chat-vs-new-chat-cost">Long chat or new chat?</a>',
                  [("ai-coffee-break-cache-cost.csv", "CSV"), ("ai-coffee-break-cache-cost.json", "JSON")],
                  COF_CHART, "Cost of the next Claude Code message after pauses from 0 to 65 minutes", doi=COF_DOI, mirrors=COF_MIRRORS)
            + body + _page_tail(cof_citation(), _embed(COF_PATH, COF_CHART, "Cost of the next message after a pause", "The coffee-break tax"),
                                [("/data/long-chat-vs-new-chat-cost", "Long chat or new chat?"), (HAR_PATH, "What the Claude Code harness costs"), ("/blog/claude-code-save-tokens", "How to save tokens in Claude Code")]))


# ---- Dataset 18: text rendered as images (pxpipe) on Claude: tokens vs exact values (measured 2026-10-21) ----
TAI_PATH = "/data/text-as-image-token-cost"
TAI_MEASURED = "2026-10-21"
TAI_CHART = "/text-as-image-token-cost-chart.png"
TAI_DOI = "10.5281/zenodo.23525350"  # concept DOI
TAI_MIRRORS = [("Zenodo", "https://zenodo.org/records/23525351"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/text-as-image-token-cost"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/text-as-images-ai-token-cost-pxpipe-on-claude"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/text-as-image")]
TAI_TITLE = "Text as images to cut AI tokens: an independent check of pxpipe on Claude"
TAI_DESC = ("Dataset: six documents (English, Korean and Japanese prose, code, JSON, a server log) sent to Claude Haiku, Sonnet and Opus 5.5 and Fable 5.1 "
            "as plain text and as pxpipe images. Input tokens fell 64% to 81%, but exact ids and numbers were often lost: ids not in pxpipe's factsheet were read 0 of 80 times. Free CSV, CC BY 4.0.")
TAI_MODELS = [("claude-haiku-5-5", "Haiku 5.5"), ("claude-sonnet-5-5", "Sonnet 5.5"), ("claude-opus-5-5", "Opus 5.5"), ("claude-fable-5-1", "Fable 5.1")]
TAI_DOCS = [("prose_en", "English prose"), ("prose_ko", "Korean prose"), ("prose_ja", "Japanese prose"), ("code", "Code"), ("json", "JSON"), ("log", "Server log")]
TAI_TYPES = ["planted_hex", "planted_num", "natural_hex", "natural_num"]
TAI_COLS = ["model", "doc", "arm", "rep", "input_tokens", "output_tokens"] + [t + s for t in TAI_TYPES for s in ("_correct", "_wrong", "_null")]


def _tai():
    return json.load(open(os.path.join(ROOT, "blog_data", "pxpipe", "combined.json"), encoding="utf-8"))


def tai_citation():
    if TAI_DOI:
        return f"TokenSave (2026). {TAI_TITLE} [Data set]. Zenodo. https://doi.org/{TAI_DOI}"
    return f"TokenSave (2026). {TAI_TITLE} [Data set]. {BASE}{TAI_PATH}"


def write_tai_files(dist):
    d = _tai()
    buf = io.StringIO(); w = csv.writer(buf); w.writerow(TAI_COLS)
    for r in d["rows"]:
        w.writerow([r.get(c) for c in TAI_COLS])
    open(os.path.join(dist, "data", "text-as-image-token-cost.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=TAI_TITLE, url=BASE + TAI_PATH, license="CC BY 4.0", measured=TAI_MEASURED, citation=tai_citation(),
                tool=d["tool"], pxpipe=d["pxpipe"], docs=d["docs"], rows=d["rows"])
    open(os.path.join(dist, "data", "text-as-image-token-cost.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def tai_ld():
    return _dataset_ld(TAI_TITLE, TAI_DESC, TAI_PATH, TAI_MEASURED,
                       ["pxpipe", "text as image", "vision tokens", "context compression", "Claude Code", "token cost", "OCR accuracy", "Korean", "Japanese"],
                       ["input tokens per document", "exact values answered correctly", "wrong answers", "null answers"],
                       "Claude Code 2.1.295 (claude -p, stream-json input, no tools) on one Windows laptop; images made with pxpipe-proxy 0.15.0's own transform",
                       TAI_CHART, [("text-as-image-token-cost.csv", "text/csv"), ("text-as-image-token-cost.json", "application/json")], doi=TAI_DOI, mirrors=TAI_MIRRORS)


def tai_stats(d=None):
    d = d or _tai(); R = d["rows"]
    tok = lambda m, doc, arm: statistics.mean(r["input_tokens"] for r in R if r["model"] == m and r["doc"] == doc and r["arm"] == arm)
    def score(m, arm, types):
        c = wr = t = 0
        for r in R:
            if r["model"] == m and r["arm"] == arm:
                for ty in types:
                    if r[ty + "_correct"] is not None:
                        c += r[ty + "_correct"]; wr += r[ty + "_wrong"]; t += r[ty + "_correct"] + r[ty + "_wrong"] + r[ty + "_null"]
        return c, wr, t
    return tok, score


def tai_html():
    d = _tai(); tok, score = tai_stats(d)
    f = lambda v: "{:,}".format(round(v))
    cut = lambda m, doc: (tok(m, doc, "px") / tok(m, doc, "text") - 1) * 100
    cuts = [cut(m, doc) for m, _ in TAI_MODELS for doc, _ in TAI_DOCS]
    lo, hi = min(cuts), max(cuts)
    nat = [score(m, "px", ["natural_hex"]) for m, _ in TAI_MODELS]
    nat_c, nat_t = sum(x[0] for x in nat), sum(x[2] for x in nat)
    op = "claude-opus-5-5"
    tok_rows = "\n".join(
        '          <tr><td>%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td></tr>' % (
            lab, f(tok(op, doc, "text")), f(tok(op, doc, "px")), _pct(round(cut(op, doc))), _pct(round(cut("claude-fable-5-1", doc))))
        for doc, lab in TAI_DOCS)
    tok_head = ['<th>Document</th>', '<th class="text-right">As text</th>', '<th class="text-right">As pxpipe images</th>',
                '<th class="text-right">Change</th>', '<th class="text-right">Change (Fable profile)</th>']
    def cell(m, arm, types):
        c, wr, t = score(m, arm, types)
        return '%d/%d%s' % (c, t, (' <span class="text-zinc-500">(%d wrong)</span>' % wr) if wr else '')
    rec_rows = "\n".join(
        '          <tr><td>%s</td><td>%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td></tr>' % (
            lab, arm_l, cell(m, arm, ["planted_hex"]), cell(m, arm, ["planted_num"]), cell(m, arm, ["natural_hex"]), cell(m, arm, ["natural_num"]))
        for m, lab in TAI_MODELS for arm, arm_l in (("px", "pxpipe"), ("img", "images only")))
    rec_head = ['<th>Model</th>', '<th>Input</th>', '<th class="text-right">Planted ids</th>', '<th class="text-right">Planted numbers</th>',
                '<th class="text-right">Other ids (JSON, log)</th>', '<th class="text-right">Other numbers (JSON, log)</th>']
    oc, ow, ot = score(op, "px", ["planted_num"])
    lead = ('<strong>Rendering context as images really does cut Claude&rsquo;s input tokens, by %d%% to %d%% in our runs. '
            'But exact values did not survive: ids that pxpipe did not copy into its text factsheet were read back %d of %d times.</strong> '
            'pxpipe is an open-source proxy that turns bulky Claude Code context into dense PNG pages. We sent the same six documents as text and through pxpipe&rsquo;s own transform '
            'and asked four Claude models for values in them. As text, every model answered every item correctly.') % (round(-hi), round(-lo), nat_c, nat_t)
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>The token cut is real.</strong> Across six documents, the pxpipe version needed {round(-hi)}% to {round(-lo)}% fewer input tokens than plain text. Haiku, Sonnet and Opus 5.5 use the same tokenizer and image profile, so their counts matched; Fable&rsquo;s denser profile cut a few points more.</li>
        <li><strong>Non-English text gained most.</strong> Korean prose went from {f(tok(op, "prose_ko", "text"))} to {f(tok(op, "prose_ko", "px"))} tokens ({_pct(round(cut(op, "prose_ko")))}), Japanese {_pct(round(cut(op, "prose_ja")))}, English {_pct(round(cut(op, "prose_en")))}: the more tokens a language costs as text, the more an image saves.</li>
        <li><strong>Ids came back mostly through the factsheet, not the image.</strong> pxpipe adds a text list of &ldquo;exact identifiers&rdquo; next to the images. Our planted ids were all in it. Ids that were not, such as most request ids in the 230-line log (94 of 235 ids made the list), were read {nat_c} of {nat_t} times across all four models.</li>
        <li><strong>Numbers were the weak spot.</strong> Even the best model, Opus 5.5, gave the right planted number {oc} of {ot} times. In Korean prose it got 3 of 10.</li>
        <li><strong>Wrong answers were silent.</strong> Models were told to answer null if unsure. Some still answered with a plausible wrong value: a digit dropped (94392 read as 9392), a number that is not in the document, or, for Fable 5.1, a real value from the factsheet attached to the wrong ticket.</li>
      </ul>
      <h2>Input tokens per document</h2>
      <p class="text-sm text-zinc-400">Tokens the document added to the request (call input minus the same call with only the question). Opus 5.5 shown; Haiku and Sonnet 5.5 were the same within a few tokens. Mean of 2 runs.</p>
{_table(tok_head, tok_rows)}      <h2>Exact values read back</h2>
      <p class="text-sm text-zinc-400">Correct answers out of all asked, both runs together. As plain text, all four models answered every item correctly. &ldquo;pxpipe&rdquo; is images plus pxpipe&rsquo;s factsheet, as the proxy sends them; &ldquo;images only&rdquo; leaves the factsheet out. &ldquo;Other&rdquo; values are ids and numbers that were already in the JSON and log, not planted by us.</p>
{_table(rec_head, rec_rows)}      <h2>What to take from it</h2>
      <ul>
        <li>Use image context for what the model needs to understand, not for what it needs to copy. Ids, hashes, prices and line numbers should stay text.</li>
        <li>Don&rsquo;t judge it by one ID test. A value that happens to be in the factsheet comes back fine; most values in a large log won&rsquo;t be in it.</li>
        <li>Haiku 5.5 read the pages poorly. pxpipe does not enable Haiku by default (Sonnet 5.5 is opt-in, Opus 5.5 and Fable are on by default).</li>
      </ul>
      <h2>Method</h2>
      <ul>
        <li>Six documents of 10,600 to 23,200 characters: one of our own articles in English, Korean and Japanese, part of our usage-analyzer source code, a generated JSON API response and a generated server log. Into each we planted five lines like &ldquo;ticket T123 uses build hash 3f9a1c7e02bd and a timeout of 19043 ms&rdquo;; for the JSON and the log we also asked for five existing records (an id and a number each). 10 or 20 items per document.</li>
        <li>Images came from pxpipe-proxy 0.15.0&rsquo;s own <code>transformAnthropicMessages</code>, with the document as an earlier tool result: Opus 5.5&rsquo;s spaced profile for Haiku, Sonnet and Opus 5.5, the dense Fable profile for Fable 5.1. We sent the page images and the factsheet text exactly as returned, followed by the question.</li>
        <li>Claude Code 2.1.295 on one Windows laptop, signed in with a subscription: <code>claude -p --input-format stream-json --tools ""</code>, no MCP servers, system prompt &ldquo;Answer from the provided document only. Never guess: use null for anything you cannot read with certainty.&rdquo; Two runs per model, document and input type (144 calls), plus one question-only call per model and document for the token baseline. Answers were scored by exact match after removing spaces, commas and a trailing &ldquo;ms&rdquo;.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>Two runs per cell, six documents: small samples. Treat single cells as examples.</li>
        <li>We tested exact recall only. pxpipe&rsquo;s own tests report good results on gist, state and arithmetic questions, which we did not repeat.</li>
        <li>In real use pxpipe images older history and the system prompt, while recent turns stay text; we imaged one whole document at a time. Savings on a full Claude Code bill depend on how much of each request is imaged and cached.</li>
        <li>pxpipe changes quickly; this is version 0.15.0 on {TAI_MEASURED}.</li>
      </ul>
'''
    return (_head("Text as images: fewer AI tokens, fewer exact values", lead,
                  f'Measured {TAI_MEASURED} · Claude Haiku, Sonnet, Opus 5.5 and Fable 5.1 · pxpipe 0.15.0 · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{IMG_PATH}">Image token cost</a>',
                  [("text-as-image-token-cost.csv", "CSV"), ("text-as-image-token-cost.json", "JSON")],
                  TAI_CHART, "Input tokens as text and as pxpipe images, and exact values read back, on four Claude models", doi=TAI_DOI, mirrors=TAI_MIRRORS)
            + body + _page_tail(tai_citation(), _embed(TAI_PATH, TAI_CHART, "Text as images: tokens and exact values", "Text as images to cut AI tokens"),
                                [(IMG_PATH, "Image token cost on Claude, Gemini and GPT"), (LTI_PATH, "Language Tax Index"), (FMT_PATH, "Token cost by data format")]))


# ---- Dataset 19: Claude Code baseline tokens by version (measured 2026-10-21) ----
CCV_PATH = "/data/claude-code-baseline-tokens-by-version"
CCV_MEASURED = "2026-10-21"
CCV_CHART = "/claude-code-baseline-tokens-chart.png"
CCV_DOI = "10.5281/zenodo.23527278"  # concept DOI
CCV_MIRRORS = [("Zenodo", "https://zenodo.org/records/23527279"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/claude-code-baseline-tokens-by-version"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/claude-code-baseline-tokens-by-version"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/claude-code-versions")]
CCV_TITLE = "Claude Code baseline tokens by version: what every request carries before you type"
CCV_DESC = ("Dataset: the input tokens of Claude Code's first request for the one-letter prompt \"a\", measured on {n} versions from July 2025 to October 2026, "
            "with MCP off and with 16 claude.ai connectors on. The baseline rose 86% to a peak in May 2026, then fell back to half that by October. Free CSV, CC BY 4.0.")
CCV_COLS = ["version", "released", "arm", "runs", "first_request_input_tokens", "min", "max", "tools", "builtin_tools", "mcp_tools", "connected_servers", "cache_write_1h"]


def _ccv():
    return json.load(open(os.path.join(ROOT, "blog_data", "ccversions", "combined.json"), encoding="utf-8"))


def ccv_citation():
    if CCV_DOI:
        return f"TokenSave (2026). {CCV_TITLE} [Data set]. Zenodo. https://doi.org/{CCV_DOI}"
    return f"TokenSave (2026). {CCV_TITLE} [Data set]. {BASE}{CCV_PATH}"


def write_ccv_files(dist):
    d = _ccv()
    buf = io.StringIO(); w = csv.writer(buf); w.writerow(CCV_COLS + ["builtin_tool_names"])
    for r in d["rows"]:
        w.writerow([r.get(c) for c in CCV_COLS] + [" ".join(r["builtin_tool_names"])])
    open(os.path.join(dist, "data", "claude-code-baseline-tokens-by-version.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=CCV_TITLE, url=BASE + CCV_PATH, license="CC BY 4.0", measured=CCV_MEASURED, citation=ccv_citation(),
                model=d["model"], prompt=d["prompt"], rows=d["rows"], not_measured=d["not_measured"])
    open(os.path.join(dist, "data", "claude-code-baseline-tokens-by-version.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def _ccv_clean(d=None):
    d = d or _ccv()
    key = lambda v: tuple(map(int, v.split(".")))
    return sorted([r for r in d["rows"] if r["arm"] == "clean"], key=lambda r: key(r["version"])), {r["version"]: r for r in d["rows"] if r["arm"] == "connectors"}


def ccv_ld():
    n = len(_ccv_clean()[0])
    return _dataset_ld(CCV_TITLE, CCV_DESC.format(n=n), CCV_PATH, CCV_MEASURED,
                       ["Claude Code", "system prompt", "baseline tokens", "context overhead", "MCP", "claude.ai connectors", "token usage", "version history"],
                       ["input tokens of the first request", "number of tools", "MCP tools from claude.ai connectors"],
                       "Each Claude Code version installed from npm on one Windows laptop and run with claude -p \"a\" (Claude Haiku 5.5), fresh config folder, 3 runs per version",
                       CCV_CHART, [("claude-code-baseline-tokens-by-version.csv", "text/csv"), ("claude-code-baseline-tokens-by-version.json", "application/json")], doi=CCV_DOI, mirrors=CCV_MIRRORS)


def ccv_html():
    d = _ccv(); C, K = _ccv_clean(d)
    f = lambda v: "{:,}".format(round(v))
    tok = lambda r: r["first_request_input_tokens"]
    first, last = C[0], C[-1]
    peak = max(C, key=tok)
    drops = [(a, b) for a, b in zip(C, C[1:])]
    big = min(drops, key=lambda ab: tok(ab[1]) / tok(ab[0]))
    pct = lambda a, b: round((b / a - 1) * 100)
    on = [r for r in C if r["version"] in K and K[r["version"]]["mcp_tools"] > 0]
    on_tok = [tok(K[r["version"]]) for r in on]
    on_tools = [K[r["version"]]["mcp_tools"] for r in on]
    before_on = [r for r in C if r["version"] in K and r not in on and tuple(map(int, r["version"].split("."))) < tuple(map(int, on[0]["version"].split(".")))]
    after_on = [r for r in C if r["version"] in K and tuple(map(int, r["version"].split("."))) > tuple(map(int, on[-1]["version"].split(".")))]
    srv = K[on[0]["version"]]["connected_servers"]
    prev = None; trs = []
    for r in C:
        ch = "" if prev is None else _pct(pct(tok(prev), tok(r)))
        k = K.get(r["version"])
        conn = f(tok(k)) if k else "&ndash;"
        trs.append('          <tr><td class="tabular-nums">%s</td><td class="tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%s</td><td class="text-right tabular-nums">%d</td><td class="text-right tabular-nums">%s</td></tr>' % (
            r["version"], r["released"], f(tok(r)), ch, r["builtin_tools"], conn))
        prev = r
    head = ['<th>Version</th>', '<th>Released</th>', '<th class="text-right">Baseline tokens</th>', '<th class="text-right">Change</th>',
            '<th class="text-right">Built-in tools</th>', '<th class="text-right">With connectors on</th>']
    nm = ", ".join(x["version"] for x in d["not_measured"])
    lead = ('<strong>Every Claude Code request starts with a fixed block of instructions and tool definitions. Between mid-2025 and May 2026 that block grew by %d%%, '
            'from %s tokens in %s to %s in %s, then came back down: version %s sends %s tokens before you type anything, half the peak.</strong> '
            'We installed %d versions from npm and sent each the one-letter prompt &ldquo;a&rdquo;.') % (
        pct(tok(first), tok(peak)), f(tok(first)), first["released"][:7], f(tok(peak)), peak["released"][:7], last["version"], f(tok(last)), len(C))
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Ten months of growth.</strong> Version {first["version"]} ({first["released"]}) sent {f(tok(first))} tokens with the prompt &ldquo;a&rdquo;. By {peak["version"]} ({peak["released"]}) it was {f(tok(peak))} ({_pct(pct(tok(first), tok(peak)))}). Built-in tools went from {first["builtin_tools"]} to {peak["builtin_tools"]} along the way: plan mode, task lists, scheduled tasks, worktrees and more.</li>
        <li><strong>The biggest single change was a cut.</strong> Between {big[0]["version"]} ({big[0]["released"]}) and {big[1]["version"]} ({big[1]["released"]}) the baseline fell from {f(tok(big[0]))} to {f(tok(big[1]))} tokens ({_pct(pct(tok(big[0]), tok(big[1])))}), with the same number of tools. Today&rsquo;s {f(tok(last))} is about where it was in mid-2025.</li>
        <li><strong>Connected apps once came along in full.</strong> Apps connected to a claude.ai account (connectors) are also available in Claude Code. In versions {on[0]["version"]} to {on[-1]["version"]} ({on[0]["released"]} to {on[-1]["released"]}), all of their tools were sent with every request: with the {srv} connected apps on our account that was {min(on_tool for on_tool in on_tools)}&ndash;{max(on_tools)} extra tools and about {f(statistics.mean(on_tok))} tokens for the prompt &ldquo;a&rdquo;, roughly {round(statistics.mean(on_tok) / statistics.mean(tok(r) for r in on))} times the baseline. {before_on[-1]["version"]} and earlier did not load them; by {after_on[0]["version"]} they were loaded only when needed, and the baseline is now the same with them on or off.</li>
        <li><strong>The numbers are exact and repeatable.</strong> Three runs of the same version gave the same count every time.</li>
      </ul>
      <h2>Baseline by version</h2>
      <p class="text-sm text-zinc-400">Input tokens of the first model request (uncached + cache read + cache write) for the prompt &ldquo;a&rdquo;, Claude Haiku 5.5, MCP off. &ldquo;With connectors on&rdquo; is the same request with the {srv} connected claude.ai apps of our account enabled (one run). Change is against the previous row.</p>
{_table(head, chr(10).join(trs))}      <h2>What to take from it</h2>
      <ul>
        <li>The baseline is paid on every request, but after the first one it is usually read from the prompt cache at a tenth of the input price or less. It matters most for short sessions, subagents (each starts with its own copy) and after the cache expires (see our <a href="/data/ai-coffee-break-cache-cost">coffee-break measurement</a>).</li>
        <li>If you used Claude Code between late March and May 2026 with many apps connected on claude.ai, sessions started with hundreds of thousands of tokens. Updating removes that cost.</li>
        <li>Your own number will be higher than ours: CLAUDE.md files, MCP servers, plugins, skills and hooks all add to it (see <a href="{HAR_PATH}">what the harness costs</a> and <a href="{AMD_PATH}">CLAUDE.md size</a>).</li>
      </ul>
      <h2>Method</h2>
      <ul>
        <li>Each version was installed with <code>npm install @anthropic-ai/claude-code@&lt;version&gt;</code> into its own folder on one Windows laptop and run as <code>claude -p "a" --model claude-haiku-5-5 --output-format stream-json --verbose</code>, in an empty folder, with auto-update off and a fresh config folder holding only the login (no user settings, CLAUDE.md, plugins or skills). MCP was off (<code>--strict-mcp-config</code> with an empty config, <code>ENABLE_CLAUDEAI_MCP_SERVERS=false</code>); the second set left our account&rsquo;s claude.ai connectors on.</li>
        <li>We count the usage of the first assistant message in the log, because some older versions made a second request for the same prompt and their final total counts both.</li>
        <li>Release dates are npm publish dates. Three runs per version with MCP off, one with connectors on, on {CCV_MEASURED}.</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>Versions {nm} would not install on Windows (early Claude Code required WSL), so the series starts in July 2025.</li>
        <li>One model (Haiku 5.5), one prompt, one machine. Tool definitions and the system prompt can differ by model, operating system and account features, so other setups will see other absolute numbers; the trend is what this shows.</li>
        <li>Old versions were run against today&rsquo;s API and account. Features the server switches on per account may make an old version send more or less than it did at release.</li>
        <li>The connector numbers depend on how many apps are connected; ours had {srv}.</li>
      </ul>
'''
    return (_head("What Claude Code sends before you type: baseline tokens by version", lead,
                  f'Measured {CCV_MEASURED} · {len(C)} versions, {C[0]["released"][:7]} to {C[-1]["released"][:7]} · Claude Haiku 5.5 · License <a href="{LICENSE}">CC BY 4.0</a> · Related: <a href="{HAR_PATH}">Claude Code harness cost</a>',
                  [("claude-code-baseline-tokens-by-version.csv", "CSV"), ("claude-code-baseline-tokens-by-version.json", "JSON")],
                  CCV_CHART, "Claude Code baseline input tokens by version, and with claude.ai connectors on", doi=CCV_DOI, mirrors=CCV_MIRRORS)
            + body + _page_tail(ccv_citation(), _embed(CCV_PATH, CCV_CHART, "Claude Code baseline tokens by version", "Claude Code baseline tokens by version"),
                                [(HAR_PATH, "What the Claude Code harness costs"), (AMD_PATH, "CLAUDE.md and AGENTS.md size"), ("/data/ai-coffee-break-cache-cost", "The coffee-break tax")]))



# ---- Dataset 20: browser MCP token cost (Playwright MCP, Chrome DevTools MCP) and tokensave-mcp-diet (measured 2026-10-22) ----
BMC_PATH = "/data/browser-mcp-token-cost"
BMC_MEASURED = "2026-10-22"
BMC_CHART = "/browser-mcp-token-cost-chart.png"
BMC_DOI = "10.5281/zenodo.23555401"  # concept DOI
BMC_MIRRORS = [("Zenodo", "https://zenodo.org/records/23555402"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/browser-mcp-token-cost"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/browser-mcp-token-cost-playwright-vs-devtools"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/browser-mcp"),
               ("GitHub (tokensave-mcp-diet)", "https://github.com/johnisking/tokensave-mcp-diet")]
BMC_TITLE = "Browser MCP token cost: Playwright MCP vs Chrome DevTools MCP, and what a snapshot diet saves"
BMC_DESC = ("Dataset: input tokens, cost and tool-result size for Playwright MCP and Chrome DevTools MCP in Claude Code (Opus 5.5) on 7 browser tasks, 94 runs. "
            "One full snapshot of a long Wikipedia article is about 206,000 Claude tokens; the tokensave-mcp-diet proxy turns it into a table of contents of about 1,100. Free CSV, CC BY 4.0.")
BMC_COLS = ["server", "mode", "task", "run", "input_tokens", "output_tokens", "api_cost_usd", "requests", "seconds", "max_tool_result_chars",
            "snapshot_raw_chars", "snapshot_result_chars", "snapshot_tokens_added", "snapshot_blocked_by_claude_code", "answered"]


def _bmc():
    return json.load(open(os.path.join(ROOT, "blog_data", "mcpdiet", "combined.json"), encoding="utf-8"))


def bmc_citation():
    if BMC_DOI:
        return f"TokenSave (2026). {BMC_TITLE} [Data set]. Zenodo. https://doi.org/{BMC_DOI}"
    return f"TokenSave (2026). {BMC_TITLE} [Data set]. {BASE}{BMC_PATH}"


def write_bmc_files(dist):
    d = _bmc()
    buf = io.StringIO(); w = csv.writer(buf); w.writerow(BMC_COLS + ["task_label", "tool_calls"])
    for r in d["rows"]:
        s = r["snapshots"][-1] if r["snapshots"] else {}
        w.writerow([r["server"], r["mode"], r["task"], r["run"], r["input_tokens"], r["output_tokens"], r["api_cost_usd"], r["requests"], r["seconds"],
                    r["max_tool_result_chars"], s.get("raw_snapshot_chars") or "", s.get("result_chars", ""), s.get("tokens_added_next_request", ""),
                    s.get("blocked_by_claude_code", ""), r["answered"], r["task_label"], " ".join(r["tool_calls"])])
    open(os.path.join(dist, "data", "browser-mcp-token-cost.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=BMC_TITLE, url=BASE + BMC_PATH, license="CC BY 4.0", citation=bmc_citation(), **d)
    open(os.path.join(dist, "data", "browser-mcp-token-cost.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def bmc_ld():
    return _dataset_ld(BMC_TITLE, BMC_DESC, BMC_PATH, BMC_MEASURED,
                       ["Playwright MCP tokens", "Chrome DevTools MCP tokens", "MCP token usage", "browser snapshot tokens", "Claude Code MCP cost", "reduce MCP tokens"],
                       ["input tokens per task", "API cost per task", "tool result size (characters)", "tokens added by one page snapshot"],
                       "Claude Code 2.1.295 with one browser MCP server per run (Playwright MCP 0.0.83 or Chrome DevTools MCP 1.11.0, headless), 7 tasks on public pages, 2 to 5 runs each, with and without the tokensave-mcp-diet proxy (versions 0.1 and 0.2)",
                       BMC_CHART, [("browser-mcp-token-cost.csv", "text/csv"), ("browser-mcp-token-cost.json", "application/json")], doi=BMC_DOI, mirrors=BMC_MIRRORS)


def bmc_html():
    d = _bmc(); R = d["rows"]; F = d["full_snapshot_claude_tokens"]
    f = lambda v: "{:,}".format(round(v))
    SRV = [("pw", "Playwright MCP"), ("cdt", "Chrome DevTools MCP")]
    pick = lambda srv, mode, task: [r for r in R if r["srv"] == srv and r["mode"].startswith(mode) and r["task"] == task]
    avg = lambda rs, k: statistics.mean(r[k] for r in rs)
    snap = lambda srv, mode, task: pick(srv, mode, task)[0]["snapshots"][-1]
    pct = lambda a, b: round((b / a - 1) * 100)
    rng = lambda rs: f"${min(r['api_cost_usd'] for r in rs):.3f}&ndash;${max(r['api_cost_usd'] for r in rs):.3f}"
    # everyday tasks, as shipped
    tasks = [("todo", "TodoMVC: add 3 items, complete 1"), ("wiki", "Wikipedia: designer and first year"), ("hn", "Hacker News: top 5 stories"), ("hist", "Wikipedia: 5 release dates")]
    trs = []
    for tk, lab in tasks:
        cells = []
        for s, _ in SRV:
            rs = pick(s, "as", tk)
            cells.append(f'<td class="text-right tabular-nums">{f(avg(rs, "input_tokens"))}</td><td class="text-right tabular-nums">${avg(rs, "api_cost_usd"):.2f}</td>'
                         f'<td class="text-right tabular-nums">{f(max(r["max_tool_result_chars"] for r in rs))}</td>')
        trs.append(f'          <tr><td>{esc(lab)}</td>{"".join(cells)}</tr>')
    head1 = ['<th>Task (2 runs each)</th>'] + [f'<th class="text-right">{n}: {k}</th>' for _, n in SRV for k in ("input", "cost", "largest result (chars)")]
    # snapshot tasks, as shipped vs diet
    trs2 = []
    for tk, lab in [("hnsnap", "Hacker News top 5, from a snapshot"), ("snapread", "Wikipedia facts, from a snapshot"), ("probe", "Wikipedia, one full snapshot")]:
        for s, n in SRV:
            b, g = pick(s, "as", tk), pick(s, "tokensave-mcp-diet 0.2", tk)
            sb, sg = b[0]["snapshots"][-1], g[0]["snapshots"][-1]
            nb = sum(1 for r in b for x in r["snapshots"][-1:] if x["blocked_by_claude_code"])
            sb_txt = (f(sb["tokens_added_next_request"]) if nb == 0 else "refused, saved to file" if nb == len(b) else f"refused in {nb} of {len(b)} runs")
            trs2.append(f'          <tr><td>{esc(lab)}</td><td>{n}</td><td class="text-right tabular-nums">{sb_txt}</td><td class="text-right tabular-nums">{f(sg["tokens_added_next_request"])}</td>'
                        f'<td class="text-right tabular-nums">${avg(b, "api_cost_usd"):.3f} <span class="text-zinc-500">({rng(b)})</span></td><td class="text-right tabular-nums">${avg(g, "api_cost_usd"):.3f} <span class="text-zinc-500">({rng(g)})</span></td>'
                        f'<td class="text-right tabular-nums">{_pct(pct(avg(b, "api_cost_usd"), avg(g, "api_cost_usd")))}</td></tr>')
    head2 = ['<th>Task</th>', '<th>Server</th>', '<th class="text-right">Snapshot tokens, as shipped</th>', '<th class="text-right">With the diet</th>',
             '<th class="text-right">Task cost, as shipped</th>', '<th class="text-right">With the diet</th>', '<th class="text-right">Change</th>']
    hn_pw, hn_cdt = (snap("pw", "as", "hnsnap")["tokens_added_next_request"], snap("pw", "tokensave-mcp-diet 0.2", "hnsnap")["tokens_added_next_request"]), \
                    (snap("cdt", "as", "hnsnap")["tokens_added_next_request"], snap("cdt", "tokensave-mcp-diet 0.2", "hnsnap")["tokens_added_next_request"])
    wk_pw, wk_cdt = F["playwright_mcp_0.0.83"], F["chrome_devtools_mcp_1.11.0"]
    ol_pw, ol_cdt = snap("pw", "tokensave-mcp-diet 0.2", "probe")["tokens_added_next_request"], snap("cdt", "tokensave-mcp-diet 0.2", "probe")["tokens_added_next_request"]
    every = [r for r in R if r["mode"] == "as shipped" and r["task"] in ("todo", "wiki", "hn", "hist")]
    base_req = statistics.median(r["input_tokens"] / r["requests"] for r in every)
    lead = (f'<strong>On everyday browser tasks both servers were light: the largest tool result in 16 runs was {f(max(r["max_tool_result_chars"] for r in every))} characters, because Claude ran small scripts or searches instead of reading whole pages. '
            f'One full snapshot of a long Wikipedia article is another story: about {f(wk_pw)} Claude tokens from Playwright MCP and {f(wk_cdt)} from Chrome DevTools MCP.</strong> '
            f'Our open-source proxy, tokensave-mcp-diet 0.2, turned that into a table of contents of about {f(ol_pw)} and {f(ol_cdt)} tokens, cut a Hacker News snapshot by {abs(pct(hn_pw[0], hn_pw[1]))}% and {abs(pct(hn_cdt[0], hn_cdt[1]))}%, and made the Wikipedia fact-finding task cheaper on both servers.')
    body = f'''      <h2>Key findings</h2>
      <ul>
        <li><strong>Everyday tasks were cheap, and not because of the MCP.</strong> Filling a to-do list, finding facts on Wikipedia and reading Hacker News took 90,000 to 224,000 input tokens per task ($0.16 to $0.22 at API prices). Each request carried about {f(base_req)} tokens, most of it Claude Code&rsquo;s own instructions and tools; the browser results added little. Opus 5.5 preferred <code>evaluate</code> scripts and Playwright&rsquo;s <code>find</code> over full snapshots.</li>
        <li><strong>One full snapshot of a long page is over 200,000 tokens.</strong> The accessibility snapshot of the Python article on English Wikipedia was {f(F["chars"]["playwright"])} characters from Playwright MCP and {f(F["chars"]["chrome_devtools"])} from Chrome DevTools MCP. Sent to Opus 5.5 it counted {f(wk_pw)} and {f(wk_cdt)} tokens, about ${F["api_cost_usd_one_snapshot_cache_write"]["playwright"]:.2f} each at list price. (OpenAI&rsquo;s o200k tokenizer counts {f(F["o200k"]["playwright"])} and {f(F["o200k"]["chrome_devtools"])}.)</li>
        <li><strong>Claude Code already blocks that.</strong> It refused both results as too large, saved them to a file and told the model to read it in pieces. The task still got answered. Clients without such a limit would put the whole page into the context.</li>
        <li><strong>Medium pages get through, and that is where a diet pays off inside Claude Code.</strong> A Hacker News snapshot added {f(hn_pw[0])} tokens (Playwright) and {f(hn_cdt[0])} (Chrome DevTools). Through tokensave-mcp-diet: {f(hn_pw[1])} ({_pct(pct(*hn_pw))}) and {f(hn_cdt[1])} ({_pct(pct(*hn_cdt))}), with the same answer in all 5 runs. The whole task cost {abs(pct(avg(pick("pw", "as", "hnsnap"), "api_cost_usd"), avg(pick("pw", "tokensave-mcp-diet 0.2", "hnsnap"), "api_cost_usd")))}% and {abs(pct(avg(pick("cdt", "as", "hnsnap"), "api_cost_usd"), avg(pick("cdt", "tokensave-mcp-diet 0.2", "hnsnap"), "api_cost_usd")))}% less.</li>
        <li><strong>Very large pages: version 0.1 lost money, version 0.2 does not.</strong> Our first version sent a 9,000-token outline where Claude Code would have sent a short refusal note, and the Wikipedia tasks cost 3% to 44% more. Version 0.2 sends only a table of contents (headings with refs, about {f(ol_pw)} tokens) and lets the model open a section by its ref. With it, finding facts on the Python article cost {abs(pct(avg(pick("pw", "as", "snapread"), "api_cost_usd"), avg(pick("pw", "tokensave-mcp-diet 0.2", "snapread"), "api_cost_usd")))}% less on Playwright and {abs(pct(avg(pick("cdt", "as", "snapread"), "api_cost_usd"), avg(pick("cdt", "tokensave-mcp-diet 0.2", "snapread"), "api_cost_usd")))}% less on Chrome DevTools, and a bare full snapshot cost about the same as Claude Code&rsquo;s own refusal (+2% and +3%). Every task was answered correctly in all {len(R)} runs.</li>
      </ul>
      <h2>Everyday tasks, servers as shipped</h2>
      <p class="text-sm text-zinc-400">Average of 2 runs. Input = all input tokens of the task (uncached + cache read + cache write). Cost at Opus 5.5 API prices as reported by Claude Code. Largest result = the biggest single tool result in either run.</p>
{_table(head1, chr(10).join(trs))}      <h2>Snapshot tasks, with and without tokensave-mcp-diet 0.2</h2>
      <p class="text-sm text-zinc-400">The prompt asked for an accessibility snapshot and forbade JavaScript. &ldquo;Snapshot tokens&rdquo; = how much the next request grew after the snapshot came back. Cost = average of 5 runs (3 for the full-snapshot probe), lowest and highest run in brackets. The snapshot token counts varied by at most 4% between runs.</p>
{_table(head2, chr(10).join(trs2))}      <h2>What tokensave-mcp-diet does</h2>
      <p>It is a small open-source MCP proxy (<a href="https://github.com/johnisking/tokensave-mcp-diet">github.com/johnisking/tokensave-mcp-diet</a>, MIT) that sits in front of either server. Every tool passes through. When a page snapshot is over 8,000 characters it first removes noise (link targets, cursor marks, separators, empty layout wrappers) and keeps every element ref, so clicking still works. If the result is still over 20,000 characters it sends an outline of headings, form fields, buttons and links instead, and above 60,000 characters only a table of contents. The full snapshot stays in memory, and a new tool, <code>snapshot_detail</code>, returns any part of it by ref (a heading ref returns its whole section) or by text. The CSV also has the runs of version 0.1, which had no table of contents.</p>
      <h2>What to take from it</h2>
      <ul>
        <li>If an agent works through browser MCP in Claude Code, most of the bill is Claude Code&rsquo;s fixed per-request overhead and the number of steps, not the pages.</li>
        <li>The expensive case is a full snapshot of a long page. Ask for a specific element, a search or a script instead of &ldquo;read the page&rdquo;.</li>
        <li>In clients that pass large tool results straight through, one long page can add more than 200,000 tokens to the context. A proxy like tokensave-mcp-diet, or a server option that saves snapshots to files, keeps that out of the context.</li>
      </ul>
      <h2>Method</h2>
      <ul>
        <li>Claude Code 2.1.295, <code>claude -p &lt;prompt&gt; --effort medium --output-format stream-json --verbose</code>, model Opus 5.5, Windows 11, on {BMC_MEASURED}. Each run had exactly one MCP server (<code>--strict-mcp-config</code>) and could use only its tools: WebFetch, WebSearch, Bash, file tools and subagents were disabled.</li>
        <li>Servers: <code>@playwright/mcp@0.0.83</code> and <code>chrome-devtools-mcp@1.11.0</code>, both <code>--headless --isolated</code>. tokensave-mcp-diet 0.1.0 and 0.2.0 wrapped the same commands.</li>
        <li>Pages: demo.playwright.dev/todomvc, the English Wikipedia articles &ldquo;Python (programming language)&rdquo; and &ldquo;History of Python&rdquo;, and the Hacker News front page, live on the day. Snapshot tasks forbade JavaScript (<code>evaluate</code> tools disabled).</li>
        <li>The Claude token count of a full Wikipedia snapshot was measured by piping the saved snapshot text to <code>claude -p "Reply with OK only."</code> with no tools, minus an empty run ({f(2889)} tokens).</li>
      </ul>
      <h2>Limitations</h2>
      <ul>
        <li>Two runs per everyday task, five per snapshot task (three for the full-snapshot probe) for each version, one model, one machine, live pages that change during the day (Hacker News points moved between runs).</li>
        <li>Only Claude Code was measured. We did not test Claude Desktop, Cursor or Codex, so we do not know which of them pass a 200,000-token result through.</li>
        <li>Snapshot formats change between server versions; Playwright MCP already saves the snapshot to a file when navigating.</li>
        <li>The outline drops plain text, so the model must ask for details; on some tasks that adds steps.</li>
      </ul>
'''
    return (_head("How many tokens does browser MCP cost? Playwright vs Chrome DevTools, and a snapshot diet", lead,
                  f'Measured {BMC_MEASURED} · {len(R)} runs · Claude Code 2.1.295, Opus 5.5 · License <a href="{LICENSE}">CC BY 4.0</a> · Tool: <a href="https://github.com/johnisking/tokensave-mcp-diet">tokensave-mcp-diet</a> · Related: <a href="{AGT_PATH}">Claude Code vs Codex</a>',
                  [("browser-mcp-token-cost.csv", "CSV"), ("browser-mcp-token-cost.json", "JSON")],
                  BMC_CHART, "Claude tokens one browser MCP page snapshot adds, as shipped and with tokensave-mcp-diet", doi=BMC_DOI, mirrors=BMC_MIRRORS)
            + body + _page_tail(bmc_citation(), _embed(BMC_PATH, BMC_CHART, "Claude tokens one browser MCP page snapshot adds", "browser MCP token cost"),
                                [(AGT_PATH, "Claude Code vs Codex: startup tokens and MCP tools"), (HAR_PATH, "What the Claude Code harness costs"), (CCV_PATH, "Claude Code baseline tokens by version")]))


# ---- Dataset 21: Blender MCP token cost, with and without tokensave-mcp-diet 0.3 (measured 2026-10-22) ----
BLM_PATH = "/data/blender-mcp-token-cost"
BLM_MEASURED = "2026-10-22"
BLM_CHART = "/blender-mcp-token-cost-chart.png"
BLM_DOI = "10.5281/zenodo.23562484"  # concept DOI
BLM_MIRRORS = [("Zenodo", "https://zenodo.org/records/23562485"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/blender-mcp-token-cost"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/blender-mcp-token-cost-72-claude-code-runs"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/blender-mcp"),
               ("GitHub (tokensave-mcp-diet)", "https://github.com/johnisking/tokensave-mcp-diet")]
BLM_TITLE = "Blender MCP token cost: 72 Claude Code runs, from a table and chairs to a racing scene"
BLM_DESC = ("Dataset: input tokens, cost, images and tool-result size for MCP for Blender in Claude Code (Opus 5.5) on 8 tasks, 72 runs, with and without the tokensave-mcp-diet 0.3 proxy. "
            "Everyday tasks cost $0.16 to $0.23; a racing scene with a chase camera about $0.47; one long property dump $0.87, or $0.17 with the proxy. Free CSV, CC BY 4.0.")
BLM_TASKS = [("infoS", "Describe a small room (13 objects)"), ("infoL", "Describe a city block (580 objects)"), ("build", "Build a table and four chairs"),
             ("red", "Make the chairs red, then look"), ("sides", "Look at the table from four sides"), ("verts", "Probe: print every vertex (19,042)"),
             ("props", "Probe: print every property of 580 objects"), ("race", "Showcase: racing car, circuit, 5 s chase camera")]
BLM_COLS = ["mode", "task", "run", "input_tokens", "output_tokens", "api_cost_usd", "requests", "seconds", "tool_calls", "max_text_result_chars",
            "images", "image_tokens_est", "user_prompt_chars", "refused_too_large", "passed_check"]


def _blm():
    base = os.path.join(ROOT, "blog_data", "blendermcp")
    rows = json.load(open(os.path.join(base, "rows.json"), encoding="utf-8"))
    for r in rows:
        f = os.path.join(base, "facts", r["run"] + ".json")
        facts = json.load(open(f, encoding="utf-8")) if os.path.exists(f) else None
        t = r["task"]
        if t == "build":
            ok = bool(facts) and "Table" in facts["objects"] and all(f"Chair {i}" in facts["objects"] for i in range(1, 5))
        elif t == "red":
            cs = [v["colors"] for k, v in (facts or {}).get("objects", {}).items() if k.startswith("Chair")]
            ok = len(cs) == 4 and all(c and all(x[0] > 0.4 and x[1] < 0.2 and x[2] < 0.2 for x in c) for c in cs)
        elif t == "race":
            ok = bool(facts) and facts["frame_end"] >= 120 and facts["camera_anim"] and bool(facts["animated_objects"]) and facts["res"] == [1280, 720] and "EEVEE" in facts["engine"]
        elif t in ("verts", "props"):
            ok = bool(r["answer"].strip()) and not r.get("is_error")
        else:
            ok = bool(r["answer"].strip())
        r["passed_check"] = ok
    return rows


def blm_citation():
    if BLM_DOI:
        return f"TokenSave (2026). {BLM_TITLE} [Data set]. Zenodo. https://doi.org/{BLM_DOI}"
    return f"TokenSave (2026). {BLM_TITLE} [Data set]. {BASE}{BLM_PATH}"


def write_blm_files(dist):
    R = _blm()
    buf = io.StringIO(); w = csv.writer(buf); w.writerow(BLM_COLS + ["task_label", "calls"])
    lab = dict(BLM_TASKS)
    for r in R:
        w.writerow([r["mode"], r["task"], r["rep"], r["input_tokens"], r["output_tokens"], r["api_cost_usd"], r["requests"], r["seconds"], r["tool_calls"],
                    r["max_text_result_chars"], r["images"], r["image_tokens_est"], r["user_prompt_chars"], r["refused_too_large"], r["passed_check"],
                    lab[r["task"]], " ".join(r["calls"])])
    open(os.path.join(dist, "data", "blender-mcp-token-cost.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=BLM_TITLE, url=BASE + BLM_PATH, license="CC BY 4.0", citation=blm_citation(), measured=BLM_MEASURED,
                setup="Claude Code 2.1.295, Opus 5.5, effort medium, Windows 11; Blender 5.2.2 LTS; MCP for Blender (mcp-for-blender via uvx, add-on 1.8); tokensave-mcp-diet 0.3.0",
                tasks=lab, rows=R)
    open(os.path.join(dist, "data", "blender-mcp-token-cost.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def blm_ld():
    return _dataset_ld(BLM_TITLE, BLM_DESC, BLM_PATH, BLM_MEASURED,
                       ["Blender MCP tokens", "Blender MCP cost", "MCP for Blender", "Claude Code Blender", "MCP token usage", "reduce MCP tokens"],
                       ["input tokens per task", "API cost per task", "images and estimated image tokens", "largest text result (characters)"],
                       "Claude Code 2.1.295 with MCP for Blender only (Blender 5.2.2, add-on 1.8), 8 tasks on scenes generated by script, 3 to 5 runs each, with and without the tokensave-mcp-diet 0.3 proxy; results checked by reading the saved .blend file",
                       BLM_CHART, [("blender-mcp-token-cost.csv", "text/csv"), ("blender-mcp-token-cost.json", "application/json")], doi=BLM_DOI, mirrors=BLM_MIRRORS)


def blm_stats():
    R = _blm(); out = {}
    for t, _ in BLM_TASKS:
        for m in ("base", "diet"):
            rs = [r for r in R if r["task"] == t and r["mode"] == m]
            c = [r["api_cost_usd"] for r in rs]
            out[(t, m)] = dict(n=len(rs), inp=statistics.mean(r["input_tokens"] for r in rs), cost=statistics.mean(c), lo=min(c), hi=max(c),
                               sd=statistics.stdev(c) if len(c) > 1 else 0, img=statistics.mean(r["image_tokens_est"] for r in rs),
                               maxt=max(r["max_text_result_chars"] for r in rs), req=statistics.mean(r["requests"] for r in rs),
                               refused=sum(r["refused_too_large"] for r in rs), passed=sum(r["passed_check"] for r in rs),
                               up=statistics.mean(r["user_prompt_chars"] for r in rs), sec=statistics.mean(r["seconds"] for r in rs))
    return R, out


def blm_html():
    R, S = blm_stats()
    f = lambda v: "{:,}".format(round(v))
    pct = lambda a, b: round((b / a - 1) * 100)
    trs = []
    for t, lab in BLM_TASKS:
        b, d = S[(t, "base")], S[(t, "diet")]
        trs.append(f'          <tr><td>{esc(lab)}</td><td class="text-right tabular-nums">{b["n"]} + {d["n"]}</td>'
                   f'<td class="text-right tabular-nums">{f(b["inp"])}</td><td class="text-right tabular-nums">{f(d["inp"])}</td>'
                   f'<td class="text-right tabular-nums">${b["cost"]:.3f} <span class="text-zinc-500">(${b["lo"]:.2f}&ndash;${b["hi"]:.2f})</span></td>'
                   f'<td class="text-right tabular-nums">${d["cost"]:.3f} <span class="text-zinc-500">(${d["lo"]:.2f}&ndash;${d["hi"]:.2f})</span></td>'
                   f'<td class="text-right tabular-nums">{_pct(pct(b["cost"], d["cost"]))}</td>'
                   f'<td class="text-right tabular-nums">{f(b["maxt"])}</td><td class="text-right tabular-nums">{f(b["img"])} &rarr; {f(d["img"])}</td></tr>')
    head = ['<th>Task</th>', '<th class="text-right">Runs (base + diet)</th>', '<th class="text-right">Input tokens, as shipped</th>', '<th class="text-right">With the diet</th>',
            '<th class="text-right">Cost, as shipped</th>', '<th class="text-right">With the diet</th>', '<th class="text-right">Change</th>',
            '<th class="text-right">Largest text result (chars)</th>', '<th class="text-right">Image tokens (est.)</th>']
    EV = ("infoS", "infoL", "build", "red", "sides")
    every = [r for r in R if r["mode"] == "base" and r["task"] in EV]
    pb, pd = S[("props", "base")], S[("props", "diet")]
    rb, rd = S[("race", "base")], S[("race", "diet")]
    ib, idd = S[("infoS", "base")], S[("infoS", "diet")]
    npass = sum(r["passed_check"] for r in R)
    base_req = statistics.median(r["input_tokens"] / r["requests"] for r in every)
    lo_ev, hi_ev = min(S[(t, "base")]["cost"] for t in EV), max(S[(t, "base")]["cost"] for t in EV)
    lead = (f'<strong>Blender MCP is lighter than its reputation. Everyday tasks in Claude Code cost ${lo_ev:.2f} to ${hi_ev:.2f} each, '
            f'and a racing car with a circuit and a 5-second chase-camera animation cost ${rb["cost"]:.2f}.</strong> '
            f'The expensive case is a long script output: printing every property of 580 objects cost ${pb["cost"]:.2f}, and ${pd["cost"]:.2f} ({_pct(pct(pb["cost"], pd["cost"]))}) through our open-source tokensave-mcp-diet proxy. '
            f'Elsewhere the proxy saved little.')
    li = []
    li.append(f'<li><strong>Everyday tasks were cheap.</strong> Describing a scene, building a table with four chairs, recolouring the chairs and checking them with a screenshot took 69,000 to 126,000 input tokens per task. '
              f'The largest text result in {len(every)} everyday runs was {f(max(r["max_text_result_chars"] for r in every))} characters: the current MCP for Blender already returns short summaries (20 objects per call by default) and 768-pixel images. '
              f'Each request carried about {f(base_req)} tokens, most of it Claude Code&rsquo;s own instructions.</li>')
    li.append(f'<li><strong>A racing scene cost about ${rb["cost"]:.2f}.</strong> Claude built a low-poly car of its own design and a circuit with a corner, animated the car over 120 frames and added a chase camera, '
              f'in {rb["req"]:.1f} requests and about {round(rb["sec"])} seconds on average. All {rb["n"] + rd["n"]} runs produced a working animation.</li>')
    li.append(f'<li><strong>The expensive case is a long script output.</strong> Asked to print every property of 580 objects, the script returned 122,373 characters. Claude Code refused it as too large; Claude then re-ran it in four chunks of about 32,000 characters, '
              f'and all of them stayed in the context: {f(pb["inp"])} input tokens and ${pb["cost"]:.2f}, more than four times an everyday task.</li>')
    li.append(f'<li><strong>tokensave-mcp-diet 0.3 cut that case by {abs(pct(pb["cost"], pd["cost"]))}%.</strong> It keeps the first 2,000 and last 1,000 characters of any text result over 8,000, describes the hidden lines '
              f'(&ldquo;568 lines like: name=Building ## | type=MESH | location=(#, #, #) ...&rdquo;) and lets the model read any part with a new <code>result_detail</code> tool. The task cost ${pd["lo"]:.2f} to ${pd["hi"]:.2f} in its three runs.</li>')
    li.append(f'<li><strong>Elsewhere the proxy changed little, and we say so.</strong> It also asks for 512-pixel images by default, which cut image tokens by {abs(pct(rb["img"], rd["img"]))}% on the racing scene, but images were a small share of the input, '
              f'so the scene cost {abs(pct(rb["cost"], rd["cost"]))}% less ({rb["n"]} runs each, within run-to-run noise). The small-room description, where the proxy changed nothing, came out {abs(pct(ib["cost"], idd["cost"]))}% cheaper too, so treat differences under about 8% as noise.</li>')
    li.append(f'<li>Every task passed its check in {npass} of {len(R)} runs (read back from the saved .blend file: names, colours, frame range, camera, engine).</li>')
    body = ('      <h2>Key findings</h2>\n      <ul>\n' + "\n".join("        " + x for x in li) + '\n      </ul>\n'
            '      <figure class="my-6"><img src="/blender-mcp-race-scenes.jpg" alt="Frames from the 6 first racing-scene runs: low-poly race cars on circuits, seen from a chase camera" width="1440" height="1620" loading="lazy" class="rounded-lg">'
            '<figcaption class="text-sm text-zinc-400 mt-2">Frames 10, 60 and 110 from the first three runs without the proxy (top) and with it (bottom), rendered afterwards in EEVEE. Every car and circuit was designed by Claude in that run.</figcaption></figure>\n'
            '      <h2>All tasks, with and without tokensave-mcp-diet 0.3</h2>\n'
            '      <p class="text-sm text-zinc-400">Averages. Input = all input tokens of the task (uncached + cache read + cache write). Cost at Opus 5.5 API prices as reported by Claude Code, lowest and highest run in brackets. '
            'Image tokens estimated as width &times; height / 750 for every image returned. Largest text result is from the runs without the diet.</p>\n'
            + _table(head, chr(10).join(trs)) +
            '      <h2>What tokensave-mcp-diet 0.3 does for Blender</h2>\n'
            '      <p>The proxy (<a href="https://github.com/johnisking/tokensave-mcp-diet">github.com/johnisking/tokensave-mcp-diet</a>, MIT) sits in front of MCP for Blender and passes every tool through. Version 0.3 adds three things: '
            'long text results (over 8,000 characters) keep their head and tail plus a summary of the hidden lines, with the full text available through <code>result_detail</code>; '
            'tools with a <code>max_size</code> get 512-pixel images unless the model asks for more than 1,000; and an optional <code>--drop-user-prompt</code> flag removes the server&rsquo;s <code>user_prompt</code> argument (used for its opt-in telemetry), '
            f'which Claude filled with about {f(rb["up"])} characters per racing-scene run. That flag was off in these runs. Install: <code>npx -y github:johnisking/tokensave-mcp-diet -- uvx mcp-for-blender</code>.</p>\n'
            '      <p>One bug surfaced during the runs: MCP for Blender also sends each result as <code>structuredContent</code>, and Claude Code shows that instead of the text, so the first diet runs of the two probes were not shortened. '
            'Version 0.3 now shortens those fields too, and the probe runs were repeated after the fix in fresh working directories.</p>\n'
            '      <h2>Method</h2>\n      <ul>\n'
            f'        <li>Claude Code 2.1.295, <code>claude -p &lt;prompt&gt; --effort medium --output-format stream-json --verbose</code>, model Opus 5.5, Windows 11 with a GTX 1650, on {BLM_MEASURED}. Only the Blender MCP server was attached (<code>--strict-mcp-config</code>); web, file and shell tools were disabled, and so were the server&rsquo;s 3D-generation and asset-download tools.</li>\n'
            '        <li>Blender 5.2.2 LTS with the window open (screenshots need it); MCP for Blender via <code>uvx mcp-for-blender</code>, add-on 1.8, telemetry off. A fresh copy of the scene was opened for every run, and every run had its own working directory.</li>\n'
            '        <li>Scenes were generated by our own script, so they are identical in every run and contain no third-party assets: a room with 13 objects, a city block with 580 objects including a 19,042-vertex sphere, and an empty scene with a camera and a light.</li>\n'
            '        <li>After each run the scene was saved and checked headlessly: the named table and chairs, the chair colours, the frame range, the scene camera and its animation, the render engine and the resolution. The racing scenes were rendered afterwards, outside the measured runs.</li>\n'
            '        <li>Everyday tasks and the racing scene ran 5 times per mode, the two probes 3 times.</li>\n'
            '      </ul>\n      <h2>Limitations</h2>\n      <ul>\n'
            '        <li>One model, one machine, one client (Claude Code). Clients that do not refuse large results would take in all 122,000 characters of the property dump at once.</li>\n'
            f'        <li>Costs vary from run to run (racing scene: ${rb["lo"]:.2f} to ${rb["hi"]:.2f} without the diet), because Claude takes a different number of steps each time.</li>\n'
            '        <li>Image tokens are an estimate from the image size; the input totals are exact.</li>\n'
            f'        <li>MCP for Blender changes quickly; these results are for the version of {BLM_MEASURED}, which already keeps most results small.</li>\n'
            '      </ul>\n')
    return (_head(f"How many tokens does Blender MCP cost? 72 Claude Code runs, and a racing scene for ${rb['cost']:.2f}", lead,
                  f'Measured {BLM_MEASURED} · {len(R)} runs · Claude Code 2.1.295, Opus 5.5, Blender 5.2.2 · License <a href="{LICENSE}">CC BY 4.0</a> · Tool: <a href="https://github.com/johnisking/tokensave-mcp-diet">tokensave-mcp-diet</a> · Related: <a href="{BMC_PATH}">Browser MCP token cost</a>',
                  [("blender-mcp-token-cost.csv", "CSV"), ("blender-mcp-token-cost.json", "JSON")],
                  BLM_CHART, "Cost per task with MCP for Blender in Claude Code, with and without tokensave-mcp-diet", doi=BLM_DOI, mirrors=BLM_MIRRORS)
            + body + _page_tail(blm_citation(), _embed(BLM_PATH, BLM_CHART, "Blender MCP cost per task", "Blender MCP token cost"),
                                [(BMC_PATH, "Browser MCP token cost"), (AGT_PATH, "Claude Code vs Codex: startup tokens and MCP tools"), (HAR_PATH, "What the Claude Code harness costs")]))


# ---- Dataset 22: Antigravity CLI vs Claude Code vs Codex (measured 2026-10-22) ----
AGY_PATH = "/data/antigravity-cli-vs-claude-code-vs-codex"
AGY_MEASURED = "2026-10-22"
AGY_MEASURED_SHOW = "2026-10-18 to 2026-10-23"
AGY_CHART = "/antigravity-cli-vs-claude-code-vs-codex-chart.png"
AGY_DOI = "10.5281/zenodo.23569397"  # concept DOI
AGY_MIRRORS = [("Zenodo", "https://zenodo.org/records/23589130"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/antigravity-cli-vs-claude-code-vs-codex"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/antigravity-cli-vs-claude-code-vs-codex-44-runs"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/antigravity-cli")]
AGY_TITLE = "Antigravity CLI vs Claude Code vs Codex: startup tokens, MCP tools and the same coding task"
AGY_DESC = ("Dataset: input tokens Google's Antigravity CLI (with Gemini 4 Argon and with Claude Opus 5.5), Claude Code and Codex use before any work, what 1 to 30 MCP tools add, "
            "and tokens, time and output for the same browser-game task. Opus 5.5 used 71% to 89% fewer input tokens in Antigravity than in Claude Code. 52 runs, free CSV, CC BY 4.0.")
AGY_TOOLS = [("claude", "Claude Code + Opus 5.5"), ("codex", "Codex + gpt-6-luna"), ("agyg", "Antigravity + Gemini 4 Argon"), ("agyo", "Antigravity + Opus 5.5")]
AGY_COLS = ["tool", "test", "mcp_tools", "run", "input_tokens_reported", "cache_read_tokens", "output_tokens", "seconds", "api_cost_usd",
            "file_lines", "check_score", "check_level2", "check_lives", "game_ok", "check_note"]


def _agy():
    return json.load(open(os.path.join(ROOT, "blog_data", "agy3", "rows.json"), encoding="utf-8"))


def agy_citation():
    if AGY_DOI:
        return f"TokenSave (2026). {AGY_TITLE} [Data set]. Zenodo. https://doi.org/{AGY_DOI}"
    return f"TokenSave (2026). {AGY_TITLE} [Data set]. {BASE}{AGY_PATH}"


def write_agy_files(dist):
    R = _agy()
    buf = io.StringIO(); w = csv.writer(buf); w.writerow(AGY_COLS + ["tool_label"])
    lab = dict(AGY_TOOLS)
    for r in R:
        g = r["kind"] == "game"
        w.writerow([r["tool"], "game" if g else "startup", "" if g else r["n"], r["rep"], r["inp"], r.get("cache_read", 0), r["out"], r["seconds"],
                    r.get("cost", ""), r.get("lines", ""), r.get("check_score", ""), r.get("check_level2", ""), r.get("check_lives", ""),
                    r.get("game_ok", ""), r.get("check_note", ""), lab[r["tool"]]])
    open(os.path.join(dist, "data", "antigravity-cli-vs-claude-code-vs-codex.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=AGY_TITLE, url=BASE + AGY_PATH, license="CC BY 4.0", citation=agy_citation(), measured=AGY_MEASURED_SHOW,
                setup="Windows 11; Claude Code 2.1.295 (Opus 5.5, Max plan); Codex CLI 0.162.0-alpha.17.2 (gpt-6-luna, ChatGPT plan); Antigravity CLI 1.4.5 "
                      "(gemini-4-argon-medium and claude-opus-5-5-medium, personal Google account)",
                note=("input_tokens_reported is each CLI's own figure. Claude Code: input + cache creation + cache read. Codex: input including cached input. "
                      "Antigravity: the usage.input_tokens field of agy --output-format json; cache_read_tokens is reported separately and for the Opus runs is larger than input_tokens, "
                      "so it is not contained in it there. Read input_tokens_reported + cache_read_tokens as an upper bound for Antigravity."),
                tools=lab, rows=R)
    open(os.path.join(dist, "data", "antigravity-cli-vs-claude-code-vs-codex.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def agy_ld():
    return _dataset_ld(AGY_TITLE, AGY_DESC, AGY_PATH, AGY_MEASURED,
                       ["Antigravity CLI tokens", "Antigravity CLI vs Claude Code", "Gemini CLI replacement", "agy CLI", "Claude Code vs Codex", "AI coding agent tokens", "MCP tools tokens"],
                       ["input tokens before any work", "input tokens added by 1, 10 and 30 MCP tools", "input and output tokens for one coding task", "seconds", "whether the game works"],
                       "Each CLI run headless on Windows 11 with the same prompts: a one-word reply with 0, 1, 10 and 30 dummy MCP tools (2 runs each) and a brick-breaker game task (5 runs each); every game checked in a headless browser",
                       AGY_CHART, [("antigravity-cli-vs-claude-code-vs-codex.csv", "text/csv"), ("antigravity-cli-vs-claude-code-vs-codex.json", "application/json")],
                       doi=AGY_DOI or None, mirrors=AGY_MIRRORS)


def agy_stats():
    R = _agy(); B = {}; G = {}
    mean = statistics.mean
    for k, _ in AGY_TOOLS:
        for n in (0, 1, 10, 30):
            rs = [r for r in R if r["tool"] == k and r["kind"] == "base" and r["n"] == n]
            B[(k, n)] = dict(inp=mean(r["inp"] for r in rs), cache=mean(r.get("cache_read", 0) for r in rs))
        rs = [r for r in R if r["tool"] == k and r["kind"] == "game"]
        G[k] = dict(inp=mean(r["inp"] for r in rs), cache=mean(r.get("cache_read", 0) for r in rs), out=mean(r["out"] for r in rs),
                    sec=mean(r["seconds"] for r in rs), lines=mean(r["lines"] for r in rs), ok=sum(bool(r["game_ok"]) for r in rs), n=len(rs),
                    lo=min(r["inp"] for r in rs), hi=max(r["inp"] for r in rs),
                    cost=(mean(r["cost"] for r in rs) if all(r.get("cost") for r in rs) else None))
    return R, B, G


def agy_html():
    R, B, G = agy_stats()
    f = lambda v: "{:,}".format(round(v))
    pct = lambda a, b: round((b / a - 1) * 100)
    cc, ao, ag, cx = G["claude"], G["agyo"], G["agyg"], G["codex"]
    s_lo, s_hi = abs(pct(B[("claude", 0)]["inp"], B[("agyo", 0)]["inp"] + B[("agyo", 0)]["cache"])), abs(pct(B[("claude", 0)]["inp"], B[("agyo", 0)]["inp"]))
    g_lo, g_hi = abs(pct(cc["inp"], ao["inp"] + ao["cache"])), abs(pct(cc["inp"], ao["inp"]))
    lead = (f'<strong>The same model, Claude Opus 5.5, read {g_lo}% to {g_hi}% fewer input tokens in Google&rsquo;s Antigravity CLI than in Claude Code for the same coding task, '
            f'and {s_lo}% to {s_hi}% fewer before doing anything.</strong> Both made a working game. Gemini 4 Argon in Antigravity also stayed far below Claude Code and Codex. '
            'The range comes from one open question: whether Antigravity&rsquo;s separately reported cache reads should be added on top.')
    agy_add = lambda k, n: B[(k, n)]["inp"] - B[(k, 0)]["inp"]
    li = []
    li.append(f'<li><strong>Startup: {f(B[("claude", 0)]["inp"])} input tokens in Claude Code, {f(B[("codex", 0)]["inp"])} in Codex, {f(B[("agyg", 0)]["inp"])} in Antigravity with Gemini 4 Argon '
              f'and {f(B[("agyo", 0)]["inp"])} in Antigravity with Opus 5.5</strong> ({f(B[("agyo", 0)]["inp"] + B[("agyo", 0)]["cache"])} counting its cache reads), for the prompt &ldquo;Reply with the single word OK.&rdquo; with no MCP server. '
              'Most of it is each tool&rsquo;s own instructions and tool definitions, sent with every request.</li>')
    li.append(f'<li><strong>Same task, same model:</strong> asked to build a brick-breaker game, Opus 5.5 read {f(cc["inp"])} input tokens in Claude Code and {f(ao["inp"])} in Antigravity '
              f'({f(ao["inp"] + ao["cache"])} counting cache reads), wrote {f(cc["out"])} and {f(ao["out"])} output tokens, and took {round(cc["sec"])} and {round(ao["sec"])} seconds. '
              f'Claude Code&rsquo;s games were longer ({round(cc["lines"])} lines on average against {round(ao["lines"])}). Claude Code put the run at ${cc["cost"]:.2f} at API prices; Antigravity shows no price.</li>')
    li.append(f'<li><strong>Gemini 4 Argon in Antigravity</strong> read {f(ag["inp"])} input tokens ({f(ag["inp"] + ag["cache"])} counting cache reads) and wrote the longest games ({round(ag["lines"])} lines), but took the longest too ({round(ag["sec"])} seconds). '
              f'Codex read {f(cx["inp"])} on average ({f(cx["lo"])} to {f(cx["hi"])}) and wrote minified games of about {round(cx["lines"])} lines.</li>')
    li.append(f'<li><strong>MCP tools barely matter any more.</strong> Thirty test tools added {f(agy_add("claude", 30))} tokens in Claude Code, none in Codex (14,618 in seven of its eight startup runs, with or without tools), {f(agy_add("agyg", 30))} in Antigravity with Gemini and {f(agy_add("agyo", 30))} with Opus. '
              f'In Antigravity one tool already added {f(agy_add("agyg", 1))} (Gemini) and {f(agy_add("agyo", 1))} (Opus) and 29 more added little, so all four now seem to load a tool&rsquo;s details only when it is used.</li>')
    li.append(f'<li><strong>All {sum(g["ok"] for g in G.values())} games worked</strong> in a headless-browser check: the score rises when bricks break, level 2 appears, and lives go 3, 2, 1, 0. '
              'The automatic check could not read the score in two Codex games; a manual check showed bricks breaking and points adding up in both.</li>')
    li.append('<li><strong>Why Antigravity:</strong> Google stopped serving Gemini CLI to personal accounts (Google AI Pro, Ultra and free Code Assist) on 2026-06-18 and pointed them to Antigravity CLI. '
              'Antigravity can also run Claude models, which is what makes the same-model comparison possible.</li>')
    hb = ['<th>MCP tools</th>'] + [f'<th class="text-right">{esc(l)}</th>' for _, l in AGY_TOOLS]
    rb = []
    for n in (0, 1, 10, 30):
        cells = []
        for k, _ in AGY_TOOLS:
            v = B[(k, n)]; extra = f' <span class="text-zinc-500">(+{f(v["cache"])} cache)</span>' if k.startswith("agy") and v["cache"] else ""
            add = "" if n == 0 else f' <span class="text-zinc-500">({"+" if agy_add(k, n) >= 0 else "&minus;"}{f(abs(agy_add(k, n)))})</span>'
            cells.append(f'<td class="text-right tabular-nums">{f(v["inp"])}{extra}{add}</td>')
        rb.append(f'          <tr><td>{n}</td>' + "".join(cells) + "</tr>")
    hg = ['<th>Tool</th>', '<th class="text-right">Input tokens</th>', '<th class="text-right">Cache reads reported separately</th>', '<th class="text-right">Output tokens</th>',
          '<th class="text-right">Seconds</th>', '<th class="text-right">Lines</th>', '<th class="text-right">Games working</th>']
    rg = []
    for k, l in AGY_TOOLS:
        g = G[k]
        rg.append(f'          <tr><td>{esc(l)}</td><td class="text-right tabular-nums">{f(g["inp"])}</td>'
                  f'<td class="text-right tabular-nums">{f(g["cache"]) if k.startswith("agy") else "included"}</td><td class="text-right tabular-nums">{f(g["out"])}</td>'
                  f'<td class="text-right tabular-nums">{round(g["sec"])}</td><td class="text-right tabular-nums">{round(g["lines"])}</td><td class="text-right tabular-nums">{g["ok"]} of {g["n"]}</td></tr>')
    body = ('      <h2>Key findings</h2>\n      <ul>\n' + "\n".join("        " + x for x in li) + '\n      </ul>\n'
            '      <h2>Startup tokens and MCP tools</h2>\n'
            '      <p class="text-sm text-zinc-400">Input tokens for &ldquo;Reply with the single word OK.&rdquo;, average of two runs. In brackets: Antigravity&rsquo;s separately reported cache reads, and the change against no MCP server.</p>\n'
            + _table(hb, chr(10).join(rb)) +
            '      <h2>The same coding task</h2>\n'
            '      <p class="text-sm text-zinc-400">&ldquo;Make a brick-breaker game that runs in the browser as a single file named index.html &hellip; 2 levels, a score display and 3 lives &hellip; keyboard and mouse.&rdquo; Average of five runs each, medium effort. Claude Code and Codex runs 4 and 5 are the 2026-10-18 runs of our Claude Code vs Codex dataset (same versions); the Antigravity runs 4 and 5 are from 2026-10-23; one Claude Code run took an extra step and read 123,666 tokens.</p>\n'
            + _table(hg, chr(10).join(rg)) +
            '      <h2>How to read Antigravity&rsquo;s numbers</h2>\n'
            '      <p><code>agy --output-format json</code> reports <code>input_tokens</code>, <code>output_tokens</code>, <code>thinking_tokens</code>, <code>cache_read_tokens</code> and <code>total_tokens</code>, '
            f'where total is input plus output. Its documentation does not say whether cache reads are part of input. In our Opus runs the cache reads ({f(ao["cache"])} on the game task) were larger than the reported input ({f(ao["inp"])}), '
            'so there they cannot be contained in it. We therefore show both: the reported input as the low figure and input plus cache reads as the high one. Even the high figure is far below Claude Code&rsquo;s.</p>\n'
            '      <h2>Method</h2>\n      <ul>\n'
            f'        <li>Windows 11, {AGY_MEASURED_SHOW}. Every run in its own empty folder, one after another, with no other MCP servers.</li>\n'
            '        <li><strong>Claude Code 2.1.295</strong>, Opus 5.5, Max plan: <code>claude -p --output-format json --mcp-config mcp.json --strict-mcp-config</code>; the game at <code>--effort medium --permission-mode acceptEdits</code>. Input = input + cache creation + cache read.</li>\n'
            '        <li><strong>Codex CLI 0.162.0-alpha.17.2</strong>, gpt-6-luna, ChatGPT plan: <code>codex exec --json</code>, reasoning effort low for startup and medium for the game, MCP server added with <code>-c mcp_servers.&hellip;</code>. Input includes cached input.</li>\n'
            '        <li><strong>Antigravity CLI 1.4.5</strong> (<code>agy</code>), personal Google account: <code>agy -p --output-format json --model gemini-4-argon-medium</code> or <code>claude-opus-5-5-medium</code>; the game with <code>--mode accept-edits</code>. '
            'The MCP server was written to the global <code>~/.gemini/config/mcp_config.json</code> for each startup run and removed afterwards.</li>\n'
            f'        <li>MCP test server: the same small stdio server as in our <a href="{AGT_PATH}">Claude Code vs Codex dataset</a>, exposing 1, 10 or 30 tracker tools with a one-sentence description and a five-field schema each.</li>\n'
            '        <li>Games were checked in headless Chromium: break bricks and watch the score, clear or skip to level 2, and lose the ball until lives reach zero. Scripts and every log are in the GitHub mirror.</li>\n'
            '      </ul>\n      <h2>Limitations</h2>\n      <ul>\n'
            '        <li>Two runs per startup test and five per game, on three days with the same tool versions. One task, one machine.</li>\n'
            '        <li>Token counts are each tool&rsquo;s own report, and the three tools count cache differently (see above). Prices are not compared: Codex and Antigravity show none on a subscription.</li>\n'
            '        <li>We cannot see how Antigravity sets up Opus 5.5 behind its <code>claude-opus-5-5-medium</code> name, so its settings may differ from Claude Code&rsquo;s medium effort.</li>\n'
            '      </ul>\n')
    return (_head(f"Antigravity CLI vs Claude Code vs Codex: the same Opus 5.5 read {g_lo}% to {g_hi}% fewer tokens in Antigravity", lead,
                  f'Measured {AGY_MEASURED_SHOW} · {len(R)} runs · Claude Code 2.1.295, Codex CLI 0.162, Antigravity CLI 1.4.5 · License <a href="{LICENSE}">CC BY 4.0</a> · Earlier: <a href="{AGT_PATH}">Claude Code vs Codex</a>',
                  [("antigravity-cli-vs-claude-code-vs-codex.csv", "CSV"), ("antigravity-cli-vs-claude-code-vs-codex.json", "JSON")],
                  AGY_CHART, "Input tokens for the same coding task in Claude Code, Codex and Antigravity CLI", doi=AGY_DOI or None, mirrors=AGY_MIRRORS)
            + body + _page_tail(agy_citation(), _embed(AGY_PATH, AGY_CHART, "Input tokens for the same coding task in Claude Code, Codex and Antigravity CLI", "Antigravity CLI vs Claude Code vs Codex"),
                                [(AGT_PATH, "Claude Code vs Codex: startup tokens and MCP tools"), (HAR_PATH, "What the Claude Code harness costs"), (CCV_PATH, "Claude Code baseline tokens by version"), ("/agents", "Estimate your Claude Code or Codex bill")]))


# ---- Dataset 23: output tokens per character by model, tool and prompt language (measured 2026-10-18 to 2026-10-23) ----
LGO_PATH = "/data/output-tokens-per-character-by-model"
LGO_MEASURED = "2026-10-23"
LGO_CHART = "/output-tokens-per-character-by-model-chart.png"
LGO_DOI = "10.5281/zenodo.23585139"  # concept DOI
LGO_MIRRORS = [("Zenodo", "https://zenodo.org/records/23589133"),
               ("Hugging Face", "https://huggingface.co/datasets/JOHNISKING/output-tokens-per-character-by-model"),
               ("Kaggle", "https://www.kaggle.com/datasets/johnisking/output-tokens-per-character-claude-gpt-gemini"),
               ("GitHub", "https://github.com/johnisking/token-cost-by-language/tree/main/output-tokens-per-character")]
LGO_TITLE = "Same code, about 60% more output tokens: Claude vs GPT vs Gemini in four coding tools and five languages"
LGO_DESC = ("Dataset: the same brick-breaker task in Claude Code, Codex and Antigravity CLI (Gemini 4 Argon and Claude Opus 5.5), prompted in English, Korean, Japanese, Spanish and Ukrainian, 100 runs. "
            "Claude Opus 5.5 used about 60% more output tokens per 1,000 characters of game code than Gemini or GPT, in both tools that ran it. Prompt language moved input tokens only a few percent. Free CSV, CC BY 4.0.")
LGO_TOOLS = [("claude_code", "Claude Code + Opus 5.5"), ("antigravity_opus", "Antigravity + Opus 5.5"), ("antigravity_gemini", "Antigravity + Gemini 4 Argon"), ("codex", "Codex + gpt-6-luna")]
LGO_LANGS = [("en", "English"), ("ko", "Korean"), ("ja", "Japanese"), ("es", "Spanish"), ("uk", "Ukrainian")]
LGO_COLS = ["tool", "lang", "run", "measured", "input_tokens", "cache_read_reported_separately", "output_tokens", "seconds", "file_chars", "file_lines",
            "output_tokens_per_1000_chars", "game_ok", "source"]


def _lgo():
    return json.load(open(os.path.join(ROOT, "blog_data", "agylang", "rows.json"), encoding="utf-8"))


def lgo_citation():
    if LGO_DOI:
        return f"TokenSave (2026). {LGO_TITLE} [Data set]. Zenodo. https://doi.org/{LGO_DOI}"
    return f"TokenSave (2026). {LGO_TITLE} [Data set]. {BASE}{LGO_PATH}"


def write_lgo_files(dist):
    R = _lgo()
    buf = io.StringIO(); w = csv.writer(buf); w.writerow(LGO_COLS)
    for r in R:
        w.writerow([r[c] if r[c] is not None else "" for c in LGO_COLS])
    open(os.path.join(dist, "data", "output-tokens-per-character-by-model.csv"), "w", encoding="utf-8", newline="").write(buf.getvalue())
    meta = dict(title=LGO_TITLE, url=BASE + LGO_PATH, license="CC BY 4.0", citation=lgo_citation(), measured="2026-10-18 to 2026-10-23",
                setup="Windows 11; Claude Code 2.1.295 (Opus 5.5, effort medium); Codex CLI 0.162 (gpt-6-luna, medium); Antigravity CLI 1.4.5 (gemini-4-argon-medium, claude-opus-5-5-medium)",
                note=("output_tokens_per_1000_chars = output tokens reported by the tool / characters of the index.html it wrote x 1000. Output tokens include the short final reply and any tool-call wrapping. "
                      "Claude Code and Codex rows are the runs of our dataset 'ai-coding-prompt-language' (same versions); Antigravity English rows are from 'antigravity-cli-vs-claude-code-vs-codex'."),
                tools=dict(LGO_TOOLS), rows=R)
    open(os.path.join(dist, "data", "output-tokens-per-character-by-model.json"), "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))


def lgo_ld():
    return _dataset_ld(LGO_TITLE, LGO_DESC, LGO_PATH, LGO_MEASURED,
                       ["output tokens per character", "Claude tokenizer", "Claude vs GPT tokens", "Claude vs Gemini tokens", "Antigravity CLI", "prompt language tokens", "AI coding cost by language"],
                       ["input tokens", "output tokens", "output tokens per 1,000 characters of generated code", "seconds", "whether the game works"],
                       "The same brick-breaker prompt in five languages, run headless in Claude Code, Codex and Antigravity CLI; every game checked in headless Chromium for score, a second level and lives 3 to 0",
                       LGO_CHART, [("output-tokens-per-character-by-model.csv", "text/csv"), ("output-tokens-per-character-by-model.json", "application/json")],
                       doi=LGO_DOI or None, mirrors=LGO_MIRRORS)


def lgo_stats():
    R = _lgo(); S = {}
    for t, _ in LGO_TOOLS:
        for l, _ in LGO_LANGS:
            rs = [r for r in R if r["tool"] == t and r["lang"] == l]
            S[(t, l)] = dict(n=len(rs), inp=statistics.mean(r["input_tokens"] for r in rs), out=statistics.mean(r["output_tokens"] for r in rs),
                             chars=statistics.mean(r["file_chars"] for r in rs), per=statistics.mean(r["output_tokens_per_1000_chars"] for r in rs),
                             ok=sum(bool(r["game_ok"]) for r in rs))
        rs = [r for r in R if r["tool"] == t]
        S[t] = dict(per=statistics.mean(r["output_tokens_per_1000_chars"] for r in rs), lo=min(S[(t, l)]["per"] for l, _ in LGO_LANGS),
                    hi=max(S[(t, l)]["per"] for l, _ in LGO_LANGS), ok=sum(bool(r["game_ok"]) for r in rs), n=len(rs))
    return R, S


def lgo_html():
    R, S = lgo_stats()
    f = lambda v: "{:,}".format(round(v))
    pct = lambda a, b: round((b / a - 1) * 100)
    op, cc, gm, cx = S["antigravity_opus"], S["claude_code"], S["antigravity_gemini"], S["codex"]
    vs_g, vs_x = pct(gm["per"], op["per"]), pct(cx["per"], cc["per"])
    nok = sum(S[t]["ok"] for t, _ in LGO_TOOLS)
    lead = (f'<strong>To write the same kind of game, Claude Opus 5.5 spent about {vs_g}% more output tokens per character of code than Gemini 4 Argon, and about {vs_x}% more than GPT.</strong> '
            f'Opus came out the same in Claude Code ({f(cc["per"])} tokens per 1,000 characters) and in Google&rsquo;s Antigravity CLI ({f(op["per"])}), so it is the model&rsquo;s tokenizer, not the tool. '
            'Writing the prompt in Korean, Japanese, Spanish or Ukrainian instead of English changed input tokens by only a few percent.')
    li = []
    li.append(f'<li><strong>Output tokens per 1,000 characters of game code:</strong> Opus 5.5 {f(cc["per"])} in Claude Code and {f(op["per"])} in Antigravity, Gemini 4 Argon {f(gm["per"])}, gpt-6-luna {f(cx["per"])} in Codex. '
              f'The range across the five prompt languages was narrow for every model (Opus {f(min(cc["lo"], op["lo"]))} to {f(max(cc["hi"], op["hi"]))}, Gemini {f(gm["lo"])} to {f(gm["hi"])}, GPT {f(cx["lo"])} to {f(cx["hi"])}).</li>')
    li.append('<li><strong>Why it matters:</strong> output tokens are the expensive ones (Opus 5.5 charges five times more for output than for input), and because the gap is per character, it comes on top of any difference in how long each model&rsquo;s game turned out. '
              'It matches the direction of our earlier tokenizer test, where the same source code needed 43% to 59% more Claude tokens than GPT tokens.</li>')
    li.append(f'<li><strong>Prompt language barely moved input tokens.</strong> Inside each tool the five languages stayed within a few percent; the tool decided the size: about {f(S[("claude_code","ko")]["inp"])} input tokens in Claude Code, '
              f'{f(S[("codex","ko")]["inp"])} in Codex and {f(S[("antigravity_opus","ko")]["inp"])} to {f(S[("antigravity_gemini","ko")]["inp"])} in Antigravity for the Korean prompt. Most of every request is the tool&rsquo;s own instructions.</li>')
    li.append(f'<li><strong>Opus wrote longer games in Korean and Ukrainian</strong> in Antigravity ({f(S[("antigravity_opus","ko")]["chars"])} and {f(S[("antigravity_opus","uk")]["chars"])} characters against {f(S[("antigravity_opus","en")]["chars"])} in English), '
              'so its total output rose there, but per character it stayed the same.</li>')
    li.append(f'<li><strong>{nok} of {len(R)} games worked</strong> (score rises, level 2 appears, lives go 3, 2, 1, 0), and every game showed its text in the prompt language. The one failure is a Codex game from the earlier dataset.</li>')
    hp = ['<th>Tool + model</th>'] + [f'<th class="text-right">{n}</th>' for _, n in LGO_LANGS]
    rp, ri = [], []
    for t, lab in LGO_TOOLS:
        rp.append(f'          <tr><td>{esc(lab)}</td>' + "".join(f'<td class="text-right tabular-nums">{f(S[(t, l)]["per"])}</td>' for l, _ in LGO_LANGS) + '</tr>')
        ri.append(f'          <tr><td>{esc(lab)}</td>' + "".join(f'<td class="text-right tabular-nums">{f(S[(t, l)]["inp"])}</td>' for l, _ in LGO_LANGS) + '</tr>')
    body = ('      <h2>Key findings</h2>\n      <ul>\n' + "\n".join("        " + x for x in li) + '\n      </ul>\n'
            '      <h2>Output tokens per 1,000 characters of code</h2>\n'
            '      <p class="text-sm text-zinc-400">Output tokens reported by each tool divided by the characters of the index.html it wrote. Average of 5 runs per tool and language.</p>\n'
            + _table(hp, chr(10).join(rp)) +
            '      <h2>Input tokens by prompt language</h2>\n'
            '      <p class="text-sm text-zinc-400">Claude Code: input + cache creation + cache read. Codex: input including cached. Antigravity: its reported input_tokens (cache reads are reported separately and are in the CSV). '
            'Claude Code&rsquo;s English average includes two runs from 2026-10-18 that took an extra step.</p>\n'
            + _table(hp, chr(10).join(ri)) +
            '      <h2>Method</h2>\n      <ul>\n'
            '        <li>Task: &ldquo;Make a brick-breaker game that runs in the browser as a single file named index.html &hellip; 2 levels, a score display and 3 lives &hellip; keyboard and mouse&rdquo;, translated into Korean, Japanese, Spanish and Ukrainian. Medium effort everywhere, each run in its own empty folder on Windows 11.</li>\n'
            f'        <li>Claude Code 2.1.295 and Codex CLI 0.162: the 50 runs of our <a href="{TL_PATH}">prompt-language dataset</a> (2026-10-18 and 19). Antigravity CLI 1.4.5: English runs 1 to 3 from our <a href="{AGY_PATH}">three-way comparison</a> (2026-10-22), the other 44 runs new (2026-10-23; runs 4 and 5 in every language added the same day).</li>\n'
            '        <li>Every game was played in headless Chromium by a script that watches the score, the level and the lives; the check reads the game&rsquo;s own text in all five languages.</li>\n'
            '      </ul>\n      <h2>Limitations</h2>\n      <ul>\n'
            '        <li>Output tokens include the short final reply and the tool-call wrapping around the file, not only the code. Antigravity reported no or few thinking tokens; Claude Code and Codex count any reasoning inside their output figure.</li>\n'
            '        <li>One task (a browser game in HTML, CSS and JavaScript). Other kinds of code may tokenize differently.</li>\n'
            '        <li>3 to 5 runs per cell, measured over six days with the same tool versions.</li>\n'
            '      </ul>\n')
    return (_head(f"Same code, about {vs_g}% more output tokens: Claude vs GPT vs Gemini in four coding tools and five languages", lead,
                  f'Measured 2026-10-18 to {LGO_MEASURED} · {len(R)} runs · Claude Code 2.1.295, Codex CLI 0.162, Antigravity CLI 1.4.5 · License <a href="{LICENSE}">CC BY 4.0</a>',
                  [("output-tokens-per-character-by-model.csv", "CSV"), ("output-tokens-per-character-by-model.json", "JSON")],
                  LGO_CHART, "Output tokens per 1,000 characters of generated game code by model, tool and prompt language", doi=LGO_DOI or None, mirrors=LGO_MIRRORS)
            + body + _page_tail(lgo_citation(), _embed(LGO_PATH, LGO_CHART, "Output tokens per 1,000 characters of code by model", "output tokens per character by model"),
                                [(AGY_PATH, "Antigravity CLI vs Claude Code vs Codex"), (TL_PATH, "Does prompt language change AI coding cost?"), (CODE_PATH, "Token cost by programming language"), ("/", "Count tokens for your own text")]))


# ---- "Try it yourself" box near the top of every dataset page (2026-10-22) ----
_CTA = {
    "/": ("Count the tokens in your own text", "Paste your prompt and see tokens, characters and API cost on GPT, Claude and Gemini. Free and private: it runs in your browser."),
    "/agents": ("Estimate your own Claude Code or Codex bill", "See the monthly cost of Claude Code and Codex for your usage: API per task vs Claude and ChatGPT plans. Free, no sign-up."),
    "/claude-code-usage": ("Check your own Claude Code usage", "Open your Claude Code or Codex log folder, or a Cursor usage CSV, and see tokens and API-equivalent cost by day, project and model. Runs in your browser."),
}
_CTA_MAP = {LANG_PATH: "/", MULTI_PATH: "/", FMT_PATH: "/", CODE_PATH: "/", PDF_PATH: "/", LTI_PATH: "/", TL_PATH: "/", POL_PATH: "/",
            IMG_PATH: "/", TAI_PATH: "/",
            EFF_PATH: "/agents", AGT_PATH: "/agents", AGS_PATH: "/agents", AGL_PATH: "/agents", AMD_PATH: "/agents", HAR_PATH: "/agents",
            VIB_PATH: "/agents", CCV_PATH: "/claude-code-usage",
            LNG_PATH: "/claude-code-usage", COF_PATH: "/claude-code-usage", BMC_PATH: "/agents", BLM_PATH: "/agents", AGY_PATH: "/agents", LGO_PATH: "/"}


def add_cta(path, body):
    tool = _CTA_MAP.get(path)
    if not tool:
        return body
    head, text = _CTA[tool]
    box = (f'      <a href="{tool}" class="not-prose block no-underline my-5 rounded-xl border border-violet-500/50 bg-violet-500/10 hover:bg-violet-500/20 p-4" '
           f'style="text-decoration:none" data-cta="data-top">\n'
           f'        <span class="block text-base font-bold text-white">{esc(head)} &rarr;</span>\n'
           f'        <span class="block mt-1 text-sm text-zinc-300">{esc(text)}</span>\n      </a>\n')
    i = body.find('href="#cite"')
    j = body.find('</div>', i) if i >= 0 else -1
    if j < 0:
        return body
    j += len('</div>') + 1
    return body[:j] + box + body[j:]
