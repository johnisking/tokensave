# -*- coding: utf-8 -*-
"""Model-specific landing pages that reuse the token counter with a provider preselected.

People search "claude token counter" far more than a generic "token counter" in some markets,
so /claude-token-counter (and /ko/, /ja/) open the same tool with the Claude tab active, plus
a Claude-specific title, intro, price table and FAQ.
"""
import html
import compare

esc = lambda s: html.escape(str(s), quote=True)
CLAUDE_IDS = ["claude-fable-5-1", "claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-4-5"]
PATHS = {"en": "/claude-token-counter", "ko": "/ko/claude-token-counter", "ja": "/ja/claude-token-counter"}

TXT = {
 "en": dict(
    title="Claude Token Counter – Opus, Sonnet, Haiku",
    desc="Count Claude tokens and API cost for Opus 5.5, Sonnet 5.5 and Haiku 4.5. Free, in your browser, nothing uploaded.",
    h1="Claude Token Counter", sub="Count tokens and API cost for Claude Opus 5.5, Sonnet 5.5 and Haiku 4.5, in any language.",
    g_h="How Claude counts tokens",
    g_p=["Claude uses its own tokenizer, which Anthropic does not publish as a library. For the same English text it produces about <strong>30% more tokens</strong> than GPT's tokenizer, so the same prompt costs more tokens on Claude than the price per token alone suggests. This counter applies that difference automatically, so the Claude numbers above are a close estimate.",
         "Need the exact count for a request? Anthropic's API has a token counting endpoint (<code>count_tokens</code>) that returns the precise number before you send. Use this page for quick estimates and comparing models; use the API when you need the exact figure."],
    t_h="Claude API prices", th=("Model", "Input / output per 1M", "1,000 chat requests"),
    t_note="Chat request = 1,500 input + 400 output tokens of English text, after Claude's tokenizer difference. Standard list prices, no caching or batch discounts.",
    links_h="Compare Claude", links=[("/compare/claude-sonnet-5-5-vs-claude-opus-5-5", "Claude Sonnet 5.5 vs Opus 5.5"),
        ("/compare/gpt-6-sol-vs-claude-sonnet-5-5", "GPT-6 Sol vs Claude Sonnet 5.5"), ("/compare/gemini-4-argon-vs-claude-opus-5-5", "Gemini 4 Argon vs Claude Opus 5.5"),
        ("/compare/performance", "AI model capability vs price"), ("/agents", "Claude Code monthly cost calculator")],
    faq=[("How do I count tokens for Claude?", "Paste your text above with the Claude tab selected. The counter shows tokens, characters and the input and output cost on Claude Opus, Sonnet and Haiku. For an exact count from Anthropic, use the count_tokens endpoint of the Claude API."),
         ("Does Claude use the same tokenizer as GPT?", "No. Claude has its own tokenizer and usually needs about 30% more tokens than GPT for the same English text. This counter applies that difference to its estimate."),
         ("How much does Claude cost per token?", "{prices}"),
         ("Is my text sent anywhere?", "No. The count runs in your browser and your text is never uploaded.")],
 ),
 "ko": dict(
    title="Claude 토큰 계산기 – Opus·Sonnet·Haiku",
    desc="Claude Opus 5.5, Sonnet 5.5, Haiku 4.5의 토큰 수와 API 비용을 계산합니다. 무료, 브라우저에서 처리, 업로드 없음.",
    h1="Claude 토큰 계산기 (Claude Token Counter)", sub="Claude Opus 5.5, Sonnet 5.5, Haiku 4.5의 토큰 수와 API 비용을 바로 계산합니다. 한국어도 됩니다.",
    g_h="Claude는 토큰을 어떻게 셀까",
    g_p=["Claude는 자체 토크나이저를 쓰고, Anthropic은 이를 라이브러리로 공개하지 않았습니다. 같은 영어 문장이면 GPT보다 <strong>토큰이 약 30% 더</strong> 나옵니다. 그래서 같은 프롬프트라도 토큰당 가격만 볼 때보다 Claude 쪽 비용이 더 듭니다. 이 계산기는 그 차이를 자동으로 반영하므로, 위의 Claude 숫자는 실제에 가까운 추정치입니다.",
         "요청 하나의 정확한 토큰 수가 필요하면 Claude API의 토큰 계산 기능(<code>count_tokens</code>)으로 보내기 전에 확인할 수 있습니다. 빠른 추정과 모델 비교는 이 페이지에서, 정확한 숫자는 API로 확인하세요. 한국어는 영어보다 토큰을 약 1.44배 쓰니 같은 내용이면 비용도 그만큼 더 듭니다."],
    t_h="Claude API 가격", th=("모델", "100만 토큰당 입력 / 출력", "대화 요청 1,000번"),
    t_note="대화 요청 1번 = 영어 기준 입력 1,500 + 출력 400토큰, Claude 토크나이저 차이 반영. 정가 기준이며 캐싱·배치 할인은 넣지 않았습니다.",
    links_h="Claude 비교", links=[("/compare/claude-sonnet-5-5-vs-claude-opus-5-5", "Claude Sonnet 5.5 vs Opus 5.5 (영어)"),
        ("/compare/gpt-6-sol-vs-claude-sonnet-5-5", "GPT-6 Sol vs Claude Sonnet 5.5 (영어)"), ("/ko/compare/performance", "AI 모델 성능 vs 가격 순위"),
        ("/ko/blog/claude-code-yogeum", "Claude Code 요금: 한 달에 얼마?"), ("/ko/agents", "Claude Code 월 비용 계산기")],
    faq=[("Claude 토큰은 어떻게 세나요?", "위 입력창에 글을 붙여 넣고 Claude 탭을 고르면 토큰 수, 글자 수, Opus·Sonnet·Haiku의 입력·출력 비용이 바로 나옵니다. Anthropic 기준의 정확한 숫자는 Claude API의 count_tokens 기능으로 확인할 수 있습니다."),
         ("Claude와 GPT는 토크나이저가 같나요?", "아닙니다. Claude는 자체 토크나이저를 쓰고, 같은 영어 문장에 GPT보다 토큰이 약 30% 더 나옵니다. 이 계산기는 그 차이를 추정치에 반영합니다."),
         ("Claude 토큰 가격은 얼마인가요?", "{prices}"),
         ("입력한 글이 어딘가로 전송되나요?", "아닙니다. 계산은 브라우저 안에서만 이뤄지고 글은 업로드되지 않습니다.")],
 ),
 "ja": dict(
    title="Claude トークンカウンター – Opus・Sonnet・Haiku",
    desc="Claude Opus 5.5・Sonnet 5.5・Haiku 4.5 のトークン数とAPI料金を計算。無料、ブラウザ内で処理、アップロードなし。",
    h1="Claude トークンカウンター（Claude Token Counter）", sub="Claude Opus 5.5・Sonnet 5.5・Haiku 4.5 のトークン数とAPI料金をすぐに計算。日本語にも対応。",
    g_h="Claude のトークンの数え方",
    g_p=["Claude は独自のトークナイザーを使っており、Anthropic はライブラリとして公開していません。同じ英文なら GPT より<strong>約30%多くトークンを使います</strong>。そのため同じプロンプトでも、トークン単価から想像するより Claude の費用は高くなります。このカウンターはその差を自動で反映するので、上の Claude の数字は実際に近い推定値です。",
         "1件のリクエストの正確なトークン数が必要なら、Claude API のトークン計算機能（<code>count_tokens</code>）で送信前に確認できます。手早い見積もりとモデル比較はこのページで、正確な数字は API でどうぞ。日本語は英語の約1.79倍のトークンを使うため、同じ内容なら費用もそのぶん増えます。"],
    t_h="Claude API 料金", th=("モデル", "100万トークンあたり入力 / 出力", "チャット1,000回"),
    t_note="チャット1回 = 英語で入力1,500 + 出力400トークン、Claude のトークナイザー差を反映。定価で、キャッシュ・バッチ割引は含みません。",
    links_h="Claude の比較", links=[("/compare/claude-sonnet-5-5-vs-claude-opus-5-5", "Claude Sonnet 5.5 vs Opus 5.5（英語）"),
        ("/compare/gpt-6-sol-vs-claude-sonnet-5-5", "GPT-6 Sol vs Claude Sonnet 5.5（英語）"), ("/ja/compare/performance", "AIモデルの性能と価格ランキング"),
        ("/ja/blog/claude-code-ryoukin", "Claude Code の料金：月いくら？"), ("/ja/agents", "Claude Code 月額コスト計算機")],
    faq=[("Claude のトークンはどう数えますか？", "上の入力欄にテキストを貼り付けて Claude タブを選ぶと、トークン数、文字数、Opus・Sonnet・Haiku の入力・出力料金がすぐに表示されます。Anthropic 基準の正確な数は Claude API の count_tokens 機能で確認できます。"),
         ("Claude と GPT のトークナイザーは同じですか？", "いいえ。Claude は独自のトークナイザーを使い、同じ英文で GPT より約30%多くトークンを使います。このカウンターはその差を推定値に反映しています。"),
         ("Claude のトークン料金はいくらですか？", "{prices}"),
         ("入力したテキストはどこかに送信されますか？", "いいえ。計算はブラウザ内だけで行われ、テキストはアップロードされません。")],
 ),
}

def guide_and_faq(tag, llm, spec=None):
    spec = spec or SPECS[0]
    t = spec['txt'][tag]
    models = compare.load_models(llm)
    rows, plain = [], []
    for mid in spec['ids']:
        m = models.get(mid)
        if not m:
            continue
        k = compare.cost(m, 1500, 400) * 1000
        rows.append(f"<tr><td><strong>{esc(m['name'])}</strong></td><td>${m['inp']:g} / ${m['out']:g}</td><td>${k:.2f}</td></tr>")
        plain.append(f"{m['name']} ${m['inp']:g} / ${m['out']:g}")
    tbl = f"<table><thead><tr>{''.join(f'<th>{h}</th>' for h in t['th'])}</tr></thead><tbody>{''.join(rows)}</tbody></table>"
    links = "".join(f'<li><a href="{p}">{esc(n)}</a></li>' for p, n in t["links"])
    paras = "".join(f"<p>{p}</p>" for p in t["g_p"])
    guide = f"""    <section class="prose-ts mt-12 max-w-3xl mx-auto bg-zinc-900/40 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <h2 style="margin-top:0">{t['g_h']}</h2>
      {paras}
      <h2>{t['t_h']}</h2>
      <div class="overflow-x-auto">{tbl}</div>
      <p class="text-xs text-zinc-500">{t['t_note']} ({esc(llm.get('checked', ''))})</p>
      <h2>{t['links_h']}</h2>
      <ul>{links}</ul>
    </section>"""
    price_sent = {"en": "Per million input / output tokens: ", "ko": "100만 토큰당 입력 / 출력: ", "ja": "100万トークンあたり入力 / 出力："}[tag] + "; ".join(plain) + "."
    faq = [(q, a.replace("{prices}", price_sent)) for q, a in t["faq"]]
    return guide, faq


OPENAI_IDS = ["gpt-6-astra", "gpt-6-1-sol", "gpt-6-sol", "gpt-6-luna", "gpt-5-mini", "gpt-4o"]
GEMINI_IDS = ["gemini-4-argon", "gemini-3-1-pro", "gemini-3-8-flash", "gemini-3-5-flash-lite", "gemini-3-1-flash-lite"]

OPENAI_TXT = {"en": dict(
    title="OpenAI Token Counter – GPT-6 API Cost",
    desc="Count GPT tokens and API cost for GPT-6 Astra, GPT-6.1 Sol, Sol and Luna. Free, runs in your browser, nothing uploaded.",
    h1="OpenAI Token Counter & GPT API Cost Calculator",
    sub="Count tokens and see what GPT-6 Astra, GPT-6.1 Sol, GPT-6 Sol and Luna charge for your prompt, in any language.",
    g_h="How GPT counts tokens",
    g_p=["OpenAI publishes its tokenizer, so GPT counts can be exact. GPT-4o, GPT-4.1 and GPT-5 mini and nano use the <code>o200k</code> tokenizer, and this counter uses the same one, so their numbers match what OpenAI bills. OpenAI has not published the tokenizer for GPT-5.4 and later, including GPT-6, so for those models the count is an o200k-based estimate.",
         "The biggest price decision on OpenAI is the model, not a discount. GPT-6 Astra costs 5 times GPT-6 Sol per token, and Sol costs 20 times GPT-6 Luna. Most apps run well on Sol or Luna and send only the hard requests to Astra.",
         "Two ways to pay less on the same model: <strong>prompt caching</strong> bills repeated input (fixed instructions, documents) at a tenth of the normal input price, and the <strong>Batch API</strong> charges about half for work that can wait up to 24 hours. Requests with more than 272,000 input tokens are billed at a higher rate than the table below."],
    t_h="OpenAI API prices", th=("Model", "Input / output per 1M", "1,000 chat requests"),
    t_note="Chat request = 1,500 input + 400 output tokens of English text. Standard list prices, no caching or batch discounts.",
    links_h="More on GPT costs", links=[("/blog/gpt-6-api-pricing", "GPT-6 API pricing: Astra vs Sol vs Luna"),
        ("/compare/gpt-6-sol-vs-gpt-6-astra", "GPT-6 Sol vs GPT-6 Astra"), ("/compare/gpt-6-sol-vs-claude-sonnet-5-5", "GPT-6 Sol vs Claude Sonnet 5.5"),
        ("/plans", "ChatGPT Plus or the API: which costs less for you?"), ("/blog/prompt-caching-explained", "Prompt caching explained")],
    faq=[("How do I count tokens for GPT-6?", "Paste your text above with the GPT tab selected. You get the token count, characters and the input and output cost on each GPT model. OpenAI has not published GPT-6's tokenizer yet, so GPT-6 counts are an estimate based on o200k; GPT-4o, GPT-4.1 and GPT-5 mini counts are exact."),
         ("Is this the same tokenizer as tiktoken?", "Yes for the exact models: it uses the same o200k encoding that OpenAI's tiktoken library uses for GPT-4o and GPT-5 mini, running in your browser."),
         ("How much does GPT-6 cost per token?", "{prices}"),
         ("Should I use ChatGPT Plus or the API?", "It depends on how much you use. The ChatGPT Plus or API calculator on this site compares a monthly subscription with pay-per-token API cost for your own usage."),
         ("Is my text sent anywhere?", "No. The count runs in your browser and your text is never uploaded.")],
)}

GEMINI_TXT = {"en": dict(
    title="Gemini Token Counter – Gemini API Cost",
    desc="Count Gemini tokens and API cost for Gemini 4 Argon, 3.1 Pro, 3.8 Flash and Flash-Lite. Free, in your browser, nothing uploaded.",
    h1="Gemini Token Counter & API Cost Calculator",
    sub="Count tokens and see what Gemini 4 Argon, Gemini 3.1 Pro, 3.8 Flash and Flash-Lite charge for your prompt, in any language.",
    g_h="How Gemini counts tokens",
    g_p=["Google does not publish Gemini's tokenizer as a library. For English text it produces slightly fewer tokens than GPT, about 5% fewer, and this counter applies that difference, so the Gemini numbers above are a close estimate. For the exact count of one request, the Gemini API has a <code>countTokens</code> method you can call before sending.",
         "Gemini 4 Argon, Google's newest top model (announced September 30, 2026), launched at an <strong>introductory price of $2 input / $10 output</strong> per million tokens, moving later to a standard $4 / $20. Google has not said how long the introductory rate lasts; the table below uses the standard price. Cached input on Argon is 95% off the normal input price.",
         "For high-volume work the Flash models are where Gemini is cheapest: Gemini 3.1 Flash-Lite costs a sixteenth of Argon's standard input price."],
    t_h="Gemini API prices", th=("Model", "Input / output per 1M", "1,000 chat requests"),
    t_note="Chat request = 1,500 input + 400 output tokens of English text, after Gemini's tokenizer difference. Standard list prices, no caching or batch discounts.",
    links_h="More on Gemini costs", links=[("/blog/gemini-4-argon-api-pricing", "Gemini 4 Argon API pricing vs GPT-6 and Claude"),
        ("/compare/gemini-4-argon-vs-gemini-3-1-pro", "Gemini 4 Argon vs Gemini 3.1 Pro"), ("/compare/gemini-4-argon-vs-claude-opus-5-5", "Gemini 4 Argon vs Claude Opus 5.5"),
        ("/compare/gpt-6-luna-vs-gemini-3-8-flash", "GPT-6 Luna vs Gemini 3.8 Flash"), ("/compare/performance", "AI model capability vs price")],
    faq=[("How do I count tokens for Gemini?", "Paste your text above with the Gemini tab selected. You get the token count, characters and the input and output cost on Gemini 4 Argon, 3.1 Pro, 3.8 Flash and Flash-Lite. For Google's exact number, call countTokens in the Gemini API."),
         ("Does Gemini use the same tokenizer as GPT?", "No. Gemini has its own tokenizer and usually needs about 5% fewer tokens than GPT for the same English text. This counter applies that difference to its estimate."),
         ("How much does Gemini cost per token?", "{prices}"),
         ("What is the Gemini 4 Argon introductory price?", "At launch Gemini 4 Argon is $2 per million input tokens and $10 per million output tokens, half its standard $4 / $20. Google has not announced when the introductory rate ends."),
         ("Is my text sent anywhere?", "No. The count runs in your browser and your text is never uploaded.")],
)}

SPECS = [
    dict(key="claude", provider="claude", model="claude-sonnet-5-5", ids=CLAUDE_IDS, paths=PATHS, txt=TXT,
         nav={"en": "Claude token counter", "ko": "Claude 토큰 계산기", "ja": "Claude トークンカウンター"}),
    dict(key="openai", provider="openai", model="gpt-6-sol", ids=OPENAI_IDS, paths={"en": "/openai-token-counter"}, txt=OPENAI_TXT,
         nav={"en": "OpenAI (GPT) token counter"}),
    dict(key="gemini", provider="gemini", model="gemini-3-8-flash", ids=GEMINI_IDS, paths={"en": "/gemini-token-counter"}, txt=GEMINI_TXT,
         nav={"en": "Gemini token counter"}),
]
