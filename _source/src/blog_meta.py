# -*- coding: utf-8 -*-
# Language-specific articles. Body HTML lives in src/blog/<tag>.html, generated from
# blog_src/<tag>.md by `python3 _source/make_blog.py` (needs the `markdown` package; the
# site build itself does not).
# All four are versions of the same study, so they point at each other with hreflang.

BLOG_DATE = "2026-09-30"

BLOG = [
    dict(tag="cs", path="/cs/blog/cestina-tokeny-gpt",
         title="Čeština v GPT stojí 2× víc tokenů než angličtina",
         desc="Stejný prompt v 27 jazycích: čeština je nejdražší, 68 tokenů proti 34. Proč a jak ušetřit.",
         byline="Jonhisking · 30. 9. 2026",
         cta="Změřte si vlastní text: kolik tokenů a peněz stojí váš prompt v češtině oproti angličtině.",
         ctaBtn="Otevřít počítadlo tokenů"),
    dict(tag="pl", path="/pl/blog/polski-tokeny-gpt",
         title="Polski w GPT zużywa 1,88× więcej tokenów niż angielski",
         desc="Ten sam prompt w 27 językach: polski prawie 2× droższy od angielskiego. Dlaczego i jak oszczędzać.",
         byline="Jonhisking · 30.09.2026",
         cta="Sprawdź własny tekst: ile tokenów i pieniędzy kosztuje twój prompt po polsku w porównaniu z angielskim.",
         ctaBtn="Otwórz licznik tokenów"),
    dict(tag="ja", path="/ja/blog/nihongo-tokens-gpt",
         title="日本語は英語の1.79倍のトークンを使う：27言語で実測",
         desc="同じプロンプトを27言語で測定。日本語は英語の1.79倍、旧GPT-4からほぼ改善なし。節約のコツも。",
         byline="Jonhisking · 2026年9月30日",
         cta="自分の文章で測ってみましょう。日本語のプロンプトが英語の何倍のトークンと料金になるかすぐ分かります。",
         ctaBtn="トークンカウンターを開く"),
    dict(tag="ko", path="/ko/blog/korean-tokens-gpt",
         title="한국어 프롬프트는 영어보다 토큰이 몇 배 들까? 27개 언어 실측",
         desc="같은 프롬프트를 27개 언어로 측정. 한국어는 영어의 1.44배, 예전 2.5배에서 크게 줄었습니다.",
         byline="Jonhisking · 2026년 9월 30일",
         cta="내 프롬프트로 직접 재보세요. 한국어가 영어보다 토큰과 비용이 몇 배 드는지 바로 보여드립니다.",
         ctaBtn="토큰 계산기 열기"),
]

# Generated articles (blog_gen.py): English overview + 22 more languages
import json as _json, os as _os
_auto = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "blog_data", "auto.json")
BLOG += _json.load(open(_auto, encoding="utf-8"))
