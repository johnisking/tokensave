# -*- coding: utf-8 -*-
# Language-specific articles. Body HTML lives in src/blog/<tag>.html, generated from
# blog_src/<tag>.md by `python3 _source/make_blog.py` (needs the `markdown` package; the
# site build itself does not).
# All four are versions of the same study, so they point at each other with hreflang.

BLOG_DATE = "2026-09-30"

BLOG = [
    dict(tag="cs", path="/cs/blog/cestina-tokeny-gpt",
         title="Čeština v GPT stojí 2× víc tokenů než angličtina",
         desc="Stejný prompt v 41 jazycích: čeština patří k nejdražším, 68 tokenů proti 34. Proč a jak ušetřit.",
         byline="Jonhisking · 30. 9. 2026",
         cta="Změřte si vlastní text: kolik tokenů a peněz stojí váš prompt v češtině oproti angličtině.",
         ctaBtn="Otevřít počítadlo tokenů"),
    dict(tag="pl", path="/pl/blog/polski-tokeny-gpt",
         title="Polski w GPT zużywa o 88% więcej tokenów niż angielski",
         desc="Ten sam prompt w 41 językach: polski zużywa o 88% więcej tokenów niż angielski. Licznik tokenów, dlaczego tak jest i jak oszczędzać.",
         byline="Jonhisking · 30.09.2026",
         cta="Sprawdź własny tekst: ile tokenów i pieniędzy kosztuje twój prompt po polsku w porównaniu z angielskim.",
         ctaBtn="Otwórz licznik tokenów"),
    dict(tag="ja", path="/ja/blog/nihongo-tokens-gpt",
         title="日本語プロンプトは英語で送るとトークン44%節約：41言語で実測",
         desc="同じプロンプトを41言語で測定。日本語は英語の1.79倍。ボタンひとつで英語に変えてトークンを減らす方法まで。",
         byline="Jonhisking · 2026年9月30日（10月2日更新）", date="2026-10-02",
         cta="プロンプトを貼り付けて💸 トークン節約を押してみてください。英語にするとどれだけ減るかすぐ分かります。",
         ctaBtn="トークンカウンターを開く"),
    dict(tag="ko", path="/ko/blog/korean-tokens-gpt",
         title="한국어 프롬프트, 영어로 보내면 토큰 31% 절약: 41개 언어 실측",
         desc="같은 프롬프트를 41개 언어로 측정. 한국어는 영어의 1.44배. 버튼 하나로 영어로 바꿔 토큰을 아끼는 방법까지.",
         byline="Jonhisking · 2026년 9월 30일 (10월 2일 업데이트)", date="2026-10-02",
         cta="내 프롬프트를 붙여 넣고 💸 토큰 절약을 눌러 보세요. 영어로 바꾸면 토큰이 얼마나 줄어드는지 바로 보여드립니다.",
         ctaBtn="토큰 계산기 열기"),
]

# Generated articles (blog_gen.py): English overview + 22 more languages
import json as _json, os as _os
_auto = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "blog_data", "auto.json")
BLOG += _json.load(open(_auto, encoding="utf-8"))


# "ChatGPT Pro 100 vs 200 vs 500" (blog_src/pro-<tag>.md), links to the /plans calculator
PRO = [
 {
  "tag": "en",
  "path": "/blog/chatgpt-pro-100-vs-200-vs-500",
  "src": "pro-en",
  "title": "ChatGPT Pro 100 vs 200 vs 500: Differences and Which GPT Pro Plan to Pick",
  "desc": "GPT Pro now has $100, $200 and $500 plans. All cost the same per unit of usage and differ only in usage (5x, 10x, 25x) and Ultrafast. Which to pick.",
  "byline": "Jonhisking · October 1, 2026",
  "cta": "Enter how many messages you send, how long they are and your language, and see whether a subscription or the API is cheaper for you.",
  "ctaBtn": "Open the Subscription vs API calculator",
  "date": "2026-10-01"
 },
 {
  "tag": "ko",
  "path": "/ko/blog/chatgpt-pro-yogeumje-bigyo",
  "src": "pro-ko",
  "title": "GPT 프로 요금제 비교: ChatGPT Pro 100·200·500 차이와 고르는 법",
  "desc": "GPT 프로 요금제가 Pro 100·200·500으로 나뉘었습니다. 셋 다 사용량당 가격은 같고 차이는 사용량(5·10·25배)과 Ultrafast뿐입니다. 고르는 법과 Pro 200 한도 축소까지.",
  "byline": "Jonhisking · 2026년 10월 1일",
  "cta": "내 메시지 수와 길이, 언어를 넣고 구독과 API 중 어느 쪽이 더 싼지 직접 계산해 보세요.",
  "ctaBtn": "구독 vs API 계산기 열기",
  "date": "2026-10-01"
 },
 {
  "tag": "ja",
  "path": "/ja/blog/chatgpt-pro-ryokin-hikaku",
  "src": "pro-ja",
  "title": "ChatGPT Pro 料金比較：Pro 100・200・500どれを選ぶ？",
  "desc": "ChatGPT Proが3プランに。Pro 100・200・500の料金と利用量を比較し、Pro 200の縮小やAPIとの料金差、日本語のトークン約1.8倍まで解説します。",
  "byline": "Jonhisking · 2026年10月1日",
  "cta": "メッセージ数・長さ・言語を入力して、あなたの使い方ならサブスクとAPIのどちらが安いか計算してみましょう。",
  "ctaBtn": "料金を計算する",
  "date": "2026-10-01"
 },
 {
  "tag": "es",
  "path": "/es/blog/chatgpt-pro-100-200-500-precios",
  "src": "pro-es",
  "title": "ChatGPT Pro 100, 200 o 500: precios y cuál vale la pena",
  "desc": "Planes de ChatGPT Pro 100, 200 y 500: precio, uso frente a Plus, Ultrafast y cuándo te conviene más la API.",
  "byline": "Jonhisking · 1 de octubre de 2026",
  "cta": "Calcula cuánto te costaría tu uso real con una suscripción frente a la API.",
  "ctaBtn": "Calcular mi costo",
  "date": "2026-10-01"
 },
 {
  "tag": "pt",
  "path": "/pt/blog/chatgpt-pro-100-200-500-precos",
  "src": "pro-pt",
  "title": "ChatGPT Pro 100, 200 ou 500: qual plano vale a pena?",
  "desc": "Pro 100, Pro 200 ou Pro 500: preço, uso e Ultrafast comparados, e quando a API do ChatGPT sai mais barata.",
  "byline": "Jonhisking · 1 de outubro de 2026",
  "cta": "Calcule quanto você pagaria pela sua assinatura e quanto gastaria usando a API.",
  "ctaBtn": "Calcular meu custo",
  "date": "2026-10-01"
 }
]


MISTRAL_FR = [
 {
  "tag": "fr",
  "path": "/fr/blog/mistral-chatgpt-cout-prompt-francais",
  "src": "mistral-fr",
  "title": "Mistral ou ChatGPT : combien coûte vraiment un prompt en français ?",
  "desc": "Le français coûte 12 à 30 % de tokens en plus que l'anglais, chez OpenAI comme chez Mistral. Mesures, explications et astuce.",
  "byline": "Jonhisking · 2 octobre 2026",
  "cta": "Collez votre prompt pour voir ses tokens et son coût, puis traduisez-le en anglais en un clic.",
  "ctaBtn": "Ouvrir le compteur de tokens",
  "date": "2026-10-02"
 },
]

# French articles added 2026-10-03
MISTRAL_FR += [
 {"tag": "fr", "path": "/fr/blog/compteur-de-tokens-pourquoi", "src": "compteur-fr",
  "title": "Pourquoi utiliser un compteur de tokens ? 5 raisons (mesures en français)",
  "desc": "Le même e-mail coûte 21 % de tokens en plus en français, et la réponse coûte souvent plus que la question. 5 raisons de compter ses tokens avant d'envoyer.",
  "byline": "Jonhisking · 3 octobre 2026",
  "cta": "Collez votre prompt pour voir ses tokens et son coût, puis traduisez-le en anglais en un clic.",
  "ctaBtn": "Ouvrir le compteur de tokens", "date": "2026-10-03"},
 {"tag": "fr", "path": "/fr/blog/souverainete-ia-tokens", "src": "souverainete-fr",
  "title": "Souveraineté de l'IA : ce que ça change pour vos prompts (langue, données, coût)",
  "desc": "Le français coûte 11 à 21 % de tokens en plus, même chez Mistral. Langue, données, coût et AI Act : ce que la souveraineté de l'IA change concrètement.",
  "byline": "Jonhisking · 3 octobre 2026",
  "cta": "Comptez les tokens et le coût de votre prompt sans rien envoyer : tout se passe dans votre navigateur.",
  "ctaBtn": "Ouvrir le compteur de tokens", "date": "2026-10-03"},
]

PROMPT_PL = [
 {
  "tag": "pl",
  "path": "/pl/blog/ile-kosztuje-prompt-po-polsku",
  "src": "prompt-pl",
  "title": "Ile naprawdę kosztuje prompt po polsku? GPT i Mistral zmierzone",
  "desc": "Polski zużywa o 50–88% więcej tokenów niż angielski, w GPT i w Mistralu. Pomiary, przyczyny i prosty sposób, by płacić mniej.",
  "byline": "Jonhisking · 2 października 2026",
  "cta": "Wklej swój prompt, zobacz tokeny i koszt, a potem przetłumacz go na angielski jednym kliknięciem.",
  "ctaBtn": "Otwórz licznik tokenów",
  "date": "2026-10-02"
 },
]

# Polish article added 2026-10-03
PROMPT_PL += [
 {"tag": "pl", "path": "/pl/blog/jak-skrocic-prompt-po-polsku", "src": "skracanie-pl",
  "title": "Jak pisać prompty po polsku taniej? Sprawdziłem 7 wersji (GPT i Mistral)",
  "desc": "Krótszy polski prompt to 34% mniej tokenów, a usuwanie polskich znaków nic nie daje. Skrócony prompt systemowy jest prawie tak tani jak angielski.",
  "byline": "Jonhisking · 3 października 2026",
  "cta": "Wklej swój prompt, zobacz tokeny i koszt, a potem przetłumacz go na angielski jednym kliknięciem.",
  "ctaBtn": "Otwórz licznik tokenów", "date": "2026-10-03"},
]

# English guides (blog_src/g-*.md), one article each. "tool" = key of the calculator the CTA opens.
_G = lambda slug, src, tool, title, desc, cta, btn: dict(
    tag="en", path="/blog/" + slug, src=src, tool=tool, title=title, desc=desc,
    byline="Jonhisking · October 2, 2026", cta=cta, ctaBtn=btn, date="2026-10-02")
GUIDES = [
 _G("what-is-a-token", "g-token", "token", "What Is a Token? A Plain-English Guide for AI Users",
    "What AI tokens are, how many your text uses, why other languages need more, and why tokens decide cost and quality.",
    "Paste any text to see its exact token count and cost on 30+ models.", "Open the token counter"),
 _G("how-to-estimate-ai-api-cost", "g-estimate", "token", "How to Estimate Your AI API Bill Before You Build",
    "A simple formula and a worked example for estimating monthly AI API cost, plus the multipliers most estimates miss.",
    "Measure your real prompt and answer, then see the cost on every model at once.", "Open the token counter"),
 _G("why-output-tokens-cost-more", "g-output", "token", "Why Output Tokens Cost More (and 6 Ways to Use Fewer)",
    "Output tokens cost 2-6x more than input on current AI APIs. Why, the hidden cost of reasoning, and how to cut it.",
    "Paste a typical prompt and answer to see how much each side costs.", "Open the token counter"),
 _G("context-window-explained", "g-context", "token", "Context Windows Explained: Why Long Chats Get Worse and Cost More",
    "What a context window is, why AI forgets things in long chats, why long chats cost more, and what to do instead.",
    "See how much of each model's context window your text fills.", "Open the token counter"),
 _G("cut-token-cost-non-english-prompts", "g-language", "token", "Prompting in Korean, Japanese or Hindi? How to Cut the Token Cost",
    "Non-English prompts use up to 1.8x the tokens of English. Measured ratios and five ways to pay less, starting with one click.",
    "Paste your prompt, press Save tokens, and see how many tokens you save.", "Open the token counter"),
 _G("ai-video-cost-per-minute", "g-video", "video", "How Much Does One Minute of AI Video Cost?",
    "One minute of AI video on Veo, Kling, Grok, FLUX, Seedance and more, from $3 to $24 at list price, and why retries triple it.",
    "Set clip length, resolution and audio, and rank every video model by total cost.", "Open the video cost calculator"),
 _G("ai-image-cost-per-image", "g-image", "image", "AI Image Generation Cost per Image, Compared",
    "Price per image on GPT Image, Nano Banana, FLUX.2, Grok Imagine, Seedream and Runway, from $0.01 to $0.20 at 1K.",
    "Pick a resolution and number of images to compare every model.", "Open the image cost calculator"),
 _G("chatgpt-subscription-vs-api", "g-plans", "plans", "ChatGPT Plus or the API: Which Is Cheaper for You?",
    "When a $20 AI subscription beats paying per token, and when the API is far cheaper, with monthly costs by usage.",
    "Enter how you chat and see the API cost next to every ChatGPT, Claude and Gemini plan.", "Open the Subscription vs API calculator"),
 _G("ai-coding-agent-cost", "g-agents", "agents", "What Does an AI Coding Agent Really Cost per Task?",
    "Why Claude Code, Codex and Gemini CLI use millions of tokens per task, what that costs on the API, and when a plan is cheaper.",
    "Set task size and tasks per day to compare API cost with every plan.", "Open the agent cost calculator"),
]

# In-depth guides, batch 2 (original measurements + explainers)
GUIDES += [
 _G("json-vs-yaml-vs-csv-tokens", "g-formats", "token", "JSON vs YAML vs CSV: Which Data Format Uses the Fewest Tokens?",
    "One table in 9 formats: row-by-row pretty JSON used 2.9x the tokens of CSV, XML 3.6x, columnar JSON about the same as CSV.",
    "Paste your data in two formats and compare the tokens.", "Open the token counter"),
 _G("how-many-tokens-does-code-use", "g-code", "agents", "How Many Tokens Does Code Use? Indentation, Comments and Minification",
    "Measured: indentation is almost free, docstrings are not, minified JS is half the tokens. Where coding tokens really go.",
    "Estimate what a month of coding-agent work costs on the API and on each plan.", "Open the agent cost calculator"),
 _G("numbers-dates-emoji-tokens", "g-numbers", "token", "Why Numbers, IDs, Dates and Emoji Use More Tokens Than You Think",
    "Measured on GPT's tokenizer: numbers split into 3-digit chunks, a UUID is 18 tokens, one emoji can be 11. How to save.",
    "Paste any text and see exactly how it splits into tokens.", "Open the token counter"),
 _G("gpt-tokenizer-cl100k-vs-o200k", "g-tokenizer", "token", "How GPT's New Tokenizer Cut Costs in 40 Languages",
    "cl100k vs o200k measured in 41 languages: Malayalam -82%, Hindi -67%, Korean -42%. How tokenizers work and what is left.",
    "See how many tokens your own language needs, and how much translating to English saves.", "Open the token counter"),
 _G("prompt-caching-explained", "g-caching", "token", "Prompt Caching Explained: Cut Repeated Input Costs by Around 90%",
    "How prompt caching works, why prompt order matters, a worked cost example, and a checklist to make sure your cache hits.",
    "Measure your system prompt and see what it costs per request on each model.", "Open the token counter"),
 _G("write-shorter-prompts", "g-shorter", "token", "Write Shorter Prompts Without Losing Quality: Measured Before and After",
    "Two real prompts rewritten: 98 to 20 tokens and 122 to 35. What to cut, what to keep, and what it saves at scale.",
    "Paste your prompt to see its token count and clean it up with one click.", "Open the token counter"),
 _G("reasoning-models-cost", "g-reasoning", "token", "Reasoning Models: When Thinking Is Worth Paying For",
    "Hidden reasoning tokens are billed as output and can make a request 10x pricier. When reasoning pays off and when it does not.",
    "Set a longer expected output to see what reasoning adds to each request.", "Open the token counter"),
 _G("batch-api-half-price", "g-batch", "token", "Batch APIs: Half-Price AI for Work That Can Wait",
    "How batch processing works, what it saves on a 100,000-item job, which tasks fit, and tips to avoid wasted runs.",
    "Measure one request, multiply by your item count, and halve it for a batch estimate.", "Open the token counter"),
 _G("rag-vs-long-context-cost", "g-rag", "token", "RAG vs Long Context: What It Costs to Ask Questions About Big Documents",
    "Sending a 500-page manual with every question vs retrieving 8 passages: $0.67 vs $0.009 per question. When to use each.",
    "Paste a sample of your document to see its tokens and cost per question.", "Open the token counter"),
 _G("ai-cost-per-user", "g-unit", "plans", "AI Cost per User: How to Price an App Built on an LLM",
    "Estimate AI cost per user per month, plan for heavy users and free tiers, and the levers that bring the number down.",
    "Compare what heavy chat use costs on the API with every subscription plan.", "Open the Subscription vs API calculator"),
 _G("ai-cost-glossary", "g-glossary", "token", "AI Cost Glossary: 30 Terms Explained in Plain Language",
    "Tokens, tokenizers, cached input, batch pricing, reasoning tokens, context windows, RAG and more, explained simply.",
    "Turn these terms into real numbers for your own text.", "Open the token counter"),
]

# Claude Code guides (EN/KO/JA), each group linked with hreflang; CTA opens the agent calculator
def _cc(tag, path, src, title, desc, byline, cta, btn):
    return dict(tag=tag, path=path, src=src, title=title, desc=desc, byline=byline, cta=cta, ctaBtn=btn, date="2026-10-02")
_BY = {"en": "Jonhisking · October 2, 2026", "ko": "Jonhisking · 2026년 10월 2일", "ja": "Jonhisking · 2026年10月2日"}
_CTA = {"en": ("Set task size and tasks per day to compare Claude Code's API cost with Pro and Max.", "Open the agent cost calculator"),
        "ko": ("작업 크기와 하루 작업 수를 넣고, 클로드 코드의 API 비용을 Pro·Max와 비교해 보세요.", "코딩 에이전트 비용 계산기 열기"),
        "ja": ("タスクの大きさと1日のタスク数を入れて、Claude Code の API 費用を Pro・Max と比べてみましょう。", "エージェント費用計算機を開く")}
CC_COST = [
 _cc("en", "/blog/claude-code-cost-per-month", "cc-cost-en", "Claude Code Cost per Month: Pro vs Max vs API",
     "What Claude Code really costs per month on Pro, Max 5x, Max 20x or the API, with cost per task and when each one is cheapest.", _BY["en"], *_CTA["en"]),
 _cc("ko", "/ko/blog/claude-code-yogeum", "cc-cost-ko", "클로드 코드 요금 한 달에 얼마? Pro·Max·API 비교",
     "클로드 코드를 Pro, Max 5×, Max 20×, API로 쓸 때 한 달 비용과 작업당 비용, 어떤 경우에 무엇이 가장 싼지 정리했습니다.", _BY["ko"], *_CTA["ko"]),
 _cc("ja", "/ja/blog/claude-code-ryoukin", "cc-cost-ja", "Claude Code の料金は月いくら？Pro・Max・API を比較",
     "Claude Code を Pro、Max 5×、Max 20×、API で使ったときの月額とタスクあたりの費用、どれがいちばん安いかを解説します。", _BY["ja"], *_CTA["ja"]),
]
CC_LIMITS = [
 _cc("en", "/blog/claude-code-usage-limits", "cc-limits-en", "Claude Code Usage Limits Explained: 5-Hour and Weekly Caps",
     "How Claude Code's 5-hour and weekly limits work on Pro and Max, what changed in 2026, how to check usage and what to do at the limit.", _BY["en"], *_CTA["en"]),
 _cc("ko", "/ko/blog/claude-code-sayongnyang-hando", "cc-limits-ko", "클로드 코드 사용량 한도 정리: 5시간·주간 한도와 확인 방법",
     "클로드 코드 Pro·Max의 5시간 한도와 주간 한도가 어떻게 작동하는지, 2026년 변경 사항, 사용량 확인법과 한도에 걸렸을 때 대처법.", _BY["ko"], *_CTA["ko"]),
 _cc("ja", "/ja/blog/claude-code-shiyouryou-jougen", "cc-limits-ja", "Claude Code の使用量上限まとめ：5時間・週の上限と確認方法",
     "Claude Code の Pro・Max の5時間上限と週の上限の仕組み、2026年の変更点、使用量の確認方法と上限に当たったときの対処法。", _BY["ja"], *_CTA["ja"]),
]
CC_SAVE = [
 _cc("en", "/blog/claude-code-save-tokens", "cc-save-en", "How to Save Tokens in Claude Code: 9 Habits That Matter",
     "Why Claude Code uses so many tokens and 9 practical ways to cut them, from /clear and /compact to a shorter CLAUDE.md.", _BY["en"], *_CTA["en"]),
 _cc("ko", "/ko/blog/claude-code-token-jeolyak", "cc-save-ko", "클로드 코드 토큰 절약 방법 9가지",
     "클로드 코드가 토큰을 많이 쓰는 이유와 /clear, /compact, 짧은 CLAUDE.md, 영어 지시문까지 토큰을 줄이는 실전 방법 9가지.", _BY["ko"], *_CTA["ko"]),
 _cc("ja", "/ja/blog/claude-code-token-setsuyaku", "cc-save-ja", "Claude Code のトークン節約術9選",
     "Claude Code がトークンを多く使う理由と、/clear・/compact、短い CLAUDE.md、英語の指示まで、トークンを減らす実践的な方法9つ。", _BY["ja"], *_CTA["ja"]),
]

_CTA_PL = {"en": ("Enter how you use AI and see the monthly API cost next to every ChatGPT, Claude and Gemini plan.", "Open the Subscription vs API calculator"),
           "ko": ("내 사용 방식으로 월 API 비용을 챗GPT·Claude·Gemini 모든 요금제와 비교해 보세요.", "구독 vs API 계산기 열기"),
           "ja": ("自分の使い方で、月額 API 費用を ChatGPT・Claude・Gemini の全プランと比べてみましょう。", "サブスク vs API 計算機を開く")}
_CTA_TK = {"en": ("Paste a prompt to see its tokens and cost on every GPT-6 model, Claude and Gemini.", "Open the token counter"),
           "ko": ("프롬프트를 붙여 넣고 GPT-6 각 모델·Claude·Gemini의 토큰과 비용을 비교해 보세요.", "토큰 계산기 열기"),
           "ja": ("プロンプトを貼り付けて、GPT-6 各モデル・Claude・Gemini のトークンと費用を比べましょう。", "トークンカウンターを開く")}
CMP = [
 _cc("en", "/blog/chatgpt-pro-vs-claude-max", "cmp-en", "ChatGPT Pro vs Claude Max: Which $100 or $200 Plan Gives More?",
     "ChatGPT Plus/Pro vs Claude Pro/Max compared: usage per dollar after the September 2026 changes, models, coding agents and which to pick.", _BY["en"], *_CTA_PL["en"]),
 _cc("ko", "/ko/blog/chatgpt-pro-vs-claude-max", "cmp-ko", "챗GPT Pro vs Claude Max 요금제 비교: $100·$200 어디가 더 많이 줄까",
     "챗GPT Plus·Pro와 Claude Pro·Max를 비교했습니다. 2026년 9월 변경 후 1달러당 사용량, 모델, 코딩 에이전트, 무엇을 고를지.", _BY["ko"], *_CTA_PL["ko"]),
 _cc("ja", "/ja/blog/chatgpt-pro-vs-claude-max", "cmp-ja", "ChatGPT Pro vs Claude Max 料金比較：$100・$200でどちらが多く使える？",
     "ChatGPT Plus・Pro と Claude Pro・Max を比較。2026年9月の変更後の1ドルあたり使用量、モデル、コーディングエージェント、選び方。", _BY["ja"], *_CTA_PL["ja"]),
]
GPT6 = [
 _cc("en", "/blog/gpt-6-api-pricing", "gpt6-en", "GPT-6 API Pricing: Astra vs Sol vs Luna, and What It Costs",
     "GPT-6 Astra, Sol and Luna API prices per million tokens, real cost per request, comparison with Claude and Gemini, and which to use.", _BY["en"], *_CTA_TK["en"]),
 _cc("ko", "/ko/blog/gpt-6-api-gagyeok", "gpt6-ko", "GPT-6 API 가격 정리: Astra·Sol·Luna 비교와 실제 비용",
     "GPT-6 Astra·Sol·Luna의 100만 토큰당 API 가격, 요청당 실제 비용, Claude·Gemini 비교, 어떤 모델을 쓸지 정리했습니다.", _BY["ko"], *_CTA_TK["ko"]),
 _cc("ja", "/ja/blog/gpt-6-api-ryoukin", "gpt6-ja", "GPT-6 の API 料金まとめ：Astra・Sol・Luna の比較と実際の費用",
     "GPT-6 Astra・Sol・Luna の100万トークンあたり API 料金、リクエストあたりの実費、Claude・Gemini との比較、どのモデルを使うか。", _BY["ja"], *_CTA_TK["ja"]),
]

API_CMP = [
 _cc("en", "/blog/llm-api-pricing-comparison", "api-en", "LLM API Pricing Compared: 22 Models From GPT-6 to Claude, Gemini and DeepSeek",
     "Input and output API prices of 22 models side by side, the real cost of 10,000 requests, the cheapest LLM APIs, and how to choose.", _BY["en"], *_CTA_TK["en"]),
 _cc("ko", "/ko/blog/llm-api-gagyeok-bigyo", "api-ko", "LLM API 가격 비교: GPT-6·Claude·Gemini·DeepSeek 등 22개 모델",
     "22개 모델의 입력·출력 API 가격을 나란히 비교하고, 요청 1만 건 실제 비용, 가장 싼 LLM API, 고르는 법을 정리했습니다.", _BY["ko"], *_CTA_TK["ko"]),
 _cc("ja", "/ja/blog/llm-api-ryoukin-hikaku", "api-ja", "LLM API 料金比較：GPT-6・Claude・Gemini・DeepSeek など22モデル",
     "22モデルの入力・出力 API 料金を並べて比較し、1万リクエストの実費、いちばん安い LLM API、選び方をまとめました。", _BY["ja"], *_CTA_TK["ja"]),
]
TPW = [
 _cc("en", "/blog/tokens-per-word", "tpw-en", "Tokens per Word, Measured: English and 11 Other Languages",
     "How many tokens per word and per character on current GPT models: about 1.1-1.3 per English word, and the real numbers for other languages.", _BY["en"], *_CTA_TK["en"]),
 _cc("ko", "/ko/blog/token-dangeo-geulja", "tpw-ko", "단어·글자당 토큰 수 실측: 한국어는 몇 글자에 1토큰일까",
     "최신 GPT 모델에서 영어는 단어당 약 1.1~1.3토큰, 한국어·일본어·중국어 등은 글자당 몇 토큰인지 직접 재서 정리했습니다.", _BY["ko"], *_CTA_TK["ko"]),
 _cc("ja", "/ja/blog/token-mojisuu", "tpw-ja", "1トークンは何文字？日本語・英語など12言語で実測",
     "最新の GPT モデルで、英語は1単語あたり約1.1〜1.3トークン、日本語は約1.2文字で1トークン。12言語の実測値をまとめました。", _BY["ja"], *_CTA_TK["ja"]),
]
COUNT = [
 _cc("en", "/blog/how-to-count-tokens-gpt-claude-gemini", "count-en", "How to Count Tokens for GPT, Claude and Gemini",
     "Why GPT, Claude and Gemini count tokens differently, how to get an exact count for each, and a quick way to estimate without code.", _BY["en"], *_CTA_TK["en"]),
 _cc("ko", "/ko/blog/token-segi-bangbeop", "count-ko", "GPT·Claude·Gemini 토큰 세는 방법",
     "GPT, Claude, Gemini가 토큰을 다르게 세는 이유, 각각 정확하게 세는 방법, 코드 없이 바로 어림잡는 방법을 정리했습니다.", _BY["ko"], *_CTA_TK["ko"]),
 _cc("ja", "/ja/blog/token-kazoekata", "count-ja", "GPT・Claude・Gemini のトークンの数え方",
     "GPT・Claude・Gemini でトークン数が違う理由、それぞれ正確に数える方法、コードなしですぐ見積もる方法をまとめました。", _BY["ja"], *_CTA_TK["ja"]),
]

_CTA_AG = _CTA
CHLIM = [
 _cc("en", "/blog/chatgpt-usage-limits", "chlim-en", "ChatGPT Usage Limits in 2026: What Is Still Capped and When It Resets",
     "Text chat is unlimited since August 2026, but GPT-6 Astra, Work, Codex, files and images still have limits. What resets when, and how to check.", _BY["en"], *_CTA_PL["en"]),
 _cc("ko", "/ko/blog/chatgpt-sayongnyang-hando", "chlim-ko", "챗GPT 사용량 한도 정리: 무엇이 아직 제한되고 언제 초기화될까",
     "2026년 8월부터 일반 채팅은 무제한이지만 GPT-6 Astra, Work, Codex, 파일·이미지는 아직 한도가 있습니다. 초기화 시점과 확인 방법까지.", _BY["ko"], *_CTA_PL["ko"]),
 _cc("ja", "/ja/blog/chatgpt-shiyouryou-jougen", "chlim-ja", "ChatGPT の使用量上限まとめ：まだ制限があるものとリセットのタイミング",
     "2026年8月から通常のチャットは無制限。ただし GPT-6 Astra、Work、Codex、ファイル・画像には上限があります。リセット時期と確認方法も。", _BY["ja"], *_CTA_PL["ja"]),
]
CXLIM = [
 _cc("en", "/blog/codex-usage-limits", "cxlim-en", "Codex Usage Limits Explained: 5-Hour Window, Weekly Cap and Resets",
     "How Codex limits work on ChatGPT Plus and Pro, messages per 5 hours by model, how to check usage, and how to make it last longer.", _BY["en"], *_CTA_AG["en"]),
 _cc("ko", "/ko/blog/codex-sayongnyang-hando", "cxlim-ko", "Codex 사용량 한도 정리: 5시간·주간 한도와 초기화",
     "챗GPT Plus·Pro에서 Codex 한도가 어떻게 작동하는지, 모델별 5시간당 메시지 수, 사용량 확인법과 오래 쓰는 방법을 정리했습니다.", _BY["ko"], *_CTA_AG["ko"]),
 _cc("ja", "/ja/blog/codex-shiyouryou-jougen", "cxlim-ja", "Codex の使用量上限まとめ：5時間・週の上限とリセット",
     "ChatGPT Plus・Pro での Codex の上限の仕組み、モデル別の5時間あたりメッセージ数、使用量の確認方法と長持ちさせるコツ。", _BY["ja"], *_CTA_AG["ja"]),
]
CMAX = [
 _cc("en", "/blog/claude-max-vs-pro", "cmax-en", "Claude Max vs Pro: Is the $100 or $200 Plan Worth It?",
     "Claude Pro vs Max 5x vs Max 20x: price per unit of usage, how the limits work, and who should upgrade, with API cost comparisons.", _BY["en"], *_CTA_AG["en"]),
 _cc("ko", "/ko/blog/claude-max-vs-pro", "cmax-ko", "Claude Max vs Pro 비교: $100·$200 요금제, 올릴 가치가 있을까",
     "Claude Pro, Max 5×, Max 20×의 사용량당 가격, 한도 구조, 누가 올려야 하는지를 API 비용과 함께 비교했습니다.", _BY["ko"], *_CTA_AG["ko"]),
 _cc("ja", "/ja/blog/claude-max-vs-pro", "cmax-ja", "Claude Max vs Pro 比較：$100・$200プランにする価値はある？",
     "Claude Pro、Max 5×、Max 20× の使用量あたりの価格、上限の仕組み、誰がアップグレードすべきかを API 費用と合わせて比較。", _BY["ja"], *_CTA_AG["ja"]),
]

_CTA_AS = {"en": ("See what your AI use really costs: tokens, plans, images and video, all in one free tool.", "Open TokenSave"),
           "ko": ("AI를 쓰는 데 실제로 얼마가 드는지 확인하세요. 토큰, 구독, 이미지, 영상 비용을 무료로 계산합니다.", "토큰세이브 열기"),
           "ja": ("AIの利用に実際いくらかかるかを確認しましょう。トークン・サブスク・画像・動画の費用を無料で計算できます。", "TokenSave を開く")}
AISITE = [
 _cc("en", "/blog/useful-ai-websites", "aisite-en", "15 Useful AI Websites Worth Bookmarking (Free to Start)",
     "The AI websites actually worth a bookmark: chat, research, translation, design, voice, music, video and model comparison, all free to try.", _BY["en"], *_CTA_AS["en"]),
 _cc("ko", "/ko/blog/ai-site-chucheon", "aisite-ko", "유용한 AI 사이트 추천 15곳: 무료로 쓰는 꿀사이트 모음",
     "즐겨찾기할 만한 AI 사이트만 골랐습니다. 채팅, 검색, 번역, 디자인, 음성, 음악, 영상, 모델 비교까지 모두 무료로 시작할 수 있습니다.", _BY["ko"], *_CTA_AS["ko"]),
 _cc("ja", "/ja/blog/ai-site-osusume", "aisite-ja", "便利なAIサイトおすすめ15選：無料で始められるツールまとめ",
     "ブックマークする価値があるAIサイトだけを厳選。チャット、調べもの、翻訳、デザイン、音声、音楽、動画、モデル比較まで無料で試せます。", _BY["ja"], *_CTA_AS["ja"]),
]

_CTA_G4 = {"en": ("Paste a prompt to compare its cost on Gemini 4 Argon, GPT-6 and Claude.", "Open the token counter"),
           "ko": ("프롬프트를 붙여 넣고 Gemini 4 Argon·GPT-6·Claude의 비용을 비교해 보세요.", "토큰 계산기 열기"),
           "ja": ("プロンプトを貼り付けて、Gemini 4 Argon・GPT-6・Claude の費用を比べましょう。", "トークンカウンターを開く"),
           "es": ("Pega un prompt y compara su costo en Gemini 4 Argon, GPT-6 y Claude.", "Abrir el contador de tokens")}
def _g4(tag, path, title, desc, by):
    d = _cc(tag, path, "gem4-" + tag, title, desc, by, *_CTA_G4[tag]); d["date"] = "2026-10-03"; return d
GEM4 = [
 _g4("en", "/blog/gemini-4-argon-api-pricing", "Gemini 4 Argon API Pricing: Cost vs GPT-6 and Claude",
     "Gemini 4 Argon API prices ($2/$10 intro, $4/$20 standard), cost per request, availability, and how it compares with GPT-6 and Claude.",
     "Jonhisking · October 3, 2026"),
 _g4("ko", "/ko/blog/gemini-4-argon-api-gagyeok", "제미나이 4 아르곤 API 가격: GPT-6·Claude와 비용 비교",
     "Gemini 4 Argon의 API 가격(출시가 $2/$10, 정가 $4/$20), 요청당 실제 비용, 출시 일정, GPT-6·Claude와의 비교를 정리했습니다.",
     "Jonhisking · 2026년 10월 3일"),
 _g4("ja", "/ja/blog/gemini-4-argon-api-ryoukin", "Gemini 4 Argon の API 料金：GPT-6・Claude との費用比較",
     "Gemini 4 Argon の API 料金（導入価格 $2/$10、通常 $4/$20）、1リクエストあたりの費用、提供時期、GPT-6・Claude との比較。",
     "Jonhisking · 2026年10月3日"),
 _g4("es", "/es/blog/gemini-4-argon-precio-api", "Precio de Gemini 4 Argon: costo frente a GPT-6 y Claude",
     "Precios de la API de Gemini 4 Argon ($2/$10 de lanzamiento, $4/$20 estándar), costo por petición, disponibilidad y comparación con GPT-6 y Claude.",
     "Jonhisking · 3 de octubre de 2026"),
]

# Spanish versions (added 2026-10-03)
_BY["es"] = "Jonhisking · 3 de octubre de 2026"
_CTA["es"] = ("Indica el tamaño de las tareas y cuántas haces al día para comparar el costo de Claude Code por API con Pro y Max.", "Abrir la calculadora de agentes")
_CTA_AS["es"] = ("Descubre cuánto te cuesta de verdad usar IA: tokens, planes, imágenes y video en una sola herramienta gratis.", "Abrir TokenSave")
def _es(path, src, title, desc, cta):
    d = _cc("es", path, src, title, desc, _BY["es"], *cta); d["date"] = "2026-10-03"; return d
CC_COST.append(_es("/es/blog/claude-code-precio", "cc-cost-es", "Precio de Claude Code: ¿cuánto cuesta al mes? Pro vs Max vs API",
    "Cuánto cuesta Claude Code al mes con Pro, Max 5×, Max 20× o la API, el costo por tarea y cuándo conviene cada opción.", _CTA["es"]))
CC_LIMITS.append(_es("/es/blog/claude-code-limites-de-uso", "cc-limits-es", "Límites de uso de Claude Code: el límite de 5 horas y el semanal",
    "Cómo funcionan los límites de 5 horas y semanales de Claude Code en Pro y Max, qué cambió en 2026 y qué hacer al llegar al límite.", _CTA["es"]))
CXLIM.append(_es("/es/blog/codex-limites-de-uso", "cxlim-es", "Límites de uso de Codex en ChatGPT Plus, Pro y Business",
    "Cómo funcionan los límites de 5 horas y semanales de Codex, cuántas tareas da cada modelo y cómo sacarle más partido a tu plan.", _CTA["es"]))
CMAX.append(_es("/es/blog/claude-max-vs-pro", "cmax-es", "Claude Max vs Pro: ¿vale la pena el plan de $100 o $200?",
    "Claude Pro vs Max 5× vs Max 20×: precio por unidad de uso, cómo funcionan los límites y quién debería subir de plan.", _CTA["es"]))
AISITE.append(_es("/es/blog/paginas-de-ia-gratis", "aisite-es", "15 páginas de IA gratis que vale la pena guardar en favoritos",
    "Las mejores páginas de inteligencia artificial para chatear, investigar, traducir, diseñar, crear voz, música y video. Todas se pueden probar gratis.", _CTA_AS["es"]))

# Monthly "best value LLM" ranking posts (blog_src/rank-<tag>.md), data from /compare/performance
_CTA_RK = {"en": ("Paste a real prompt to see what it costs on Opus 5.5, Sonnet 5.5, Gemini 3.8 Flash and DeepSeek V4 Flash.", "Open the token counter"),
           "ko": ("내 프롬프트를 붙여 넣고 Opus 5.5·Sonnet 5.5·Gemini 3.8 Flash·DeepSeek V4 Flash에서 얼마인지 확인해 보세요.", "토큰 계산기 열기"),
           "ja": ("自分のプロンプトを貼り付けて、Opus 5.5・Sonnet 5.5・Gemini 3.8 Flash・DeepSeek V4 Flash でいくらかかるか確かめましょう。", "トークンカウンターを開く")}
def _rk(tag, path, title, desc, by):
    d = _cc(tag, path, "rank-" + tag, title, desc, by, *_CTA_RK[tag]); d["date"] = "2026-10-04"; return d
RANK = [
 _rk("en", "/blog/best-value-llm-october-2026", "Best Value LLM in October 2026: AI Capability vs Price",
     "23 AI models' capability scores against API prices: Opus 5.5 leads, Sonnet 5.5 is half the price, and DeepSeek V4 Flash costs 5%.",
     "Jonhisking · October 4, 2026"),
 _rk("ko", "/ko/blog/ai-gaseongbi-sunwi-2026-10", "2026년 10월 AI 가성비 순위: 성능 vs 가격으로 본 LLM",
     "AI 모델 23개의 성능 점수와 API 가격 비교. 1위 Opus 5.5, 절반 가격의 Sonnet 5.5, 5% 가격의 DeepSeek V4 Flash까지 정리했습니다.",
     "Jonhisking · 2026년 10월 4일"),
 _rk("ja", "/ja/blog/ai-cospa-ranking-2026-10", "2026年10月 AIコスパランキング：性能と価格で比べるLLM",
     "AIモデル23種の性能スコアとAPI料金を比較。1位の Opus 5.5、半額の Sonnet 5.5、5%の料金の DeepSeek V4 Flash まで。",
     "Jonhisking · 2026年10月4日"),
]

# AI game development cost (blog_src/game-<tag>.md), CTA -> /ai-game-cost-calculator
_CTA_GM = {"en": ("Pick a genre, size, engine and platform to get your own cost, schedule and ready-to-use prompts.", "Open the AI game cost calculator"),
           "ko": ("장르·규모·엔진·플랫폼을 고르면 내 게임의 비용과 기간, 바로 쓸 수 있는 프롬프트가 나옵니다.", "AI 게임 제작 비용 계산기 열기"),
           "ja": ("ジャンル・規模・エンジン・プラットフォームを選ぶと、自分のゲームの費用と期間、すぐ使えるプロンプトが出ます。", "AIゲーム制作費計算機を開く")}
def _gm(tag, path, title, desc, by):
    d = _cc(tag, path, "game-" + tag, title, desc, by, *_CTA_GM[tag]); d["date"] = "2026-10-05"; return d
GAME = [
 _gm("en", "/blog/ai-game-development-cost", "How Much Does It Cost to Make a Game with AI? (2026)",
     "Making a 2D game solo with AI: about $130–180 and 2–3 weeks for a small mobile game. Cost by size and genre, where the money goes, and tools.",
     "Jonhisking · October 5, 2026"),
 _gm("ko", "/ko/blog/ai-game-jejakbi", "AI로 게임 만들기 비용 얼마? 2026년 2D 게임 제작비 정리",
     "AI로 혼자 2D 게임을 만들면 소형 모바일 게임 기준 약 $130~180, 2~3주. 규모·장르별 비용, 돈이 나가는 곳, 게임용 AI 도구까지 정리했습니다.",
     "Jonhisking · 2026년 10월 5일"),
 _gm("ja", "/ja/blog/ai-game-seisakuhi", "AIでゲームを作る費用はいくら？2026年版 2Dゲーム制作費の目安",
     "AIで1人で2Dゲームを作ると、小規模モバイルゲームで約$130〜180、2〜3週間。規模・ジャンル別の費用、内訳、ゲーム向けAIツールまで。",
     "Jonhisking · 2026年10月5日"),
]

# Japanese how-to (targets 「ゲーム 作り方」 + AI), CTA -> /ja/ai-game-cost-calculator
GAME_HOWTO = [
 _gm("ja", "/ja/blog/ai-game-tsukurikata", "AIでスマホゲームを作る方法：手順・ツール・費用【2026年】",
     "AIでスマホゲームを1人で作る6つの手順と必要なツール、ジャンル別の費用と期間（小規模で約$50〜180・2〜3週間）をまとめました。",
     "Jonhisking · 2026年10月5日"),
]
GAME_HOWTO[0]["src"] = "game-howto-ja"

DEVLOG1 = [
 _gm("en", "/blog/vibe-coding-a-game-beginner", "A Beginner Vibe-Codes a Game — Zero Coding, 3 Days, $45",
     "No coding experience, no idea what a game engine was. How I vibe-coded a sperm racing game with Claude in 3 days and launched it for $45.",
     "Jonhisking · October 5, 2026"),
 _gm("ko", "/ko/blog/vibe-coding-game-mandeulgi", "초보자가 바이브 코딩으로 게임 만들기 — 코딩 0, 3일, $45",
     "코딩 경험도, 게임 엔진 개념도 없던 초보자가 Claude에게 말로만 설명해 3일 만에 정자 레이싱 게임을 만들고 $45로 출시한 개발 일지입니다.",
     "Jonhisking · 2026년 10월 5일"),
 _gm("ja", "/ja/blog/vibe-coding-game-shoshinsha", "初心者がバイブコーディングでゲームを作ってみた — コード経験ゼロ、3日、$45",
     "プログラミング経験ゼロ、ゲームエンジンも知らなかった初心者が、Claude に言葉で説明するだけで3日でゲームを作り、$45でリリースした開発日誌です。",
     "Jonhisking · 2026年10月5日"),
]
for _d, _l in zip(DEVLOG1, ["en", "ko", "ja"]):
    _d["src"] = "devlog-spermrace-1-" + _l
    _d["og"] = "blog-spermrace-feature.jpg" if _l == "ko" else f"blog-spermrace-feature-{_l}.jpg"

DEVLOG2 = [
 _gm("en", "/blog/google-play-closed-testing-14-days", "Google Play Closed Testing: 14 Bugs I Fixed in 14 Days (Vibe-Coded Game)",
     "Google Play's 14-day closed test with 12+ testers, used to fix 14 bugs in a game I vibe-coded with AI. Reproduced in the real game, plus a checklist.",
     "Jonhisking · October 6, 2026"),
 _gm("ko", "/ko/blog/google-play-bigonggae-teseuteu-14il", "구글 플레이 비공개 테스트 14일, AI로 만든 게임 버그 14개 잡은 기록",
     "구글 플레이 비공개 테스트(12명·14일) 동안 바이브 코딩으로 만든 게임의 버그 14개를 잡은 기록. 실제 재현 화면과 AI에게 버그를 설명하는 법까지 정리했습니다.",
     "Jonhisking · 2026년 10월 6일"),
 _gm("ja", "/ja/blog/google-play-closed-test-14nichi", "Google Play クローズドテスト14日間で、AIで作ったゲームのバグ14個を直した記録",
     "Google Play のクローズドテスト(12人・14日)の間に、バイブコーディングで作ったゲームのバグ14個を直した記録。実際の再現画面とAIへのバグの伝え方も。",
     "Jonhisking · 2026年10月6日"),
]
for _d, _l in zip(DEVLOG2, ["en", "ko", "ja"]):
    _d["src"] = "devlog-spermrace-2-" + _l
    _d["date"] = "2026-10-06"
    _d["og"] = "blog-spermrace-2-hero.jpg" if _l == "ko" else f"blog-spermrace-2-hero-{_l}.jpg"


_BY6 = "Jonhisking · October 6, 2026"
def _n6(path, src, title, desc, cta, btn):
    return dict(tag="en", path=path, src=src, title=title, desc=desc, byline=_BY6, cta=cta, ctaBtn=btn, date="2026-10-06")
CHEAP = [_n6("/blog/cheapest-llm-api", "cheapest-en", "The Cheapest LLM APIs in 2026, Ranked by Real Cost per Request",
    "Every major LLM API ranked by what a typical request costs, after tokenizer differences: GPT-5 nano, GPT-6 Luna, Qwen, Gemini Flash-Lite, DeepSeek and more.",
    *_CTA_TK["en"])]
CTOK = [_n6("/blog/claude-pro-max-how-many-tokens", "ctok-en", "How Many Tokens Do You Get with Claude Pro and Max?",
    "Anthropic doesn't publish token limits. Measured numbers for Claude Pro, Max 5x and Max 20x per 5-hour window and per week, and what they mean in API dollars.",
    *_CTA["en"])]
SUBS = [_n6("/blog/ai-subscription-price-comparison", "subs-en", "AI Subscription Price Comparison: ChatGPT vs Claude vs Gemini vs Grok (2026)",
    "Every ChatGPT, Claude, Google AI and Grok plan side by side, from $4.99 to $500 a month: price, usage per tier, limits, and when the API is cheaper.",
    *_CTA_PL["en"])]
GPT61 = [_n6("/blog/gpt-6-1-sol-api-pricing", "gpt61-en", "GPT-6.1 Sol API Pricing: Cost vs GPT-6 Sol, Claude Opus 5.5 and Sonnet 5.5",
    "GPT-6.1 Sol is $2 / $10 per million tokens with cached input cut to $0.10. Real costs, what improved, and how it compares with Claude Opus and Sonnet 5.5.",
    *_CTA_TK["en"])]
DS41 = [_n6("/blog/deepseek-v4-1-flash-api-pricing", "ds41-en", "DeepSeek V4.1 Flash API Pricing: Peak vs Off-Peak, and How It Compares",
    "DeepSeek V4.1 Flash is $0.15 / $0.60 per million tokens off-peak, $0.003 cached. Peak hours in your time zone and how it compares with GPT-6 Luna and Gemini.",
    *_CTA_TK["en"])]
AGCMP = [_n6("/blog/claude-code-vs-codex-vs-cursor-cost", "agentcmp-en", "Claude Code vs Codex vs Cursor: What Each Costs in 2026",
    "Claude Code, Codex and Cursor plans from $20 to $500 compared: usage limits vs a dollar budget, what $200 buys on each, and which is cheapest for how you code.",
    *_CTA["en"])]
GOPLUS = [_n6("/blog/chatgpt-go-vs-plus", "gogo-en", "ChatGPT Go vs Plus: Is the $20 Plan Worth $12 More?",
    "ChatGPT Go ($8) vs Plus ($20) in 2026: Luna vs Sol, thinking levels, Codex, ads and limits, who needs which, and when the API is cheaper than both.",
    *_CTA_PL["en"])]
RBX = [_n6("/blog/roblox-trending-games", "rbxtrend-en", "What's Trending on Roblox Right Now (October 2026): 8 Game Types",
    "The 8 game formulas climbing the Roblox charts in October 2026, with real examples and player counts, why each works, and what it takes to build one with AI.",
    *_CTA_GM["en"]),
       _n6("/blog/how-to-make-a-roblox-game-with-ai", "rbxhow-en", "How to Make a Roblox Game with AI (2026): Steps, Tools, Cost",
    "Make a Roblox game with Roblox Assistant, Cube 3D models and Claude Code: the steps from idea to publishing, what it costs, and how DevEx pays you.",
    *_CTA_GM["en"])]
_BY6K = "Jonhisking · 2026년 10월 6일"
def _k6(path, src, title, desc, cta, btn):
    d = _cc("ko", path, src, title, desc, _BY6K, cta, btn); d["date"] = "2026-10-06"; return d
KO6 = [
 _k6("/ko/blog/gemini-yogeumje-gaepyeon", "gemgp-ko", "제미나이 요금제 개편 정리: 10월 9일부터 무료는 Flash-Lite만",
     "10월 9일부터 제미나이 무료는 Flash-Lite만, AI Plus(7,500원)도 Pro 모델을 못 씁니다. 요금제별 원화 가격과 쓸 수 있는 모델, 어떻게 하면 좋은지 정리했습니다.",
     *_CTA_PL["ko"]),
 _k6("/ko/blog/ai-gudokryo-bigyo", "subs-ko", "AI 구독료 원화 비교: 챗GPT·클로드·제미나이·그록 (2026)",
     "챗GPT·클로드·제미나이·그록 유료 요금제를 한국에서 실제로 내는 원화 금액으로 비교했습니다. 7,500원부터 30만 원까지, 누구에게 어떤 요금제가 맞는지.",
     *_CTA_PL["ko"]),
 _k6("/ko/blog/chatgpt-go-vs-plus", "gogo-ko", "챗GPT Go vs Plus: 13,000원과 29,000원, 무엇이 다를까",
     "챗GPT Go(13,000원)와 Plus(29,000원) 비교: Luna와 Sol 모델 차이, 추론 단계, Codex, 광고, 누구에게 어느 쪽이 맞는지, API가 더 싼 경우까지.",
     *_CTA_PL["ko"]),
]
_BY6J = "Jonhisking · 2026年10月6日"
def _j6(path, src, title, desc, cta, btn):
    d = _cc("ja", path, src, title, desc, _BY6J, cta, btn); d["date"] = "2026-10-06"; return d
JA6 = [
 _j6("/ja/blog/gemini-muryou-flash-lite", "gemgp-ja", "Gemini無料版は10月9日からFlash-Liteのみに：プラン別の変更と料金",
     "10月9日からGemini無料版はFlash-Liteのみ、AI Plus（725円）もProが使えなくなります。プラン別の日本円の料金と、APIでPro級を安く使う方法まで。",
     *_CTA_PL["ja"]),
 _j6("/ja/blog/ai-subscription-ryoukin-hikaku", "subs-ja", "生成AIのサブスク料金比較：ChatGPT・Claude・Gemini・Grok【日本円】",
     "ChatGPT・Claude・Gemini・Grokの有料プランを、日本で実際に払う金額（税込）で比較。725円から3万円台まで、誰にどのプランが向いているか。",
     *_CTA_PL["ja"]),
 _j6("/ja/blog/chatgpt-go-vs-plus", "gogo-ja", "ChatGPT GoとPlusの違い：1,400円と3,000円で何が変わる？",
     "ChatGPT Go（1,400円）とPlus（3,000円）の違い：LunaとSolのモデル差、推論レベル、Codex、広告、どちらが向いているか、APIのほうが安いケースまで。",
     *_CTA_PL["ja"]),
]
RBX_JA = [_j6("/ja/blog/roblox-game-tsukurikata", "rbx-ja", "AIでRobloxゲームを作る方法：手順・費用・今伸びているジャンル【2026年】",
     "Roblox AssistantとAIでロブロックスのゲームを作る6つの手順、今チャートで伸びている8ジャンル、費用（約4,000円〜）、DevExでの収益化まで。",
     *_CTA_GM["ja"])]
_CTA_PL_TW = ("輸入你的使用方式，看每月 API 費用和 ChatGPT・Claude・Gemini 各方案並排比較。", "開啟訂閱 vs API 計算機")
_BY6T = "Jonhisking · 2026年10月6日"
def _t6(path, src, title, desc):
    d = _cc("zh-TW", path, src, title, desc, _BY6T, *_CTA_PL_TW); d["date"] = "2026-10-06"; return d
TW6 = [
 _t6("/zh-tw/blog/gemini-mianfei-flash-lite", "gemgp-zhtw", "Gemini 免費版 10/9 起只剩 Flash-Lite：各方案變動與價格",
     "10 月 9 日起 Gemini 免費版只能用 Flash-Lite，AI Plus（NT$260）也不能再用 Pro。各方案價格、可用模型，以及用 API 便宜用到 Pro 級的方法。"),
 _t6("/zh-tw/blog/ai-dingyue-jiage-bijiao", "subs-zhtw", "AI 訂閱價格比較：ChatGPT・Claude・Gemini・Grok（台灣 2026）",
     "ChatGPT、Claude、Gemini、Grok 付費方案的台灣實際價格一次比較：從 NT$260 到 US$300，誰適合哪個方案，香港用戶注意事項。"),
 _t6("/zh-tw/blog/chatgpt-go-vs-plus", "gogo-zhtw", "ChatGPT Go 與 Plus 差在哪？NT$270 和 NT$690 怎麼選",
     "ChatGPT Go（NT$270）與 Plus（NT$690）比較：台灣開始出現廣告、Luna 與 Sol 模型差異、推理等級、Codex，以及什麼情況用 API 更便宜。"),
]

# 2026-10-06: Gemini change / subscription prices / Go vs Plus in fr, es, pt, uk, de, pl
_EU6 = {
 "fr": ("Jonhisking · 6 octobre 2026", "Abonnement ou API : entrez votre usage réel et voyez ce qui vous coûte le moins cher, tokens français compris.", "Comparer abonnement et API", [
   ("/fr/blog/gemini-gratuit-flash-lite", "gemgp-fr", "Gemini gratuit limité à Flash-Lite le 9 octobre : que faire ?",
    "Dès le 9 octobre 2026, Gemini gratuit passe à Flash-Lite et AI Plus perd le modèle Pro. Prix en euros, offre étudiante et alternative API."),
   ("/fr/blog/abonnement-ia-prix-comparatif", "subs-fr", "Abonnements IA 2026 : ChatGPT, Claude, Gemini, Mistral en euros TTC",
    "Tous les prix des abonnements IA en France, TTC : ChatGPT, Claude, Gemini, Mistral Vibe, Grok. Prix par unité et abonnement ou API."),
   ("/fr/blog/chatgpt-go-vs-plus", "gogo-fr", "ChatGPT Go ou Plus : 8 € ou 23 €, lequel choisir ?",
    "ChatGPT Go (8 €) affiche de la publicité et utilise GPT-5.6 Luna ; Plus (23 €) passe à Sol, sans pub. Différences et pour qui.")]),
 "es": ("Jonhisking · 6 de octubre de 2026", "¿Te sale más barato pagar una suscripción o usar la API? Introduce cuánto usas la IA y compáralo con todos los planes.", "Calcular suscripción vs API", [
   ("/es/blog/gemini-gratis-flash-lite", "gemgp-es", "Gemini gratis pasa a Flash-Lite el 9 de octubre: qué cambia y precios",
    "Desde el 9 de octubre Gemini gratis solo usa Flash-Lite y AI Plus pierde Pro. Planes en euros y pesos, y cuánto cuesta Gemini Pro por API."),
   ("/es/blog/precio-suscripciones-ia", "subs-es", "Precio de ChatGPT, Claude, Gemini y Grok en euros y pesos (2026)",
    "Todos los planes de IA de pago en euros y pesos: ChatGPT, Claude, Google AI y Grok, precio por unidad de uso e impuestos en Argentina."),
   ("/es/blog/chatgpt-go-vs-plus", "gogo-es", "ChatGPT Go vs Plus: diferencias, precio en euros y pesos, y anuncios",
    "ChatGPT Go o Plus: modelo Luna o Sol, razonamiento, Codex y anuncios. Precios en España, México y Colombia, y cuándo sale más barata la API.")]),
 "pt": ("Jonhisking · 6 de outubro de 2026", "Quer saber se compensa assinar ou pagar só pelo que usa? Informe seu uso e compare o custo da API, em reais, com cada plano.", "Calcular assinatura vs API", [
   ("/pt/blog/gemini-gratis-flash-lite", "gemgp-pt", "Gemini grátis só com Flash-Lite a partir de 9/10: o que muda",
    "Gemini grátis fica só com o Flash-Lite e o AI Plus perde o Pro. Preços em reais (R$ 24,99 a R$ 779,90) e quanto custa o Pro pela API."),
   ("/pt/blog/preco-assinaturas-ia", "subs-pt", "Preço do ChatGPT, Claude, Gemini e Grok em reais (com IOF)",
    "Todos os planos de IA em reais: ChatGPT Go R$ 39,99, Plus R$ 99,90, Google AI Pro R$ 96,99, Claude Pro. Quem paga IOF e qual plano compensa."),
   ("/pt/blog/chatgpt-go-vs-plus", "gogo-pt", "ChatGPT Go vs Plus: diferença, preço em reais e anúncios",
    "ChatGPT Go (R$ 39,99) ou Plus (R$ 99,90)? Luna vs Sol, anúncios no Go no Brasil, Codex e quando a API sai mais barata. Comparativo de 2026.")]),
 "uk": ("Jonhisking · 6 жовтня 2026", "Порівняйте свою підписку з оплатою за токени: введіть, скільки ви користуєтеся ШІ, і побачите ціну API поруч із кожним тарифом.", "Порахувати: підписка чи API", [
   ("/uk/blog/gemini-bezkoshtovno-flash-lite", "gemgp-uk", "Gemini безкоштовно: з 9 жовтня лише Flash-Lite. Що робити",
    "З 9 жовтня безкоштовний Gemini — лише Flash-Lite, AI Plus втрачає Pro. Ціни в гривнях, що робити студентам і скільки коштує Pro через API."),
   ("/uk/blog/tsiny-pidpysok-shi", "subs-uk", "Ціни підписок на ШІ в Україні: ChatGPT, Claude, Gemini, Grok",
    "Скільки реально коштують ChatGPT, Claude, Gemini і Grok в Україні з 20% ПДВ: таблиця в гривнях, ціна за одиницю і чи потрібна підписка."),
   ("/uk/blog/chatgpt-go-vs-plus", "gogo-uk", "ChatGPT Go чи Plus: різниця і ціна в Україні з ПДВ",
    "ChatGPT Go за $8,40 чи Plus за $24 з ПДВ: Luna проти Sol, Codex, реклама і коли дешевше API. Порівняння для України.")]),
 "de": ("Jonhisking · 6. Oktober 2026", "Trag ein, wie oft du KI nutzt, und sieh sofort, ob ein Abo oder die API für dich günstiger ist.", "Abo vs. API berechnen", [
   ("/de/blog/gemini-kostenlos-flash-lite", "gemgp-de", "Gemini kostenlos nur noch mit Flash-Lite: Was sich ab 9. Oktober ändert",
    "Ab 9. Oktober 2026 gibt es Gemini gratis nur noch mit Flash-Lite, AI Plus verliert Pro. Alle Tarife in Euro und die günstige API-Alternative."),
   ("/de/blog/ki-abo-preisvergleich", "subs-de", "KI-Abos im Preisvergleich 2026: ChatGPT, Claude, Gemini in Euro",
    "Alle KI-Abos von ChatGPT, Claude, Gemini und Grok mit Preisen inkl. MwSt, Preis pro Einheit bei Max und Ultra und wann die API günstiger ist."),
   ("/de/blog/chatgpt-go-vs-plus", "gogo-de", "ChatGPT Go vs. Plus: Lohnen sich 15 € mehr im Monat?",
    "ChatGPT Go für 7,99 € oder Plus für 22,99 €: Luna gegen Sol, Werbung seit August und für wen sich welcher Tarif lohnt. Plus die API-Alternative.")]),
 "pl": ("Jonhisking · 6 października 2026", "Sprawdź, czy przy Twoim sposobie korzystania taniej wychodzi abonament, czy płacenie za tokeny — w złotówkach i na polskich tokenach.", "Porównaj subskrypcję i API", [
   ("/pl/blog/gemini-za-darmo-flash-lite", "gemgp-pl", "Gemini za darmo od 9 października: tylko Flash-Lite. Co dalej?",
    "Od 9.10 darmowe Gemini ma tylko Flash-Lite, a AI Plus traci model Pro. Ceny planów w zł, oferta dla studentów i tańszy Pro przez API."),
   ("/pl/blog/ceny-subskrypcji-ai", "subs-pl", "Ceny subskrypcji AI w Polsce: ChatGPT, Claude, Gemini, Grok w zł",
    "Wszystkie plany ChatGPT, Claude, Gemini i Grok w złotówkach z VAT, cena za jednostkę limitu, faktura na firmę i kiedy taniej wychodzi API."),
   ("/pl/blog/chatgpt-go-vs-plus", "gogo-pl", "ChatGPT Go czy Plus: co daje 65 zł więcej (i brak reklam)",
    "ChatGPT Go za 34,99 zł czy Plus za 99,99 zł? Luna kontra Sol, reklamy od sierpnia, Codex i kiedy taniej wyjdzie API po polsku.")]),
}
EU6 = []
for _tag, (_by, _cta, _btn, _items) in _EU6.items():
    for _p, _src, _ti, _de in _items:
        _d = _cc(_tag, _p, _src, _ti, _de, _by, _cta, _btn); _d["date"] = "2026-10-06"; EU6.append([_d])


# Polish localizations (2026-10-06)
PRO.append(dict(tag="pl", path='/pl/blog/chatgpt-pro-100-200-500', src='pro-pl', title='ChatGPT Pro cena: Pro 100, 200 czy 500 – który plan i czy warto?', desc='ChatGPT Pro 100, 200 i 500 kosztują tyle samo za jednostkę limitu. Co zmieniło się 29 września 2026, który plan wybrać i kiedy API wychodzi taniej.', byline='Jonhisking · 6 października 2026', cta='Sprawdź, czy przy Twoim sposobie korzystania taniej wychodzi abonament, czy płacenie za tokeny — w złotówkach i na polskich tokenach.', ctaBtn='Porównaj subskrypcję i API', date="2026-10-06"))
CHEAP.append(dict(tag="pl", path='/pl/blog/najtansze-api-ai', src='cheapest-pl', title='Najtańsze API AI 2026: cennik API i koszt 1 mln tokenów', desc='Najtańsze API AI w październiku 2026: GPT-5 nano, GPT-6 Luna, Qwen 3.8 Flash. Cennik API, koszt 1 mln tokenów i 10 000 zapytań dla 11 modeli.', byline='Jonhisking · 6 października 2026', cta='Wklej swój prompt i zobacz, ile tokenów zużywa i ile kosztuje w każdym modelu — także po polsku.', ctaBtn='Otwórz licznik tokenów', date="2026-10-06"))
CTOK.append(dict(tag="pl", path='/pl/blog/limity-claude-pro-max', src='ctok-pl', title='Limit Claude: ile tokenów daje Claude Pro i Max? (pomiary)', desc='Claude Pro limity i ile tokenów Claude Max: ok. 39 mln na 5 godzin w Max 5×, ok. 1,9 mld tygodniowo w Max 20×. Skąd te liczby i co szybciej zużywa limit.', byline='Jonhisking · 6 października 2026', cta='Wpisz, jak korzystasz z Claude Code i Codex, i porównaj miesięczny koszt API z planami Pro i Max.', ctaBtn='Otwórz kalkulator agentów AI', date="2026-10-06"))
CC_LIMITS.append(dict(tag="pl", path='/pl/blog/limity-claude-code', src='cc-limits-pl', title='Claude Code limity: limit 5 godzin i limit tygodniowy (2026)', desc='Claude Code limity w 2026: jak działa limit 5 godzin i limit tygodniowy, ile daje Pro i Max, co zmieniło się we wrześniu i co zrobić przy limicie.', byline='Jonhisking · 6 października 2026', cta='Wpisz, jak korzystasz z Claude Code i Codex, i porównaj miesięczny koszt API z planami Pro i Max.', ctaBtn='Otwórz kalkulator agentów AI', date="2026-10-06"))
CXLIM.append(dict(tag="pl", path='/pl/blog/limity-codex', src='cxlim-pl', title='Codex limity: okno 5 godzin, limit tygodniowy i Codex limit Plus', desc='Codex limity w 2026: okno 5-godzinne, limit tygodniowy, ile wiadomości daje Plus i Pro dla każdego modelu GPT i co zrobić, gdy limit się skończy.', byline='Jonhisking · 6 października 2026', cta='Wpisz, jak korzystasz z Claude Code i Codex, i porównaj miesięczny koszt API z planami Pro i Max.', ctaBtn='Otwórz kalkulator agentów AI', date="2026-10-06"))
DEVLOG2.append(dict(tag="pl", path='/pl/blog/testy-zamkniete-google-play-14-dni', src='devlog-spermrace-2-pl', title='Testy zamknięte Google Play: 12 testerów, 14 dni i 14 błędów', desc='Testy zamknięte Google Play z 12 testerami przez 14 dni: jak vibe coding gra Sperm Race przeszła test, 14 naprawionych błędów i lista kontrolna.', byline='Jonhisking · 6 października 2026', cta='Wybierz gatunek, rozmiar, silnik i platformę, a dostaniesz koszt, czas i gotowe prompty dla swojej gry.', ctaBtn='Otwórz kalkulator kosztu gry z AI', date="2026-10-06", og="blog-spermrace-2-hero-en.jpg"))

# Polish game articles (2026-10-06)
GAME.append(dict(tag="pl", path='/pl/blog/ile-kosztuje-gra-z-ai', src='game-pl', title='Ile kosztuje stworzenie gry z AI? Koszt gry mobilnej w 2026', desc='Ile kosztuje stworzenie gry z AI: mała gra mobilna to ok. 128–181 USD i 2–3 tygodnie. Koszt według rozmiaru, gatunku i narzędzi – gra bez programowania.', byline='Jonhisking · 6 października 2026', cta='Wybierz gatunek, rozmiar, silnik i platformę, a dostaniesz koszt, czas i gotowe prompty dla swojej gry.', ctaBtn='Otwórz kalkulator kosztu gry z AI', date="2026-10-06"))
DEVLOG1.append(dict(tag="pl", path='/pl/blog/vibe-coding-gra', src='devlog-spermrace-1-pl', title='Vibe coding gra: zrobiłem grę z AI w 3 dni za 45 USD', desc='Vibe coding gra Sperm Race: jak zrobić grę bez programowania w 3 dni za 45 USD. Pierwsze prompty, grafika i dźwięk w kodzie, Claude Pro i Google Play.', byline='Jonhisking · 6 października 2026', cta='Wybierz gatunek, rozmiar, silnik i platformę, a dostaniesz koszt, czas i gotowe prompty dla swojej gry.', ctaBtn='Otwórz kalkulator kosztu gry z AI', date="2026-10-06", og="blog-spermrace-feature-en.jpg"))
RBX_PL = [[dict(tag="pl", path='/pl/blog/popularne-gry-roblox', src='rbxtrend-pl', title='Popularne gry Roblox: najpopularniejsze gry Roblox 2026', desc='Jakie gry są teraz popularne w Roblox? 8 formuł z rankingów z 6 października 2026, liczby graczy, czas budowy z AI i koszt od ok. 25–40 USD.', byline='Jonhisking · 6 października 2026', cta='Wybierz gatunek, rozmiar, silnik i platformę, a dostaniesz koszt, czas i gotowe prompty dla swojej gry.', ctaBtn='Otwórz kalkulator kosztu gry z AI', date="2026-10-06")], [dict(tag="pl", path='/pl/blog/gra-roblox-z-ai', src='rbxhow-pl', title='Jak zrobić grę w Roblox z AI: Roblox Studio AI krok po kroku', desc='Jak zrobić grę w Roblox bez kodowania: Roblox Assistant, /generate_mesh, Luau, koszt narzędzi AI i jak zarabiać na Roblox przez DevEx (0,0038 USD/Robux).', byline='Jonhisking · 6 października 2026', cta='Wybierz gatunek, rozmiar, silnik i platformę, a dostaniesz koszt, czas i gotowe prompty dla swojej gry.', ctaBtn='Otwórz kalkulator kosztu gry z AI', date="2026-10-06")]]


# Dutch localizations (2026-10-06)
PRO.append(dict(tag="nl", path='/nl/blog/chatgpt-pro-100-200-500', src='pro-nl', title='ChatGPT Pro prijs: Pro 100, 200 en 500 vergeleken (2026)', desc='ChatGPT Pro 100, 200 en 500: wat kost elk abonnement, wat veranderde op 29 september en is ChatGPT Pro het waard? Plus: wanneer de API goedkoper is.', byline='Jonhisking · 6 oktober 2026', cta='Vul in hoe je AI gebruikt en zie of een abonnement of de API goedkoper is, met Nederlandse tokens meegerekend.', ctaBtn='Abonnement vs API berekenen', date="2026-10-06"))
CHEAP.append(dict(tag="nl", path='/nl/blog/goedkoopste-ai-api', src='cheapest-nl', title='Goedkoopste AI API 2026: API-prijzen vergelijken per 1 miljoen tokens', desc='Goedkoopste AI API in oktober 2026: GPT-5 nano, GPT-6 Luna en Qwen 3.8 Flash. Kosten per 1 miljoen tokens en per verzoek, plus de Nederlandse tokentoeslag.', byline='Jonhisking · 6 oktober 2026', cta='Plak je tekst en zie hoeveel tokens hij gebruikt en wat dat kost in GPT, Claude en Gemini.', ctaBtn='Tokenteller openen', date="2026-10-06"))
CTOK.append(dict(tag="nl", path='/nl/blog/claude-limiet', src='ctok-nl', title='Claude limiet: hoeveel tokens geven Claude Pro en Claude Max?', desc="Claude limiet in tokens: Max 5x geeft zo'n 39 miljoen tokens per 5 uur, Max 20x zo'n 1,9 miljard per week. Pro-schatting, prijzen in euro en API-kosten.", byline='Jonhisking · 6 oktober 2026', cta='Vul in hoe je Claude Code en Codex gebruikt en zie de maandkosten via de API naast elk abonnement.', ctaBtn='Open de calculator voor coding agents', date="2026-10-06"))
CC_LIMITS.append(dict(tag="nl", path='/nl/blog/claude-code-limiet', src='cc-limits-nl', title='Claude Code limiet: de 5 uur limiet en de weeklimiet uitgelegd', desc='Claude Code limiet uitgelegd: hoe de 5 uur limiet en de weeklimiet werken, wat er in 2026 veranderde en wat je doet als je tegen een limiet aanloopt.', byline='Jonhisking · 6 oktober 2026', cta='Vul in hoe je Claude Code en Codex gebruikt en zie de maandkosten via de API naast elk abonnement.', ctaBtn='Open de calculator voor coding agents', date="2026-10-06"))
CXLIM.append(dict(tag="nl", path='/nl/blog/codex-limiet', src='cxlim-nl', title='Codex limiet: hoeveel geeft Codex in ChatGPT Plus en Pro?', desc='Codex limiet in Plus en Pro: het 5-uursvenster, de weeklimiet en berichten per model, van GPT-6 Astra tot GPT-5.6 Luna. Plus tips om langer door te werken.', byline='Jonhisking · 6 oktober 2026', cta='Vul in hoe je Claude Code en Codex gebruikt en zie de maandkosten via de API naast elk abonnement.', ctaBtn='Open de calculator voor coding agents', date="2026-10-06"))
GAME.append(dict(tag="nl", path='/nl/blog/wat-kost-een-game-maken-met-ai', src='game-nl', title='Game maken met AI: wat kost een game maken? ($128–181)', desc='Wat kost een game maken met AI? Een kleine mobiele game kost $128–181 en 14–22 dagen, ook zonder programmeren. Kosten per grootte, genre en toolset.', byline='Jonhisking · 6 oktober 2026', cta='Kies genre, grootte, engine en platform en krijg kosten, tijd en kant-en-klare prompts voor je game.', ctaBtn='Open de AI-gamekostencalculator', date="2026-10-06"))
NL6 = [[dict(tag="nl", path='/nl/blog/gemini-gratis-flash-lite', src='gemgp-nl', title='Gemini gratis: vanaf 9 oktober alleen Flash-Lite, AI Plus zonder Pro', desc='Gemini gratis krijgt vanaf 9 oktober 2026 alleen Flash-Lite. Google AI Plus verliest Pro. Prijzen in euro, Google AI Pro prijs en goedkoper via de API.', byline='Jonhisking · 6 oktober 2026', cta='Vul in hoe je AI gebruikt en zie of een abonnement of de API goedkoper is, met Nederlandse tokens meegerekend.', ctaBtn='Abonnement vs API berekenen', date="2026-10-06")], [dict(tag="nl", path='/nl/blog/ai-abonnement-prijzen', src='subs-nl', title='ChatGPT, Claude en Gemini prijzen in euro (incl. 21% btw)', desc='Wat kost ChatGPT, Claude Pro en een Gemini abonnement? Alle AI-abonnementen in euro incl. 21% btw (NL & BE), plus wanneer de API goedkoper is.', byline='Jonhisking · 6 oktober 2026', cta='Vul in hoe je AI gebruikt en zie of een abonnement of de API goedkoper is, met Nederlandse tokens meegerekend.', ctaBtn='Abonnement vs API berekenen', date="2026-10-06")], [dict(tag="nl", path='/nl/blog/chatgpt-go-vs-plus', src='gogo-nl', title='ChatGPT Go vs Plus: €8 of €23, welk abonnement past bij jou?', desc='ChatGPT Go vs Plus: Luna of Sol, denkstanden, Codex en advertenties. ChatGPT Plus prijs €23, Go €8 met reclame. Voor wie welk abonnement loont.', byline='Jonhisking · 6 oktober 2026', cta='Vul in hoe je AI gebruikt en zie of een abonnement of de API goedkoper is, met Nederlandse tokens meegerekend.', ctaBtn='Abonnement vs API berekenen', date="2026-10-06")]]

GCREV = [_gm("en", "/blog/ai-game-cost-calculator-review", "I Ran My Released Game Through My AI Game Cost Calculator: Prediction vs Reality",
     "I fed my shipped Google Play game into my own AI game cost calculator. Predicted $47–102 and 19–31 days; actual $45 and 17 days. What it got right and wrong.",
     "Jonhisking · October 8, 2026")]
GCREV[0].update(src="gamecalc-review-en", date="2026-10-08", og="gamecalc-spermrace-en.jpg")

# 2026-10-08: ChatGPT free vs paid (ko, en, ja, uk, zh-CN, fr, de)
_FPCTA = {"uk": _EU6["uk"][1:3], "fr": _EU6["fr"][1:3], "de": _EU6["de"][1:3],
          "zh-CN": ("输入你的使用方式，看每月 API 费用和 ChatGPT・Claude・Gemini 各套餐并排比较。", "打开订阅 vs API 计算器")}
def _fpd(tag, path, src, title, desc, by, img):
    cta = _CTA_PL[tag] if tag in _CTA_PL else _FPCTA[tag]
    d = _cc(tag, path, src, title, desc, by, *cta); d.update(date="2026-10-08", og=img); return d
FREEPAID = [
 _fpd("ko", "/ko/blog/chatgpt-muryo-yuryo-chai", "freepaid-ko", "챗GPT 무료 vs 유료 차이: 무료·Go·Plus·Pro 한도와 원화 가격 (2026)",
      "2026년 8월부터 챗GPT 무료도 대화는 무제한. 무료·Go(13,000원)·Plus(29,000원)·Pro 차이, 유료로 갈아탈 타이밍, 직업별 추천, 요금제 + API 전략까지.",
      "Jonhisking · 2026년 10월 8일", "chatgpt-free-vs-paid-ko.jpg"),
 _fpd("en", "/blog/chatgpt-free-vs-paid", "freepaid-en", "ChatGPT Free vs Paid (2026): What You Actually Get for $0, $8, $20 and $100",
      "ChatGPT free vs paid in 2026: chat is now unlimited on Free. See what Go ($8), Plus ($20) and Pro ($100+) really add, and when it's worth upgrading.",
      "Jonhisking · October 8, 2026", "chatgpt-free-vs-paid-en.jpg"),
 _fpd("ja", "/ja/blog/chatgpt-muryou-yuuryou-chigai", "freepaid-ja", "ChatGPT 無料と有料の違い【2026年】：Go・Plus・Pro はいつ課金すべき？料金と選び方",
      "2026年8月からChatGPT無料版もチャット無制限に。無料・Go 1,400円・Plus 3,000円・Pro 16,800円〜の違い、有料にするタイミング、職業別のおすすめ、API併用で節約する方法。",
      "Jonhisking · 2026年10月8日", "chatgpt-free-vs-paid-ja.jpg"),
 _fpd("uk", "/uk/blog/chatgpt-bezkoshtovno-chy-platno", "freepaid-uk", "ChatGPT безкоштовно чи платно 2026: різниця і ціни в Україні з ПДВ",
      "Безкоштовний ChatGPT тепер без ліміту розмов. Чим відрізняються Free, Go (≈375 ₴), Plus (≈1 070 ₴) і Pro з ПДВ, коли варто платити і що обрати під вашу роботу.",
      "Jonhisking · 8 жовтня 2026", "chatgpt-free-vs-paid-uk.jpg"),
 _fpd("zh-CN", "/zh-cn/blog/chatgpt-mianfei-vs-fufei", "freepaid-zhcn", "ChatGPT 免费版和付费版区别（2026）：Go、Plus、Pro 怎么选？",
      "2026 年起 ChatGPT 免费版日常对话也不限条数。免费 $0、Go $8、Plus $20、Pro $100 起的区别，什么时候该升级，按职业推荐，以及用 API 省钱的方法。",
      "Jonhisking · 2026年10月8日", "chatgpt-free-vs-paid-zhcn.jpg"),
 _fpd("fr", "/fr/blog/chatgpt-gratuit-ou-payant", "freepaid-fr", "ChatGPT gratuit ou payant en 2026 : Gratuit, Go, Plus, Pro, quelles différences ?",
      "ChatGPT gratuit ou payant ? Le chat est illimité partout depuis août 2026. Modèle, limites, pub : Go 8 €, Plus 23 €, Pro dès 103 €. Quand passer au payant.",
      "Jonhisking · 8 octobre 2026", "chatgpt-free-vs-paid-fr.jpg"),
 _fpd("de", "/de/blog/chatgpt-kostenlos-vs-plus", "freepaid-de", "ChatGPT kostenlos vs. Plus 2026: Lohnt sich das Bezahl-Abo?",
      "ChatGPT kostenlos vs. bezahlt 2026: Chat ist überall unbegrenzt. Was Go (7,99 €), Plus (22,99 €) und Pro unterscheidet und wann sich ein Upgrade lohnt.",
      "Jonhisking · 8. Oktober 2026", "chatgpt-free-vs-paid-de.jpg"),
]

# 2026-10-08: indie game development cost (ko)
INDIECOST = [_gm("ko", "/ko/blog/indie-game-gaebal-biyong", "인디게임 개발 비용 얼마? 1인 개발 vs 외주, 엔진·스토어 등록비 정리 (2026)",
     "인디게임 개발 비용 총정리: Unity·Godot·Unreal 엔진 비용과 장단점, Steam·Google Play·Apple 등록비와 준비물, 외주 vs AI로 혼자 만들기 비용 비교.",
     "Jonhisking · 2026년 10월 8일")]
INDIECOST[0].update(src="indiecost-ko", date="2026-10-08")

# 2026-10-09: Turkish localizations (subs, gogo, gemgp, freepaid)
_TR_BY = "Jonhisking · 9 Ekim 2026"
_TR_CTA = ("Yapay zekâyı ne kadar kullandığınızı girin; abonelik mi yoksa API mi daha ucuz, Türkçe tokenlarla birlikte görün.", "Abonelik vs API hesapla")
for _p, _src, _ti, _de in [
    ("/tr/blog/yapay-zeka-abonelik-fiyatlari", "subs-tr", "Yapay zeka abonelik fiyatları 2026: ChatGPT, Claude, Gemini TL fiyatları",
     "ChatGPT Go 249,99 TL, Plus 999,99 TL, Google AI Pro 869,99 TL, Claude Pro $20 + KDV. Türkiye'deki tüm yapay zeka abonelik fiyatları ve API ile karşılaştırma."),
    ("/tr/blog/chatgpt-go-vs-plus", "gogo-tr", "ChatGPT Go vs Plus: 249,99 TL mi 999,99 TL mi? Farklar ve kime uygun",
     "ChatGPT Go vs Plus: Go 249,99 TL ve reklamlı, Plus 999,99 TL ve reklamsız. Model, düşünme modu, Codex farkları ve hangi planın size uygun olduğu."),
    ("/tr/blog/gemini-ucretsiz-flash-lite", "gemgp-tr", "Gemini ücretsiz artık Flash-Lite: 9 Ekim değişikliği ve Google AI fiyatları",
     "9 Ekim 2026'dan itibaren Gemini ücretsiz sadece Flash-Lite kullanıyor. Google AI Plus 199,99 TL, Pro 869,99 TL. Ne değişti ve API ile ucuz alternatif."),
]:
    _d = _cc("tr", _p, _src, _ti, _de, _TR_BY, *_TR_CTA); _d["date"] = "2026-10-09"; EU6.append([_d])
FREEPAID.append(dict(_cc("tr", "/tr/blog/chatgpt-ucretsiz-mi-ucretli-mi", "freepaid-tr", "ChatGPT ücretsiz mi ücretli mi? Ücretsiz, Go, Plus, Pro farkları ve TL fiyatları",
     "ChatGPT ücretsiz mi ücretli mi? Ağustos 2026'dan beri sohbet ücretsizde de sınırsız. Go 249,99 TL, Plus 999,99 TL, Pro farkları ve ne zaman yükseltmeli.",
     _TR_BY, *_TR_CTA), date="2026-10-09"))

# 2026-10-09: Meta Muse Spark 1.3 API pricing (en, ko)
MUSE13 = [
 _cc("en", "/blog/muse-spark-1-3-api-pricing", "muse13-en", "Muse Spark 1.3 API Pricing: Meta's Model vs Claude, GPT-6 and Gemini",
     "Meta's Muse Spark 1.3 costs $1.25 / $4.25 per million tokens, $0.15 cached, no long-context premium. Real costs vs Claude Sonnet 5.5, GPT-6 Sol and Gemini.",
     "Jonhisking · October 9, 2026", "Paste a prompt to see its tokens and cost on Muse Spark 1.3, GPT-6, Claude, Gemini and 30+ models.", "Open the token counter"),
 _cc("ko", "/ko/blog/muse-spark-1-3-api-gagyeok", "muse13-ko", "메타 Muse Spark 1.3 API 가격: Claude·GPT-6·Gemini와 비용 비교",
     "메타 Muse Spark 1.3 API 가격은 100만 토큰당 입력 $1.25, 출력 $4.25, 캐시 $0.15. 긴 컨텍스트 할증 없음. Claude Sonnet 5.5·GPT-6 Sol·Gemini와 실제 비용 비교.",
     "Jonhisking · 2026년 10월 9일", "프롬프트를 붙여 넣고 Muse Spark 1.3·GPT-6·Claude·Gemini 등 30개 넘는 모델의 토큰과 비용을 비교해 보세요.", "토큰 계산기 열기"),
]
MUSE13.append(_cc("ja", "/ja/blog/muse-spark-1-3-api-ryoukin", "muse13-ja", "Meta Muse Spark 1.3 の API 料金：Claude・GPT-6・Gemini と費用比較",
     "Meta Muse Spark 1.3 の API 料金は100万トークンあたり入力 $1.25、出力 $4.25、キャッシュ $0.15。長文割増なし。Claude Sonnet 5.5・GPT-6 Sol・Gemini と実費用を比較。",
     "Jonhisking · 2026年10月9日", "プロンプトを貼り付けて、Muse Spark 1.3・GPT-6・Claude・Gemini など30以上のモデルのトークンと費用を比べましょう。", "トークンカウンターを開く"))
for _d in MUSE13: _d["date"] = "2026-10-09"
