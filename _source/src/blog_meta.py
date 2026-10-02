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
         title="Polski w GPT zużywa 1,88× więcej tokenów niż angielski",
         desc="Ten sam prompt w 41 językach: polski prawie 2× droższy od angielskiego. Dlaczego i jak oszczędzać.",
         byline="Jonhisking · 30.09.2026",
         cta="Sprawdź własny tekst: ile tokenów i pieniędzy kosztuje twój prompt po polsku w porównaniu z angielskim.",
         ctaBtn="Otwórz licznik tokenów"),
    dict(tag="ja", path="/ja/blog/nihongo-tokens-gpt",
         title="日本語は英語の1.79倍のトークンを使う：41言語で実測",
         desc="同じプロンプトを41言語で測定。日本語は英語の1.79倍、旧GPT-4からほぼ改善なし。節約のコツも。",
         byline="Jonhisking · 2026年9月30日",
         cta="自分の文章で測ってみましょう。日本語のプロンプトが英語の何倍のトークンと料金になるかすぐ分かります。",
         ctaBtn="トークンカウンターを開く"),
    dict(tag="ko", path="/ko/blog/korean-tokens-gpt",
         title="한국어 프롬프트는 영어보다 토큰이 몇 배 들까? 41개 언어 실측",
         desc="같은 프롬프트를 41개 언어로 측정. 한국어는 영어의 1.44배, 예전 2.5배에서 크게 줄었습니다.",
         byline="Jonhisking · 2026년 9월 30일",
         cta="내 프롬프트로 직접 재보세요. 한국어가 영어보다 토큰과 비용이 몇 배 드는지 바로 보여드립니다.",
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
  "title": "ChatGPT Pro 100 vs 200 vs 500: Which Plan Is Worth It?",
  "desc": "ChatGPT Pro now comes in $100, $200 and $500 tiers. Usage per dollar, the Pro 200 cut, Ultrafast, and when the API is cheaper.",
  "byline": "Jonhisking · October 1, 2026",
  "cta": "Enter how many messages you send, how long they are and your language, and see whether a subscription or the API is cheaper for you.",
  "ctaBtn": "Open the Subscription vs API calculator",
  "date": "2026-10-01"
 },
 {
  "tag": "ko",
  "path": "/ko/blog/chatgpt-pro-yogeumje-bigyo",
  "src": "pro-ko",
  "title": "챗GPT Pro 100 vs 200 vs 500 요금제 비교: 뭘 골라야 할까",
  "desc": "ChatGPT 프로 요금제가 Pro 100·200·500으로 나뉘었습니다. 사용량 대비 가격, Ultrafast 차이, 플러스와 API 중 무엇이 싼지 정리했습니다.",
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
    "Paste your prompt, press To English, and see how many tokens you save.", "Open the token counter"),
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
