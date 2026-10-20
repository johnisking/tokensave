"""/tokens-to-words: convert between tokens, words, characters and pages.

Ratios come from our own measurements (blog/tokens-per-word, token-cost-by-language) and the
tokenizer factors the token counter uses for Claude and Gemini.
"""
import json, html, os

esc = lambda s: html.escape(str(s), quote=True)

# tokens per English word on GPT's o200k tokenizer (measured, see /blog/tokens-per-word)
TPW = {"prose": 1.15, "tech": 1.33}
# tokenizer factor vs GPT for English, measured (blog_data/langmulti, 2026-10-17); per-language factors in _model_factors()
MODELS = [("GPT (OpenAI)", 1.00), ("Claude Opus / Sonnet / Haiku 5.5", 1.38), ("Claude Haiku 4.5", 1.03), ("Gemini", 1.00)]
_MULTI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "blog_data", "langmulti", "combined.json")


def _model_factors():
    """{lang code: [GPT, Claude 5.x, Claude Haiku 4.5, Gemini]} — tokens vs GPT for the same prompt, measured"""
    rows = json.load(open(_MULTI, encoding="utf-8"))
    return {r["code"]: [1.0, round(r["claude55"] / r["gpt"], 2), round(r["claude45"] / r["gpt"], 2), round(r["gemini"] / r["gpt"], 2)] for r in rows}
WORDS_PER_PAGE = 500
CHARS_PER_TOKEN_EN = 4.8

TITLE = "Tokens to Words Converter (GPT, Claude, Gemini)"
DESC = "Convert tokens to words and words to tokens for GPT, Claude and Gemini, in 41 languages. Based on measured text, free, in your browser."

FAQ = [
    ("How many words is 1,000 tokens?",
     "In everyday English on GPT models, 1,000 tokens is about 870 words, or roughly 1¾ pages. Technical writing is closer to 750 words. On Claude Opus, Sonnet and Haiku 5.5 the same 1,000 tokens hold only about 630 words, because in our test Claude used 38% more tokens than GPT for the same English text."),
    ("How many tokens is 1,000 words?",
     "About 1,150 tokens on GPT for ordinary English prose, and about 1,330 for technical text. The same 1,000 words are about 1,590 tokens on Claude Opus, Sonnet and Haiku 5.5, and about the same as GPT on Gemini."),
    ("Is \"1 token = ¾ of a word\" still right?",
     "It is a safe, slightly high estimate. That rule of thumb comes from OpenAI's older tokenizers. On current GPT models we measured 1.12 to 1.33 tokens per English word, so ordinary writing usually uses about 15% fewer tokens than the rule predicts."),
    ("Why do other languages need more tokens?",
     "Tokenizers are trained mostly on English, so other scripts get split into smaller pieces. For the same meaning, Korean needs about 44% more tokens than English and Japanese about 79% more, while Chinese is close to English. Pick a language above to see the effect."),
    ("Is this exact?",
     "No, it is an estimate from average ratios. For the exact count of a specific text, paste it into the token counter, which runs the real GPT tokenizer in your browser."),
]


def _row(tokens, label):
    cells = []
    for _, f in MODELS[:2] + MODELS[3:]:
        w = tokens / (TPW["prose"] * f)
        cells.append(f"<td>{w:,.0f} words</td>")
    return f"<tr><td><strong>{label}</strong></td>{''.join(cells)}</tr>"


def body(lang_ratios):
    """lang_ratios: [[tag, native name, ratio vs English], ...]"""
    langs = sorted(lang_ratios, key=lambda x: (x[0] != "en", x[1]))
    mf = _model_factors()
    opts = "".join(f'<option value="{t}" data-r="{r}" data-m="{",".join(str(x) for x in mf.get(t, [f for _, f in MODELS]))}"{" selected" if t == "en" else ""}>{esc(n)}</option>' for t, n, r in langs)
    mopts = "".join(f'<option value="{i}">{esc(n)}</option>' for i, (n, f) in enumerate(MODELS))
    table = "".join(_row(t, l) for t, l in [(1_000, "1,000 tokens"), (10_000, "10,000 tokens"), (128_000, "128,000 tokens"), (1_000_000, "1 million tokens")])
    faq_cards = "\n".join(f'''      <div class="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-5">
        <h2 class="font-semibold mb-1.5">{esc(q)}</h2>
        <p class="text-zinc-400">{esc(a)}</p>
      </div>''' for q, a in FAQ)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebApplication", "name": "Tokens to Words Converter", "url": "https://tokensave.app/tokens-to-words",
         "applicationCategory": "DeveloperApplication", "operatingSystem": "Any", "isAccessibleForFree": True, "description": DESC,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]}
    sel = "bg-zinc-900 border border-zinc-800 rounded-lg px-3 py-2 text-sm text-zinc-200 focus:outline-none focus:ring-2 focus:ring-violet-500/50 w-full"
    inp = "ltr bg-zinc-950 border border-zinc-800 rounded-xl px-4 py-3 text-2xl font-bold text-white w-full focus:outline-none focus:ring-2 focus:ring-violet-500/50"
    return f'''    <header class="text-center mb-8">
      <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight bg-gradient-to-r from-white via-violet-200 to-indigo-300 bg-clip-text text-transparent leading-tight pb-1">Tokens to Words Converter</h1>
      <p class="mt-3 text-zinc-400 text-sm sm:text-base">Turn a token count into words and pages, or words into tokens, for GPT, Claude and Gemini in 41 languages.</p>
    </header>

    <section class="max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-5 sm:p-7">
      <div class="grid sm:grid-cols-3 gap-3">
        <label class="text-xs text-zinc-400">Model<select id="twModel" class="{sel} mt-1">{mopts}</select></label>
        <label class="text-xs text-zinc-400">Language<select id="twLang" class="{sel} mt-1">{opts}</select></label>
        <label class="text-xs text-zinc-400">Kind of text<select id="twKind" class="{sel} mt-1"><option value="prose">Everyday writing</option><option value="tech">Technical / documentation</option></select></label>
      </div>
      <div class="grid sm:grid-cols-2 gap-4 mt-5">
        <label class="text-sm font-semibold text-zinc-300">Tokens<input id="twTokens" type="number" min="0" step="1" value="1000" class="{inp} mt-1" /></label>
        <label class="text-sm font-semibold text-zinc-300">Words<input id="twWords" type="number" min="0" step="1" class="{inp} mt-1" /></label>
      </div>
      <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 mt-5 text-center">
        <div class="bg-zinc-950/60 border border-zinc-800 rounded-xl p-3"><div class="text-xs text-zinc-500">Pages (500 words)</div><div id="twPages" class="text-xl font-bold text-white mt-1">–</div></div>
        <div class="bg-zinc-950/60 border border-zinc-800 rounded-xl p-3"><div class="text-xs text-zinc-500">Characters (English)</div><div id="twChars" class="text-xl font-bold text-white mt-1">–</div></div>
        <div class="bg-zinc-950/60 border border-zinc-800 rounded-xl p-3 col-span-2 sm:col-span-1"><div class="text-xs text-zinc-500">Same text in English</div><div id="twEn" class="text-xl font-bold text-white mt-1">–</div></div>
      </div>
      <p id="twNote" class="mt-4 text-xs text-zinc-500 leading-relaxed"></p>
      <p class="mt-2 text-xs text-zinc-500">Need an exact count for a real text? Paste it into the <a class="text-violet-300 underline" href="/">token counter</a>.</p>
    </section>

    <section class="prose-ts mt-12 max-w-3xl mx-auto bg-zinc-900/40 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <h2 style="margin-top:0">Quick reference (everyday English)</h2>
      <p>A page is about 500 words, so 1,000 tokens on GPT is roughly 1¾ pages and a 128,000-token context window holds about 220 pages.</p>
      <div class="overflow-x-auto"><table><thead><tr><th>Tokens</th><th>GPT</th><th>Claude Opus / Sonnet / Haiku 5.5</th><th>Gemini</th></tr></thead><tbody>{table}</tbody></table></div>
      <h2>Where the numbers come from</h2>
      <p>We counted real English text on GPT's current tokenizer (o200k): ordinary prose came out at <strong>1.12–1.15 tokens per word</strong>, technical documentation at <strong>1.33</strong>, about 4.4–4.9 characters per token. For Claude and Gemini we use <a href=\"/data/token-cost-by-language-claude-gemini\">our own measurement</a> of the same prompt in 41 languages, counted with each provider's token-counting API: in English, Claude Opus, Sonnet and Haiku 5.5 used 38% more tokens than GPT, Claude Haiku 4.5 3% more, and Gemini the same. The gap changes by language (Korean +82% on Claude 5.5, Japanese +16%), and the converter uses the figure for the language you pick. The full method is in <a href="/blog/tokens-per-word">How many tokens is a word?</a></p>
      <p>Other languages use the ratios from our <a href="/blog/token-cost-by-language">41-language measurement</a>: the same prompt translated into each language and counted on GPT. Words are a poor unit across languages (Chinese, Japanese and Thai do not separate words with spaces), so for them the converter shows how much English-equivalent content fits in your tokens.</p>
      <h2>Related</h2>
      <ul>
        <li><a href="/">AI token counter</a> — exact GPT counts and API cost for any text</li>
        <li><a href="/blog/what-is-a-token">What is a token?</a></li>
        <li><a href="/blog/context-window-explained">Context windows explained</a></li>
        <li><a href="/blog/token-cost-by-language">Same prompt, 41 languages: token cost compared</a></li>
      </ul>
    </section>

    <section class="mt-12 max-w-5xl mx-auto grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
{faq_cards}
    </section>
    <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
    <script>
    (() => {{
      const TPW = {json.dumps(TPW)}, PAGE = {WORDS_PER_PAGE}, CPT = {CHARS_PER_TOKEN_EN};
      const $ = id => document.getElementById(id);
      const tok = $('twTokens'), wrd = $('twWords'), model = $('twModel'), lang = $('twLang'), kind = $('twKind');
      const R = () => parseFloat(lang.selectedOptions[0].dataset.r);
      const M = () => parseFloat(lang.selectedOptions[0].dataset.m.split(',')[+model.value]);
      const f = () => TPW[kind.value] * M() * R();
      const fmt = n => isFinite(n) ? Math.round(n).toLocaleString('en-US') : '–';
      let last = 'tok';
      function out(t, w) {{
        $('twPages').textContent = isFinite(w) ? (w / PAGE).toLocaleString('en-US', {{maximumFractionDigits: 1}}) : '–';
        const en = t / R();
        const isEn = lang.value === 'en';
        $('twChars').textContent = isEn ? fmt(en / M() * CPT) : '–';
        $('twEn').textContent = isEn ? fmt(t) + ' tokens' : fmt(en) + ' tokens';
        const ln = lang.selectedOptions[0].text, r = R();
        const pct = Math.round((r - 1) * 100);
        $('twNote').textContent = isEn
          ? 'English, ' + kind.selectedOptions[0].text.toLowerCase() + ': ' + (TPW[kind.value] * M()).toFixed(2) + ' tokens per word on ' + model.selectedOptions[0].text + '.'
          : ln + ' uses ' + (pct >= 0 ? pct + '% more' : -pct + '% fewer') + ' tokens than English for the same meaning, so "words" here means English-equivalent words of content.';
      }}
      function fromTokens() {{ const t = parseFloat(tok.value); const w = t / f(); wrd.value = isFinite(w) ? Math.round(w) : ''; out(t, w); }}
      function fromWords() {{ const w = parseFloat(wrd.value); const t = w * f(); tok.value = isFinite(t) ? Math.round(t) : ''; out(t, w); }}
      tok.addEventListener('input', () => {{ last = 'tok'; fromTokens(); }});
      wrd.addEventListener('input', () => {{ last = 'wrd'; fromWords(); }});
      [model, lang, kind].forEach(el => el.addEventListener('change', () => last === 'tok' ? fromTokens() : fromWords()));
      fromTokens();
    }})();
    </script>'''
