![The Cheapest LLM APIs in 2026, Ranked by Real Cost per Request](/cheapest-llm-api-en.jpg)

If you only need the lowest bill, the cheapest LLM API in October 2026 is **GPT-5 nano**, followed by **GPT-6 Luna** and **Qwen 3.8 Flash**. But the cheapest model is rarely the right one for every job. Here is every major model ranked by what a real request costs, which cheap models are worth using, and where paying more saves money.

## How we ranked them

Price per million tokens is misleading on its own, for two reasons:

- **Output costs 200 to 700% more than input** on most models, so a model with cheap input and expensive output can lose to one with the opposite.
- **Tokenizers differ.** The same English text is about 30% more tokens on Claude Opus and Sonnet than on GPT, and about 5% fewer on Gemini. A "$2 per million" Claude model costs more per request than a "$2 per million" GPT model.

So we priced one typical request: **2,000 input tokens and 500 output tokens of English**, counted the way each model's tokenizer would count it, at official list prices checked October 1, 2026. No caching or batch discounts.

## The cheapest LLM APIs

![The cheapest LLM APIs: Model, Maker, Input / output per 1M, 1 request, 10,000 requests](/cheapest-llm-api-the-cheapest-llm-apis-en.jpg)

| Model | Maker | Input / output per 1M | 1 request | 10,000 requests |
|---|---|---|---:|---:|
| GPT-5 nano | OpenAI | $0.05 / $0.40 | $0.00030 | $3.00 |
| GPT-6 Luna | OpenAI | $0.10 / $0.50 | $0.00045 | $4.50 |
| Qwen 3.8 Flash | Qwen | $0.15 / $0.47 | $0.00053 | $5.35 |
| GPT-4o mini | OpenAI | $0.15 / $0.60 | $0.00060 | $6.00 |
| Mistral Small | Mistral | $0.15 / $0.60 | $0.00063 | $6.30 |
| Gemini 3.1 Flash-Lite | Google | $0.25 / $1.50 | $0.00119 | $11.88 |
| DeepSeek V4.1 Flash (peak) | DeepSeek | $0.30 / $1.20 | $0.00120 | $12.00 |
| GPT-5 mini | OpenAI | $0.25 / $2.00 | $0.00150 | $15.00 |
| GPT-4.1 mini | OpenAI | $0.40 / $1.60 | $0.00160 | $16.00 |
| Gemini 3.5 Flash-Lite | Google | $0.30 / $2.50 | $0.00176 | $17.57 |
| Mistral Large 3 | Mistral | $0.50 / $1.50 | $0.00184 | $18.38 |

For comparison, the same 10,000 requests cost **$90** on GPT-6 Sol, **$117** on Claude Sonnet 5.5, **$234** on Claude Opus 5.5 and **$450** on GPT-6 Astra. The cheapest model in the table costs less than 1% of what GPT-6 Astra does.

## Which cheap model to pick

![Which cheap model to pick: GPT-6 Luna is the one to try first. It is the newest small model from OpenAI (September 2026), and only $1.50 ](/cheapest-llm-api-which-cheap-model-to-pick-en.jpg)

- **GPT-6 Luna** is the one to try first. It is the newest small model from OpenAI (September 2026), and only $1.50 per 10,000 requests more than GPT-5 nano. Good for classification, extraction, routing, short answers and summaries.
- **GPT-5 nano** for the very simplest, highest-volume work, where every fraction of a cent matters: tagging, yes/no checks, spam filtering.
- **Qwen 3.8 Flash** and **Mistral Small** are the cheapest non-OpenAI options, useful if you want a second provider or open-weight models you could later host yourself.
- **Gemini 3.1 Flash-Lite** and **DeepSeek V4.1 Flash** cost about 100% more than Luna but are a step up for writing and reasoning, and still about 87% cheaper than GPT-6 Sol per request. DeepSeek V4.1 Flash is half price outside peak hours ($0.15 / $0.60), which puts it right behind GPT-6 Luna; see [DeepSeek V4.1 Flash pricing](/blog/deepseek-v4-1-flash-api-pricing).
- **Claude Haiku 4.5** is the cheapest Claude model at $0.0047 per request, around 900% more than Luna. Pick it when you need Claude's behavior specifically, not for price.

## When the cheapest model costs more

A cheap model that fails costs you twice: once for the bad answer, and again for the retry on a better model, plus your time. Two patterns save more than picking the cheapest model everywhere:

1. **Route by difficulty.** Send everything to a small model first and escalate only the requests it gets wrong (or that you flag as hard) to GPT-6 Sol, Claude Sonnet or Gemini 3.1 Pro. If 80% of requests stay on GPT-6 Luna and 20% go to GPT-6 Sol, the average cost drops by about 75% compared with sending all of them to Sol.
2. **Cut the tokens, not just the price.** Prompt caching bills repeated instructions and documents at about a tenth of the input price on most providers, and batch APIs charge about half for work that can wait. See [Prompt caching explained](/blog/prompt-caching-explained) and [Batch APIs: half-price AI](/blog/batch-api-half-price).

## Your language changes the ranking

All the costs above are for English. Other languages use more tokens for the same meaning: Korean about 44% more and Japanese about 79% more on GPT, so every price in the table rises by the same share. The ranking stays the same; the bill does not. See [the same prompt in 41 languages](/blog/token-cost-by-language).

## Check your own prompt

Paste a real prompt into the [token counter](/) to see its exact token count and cost on every model, or open the [OpenAI](/openai-token-counter), [Claude](/claude-token-counter) or [Gemini](/gemini-token-counter) counter. For a full side-by-side of capability against price, see [AI model capability vs price](/compare/performance).

*Prices change often. Check the provider's pricing page before you commit to a model.*

## Sources

- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI: GPT-5 nano model](https://developers.openai.com/api/docs/models/gpt-5-nano)
- [Alibaba Cloud: qwen3.8-flash pricing](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-flash)
- [Mistral AI: Mistral Large 3](https://docs.mistral.ai/models/mistral-large-3-25-12)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [DeepSeek API models and pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing)
<!-- autoimg -->
