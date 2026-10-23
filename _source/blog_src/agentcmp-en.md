![Claude Code vs Codex vs Cursor: Cost and a Real Test (2026)](/claude-code-vs-codex-vs-cursor-cost-en.jpg)

Claude Code, OpenAI's Codex and Cursor all sell plans up to $200 a month, so on the pricing page they look interchangeable. They are not. Claude Code and Codex give you a usage allowance that refills on a schedule. Cursor, sold as part of The X Subscription since mid-October 2026, includes a weekly pool for its own Grok and Composer models only and charges Claude, GPT and Gemini separately at API prices. Their free options differ too, and so does how much work each one gets out of a task. This comparison covers the plans, how each tool counts usage, what independent benchmarks show, and what happened when we gave all three the same prompt.

## Claude Code vs Codex vs Cursor at a glance

| | Claude Code | Codex | Cursor |
|---|---|---|---|
| Made by | Anthropic | OpenAI | Anysphere (Cursor) |
| Where it runs | Terminal, IDE, Claude app | ChatGPT app, CLI, IDE, web | Its own code editor |
| Models | Claude only | OpenAI only | Claude, GPT, Gemini, Grok and Cursor's own |
| Free option | No (Claude Free has no Claude Code) | Yes, GPT-6 Luna | Yes, Free plan (Cursor's own models) |
| Entry paid plan | Claude Pro $20 | ChatGPT Plus $20 | Plus $8 (Grok and Composer only) |
| How usage is counted | 5-hour and weekly limits | 5-hour and weekly limits on Plus; weekly on Pro | Weekly pool for Cursor models; other models at API prices |
| Shares usage with | The Claude app | ChatGPT Work and other agent features | The Grok apps and Grok Bot |

The biggest structural difference is lock-in. Claude Code and Codex each run their own company's models, while Cursor lets you switch between providers in one editor and pays each model's list price.

## The plans and prices (2026)

US monthly prices, checked October 11, 2026 (Cursor rechecked October 23 after its plans changed):

| Price | Claude Code (Anthropic) | Codex (OpenAI) | Cursor |
|---|---|---|---|
| Free | – | ChatGPT Free (GPT-6 Luna) | Free (limited usage) |
| $8 | – | ChatGPT Go (GPT-6 Luna) | Plus (Grok and Composer only) |
| $20 | Claude Pro | ChatGPT Plus | – |
| $30 | – | – | Premium |
| $100 | Max 5x | Pro 100 | Super |
| $200 | Max 20x | Pro 200 | Ultra |
| $500 | – | Pro 500 (adds Ultrafast) | – |

- **Claude's Max plans are named after their usage.** Max 5x gives 500% of Pro's usage and Max 20x gives 2,000%, per Anthropic's pricing page.
- **ChatGPT's Pro multiples are reported, not official.** OpenAI's help center only says each Pro tier includes more usage than the one below. Press reports and an OpenAI staff post on X put Pro 100, 200 and 500 at about 500%, 1,000% and 2,500% of Plus. New Pro 200 subscribers since September 29, 2026 get the smaller allowance.
- **Cursor's plans no longer include Claude or GPT.** Premium, Super and Ultra give 400%, 1,500% and 5,000% of Plus's usage for Cursor's own models, and third-party models are paid from prepaid credit at API list price. Cursor doesn't publish the dollar size of the pool. See [Cursor pricing](/blog/cursor-pricing).
- **Codex has the only free option that runs a real agent on its own models.** Claude's free plan doesn't include Claude Code, and Cursor's free plan covers only its own models.

Full details for each tool: [Claude Code pricing](/blog/claude-code-cost-per-month), [Codex pricing](/blog/codex-pricing) and [Cursor pricing](/blog/cursor-pricing).

## How each one counts usage

### Claude Code: 5-hour and weekly limits

You get an allowance per 5-hour session and a weekly cap on top, both shared with the Claude app on web, desktop and mobile. A long chat in the app uses the same allowance as a coding session. Anthropic doubled Claude Code's five-hour limits for Pro and Max on May 6, 2026. Anthropic doesn't publish the allowance in tokens. More: [Claude Code usage limits](/blog/claude-code-usage-limits).

### Codex: 5-hour and weekly limits, a monthly meter on Free

On Plus and Business, Codex has a rolling 5-hour window, and weekly limits may also apply. Pro plans currently have no 5-hour window, only a weekly allowance. OpenAI publishes ranges per model for Plus: about 5 to 45 local messages per 5 hours on GPT-6 Astra and 350 to 3,000 on GPT-6 Luna. Since April 2, 2026, usage is metered in credits based on API token prices.

On our free account, Codex showed neither a 5-hour nor a weekly meter. It showed one usage bar, labeled one month, with a reset date a month out. More: [Codex usage limits](/blog/codex-usage-limits).

### Cursor: a weekly pool for its own models, API prices for the rest

Since mid-October 2026, each paid Cursor plan includes one weekly pool for Cursor's own models (Grok 4.7, 4.6, 4.5 and Composer 2.5), shared with the Grok apps. Claude, GPT, Gemini and the rest are not included: on Premium and above they are charged at each model's API list price from the first request, paid from prepaid credit. When the pool runs out, you wait for the weekly reset, pay from credit or upgrade. Existing Pro and Pro+ subscribers stay on the older monthly pools.

- **Claude Code and Codex hide the price per task.** You see a percentage of your allowance, not dollars.
- **Cursor shows the price per task, but not the size of the pool.** A Claude task that would cost $0.50 on the API costs $0.50 of your prepaid credit.
- **Running out works differently.** On Claude Code and Codex you wait for the reset or buy extra usage; on Cursor you pay from prepaid credit or upgrade.

## Same prompt, three tools: our test

Plans and benchmarks only go so far, so we gave each tool the same task between October 9 and 11, 2026. The prompt, word for word:

> "Make a brick-breaker game that runs in the browser as a single file named index.html in the current folder. It needs 2 levels, a score display and 3 lives, and it must be playable with the keyboard and the mouse. Write the file and finish."

![Same prompt in Claude Code, Codex and Cursor: Sonnet 5.5 medium 37 s, GPT-6 Luna medium 39 s, Grok 4.6 1 min 31 s](/claude-code-vs-codex-vs-cursor-cost-same-prompt-en.jpg)

| Tool · model · effort | Plan | Time | Game code | Usage or cost |
|---|---|---:|---:|---|
| Claude Code · Sonnet 5.5 · medium | Max 5x | 37 s | 198 lines | $0.25 at API prices |
| Claude Code · Sonnet 5.5 · high | Max 5x | 58 s | 398 lines | $0.30 at API prices |
| Claude Code · Opus 5.5 · medium | Max 5x | 52 s | 358 lines | $0.56 at API prices |
| Claude Code · Opus 5.5 · high | Max 5x | 1 min 50 s | 523 lines | $0.75 at API prices |
| Codex · GPT-6 Luna · medium | Free | 39 s | 398 lines | Both Codex runs together: 1% of the monthly free usage |
| Codex · GPT-6 Luna · extra high | Free | 39 s | 273 lines | (included above) |
| Cursor · Auto (Grok 4.6) | Free (Hobby) | 1 min 31 s | 398 lines | 15% of the monthly free usage |

Every run produced a working game that met the prompt: two levels, a score, three lives, and keyboard and mouse controls. The Claude Code costs were measured with ccusage and converted at API prices. The Codex and Cursor figures are what each app's usage meter showed.

### What the games were like

The person who ran the tests played every game. In his words, translated from Korean:

- **Sonnet 5.5, medium:** very simple, with no game effects and no hearts for lives, so it felt plain, but everything worked.
- **Sonnet 5.5, high:** about the level of Opus 5.5 at high effort. It added bricks that take two hits but made them impossible to tell apart, and the particles were well made.
- **Codex, GPT-6 Luna, medium:** "It feels kind of smooth, but there are no game effects, so the hits feel a bit weak."
- **Codex, GPT-6 Luna, extra high:** "The particles aren't flashy, but it's better than having none. I couldn't really tell the other features apart."

The Opus 5.5 runs are reviewed in detail in [Claude Opus 5.5 effort levels tested](/blog/claude-opus-5-5-effort), and the Sonnet runs in [Claude Sonnet vs Opus 5.5 for coding](/blog/claude-sonnet-5-5-vs-opus-5-5).

### What the numbers mean (our reading)

- **On a small task, speed was close.** Claude Code on Sonnet and Codex on GPT-6 Luna both finished in under 40 seconds at medium effort. Cursor took 1 min 31 s with Grok 4.6.
- **The free plans differ a lot in headroom.** One run took 15% of Cursor's monthly free usage, while two Codex runs together took 1% of Codex's. Taken at face value, that is about 6 games like this a month on Cursor Free and roughly 200 on Codex Free. Both meters round to whole percents, and we ran only one or two tests on each.
- **Higher effort bought polish, not speed, on Codex.** The extra high run took the same 39 seconds but added particle effects. On Claude Code, higher effort took longer and cost more.
- **The models aren't equal, so this isn't a quality ranking.** GPT-6 Luna and Grok 4.6 are each company's lightweight models, while Sonnet and Opus are Anthropic's mid-tier and top models. The test shows what you get from each tool's free or default setup on a small, well-defined job.
- **Usage meters are not comparable across companies.** 1% of Codex Free and 15% of Cursor Free are different budgets, and neither company says what 100% is.

## What independent benchmarks say

![What independent benchmarks say: Metric, Claude Code (Sonnet 5.5, max), Codex (GPT-6.1 Sol, xhigh)](/claude-code-vs-codex-vs-cursor-cost-what-independent-benchmarks-say-en.jpg)

For larger tasks, Artificial Analysis runs both agents on its Coding Agent Index, which combines three coding-agent benchmarks. Its representative configurations are Claude Code with Sonnet 5.5 at max effort and Codex with GPT-6.1 Sol at extra high:

| Metric | Claude Code (Sonnet 5.5, max) | Codex (GPT-6.1 Sol, xhigh) |
|---|---:|---:|
| Coding Agent Index | 68 | 63 |
| DeepSWE v1.1 | 72% | 73% |
| Terminal-Bench 4.0 | 66% | 55% |
| SWE-Atlas-QnA | 67% | 61% |
| Cost per task | $14.19 | $1.04 |
| Time per task | 1.5 hours | 15.5 minutes |
| Tokens per task | 27.7M | 3.2M |

- **Claude Code scored higher at its top setting,** leading on two of the three benchmarks.
- **Codex used far fewer tokens and far less money per task.** Its cost per task was 93% lower, and it finished in about a sixth of the time.
- **Lower effort narrows the cost gap.** In the same index, Claude Code on Sonnet 5.5 at high effort scores 55 at $1.24 per task, and Codex on GPT-6.1 Sol at medium scores 61 at $0.70.

In our reading, the pattern matches our small test: Codex tends to be lean with tokens, while Claude Code at high effort does more work per task and charges for it. On a subscription you don't see the dollars, but the extra tokens count against your allowance.

## Which gives the most for $200?

- **Claude Max 20x** gives 2,000% of Pro's usage for 1,000% of Pro's price, so each unit of usage costs 50% less than on Pro. FinOps LLM, which logged one heavy user's Claude Code sessions, measured about 1.9 billion tokens in a Max 20x week, almost all of it cache reads. See [how many tokens you get with Claude Pro and Max](/blog/claude-pro-max-how-many-tokens).
- **ChatGPT Pro 200** is reported at 1,000% of Plus usage for 1,000% of the price: no bulk discount, but no 5-hour window and all of ChatGPT's Pro features.
- **Cursor Ultra** gives 5,000% of Plus's usage for Grok and Composer, but Claude and GPT are paid on top at API prices, and Cursor doesn't publish the pool's dollar size.

If you use one agent all day, the flat allowances from Anthropic and OpenAI usually go further than paying API prices, because they aren't tied to per-token rates. Cursor wins on flexibility (any model in one editor) and on seeing the cost of each task.

## What a month costs on the API, for reference

From our [Claude Code pricing](/blog/claude-code-cost-per-month) model, 22 working days, with cache reads at 5% of the input price. The range runs from new context billed at the input price to new context billed at the 1-hour cache-write rate, as in our measured runs:

| How you use it | API with Claude Sonnet 5.5 | API with Claude Opus 5.5 | Cheapest plan that usually fits |
|---|---|---|---|
| Light: 3 small fixes a day | $9–14 | $18–28 | API, or any $20 plan |
| Regular: 5 features a day | $63–90 | $125–179 | $20–$100 plan |
| Heavy: 15 features a day | $188–269 | $375–537 | $100–$200 plan |
| Agents all day | $336–446 | $672–893 | $200 plan |

On Cursor, the API column is roughly what you would pay from prepaid credit, on top of the plan, when using Claude models. On Codex, GPT-6.1 Sol's API prices are the same as Sonnet 5.5's ($2 input and $10 output per million tokens), and GPT-6 Luna's are 95% lower, so a similar workload on Luna would cost far less.

## My own setup

I use Claude on the Max 5x plan every day. On Opus 5 I used to run out of my limit; since Opus 5.5 I haven't hit it, though one week recently reached 93%. On the OpenAI side I'm on the free plan, which is where the Codex runs above were done. Cursor was new to me; I installed it for the test above.

## Claude Code or Codex: which should you pick?

- **You want to try an AI coding agent without paying:** Codex on ChatGPT Free. In our test it built a complete game for a sliver of its monthly allowance.
- **You want the highest scores on hard tasks and can pay for it:** Claude Code. It led the Artificial Analysis index at max effort, and Max 5x or Max 20x makes heavy use affordable compared with API prices.
- **You want the most work per dollar on long tasks:** Codex. In the same index it used 88% fewer tokens per task than Claude Code at their top settings.
- **You want to switch between Claude, GPT and others in one editor:** Cursor. Expect to pay for Claude and GPT on top of the plan; Plus at $8 is enough if Grok and Composer will do.
- **You code with AI a few times a week:** any $20 plan, or an API key. At light use the API can cost less than $20 a month.
- **You keep hitting limits:** move up one tier before adding a second subscription.

## Verdict

- **Only Codex and Cursor have a real free tier,** and Codex's went much further in our test.
- **Claude Code does more per task at high effort,** scoring highest in independent benchmarks, and uses far more tokens to do it.
- **Codex is the lean option,** cheaper per task and faster on long jobs, with a weekly-only limit on Pro.
- **Cursor is the flexible option,** with every major model in one editor, but Claude and GPT now cost API prices on top of the plan.
- **For heavy daily use, a $100 or $200 flat plan from Anthropic or OpenAI is usually the cheapest way to buy agent time.**

## FAQ

**Is Claude Code better than Codex?**
On Artificial Analysis's Coding Agent Index, Claude Code with Sonnet 5.5 at max effort scores 68 against Codex with GPT-6.1 Sol at 63, but at $14.19 per task against $1.04. Which is better depends on whether you value the higher score or the lower cost.

**Is Codex cheaper than Claude Code?**
Both start at $20 a month. Codex also has a free option with GPT-6 Luna, and in independent benchmarks it uses far fewer tokens per task, so the same allowance or budget goes further.

**Can I use Claude Code for free?**
No. Claude Code needs a paid Claude plan (Pro, Max, Team or Enterprise) or an API key.

**Is Codex free?**
Yes, in a limited form. ChatGPT Free includes Codex with GPT-6 Luna in the desktop app. On our account the free plan showed one monthly usage meter.

**Can Cursor use Claude and GPT models?**
Yes. Cursor's paid plans include Claude, GPT, Gemini and Grok models, charged at each model's API price. On the free plan, Cursor picks the model for you.

**Do Claude Code and Codex share limits with the chat apps?**
Yes. Claude Code shares its allowance with the Claude app, and Codex shares one with ChatGPT Work, ChatGPT for Excel and Workspace Agents.

## Estimate your own month

Put in your task size and tasks per day in the [coding agent cost calculator](/agents) to see the API cost next to every Claude and ChatGPT plan.

*Plan details checked on each company's pricing page on October 11, 2026. Our test is one run per setup between October 9 and 11, 2026; Claude Code costs were measured with ccusage, and Codex and Cursor usage was read from each app's meter.*

## Sources

- [Claude plans and pricing (Anthropic)](https://claude.com/pricing)
- [Using Claude Code with your Pro or Max plan (Claude Help Center)](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [Codex pricing and plans (OpenAI)](https://learn.chatgpt.com/docs/pricing)
- [Codex rate card (OpenAI Help Center)](https://help.openai.com/en/articles/20001106-codex-rate-card-2)
- [About ChatGPT Pro tiers (OpenAI Help Center)](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [Cursor pricing](https://cursor.com/pricing)
- [Artificial Analysis: Claude Code vs Codex](https://artificialanalysis.ai/agents/coding-agents/comparisons/claude-code-vs-codex)
- [FinOps LLM: Claude Pro and Max token limits](https://finopsllm.com/research/claude-pro-max-tokens-limit)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
<!-- autoimg -->
