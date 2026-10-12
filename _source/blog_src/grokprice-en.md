![Grok API Pricing 2026: Grok 4.7, 4.3, Tools and Imagine Costs](/grok-api-pricing-en.jpg)

Grok API pricing is easy to find and easy to misread. xAI now lists eight text model IDs across four price levels, with three different cached-input prices, and every one of them switches to a higher rate once a prompt reaches 200,000 tokens. Tool calls such as web search are billed on top, and image and video generation have their own price lists. This guide covers xAI's official prices as of October 12, 2026, including Grok 4.7, released on September 21: what each model costs, what the extras add, how to get an API key, and what common workloads cost compared with GPT-6, Claude and DeepSeek.

## Grok API pricing (official, October 2026)

![Grok API pricing (official, October 2026): Model, Context, Input, Cached input, Output](/grok-api-pricing-grok-api-pricing-official-october-2026-en.jpg)

xAI's pricing page lists these text models. Prices are per 1 million tokens:

| Model | Context | Input | Cached input | Output |
|---|---:|---:|---:|---:|
| grok-4.7 (newest) | 500K | $2.00 | $0.50 | $6.00 |
| grok-4.6 | 500K | $2.00 | $0.50 | $6.00 |
| grok-4.5 | 500K | $2.00 | $0.30 | $6.00 |
| grok-4.3 | 1M | $1.25 | $0.20 | $2.50 |
| grok-4.20 (reasoning, non-reasoning, multi-agent) | 1M | $1.25 | $0.20 | $2.50 |
| grok-build-0.1 | 256K | $1.00 | $0.20 | $2.00 |

- **Grok 4.7, 4.6 and 4.5 cost the same per token,** except that Grok 4.5's cached input is 40% cheaper ($0.30 against $0.50).
- **Grok 4.3 and the 4.20 family are the budget line,** with a 1 million token context and output at $2.50, 58% less than Grok 4.7.
- **grok-build-0.1 is the cheapest,** at $1 input and $2 output, with a 256K context.
- **Grok 4.7 takes text and images** and offers reasoning effort from low to extra high, with high as the default. It supports function calling and structured outputs, and its knowledge cutoff is May 2026.

### Long-context pricing above 200K tokens

Every text model has a second price tier. Once a single prompt reaches 200,000 tokens, the higher rate applies to every token in that request, not just the part above 200K:

| Model | Input | Cached input | Output |
|---|---:|---:|---:|
| grok-4.7, 4.6 | $4.00 | $1.00 | $12.00 |
| grok-4.5 | $4.00 | $0.60 | $12.00 |
| grok-4.3, 4.20 | $2.50 | $0.40 | $5.00 |
| grok-build-0.1 | $2.00 | $0.40 | $4.00 |

- **Long prompts cost 100% more per token.** A 199K-token request and a 201K-token request differ by more than the extra 2K tokens; the second is billed entirely at the higher rate.
- **Agents hit this threshold.** Coding agents that keep a large repository in context can cross 200K tokens late in a session, and every step after that is billed at the higher rate.

### Price modifiers

- **US regional endpoint:** 10% more than the global rates, available for Grok 4.7 and 4.6 only.
- **Priority processing:** 100% more on all token rates, charged only when the response comes back with `service_tier: "priority"`.
- **Batch API:** 20% off for Grok 4.3 and the three Grok 4.20 models only. Grok 4.7 doesn't support batch.
- **Grok 4.7 Fast is not on the public API.** xAI describes it as faster output at prices 100% higher, but it is only offered in Cursor and xAI's own Grok Build.

## Tools, images, video and voice

### Tool calls

When Grok uses a server-side tool, you pay per call on top of the tokens:

| Tool | Price |
|---|---|
| Web search, image search | $5 per 1,000 calls |
| X search | $5 per 1,000 posts, $10 per 1,000 profiles |
| Code execution | $5 per 1,000 calls |
| File attachment search | $5 per 1,000 calls |
| Collections search | $2.50 per 1,000 calls |
| Viewing images, X videos, remote MCP tools | Billed as tokens |

- **Search adds up in agents.** An agent that runs 10 web searches per task pays $0.05 in search fees per task before any tokens.
- **Storage is billed too:** files at $0.025 per GiB per day, collections at $0.10 per GiB per day, and downloads at $0.20 per GiB.
- **Blocked requests aren't free.** On the Responses API, a request stopped for a usage-guideline violation before generation costs $0.05.

### Grok Imagine: images and video

| Model | Price |
|---|---|
| grok-imagine-image | $0.02 per image |
| grok-imagine-image-2.0 | $0.04–$0.06 per image (low quality), $0.06–$0.08 (medium), by resolution |
| grok-imagine-image-quality | $0.05–$0.07 per image (retiring November 2, 2026) |
| grok-imagine-video-1.5 | $0.08 / $0.14 / $0.25 per second at 480p / 720p / 1080p |
| grok-imagine-video-1.5-lite | $0.02 / $0.03 / $0.14 per second at 480p / 720p / 1080p |

Input images for editing cost $0.002 to $0.01 each. A 10-second 1080p clip on grok-imagine-video-1.5 costs $2.50; the same clip at 720p on the lite model costs $0.30. To compare with other image and video models, use the [AI image cost calculator](/image) and the [AI video cost calculator](/video).

### Voice

Speech-to-speech costs $0.08 per minute, text-to-speech $15 per million characters, and speech-to-text $0.10 per hour (or $0.20 per hour streaming).

## What Grok costs for real workloads

Here are three common jobs priced at list rates. All prices are per million tokens from each provider's official page.

### 1. A chatbot: 1,000 conversations

Each conversation sends 2,000 input tokens and returns 500 output tokens, with no caching: 2 million input and 0.5 million output tokens in total.

| Model | Price (input / output) | Cost |
|---|---|---:|
| GPT-6 Luna | $0.10 / $0.50 | $0.45 |
| DeepSeek V4.1 Flash (off-peak) | $0.15 / $0.60 | $0.60 |
| **grok-build-0.1** | $1.00 / $2.00 | **$3.00** |
| **Grok 4.3** | $1.25 / $2.50 | **$3.75** |
| **Grok 4.7** | $2.00 / $6.00 | **$7.00** |
| GPT-6.1 Sol | $2.00 / $10.00 | $9.00 |
| Claude Sonnet 5.5 | $2.00 / $10.00 | $9.00 |

- **Grok 4.7 costs 22% less than GPT-6.1 Sol or Claude Sonnet 5.5** for this workload. The input price is the same; the saving comes from output at $6 against $10.
- **Grok 4.3 costs 58% less than those two models.**
- **Grok has no low-cost tier like Luna or Flash.** For this job, GPT-6 Luna costs 85% less than even the cheapest Grok model.

### 2. A coding agent task

A medium agent task: 1.6 million input tokens, 90% of them cache hits, and 40,000 output tokens. The prompt stays under 200K tokens per request.

| Model | Cost per task |
|---|---:|
| GPT-6 Luna | $0.05 |
| **grok-build-0.1** | **$0.53** |
| **Grok 4.3** | **$0.59** |
| GPT-6.1 Sol | $0.86 |
| Claude Sonnet 5.5 | $0.86 |
| **Grok 4.5** | **$0.99** |
| **Grok 4.7** | **$1.28** |

- **For agents, Grok 4.7 costs more than GPT-6.1 Sol and Sonnet 5.5.** The reason is caching: Grok 4.7 charges $0.50 per million cached tokens, 400% more than the $0.10 that OpenAI and Anthropic charge for their mid-size models, and agents are mostly cached tokens.
- **Grok 4.5 is cheaper than 4.7 for agents** because of its $0.30 cache price, at the same input and output rates.
- **Crossing 200K tokens raises every price by 100%.** The same task, if each step exceeded 200K tokens, would cost $2.56 on Grok 4.7.

### 3. The same agent with web search

Add 10 web searches per task at $5 per 1,000 calls, and each task above costs $0.05 more. That is small next to Grok 4.7's token cost, but it is the whole budget of a Luna-based task.

These are our calculations from list prices. To estimate a month of agent work, use the [AI coding agent cost calculator](/agents).

## Grok 4.7 vs GPT-6.1 Sol vs Claude Sonnet 5.5: per-token prices

![Coding agent task cost on Grok, GPT and Claude models: from GPT-6 Luna at $0.05 to Grok 4.7 at $1.28](/grok-api-pricing-agent-task-cost-en.jpg)

| Price per 1M tokens | Grok 4.7 | GPT-6.1 Sol | Claude Sonnet 5.5 |
|---|---:|---:|---:|
| Input | $2.00 | $2.00 | $2.00 |
| Cached input | $0.50 | $0.10 | $0.10 |
| Output | $6.00 | $10.00 | $10.00 |

The three mid-size flagships charge the same for fresh input, so the difference comes down to two numbers. Grok 4.7's output is 40% cheaper, which favors work that writes a lot: long answers, drafts, translations and code generation from short prompts. Its cached input is 400% more expensive, which penalizes work that re-reads the same context many times: agents, long chats and question-answering over a large document. If you know roughly what share of your tokens are cached and what share are output, you can tell in advance which model will cost less.

## Grok in Cursor: what we saw

Cursor lists Grok 4.7 at the same per-token prices as xAI's API: $2 input, $0.50 cache read and $6 output, and Grok 4.7 Fast at $4, $1 and $12. One difference: Cursor applies its long-context rate above 256K tokens, while xAI's own threshold is 200K.

On October 11, 2026, we gave Cursor's free plan a simple prompt to build a browser brick-breaker game. With the model left on Auto, Cursor sent this request to Grok 4.6. It finished in 1 minute 31 seconds, wrote 398 lines and produced a working game, and it used 15% of the free plan's monthly allowance. The full test is in [Cursor pricing](/blog/cursor-pricing), and the same prompt in Claude Code and Codex is compared in [Claude Code vs Codex vs Cursor](/blog/claude-code-vs-codex-vs-cursor-cost).

## How to get a Grok API key

xAI's quick-start guide describes these steps:

1. **Create an account** at console.x.ai.
2. **Add credits.** The API is prepaid: you load credits before making requests. xAI doesn't state a minimum purchase; the minimum for automatic top-up is $5.
3. **Create a key** on the API Keys page and copy it somewhere safe.
4. **Store it** as the environment variable `XAI_API_KEY`.
5. **Call the API.** It is OpenAI-compatible: use the OpenAI SDK with base URL `https://api.x.ai/v1` and a model such as `grok-4.7`.

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["XAI_API_KEY"], base_url="https://api.x.ai/v1")
reply = client.chat.completions.create(
    model="grok-4.3",
    messages=[{"role": "user", "content": "Explain prompt caching in two sentences."}],
)
print(reply.choices[0].message.content, reply.usage)
```

- **Free credits:** xAI's official pages don't currently mention a free-credit program. The $25 a month that xAI announced for the 2024 public beta was tied to that beta, which ran to the end of 2024.

### Rate limit tiers

xAI raises your rate limits as your total spend grows. Spend is counted from January 1, 2026, and tiers never go down:

| Tier | Total spend |
|---|---:|
| Tier 0 | $0 |
| Tier 1 | $50 |
| Tier 2 | $250 |
| Tier 3 | $1,000 |
| Tier 4 | $5,000 |
| Enterprise | On request |

The limits per tier differ by model; check xAI's rate limits page for your model.

## Grok API vs SuperGrok subscription

The API is separate from xAI's consumer plans. On x.ai's pricing page, Grok is free with limits, SuperGrok costs $30 a month and SuperGrok Plus costs $100 a month. The pricing page doesn't list API credits as part of either subscription, and the API is billed separately in the xAI console. If you only want to chat with Grok, a subscription is simpler; if you are building an app or running an agent, you need the API.

## Which Grok model should you use?

- **Grok 4.7 for the hardest tasks,** where you want xAI's newest model and the reasoning-effort setting. Keep prompts under 200K tokens.
- **Grok 4.5 for cache-heavy work at the same tier.** It costs the same per fresh token but 40% less per cached token.
- **Grok 4.3 or 4.20 for volume.** They cost 38% less per input token and 58% less per output token than Grok 4.7, with a 1 million token context and batch discounts.
- **grok-build-0.1 for the lowest Grok price,** at $1 and $2.
- **Something else for very cheap bulk work.** If price is the main factor, GPT-6 Luna, Claude Haiku 5.5 and DeepSeek V4.1 Flash cost a fraction of any Grok model. See [DeepSeek API pricing](/blog/deepseek-api-pricing) and [the cheapest LLM APIs](/blog/cheapest-llm-api).

## How to keep your Grok bill down

1. **Stay under 200K tokens per request.** Trim old conversation turns or summarize them before a long session crosses the threshold, since crossing it raises the price of the whole request.
2. **Reuse a stable prompt prefix.** Cached input costs 75% less than fresh input on Grok 4.7 and 85% less on Grok 4.5, so keep fixed instructions and documents at the start of the prompt.
3. **Send bulk jobs to the Batch API.** It takes 20% off Grok 4.3 and the 4.20 models.
4. **Use the global endpoint unless you need US data residency.** The US regional endpoint costs 10% more.
5. **Limit tool calls.** Web search costs $5 per 1,000 calls and X search $5 per 1,000 posts, on top of tokens, so ask for search only when the answer depends on fresh information.
6. **Pick the model per task.** Route simple requests to Grok 4.3 or grok-build-0.1 and keep Grok 4.7 for the hard ones.

## Grok API changes in 2026

- **September 21, 2026:** Grok 4.7 released as xAI's newest model, at the same token prices as Grok 4.6.
- **May 15, 2026:** xAI retired older models; its docs carry a migration guide for that date. Pages that still list Grok 4.1 Fast as a current model are out of date.
- **November 2, 2026:** grok-imagine-image-quality is scheduled to retire. Move image work to grok-imagine-image-2.0 before then.

## Verdict

- **Grok 4.7 costs $2 input and $6 output per million tokens,** with cached input at $0.50 and prices 100% higher above 200K tokens.
- **For chat-style requests it undercuts GPT-6.1 Sol and Claude Sonnet 5.5,** thanks to cheaper output.
- **For agents, it can cost more than both,** because its cached-input price is 400% higher.
- **Grok 4.3, 4.20 and grok-build-0.1 are the value options,** and the Batch API takes another 20% off Grok 4.3 and 4.20.
- **Watch the extras:** web search at $5 per 1,000 calls, the 200K threshold and priority processing at 100% more.

## FAQ

**How much does the Grok API cost?**
Grok 4.7 costs $2 per million input tokens, $0.50 per million cached input tokens and $6 per million output tokens. Grok 4.3 costs $1.25, $0.20 and $2.50, and grok-build-0.1 costs $1, $0.20 and $2. Prompts of 200K tokens or more are billed at rates 100% higher.

**Is the Grok API free?**
No. It is prepaid with credits. The free $25 monthly credit from the 2024 beta has ended, and no current free-credit program is listed on xAI's site.

**What is the cheapest Grok model?**
grok-build-0.1, at $1 input and $2 output per million tokens. Among general models, Grok 4.3 and Grok 4.20 at $1.25 and $2.50.

**Does SuperGrok include API access?**
No. SuperGrok ($30 a month) and SuperGrok Plus ($100 a month) are consumer subscriptions. The API is billed separately through console.x.ai.

**How much does Grok web search cost in the API?**
$5 per 1,000 calls, on top of the tokens the model uses.

**What is Grok 4.7's context window?**
500,000 tokens. Grok 4.3 and the Grok 4.20 models offer 1 million tokens, and grok-build-0.1 offers 256,000. On every model, prompts of 200K tokens or more are billed at the higher long-context rate.

**Does the Grok API have a batch discount?**
Yes, 20% off, but only for Grok 4.3 and the three Grok 4.20 models. Grok 4.7 doesn't support batch requests.

**Is Grok cheaper than GPT and Claude?**
For chat with little caching, Grok 4.7 costs about 22% less than GPT-6.1 Sol or Claude Sonnet 5.5. For agent work with heavy caching, it costs more, because its cached-input price is higher.

## Run the numbers

Paste a prompt into the [token counter](/) to see its cost on Grok, GPT, Claude and Gemini models. For agent workloads, the [AI coding agent cost calculator](/agents) estimates a month of use.

*Prices checked on xAI's documentation on October 12, 2026. Workload costs are our calculations from each provider's list prices. The Cursor test was one run on October 11, 2026.*

## Sources

- [xAI: Models and pricing](https://docs.x.ai/developers/pricing)
- [xAI: Grok 4.7 model page](https://docs.x.ai/developers/models/grok-4.7)
- [xAI: Grok 4.7 developer guide](https://docs.x.ai/developers/grok-4-7)
- [xAI: Grok 4.7 announcement](https://x.ai/news/grok-4-7)
- [xAI: Quickstart](https://docs.x.ai/developers/quickstart)
- [xAI: Rate limits](https://docs.x.ai/developers/rate-limits)
- [xAI: Billing](https://docs.x.ai/console/billing)
- [xAI: Consumer pricing](https://x.ai/pricing)
- [Cursor: Grok 4.7 model page](https://cursor.com/docs/models/grok-4-7)
- [OpenAI: API pricing](https://developers.openai.com/api/docs/pricing)
- [Anthropic: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
<!-- autoimg -->
