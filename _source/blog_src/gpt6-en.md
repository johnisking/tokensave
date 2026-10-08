![GPT-6 API Pricing: Astra vs Sol vs Luna, and What It Costs](/gpt-6-api-pricing-en.jpg)

OpenAI released three GPT-6 models in September 2026: **GPT-6 Astra**, the flagship, on September 4, and **GPT-6 Sol** and **GPT-6 Luna** on September 22. Their API prices are very different, so picking the right one matters far more than any discount. Here are the prices, what they mean for real workloads, and how they compare with Claude and Gemini.

## GPT-6 API prices

![GPT-6 API prices: Model, Input, Cached input, Output](/gpt-6-api-pricing-gpt-6-api-prices-en.jpg)

Per million tokens:

| Model | Input | Cached input | Output |
|---|---|---|---|
| GPT-6 Astra | $10 | $1 | $50 |
| GPT-6 Sol | $2 | $0.20 | $10 |
| GPT-6 Luna | $0.10 | $0.01 | $0.50 |

Astra costs 400% more than Sol. Luna is far cheaper again: $0.10 input and $0.50 output per million tokens, against $10 and $50 for Astra, in the same model family.

Requests with more than 272,000 input tokens are billed at a higher rate, so very long contexts cost more than this table suggests.

## How that compares with GPT-5.6

Sol and Luna launched at 50% less than the price of the models they replace. GPT-5.6 Sol was $4 input and $20 output; GPT-5.6 Luna was $0.20 and $1.20. If you are still on GPT-5.6, switching model names alone cuts the bill by 50%.

## What it costs in practice

![What it costs in practice: Model, One request, 10,000 requests](/gpt-6-api-pricing-what-it-costs-in-practice-en.jpg)

A typical request with 2,000 input tokens and 500 output tokens:

| Model | One request | 10,000 requests |
|---|---|---|
| GPT-6 Luna | $0.00045 | $4.50 |
| Gemini 3.8 Flash | $0.0034 | $34 |
| GPT-6 Sol | $0.009 | $90 |
| Claude Sonnet 5.5 | $0.009 | $90 |
| Gemini 3.1 Pro | $0.010 | $100 |
| Claude Opus 5.5 | $0.018 | $180 |
| GPT-6 Astra | $0.045 | $450 |

Prices for the other models are list API prices checked October 1, 2026.

GPT-6 Sol costs exactly the same per token as Claude Sonnet 5.5. GPT-6 Astra costs 150% more than Claude Opus 5.5.

## Which GPT-6 model should you use?

**GPT-6 Luna** for high-volume, simple work: classification, extraction, routing, short answers, summaries of short texts. At $0.10 per million input tokens it is cheap enough to run on every request.

**GPT-6 Sol** as the default for most apps and coding work: chat assistants, writing, analysis, agents. It is the sensible middle.

**GPT-6 Astra** only where you can measure that it does better: long, multi-step agent work, hard reasoning, tasks where a mistake is expensive. Route only those requests to it.

A common setup is to send everything to Sol or Luna by default and escalate to Astra when a cheaper model fails or the task is flagged as hard.

## Ways to pay less

![Ways to pay less: Use prompt caching. Cached input is 90% cheaper than the normal price on all three models. Put fixed instructi](/gpt-6-api-pricing-ways-to-pay-less-en.jpg)

1. **Use prompt caching.** Cached input is 90% cheaper than the normal price on all three models. Put fixed instructions and documents at the start of the prompt. See [Prompt caching explained](/blog/prompt-caching-explained).
2. **Use the Batch API** for work that can wait, typically at 50% off. See [Batch APIs](/blog/batch-api-half-price).
3. **Keep output short.** Output costs 400% more than input on every GPT-6 model.
4. **Watch reasoning.** Hidden reasoning tokens are billed as output. Use the lowest reasoning effort that works. See [Reasoning models](/blog/reasoning-models-cost).
5. **Write prompts in English.** On the GPT tokenizer, the same prompt uses about 44% more tokens in Korean and 79% more in Japanese than in English.

## GPT-6 in ChatGPT plans

You do not need the API to use GPT-6. GPT-6 Astra is available to ChatGPT Pro, Business Premium and Enterprise users, and is rolling out to Plus, first in ChatGPT's Work section and Codex. For heavy use, a plan can be much cheaper than paying Astra's API rate. Compare in the [Subscription vs API calculator](/plans).

## Calculate your own cost

Paste a typical prompt into the [token counter](/) to see its exact token count on GPT models and its cost on every GPT-6 model, Claude and Gemini side by side.

*Prices change. Check [OpenAI's pricing page](https://openai.com/api/pricing/) before a large job.*

## Sources

- [OpenAI: GPT-6 Astra model and pricing](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [OpenAI: GPT-6 Sol model and pricing](https://developers.openai.com/api/docs/models/gpt-6-sol)
- [OpenAI: GPT-6 Luna model and pricing](https://developers.openai.com/api/docs/models/gpt-6-luna)
- [OpenAI: Introducing GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/)
- [Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
<!-- autoimg -->
