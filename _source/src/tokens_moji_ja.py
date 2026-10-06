"""/ja/token-moji-henkan: Japanese tokens <-> characters converter.

Ratio from our own measurement (blog_src/tpw-ja.md): the same support prompt in Japanese was 73 characters
and 61 tokens on GPT's o200k tokenizer (1.2 characters per token), 79% more tokens than the English version.
Model factors are the same ones token.js uses (measured on English text).
"""
import json, html

esc = lambda s: html.escape(str(s), quote=True)

PATH = "/ja/token-moji-henkan"
CPT_JA = 1.2          # Japanese characters per GPT token
JA_VS_EN = 1.79       # Japanese needs 79% more tokens than English for the same meaning
TPW_EN = 1.15         # GPT tokens per English word (everyday prose)
GENKOU = 400          # characters per 原稿用紙 sheet
MODELS = [("GPT（OpenAI）", 1.00), ("Claude Opus / Sonnet", 1.30), ("Claude Haiku 4.5", 1.05), ("Gemini", 0.95)]

TITLE = "トークン⇔文字数 変換ツール｜日本語・GPT／Claude／Gemini"
DESC = "トークン数を日本語の文字数・原稿用紙の枚数に、文字数をトークン数に変換。GPT・Claude・Gemini対応、実測の比率で計算する無料ツール。"


def _c(tokens, f):
    return tokens * CPT_JA / f


FAQ = [
    ("1トークンは日本語で何文字？",
     f"GPT の現行トークナイザーで、ふつうの日本語は1トークンあたり約1.2文字です。Claude Opus・Sonnet は同じ文章を約30%多いトークンに分けるので約0.9文字、Gemini は約1.3文字です。漢字とかなの割合で多少変わります。"),
    ("日本語1,000文字は何トークン？",
     f"GPT で約{1000 / CPT_JA:,.0f}トークン、Claude Opus・Sonnet で約{1000 / CPT_JA * 1.30:,.0f}トークン、Gemini で約{1000 / CPT_JA * 0.95:,.0f}トークンです。原稿用紙なら2枚半ほどです。"),
    ("なぜ日本語はトークンが多いの？",
     "トークナイザーは主に英語のデータで作られているため、日本語は細かく分けられます。同じ意味を伝えるのに、日本語は英語より約79%多いトークンが必要です。API はトークン単位の課金なので、そのぶん料金も高くなります。"),
    ("正確な数はわかる？",
     "このツールは平均の比率から出した目安です。実際の文章の正確なトークン数は、トークンカウンターに貼り付けると本物の GPT トークナイザーがブラウザの中で数えます。"),
]


def _row(tokens, label):
    cells = "".join(f"<td>約{_c(tokens, f):,.0f}字</td>" for _, f in (MODELS[0], MODELS[1], MODELS[3]))
    return f"<tr><td><strong>{label}</strong></td>{cells}<td>約{_c(tokens, 1.0) / GENKOU:,.0f}枚</td></tr>"


def ld(url):
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "WebApplication", "name": "トークン⇔文字数 変換ツール", "url": url, "inLanguage": "ja",
         "applicationCategory": "DeveloperApplication", "operatingSystem": "Any", "isAccessibleForFree": True, "description": DESC,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
        {"@type": "FAQPage", "inLanguage": "ja", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]}


def body():
    mopts = "".join(f'<option value="{f}">{esc(n)}</option>' for n, f in MODELS)
    table = "".join(_row(t, l) for t, l in [(1_000, "1,000トークン"), (10_000, "1万トークン"), (128_000, "12.8万トークン"), (1_000_000, "100万トークン")])
    faq_cards = "\n".join(f'''      <div class="bg-zinc-900/50 border border-zinc-800 rounded-2xl p-5">
        <h2 class="font-semibold mb-1.5">{esc(q)}</h2>
        <p class="text-zinc-400">{esc(a)}</p>
      </div>''' for q, a in FAQ)
    sel = "bg-zinc-900 border border-zinc-800 rounded-lg px-3 py-2 text-sm text-zinc-200 focus:outline-none focus:ring-2 focus:ring-violet-500/50 w-full"
    inp = "ltr bg-zinc-950 border border-zinc-800 rounded-xl px-4 py-3 text-2xl font-bold text-white w-full focus:outline-none focus:ring-2 focus:ring-violet-500/50"
    card = "bg-zinc-950/60 border border-zinc-800 rounded-xl p-3"
    return f'''    <header class="text-center mb-8">
      <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight bg-gradient-to-r from-white via-violet-200 to-indigo-300 bg-clip-text text-transparent leading-tight pb-1">トークン⇔文字数 変換</h1>
      <p class="mt-3 text-zinc-400 text-sm sm:text-base">トークン数を日本語の文字数と原稿用紙の枚数に、文字数をトークン数に。GPT・Claude・Gemini に対応。</p>
    </header>

    <section class="max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-5 sm:p-7">
      <label class="block text-xs text-zinc-400 sm:max-w-xs">モデル<select id="tmModel" class="{sel} mt-1">{mopts}</select></label>
      <div class="grid sm:grid-cols-2 gap-4 mt-5">
        <label class="text-sm font-semibold text-zinc-300">トークン数<input id="tmTokens" type="number" min="0" step="1" value="1000" class="{inp} mt-1" /></label>
        <label class="text-sm font-semibold text-zinc-300">日本語の文字数<input id="tmChars" type="number" min="0" step="1" class="{inp} mt-1" /></label>
      </div>
      <div class="grid grid-cols-2 gap-3 mt-5 text-center">
        <div class="{card}"><div class="text-xs text-zinc-500">原稿用紙（400字）</div><div id="tmGenkou" class="text-xl font-bold text-white mt-1">–</div></div>
        <div class="{card}"><div class="text-xs text-zinc-500">同じ内容を英語で書くと</div><div id="tmEn" class="text-xl font-bold text-white mt-1">–</div></div>
      </div>
      <p class="mt-4 text-xs text-zinc-500 leading-relaxed">目安です。ふつうの日本語の文章で GPT は1トークンあたり約1.2文字。漢字とかなの割合で変わります。実際の文章の正確な数は<a class="text-violet-300 underline" href="/ja/">トークンカウンター</a>で数えられます。</p>
    </section>

    <section class="prose-ts mt-12 max-w-3xl mx-auto bg-zinc-900/40 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <h2 style="margin-top:0">早見表（ふつうの日本語）</h2>
      <div class="overflow-x-auto"><table><thead><tr><th>トークン</th><th>GPT</th><th>Claude Opus / Sonnet</th><th>Gemini</th><th>原稿用紙（GPT）</th></tr></thead><tbody>{table}</tbody></table></div>
      <p>12.8万トークンは、よくあるコンテキストウィンドウの大きさです。GPT なら日本語で約15万字、原稿用紙380枚ほどが一度に入ります。</p>
      <h2>数字の出どころ</h2>
      <p>同じカスタマーサポート用のプロンプトを日本語と英語で書き、GPT の現行トークナイザー（o200k）で数えました。日本語は73文字で61トークン、<strong>1トークンあたり約1.2文字</strong>で、同じ内容の英語より<strong>約79%多いトークン</strong>になりました。Claude と Gemini の差はトークンカウンターと同じ係数（英文での実測：Claude Opus・Sonnet は約30%多く、Gemini は約5%少ない）を使っているので、日本語では多少ずれることがあります。詳しくは<a href="/ja/blog/token-mojisuu">1トークンは何文字？</a>と<a href="/ja/blog/nihongo-tokens-gpt">日本語は GPT で何トークン？</a>をご覧ください。</p>
      <h2>関連</h2>
      <ul>
        <li><a href="/ja/">AI トークンカウンター</a> — 実際の文章のトークン数と API 料金</li>
        <li><a href="/ja/blog/token-kazoekata">GPT・Claude・Gemini のトークンの数え方</a></li>
        <li><a href="/ja/blog/ai-subscription-ryoukin-hikaku">生成AIのサブスク料金比較（日本円）</a></li>
      </ul>
    </section>

    <section class="mt-12 max-w-5xl mx-auto grid sm:grid-cols-2 gap-4">
{faq_cards}
    </section>
    <script>
    (() => {{
      const CPT = {CPT_JA}, JA = {JA_VS_EN}, TPW = {TPW_EN}, G = {GENKOU};
      const $ = id => document.getElementById(id);
      const tok = $('tmTokens'), chr = $('tmChars'), model = $('tmModel');
      const f = () => parseFloat(model.value);
      const fmt = n => isFinite(n) ? Math.round(n).toLocaleString('ja-JP') : '–';
      let last = 'tok';
      function out(t, c) {{
        $('tmGenkou').textContent = isFinite(c) ? (c / G).toLocaleString('ja-JP', {{maximumFractionDigits: 1}}) + '枚' : '–';
        const enTok = t / JA;
        $('tmEn').textContent = isFinite(enTok) ? '約' + fmt(enTok / f() / TPW) + '語・' + fmt(enTok) + 'トークン' : '–';
      }}
      function fromTokens() {{ const t = parseFloat(tok.value); const c = t * CPT / f(); chr.value = isFinite(c) ? Math.round(c) : ''; out(t, c); }}
      function fromChars() {{ const c = parseFloat(chr.value); const t = c / CPT * f(); tok.value = isFinite(t) ? Math.round(t) : ''; out(t, c); }}
      tok.addEventListener('input', () => {{ last = 'tok'; fromTokens(); }});
      chr.addEventListener('input', () => {{ last = 'chr'; fromChars(); }});
      model.addEventListener('change', () => last === 'tok' ? fromTokens() : fromChars());
      fromTokens();
    }})();
    </script>'''
