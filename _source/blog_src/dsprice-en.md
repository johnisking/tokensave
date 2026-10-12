![DeepSeek API Pricing 2026: Official Rates, Peak Hours, API Key](/deepseek-api-pricing-en.jpg)

DeepSeek's API lineup and prices changed several times in 2026, and many pages that rank for it still show models that no longer exist. DeepSeek retired `deepseek-chat` and `deepseek-reasoner` in July, added peak and off-peak prices in August, and cut prices again with V4.1 Flash in September. This guide takes DeepSeek's prices and rules from its own documentation, checked October 12, 2026: the current models and rates, when the cheaper hours are, how to get an API key, how DeepSeek counts tokens, and what typical workloads cost compared with GPT-6, Claude and Grok.

## DeepSeek API pricing (official, October 2026)

![DeepSeek API pricing (official, October 2026): Model ID, Version, Cache hit input, Cache miss input, Output](/deepseek-api-pricing-deepseek-api-pricing-official-october-20-en.jpg)

DeepSeek's pricing page lists two models. Prices are per 1 million tokens:

| Model ID | Version | Cache hit input | Cache miss input | Output |
|---|---|---:|---:|---:|
| `deepseek-flash` (off-peak) | V4.1 Flash | $0.003 | $0.15 | $0.60 |
| `deepseek-flash` (peak) | V4.1 Flash | $0.006 | $0.30 | $1.20 |
| `deepseek-v4-pro` (off-peak) | V4 Pro (0813) | $0.022 | $0.66 | $1.98 |
| `deepseek-v4-pro` (peak) | V4 Pro (0813) | $0.044 | $1.32 | $3.96 |

- **Both models have a 1 million token context window** and up to 384K tokens of output.
- **Cache hits are the big saving.** On Flash, a cached input token costs 98% less than a fresh one. DeepSeek caches repeated prompt prefixes automatically, so a long system prompt or a document you ask several questions about gets cheaper after the first request.
- **Thinking mode is the default.** Both models can also run in non-thinking mode. Thinking mode generates reasoning tokens before the answer, which add to the tokens you pay for.
- **Features:** JSON output, tool calls, the Responses API, an Anthropic-compatible API and chat prefix completion (beta) on both models. Fill-in-the-middle (beta) works in non-thinking mode only. Image input works on Flash only. DeepSeek's API doesn't generate images; to price image generation on other providers, use the [AI image cost calculator](/image).
- **Old model names still work.** `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` now run on V4.1 Flash and are billed at Flash prices.

For a closer look at the Flash model alone, see [DeepSeek V4.1 Flash API pricing](/blog/deepseek-v4-1-flash-api-pricing).

### A note on V4 Pro

DeepSeek's documents don't fully agree on Pro. The September 10 announcement says requests to `deepseek-v4-pro` would be served by V4.1 Flash at Flash prices from September 14 until a V4.1 Pro is released. The change log says Pro service continues with billing unchanged, and the pricing page still lists V4 Pro at the prices above. Until DeepSeek clarifies, check the `model` field and the cost in your usage records if you call Pro.

## Peak and off-peak hours

![Peak and off-peak hours: Time zone, Peak windows (Monday–Friday)](/deepseek-api-pricing-peak-and-off-peak-hours-en.jpg)

Since August 16, 2026, DeepSeek charges half price outside peak hours. The peak windows are:

- **Monday to Friday, 01:00–04:00 UTC and 06:00–10:00 UTC**
- Chinese public holidays are off-peak all day.
- Everything else, including all of Saturday and Sunday, is off-peak.

| Time zone | Peak windows (Monday–Friday) |
|---|---|
| UTC | 01:00–04:00 and 06:00–10:00 |
| US Eastern (EDT, UTC−4) | 21:00–00:00 and 02:00–06:00 (starting the evening before) |
| US Pacific (PDT, UTC−7) | 18:00–21:00 and 23:00–03:00 (starting the evening before) |
| Central Europe (CEST, UTC+2) | 03:00–06:00 and 08:00–12:00 |
| India (IST, UTC+5:30) | 06:30–09:30 and 11:30–15:30 |
| Korea and Japan (UTC+9) | 10:00–13:00 and 15:00–19:00 |

- **Peak is 7 hours on each weekday.** That is 35 of the week's 168 hours, so about 79% of the week is off-peak.
- **For US users, peak falls overnight.** A US-based app with daytime traffic pays off-peak prices for most of its requests.
- **For East Asia, peak falls in the working day.** A team in Korea, Japan or China working office hours pays peak prices for much of its traffic.
- **Batch jobs are easy to move.** If a nightly job can run on a weekend or outside the windows above, it costs half as much.
- **Daylight saving shifts the local times.** The UTC windows stay fixed; the US and European times above move by an hour when clocks change.

## DeepSeek API pricing changes in 2026

| Date | Change |
|---|---|
| April 24, 2026 | V4 Pro and V4 Flash released |
| July 24, 2026 | `deepseek-chat` and `deepseek-reasoner` retired |
| August 13, 2026 | V4 Pro generally available; peak and off-peak pricing announced |
| August 16, 2026 | Off-peak half price takes effect (16:00 UTC) |
| August 21, 2026 | V4 Flash Vision (experimental) released |
| September 10, 2026 | V4.1 Flash released and API prices reduced (from 04:00 UTC) |

- **If a page lists V3, R1, `deepseek-chat` or `deepseek-reasoner` prices, it is out of date.** Those models no longer exist in the API.
- **DeepSeek's older platform page is also stale.** The marketing page at deepseek.com/en/platform still shows earlier V4 prices. The pricing page in the API docs is the one to trust.
- **DeepSeek says prices may change,** and it has changed them several times this year. Check the pricing page before committing to a budget.

## How DeepSeek counts tokens

DeepSeek's docs give a rule of thumb:

- **1 English character ≈ 0.3 tokens**
- **1 Chinese character ≈ 0.6 tokens**

The bill always uses the `usage` figures returned with each response, so the rule of thumb is only for estimates. In practice:

- **English text is about 3.3 characters per token.** A 1,000-word English document, at about 6,000 characters, is around 1,800 tokens.
- **A Chinese character counts as about 0.6 tokens,** 100% more than an English character, though one Chinese character often stands for a whole word.
- **Other languages vary.** DeepSeek doesn't publish a figure for Korean, Japanese or European languages. To see how different languages compare on GPT, Claude and Gemini, paste a sample into the [token counter](/), and see [tokens per word by language](/blog/tokens-per-word).

## How to get a DeepSeek API key

DeepSeek's quick-start guide makes this short:

1. **Create an account** on the DeepSeek platform (platform.deepseek.com).
2. **Add balance.** The API is prepaid. A request on an empty account returns error 402, "Insufficient Balance," and points you to the top-up page. Any granted balance is used before money you topped up.
3. **Create a key** on the API keys page of the platform. Store it somewhere safe, such as an environment variable, and never put it in client-side code.
4. **Call the API.** It is OpenAI-compatible, so you can use the OpenAI SDK with base URL `https://api.deepseek.com` and model `deepseek-flash` or `deepseek-v4-pro`. There is also an Anthropic-compatible endpoint at `https://api.deepseek.com/anthropic`, so tools built for the Anthropic API can point at DeepSeek.

What the docs don't spell out: the minimum top-up, the payment methods available in your country, and whether new accounts get free credit. These appear on the platform during sign-up, so check them there.

### Rate limits

- **DeepSeek limits concurrency, not tokens per minute.** Each account can run up to 2,500 concurrent requests on `deepseek-flash` and 500 on `deepseek-v4-pro`, shared across all its keys.
- **Going over returns HTTP 429.** DeepSeek says it will raise limits on request at no cost.
- **Long waits are cut off.** If inference hasn't started 10 minutes after a request, the server closes the connection.

## What DeepSeek costs for real workloads

Per-token prices are hard to picture, so here are three common jobs priced at list rates on DeepSeek and on the closest models from other providers. All prices are per 1 million tokens from each provider's official page; DeepSeek is shown at both peak and off-peak.

### 1. A chatbot: 1,000 conversations

Each conversation sends 2,000 input tokens and gets 500 output tokens back, with no caching. That is 2 million input and 0.5 million output tokens.

| Model | Price (input / output) | Cost |
|---|---|---:|
| GPT-6 Luna | $0.10 / $0.50 | $0.45 |
| Claude Haiku 5.5 | $0.10 / $0.50 | $0.45 |
| **DeepSeek V4.1 Flash, off-peak** | $0.15 / $0.60 | **$0.60** |
| **DeepSeek V4.1 Flash, peak** | $0.30 / $1.20 | **$1.20** |
| **DeepSeek V4 Pro, off-peak** | $0.66 / $1.98 | **$2.31** |
| Grok 4.3 | $1.25 / $2.50 | $3.75 |
| **DeepSeek V4 Pro, peak** | $1.32 / $3.96 | **$4.62** |
| GPT-6.1 Sol | $2 / $10 | $9.00 |
| Claude Sonnet 5.5 | $2 / $10 | $9.00 |

- **DeepSeek is no longer the cheapest at list price for plain requests.** GPT-6 Luna and Claude Haiku 5.5 cost 25% less than Flash off-peak, and 63% less than Flash at peak.
- **V4 Pro is the cheap option among larger models.** Off-peak, it costs 74% less than GPT-6.1 Sol or Claude Sonnet 5.5 for this workload.

### 2. The same chatbot with a cached system prompt

Now assume 1.5 million of the 2 million input tokens are a repeated system prompt and conversation history that hit the cache.

| Model | Cost |
|---|---:|
| **DeepSeek V4.1 Flash, off-peak** | **$0.38** |
| GPT-6 Luna | $0.32 |
| **DeepSeek V4.1 Flash, peak** | **$0.76** |
| **DeepSeek V4 Pro, off-peak** | **$1.35** |
| GPT-6.1 Sol | $6.15 |

- **Caching narrows the gap with Luna.** DeepSeek's cache price is extremely low ($0.003 off-peak), but output is a bigger share of this bill, and Flash output costs more than Luna's.
- **Caching helps Pro a lot.** Pro off-peak drops to $1.35, 78% less than GPT-6.1 Sol with its own cache discount.

### 3. A coding agent task

Agents re-read their context at every step, so most of their input is cache hits. Take a medium task of 1.6 million input tokens (90% cache hits) and 40,000 output tokens:

| Model | Cost per task |
|---|---:|
| **DeepSeek V4.1 Flash, off-peak** | **$0.05** |
| GPT-6 Luna | $0.05 |
| **DeepSeek V4.1 Flash, peak** | **$0.10** |
| **DeepSeek V4 Pro, off-peak** | **$0.22** |
| **DeepSeek V4 Pro, peak** | **$0.43** |
| GPT-6.1 Sol | $0.86 |
| Claude Sonnet 5.5 | $0.86 |

- **For agents, Flash and Luna are about even,** and both cost a small fraction of the mid-size models.
- **V4 Pro off-peak costs 75% less than GPT-6.1 Sol or Sonnet 5.5** for this task shape. Whether it does the job equally well is a separate question; benchmark it on your own tasks.

These are our calculations from list prices, not measurements. Real costs depend on how much of your input hits the cache and how many reasoning tokens thinking mode produces. To run your own numbers, use the [AI coding agent cost calculator](/agents) or compare models in the [LLM API pricing comparison](/blog/llm-api-pricing-comparison).

### What $10 of DeepSeek balance buys

Using the same three workloads:

| | Flash, off-peak | Flash, peak | Pro, off-peak | Pro, peak |
|---|---:|---:|---:|---:|
| Chatbot conversations (no cache) | about 16,700 | about 8,300 | about 4,300 | about 2,200 |
| Chatbot conversations (cached prompt) | about 26,400 | about 13,200 | about 7,400 | about 3,700 |
| Coding agent tasks | about 190 | about 96 | about 46 | about 23 |

On Flash, $10 covers thousands of chatbot conversations or a couple of hundred medium agent tasks off-peak. On Pro, it covers a few dozen agent tasks.

## Which DeepSeek model should you use?

- **Start with V4.1 Flash.** It handles chat, summaries, extraction, translation drafts and most coding help, it accepts images, and it is the cheaper model by a wide margin.
- **Move to V4 Pro when Flash isn't good enough.** Try it on the long multi-step problems, tricky code and analysis where Flash makes mistakes in your own tests. Off-peak, it still costs about a quarter of the mid-size models from OpenAI and Anthropic.
- **Turn thinking mode off for simple jobs.** Classification, short answers and formatting rarely need it, and reasoning tokens add to your bill.
- **Keep an eye on the Pro situation.** If DeepSeek routes Pro requests to V4.1 Flash until V4.1 Pro is out, you may be paying Pro prices for Flash answers, or Flash prices for Pro calls, depending on which document turns out to be right. Your usage records show what you were billed.

## A first API call

Because the API follows the OpenAI format, the official OpenAI Python SDK works with two changes, the base URL and the model name:

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"],
                base_url="https://api.deepseek.com")

reply = client.chat.completions.create(
    model="deepseek-flash",
    messages=[{"role": "user", "content": "Summarize this in one sentence: ..."}],
)
print(reply.choices[0].message.content)
print(reply.usage)  # the exact token counts you are billed for
```

The `usage` object includes how many input tokens hit the cache, which is the easiest way to check that your prompt structure is getting the cache discount.

## Is the DeepSeek API cheap in 2026?

It depends on the model and the time of day.

- **Flash is cheap, but no longer the cheapest.** At list prices, GPT-6 Luna and Claude Haiku 5.5 cost less per plain request, and Luna also comes out slightly ahead with a cached prompt. For agent work, Flash off-peak and Luna are about even.
- **Pro is where DeepSeek's prices stand out.** It sits well below the $2-per-million mid-size models from OpenAI and Anthropic, especially off-peak, while offering a 1 million token context window.
- **The time of day matters almost as much as the model.** The same Flash request costs 100% more at peak than off-peak. Teams in East Asia who work during the day will pay peak prices for much of their traffic unless they schedule batch work.
- **Grok is a different tier.** xAI's cheapest current text models start at $1 to $1.25 per million input tokens. See [Grok API pricing](/blog/grok-api-pricing).

For a ranked list of the lowest-cost APIs, see [the cheapest LLM APIs in 2026](/blog/cheapest-llm-api).

## Common mistakes when estimating DeepSeek costs

- **Using an old price list.** Many pages still quote V3 or R1 prices, or the pre-August flat rates. Since August 16 every price has a peak and an off-peak version, and since September 10 Flash is V4.1.
- **Forgetting reasoning tokens.** Thinking mode is on by default, and the model's reasoning adds tokens to every request. On a short question, the reasoning can be longer than the answer itself, so the output side of your bill can be much larger than the visible reply suggests. Check `usage` on a few real requests before you budget.
- **Assuming everything is cached.** The cache only matches a repeated prefix. If you put a timestamp, a user name or a random ID at the start of the prompt, nothing after it can hit the cache. Put the stable parts first.
- **Ignoring your time zone.** Peak hours are fixed in UTC. A team in Seoul or Tokyo testing during the afternoon is paying peak prices; a US team testing in the afternoon is not. Compare costs on the same time basis.
- **Mixing up the Pro model.** Until DeepSeek's documents agree on how `deepseek-v4-pro` is routed and billed, don't assume Pro quality or Pro prices. Your usage records show which model answered and what it cost.
- **Comparing list prices only.** A model with cheaper tokens can still cost more if it needs more tokens or more retries to finish a task. Test on a sample of your real requests.

## How to keep your DeepSeek bill down

1. **Use Flash by default.** It costs 77% less than Pro on cache-miss input and 70% less on output at the same time of day.
2. **Run batch work off-peak.** Moving a job from peak to off-peak halves its cost.
3. **Keep your prompt prefix stable.** Caching works on repeated prefixes, so put fixed instructions and documents first and the changing question last.
4. **Use non-thinking mode for simple tasks.** Thinking mode adds reasoning tokens to each request.
5. **Track the `usage` field.** It is the only exact count, and it shows how many tokens hit the cache.

## Verdict

- **DeepSeek has two API models now:** V4.1 Flash at $0.15 to $0.30 input and $0.60 to $1.20 output, and V4 Pro at $0.66 to $1.32 input and $1.98 to $3.96 output, depending on the hour.
- **Off-peak is half price,** and peak is only 7 hours on weekdays, which are mostly overnight for US users.
- **Getting started takes a few minutes:** an account, a prepaid balance and a key, with an OpenAI-compatible endpoint.
- **For plain requests, DeepSeek Flash is no longer the cheapest API,** but Pro costs about a quarter of GPT-6.1 Sol or Claude Sonnet 5.5 off-peak, and caching makes both much cheaper for agents.

## FAQ

**How much does the DeepSeek API cost?**
V4.1 Flash costs $0.15 per million input tokens and $0.60 per million output tokens off-peak, and 100% more at peak. V4 Pro costs $0.66 and $1.98 off-peak, and $1.32 and $3.96 at peak. Cached input is much cheaper on both.

**Is the DeepSeek API free?**
No. It is prepaid, and requests fail with error 402 when your balance runs out. The docs mention a granted balance that is used first, but don't say how much new accounts receive.

**What are DeepSeek's peak hours?**
Monday to Friday, 01:00–04:00 and 06:00–10:00 UTC. Everything else, including weekends and Chinese public holidays, is off-peak at half price.

**Do `deepseek-chat` and `deepseek-reasoner` still work?**
No. They were retired on July 24, 2026. Use `deepseek-flash` or `deepseek-v4-pro`, with thinking mode on or off.

**What is the context window of DeepSeek V4.1 Flash?**
1 million tokens, the same as V4 Pro, with up to 384K tokens of output per request.

**Where do I get a DeepSeek API key?**
On the API keys page of platform.deepseek.com, after creating an account and adding balance.

**Can I use DeepSeek with tools built for Claude?**
Yes. DeepSeek offers an Anthropic-compatible endpoint at `https://api.deepseek.com/anthropic`, so many tools written for the Anthropic API can point at DeepSeek by changing the base URL and key.

**How many tokens is a Chinese character on DeepSeek?**
About 0.6 tokens per Chinese character and 0.3 tokens per English character, according to DeepSeek's docs. The exact count is in the `usage` field of each response.

**Is DeepSeek cheaper than GPT-6 Luna?**
Not at list price for plain requests: Luna costs $0.10 input and $0.50 output, below Flash's off-peak $0.15 and $0.60. With heavy caching, the two come out about even.

## Run the numbers

The [token counter](/) shows how many tokens your text uses and what it costs on each model. For agent workloads, the [AI coding agent cost calculator](/agents) estimates a month of use from your task size and tasks per day.

*Prices and rules checked on DeepSeek's API documentation on October 12, 2026. Workload costs are our calculations from each provider's list prices.*

## Sources

- [DeepSeek API Docs: Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [DeepSeek API Docs: Change Log](https://api-docs.deepseek.com/updates/)
- [DeepSeek API Docs: V4.1 Flash release (September 10, 2026)](https://api-docs.deepseek.com/news/news260910/)
- [DeepSeek API Docs: Token & Token Usage](https://api-docs.deepseek.com/quick_start/token_usage/)
- [DeepSeek API Docs: Rate Limit](https://api-docs.deepseek.com/quick_start/rate_limit/)
- [DeepSeek API Docs: Error Codes](https://api-docs.deepseek.com/quick_start/error_codes/)
- [DeepSeek API Docs: Your First API Call](https://api-docs.deepseek.com/)
- [OpenAI: API pricing](https://developers.openai.com/api/docs/pricing)
- [Anthropic: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [xAI: Models and pricing](https://docs.x.ai/developers/pricing)
<!-- autoimg -->
