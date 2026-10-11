![GitHub Copilot Pricing 2026: Plans, AI Credits and Real Cost](/github-copilot-pricing-en.jpg)

GitHub Copilot no longer counts "premium requests." Since June 1, 2026, every individual plan includes a monthly allowance of GitHub AI Credits, and each chat, agent session or CLI task spends those credits at the model's per-token price. This page covers the current plans and prices, how the credits work, what each model costs inside Copilot, and how many real coding tasks each plan's credits cover, using four agent runs we measured ourselves. Plan details were checked on GitHub's plans page and documentation on October 11, 2026.

## GitHub Copilot pricing plans (2026)

![GitHub Copilot pricing plans (2026): Plan, Price per month, Monthly AI credits (base + flex), Value of credits](/github-copilot-pricing-github-copilot-pricing-plans-2026-en.jpg)

| Plan | Price per month | Monthly AI credits (base + flex) | Value of credits |
|---|---:|---:|---:|
| Free | $0 | Limited allowance, auto model only | – |
| Pro | $10 | 1,000 + 500 = 1,500 | $15 |
| Pro+ | $39 | 3,900 + 3,100 = 7,000 | $70 |
| Max | $100 | 10,000 + 10,000 = 20,000 | $200 |
| Business | $19 per user | 1,900 per user, pooled | $19 |
| Enterprise | $39 per user | 3,900 per user, pooled | $39 |

- **One AI credit is worth $0.01.** So Pro's 1,500 credits are $15 of model usage, Pro+'s are $70 and Max's are $200.
- **Base credits match the price.** Pro's 1,000 base credits are exactly its $10 price. On top of that comes a **flex allotment**, which GitHub says is "a variable part of your included usage" that can change as model prices change.
- **On the individual plans, the flex allotment is where the extra value is.** Pro gives you 50% more usage than you pay for, Pro+ 79% more and Max 100% more, as long as the flex amounts stay where they are.
- **Business and Enterprise have no flex allotment.** Their 1,900 and 3,900 credits per user are pooled across the whole organization, so heavy users can draw from light users' share.
- **Code completions are free on paid plans.** Inline suggestions and next edit suggestions don't use AI credits and stay unlimited on Pro, Pro+ and Max. The free plan includes 2,000 code completions a month.

## What each plan includes

According to GitHub's plans page:

- **Free:** 2,000 code completions a month, a limited allowance of chat and agent use, access to lightweight models such as Claude Haiku 4.5 and GPT-5 mini through auto model selection, and Copilot CLI. Verified students get Copilot Student instead, with unlimited completions.
- **Pro ($10):** everything in Free, plus unlimited completions and next edit suggestions, Copilot cloud agent and code review, and model choice.
- **Pro+ ($39):** everything in Pro, plus delegating tasks to third-party coding agents such as Claude by Anthropic and OpenAI Codex (in preview), and 367% more included credits than Pro.
- **Max ($100):** everything in Pro+, plus priority access to new models and features, and 186% more included credits than Pro+.

All paid plans can buy extra credits once the included ones run out.

## How GitHub AI Credits work

Every interaction uses tokens: input tokens sent to the model, output tokens it writes, and cached tokens it reuses. GitHub prices each token at the model's rate and converts the total into credits. Two things decide the cost of a task: **the model** and **how many tokens the task uses**.

- **What uses credits:** Copilot Chat, Copilot CLI, Copilot cloud agent, Copilot Spaces, Spark, and third-party coding agents.
- **What doesn't:** code completions and next edit suggestions on paid plans.
- **Code review is billed twice.** The tokens are billed in credits, and the agent that runs the review also uses GitHub Actions minutes. The model for code review is picked automatically and not shown, so its cost per review varies.
- **Base credits go first, then flex.** Your usage dashboard shows both.
- **Credits reset on the 1st of every month at 00:00 UTC**, no matter when you subscribed. Unused credits don't carry over.
- **Auto model selection is 10% cheaper.** On paid plans, letting Copilot pick the model gives a 10% discount on model costs in Chat, CLI, the Copilot app and the cloud agent.

### When you run out

GitHub gives three options:

1. **Upgrade.** You only pay the price difference between plans for the rest of the cycle, and the larger allowance is available immediately.
2. **Set a budget for extra usage.** Extra usage is billed at the same per-token rates; a $10 budget buys 1,000 credits.
3. **Wait** for the reset on the 1st of the month.

Annual Pro and Pro+ subscribers who stayed on the old system after June 1, 2026 stay on the older premium-request billing for now; check your billing page if that's you.

## What each model costs inside Copilot

![What each model costs inside Copilot: Model, Input, Cached input, Cache write, Output](/github-copilot-pricing-what-each-model-costs-inside-copilot-en.jpg)

GitHub publishes a per-token price for every model. For the models people use most for coding, the rates in Copilot match the providers' own API list prices:

| Model | Input | Cached input | Cache write | Output |
|---|---:|---:|---:|---:|
| Claude Haiku 5.5 | $0.10 | $0.01 | $0.125 | $0.50 |
| Claude Sonnet 5.5 | $2 | $0.10 | $2.50 | $10 |
| Claude Opus 5.5 | $4 | $0.20 | $5 | $20 |
| Claude Fable 5.1 | $10 | $0.25 | $12.50 | $50 |
| GPT-6 Luna | $0.10 | $0.01 | $0.125 | $0.50 |
| GPT-6.1 Sol | $2 | $0.10 | $2.50 | $10 |
| GPT-6 Astra | $10 | $1 | $12.50 | $50 |
| Gemini 3.8 Flash | $0.75 | $0.075 | – | $3.75 |
| Grok 4.7 | $2 | $0.50 | – | $6 |

Prices per million tokens, for prompts under each model's long-context threshold. Several models cost more above it: for example, GPT-6 Astra above 272K input tokens is $20 input and $75 output. Gemini 3.8 Flash is at a promotional price until December 31, 2026.

- **Copilot charges what the API would.** Claude Sonnet 5.5 costs $2 and $10 per million tokens both in Copilot and on Anthropic's API, and GPT-6 Astra $10 and $50 in both. There is no Copilot markup and no Copilot discount on these rates, apart from the 10% for auto selection.
- **In practice, a plan works like prepaid API usage with extra credits on top.** Pro's $10 buys $15 of model usage; Max's $100 buys $200.
- **Model choice changes your month more than plan choice.** A token on Claude Opus 5.5 costs 100% more than on Sonnet 5.5, and GPT-6 Astra costs 400% more than GPT-6.1 Sol.

## How many coding tasks does each plan cover?

![How many coding tasks does each plan cover?: One task like ours, Cost per run, Pro ($15 of credits), Pro+ ($70), Max ($200)](/github-copilot-pricing-how-many-coding-tasks-does-each-plan-cov-en.jpg)

Because Copilot charges list API prices, you can estimate a plan's capacity from what real tasks cost. We measured four agent runs on October 9, 2026: the same small browser game built by Claude Sonnet 5.5 and Opus 5.5 at medium and high effort, in Claude Code, with costs converted at API prices by ccusage. The full test is in [Sonnet vs Opus 5.5](/blog/claude-sonnet-5-5-vs-opus-5-5).

| One task like ours | Cost per run | Pro ($15 of credits) | Pro+ ($70) | Max ($200) |
|---|---:|---:|---:|---:|
| Sonnet 5.5, medium | $0.25 | about 60 | about 280 | about 800 |
| Sonnet 5.5, high | $0.30 | about 50 | about 233 | about 667 |
| Opus 5.5, medium | $0.56 | about 27 | about 125 | about 357 |
| Opus 5.5, high | $0.75 | about 20 | about 93 | about 267 |

These are our estimates, and they come with real caveats:

- **The runs were in Claude Code, not Copilot.** Copilot's agent sends its own instructions and context, so the same task will not use exactly the same tokens.
- **Most of our cost was cache writes.** In those runs, 63% to 81% of the cost came from writing context into the prompt cache at Anthropic's 1-hour rate. Copilot lists a cache-write price of $2.50 for Sonnet 5.5, which matches Anthropic's 5-minute rate. If Copilot caches at that rate, the same task would cost less, and each plan would cover more tasks. We haven't measured it.
- **The game was small.** Real features on a real codebase read more files and run more steps. Expect a bigger task to cost more, possibly much more.

Still, the order of magnitude is useful. Pro covers a few dozen small agent tasks a month on Sonnet, and well under that on Opus. By our estimate, if you use the agent daily, Pro+ is the first plan with enough credits for a full month of small tasks. Where all those tokens go, and why cache writes dominate, is in [How much does a Claude token cost?](/blog/claude-token-cost)

## Free vs Pro vs Pro+ vs Max: which to pick

| If you... | Pick | Why |
|---|---|---|
| Mostly want autocomplete, with a little chat | Free, then Pro | Free has 2,000 completions; Pro makes them unlimited for $10 |
| Use chat and agent mode a few times a week on Sonnet-class models | Pro ($10) | $15 of credits covers a few dozen small tasks |
| Use the agent every day | Pro+ ($39) | $70 of credits, plus third-party agents (preview) |
| Run long agent sessions or many cloud-agent tasks | Max ($100) | $200 of credits, the best ratio of credits to price |
| Work in a company that wants pooled usage and admin controls | Business ($19) or Enterprise ($39) | Credits pooled across users; no flex allotment |

Two habits change your bill as much as the plan does:

- **Default to a cheaper model.** Use auto selection for the 10% discount, Sonnet 5.5 or GPT-6.1 Sol for most coding, and Opus or GPT-6 Astra only when a task needs it.
- **Keep agent sessions short.** Long sessions resend more context at every step. Start a new session for each separate task.

## Copilot Business and Enterprise

For companies, Copilot Business costs $19 and Enterprise $39 per user per month, with 1,900 and 3,900 AI credits per user. The difference from the individual plans is how the credits are shared:

- **Credits are pooled.** GitHub's example: a company with 100 Business users gets one shared pool of 190,000 credits, not 100 separate allowances. Heavy users can draw more while light users offset them.
- **Adding seats grows the pool immediately.** Removing seats mid-cycle doesn't shrink it until the next cycle.
- **There is no flex allotment**, so the included credits equal the seat price.
- **Running out works differently.** Depending on the company's policy, usage either continues as paid overage or is blocked; users can't buy credits themselves.
- **A work seat replaces a personal plan.** If you have Pro, Pro+ or Max and your company assigns you a Business or Enterprise seat, your personal plan is canceled automatically with a prorated refund.

## Copilot vs Cursor vs Claude Code vs Codex: plan prices

| Tool | Free | Entry | Middle | Top individual |
|---|---|---:|---:|---:|
| GitHub Copilot | Free | Pro $10 | Pro+ $39 | Max $100 |
| Cursor | Hobby | Pro $20 | Pro+ $60 | Ultra $200 |
| Claude (includes Claude Code) | Free, no Claude Code | Pro $20 | Max 5x $100 | Max 20x $200 |
| ChatGPT (includes Codex) | Free, limited Codex | Plus $20 | Pro 100 $100 | Pro 500 $500 |

- **Copilot is the cheapest way in.** Pro at $10 is half the entry price of the others, and its credits are clearly stated in dollars.
- **Claude and ChatGPT plans are allowance-based, not credit-based.** They give you usage limits that reset on a schedule rather than a dollar balance, so they're harder to compare directly. Their allowances aren't tied to API prices, so the value per dollar depends on how you use them.
- **Cursor and Copilot both price usage per token.** Both include a pool of usage with the plan; Cursor adds its own token rate on third-party models, while Copilot charges the list price. See [Cursor pricing](/blog/cursor-pricing) for how Cursor's pools work.

For a fuller comparison of monthly cost by workload, see [Claude Code vs Codex vs Cursor: cost](/blog/claude-code-vs-codex-vs-cursor-cost) or the [coding agent cost calculator](/agents).

## Verdict

- **Copilot Pro at $10 is the cheapest paid plan of the four compared here**, with unlimited completions and $15 of model credits.
- **Every plan is effectively prepaid API usage.** Copilot charges each model's list price, so your month depends on which models you use and how long your agent sessions run.
- **The flex allotment adds the most on Max,** taking it from $100 to $200 of usage, but GitHub says it can change.
- **By our estimate, daily agent users will want Pro+.** Pro's credits cover a few dozen small Sonnet tasks a month by our estimate; Pro+ covers a few hundred.

## FAQ

**How much does GitHub Copilot cost in 2026?**
Copilot Free is $0, Pro is $10 a month, Pro+ is $39 and Max is $100. For teams, Business is $19 and Enterprise $39 per user per month.

**What are GitHub AI Credits?**
They are Copilot's usage currency since June 1, 2026. One credit is worth $0.01, and each interaction spends credits at the model's per-token price. Pro includes 1,500 credits a month, Pro+ 7,000 and Max 20,000.

**Is GitHub Copilot free?**
Yes, there is a free plan with 2,000 code completions a month and a limited allowance of chat and agent use through auto model selection. Verified students can get Copilot Student, with unlimited completions.

**Do code completions use AI credits?**
No. Code completions and next edit suggestions are not billed in credits and are unlimited on all paid plans.

**What happens when I run out of Copilot credits?**
You can upgrade and pay only the difference for the rest of the month, set a budget to buy more credits at the same per-token rates, or wait for the reset at 00:00 UTC on the 1st.

**Is Copilot cheaper than Claude Code or Cursor?**
At the entry level, yes: $10 against $20. For heavy agent use it depends on the model and how much you use; Copilot charges full API prices for each model, while Claude's plans use allowances that aren't tied to API prices.

## Run the numbers

The [coding agent cost calculator](/agents) estimates a month of agent work on Claude Opus 5.5, Sonnet 5.5 or GPT-6 models from your task size and tasks per day, which you can compare with Copilot's $15, $70 and $200 of credits. For one prompt, the [token counter](/) shows the exact cost on each model.

*Plan details and model prices checked on GitHub's plans page and documentation on October 11, 2026. Task estimates use our Claude Code measurements from October 9, 2026, one run each.*

## Sources

- [GitHub: Copilot plans and pricing](https://github.com/features/copilot/plans)
- [GitHub Docs: Usage-based billing for individuals](https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing)
- [GitHub Docs: Models and pricing for GitHub Copilot](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)
- [GitHub Docs: Usage-based billing for organizations and enterprises](https://docs.github.com/en/copilot/concepts/billing-and-usage/organizations-and-enterprises/billing)
- [GitHub Docs: Requests in GitHub Copilot (legacy)](https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/copilot-requests)
- [Anthropic: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI: API pricing](https://developers.openai.com/api/docs/pricing)
<!-- autoimg -->
