Claude Code is included in Anthropic's Claude Pro and Max subscriptions, and it can also run on pay-as-you-go API credits. So what does it actually cost per month? It depends on how much you use it, and the difference between the cheapest and the most expensive way to pay for the same work can be ten times or more. Here are the real numbers.

## Two ways to pay

**1. A subscription.** Claude Code is included in these plans (US prices, checked October 2026):

| Plan | Price per month | Usage |
|---|---|---|
| Pro | $20 ($17 with annual billing) | Base level |
| Max 5× | $100 | 5× the usage of Pro |
| Max 20× | $200 | 20× the usage of Pro |

You pay a flat price and get usage limits. Claude Code and the Claude app share the same limits.

**2. The API.** You pay per token at Anthropic's API prices:

| Model | Input / 1M tokens | Output / 1M tokens |
|---|---|---|
| Claude Haiku 4.5 | $1 | $5 |
| Claude Sonnet 5.5 | $2 | $10 |
| Claude Opus 5.5 | $4 | $20 |

Input that is read from the prompt cache costs about a tenth of the normal input price. There are no plan limits, only your account's rate limits, but every token is billed.

## Why Claude Code uses so many tokens

Claude Code works in steps: read files, edit, run tests, read the output, try again. At every step it sends its **whole working context** back to the model: instructions, tool definitions, the files it has read and everything that happened before. A single feature-sized task can easily send **1.6 million input tokens**, even if the code it writes is short.

**Prompt caching** is what keeps this affordable: the repeated part of the context is billed at about 10% of the normal input price. Claude Code uses it automatically.

## What one task costs on the API

Using our [coding agent cost model](/agents), with caching on:

| Task | Steps | Haiku 4.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|---|
| Small fix | ~8 | $0.08 | $0.15 | $0.31 |
| New feature | ~25 | $0.36 | $0.72 | $1.43 |
| Big refactor | ~60 | $1.33 | $2.65 | $5.30 |

Without caching, the same feature task on Sonnet would cost about $3.38 instead of $0.72.

## What a month costs

Assuming 22 working days:

| How you use it | Tasks per month | API with Sonnet | API with Opus | Cheapest plan that usually fits |
|---|---|---|---|---|
| Light: 3 small fixes a day | 66 | ~$10 | ~$20 | API or Pro ($20) |
| Regular: 5 features a day | 110 | ~$79 | ~$158 | Pro or Max 5× |
| Heavy: 15 features a day | 330 | ~$236 | ~$473 | Max 5× or Max 20× |
| Agents all day: 8 big tasks a day | 176 | ~$466 | ~$932 | Max 20× |

The pattern is clear:

- **Occasional use:** the API can be cheaper than any plan. You pay $10 for a month where Pro would cost $20.
- **Daily use:** a subscription quickly becomes much cheaper. A regular user on Opus would pay around $158 on the API versus $100 for Max 5×.
- **Heavy use:** Max is far cheaper than the API, as long as the usage limits are enough.

The catch with plans is the limits. Anthropic does not publish exact token numbers for each plan, and heavy users hit the weekly cap. See [Claude Code usage limits explained](/blog/claude-code-usage-limits).

## Converting tokens to dollars

A quick rule for Claude Sonnet 5.5:

- 1 million input tokens = $2 (or $0.20 if cached)
- 1 million output tokens = $10

Because most of what Claude Code sends is cached context, a realistic blended price for agent work on Sonnet is usually well under $1 per million total tokens processed. For Opus, double it.

## How to decide

1. **Start on Pro** if you code with it a few times a week.
2. **Watch how often you hit the limit.** If you hit it most weeks, Max 5× is likely cheaper than paying the API rate for the extra work.
3. **Use the API** for automation, CI pipelines, or very irregular use, where predictable per-token billing beats a monthly fee.
4. **Choose the model per task.** Sonnet handles most coding work; Opus costs twice as much per token.

## Estimate your own month

The [coding agent cost calculator](/agents) lets you set task size, tasks per day and working days, and compares API costs for Claude, GPT and Gemini models with every Claude and ChatGPT plan. To spend fewer tokens either way, see [How to save tokens in Claude Code](/blog/claude-code-save-tokens).

*Prices and limits change often. Check [claude.com/pricing](https://claude.com/pricing) before you decide.*
