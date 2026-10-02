If you write your prompts in Korean, Japanese, Hindi, Thai or most other languages, you pay more for the same request than someone writing in English. Not because providers charge by country, but because their tokenizers split non-English text into more pieces. Here is how big the difference is, and the simplest ways to get it back.

## The language tax, measured

We sent the same 34-token English prompt through GPT's current o200k tokenizer in 41 languages. Some results:

| Language | Tokens vs English | Saving if sent in English |
|---|---|---|
| Thai | 1.74× | about 43% |
| Japanese | 1.79× | about 44% |
| Hindi | 1.50× | about 33% |
| Turkish | 1.47× | about 32% |
| Korean | 1.44× | about 31% |
| Russian | 1.32× | about 24% |
| French | 1.29× | about 22% |
| German | 1.26× | about 21% |
| Spanish | 1.18× | about 15% |

The "saving" column is how many fewer tokens the same content needs in English. The [full 41-language study](/blog/token-cost-by-language) has every language, including the ones that cost twice as much as English.

The gap has shrunk a lot. Hindi used 4.59× the tokens of English on the old GPT-4 tokenizer and 1.50× today. But it has not closed.

## Why it matters

- **API cost** scales directly with tokens. A team sending Japanese prompts pays roughly 1.8 times what an English-speaking team pays for the same work.
- **Usage limits** on many plans and agents are counted in tokens, so you hit them sooner.
- **Context windows** fill up faster, so long documents and chats reach the limit earlier.

## Five ways to pay less

**1. Translate the prompt to English before sending it.** This is the biggest single saving, and modern models understand an English prompt perfectly well while still answering in your language if you ask. The [TokenSave token counter](/) has a one-click *To English* button that uses the AI translator built into desktop Chrome 138+ and Edge 148+. It runs on your device, so your text is not uploaded, and it shows how many tokens you saved.

**2. Ask for the answer in your language, keep the instructions in English.** System prompts and long instructions are sent with every request. Writing those in English and adding one line, *"Reply in Korean"*, saves tokens on every call without changing what the user sees.

**3. Remove repeated spaces and filler.** Extra line breaks, double spaces and polite padding all cost tokens. The token counter's *Save tokens* button cleans up spaces, trims filler and translates to English in one go.

**4. Keep chats short.** Every new message re-sends the whole conversation. Start a new chat for a new topic and carry over a short summary instead of the full history.

**5. Compare models on your own text.** Tokenizers differ. A model with a slightly higher price per token can still be cheaper for your language if it splits it into fewer tokens. Count your real text before choosing.

## When not to translate

Translate instructions and questions, not material where wording matters: legal text you need quoted exactly, poetry, names, or text the model must correct for grammar. For those, the original language is the content.

## Try it with your own prompt

Paste a prompt into the [token counter](/), press *To English*, and see the difference in tokens and cost across 30+ models.
