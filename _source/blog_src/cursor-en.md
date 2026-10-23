![Cursor Pricing 2026: Plans, Usage Pools and Real Monthly Cost](/cursor-pricing-en.jpg)

How much does **Cursor** cost in 2026? In October Cursor's pricing changed completely: it is now sold as part of **The X Subscription**, one subscription for Grok, Cursor and X, with plans from $8 to $200 a month. The bigger change is what the plans cover. The included usage is for Cursor's own models (Grok and Composer) only. **Claude, GPT and Gemini are no longer included in any plan**; on Premium and above you pay for them separately at API list price.

I rechecked Cursor's pricing page and its models and pricing docs on October 23, 2026. Earlier, on October 11, I installed Cursor on Windows and gave the free plan the same brick-breaker prompt I used to measure Claude Opus 5.5 and Sonnet 5.5 in Claude Code. Below are the new plans, how billing works now, what the free plan did, and what a month of agent use costs on each model.

## Cursor pricing plans (2026)

Prices from Cursor's official pricing page and docs, checked October 23, 2026. Prices exclude tax.

| Plan | Price | Included usage | Claude, GPT, Gemini |
|---|---:|---|---|
| Free | $0 | Limited | Not available |
| Plus | $8/mo | Base (Grok and Composer only) | Not available |
| Premium | $30/mo | 400% of Plus | API list price, from prepaid credit |
| Super | $100/mo | 1,500% of Plus | API list price, from prepaid credit |
| Ultra | $200/mo | 5,000% of Plus | API list price, from prepaid credit |
| Teams | $30, $100 or $200 per seat/mo | Same as the matching plan | API list price plus $0.25 per million tokens |
| Enterprise | Custom | Pooled | API list price plus $0.25 per million tokens |

- **Annual billing:** $80 a year for Plus, $300 for Premium, $1,000 for Super and $2,000 for Ultra.
- **The plans are shared with Grok and X.** The same subscription covers the Grok apps, Grok API access and X Premium features such as the checkmark and fewer ads.
- **Old plans keep working.** Hobby, Start, Pro ($20), Pro+ ($60), Ultra and the Teams Standard ($40) and Teams Premium ($120) seats are now listed as legacy plans. Existing customers stay on them, with two monthly usage pools and on-demand usage.

## What each Cursor plan includes

From Cursor's docs (October 23, 2026).

- **Free:** Agent and Chat with limited usage.
- **Plus ($8):** Agent with Cursor's own models only (Grok 4.7, 4.6, 4.5 and Composer 2.5) at fixed settings: medium effort, Fast off. No Auto, cloud agents, Bugbot code review, third-party models or your own API keys.
- **Premium ($30):** 400% of Plus's usage, plus cloud agents and automations, code hosting on Origin, Bugbot code review, third-party models at API list price, and Grok Bot. Cursor suggests it for new Agent users.
- **Super ($100):** 1,500% of Plus's usage and priority model access at peak times. Cursor suggests it for daily Agent users.
- **Ultra ($200):** 5,000% of Plus's usage and earliest access to new models. Cursor suggests it for power users running several agents or automations.
- **Teams:** each member gets a Premium, Super or Ultra seat at the individual price, and seat types can be mixed. Teams add central billing and admin, a team marketplace for rules, skills and plugins, usage analytics, team-wide privacy mode and SAML/OIDC single sign-on. Plus isn't available for teams.
- **Enterprise:** pooled usage across Grok and Cursor, invoicing, SCIM, granular spend controls and audit logs.

### How Auto picks a model

On individual plans Auto has one mode, Cost (classic Auto), which bills as a Cursor-model request and draws from your weekly pool whatever model serves it. On Teams and Enterprise, the Balance and Intelligence modes can route a request to Claude or GPT, and that route is billed as third-party usage.

## How Cursor billing works

- **One weekly pool for Cursor models.** Each paid plan includes usage for Grok 4.7, 4.6, 4.5 and Composer 2.5. The pool is shared across the editor, the CLI, cloud agents, Grok Bot and the Grok apps, and it refreshes every week.
- **Third-party models are always extra.** Claude, GPT and Gemini aren't part of the pool. On Premium and above they are charged at the model's API list price from the first request, paid from prepaid credit. Plus and Free can't use them.
- **Prepaid credit and caps.** You top up credit (or turn on Auto Top-up), and a monthly limit caps how much extra usage you can spend. Credit also pays for Cursor models after the weekly pool runs out.
- **Teams and Enterprise:** third-party requests carry an extra Cursor Token Rate of $0.25 per million tokens, except on a list of small models such as Claude Haiku 5.5 and GPT-5.6 Luna. Individual plans don't pay it.
- **What the docs don't say:** the dollar size of each plan's weekly pool. Your remaining usage and next reset are shown in the editor settings and on the Grok dashboard.

## What changed in October 2026

| | Before (until mid-October) | Now (The X Subscription) |
|---|---|---|
| Plans | Hobby, Pro $20, Pro+ $60, Ultra $200 | Free, Plus $8, Premium $30, Super $100, Ultra $200 |
| Teams | Standard $40, Premium $120 per user | $30, $100 or $200 per seat |
| Included usage | Two monthly pools: Cursor models and other models | One weekly pool, Cursor models only |
| Claude, GPT, Gemini | Drawn from the plan's included "Other Models" pool | Not included; API list price from prepaid credit |
| Running out | On-demand usage, billed afterwards | Wait for the weekly reset or use prepaid credit |

Many older guides also describe Cursor Pro as a fixed number of requests a month, with "slow" requests after that and a separate Max Mode. That request-based pricing is now a legacy plan, and Max Mode exists only there, billed at the API rate plus 20%.

## Model prices inside Cursor

![Models available in Cursor settings, including Claude Opus 5.5, Sonnet 5.5, GPT-5.6 Sol, Gemini 3.8 Flash and Grok](/cursor-pricing-en-6.jpg)

Prices per million tokens, from Cursor's docs (October 23, 2026). Cursor models use these rates only when you buy usage beyond the weekly pool.

| Model | Input | Output | Paid from |
|---|---:|---:|---|
| Composer 2.5 | $0.50 | $2.50 | Weekly pool |
| Grok 4.6 / 4.7 | $2 | $6 | Weekly pool |
| Gemini 3.8 Flash | $0.75 | $3.75 | Prepaid credit |
| Claude Sonnet 5.5 | $2 | $10 | Prepaid credit |
| Claude Opus 5.5 | $4 | $20 | Prepaid credit |
| GPT-5.6 Sol | $4 | $20 | Prepaid credit |
| Claude Fable 5.1 | $10 | $50 | Prepaid credit |

- **Claude Sonnet 5.5 and Opus 5.5 cost the same in Cursor as on Anthropic's API.** The difference is that none of it is covered by the plan any more.
- **Grok 4.6 has the same input price as Sonnet 5.5 but 40% lower output,** and it comes out of the included pool. Composer 2.5 is the cheapest option on the list.

## What the free plan actually did

![Cursor free plan result for the brick-breaker prompt: Auto picked Grok 4.6, 1 min 31 s, 398 lines, 15% of the monthly free usage](/cursor-pricing-en-5.jpg)

I tested this on October 11, when the free plan was still called Hobby. I installed Cursor on Windows, signed up and pasted in the exact prompt from my Claude Code tests: a browser brick-breaker game in a single `index.html` file, with 2 levels, a score, 3 lives, and keyboard and mouse controls.

| Item | Result |
|---|---|
| Model | Auto, which picked Grok 4.6 (medium) |
| Time | 1 min 31 s (shown in Cursor) |
| Game code | 398 lines, ran without errors |
| Free usage spent | 15% of the monthly limit |

- **You couldn't pick the model on the free plan.** Choosing Claude Sonnet 5.5 asked me to upgrade. Under the new plans, Free and Plus can't use Claude at all.
- **15% per run meant roughly 6 games like this a month.** The new plans measure usage weekly, so the free limit may now work out differently.
- **The game was clean but plain.** Rounded bricks, a gradient background, a narrower paddle and a faster ball on level 2, and points that rise toward the top rows. No particles, sound or saved high score.

For comparison, the same prompt in Claude Code took 37 seconds with Sonnet 5.5 at medium effort and 58 seconds at high. The full results are in [Claude Sonnet vs Opus 5.5 for Coding](/blog/claude-sonnet-5-5-vs-opus-5-5).

## What a month of agent use costs on each model

Cursor now bills Claude entirely at API rates, so my Claude Code measurements give a direct reference point. The same game prompt cost:

| Model · effort (Claude Code, API prices) | Cost per run |
|---|---:|
| Sonnet 5.5 · medium | $0.25 |
| Sonnet 5.5 · high | $0.30 |
| Opus 5.5 · medium | $0.56 |
| Opus 5.5 · high | $0.75 |

As a simple example, take 10 tasks of this size per working day, 22 days a month (220 tasks):

- **Sonnet 5.5 high in Cursor:** about $66 of prepaid credit, plus at least $30 for Premium, so about **$96 a month**
- **Opus 5.5 high in Cursor:** about $165 of credit plus $30, so about **$195 a month**
- **Grok or Composer:** covered by the weekly pool until it runs out, so the plan price may be all you pay

Treat these as ballpark figures: Cursor's agent sends its own instructions and context, so it won't use exactly the same number of tokens as Claude Code, and real tasks vary in size.

## Cursor vs Claude Code vs GitHub Copilot vs Devin: plan prices

Monthly prices before tax, from each company's official pricing page (Cursor checked October 23, the others October 11, 2026).

| Tool | Free | Entry plan | Middle plan | Top individual plan |
|---|---|---:|---:|---:|
| Cursor | Free | Plus $8 (Grok and Composer only) | Premium $30 / Super $100 | Ultra $200 |
| Claude (includes Claude Code) | Free, no Claude Code | Pro $20 | Max 5x $100 | Max 20x $200 |
| GitHub Copilot | Free | Pro $10 | Pro+ $39 | Max $100 |
| Devin (windsurf.com/pricing now points here) | Free | Pro $20 | – | Max $200 |

- **Claude Code comes with Claude Pro and Max,** and their usage limits cover Claude models. In Cursor, the same Claude usage is paid on top of the plan.
- **GitHub Copilot is the cheapest entry plan with Claude and GPT,** at $10, and its pricing page lists monthly credits of $15 on Pro, $70 on Pro+ and $200 on Max.
- **Cursor Plus at $8 is the cheapest paid plan here,** but only for Grok and Composer.
- **The headline price isn't the whole story.** Cursor and Devin charge extra usage at API prices, so heavy agent use can cost more than the plan.

## Which Cursor plan should you pick?

| If you... | Pick | Why |
|---|---|---|
| Just want to try it | Free | Limited usage, Cursor models only |
| Are happy with Grok and Composer | Plus ($8) | Cheapest paid plan; no Claude, GPT or cloud agents |
| Want Claude or GPT now and then | Premium ($30) | Third-party models open up, paid per use from credit |
| Use the agent every day | Super ($100) | Cursor's own suggestion for daily Agent users |
| Run several agents or automations | Ultra ($200) | 5,000% of Plus's usage |
| Mostly want Claude | Compare with Claude Code first | In Cursor every Claude token is extra; see below |

- **Pick Grok or Composer for routine work.** They come out of the included weekly pool; Claude, GPT and Gemini always cost extra.
- **Set a monthly limit on extra usage** before you use third-party models, so a long session can't run up the bill.

## Cursor vs Claude Code on cost

If Claude is the model you want, compare with Claude Code before paying for Cursor.

- **Same per-token price, different coverage:** Cursor charges Claude at Anthropic's API rates, and since October none of that is included in the plan. A Claude subscription includes Claude Code usage up to its limits.
- **A rough comparison:** for the $66 a month of Sonnet usage in the example above, Cursor costs the plan plus the full $66. On a Claude plan the same work is a flat $20 to $200, as long as it fits the plan's usage limits. See [Claude Code vs Codex vs Cursor](/blog/claude-code-vs-codex-vs-cursor-cost) and [Claude Code cost per month](/blog/claude-code-cost-per-month) for the plan-by-plan numbers.
- **What Cursor adds:** an editor with Tab completions, Grok and Composer in the included pool, and the option to switch between Claude, GPT, Gemini and Grok in one place.

## Cursor pros and cons vs Claude Code

Based on Cursor's docs and my own test.

**Pros**

- **Cheap entry for its own models.** Plus at $8 covers Grok and Composer, and every paid plan has a weekly pool for them.
- **Many models in one editor.** Claude, GPT, Gemini, Grok and Muse can all be used in Cursor, as the screenshot above shows.
- **Same Claude prices as the API.** Claude Sonnet 5.5 and Opus 5.5 cost the same per token as on Anthropic's API.
- **A free plan to try it.** In my test it built a working game in 1 min 31 s at no cost.

**Cons**

- **Claude and GPT are always extra.** No plan includes them any more, so Claude-heavy work costs the plan price plus API prices.
- **The same model doesn't mean the same result.** Each tool wraps the model in its own agent, so Sonnet 5.5 in Cursor won't behave exactly like Sonnet 5.5 in Claude Code.
- **Hard to predict.** Cursor doesn't publish the dollar size of each plan's weekly pool.
- **Bundled with X.** The plans now come as one subscription with Grok and X Premium, whether you want those or not.

**Avoiding a surprise bill**

- **Set the monthly limit on additional usage** before turning on Auto Top-up.
- **Split big jobs into smaller tasks** instead of handing one huge request to the most expensive model.
- **Use Grok or Composer for routine edits** and save Claude Opus or GPT-5.6 Sol for the hard parts.
- **Check the usage dashboard weekly,** since the pool now resets every week.

## Verdict: Plus for Grok, Claude Code for Claude

- **For Grok and Composer, Cursor is now cheap.** Plus at $8 covers them, and Super at $100 is Cursor's pick for daily agent work.
- **For Claude, Cursor is now the expensive route.** Every Claude token is paid at API price on top of the plan, while Claude Pro and Max include Claude Code usage.
- **The model matters more than the plan.** Claude Opus 5.5 cost 150% more per task than Sonnet 5.5 at high effort in my test ($0.75 vs $0.30), and Grok and Composer come out of the included pool.

## FAQ

**Is Cursor free?**
Yes, the Free plan costs nothing but has limited usage and only Cursor's own models. In my October 11 test, one small game used 15% of the free monthly limit.

**How much is Cursor Pro?**
Pro ($20) and Pro+ ($60) are now legacy plans for existing customers. New subscribers choose Plus ($8), Premium ($30), Super ($100) or Ultra ($200).

**Can I use Claude in Cursor?**
On Premium and above, yes, at Anthropic's API list price paid from prepaid credit: Sonnet 5.5 at $2/$10 and Opus 5.5 at $4/$20 per million tokens. Plus and Free can't use Claude. Teams and Enterprise add $0.25 per million tokens.

**How much is Cursor for teams?**
$30, $100 or $200 per seat a month, matching Premium, Super and Ultra. Seat types can be mixed on one team.

**What happens when I run out of usage?**
Wait for the weekly reset, keep working with prepaid credit at the same per-model rates, or upgrade. Cursor says requests are never downgraded in quality or speed.

## Run the numbers for your own work

In the [coding agent cost calculator](/agents), enter your task size and tasks per day to compare a month on Claude Opus 5.5, Sonnet 5.5 and other models. To check what a single prompt costs, use the [token counter](/).

*Prices checked October 23, 2026 (first published October 11). The free plan test was a single run on the earlier Hobby plan; results will vary with the model Auto picks and the size of the task.*

## Sources

- [Cursor: Pricing](https://cursor.com/pricing)
- [Cursor Docs: Models & Pricing](https://cursor.com/docs/models-and-pricing)
- [Anthropic: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Claude: Plans and pricing](https://claude.com/pricing)
- [GitHub Copilot: Plans and pricing](https://github.com/features/copilot/plans)
- [Devin: Plans and pricing](https://devin.ai/pricing)
