![Cursor Pricing 2026: Plans, Usage Pools and Real Monthly Cost](/cursor-pricing-en.jpg)

How much does **Cursor** cost in 2026? The plan prices are easy to find, but what you actually pay depends on which model the agent uses and how often you run it. On October 11, 2026, I went through Cursor's official pricing page and its models and pricing docs, then installed Cursor on Windows and gave the free plan the same brick-breaker prompt I used to measure Claude Opus 5.5 and Sonnet 5.5 in Claude Code. Below are the plans, how billing works, what the free plan actually did, and what a month of agent use costs on each model.

## Cursor pricing plans (2026)

![Cursor pricing plans (2026): Plan, Price, Who it's for (Cursor's wording, summarized)](/cursor-pricing-cursor-pricing-plans-2026-en.jpg)

Prices from Cursor's official pricing page, checked October 11, 2026. Prices exclude tax.

| Plan | Price | Who it's for (Cursor's wording, summarized) |
|---|---:|---|
| Hobby | Free | Trying Cursor; limited Agent requests, no credit card |
| Pro | $20/mo | Individuals; extended Agent limits, frontier models, cloud agents |
| Pro+ | $60/mo | Recommended by Cursor for daily agent users |
| Ultra | $200/mo | Recommended by Cursor for agent power users |
| Teams Standard | $40/user/mo | Teams; central billing, SSO, usage analytics |
| Teams Premium | $120/user/mo | Higher Agent limits than Standard |
| Enterprise | Custom | Pooled usage, invoicing, SCIM, audit logs |

![Cursor official pricing page: Hobby free, Pro $20, Teams $40 per user, Enterprise custom](/cursor-pricing-en-7.jpg)

- **Start (India only):** ₹649 a month, tax included. It covers only Cursor's own models.
- **Annual billing** is offered on the pricing page as an alternative to monthly.

## What each Cursor plan includes

The feature lists below are from Cursor's pricing page and docs (October 11, 2026).

- **Hobby (free):** no credit card, limited Agent requests, access to Composer. You can't pick a specific model; in my test, choosing one asked me to upgrade to Pro.
- **Pro, Pro+ and Ultra:** everything in Hobby plus extended Agent limits, generous Grok usage, frontier models from Anthropic, OpenAI and Google, MCP servers, skills and hooks, cloud agents, and Bugbot code review billed by usage. Cursor's docs add unlimited Tab completions. The three plans differ in how much usage is included, not in features.
- **Teams:** everything in the individual plans plus central billing and admin, a team marketplace for internal rules, skills and plugins, cloud agents and automations with shared team context, usage analytics, team-wide Privacy Mode and SAML/OIDC single sign-on.
- **Enterprise:** pooled usage across the company, invoice and purchase-order billing, SCIM seat management, controls over which repositories, models and MCP servers people can use, audit logs, and priority support.
- **Start (India only):** ₹649 a month for Cursor's own models (Grok 4.7, 4.6, 4.5 and Composer 2.5) at a fixed medium effort. It doesn't include Claude, GPT or Gemini, Auto, or on-demand usage.

### How Auto picks a model

If you leave the model on Auto, Cursor routes each request for you. The docs describe three Auto modes, Cost, Balance and Intelligence, and every mode bills at the list price of whichever model the request was sent to. On the free plan, Auto is the only option; in my test it sent the request to Grok 4.6.

## How Cursor billing works

Cursor's docs split paid usage into two pools that reset every month.

- **Cursor Models pool:** Grok 4.7, Grok 4.6, Grok 4.5 and Composer 2.5. Cursor says this pool has "significantly more included usage."
- **Other Models pool:** Claude, GPT, Gemini and the rest, charged at each model's API price.
- **When you run out:** you can turn on on-demand usage at the same API rates, billed afterwards, or upgrade to a higher plan.
- **Teams and Enterprise:** third-party models carry an extra Cursor Token Rate of $0.25 per million tokens.
- **What the docs don't say:** the dollar size of each plan's included usage is not listed, so you can't calculate exactly when you'll hit the limit.

Cursor's own guide gives a rough picture: daily Tab users and light Agent users usually stay within the included usage, daily Agent users typically spend **$60–$100 a month** in total, and power users running several agents often pass **$200**.

## What changed: from requests to usage

Many older guides describe Cursor Pro as a fixed number of requests a month, with "slow" requests after that and a separate Max Mode billed by tokens. That is no longer how current plans work.

- **Today every plan draws down usage by tokens** at each model's API price, split into the Cursor Models pool and the Other Models pool.
- **Request-based pricing is now listed as legacy.** Cursor's docs keep a "legacy request-based pricing" section for older plans.
- **Max Mode only exists on those legacy plans.** There it extends a model's context window and is billed at the API rate plus 20%.
- **What this means for you:** a long conversation or a large codebase now costs more than a short one, even on the same model, because every token in the context is counted.

## Model prices inside Cursor

![Models available in Cursor settings, including Claude Opus 5.5, Sonnet 5.5, GPT-5.6 Sol, Gemini 3.8 Flash and Grok](/cursor-pricing-en-6.jpg)

Because third-party models are billed at API rates, the model you pick decides how fast your usage goes. Prices per million tokens, from Cursor's docs:

| Model | Input | Output | Pool |
|---|---:|---:|---|
| Composer 2.5 | $0.50 | $2.50 | Cursor Models |
| Grok 4.6 / 4.7 | $2 | $6 | Cursor Models |
| Gemini 3.8 Flash | $0.75 | $3.50 | Other Models |
| Claude Sonnet 5.5 | $2 | $10 | Other Models |
| Claude Opus 5.5 | $4 | $20 | Other Models |
| GPT-5.6 Sol | $4 | $20 | Other Models |
| Claude Fable 5.1 | $10 | $50 | Other Models |

- **Claude Sonnet 5.5 and Opus 5.5 cost the same in Cursor as on Anthropic's API.** The Cursor price list matches Anthropic's official rates for both.
- **Grok 4.6 has the same input price as Sonnet 5.5 but 40% lower output.** Composer 2.5 is the cheapest option on the list.

## What the free Hobby plan actually did

![Cursor free plan result for the brick-breaker prompt: Auto picked Grok 4.6, 1 min 31 s, 398 lines, 15% of the monthly free usage](/cursor-pricing-en-5.jpg)

I installed Cursor on Windows, signed up for the free plan and pasted in the exact prompt from my Claude Code tests: a browser brick-breaker game in a single `index.html` file, with 2 levels, a score, 3 lives, and keyboard and mouse controls.

| Item | Result |
|---|---|
| Model | Auto, which picked Grok 4.6 (medium) |
| Time | 1 min 31 s (shown in Cursor) |
| Game code | 398 lines, ran without errors |
| Free usage spent | 15% of the monthly limit |

- **You can't pick the model on the free plan.** Choosing Claude Sonnet 5.5 or another specific model asked me to upgrade to Pro.
- **15% per run means roughly 6 games like this a month** on the free plan. Bigger tasks will use more.
- **The game was clean but plain.** Rounded bricks, a gradient background, a narrower paddle and a faster ball on level 2, and points that rise toward the top rows. No particles, sound or saved high score.

For comparison, the same prompt in Claude Code took 37 seconds with Sonnet 5.5 at medium effort and 58 seconds at high. The full results are in [Claude Sonnet vs Opus 5.5 for Coding](/blog/claude-sonnet-5-5-vs-opus-5-5).

## What a month of agent use costs on each model

Since Cursor bills Claude at API rates, my Claude Code measurements give a useful reference point. The same game prompt cost:

| Model · effort (Claude Code, API prices) | Cost per run |
|---|---:|
| Sonnet 5.5 · medium | $0.25 |
| Sonnet 5.5 · high | $0.30 |
| Opus 5.5 · medium | $0.56 |
| Opus 5.5 · high | $0.75 |

As a simple example, take 10 tasks of this size per working day, 22 days a month (220 tasks):

- **Sonnet 5.5 high:** about $66 a month
- **Opus 5.5 high:** about $165 a month

That lines up with Cursor's own estimate of $60–$100 a month for daily Agent users. Treat these as ballpark figures: Cursor's agent sends its own instructions and context, so it won't use exactly the same number of tokens as Claude Code, and real tasks vary in size.

## Cursor vs Claude Code vs GitHub Copilot vs Devin: plan prices

Monthly prices before tax, from each company's official pricing page (October 11, 2026).

| Tool | Free | Entry plan | Middle plan | Top individual plan |
|---|---|---:|---:|---:|
| Cursor | Hobby | Pro $20 | Pro+ $60 | Ultra $200 |
| Claude (includes Claude Code) | Free, no Claude Code | Pro $20 | Max 5x $100 | Max 20x $200 |
| GitHub Copilot | Free | Pro $10 | Pro+ $39 | Max $100 |
| Devin (windsurf.com/pricing now points here) | Free | Pro $20 | – | Max $200 |

- **Claude Code comes with Claude Pro and Max.** The free Claude plan doesn't include it. Max plans also include $100–$200 a month in API credits for building on the Claude Platform, according to Anthropic's pricing page.
- **GitHub Copilot is the cheapest entry plan at $10,** and its pricing page lists monthly credits of $15 on Pro, $70 on Pro+ and $200 on Max.
- **Devin's Pro and Max cost the same as Cursor Pro and Ultra.** Its team plan is $80 a month plus $40 per developer seat.
- **The headline price isn't the whole story.** Cursor and Devin let you buy extra usage at API prices, so heavy agent use can cost more than the plan.

## Which Cursor plan should you pick?

![Which Cursor plan should you pick?: If you..., Pick, Why](/cursor-pricing-which-cursor-plan-should-you-pick-en.jpg)

| If you... | Pick | Why |
|---|---|---|
| Just want to try it | Hobby | Free, but Auto model only and about 6 small games a month in my test |
| Use Tab and the agent now and then | Pro ($20) | Cursor says light Agent users often stay within included usage |
| Use the agent every day | Pro+ ($60) | Cursor's own recommendation; daily Agent use runs $60–$100 a month |
| Run several agents or automations | Ultra ($200) | Power users often pass $200 a month in usage |
| Mostly want Claude | Compare with Claude Code first | Same Claude prices; see the comparison below |

- **Pick cheaper models for routine work.** Composer 2.5 and Grok cost less per token than Claude or GPT, and they draw from the separate Cursor Models pool.
- **Watch the usage dashboard.** Both pools are shown in the editor settings and on the dashboard.

## Cursor vs Claude Code on cost

If Claude is the model you want, it's worth comparing with Claude Code before paying for Cursor.

- **Same per-token price:** Cursor charges Claude at Anthropic's API rates, so a Claude task costs about the same either way when you pay by usage.
- **Different plans:** Claude Code is included in Anthropic's Claude subscriptions, which have their own usage limits instead of an API-priced pool. See [Claude Code vs Codex vs Cursor](/blog/claude-code-vs-codex-vs-cursor-cost) and [Claude Code cost per month](/blog/claude-code-cost-per-month) for the plan-by-plan numbers.
- **What Cursor adds:** an editor with Tab completions, its own cheaper models, and the option to switch between Claude, GPT, Gemini and Grok in one place.

## Cursor pros and cons vs Claude Code

Based on Cursor's docs and my own test.

**Pros**

- **Cheaper in-house models.** Composer 2.5 ($0.50/$2.50) and Grok 4.6 ($2/$6) cost less than Claude or GPT and draw from a separate pool with more included usage.
- **Many models in one editor.** Claude, GPT, Gemini, Grok and Muse Spark can all be switched on in Cursor's settings, as the screenshot above shows.
- **Same Claude prices.** Claude Sonnet 5.5 and Opus 5.5 cost the same per token as on Anthropic's API.
- **A free plan to try it.** In my test it built a working game in 1 min 31 s at no cost.

**Cons**

- **The same model doesn't mean the same result.** Each tool wraps the model in its own agent, with its own instructions and context, so Sonnet 5.5 in Cursor won't behave exactly like Sonnet 5.5 in Claude Code.
- **Costs can climb past the plan price.** Once the included usage runs out, on-demand usage is charged by tokens at API rates, so big contexts and expensive models add up fast.
- **Hard to predict.** Cursor doesn't publish the dollar size of each plan's included usage.
- **The free plan is limited.** No model choice, and one small game used 15% of the month.

**Avoiding a surprise bill**

- **Leave on-demand usage off** until you know how quickly you use up your included usage.
- **Split big jobs into smaller tasks** instead of handing one huge request to the most expensive model.
- **Use Composer or Grok for routine edits** and save Claude Opus or GPT-5.6 Sol for the hard parts.
- **Check the usage dashboard weekly.** Both pools are shown there.

## Verdict: free to try, Pro+ for daily agent work

- **The free plan is a real trial, not a working plan.** It ran a small game in 1 min 31 s, but used 15% of the month and wouldn't let me choose the model.
- **Pro at $20 suits light agent use.** Daily agent users should expect $60–$100 a month in usage, which is why Cursor recommends Pro+.
- **The model matters more than the plan.** Claude Opus 5.5 cost 150% more per task than Sonnet 5.5 at high effort in my test ($0.75 vs $0.30), and Composer and Grok are cheaper still.

## FAQ

**Is Cursor free?**
Yes, the Hobby plan is free with no credit card, but Agent requests are limited and the model is chosen automatically. In my test one small game used 15% of the monthly limit.

**How much is Cursor Pro?**
$20 a month before tax. Pro+ is $60 and Ultra is $200.

**Does Cursor charge more for Claude?**
No, not on individual plans. Cursor lists Claude Sonnet 5.5 at $2/$10 and Opus 5.5 at $4/$20 per million tokens, the same as Anthropic's API. Teams and Enterprise add $0.25 per million tokens for third-party models.

**Does Cursor have a student discount?**
Not a standing one. Cursor's student page says anyone can start for free and that upgrades will come through promotions at on-campus and online events. Older posts about a free year for students may be out of date, so check the student page before you rely on one.

**What happens when I run out of usage?**
You can turn on on-demand usage at the same API rates or upgrade your plan. Cursor says requests are never downgraded in quality or speed.

## Run the numbers for your own work

In the [coding agent cost calculator](/agents), enter your task size and tasks per day to compare a month on Claude Opus 5.5, Sonnet 5.5 and other models. To check what a single prompt costs, use the [token counter](/).

*Prices checked October 11, 2026. The free plan test was a single run; results will vary with the model Auto picks and the size of the task.*

## Sources

- [Cursor: Pricing](https://cursor.com/pricing)
- [Cursor Docs: Models & Pricing](https://cursor.com/docs/models-and-pricing)
- [Anthropic: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Cursor: Students](https://cursor.com/students)
- [Claude: Plans and pricing](https://claude.com/pricing)
- [GitHub Copilot: Plans and pricing](https://github.com/features/copilot/plans)
- [Devin: Plans and pricing](https://devin.ai/pricing)
<!-- autoimg -->
