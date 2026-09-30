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
