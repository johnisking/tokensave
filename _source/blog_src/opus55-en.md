![Claude Opus 5 vs 5.5: Price, Performance and a Real Test](/claude-opus-5-vs-5-5-en.jpg)

Claude **Opus 5.5** is Anthropic's new top model, released on September 22, 2026. Compared with **Opus 5**, its token prices are 20% lower and cache reads are 60% cheaper. Anthropic says it costs "40% less to run on typical work"; our own math for a coding agent workload came out about 37% cheaper. When we gave both models the same game-building request, Opus 5.5 used 64% fewer tokens. Below: price, performance and measured results side by side, plus a Max 20x user's experience with both models and whether it is worth switching.

## Opus 5 vs 5.5 pricing

![Opus 5 vs 5.5 pricing: Item, Opus 5, Opus 5.5, Difference](/claude-opus-5-vs-5-5-opus-5-vs-5-5-pricing-en.jpg)

Price per million tokens, from Anthropic's official pricing page.

| Item | Opus 5 | Opus 5.5 | Difference |
|---|---:|---:|---:|
| Input | $5 | $4 | 20% cheaper |
| Output | $25 | $20 | 20% cheaper |
| Cache write (5 min) | $6.25 | $5 | 20% cheaper |
| Cache read | $0.50 | $0.20 | **60% cheaper** |
| Fast mode | – | $8 / $40 | New in Opus 5.5 |

- **Cache reads dropped the most.** On Opus 5 they cost 10% of the input price; on Opus 5.5 they cost 5%. The more a task re-reads the same documents or conversation, the bigger the gap.
- **Same text, same token count.** Both models use the newer tokenizer introduced after Claude 4.7, so the same input text produces the same number of tokens and the price difference goes straight through to cost. How many tokens the model spends while working can still differ (see our test below).
- **Fast mode:** Opus 5.5 adds a fast mode at $8 input and $40 output. It works in Claude Code and the API, and Anthropic says it is up to 150% faster.

## Hands-on: my Max 20x weekly limit started to last

I (Jaehyun) have used both Opus 5 and Opus 5.5 on the Claude Max 20x plan while building games. This is what it felt like in daily use, not a measured figure.

- **Weekly limit:** With Opus 5, I would use up the weekly limit about a day before it reset. Since switching to Opus 5.5, I often finish the week at around 90% usage.
- **External tasks:** The gap was biggest on token-heavy external tasks. Of the models I have used, Opus 5.5 felt like the one that burns the fewest tokens.
- **Coding and value:** For coding, it feels as capable as Fable 5.1, and it feels like much better value. For reference, Opus 5.5's API price ($4 input, $20 output) is 60% lower than Fable 5.1's ($10 input, $50 output).

The official prices above and the calculations below point the same way. Doing the same work for less cost (that is, less of your limit) means the same plan lasts longer.

## We measured it with the same request

![Same request, measured: the brick-breaker games built by Opus 5 and Opus 5.5 side by side](/claude-opus-5-vs-5-5-en-5.jpg)

Feelings are not enough, so on October 9, 2026 we gave both models the **same request** once each in Claude Code, changing only the model name: build a brick-breaker game that runs in the browser (two levels, score and lives) as a single HTML file. Usage was measured with the free tool ccusage.

| Item | Opus 5 | Opus 5.5 | Difference |
|---|---:|---:|---:|
| Output tokens | 36,640 | 15,180 | 59% fewer |
| Cache write tokens | 74,533 | 63,917 | 14% fewer |
| Cache read tokens | 1,774,025 | 595,337 | 66% fewer |
| Total tokens | 1,885,246 | 674,452 | **64% fewer** |
| Cost (at API prices) | $2.55 | $0.93 | **64% cheaper** |
| Game code produced | about 684 lines | 409 lines | 40% shorter |

![Token chart for the same request: Opus 5 used 1.89M tokens, Opus 5.5 used 674K](/claude-opus-5-vs-5-5-en-6.jpg)

- **The cost gap was far bigger than the price gap (20%).** Handling the same request, Opus 5.5 used 64% fewer tokens in total. Cache reads, where the model re-reads the earlier conversation, fell 66%. That matches why the Max weekly limit started to last.
- **Opus 5 built more features.** Both games had bricks that take two hits (Opus 5.5 from level 2), but Opus 5 also added particle effects, a restart-anytime (R) key, a level-clear bonus and hit counts drawn on the bricks. To my eye, though, Opus 5.5's screen looked cleaner and nicer. Part of the token gap comes from this feature difference.
- **Opus 5.5's file was cut short.** The closing tags (`</script></body></html>`) were missing, so it showed a blank screen at first; adding those three tags made it play normally. Opus 5's file ran straight away.
- **Caveat:** Each model ran once, so a rerun may give different numbers. Cost is ccusage's conversion at API prices; plan users do not pay this, it comes out of their limit.

![ccusage measurement record: Opus 5 and Opus 5.5 tokens and cost on October 9, 2026](/claude-opus-5-vs-5-5-en-7.jpg)

## Cost on real workloads

![Cost on real workloads: Task, Opus 5, Opus 5.5, Difference](/claude-opus-5-vs-5-5-cost-on-real-workloads-en.jpg)

We calculated the cost of the same work on both models, keeping token counts equal and changing only the prices.

| Task | Opus 5 | Opus 5.5 | Difference |
|---|---:|---:|---:|
| 1 chat request (2,000 in / 500 out) | $0.0225 | $0.018 | 20% cheaper |
| 1 document question (50,000 in, 45,000 cached / 1,000 out) | $0.0725 | $0.049 | 32% cheaper |
| 1 coding agent feature (1.6M in, mostly cached / 17,500 out) | $1.79 | $1.14 | 37% cheaper |
| Coding agent for a month (110 features) | about $197 | about $125 | 37% cheaper |

Example: Opus 5.5 document question = 5,000 new input × $4 + 45,000 cached × $0.20 + 1,000 output × $20 (all per million tokens) = $0.049.

**The more you cache, the more you save.** Plain chat is only 20% cheaper, but a coding agent that keeps re-reading the conversation gets close to 37% cheaper. This table assumes equal token counts. Anthropic says its "40% less" comes from lower prices **plus fewer tokens per task** at default settings, and our test above also used 64% fewer tokens.

## Performance (as reported by Anthropic)

![Performance (as reported by Anthropic): benchmark bar chart, Opus 5 vs Opus 5.5](/claude-opus-5-vs-5-5-en-4.jpg)

Benchmarks published by Anthropic. Opus 5.5 scores use the highest setting (max effort), except Terminal-Bench 4.0, which uses one step lower (xhigh). All are Anthropic's own measurements.

| Benchmark | Opus 5 | Opus 5.5 |
|---|---:|---:|
| Terminal-Bench 4.0 (terminal tasks) | 52.3% | 66.4% |
| CursorBench 4.0 (coding) | 46.6% | 57.8% |
| FrontierCode v1.1 (coding) | 48.0% | 54.4% |
| AutomationBench (work automation) | 26.9% | 40.0% |
| OSWorld 2.1 (computer use, subset) | 74.0% | 81.8% |
| Humanity's Last Exam (with tools) | 63.6% | 67.7% |

- **The biggest gains are in coding and agent work.** Terminal tasks rose 14.1 points and work automation 13.1 points.
- **Speed:** According to Anthropic, output is generated more than 30% faster than on Opus 5.
- **Caveat:** These are the company's own scores; test on your own tasks to see whether you get the same gap.

## Independent results: Artificial Analysis

There are outside scores too. On the Intelligence Index from independent evaluator Artificial Analysis, Opus 5.5 at max effort took first place with 58 (per press reports).

| Model | Intelligence Index |
|---|---:|
| Claude Opus 5.5 (max effort) | 58 |
| GPT-6 Astra | 53 |
| Claude Fable 5.1 | 53 |
| Claude Opus 5 | 51 |

- **Opus 5.5 leads in independent testing too,** 7 points ahead of Opus 5.
- **But it used more tokens there.** Output tokens per task were about 119,000 for Opus 5.5 at max effort versus about 73,000 for Opus 5, 63% more. The next section explains why.

## Effort settings change the savings

- **The default changed.** Per Anthropic's migration guide, requests without an effort setting run at high on Opus 5 and at medium on Opus 5.5. The "40% less" claim is at this default.
- **At the highest setting the saving can disappear.** Artificial Analysis found Opus 5.5 at max effort used 63% more output tokens and cost about the same per task as Opus 5 (per press reports).
- **Our test went the other way.** In Claude Code with only the model name changed, Opus 5.5 used 64% fewer tokens. Results depend heavily on settings and the task.
- **Our advice:** start at medium and raise effort only where quality falls short. At xhigh or max, give max_tokens plenty of room; Anthropic suggests starting at 64k.
- **Measured by level:** we ran the same prompt from low to max in [Claude Opus 5.5 effort levels tested](/blog/claude-opus-5-5-effort).

## For Pro and Max plan users

- On a subscription, what matters is your **limit**, not the token price. Anthropic said that with the Opus 5.5 launch it raised the 5-hour usage limits on Pro, Max, Team and seat-based Enterprise, and is giving a limit reset you can use later.
- Because the model does the same work for less, you will likely fit more into the same limit. Anthropic does not publish exact limits per plan.

## Pros and cons

![Opus 5.5 pros and cons summary card](/claude-opus-5-vs-5-5-en-9.jpg)

**Pros**

- **Cheaper and better:** token prices down 20% and cache reads down 60%, with higher benchmark scores.
- **Especially good for agent work:** cache-heavy coding and automation cost about 37% less.
- **Optional fast mode:** pay more for speed when you are in a hurry.

**Cons**

- **Still an expensive model:** 100% more per token than Sonnet 5.5 ($2 input, $10 output). Sonnet is enough for simple work.
- **Most performance figures come from the company:** it also tops the independent Artificial Analysis index, but test on your own work.
- **Savings shrink at the highest setting:** it thinks longer, so output tokens go up.
- **Fast mode is pricey:** 100% more than standard mode.

## What to change when moving your API code

Per Anthropic's migration guide, some Opus 5 code returns a 400 error on Opus 5.5.

| Change | What to do on Opus 5.5 |
|---|---|
| Thinking can't be turned off: `disabled` and `budget_tokens` error | Drop the thinking setting and control cost with effort |
| No forced tool use: `tool_choice` `any` and `tool` error | Use `auto` with strict tools, or structured outputs |
| Old computer-use tool (`computer_20251124`) errors on the API and Google Cloud | Switch to `computer_toolset_20260801` |
| Replaying thinking blocks after editing earlier turns errors (accounts created on or after August 31, 2026) | Keep conversation history append-only |
| Notes between tool calls move into thinking blocks | Set `thinking.display` if you show them to users |
| Wider refusals (`stop_reason: "refusal"`) | Handle refusals and set up a fallback |

Priority Tier is also not supported on Opus 5.5. If you use it through Claude Code or a subscription plan, there is no code for you to change.

## Should you switch from Opus 5?

- **If you use Opus 5 through the API:** switch; costs drop 20 to 37% while performance goes up. It is not just a model-name change, though: fix the breaking changes above, set effort explicitly, and test in a development environment first.
- **If you run big jobs in Claude Code often:** this is where the cache discount helps most.
- **If Sonnet is enough for the job:** no need to move up to Opus 5.5. Giving only hard design and debugging to Opus is the most economical setup.

## FAQ

**How much cheaper is Opus 5.5 than Opus 5?**
Token prices are 20% lower and cache reads 60% lower. On real workloads, chat is 20% cheaper and cache-heavy coding agent work about 37% cheaper.

**Do token counts change?**
The same input text gives the same token count (same tokenizer). The tokens spent doing the work differ: Opus 5.5 used 64% fewer in our test, and it can use more at the highest setting.

**Opus 5.5 or Sonnet 5.5?**
Sonnet 5.5 is enough for most work at half the price per token. Use Opus 5.5 for hard coding, long agent runs and writing where quality matters.

**Can I reuse my Opus 5 API code as is?**
No. Settings such as turning thinking off or forcing a tool with `tool_choice` return errors on Opus 5.5. See "What to change when moving your API code" above.

## Calculate it for your own work

In the [coding agent cost calculator](/agents), enter task size and tasks per day to compare a month on Opus 5.5, Sonnet 5.5 and GPT-6 Sol. Check the cost of a single prompt in the [token counter](/). To decide between a plan and the API, see [Claude Code cost per month](/blog/claude-code-cost-per-month).

*Prices as of October 9, 2026. Prices change; check Anthropic's pricing page before you rely on them.*

## Sources

- [Anthropic: Claude Opus 5.5 announcement (September 22, 2026)](https://www.anthropic.com/claude-opus-5-5)
- [Anthropic: Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Anthropic: Prompt caching docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [DataNorth: Claude Opus 5 launch summary (July 24, 2026)](https://datanorth.ai/news/claude-opus-5-by-anthropic)
- [ccusage: Claude Code usage tool (GitHub)](https://github.com/ryoppippi/ccusage)
- [Anthropic: Migrating from Claude Opus 5 to Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)
- [OfficeChai: Artificial Analysis Intelligence Index report](https://officechai.com/ai/claude-opus-5-5-creates-5-point-lead-over-gpt-6-astra-jumps-to-top-spot-on-artificial-analysis-intelligence-index/)
<!-- autoimg -->
