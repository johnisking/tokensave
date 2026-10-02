"How many tokens is this?" has a different answer depending on which model you ask. OpenAI, Anthropic and Google each use their own tokenizer, so the same paragraph can be 100 tokens on one model and 130 on another. Here is how to get an exact count for each, and how to get a quick estimate without writing code.

## Why the counts differ

A tokenizer splits text into pieces from a fixed vocabulary that was built from the company's own training data. Different vocabularies mean different splits. A word that is one token for GPT may be two for Claude, and the other way round. The differences are usually small for plain English and larger for code, numbers and other languages.

Anthropic has said that the tokenizer used by its newer Claude models produces noticeably more tokens for the same text than its earlier one. Our token counter assumes about 30% more tokens than GPT for current Claude Sonnet and Opus models when it estimates.

Because API prices are per token, this changes real costs: two models with the same price per million tokens can cost different amounts for the same prompt.

## GPT (OpenAI): count locally

OpenAI publishes its tokenizers, so you can count exactly on your own machine, with no API call.

In Python, with the `tiktoken` library:

```python
import tiktoken
enc = tiktoken.get_encoding("o200k_base")
print(len(enc.encode("Your text here")))
```

In JavaScript, with `js-tiktoken`:

```js
import { getEncoding } from "js-tiktoken";
const enc = getEncoding("o200k_base");
console.log(enc.encode("Your text here").length);
```

`o200k_base` is the encoding behind GPT-4o and later models. The newest GPT models may differ slightly, so treat local counts for them as a very close estimate. Chat requests also add a few tokens per message for formatting.

## Claude (Anthropic): use the token counting endpoint

Claude's current tokenizer is not published as a library, but Anthropic's API has a **token counting endpoint** that returns the exact number of input tokens for a message, including system prompt, tools and images, before you send it. Anthropic makes it free to use, subject to rate limits. In the Python SDK, it is `client.messages.count_tokens(...)` with the same arguments you would pass to `messages.create`.

After a real request, every API response also reports the exact input and output tokens used, under `usage`.

## Gemini (Google): use countTokens

The Gemini API has a `countTokens` method that returns the token count for a prompt without generating anything. Like Anthropic's endpoint, it uses the real tokenizer, and responses from real requests include `usageMetadata` with the exact counts.

## Quick estimates without code

If you just want to know roughly how many tokens your text is, and what it costs:

1. Paste it into the [TokenSave token counter](/).
2. GPT models are counted with the real o200k tokenizer, running in your browser.
3. Claude, Gemini and other models show an estimate calibrated on real text, clearly marked as an estimate.
4. You see the cost on every model side by side, and nothing you paste is uploaded.

For English, a rough mental rule also works: about 1.1–1.3 tokens per word on current GPT models. See [Tokens per word, measured](/blog/tokens-per-word).

## Which count should you trust?

- **For budgeting:** a calibrated estimate is fine. Differences between models are usually smaller than the uncertainty in how much your app will be used.
- **For hard limits** (context window, maximum output, rate limits): use the provider's own counting method, because going one token over a limit causes an error.
- **For billing disputes or exact cost tracking:** use the `usage` numbers in the API responses. That is what you are billed for.

## Related

- [What is a token?](/blog/what-is-a-token)
- [LLM API pricing compared](/blog/llm-api-pricing-comparison)
- [How to estimate your AI API bill](/blog/how-to-estimate-ai-api-cost)
