I translated one ordinary customer-support prompt into 41 languages and counted tokens with **o200k_base**, the tokenizer behind GPT-4o and every newer OpenAI model English needs 34 tokens. The same request costs anywhere from **1.03×** (Simplified Chinese) to **2.44×** (Punjabi).

The English prompt:

> Please summarize the customer email below in three bullet points and suggest a polite reply. The customer says the order arrived two days late and one item was missing from the box.

## All 41 languages

| Language | Tokens | vs English | Saved if sent in English |
|---|---:|---:|---:|
| English | 34 | 1.00× | – |
| Chinese (Simplified) | 35 | 1.03× | 3% |
| Indonesian | 39 | 1.15× | 13% |
| Spanish | 40 | 1.18× | 15% |
| Portuguese | 41 | 1.21× | 17% |
| Persian | 42 | 1.24× | 19% |
| German | 43 | 1.26× | 21% |
| Arabic | 43 | 1.26× | 21% |
| French | 44 | 1.29× | 22% |
| Dutch | 44 | 1.29× | 22% |
| Russian | 45 | 1.32× | 24% |
| Swedish | 45 | 1.32× | 24% |
| Norwegian | 45 | 1.32× | 24% |
| Chinese (Traditional) | 46 | 1.35× | 26% |
| Vietnamese | 46 | 1.35× | 26% |
| Danish | 46 | 1.35× | 26% |
| Italian | 47 | 1.38× | 28% |
| Korean | 49 | 1.44× | 31% |
| Finnish | 49 | 1.44× | 31% |
| Turkish | 50 | 1.47× | 32% |
| Hindi | 51 | 1.50× | 33% |
| Filipino | 52 | 1.53× | 35% |
| Romanian | 52 | 1.53× | 35% |
| Hebrew | 53 | 1.56× | 36% |
| Urdu | 54 | 1.59× | 37% |
| Gujarati | 54 | 1.59× | 37% |
| Marathi | 56 | 1.65× | 39% |
| Bengali | 57 | 1.68× | 40% |
| Thai | 59 | 1.74× | 43% |
| Hungarian | 59 | 1.74× | 43% |
| Japanese | 61 | 1.79× | 44% |
| Kannada | 61 | 1.79× | 44% |
| Malayalam | 63 | 1.85× | 46% |
| Ukrainian | 64 | 1.88× | 47% |
| Polish | 64 | 1.88× | 47% |
| Tamil | 67 | 1.97× | 49% |
| Czech | 68 | 2.00× | 50% |
| Slovak | 68 | 2.00× | 50% |
| Telugu | 69 | 2.03× | 51% |
| Greek | 70 | 2.06× | 51% |
| Punjabi | 83 | 2.44× | 59% |

![Extra tokens per language vs English](/blog-language-tax-chart-v4.png)

## Why some languages cost more

Tokenizers are trained mostly on English, so common English words are a single token (" polite", " customer"). Words in other languages are split into pieces, and endings or diacritics often become tokens of their own:

- Czech: navrhněte → `nav | r | hn | ě | te`
- Polish: opóźnieniem → `op | ó | ź | n | ieniem`
- Hindi: सारांशित → `सार | ांश | ित`

## Send it in English and save

Current models understand English instructions perfectly well and answer in your language if you ask, so the simplest saving is to send the prompt in English: about 31% fewer tokens for Korean, 44% for Japanese and 50% for Czech. In the [token counter](/), paste a prompt and press **💸 Save tokens**: it cleans up spaces, translates to English with the translator built into desktop Chrome 138+ / Edge 148+ (on your device; nothing is uploaded), trims filler and adds a line asking for the reply in your language. How the gap has changed over time is covered in [How GPT's new tokenizer cut costs in 40 languages](/blog/gpt-tokenizer-cl100k-vs-o200k).

## What it costs

With a model at $2 per million input tokens, sending this prompt one million times costs $68 in English, $98 in Korean, $122 in Japanese and $136 in Czech. If the model also answers in that language, the same multiplier applies to output tokens, which usually cost 4–5× more.

## How to spend fewer tokens

- Send the prompt in English and ask for the answer in your language (the Save tokens button does this in one click).
- Write the system prompt and fixed instructions in English; keep only user input in the user's language.
- Ask for intermediate steps (classification, extraction, tool calls) in English or JSON, and only the final answer in the user's language.
- Cache the fixed part of the prompt (prompt caching).

## Limitations

- One prompt only; with other text the ratios move by about ±0.1–0.2.
- Claude and Gemini use different tokenizers, so these numbers apply to OpenAI models.
- Translations started from machine translation and were checked.

## Read it in your language

[Čeština](/cs/blog/cestina-tokeny-gpt) · [Polski](/pl/blog/polski-tokeny-gpt) · [日本語](/ja/blog/nihongo-tokens-gpt) · [한국어](/ko/blog/korean-tokens-gpt) · [简体中文](/zh-cn/blog/zhongwen-token-gpt) · [繁體中文](/zh-tw/blog/zhongwen-fanti-token-gpt) · [Español](/es/blog/tokens-espanol-gpt) · [Português](/pt/blog/tokens-portugues-gpt) · [Français](/fr/blog/tokens-francais-gpt) · [Deutsch](/de/blog/tokens-deutsch-gpt) · [Italiano](/it/blog/token-italiano-gpt) · [Русский](/ru/blog/tokeny-russkiy-gpt) · [Українська](/uk/blog/tokeny-ukrainska-gpt) · [Türkçe](/tr/blog/token-turkce-gpt) · [العربية](/ar/blog/tokens-arabic-gpt) · [فارسی](/fa/blog/token-farsi-gpt) · [हिन्दी](/hi/blog/tokens-hindi-gpt) · [Bahasa Indonesia](/id/blog/token-bahasa-indonesia-gpt) · [Tiếng Việt](/vi/blog/token-tieng-viet-gpt) · [ไทย](/th/blog/token-phasa-thai-gpt) · [Nederlands](/nl/blog/tokens-nederlands-gpt) · [বাংলা](/bn/blog/token-bangla-gpt) · [اردو](/ur/blog/token-urdu-gpt) · [Filipino](/fil/blog/token-filipino-gpt) · [Svenska](/sv/blog/tokens-svenska-gpt) · [עברית](/he/blog/tokens-ivrit-gpt) · [Ελληνικά](/el/blog/tokens-ellinika-gpt) · [Română](/ro/blog/tokeni-romana-gpt) · [Magyar](/hu/blog/tokenek-magyar-gpt) · [Dansk](/da/blog/tokens-dansk-gpt) · [Suomi](/fi/blog/tokenit-suomi-gpt) · [Norsk](/no/blog/tokens-norsk-gpt) · [Slovenčina](/sk/blog/tokeny-slovencina-gpt) · [मराठी](/mr/blog/marathi-tokens-gpt) · [ગુજરાતી](/gu/blog/gujarati-tokens-gpt) · [ಕನ್ನಡ](/kn/blog/kannada-tokens-gpt) · [മലയാളം](/ml/blog/malayalam-tokens-gpt) · [தமிழ்](/ta/blog/tamil-tokens-gpt) · [తెలుగు](/te/blog/telugu-tokens-gpt) · [ਪੰਜਾਬੀ](/pa/blog/punjabi-tokens-gpt)

The original write-up and discussion are on [DEV](https://dev.to/jaehyun_cho_0dff271e0d2e5/i-sent-the-same-prompt-in-27-languages-czech-costs-2x-english-chinese-costs-the-same-420m).
