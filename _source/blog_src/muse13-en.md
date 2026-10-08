![Muse Spark 1.3 API Pricing: Meta's Model vs Claude, GPT-6 and Gemini](/muse-spark-1-3-api-pricing-en.jpg)

Meta's Muse Spark 1.3 is available on the Meta Model API at **$1.25 per million input tokens and $4.25 per million output tokens**, with cached input at $0.15. There is no long-context surcharge on its 1M-token context window. Meta also offers a much cheaper "contributor" version that lets Meta train on your data. Here is what Muse Spark 1.3 costs next to Claude Sonnet 5.5, GPT-6 Sol, Gemini 3.1 Pro, DeepSeek and Grok.

## Muse Spark 1.3 API pricing

![Muse Spark 1.3 API pricing: Model name, Input, Cached input, Output](/muse-spark-1-3-api-pricing-muse-spark-1-3-api-pricing-en.jpg)

Per million tokens, from Meta's official pricing page:

| Model name | Input | Cached input | Output |
|---|---:|---:|---:|
| `muse-spark-1.3` (standard) | $1.25 | $0.15 | $4.25 |
| `muse-spark-1.3-contributor` | $0.10 | $0.002 | $0.20 |

- **Same price for 1.1, 1.2 and 1.3.** Meta says the standard versions share one price, so upgrading costs nothing extra.
- **No long-context premium.** You pay the same rate whether the 1M-token window is nearly empty or almost full.
- **Contributor tier:** Meta uses your prompts and completions to train future models. It is cheap, but do not send private or customer data to it.
- **Rate limits (standard):** 3,000 requests and 4,000,000 tokens per minute per team.

## Muse Spark 1.3 vs other models

![Muse Spark 1.3 vs other models: Model, Input, Output](/muse-spark-1-3-api-pricing-muse-spark-1-3-vs-other-models-en.jpg)

List prices per million tokens:

| Model | Input | Output |
|---|---:|---:|
| **Muse Spark 1.3** | $1.25 | $4.25 |
| DeepSeek V4 Pro | $1.32 | $3.96 |
| Grok 4.7 | $2.00 | $6.00 |
| GPT-6 Sol | $2.00 | $10.00 |
| Claude Sonnet 5.5 | $2.00 | $10.00 |
| Gemini 3.1 Pro | $2.00 | $12.00 |

## What it costs on real work

A typical request here is 2,000 input tokens and 500 output tokens. Prices include each model's tokenizer difference on the same English text (Claude uses about 30% more tokens; Meta's tokenizer is not public, so we treat it like GPT's).

| Task | Muse Spark 1.3 | Claude Sonnet 5.5 | GPT-6 Sol | Gemini 3.1 Pro | DeepSeek V4 Pro | Grok 4.7 |
|---|---:|---:|---:|---:|---:|---:|
| One typical request | $0.0046 | $0.0117 | $0.0090 | $0.0095 | $0.0046 | $0.0070 |
| 10,000 requests a month | $46 | $117 | $90 | $95 | $46 | $70 |

- On this request, Claude Sonnet 5.5 costs **153% more** than Muse Spark 1.3, GPT-6 Sol **95% more**, and Gemini 3.1 Pro **105% more**.
- DeepSeek V4 Pro costs about the same. Grok 4.7 costs **51% more**.

## What Meta says it is good at

According to Meta, Muse Spark 1.3 is trained for long, multi-step agent work and tuned for coding, with "fewer unnecessary turns and cleaner output." Meta also says it reads images, video and documents natively. These are Meta's claims; test it on your own tasks before you switch.

## Strengths and weaknesses

![Muse Spark 1.3 strengths and weaknesses: low price, 1M context, coding gains vs verbose output, trails Claude Opus 5 on agent tasks](/muse-spark-1-3-pros-cons-en.jpg)

**Strengths**

- **Price:** $1.25 / $4.25 per million tokens, below Claude Sonnet 5.5 and GPT-6 Sol.
- **Long context:** 1M tokens with no surcharge. On Meta's long-context recall test (MRCR, 512K–1M tokens) it scores 98.1, against 73.8 for GPT-5.6 Sol.
- **Coding:** Meta reports DeepSWE v1.1 at 75.4 (up from 55.0 on 1.2) and Terminal-Bench 2.1 at 88.8, the same as GPT-5.6 Sol. Meta's engineers saw about 20% fewer tool calls and 25% fewer tokens than 1.2 on the same tasks.
- **Independent ranking:** at its max setting it scores 62 on the Artificial Analysis Intelligence Index, 6th of 636 models.

**Weaknesses**

- **Verbose:** Artificial Analysis measured 120 million output tokens to finish its index, against a median of 72 million. That is about **67% more output**, so your real bill can be higher than the per-token price suggests. Measure it on your own prompts.
- **Not first on agent tasks:** in Meta's own table, Claude Opus 5 is slightly ahead on agent benchmarks such as OSWorld 2.0 (68.3 vs 66.9), and GPT-5.6 Sol leads on search and instruction following.
- **Max mode came later:** the max reasoning mode behind the top score was held back for safety testing at launch; the generally available xhigh setting scores 61.
- **No visible reasoning:** it does not show its thinking, which some users find harder to debug.
- **Closed model, one provider:** no open weights, and Meta is the only host.

## Should you switch?

![Should you switch?: On Claude Sonnet 5.5, GPT-6 Sol or Gemini 3.1 Pro for cost; On DeepSeek V4 Pro; For non-sensitive bulk jobs](/muse-spark-1-3-api-pricing-should-you-switch-en.jpg)

- **On Claude Sonnet 5.5, GPT-6 Sol or Gemini 3.1 Pro for cost:** Muse Spark 1.3 is a lot cheaper per request. Run a small test on your real prompts and compare quality.
- **On DeepSeek V4 Pro:** the price is about the same, so choose on quality, speed and where your data is processed.
- **For non-sensitive bulk jobs:** the contributor tier ($0.10 / $0.20) is one of the cheapest options, as long as you are fine with Meta training on that data.
- **Using it in Cursor:** Cursor lists Muse Spark 1.3 at the same $1.25 / $4.25 in its "other models" pool.

## Check your own prompt

Paste your prompt into the [token counter](/) to see its cost on Muse Spark 1.3 and 30+ other models, or compare [Muse Spark 1.3 vs Claude Sonnet 5.5](/compare/muse-spark-1-3-vs-claude-sonnet-5-5) side by side.

*Prices checked October 9, 2026. Check Meta's pricing page before you commit.*

## Sources

- [Meta Model API: Pricing and rate limits](https://dev.meta.ai/docs/pricing-rate-limits)
- [Meta Model API: Muse Spark 1.3](https://dev.meta.ai/models/muse-spark)
- [Cursor: Models & Pricing](https://cursor.com/docs/models-and-pricing)
- [Artificial Analysis / eesel: Muse Spark 1.3 review](https://www.eesel.ai/blog/meta-muse-spark-13-review)
- [DataCamp: Muse Spark 1.3](https://www.datacamp.com/blog/muse-spark-1-3)
<!-- autoimg -->
