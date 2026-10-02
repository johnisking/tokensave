Most people estimate tokens from word count: about four characters, or three-quarters of a word, per token. That rule works for ordinary prose. It breaks down badly for numbers, IDs, dates, links, phone numbers and emoji, which are exactly the things that fill product catalogs, logs, spreadsheets and chat messages. We measured them on GPT's o200k tokenizer.

## Numbers are split into groups of three digits

| Text | Tokens | How it splits |
|---|---|---|
| `2026` | 2 | 202 · 6 |
| `1234567` | 3 | 123 · 456 · 7 |
| `1,234,567` | 5 | 1 · , · 234 · , · 567 |
| `3.14159265` | 5 | 3 · . · 141 · 592 · 65 |
| `0.000123` | 4 | 0 · . · 000 · 123 |
| `$1,299.99` | 6 | $ · 1 · , · 299 · . · 99 |

The o200k tokenizer splits long numbers into chunks of up to three digits, counted from the left. Thousands separators and decimal points each become a token of their own. So `1,234,567` costs more than `1234567`, and a price like `$1,299.99` costs six tokens.

This chunking is also one reason language models are unreliable at exact arithmetic on long numbers: the model never sees `1234567` as one number, only as three pieces that happen to sit next to each other. For calculations that matter, have the model write and run code, or do the maths in your own code.

## Dates and times

| Text | Tokens |
|---|---|
| `2026-10-02` | 6 |
| `10/02/2026` | 6 |
| `October 2, 2026` | 7 |
| `14:35:07` | 5 |

A full timestamp like `2026-10-02T14:35:07Z` is 13 tokens. In a log with thousands of lines, timestamps alone can be a large part of the prompt. If the model does not need the exact time, remove them or keep only the time of day.

## IDs, links and contact details

| Text | Characters | Tokens |
|---|---|---|
| A UUID (`550e8400-e29b-41d4-...`) | 36 | 18 |
| `https://tokensave.app/blog/what-is-a-token` | 42 | 11 |
| `+82 10 1234 5678` | 16 | 10 |
| `192.168.0.1` | 11 | 7 |
| `user@example.com` | 16 | 3 |

A UUID costs 18 tokens: about two characters per token, half the efficiency of English text. Random-looking strings such as IDs, hashes, API keys and tracking parameters do not match anything in the tokenizer's vocabulary, so they break into small pieces.

The email address is the opposite case: `@example` and `.com` are common enough to be single tokens.

## Emoji: one token, or eleven

| Emoji | o200k (GPT-4o and later) | cl100k (older GPT-4) |
|---|---|---|
| 😀 | 1 | 2 |
| 👍 | 1 | 3 |
| ❤️ | 1 | 3 |
| 🇰🇷 (flag) | 4 | 6 |
| 👨‍👩‍👧‍👦 (family) | 11 | 18 |

Common emoji are a single token on the current tokenizer. But some emoji are built from several characters joined together. A flag is two special letters; the family emoji is four people glued with invisible joiner characters. Those cost many tokens. Arrows and symbols such as → and © are usually one token each.

## Why this matters

**Spreadsheets and catalogs.** A product table full of SKUs, prices and dates can use two to three times the tokens its character count suggests.

**Logs.** Timestamps, request IDs and IP addresses on every line add up fast.

**User data.** Chat messages full of emoji and links cost more than plain text of the same length.

**Estimates.** If you budget with the "4 characters per token" rule, number-heavy prompts will cost more than you planned.

## How to save tokens on this kind of data

1. **Replace long IDs with short keys.** Send `#1, #2, #3` to the model and keep a lookup table in your code to map them back.
2. **Drop precision the task does not need.** Round prices and measurements, and trim timestamps to the date or the time.
3. **Remove thousands separators** from numbers you send as data.
4. **Strip tracking parameters** from URLs (`?utm_source=...`).
5. **Don't send what the model does not use.** Columns of IDs and timestamps are often there only because they were in the export.

## Measure it

The [token counter](/) shows exactly how any text splits into tokens. Open *See how it splits into tokens* under the text box to see each piece highlighted.
