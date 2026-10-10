![How Much Does a Claude Token Cost? 2026 Prices Per Token](/claude-token-cost-en.jpg)

How much does a Claude token cost? Anthropic lists its API prices per million tokens, so a single token looks almost free. What you actually pay depends on how many tokens a request uses and which kind they are. This page has the current price of every Claude model, the cost of one token and of a few common messages, and the cost breakdown of four Claude Code runs we measured with ccusage on October 9. Prices were checked against Anthropic's official pricing page on October 11, 2026.

## Claude token prices per million tokens (2026)

![Claude token prices per million tokens (2026): Model, Input, Output, Cache write (5 min), Cache write (1 hour), Cache read](/claude-token-prices-per-million-tokens-en.jpg)

These are Anthropic's list prices for the current Claude models on the Claude API, in US dollars per million tokens (MTok). Haiku 5.5 has two rows: prompts up to 100,000 tokens, and prompts over 100,000 tokens.

| Model | Input | Output | Cache write (5 min) | Cache write (1 hour) | Cache read |
|---|---:|---:|---:|---:|---:|
| Fable 5.1 | $10 | $50 | $12.50 | $20 | $0.25 |
| Opus 5.5 | $4 | $20 | $5 | $8 | $0.20 |
| Sonnet 5.5 | $2 | $10 | $2.50 | $4 | $0.10 |
| Haiku 5.5 (up to 100K) | $0.10 | $0.50 | $0.125 | $0.20 | $0.01 |
| Haiku 5.5 (over 100K) | $0.50 | $2.50 | $0.625 | $1 | $0.05 |

- **Output costs 400% more than input on every current model.**
- **Opus 5.5 costs 100% more than Sonnet 5.5, and Sonnet 5.5 costs 1,900% more than Haiku 5.5** (for prompts up to 100K tokens). Of all the price differences on this page, the one between models is the largest.
- **Cache reads are the cheapest tokens.** On Opus 5.5 and Sonnet 5.5 a cache read costs 5% of the input price, on Fable 5.1 2.5%, and on Haiku 5.5 10%.
- **Haiku 5.5 is the only current model with a long-prompt price.** When a request's prompt goes over 100,000 tokens, every token in that request is billed at the higher row. Opus 5.5, Sonnet 5.5 and Fable 5.1 bill the whole 1M context window at the standard rate.

Older models are still on sale at older prices. Opus 5, for example, is $5 input and $25 output, 25% more than Opus 5.5, and Sonnet 4.6 is $3 and $15, 50% more than Sonnet 5.5. If you are still calling an older model ID, moving to the 5.5 version lowers the price per token. See [Claude Opus 5 vs 5.5](/blog/claude-opus-5-vs-5-5) for what changed.

## How much does one Claude token cost?

Divide the per-million price by 1,000,000 and you get the price of one token. Per 1,000 tokens is easier to read:

| Model | One input token | One output token | 1,000 input tokens | 1,000 output tokens |
|---|---:|---:|---:|---:|
| Claude Fable 5.1 | $0.00001 | $0.00005 | $0.01 | $0.05 |
| Claude Opus 5.5 | $0.000004 | $0.00002 | $0.004 | $0.02 |
| Claude Sonnet 5.5 | $0.000002 | $0.00001 | $0.002 | $0.01 |
| Claude Haiku 5.5 | $0.0000001 | $0.0000005 | $0.0001 | $0.0005 |

So a Sonnet 5.5 output token costs one thousandth of a cent. One dollar buys 500,000 input tokens or 100,000 output tokens on Sonnet 5.5, 250,000 or 50,000 on Opus 5.5, and 10 million or 2 million on Haiku 5.5.

A request is never one token, though. The next sections look at how many tokens text turns into and how many a real request uses.

## What counts as a token in Claude?

A token is a piece of text the model reads or writes: often a whole short word, sometimes part of a longer word, a space, or a punctuation mark. Each model family splits text with its own tokenizer, so the same paragraph is a different number of tokens on Claude, GPT and Gemini.

Two facts from Anthropic matter for cost:

- **Newer Claude models use more tokens for the same text.** Anthropic says Claude 4.7 and later models use a new tokenizer that produces about 30% more tokens for the same text than earlier models. All the 5.x models above use it. The tokenizer change came with 4.7; the lower per-token prices came later, with 5.5.
- **Web content adds up fast.** Anthropic's own rule of thumb is that an average 10 KB web page is about 2,500 tokens, a large 100 KB documentation page about 25,000, and a 500 KB research paper PDF about 125,000.

How many tokens per word? On OpenAI's current tokenizer we measured about 1.1 to 1.3 tokens per English word ([full results](/blog/tokens-per-word)). Anthropic doesn't publish a word ratio for Claude, so for the estimates on this page we use **about 1.5 Claude tokens per English word**: our GPT measurement plus the 30% our [token counter](/claude-token-counter) adds for Claude over GPT. That 30% is our own estimate, not an Anthropic figure. For anything you'll pay real money for, count your actual text instead of trusting a ratio.

Language matters even more. In our measurements on the same content, Korean used about 44% more tokens than English, Japanese about 79% more, Polish about 88% more and Spanish about 18% more. Those numbers were measured on GPT's tokenizer. We haven't measured the language gap on Claude, but if you prompt in a language other than English, count your text before assuming English-level costs.

## How much does a Claude message cost?

![How much does a Claude message cost?: Request, Tokens in / out, Haiku 5.5, Sonnet 5.5, Opus 5.5](/claude-token-cost-how-much-does-a-claude-message-cost-en.jpg)

Here are four everyday requests, priced with the estimate of 1.5 tokens per English word: a short question with a 300-word answer, a 5,000-word report summarized into 400 words, a 100-page document (about 40,000 words) with a 1,000-word answer, and a message deep in a chat that already holds 30,000 tokens of history, without caching. These are our calculations from the list prices, not measurements. Thinking tokens, tools and caching are left out to keep them simple.

| Request | Tokens in / out | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---:|---:|---:|
| Question + 300-word answer | 75 / 450 | $0.0002 | $0.005 | $0.009 |
| Summarize a 5,000-word report | 7,500 / 600 | $0.001 | $0.021 | $0.042 |
| 100-page document + answer | 60,000 / 1,500 | $0.007 | $0.135 | $0.27 |
| Chat with 30K tokens of history | 30,000 / 600 | $0.003 | $0.066 | $0.132 |

- **A short answer costs less than a cent,** on Sonnet 5.5 and on Opus 5.5.
- **In these examples the input cost more than the answer** once a document was pasted in, even though each output token costs more.
- **Long chats cost more per message.** Every message re-sends the whole conversation as input. On Sonnet 5.5 the 30,000-token chat costs $0.066 per message, against half a cent for the short question. With prompt caching on, that same message would cost about $0.009 on Sonnet 5.5 and $0.018 on Opus 5.5, because the history is read from cache at 5% of the input price.

To get an exact count for your own text and its cost on every model, paste it into the [token counter](/).

## Where the money actually goes: four measured Claude Code runs

The per-message math above assumes simple chat. Agents such as Claude Code work differently: they write large chunks of context into the prompt cache and re-read them at every step. To see what that does to cost, here are four runs we measured on October 9, 2026, each building the same small browser game in Claude Code with a different model and effort level (the full test is in [Sonnet vs Opus 5.5](/blog/claude-sonnet-5-5-vs-opus-5-5)). The token counts come from ccusage.

![ccusage measurement record: input, output, cache write and cache read tokens for the four runs](/claude-sonnet-5-5-vs-opus-5-5-en-7.jpg)

| Run | Output tokens | Cache write tokens | Cache read tokens | Total | Cost |
|---|---:|---:|---:|---:|---:|
| Sonnet 5.5, medium | 4,100 | 50,337 | 60,632 | 115,073 | $0.25 |
| Sonnet 5.5, high | 8,073 | 53,980 | 75,536 | 137,593 | $0.30 |
| Opus 5.5, medium | 6,299 | 53,002 | 74,123 | 133,428 | $0.56 |
| Opus 5.5, high | 12,376 | 59,146 | 151,326 | 222,854 | $0.75 |

Fresh input was only 4 to 6 tokens per run, so it is left out of the table. We split each run's cost by token type using Anthropic's prices:

| Run | Output share of cost | Cache write share | Cache read share | Average cost per 1M tokens |
|---|---:|---:|---:|---:|
| Sonnet 5.5, medium | 17% | 81% | 2% | $2.16 |
| Sonnet 5.5, high | 27% | 71% | 2% | $2.21 |
| Opus 5.5, medium | 22% | 75% | 3% | $4.23 |
| Opus 5.5, high | 33% | 63% | 4% | $3.37 |

![Where the cost went in four Claude Code runs: cache writes took 63 to 81% of the cost](/claude-token-cost-where-the-money-goes-en.jpg)

- **Cache writes were 63% to 81% of the cost.** Output, the game code itself, was 17% to 33%.
- **Cache reads were the most tokens but the least cost.** In the Opus high run they were 68% of all tokens and 4% of the cost.
- **The costs only add up at the 1-hour cache-write rate.** Pricing these cache writes at the 5-minute rate gives $0.17 instead of $0.25 for Sonnet medium and $0.57 instead of $0.75 for Opus high. ccusage's totals match the 1-hour price ($4 per million on Sonnet 5.5, $8 on Opus 5.5), which is twice the input price. That is our reading of the numbers: in these runs, Claude Code's cache writes were billed at the 1-hour rate.
- **The average token cost about the input price.** Across each run, the blended price came to about $2.2 per million tokens on Sonnet 5.5 and $3.4 to $4.2 on Opus 5.5, close to each model's input price.

A longer run looked different. In a separate Opus 5.5 run from our [Opus 5 vs 5.5 test](/blog/claude-opus-5-vs-5-5), cache reads were 88% of 674,452 tokens. The same arithmetic puts cache reads at 13% of that run's $0.93, cache writes at 55% and output at 33%, for an average of about $1.38 per million tokens. With more steps, more of the tokens were cheap cache reads. That is one run, so treat it as an example, not a rule.

So for agent work, an estimate based on output tokens alone would have missed most of these bills. Cache writes need to be counted too.

## Hidden costs that change the price per token

These official modifiers change what a token costs:

| Item | What it does to cost |
|---|---|
| Thinking tokens | Billed as output tokens. Higher effort means more of them. |
| Batch API | 50% off input and output for jobs that can wait. |
| Prompt cache write | 25% more than input (5 minutes) or 100% more (1 hour). |
| Prompt cache read | 95% off input on Opus 5.5 and Sonnet 5.5. |
| Fast mode (Opus 5.5, research preview) | $8 input and $40 output: 100% more than standard. |
| US-only inference | 10% more on every token category. |
| Tool use | A 286-token system prompt on the 5.5 models, plus your tool definitions, on every request. |
| Web search | $10 per 1,000 searches, plus the result tokens as input. |
| Haiku 5.5 over 100K tokens | 400% more for the whole request. |

- **Thinking tokens count as output.** When you raise effort, Claude spends more tokens reasoning before it answers, and those are billed at the output price. In our runs, high effort used 96% to 97% more output tokens than medium. See [Claude Opus 5.5 effort levels](/blog/claude-opus-5-5-effort).
- **Batch and caching discounts can be combined,** according to Anthropic.
- **Tool definitions are input tokens.** Every tool you include is sent with every request, whether Claude calls it or not.

## How to pay less per Claude token

1. **Pick the smallest model that does the job.** Anthropic positions Haiku 5.5 for classification, extraction and routing, at 95% less than Sonnet 5.5. Sonnet 5.5 is enough for most coding; in our test it was 55% to 60% cheaper than Opus 5.5 at the same effort.
2. **Turn on prompt caching for anything repeated.** A long system prompt, a document you ask several questions about, a growing chat. On the 5.5 models a cached read is 95% cheaper than fresh input.
3. **Use the Batch API for work that can wait.** Overnight summaries, bulk tagging and evals get 50% off.
4. **Keep output short.** Ask for the length you need; output is the most expensive token type.
5. **Lower effort for simple tasks.** Medium effort used about half the output tokens of high in our runs.
6. **Start fresh conversations.** In Claude Code, use /clear between unrelated tasks so old context stops being re-sent. More tips: [How to save tokens in Claude Code](/blog/claude-code-save-tokens).

## My own usage on Max 5x

I started on the free plan and moved up through Pro to Max 5x, which I use now. I build games on it, and I do it by typing into the Claude app's chat window, not by running Claude Code in a terminal. This is how it feels in daily use, not a measurement.

### Opus 5.5 made the limit last

On Opus 5, I used up the whole limit. Since Opus 5.5 came out, I haven't hit the limit once. Last week I used up to 93% of my weekly limit, as I remember it. For coding, Opus 5.5 feels like it's on Fable's level, and the value is far better.

### I leave effort on auto

Most of the time it runs at medium, and it goes up to high for coding work. I tried low a few times, found it frustrating and stopped using it. High gives clearly better results. I've tried xhigh and max only about once.

### Sonnet: cheaper per token, more rounds of fixes

With Sonnet, even when I explained in detail, the details I wanted often didn't come out right. The features get built, but getting the details right meant asking again and again, so I went through more build-and-fix rounds than with Opus.

### What that means for cost (our reading)

Extra rounds are why a cheaper token doesn't always make a cheaper task. In the measured runs above, one Sonnet high run cost $0.30 and one Opus high run $0.75. Two more Sonnet requests of the same size would bring Sonnet to $0.90, more than Opus. Real fix-up requests vary in size, so this is simple arithmetic, not a measurement. On a plan, the same thing shows up as more of your limit used instead of more dollars.

## Subscription vs API: what a token costs on a Claude plan

Claude Pro ($20 a month in the US) and Max ($100 or $200) don't bill per token at all. You get a usage allowance that resets every five hours, plus a weekly limit, and the Claude apps and Claude Code share it. Anthropic doesn't publish the allowance in tokens. Its pricing page also lists monthly API credits for the Claude Platform with Max: $100 on Max 5x and $200 on Max 20x.

For heavy users, a plan has worked out much cheaper per token than the API. [FinOps LLM](https://finopsllm.com/research/claude-pro-max-tokens-limit) logged one user's Claude Code sessions: a typical Max 5x window came to roughly $37 of API-equivalent usage, and a Max 20x week to about 1.9 billion tokens, which we priced at around $1,800 at API rates, against $200 for the month. 96% of those tokens were cache reads. The details are in [How many tokens do you get with Claude Pro and Max?](/blog/claude-pro-max-how-many-tokens).

If you use Claude every day, especially Claude Code, a plan is likely cheaper per token. If you call Claude from your own app, or use it a few times a week, pay-as-you-go API usage can cost less than $20 a month. The [subscription vs API calculator](/plans) compares the two with your own usage.

## Claude vs GPT and Gemini: price per token

On list price, Claude's current models match OpenAI's closest ones. Input / output prices per million tokens, from each provider's official pricing page on October 11, 2026 (Gemini 3.1 Pro is a preview model; the price shown is for prompts up to 200K tokens):

| Tier | Claude | OpenAI | Google |
|---|---|---|---|
| Cheapest | Haiku 5.5: $0.10 / $0.50 | GPT-6 Luna: $0.10 / $0.50 | – |
| Mid | Sonnet 5.5: $2 / $10 | GPT-6.1 Sol: $2 / $10 | Gemini 3.1 Pro: $2 / $12 |
| Top | Fable 5.1: $10 / $50 | GPT-6 Astra: $10 / $50 | – |
| Between | Opus 5.5: $4 / $20 | – | – |

The same price doesn't give the same bill. Each model turns the same text into a different number of tokens, and each uses a different number of tokens to finish the same task. In our tests, Sonnet 5.5 used 35% fewer output tokens than Opus 5.5 on the same job. For a real comparison, cost per finished task tells you more than cost per token. For the full list of 22 models, see [LLM API pricing compared](/blog/llm-api-pricing-comparison).

## Verdict

- **One Claude token costs between $0.0000001 (Haiku 5.5 input) and $0.00005 (Fable 5.1 output).** Sonnet 5.5, the usual default, is $2 per million input tokens and $10 per million output tokens.
- **A typical chat message costs less than a cent on Sonnet 5.5.** Long documents and long conversations are what push it up.
- **In agent work, cache writes were the largest cost.** In our four Claude Code runs they took 63% to 81% of the bill, and the average token cost about the input price.
- **The biggest price difference is between models.** Opus 5.5 costs 100% more than Sonnet 5.5 per token; Haiku 5.5 costs 95% less than Sonnet 5.5.

## FAQ

**How much does a Claude token cost?**
On Claude Sonnet 5.5, one input token costs $0.000002 and one output token $0.00001 ($2 and $10 per million). Opus 5.5 is $4 and $20 per million, Haiku 5.5 $0.10 and $0.50, and Fable 5.1 $10 and $50.

**How much is 1,000 tokens on Claude?**
On Sonnet 5.5, 1,000 input tokens cost $0.002 and 1,000 output tokens cost $0.01. On Opus 5.5 it is $0.004 and $0.02. In English, 1,000 Claude tokens is roughly 650 to 700 words by our estimate.

**Why is output more expensive than input?**
Anthropic doesn't explain the gap; it simply prices output higher. On all current Claude models, output costs 400% more than input, which is why long answers and high effort settings add up.

**Are thinking tokens charged?**
Yes. Extended thinking tokens are billed as output tokens, so higher effort levels cost more even if the visible answer is the same length.

**Is Claude more expensive than ChatGPT per token?**
At list price, no. Sonnet 5.5 and GPT-6.1 Sol are both $2 input and $10 output per million tokens, and Haiku 5.5 matches GPT-6 Luna. Real costs differ because the models count text differently and use different amounts of tokens per task.

**Does a Claude Pro or Max subscription charge per token?**
No. Plans have usage limits that reset every five hours, plus a weekly limit. Anthropic doesn't publish them in tokens, and per-token prices apply only on the API, or if you turn on extra usage credits after hitting your limit.

## Run the numbers

Paste any prompt into the [token counter](/) to see its exact token count and cost on Claude, GPT and Gemini. For agents, the [coding agent cost calculator](/agents) estimates a month of Claude Code on Opus 5.5 or Sonnet 5.5 from your task size and tasks per day. Related: [Claude Code cost per month](/blog/claude-code-cost-per-month) · [How to count tokens for GPT, Claude and Gemini](/blog/how-to-count-tokens-gpt-claude-gemini).

*Prices checked October 11, 2026. Claude Code measurements from October 9, 2026, one run each; costs are ccusage conversions at API prices.*

## Sources

- [Anthropic: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Anthropic: Claude plans and pricing](https://claude.com/pricing)
- [Anthropic: Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)
- [Anthropic: Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [OpenAI: API pricing](https://developers.openai.com/api/docs/pricing)
- [Google: Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [FinOps LLM: Claude Pro and Max token limits](https://finopsllm.com/research/claude-pro-max-tokens-limit)
- [ccusage: Claude Code usage tool (GitHub)](https://github.com/ryoppippi/ccusage)
<!-- autoimg -->
