![GPT-6.1 Sol Ultrafast: Price, Speed and When It's Worth It](/gpt-6-1-sol-ultrafast-pricing-en.jpg)

GPT-6.1 Sol **Ultrafast** is a much faster mode for GPT-6.1 Sol. OpenAI started rolling it out on October 8, 2026 in the API, Codex and ChatGPT Work. API pricing is **$12 per million input tokens and $60 per million output tokens**: 500% more than standard GPT-6.1 Sol ($2 / $10) and 20% more than GPT-6 Astra ($10 / $50). Here is how fast it is, what a real request costs, and when it is worth it.

## What GPT-6.1 Sol Ultrafast is

OpenAI describes Ultrafast as near-Astra intelligence at speeds up to 700% faster than standard Sol. WinCentral reported a figure of about 300 tokens per second. Both are OpenAI's claim and press reports; real speed depends on request length and load.

OpenAI presents Ultrafast as a processing mode of GPT-6.1 Sol, not a new model. You pick the same model and choose a mode with a different speed and price.

## Pricing: Standard vs Fast vs Ultrafast

![Pricing: Standard vs Fast vs Ultrafast: Mode, Input, Cached input, Output](/gpt-6-1-sol-ultrafast-pricing-pricing-standard-vs-fast-vs-ultrafast-en.jpg)

Price per million tokens, from OpenAI's pricing page.

| Mode | Input | Cached input | Output |
|---|---:|---:|---:|
| GPT-6.1 Sol Standard | $2.00 | $0.10 | $10.00 |
| GPT-6.1 Sol Fast | $4.00 | $0.20 | $20.00 |
| **GPT-6.1 Sol Ultrafast** | **$12.00** | **$0.60** | **$60.00** |
| GPT-6 Astra (Standard) | $10.00 | $1.00 | $50.00 |

- **Fast** costs 100% more than Standard (per OpenAI's model page).
- **Ultrafast** costs 500% more than Standard. Cached input rises by the same share, to $0.60.
- Prompts over 272,000 input tokens get a surcharge on the whole request. The pricing table shows $24 input and $90 output on what appears to be the Ultrafast row, but the table does not name the mode, so treat that as an estimate.

## What it costs in practice

![What it costs in practice: Mode, 1 request, 10,000 a month](/gpt-6-1-sol-ultrafast-pricing-what-it-costs-in-practice-en.jpg)

A **typical request** of 2,000 input tokens and 500 output tokens, no caching:

| Mode | 1 request | 10,000 a month |
|---|---:|---:|
| GPT-6.1 Sol Standard | $0.009 | $90 |
| GPT-6.1 Sol Fast | $0.018 | $180 |
| **GPT-6.1 Sol Ultrafast** | **$0.054** | **$540** |
| GPT-6 Astra | $0.045 | $450 |

A **coding agent step** re-reads the earlier conversation, so most input is cached. With 50,000 input tokens, 45,000 of them cached, and 1,000 output tokens:

| Mode | Cost per step |
|---|---:|
| GPT-6.1 Sol Standard | $0.0245 |
| GPT-6.1 Sol Fast | $0.049 |
| **GPT-6.1 Sol Ultrafast** | **$0.147** |
| GPT-6 Astra | $0.145 |

Arithmetic: Ultrafast = 5,000 new input × $12 + 45,000 cached × $0.60 + 1,000 output × $60, all per million tokens. For agent work, Ultrafast and Astra cost almost the same (about 1% apart). At the same price, the choice is whether you need Astra's intelligence or 6.1 Sol's speed.

## Where and who can use it

![Where and who can use it: API; Codex and ChatGPT Work; Regions](/gpt-6-1-sol-ultrafast-pricing-where-and-who-can-use-it-en.jpg)

- **API:** choose the Ultrafast mode on GPT-6.1 Sol. OpenAI's docs describe a WebSocket connection, with an HTTP option as well.
- **Codex and ChatGPT Work:** available on **Pro 500**, usage-based **Enterprise** (admins must enable it) and credit-based **Edu** plans. Not on Pro 100, Pro 200 or Plus.
- **Regions:** all supported regions, including US and EU data residency.

## Pros and cons

**Pros**

- **Much less waiting.** Long code or documents arrive up to 700% faster, per OpenAI.
- **Near-Astra performance at an Astra-like price:** on cache-heavy agent work the cost is almost the same as Astra.
- **Built for work someone is watching.** OpenAI's examples are debugging outages, agents navigating apps and live experiences.

**Cons**

- **Expensive.** At 500% more than standard GPT-6.1 Sol, using it for work that can wait just costs more.
- **Pro 500 in ChatGPT:** individuals need the $500 a month plan to use it in Codex and Work.
- **Speed is a "up to" claim.** Measure it on your own tasks before relying on it.

## When to use Ultrafast

- **Use it:** when a person is waiting on the result, for live chat or voice products, during incidents where minutes matter, or for long agent runs you need to finish quickly.
- **Skip it:** for overnight batch jobs, bulk summarizing or classification, and products where response time barely matters. Standard mode or the [Batch API](/blog/batch-api-half-price) is far cheaper there.

## FAQ

**How much does GPT-6.1 Sol Ultrafast cost?**
In the API, $12 per million input tokens, $0.60 cached input and $60 output: 500% more than standard GPT-6.1 Sol.

**Can I use it on ChatGPT Plus or Pro 100?**
No. In Codex and ChatGPT Work it is available on Pro 500, usage-based Enterprise and credit-based Edu plans. In the API you pay per token on any account.

**How is it different from GPT-6 Astra?**
Astra is the smarter flagship model; Ultrafast is a faster mode of 6.1 Sol. On cache-heavy agent work the two cost almost the same, so choose by whether intelligence or speed matters more.

## Calculate it with your own prompt

Paste a prompt into the [token counter](/) to see its cost on GPT-6.1 Sol and 30+ other models. To decide between a plan and the API for Codex, see [ChatGPT Pro 100 vs 200 vs 500](/blog/chatgpt-pro-100-vs-200-vs-500) and the [coding agent cost calculator](/agents).

*Prices checked October 9, 2026. Pricing and availability change often; check OpenAI's pricing page before you rely on them.*

## Sources

- [OpenAI Developer Community: Ultrafast rolling out for GPT-6.1 Sol (October 8, 2026)](https://community.openai.com/t/ultrafast-is-rolling-out-today-for-gpt-6-1-sol-in-the-api-codex-and-chatgpt-work/1404475)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI: GPT-6.1 Sol model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
- [OpenAI: GPT-6 Astra model page](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [WinCentral: GPT-6.1 Sol Ultrafast speed report](https://thewincentral.com/gpt-6-1-sol-ultrafast-openai-dots-ai-agents/)
<!-- autoimg -->
