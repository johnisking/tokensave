![Prompt Caching Explained: Cut Repeated Input Costs by Around 90%](/prompt-caching-explained-en.jpg)

If your app sends the same long instructions, documents or tool definitions with every request, you are paying full price for text the model has already seen. **Prompt caching** fixes that. It is the single biggest cost saving available on most AI APIs, often cutting the price of repeated input by around 90%, and it needs only a small change in how you build your prompts.

## What prompt caching does

When a model processes a prompt, it does a lot of computation on every token before it starts writing. If the next request begins with exactly the same text, the provider can keep the result of that computation and reuse it instead of doing it again.

Providers pass that saving on: tokens read from the cache are billed at a fraction of the normal input price. Discounts of about 90% (paying around 10% of the normal price) are common, though the exact rate depends on the provider and model.

## The one rule: the cached part must be an identical prefix

![The one rule: the cached part must be an identical prefix: System instructions (never change); Tool definitions (never change); Reference documents (change rarely)](/prompt-caching-explained-the-one-rule-the-cached-part-must-be-an-en.jpg)

Caching works on the **beginning** of the prompt. The provider looks for the longest stretch from the very first token that exactly matches a recent request. As soon as one token differs, everything after it is processed and billed normally.

That means order matters:

**Cache-friendly** — fixed content first, changing content last:

1. System instructions (never change)
2. Tool definitions (never change)
3. Reference documents (change rarely)
4. Conversation history (grows, but the earlier part stays the same)
5. The user's new message (always new)

**Cache-breaking** — a timestamp, user name or random ID at the top of the system prompt. Because the first line differs every time, nothing after it can be reused.

## A worked example

![A worked example: Fixed part billed, Cost per hour](/prompt-caching-explained-a-worked-example-en.jpg)

A support assistant has 10,000 tokens of fixed instructions and product documentation, followed by a short question. It answers 1,000 questions an hour. Input price: $2 per million tokens (GPT-6 Sol, checked October 1, 2026).

| | Fixed part billed | Cost per hour |
|---|---|---|
| Without caching | 1,000 × 10,000 tokens at $2/M | $20.00 |
| With caching (90% off cached reads) | 1 full read + 999 cached reads at $0.20/M | about $2.02 |

Over a month of steady traffic, that is the difference between roughly $14,600 and $1,500 for the fixed part of the prompt alone.

## Details that vary by provider

![Details that vary by provider: Automatic or explicit. Some providers cache automatically whenever a prefix repeats. Others need you to mark w](/prompt-caching-explained-details-that-vary-by-provider-en.jpg)

Caching works differently on each platform, so check the documentation for the one you use. Things to look for:

- **Automatic or explicit.** Some providers cache automatically whenever a prefix repeats. Others need you to mark where the cached part ends.
- **Minimum length.** Very short prompts are usually not cached. A common minimum is around 1,000 tokens.
- **How long it lasts.** Caches typically expire after a few minutes without use. Some providers offer longer lifetimes, sometimes for an extra fee.
- **Write cost.** Some providers charge a little more than the normal price the first time a prefix is written to the cache, then much less for every read.
- **Output is never cached.** The discount applies to input tokens only.

## Where caching helps most

- **Chatbots with long system prompts**, especially when the same instructions go out with every message.
- **Multi-turn conversations**, where each message re-sends all earlier turns. With caching, only the newest turn is billed at full price.
- **Coding agents**, which resend the same files and tool definitions on every step. Our [agent cost calculator](/agents) shows that caching cuts a typical task's cost by roughly four-fifths.
- **Question answering over a fixed document**, such as a manual or contract, where many questions share the same long context.

## Where it does not help

- One-off requests with no repeated prefix.
- Prompts where the long part changes every time, such as summarizing a different document per request.
- Traffic so sparse that the cache expires between requests.

## A checklist

1. Move everything that changes per request (dates, names, IDs, the user's message) to the end of the prompt.
2. Keep system prompts and tool definitions byte-for-byte identical across requests. Even a changed space breaks the match.
3. Put shared documents before per-user content.
4. Check your API responses: most providers report how many input tokens were read from the cache. If that number is zero, something at the top of your prompt is changing.
5. For low-traffic apps, see whether a longer cache lifetime is available and worth it.

## Related

- [How to estimate your AI API bill](/blog/how-to-estimate-ai-api-cost)
- [Context windows explained](/blog/context-window-explained)
- [What does an AI coding agent cost per task?](/blog/ai-coding-agent-cost)

## Sources

- [Prompt caching guide (OpenAI)](https://developers.openai.com/api/docs/guides/prompt-caching)
- [Prompt caching (Claude docs)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [Gemini context caching (Google)](https://ai.google.dev/gemini-api/docs/caching)
- [GPT-6 Sol model page (OpenAI)](https://developers.openai.com/api/docs/models/gpt-6-sol)
<!-- autoimg -->
