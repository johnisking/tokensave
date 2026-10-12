![Claude Code Pricing 2026: $20, $100 or $200 a Month, or the API](/claude-code-cost-per-month-en.jpg)

**Claude Code pricing in one line:** Claude Code is included in every paid Claude plan: **Pro at $20 a month** ($17 a month billed annually), **Max 5x at $100** and **Max 20x at $200**. You can also skip the plans and pay per token on the API, where one small task cost **$0.25 on Sonnet 5.5 and $0.56 to $0.75 on Opus 5.5** in our tests. The Free plan doesn't include Claude Code. All prices below are from Anthropic's pricing pages, checked October 12, 2026.

Which option is cheapest depends on how much you use it. This page covers what each plan includes, what one task really costs on the API (measured), what a month costs at four levels of use, and the point where a plan beats paying per token.

## Claude Code pricing at a glance (2026)

![Claude Code pricing at a glance (2026): Plan, Price, Claude Code, Usage per 5-hour session](/claude-code-cost-per-month-claude-code-pricing-at-a-glance-2026-en.jpg)

| Plan | Price | Claude Code | Usage per 5-hour session |
|---|---|:---:|---|
| Free | $0 | No | – |
| Pro | $20 a month ($17 billed annually) | Yes | At least 500% of Free |
| Max 5x | $100 a month | Yes | 500% of Pro |
| Max 20x | $200 a month | Yes | 2,000% of Pro |
| API (Claude Console) | Pay per token | Yes | No plan limit, every token billed |

- **Prices exclude tax,** and Max is monthly only. There is no annual discount on either Max plan.
- **One allowance for everything.** Claude Code in the terminal and in IDEs (VS Code, Cursor, JetBrains) shares the same 5-hour and weekly limits as Claude on the web, desktop and mobile. A long chat in the app leaves less for coding.
- **Only Max 20x has a volume discount.** It gives 2,000% of Pro's usage for 1,000% of Pro's price, so each unit of usage costs 50% less. Max 5x costs the same per unit as Pro.
- **Max's monthly API credits don't pay for Claude Code.** The pricing page lists $100 (Max 5x) or $200 (Max 20x) a month in API credits for building on the Claude Platform, but Anthropic's help center says those credits can't be used in Claude Code or the Claude apps.
- **Team and Enterprise.** Anthropic's pricing FAQ says Claude Code is included in all paid plans. Team seats are $25 a month ($20 annually) for Standard and $125 ($100) for Premium, with at least 2 seats. Enterprise is $20 per seat plus usage billed at API rates.

## Is Claude Code free?

No. Claude's Free plan has no Claude Code, and there is no Claude Code trial. You have two low-cost ways to start:

- **The API,** paying only for the tokens you use, through a Claude Console account. A few small tasks a week cost well under $20 a month (see the monthly table below).
- **Pro for one month,** $20, then decide based on how often you hit the limit.

If you want a coding agent that is actually free, OpenAI's Codex runs on ChatGPT's free plan with GPT-6 Luna. We ran the same task in both in [Claude Code vs Codex vs Cursor](/blog/claude-code-vs-codex-vs-cursor-cost).

## Claude Code on the API: price per million tokens

![Claude Code on the API: price per million tokens: Model, Input, Output, Cache write (1 hour), Cache read](/claude-code-cost-per-month-claude-code-on-the-api-price-per-million-en.jpg)

When Claude Code runs on API credits instead of a plan, you pay Anthropic's standard API prices. Per million tokens, from the Claude API pricing page:

| Model | Input | Output | Cache write (1 hour) | Cache read |
|---|---:|---:|---:|---:|
| Fable 5.1 | $10 | $50 | $20 | $0.25 |
| Opus 5.5 | $4 | $20 | $8 | $0.20 |
| Sonnet 5.5 | $2 | $10 | $4 | $0.10 |
| Haiku 5.5 (prompts up to 100K) | $0.10 | $0.50 | $0.20 | $0.01 |

- **Opus 5.5 costs 100% more than Sonnet 5.5 per token,** and Fable 5.1 costs 150% more than Opus 5.5.
- **Cache reads are what make Claude Code affordable.** On Opus 5.5 and Sonnet 5.5 a cache read costs 5% of the input price; on Fable 5.1, 2.5%. Claude Code caches its context automatically.
- **Fable on a plan:** Pro gets Fable only through paid usage credits, and Max has a separate weekly limit for Fable.
- Long-prompt prices, fast mode and older models are in [How much does a Claude token cost?](/blog/claude-token-cost)

## What one task really costs: four measured runs

On October 9, 2026 we gave Claude Code the same prompt four times: build a brick-breaker browser game as a single file, with 2 levels, a score, 3 lives, and keyboard and mouse controls. Token counts come from ccusage, converted at API prices.

| Model · effort | Time | Game code | Cost at API prices |
|---|---:|---:|---:|
| Sonnet 5.5 · medium | 37 s | 198 lines | $0.25 |
| Sonnet 5.5 · high | 58 s | 398 lines | $0.30 |
| Opus 5.5 · medium | 52 s | 358 lines | $0.56 |
| Opus 5.5 · high | 1 min 50 s | 523 lines | $0.75 |

- **Every run produced a working game.** Higher effort and Opus bought more polish, not a working-or-broken difference.
- **Cache writes were 63% to 81% of the cost.** The game code itself (output) was 17% to 33%. Cache reads were the most tokens but only 2% to 4% of the cost.
- **The totals only add up at the 1-hour cache-write rate,** twice the input price. That is our reading of ccusage's numbers: in these runs, Claude Code's cache writes were billed at the 1-hour rate.
- **Effort is a price lever.** Thinking tokens are billed as output, and high effort used 96% to 97% more output tokens than medium.

The full results, with the games, are in [Claude Sonnet vs Opus 5.5 for coding](/blog/claude-sonnet-5-5-vs-opus-5-5) and [Claude Opus 5.5 effort levels tested](/blog/claude-opus-5-5-effort).

## Estimated cost per task, by size

A game in one file is a small task. For bigger work we use the model behind our [coding agent cost calculator](/agents): an agent works in steps, and at every step it sends its whole working context back to the model (instructions, tool definitions, the files it has read and everything so far). The low figure is the calculator's (new context billed at the input price); the high figure bills new context at the 1-hour cache-write rate, as in our measured runs.

| Task | Steps | Tokens sent | Sonnet 5.5 | Opus 5.5 |
|---|---:|---:|---:|---:|
| Small fix | ~8 | ~0.2 million | $0.14–0.21 | $0.27–0.43 |
| New feature | ~25 | ~1.6 million | $0.57–0.81 | $1.14–1.63 |
| Big refactor | ~60 | ~7.7 million | $1.91–2.54 | $3.82–5.07 |

- **Most of what Claude Code sends is re-read context:** 82% of the tokens for a small fix and 96% for a big refactor are cache reads. That is why a feature that sends 1.6 million tokens still costs well under a dollar on Sonnet.
- **Without caching,** the same feature on Sonnet 5.5 would cost about $3.38 instead of $0.57.
- **Our measured game ($0.25–0.30 on Sonnet) sits between the small-fix and feature rows,** which is where a single-file game belongs.

## What a month of Claude Code costs

Four typical patterns over 22 working days, on the API:

| How you use it | Tasks a month | API, Sonnet 5.5 | API, Opus 5.5 | Plan that usually fits |
|---|---:|---:|---:|---|
| Light: 3 small fixes a day | 66 | $9–14 | $18–28 | API, or Pro |
| Regular: 5 features a day | 110 | $63–90 | $125–179 | Pro or Max 5x |
| Heavy: 15 features a day | 330 | $188–269 | $375–537 | Max 5x or Max 20x |
| Agents all day: 8 big tasks a day | 176 | $336–446 | $672–893 | Max 20x |

Anthropic publishes one reference point of its own: across enterprise deployments, Claude Code averages **about $13 per developer per active day and $150–250 per developer per month**, and 90% of users stay under $30 per active day. That sits between our heavy-Sonnet row ($8.50–12 a day) and our heavy-Opus row ($17–24 a day).

## When a plan is cheaper than the API

Anthropic doesn't publish the plan limits in tokens or dollars, so the break-even point has to be estimated. [FinOps LLM](https://finopsllm.com/research/claude-pro-max-tokens-limit) logged one heavy user's Claude Code sessions until the limits stopped them:

| Plan | Price | One 5-hour window at API prices |
|---|---:|---|
| Pro | $20 a month | ~$7 *(our estimate)* |
| Max 5x | $100 a month | **~$37** (measured median) |
| Max 20x | $200 a month | ~$150 *(our estimate)* |

The Pro and Max 20x figures are scaled from the measured Max 5x window using Anthropic's own multiples, so treat them as orders of magnitude. A Max 20x week measured about 1.9 billion tokens, roughly $1,800 at API prices, against $200 for the month.

Put next to the daily costs above:

- **Light use:** the API costs less than Pro's $20 a month as long as you spend under about $0.90 per working day. Three small fixes a day on Sonnet ($0.40–0.60) is well under; on Opus ($0.80–1.30) it is about even.
- **Regular use on Sonnet ($2.80–4.10 a day):** fits inside a single Pro window on that estimate, so Pro is the cheaper choice. On Opus ($5.70–8.10 a day) you are near the edge of a Pro window; if you hit it most days, Max 5x.
- **Heavy use and agents:** Max. The same month on the API would be $188 to $893.

The weekly limit is the other constraint. If you hit it on Max 5x even when the 5-hour windows are fine, Max 20x is the next step.

## My own usage

I use Claude on the Max 5x plan every day. On Opus 5 I used to run out of my limit; since Opus 5.5 I haven't hit it, though one week recently reached 93% of the weekly limit. With Sonnet I needed more rounds of fixes to get the details right, so a cheaper token didn't always mean a cheaper finished task. That is my experience, not a measurement.

## Costs that catch people out

![Costs that catch people out: An API key in your environment. If ANTHROPIC_API_KEY is set, Claude Code uses it instead of your Pro or Max lo](/claude-code-cost-per-month-costs-that-catch-people-out-en.jpg)

- **An API key in your environment.** If `ANTHROPIC_API_KEY` is set, Claude Code uses it instead of your Pro or Max login, and you are billed at API rates. Unset it if you want the plan to pay.
- **Usage credits past the limit.** On paid plans you can keep working after a limit with usage credits, billed at standard API rates.
- **Fast mode.** Fast output for Opus 5.5 (research preview) costs $8 input and $40 output per million tokens on the API, 100% more than standard.
- **Long sessions.** Each step re-sends the whole conversation. Use **/clear** between unrelated tasks and **/compact** on long ones.
- **Writing in another language.** Korean needs about 44% more tokens than English for the same meaning, and Japanese about 79% more.

To check where you stand, run **/usage** (session cost at list price, mainly for API users) or **/status** (what is left of your plan's allowance). More ways to spend less: [How to save tokens in Claude Code](/blog/claude-code-save-tokens).

## Which should you pick?

1. **A few small tasks a week:** the API. You will likely spend less than $20 a month.
2. **Daily coding on Sonnet:** Pro at $20, or $17 billed annually.
3. **You hit Pro's 5-hour limit most days, or code on Opus all day:** Max 5x at $100.
4. **You run agents for hours or hit Max 5x's weekly limit:** Max 20x at $200. It is the only plan where each unit of usage costs less.
5. **CI pipelines and automation:** the API, so each job has a predictable per-token cost.

Whatever the plan, choose the model per task: Sonnet 5.5 handles most coding work at 50% of Opus 5.5's price per token, and in our test it was 55% to 60% cheaper at the same effort. Plan limits are explained in [Claude Code usage limits](/blog/claude-code-usage-limits), and the plans side by side in [Claude Max vs Pro](/blog/claude-max-vs-pro).

## FAQ

**How much does Claude Code cost per month?**
$20 on Claude Pro ($17 billed annually), $100 on Max 5x or $200 on Max 20x. On the API, a month of regular use (5 features a day) costs roughly $63–90 on Sonnet 5.5 or $125–179 on Opus 5.5.

**Is Claude Code included in Claude Pro?**
Yes. Claude Code is included in Pro, Max, Team and Enterprise, and shares the same usage limits as the Claude app.

**Is Claude Code free?**
No. The Free plan doesn't include it. The cheapest way to use it occasionally is the API, paying per token.

**Is Claude Code cheaper on the API or on a plan?**
For a few small tasks a week, the API is cheaper. If you code with it most days, Pro or Max is cheaper, often by a wide margin: a Max 20x week of heavy use measured about $1,800 at API prices.

**Can I use Max's monthly API credits for Claude Code?**
No. Anthropic's help center says the monthly API credits included with Max can't be used in Claude Code or the Claude apps.

**How do I see what Claude Code has cost me?**
Run /usage for the session's token usage and cost at list price, or /status to see how much of your plan's allowance is left.

## Estimate your own month

The [coding agent cost calculator](/agents) lets you set task size, tasks per day and working days, and compares Claude Code's API cost with every Claude and ChatGPT plan. For the other agents, see [Codex pricing](/blog/codex-pricing) and [Cursor pricing](/blog/cursor-pricing); for Pro itself, [Claude Pro price](/blog/claude-pro-price).

*Prices and limits checked October 12, 2026. Anthropic changes limits often; check [claude.com/pricing](https://claude.com/pricing) before you decide.*

## Sources

- [Claude plans and pricing (Anthropic)](https://claude.com/pricing)
- [Claude API pricing (Anthropic docs)](https://platform.claude.com/docs/en/about-claude/pricing)
- [Manage costs effectively (Claude Code docs)](https://code.claude.com/docs/en/costs)
- [Using Claude Code with your Pro or Max plan (Claude Help Center)](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [Prompt caching (Claude docs)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [How many tokens Claude Pro and Max include (FinOps LLM)](https://finopsllm.com/research/claude-pro-max-tokens-limit)
<!-- autoimg -->
