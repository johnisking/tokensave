![Gemini 4 Argon API Pricing: Cost vs GPT-6 and Claude](/gemini-4-argon-api-pricing-en.jpg)

Google announced **Gemini 4 Argon** on September 30, 2026, its new top model. It is built for coding, cybersecurity and long agentic workflows, and Google says it beats GPT-6 Astra and Claude Fable and Opus on a range of benchmarks. Here is what it costs on the API, what a real request costs, and how it compares with GPT and Claude.

## Gemini 4 Argon API pricing

![Gemini 4 Argon API pricing: Rate, Input, Cached input, Output](/gemini-4-argon-api-pricing-gemini-4-argon-api-pricing-en.jpg)

Prices per million tokens. It starts at an introductory rate and moves to the standard rate later.

| Rate | Input | Cached input | Output |
|---|---|---|---|
| Introductory | $2 | ~$0.10 | $10 |
| Standard | $4 | ~$0.20 | $20 |

Cached input is 95% off the normal input price, which matters a lot when you resend the same instructions or documents. Google has not said how long the introductory rate lasts.

Argon can also **output up to 1 million tokens** in a single response. Long outputs cost accordingly: 1 million output tokens is $20 per response at the standard rate.

## Can you use it yet?

Not yet. For now it is limited to partners in Google's Fairwind cyber-defense program, with a rollout to Google AI Ultra subscribers and paid API customers coming next. The API model ID is reported as `gemini-4-argon`, but it is not in the public docs yet.

## How it compares

![How it compares: Model, Per 1M tokens (in/out), 1 request, 10,000 requests](/gemini-4-argon-api-pricing-how-it-compares-en.jpg)

A typical request: 2,000 input tokens and 500 output tokens.

| Model | Per 1M tokens (in/out) | 1 request | 10,000 requests |
|---|---|---|---|
| Gemini 3.8 Flash | $0.75 / $3.75 | $0.0034 | $34 |
| **Gemini 4 Argon (intro)** | $2 / $10 | $0.009 | $90 |
| GPT-6 Sol | $2 / $10 | $0.009 | $90 |
| Claude Sonnet 5.5 | $2 / $10 | $0.009 | $90 |
| Gemini 3.1 Pro | $2 / $12 | $0.010 | $100 |
| **Gemini 4 Argon (standard)** | $4 / $20 | $0.018 | $180 |
| Claude Opus 5.5 | $4 / $20 | $0.018 | $180 |
| GPT-6 Astra | $10 / $50 | $0.045 | $450 |
| Claude Fable 5.1 | $10 / $50 | $0.045 | $450 |

Other prices are official API prices checked in October 2026.

What stands out:

- **The standard price matches Claude Opus 5.5 exactly:** $4 in, $20 out.
- **The introductory price matches GPT-6 Sol and Claude Sonnet 5.5.** A top model at a mid-tier price, for now.
- **Even at the standard price it is 60% cheaper than GPT-6 Astra and Claude Fable 5.1.** If Google's benchmark claims hold, it is the best value among the top models.
- **It costs more than Gemini 3.1 Pro**, about 80% more per request at the standard price. If 3.1 Pro already does the job, there is no reason to switch.

## When to use it

**Good fit:** large code changes and migrations, security reviews, long multi-step agent runs, and analysis of long videos or charts. The more a mistake costs you, the more it is worth paying for.

**Overkill:** summaries, translation, classification and short answers. Gemini 3.8 Flash handles those at about 80% less cost per request.

A common setup is to send everyday requests to Flash or 3.1 Pro and route only the hard ones to Argon.

## How to spend less

![How to spend less: Test during the introductory period. It is half the standard price, the best time to see if it fits your workl](/gemini-4-argon-api-pricing-how-to-spend-less-en.jpg)

1. **Test during the introductory period.** It is half the standard price, the best time to see if it fits your workload.
2. **Use caching.** Cached input is 95% off, so keep fixed instructions and documents at the start of the prompt.
3. **Cap the output.** It can write up to 1 million tokens, and output costs 400% more than input. Ask for only what you need.
4. **Write prompts in English.** Most other languages take more tokens for the same text. The 💸 Save tokens button in the [token counter](/) rewrites a prompt in English on your own device.

## Check your own cost

Gemini 4 Argon is now in the [token counter](/) at the standard price. Paste a prompt you actually use and compare Argon, GPT-6 and Claude side by side.

*Prices and rollout dates can change. Check the [Gemini API pricing page](https://ai.google.dev/gemini-api/docs/pricing) before large jobs.*

## Sources

- [Google: Gemini 4 Argon announcement](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing)
<!-- autoimg -->
