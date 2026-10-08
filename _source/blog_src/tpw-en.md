![Tokens per Word, Measured: English and 11 Other Languages](/tokens-per-word-en.jpg)

"One token is about four characters, or three-quarters of a word." You will find this rule of thumb everywhere. It comes from OpenAI's older tokenizers, and for modern models it is a little pessimistic for everyday English and wildly wrong for many other languages. We measured real text on GPT's current tokenizer (o200k, used by GPT-4o and later) to give updated numbers.

## English: about 1.1 to 1.3 tokens per word

![English: about 1.1 to 1.3 tokens per word: Text, Words, Tokens, Tokens per word, Characters per token](/tokens-per-word-english-about-1-1-to-1-3-tokens-per-word-en.jpg)

We counted four kinds of English text:

| Text | Words | Tokens | Tokens per word | Characters per token |
|---|---|---|---|---|
| A short story paragraph | 66 | 74 | 1.12 | 4.9 |
| An explainer paragraph | 183 | 206 | 1.13 | 4.9 |
| A work email | 79 | 91 | 1.15 | 4.7 |
| Technical API documentation | 75 | 100 | 1.33 | 4.4 |

So for everyday English on current models:

- **100 words ≈ 115 tokens** (plain prose) to **133 tokens** (technical writing)
- **1 token ≈ 4.4–4.9 characters**
- **1,000 tokens ≈ 750–890 words**

The classic "¾ of a word per token" (1.33 tokens per word) matches technical text, so it is a safe, slightly conservative estimate. For ordinary writing, you will usually use about 15% fewer tokens than it predicts.

Code is denser: in our measurements, Python and JavaScript averaged about 3.5 characters per token. See [How many tokens does code use?](/blog/how-many-tokens-does-code-use)

## Other languages: tokens per character

![Other languages: tokens per character: Language, Characters, Tokens, Characters per token, Tokens vs English](/tokens-per-word-other-languages-tokens-per-character-en.jpg)

Words are a poor unit across languages: Chinese, Japanese and Thai do not put spaces between words, and languages like Finnish or Turkish pack a whole phrase into one long word. Characters per token is more useful. Here is the same customer-support prompt in several languages:

| Language | Characters | Tokens | Characters per token | Tokens vs English |
|---|---|---|---|---|
| English | 181 | 34 | 5.3 | ±0% |
| Spanish | 183 | 40 | 4.6 | +18% |
| German | 194 | 43 | 4.5 | +26% |
| French | 197 | 44 | 4.5 | +29% |
| Russian | 165 | 45 | 3.7 | +32% |
| Arabic | 136 | 43 | 3.2 | +26% |
| Hindi | 161 | 51 | 3.2 | +50% |
| Polish | 190 | 64 | 3.0 | +88% |
| Thai | 132 | 59 | 2.2 | +74% |
| Korean | 87 | 49 | 1.8 | +44% |
| Chinese (Simplified) | 50 | 35 | 1.4 | +3% |
| Japanese | 73 | 61 | 1.2 | +79% |

Two things stand out:

- **Characters per token tells you little about cost on its own.** Chinese has only 1.4 characters per token, yet costs almost the same as English, because each Chinese character carries much more meaning. The last column, tokens for the same meaning, is what matters for your bill.
- **For Korean and Japanese, plan on roughly one token per 1.2–1.8 characters,** and expect about 40% (Korean) and 80% (Japanese) more tokens than the same content in English.

The full results for 41 languages are in our [language comparison](/blog/token-cost-by-language).

## Quick conversion table (English, current GPT models)

| You have | Roughly this many tokens |
|---|---|
| A tweet (40 words) | 45–55 |
| A short email (150 words) | 170–200 |
| A page of text (500 words) | 560–670 |
| A blog post (1,500 words) | 1,700–2,000 |
| A 300-page book (90,000 words) | 100,000–120,000 |

## Other models count differently

These numbers are for OpenAI's o200k tokenizer. Claude and Gemini use their own tokenizers, and the same text can be noticeably more tokens on them. Anthropic's newer Claude models in particular use more tokens for the same text than GPT. See [How to count tokens for GPT, Claude and Gemini](/blog/how-to-count-tokens-gpt-claude-gemini).

## Count your own text

Rules of thumb are fine for rough planning. For anything you will pay for, paste your real text into the [token counter](/): it runs the actual tokenizer in your browser and shows the cost on every model.

Convert any token count to words and pages for GPT, Claude and Gemini with the [tokens to words converter](/tokens-to-words).

## Sources

- [tiktoken (OpenAI): the o200k_base tokenizer](https://github.com/openai/tiktoken)
- [What are tokens and how to count them (OpenAI Help Center)](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)
- [Token counting (Anthropic docs)](https://platform.claude.com/docs/en/build-with-claude/token-counting)
<!-- autoimg -->
