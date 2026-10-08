![Prompting in Korean, Japanese or Hindi? How to Cut the Token Cost](/cut-token-cost-non-english-prompts-en.jpg)

If you write your prompts in Korean, Japanese, Hindi, Thai or most other languages, you pay more for the same request than someone writing in English. Not because providers charge by country, but because their tokenizers split non-English text into more pieces. Here is how big the difference is, and the simplest ways to get it back.

## The language tax, measured

![The language tax, measured: Language, Tokens vs English, Saving if sent in English](/cut-token-cost-non-english-prompts-the-language-tax-measured-en.jpg)

We sent the same 34-token English prompt through GPT's current o200k tokenizer in 41 languages. Some results:

| Language | Tokens vs English | Saving if sent in English |
|---|---|---|
| Thai | +74% | about 43% |
| Japanese | +79% | about 44% |
| Hindi | +50% | about 33% |
| Turkish | +47% | about 32% |
| Korean | +44% | about 31% |
| Russian | +32% | about 24% |
| French | +29% | about 22% |
| German | +26% | about 21% |
| Spanish | +18% | about 15% |

The "saving" column is how many fewer tokens the same content needs in English. The [full 41-language study](/blog/token-cost-by-language) has every language, including the ones that cost 100% more than English.

## Why it matters

![Why it matters: API cost scales directly with tokens. A team sending Japanese prompts pays roughly 80% more than an English-sp](/cut-token-cost-non-english-prompts-why-it-matters-en.jpg)

- **API cost** scales directly with tokens. A team sending Japanese prompts pays roughly 80% more than an English-speaking team pays for the same work.
- **Usage limits** on many plans and agents are counted in tokens, so you hit them sooner.
- **Context windows** fill up faster, so long documents and chats reach the limit earlier.

## Five ways to pay less

**1. Translate the prompt to English before sending it.** This is the biggest single saving, and modern models understand an English prompt perfectly well while still answering in your language if you ask. The [TokenSave token counter](/) has a one-click *Save tokens* button: it cleans up spaces, translates the prompt to English with the AI translator built into desktop Chrome 138+ and Edge 148+, trims filler, and adds a line asking for the reply in your original language. Translation runs on your device, so your text is not uploaded, and the counter shows how many tokens you saved.

**2. Ask for the answer in your language, keep the instructions in English.** System prompts and long instructions are sent with every request. Writing those in English and adding one line, *"Reply in Korean"*, saves tokens on every call without changing what the user sees.

**3. Remove repeated spaces and filler.** Extra line breaks, double spaces and polite padding all cost tokens. The token counter's *Save tokens* button does this automatically as its first step.

**4. Keep chats short.** Every new message re-sends the whole conversation. Start a new chat for a new topic and carry over a short summary instead of the full history.

**5. Compare models on your own text.** Tokenizers differ. A model with a slightly higher price per token can still be cheaper for your language if it splits it into fewer tokens. Count your real text before choosing.

## When not to translate

Translate instructions and questions, not material where wording matters: legal text you need quoted exactly, poetry, names, or text the model must correct for grammar. For those, the original language is the content.

## Try it with your own prompt

Paste a prompt into the [token counter](/), press *Save tokens*, and see the difference in tokens and cost across 30+ models.

## Sources

- [tiktoken (OpenAI tokenizer, o200k_base)](https://github.com/openai/tiktoken)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
<!-- autoimg -->
