![How GPT's New Tokenizer Cut Costs in 40 Languages](/gpt-tokenizer-cl100k-vs-o200k-en.jpg)

For years, anyone using GPT in Hindi, Tamil or Malayalam paid far more than an English user for the same request. Then, with GPT-4o in May 2024, OpenAI switched to a new tokenizer, and for many languages the cost of a prompt dropped by more than 50% overnight. Here is how tokenizers work, what changed, and the measured effect on 40 languages.

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

![Measured: the same prompt in 41 languages: Language, cl100k (older GPT-4) vs English, o200k (GPT-4o and later) vs English, Cost cut](/gpt-tokenizer-cl100k-vs-o200k-measured-the-same-prompt-in-41-languages-en.jpg)

We translated one 34-token English prompt (a request to summarize a customer email and suggest a reply) into 40 languages and counted tokens on both tokenizers. Each number is how many more tokens the language needs than English.

| Language | cl100k (older GPT-4) vs English | o200k (GPT-4o and later) vs English | Cost cut |
|---|---|---|---|
| Malayalam | +909% | +85% | 82% |
| Kannada | +835% | +79% | 81% |
| Telugu | +838% | +103% | 78% |
| Gujarati | +618% | +59% | 78% |
| Tamil | +747% | +97% | 77% |
| Bengali | +509% | +68% | 72% |
| Hindi | +359% | +50% | 67% |
| Punjabi | +641% | +144% | 67% |
| Marathi | +391% | +65% | 66% |
| Urdu | +324% | +59% | 62% |
| Hebrew | +276% | +56% | 59% |
| Arabic | +203% | +26% | 58% |
| Greek | +394% | +106% | 58% |
| Persian | +179% | +24% | 56% |
| Thai | +271% | +74% | 53% |
| Korean | +150% | +44% | 42% |
| Vietnamese | +132% | +35% | 42% |
| Ukrainian | +215% | +88% | 40% |
| Russian | +115% | +32% | 39% |
| Chinese (Traditional) | +112% | +35% | 36% |
| Chinese (Simplified) | +53% | +3% | 33% |
| Finnish | +103% | +44% | 29% |
| Turkish | +106% | +47% | 29% |
| Dutch | +74% | +29% | 26% |
| Hungarian | +126% | +74% | 23% |
| Czech | +159% | +100% | 23% |
| Slovak | +153% | +100% | 21% |
| Japanese | +121% | +79% | 19% |
| Indonesian | +38% | +15% | 17% |
| German | +50% | +26% | 16% |
| Norwegian | +56% | +32% | 15% |
| Danish | +59% | +35% | 15% |
| Portuguese | +41% | +21% | 14% |
| Italian | +59% | +38% | 13% |
| Filipino | +76% | +53% | 13% |
| Romanian | +76% | +53% | 13% |
| Swedish | +50% | +32% | 12% |
| Polish | +112% | +88% | 11% |
| French | +44% | +29% | 10% |
| Spanish | +29% | +18% | 9% |

## What the numbers show

![What the numbers show: South Asian languages gained the most; Middle Eastern scripts improved a lot; East Asian languages improved less, from a lower ](/gpt-tokenizer-cl100k-vs-o200k-what-the-numbers-show-en.jpg)

**South Asian languages gained the most.** Malayalam went from about 909% more tokens than English to 85% more, an 82% cut. Kannada, Telugu, Gujarati and Tamil all fell by more than three-quarters. Hindi, spoken by hundreds of millions of people, went from 359% more to 50% more.

**Middle Eastern scripts improved a lot.** Arabic, Persian and Hebrew all fell by roughly 50%.

**East Asian languages improved less, from a lower base.** Korean went from 150% more to 44% more; Simplified Chinese is now almost at parity with English at 3% more. Japanese, at 79% more, is still one of the more expensive languages.

**European languages changed least.** They were already close to English on the old tokenizer. Some, such as Czech, Slovak and Polish, remain among the most expensive on the new one, at around 100% more than English, because of their accented letters and long word forms.

## The gap is smaller, not gone

On o200k, the same prompt still costs 15% more in Spanish, 44% more in Korean and 100% more in Czech than in English. Pricing is per token, so that difference goes straight to the bill, and it also means the context window fills up faster and usage limits are reached sooner.

## Other providers are different

Anthropic, Google, Meta, Mistral and DeepSeek all train their own tokenizers, and their efficiency by language varies. A model with a lower price per token can still cost more for your language if its tokenizer splits your text into more pieces. When comparing providers, compare the cost of your actual text, not the price list. We compared GPT and Mistral for French and Polish in separate articles ([French](/fr/blog/mistral-chatgpt-cout-prompt-francais), [Polish](/pl/blog/ile-kosztuje-prompt-po-polsku)).

## How we measured

One English prompt of 34 tokens was translated into each language, starting from machine translation that was then checked, keeping the meaning and tone the same. Tokens were counted with OpenAI's published tokenizers (cl100k_base and o200k_base). One prompt is a small sample, so longer texts and different topics will give somewhat different ratios, but the large gaps between scripts are far bigger than that variation. Full details and per-language articles are in our [41-language study](/blog/token-cost-by-language).

## Paying less in any language

The easiest saving is still to write instructions in English and ask for the answer in your language. See [How to cut the token cost of non-English prompts](/blog/cut-token-cost-non-english-prompts), or paste your prompt into the [token counter](/) and press *Save tokens* to see the difference.

## Sources

- [tiktoken (OpenAI tokenizer, o200k_base)](https://github.com/openai/tiktoken)
- [tiktoken model-to-encoding map](https://github.com/openai/tiktoken/blob/main/tiktoken/model.py)
- [Hello GPT-4o (OpenAI, May 13, 2024)](https://openai.com/index/hello-gpt-4o/)
<!-- autoimg -->
