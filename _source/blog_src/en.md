I translated one ordinary customer-support prompt into 41 languages and counted tokens with **o200k_base**, the tokenizer behind GPT-4o and every newer OpenAI model (the last column uses cl100k, the GPT-4-era tokenizer). English needs 34 tokens. The same request costs anywhere from **1.03×** (Simplified Chinese) to **2.44×** (Punjabi).

The English prompt:

> Please summarize the customer email below in three bullet points and suggest a polite reply. The customer says the order arrived two days late and one item was missing from the box.

## All 41 languages

| Language | Tokens | vs English | Old GPT-4 |
|---|---:|---:|---:|
| English | 34 | 1.00× | 1.00× |
| Chinese (Simplified) | 35 | 1.03× | 1.53× |
| Indonesian | 39 | 1.15× | 1.38× |
| Spanish | 40 | 1.18× | 1.29× |
| Portuguese | 41 | 1.21× | 1.41× |
| Persian | 42 | 1.24× | 2.79× |
| German | 43 | 1.26× | 1.50× |
| Arabic | 43 | 1.26× | 3.03× |
| French | 44 | 1.29× | 1.44× |
| Dutch | 44 | 1.29× | 1.74× |
| Russian | 45 | 1.32× | 2.15× |
| Swedish | 45 | 1.32× | 1.50× |
| Norwegian | 45 | 1.32× | 1.56× |
| Chinese (Traditional) | 46 | 1.35× | 2.12× |
| Vietnamese | 46 | 1.35× | 2.32× |
| Danish | 46 | 1.35× | 1.59× |
| Italian | 47 | 1.38× | 1.59× |
| Korean | 49 | 1.44× | 2.50× |
| Finnish | 49 | 1.44× | 2.03× |
| Turkish | 50 | 1.47× | 2.06× |
| Hindi | 51 | 1.50× | 4.59× |
| Filipino | 52 | 1.53× | 1.76× |
| Romanian | 52 | 1.53× | 1.76× |
| Hebrew | 53 | 1.56× | 3.76× |
| Urdu | 54 | 1.59× | 4.24× |
| Gujarati | 54 | 1.59× | 7.18× |
| Marathi | 56 | 1.65× | 4.91× |
| Bengali | 57 | 1.68× | 6.09× |
| Thai | 59 | 1.74× | 3.71× |
| Hungarian | 59 | 1.74× | 2.26× |
| Japanese | 61 | 1.79× | 2.21× |
| Kannada | 61 | 1.79× | 9.35× |
| Malayalam | 63 | 1.85× | 10.09× |
| Ukrainian | 64 | 1.88× | 3.15× |
| Polish | 64 | 1.88× | 2.12× |
| Tamil | 67 | 1.97× | 8.47× |
| Czech | 68 | 2.00× | 2.59× |
| Slovak | 68 | 2.00× | 2.53× |
| Telugu | 69 | 2.03× | 9.38× |
| Greek | 70 | 2.06× | 4.94× |
| Punjabi | 83 | 2.44× | 7.41× |

![Extra tokens per language vs English](/blog-language-tax-chart-v4.png)

## Why some languages cost more

Tokenizers are trained mostly on English, so common English words are a single token (" polite", " customer"). Words in other languages are split into pieces, and endings or diacritics often become tokens of their own:

- Czech: navrhněte → `nav | r | hn | ě | te`
- Polish: opóźnieniem → `op | ó | ź | n | ieniem`
- Hindi: सारांशित → `सार | ांश | ित`

## The old tokenizer was much worse

On the GPT-4-era tokenizer (cl100k), the gap was far larger. The biggest improvements:

- Malayalam: 10.09× → 1.85×
- Kannada: 9.35× → 1.79×
- Telugu: 9.38× → 2.03×
- Gujarati: 7.18× → 1.59×
- Tamil: 8.47× → 1.97×

That is why the common advice "Korean costs 2–3× English" is out of date: Korean went from 2.50× to 1.44×.

## What it costs

With a model at $2 per million input tokens, sending this prompt one million times costs $68 in English, $98 in Korean, $122 in Japanese and $136 in Czech. If the model also answers in that language, the same multiplier applies to output tokens, which usually cost 4–5× more.

## How to spend fewer tokens

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
