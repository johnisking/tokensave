For years, anyone using GPT in Hindi, Tamil or Malayalam paid several times more than an English user for the same request. Then, with GPT-4o in May 2024, OpenAI switched to a new tokenizer, and for many languages the cost of a prompt dropped by more than half overnight. Here is how tokenizers work, what changed, and the measured effect on 40 languages.

## How a tokenizer is built

GPT models use a method called **byte-pair encoding (BPE)**. It starts from raw bytes and repeatedly merges the pairs that appear together most often in a large training text, until it has a fixed vocabulary of pieces. Frequent words end up as single tokens. Rare words are built from several smaller pieces, and in the worst case from individual bytes.

The key point: **the vocabulary reflects the text it was trained on.** If that text is mostly English, English words get their own tokens and everything else is pieced together from fragments.

Scripts outside the Latin alphabet suffer most. A character in Hindi's Devanagari script, or in Tamil or Malayalam, takes three bytes in UTF-8. If the tokenizer has few merges for that script, a single letter can cost several tokens.

## cl100k vs o200k

OpenAI has used two main tokenizers for its recent models:

- **cl100k_base**, about 100,000 tokens, used by GPT-3.5 Turbo and GPT-4.
- **o200k_base**, about 200,000 tokens, introduced with GPT-4o and used by later GPT models.

Doubling the vocabulary left room for far more pieces from non-English languages, so whole words and common syllables in many scripts became single tokens.

## Measured: the same prompt in 41 languages

We translated one 34-token English prompt (a request to summarize a customer email and suggest a reply) into 40 languages and counted tokens on both tokenizers. Each number is how many tokens the language needs compared with English.

| Language | cl100k (older GPT-4) | o200k (GPT-4o and later) | Cost cut |
|---|---|---|---|
| Malayalam | 10.09× | 1.85× | 82% |
| Kannada | 9.35× | 1.79× | 81% |
| Telugu | 9.38× | 2.03× | 78% |
| Gujarati | 7.18× | 1.59× | 78% |
| Tamil | 8.47× | 1.97× | 77% |
| Bengali | 6.09× | 1.68× | 72% |
| Hindi | 4.59× | 1.50× | 67% |
| Punjabi | 7.41× | 2.44× | 67% |
| Marathi | 4.91× | 1.65× | 66% |
| Urdu | 4.24× | 1.59× | 62% |
| Hebrew | 3.76× | 1.56× | 59% |
| Arabic | 3.03× | 1.26× | 58% |
| Greek | 4.94× | 2.06× | 58% |
| Persian | 2.79× | 1.24× | 56% |
| Thai | 3.71× | 1.74× | 53% |
| Korean | 2.50× | 1.44× | 42% |
| Vietnamese | 2.32× | 1.35× | 42% |
| Ukrainian | 3.15× | 1.88× | 40% |
| Russian | 2.15× | 1.32× | 39% |
| Chinese (Traditional) | 2.12× | 1.35× | 36% |
| Chinese (Simplified) | 1.53× | 1.03× | 33% |
| Finnish | 2.03× | 1.44× | 29% |
| Turkish | 2.06× | 1.47× | 29% |
| Dutch | 1.74× | 1.29× | 26% |
| Hungarian | 2.26× | 1.74× | 23% |
| Czech | 2.59× | 2.00× | 23% |
| Slovak | 2.53× | 2.00× | 21% |
| Japanese | 2.21× | 1.79× | 19% |
| Indonesian | 1.38× | 1.15× | 17% |
| German | 1.50× | 1.26× | 16% |
| Norwegian | 1.56× | 1.32× | 15% |
| Danish | 1.59× | 1.35× | 15% |
| Portuguese | 1.41× | 1.21× | 14% |
| Italian | 1.59× | 1.38× | 13% |
| Filipino | 1.76× | 1.53× | 13% |
| Romanian | 1.76× | 1.53× | 13% |
| Swedish | 1.50× | 1.32× | 12% |
| Polish | 2.12× | 1.88× | 11% |
| French | 1.44× | 1.29× | 10% |
| Spanish | 1.29× | 1.18× | 9% |

## What the numbers show

**South Asian languages gained the most.** Malayalam went from about 10 times the tokens of English to 1.85 times, an 82% cut. Kannada, Telugu, Gujarati and Tamil all fell by more than three-quarters. Hindi, spoken by hundreds of millions of people, went from 4.59× to 1.50×.

**Middle Eastern scripts improved a lot.** Arabic, Persian and Hebrew all roughly halved.

**East Asian languages improved less, from a lower base.** Korean went from 2.50× to 1.44×; Simplified Chinese is now almost at parity with English at 1.03×. Japanese, at 1.79×, is still one of the more expensive languages.

**European languages changed least.** They were already close to English on the old tokenizer. Some, such as Czech, Slovak and Polish, remain among the most expensive on the new one, at around 2×, because of their accented letters and long word forms.

## The gap is smaller, not gone

On o200k, the same prompt still costs 15% more in Spanish, 44% more in Korean and twice as much in Czech as in English. Pricing is per token, so that difference goes straight to the bill, and it also means the context window fills up faster and usage limits are reached sooner.

## Other providers are different

Anthropic, Google, Meta, Mistral and DeepSeek all train their own tokenizers, and their efficiency by language varies. A model with a lower price per token can still cost more for your language if its tokenizer splits your text into more pieces. When comparing providers, compare the cost of your actual text, not the price list. We compared GPT and Mistral for French and Polish in separate articles ([French](/fr/blog/mistral-chatgpt-cout-prompt-francais), [Polish](/pl/blog/ile-kosztuje-prompt-po-polsku)).

## How we measured

One English prompt of 34 tokens was translated into each language, starting from machine translation that was then checked, keeping the meaning and tone the same. Tokens were counted with OpenAI's published tokenizers (cl100k_base and o200k_base). One prompt is a small sample, so longer texts and different topics will give somewhat different ratios, but the large gaps between scripts are far bigger than that variation. Full details and per-language articles are in our [41-language study](/blog/token-cost-by-language).

## Paying less in any language

The easiest saving is still to write instructions in English and ask for the answer in your language. See [How to cut the token cost of non-English prompts](/blog/cut-token-cost-non-english-prompts), or paste your prompt into the [token counter](/) and press *To English* to see the difference.
