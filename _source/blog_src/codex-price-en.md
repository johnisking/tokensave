![Codex Pricing 2026: Free, Plus and Pro Plans, Credits and API](/codex-pricing-en.jpg)

Codex pricing is simpler than it looks, and you may already be paying for it. OpenAI's coding agent is included in every ChatGPT plan, from Free at $0 to Pro 500 at $500 a month, and there is a separate pay-as-you-go route through an API key. What changes between plans is which models you get, whether you can run cloud tasks, and how much you can do before you hit a limit. This guide covers each plan, how Codex credits work, what the API costs, and what happened when we built the same small game twice on the free plan.

## Codex pricing at a glance (2026)

| Plan | Price per month (US) | Codex models | 5-hour limit | Cloud tasks |
|---|---:|---|---|:---:|
| Free | $0 | GPT-6 Luna (desktop app) | None seen; one monthly meter | – |
| Go | $8 | GPT-6 Luna (desktop app) | Not published | – |
| Plus | $20 | GPT-6 Astra, 6.1 Sol, 6 Sol, Luna | Yes | ✓ |
| Pro 100 / 200 / 500 | $100 / $200 / $500 | Same as Plus, Ultrafast on Pro 500 | None | ✓ |
| Business | $20 per user (annual), $25 (monthly) | Same as Plus | Yes, same as Plus | ✓ |
| Enterprise and Edu | Contact sales | Same as Plus | Depends on contract | ✓ |
| API key | Pay per token | API models | None (pay per use) | – |

- **Codex is not a separate subscription.** OpenAI's pricing page says ChatGPT Work and Codex are included in the Free, Go, Plus, Pro, Business, Edu and Enterprise plans. There is no "Codex Pro" to buy on its own.
- **The free plan really includes Codex.** It runs GPT-6 Luna at standard speed in the desktop app, subject to rollout. OpenAI describes it as a way to explore Codex on quick coding tasks.
- **Cloud tasks start at Plus.** Codex Cloud, which runs tasks on OpenAI's servers and connects to GitHub for code review, is available on eligible Plus accounts, all Pro tiers, Business, Enterprise, Healthcare and Education. Free and Go are local only.
- **The API key route has no cloud features.** You can use your own API key with the Codex CLI, SDK and IDE extension, and you pay standard API rates, but GitHub review, Slack and other cloud integrations are not available that way.

## What each plan gets in Codex

The plans differ in more than the size of the allowance. Going by OpenAI's pricing page and help center:

- **Free ($0):** GPT-6 Luna at standard speed in the desktop app. No cloud tasks and no image generation (to price images through the API instead, see the [image cost calculator](/image)). OpenAI doesn't publish a usage limit for Free; it only says limits vary by plan. On our free account, the Codex app showed a single meter for remaining usage, labeled one month, with a reset date one month out. There was no 5-hour or weekly meter. Credit purchases are open to a limited group of Free users.
- **Go ($8):** the same GPT-6 Luna access as Free, positioned for lightweight coding tasks. Go adds more general ChatGPT usage, but for Codex the published access is the same as Free.
- **Plus ($20):** Codex on the web, the CLI, the IDE extension and iOS, plus cloud integrations. Plus can use the full GPT-6 line, from GPT-6 Astra for hard problems to GPT-6 Luna for quick edits, within a rolling 5-hour window. Plus users can buy extra credits when they hit a limit.
- **Pro ($100, $200 or $500):** everything in Plus with a bigger allowance and, for now, no 5-hour limit. The allowance is weekly. Pro 500 adds Ultrafast mode for GPT-6 Astra and GPT-6.1 Sol. For how the three Pro tiers compare, see [ChatGPT Plus vs Pro](/blog/chatgpt-plus-vs-pro).
- **Business ($20 or $25 per user):** the Standard seat has roughly the same Codex limits as Plus, and the workspace can buy Codex credit plans. Teams need at least two users.
- **Enterprise and Edu:** priced by contract. With flexible pricing there are no fixed rate limits and usage is billed in credits; without it, the per-seat limits are roughly the same as Plus.

On every plan, Codex shares one allowance with ChatGPT Work, ChatGPT for Excel and Workspace Agents. A long Codex session can leave less room for the other agent features, and the reverse is also true.

## Codex usage limits by model

![Codex usage limits by model: Model, Local messages per 5 hours (Plus and Business Standard)](/codex-pricing-codex-usage-limits-by-model-en.jpg)

OpenAI publishes estimated local messages per 5-hour window for Plus and Business Standard seats. These are ranges, not fixed limits:

| Model | Local messages per 5 hours (Plus and Business Standard) |
|---|---:|
| GPT-6 Astra | 5–45 |
| GPT-6.1 Sol | 15–160 |
| GPT-6 Sol | 15–150 |
| GPT-6 Luna | 350–3,000 |

- **The model is the biggest lever.** At the low end of each range, GPT-6 Luna gives you 7,000% as many messages as GPT-6 Astra (350 against 5). Picking Luna for simple edits and Astra only for hard bugs stretches a plan much further than upgrading does.
- **The ranges are wide because tasks are.** A message that reads a few files costs far less than one that reads half a repository, plans, writes and runs tests. Cloud tasks can use more of the allowance than local messages.
- **Weekly limits may also apply** on top of the 5-hour window.
- **Pro has no 5-hour window** at the moment, so you can work in one long session until you reach the weekly allowance.
- **Speed modes cost more.** On included subscription usage, Fast mode uses the allowance at 250% of the standard rate, and Ultrafast at 800%.
- **Images use the allowance faster too.** OpenAI says image generation uses included limits at roughly 300% to 500% of the normal rate on average, depending on quality and size. The free plan doesn't include image generation.

The full breakdown of the 5-hour window, the weekly cap and resets is in [Codex usage limits explained](/blog/codex-usage-limits).

## How Codex credits work

![How Codex credits work: Model, Input, Cached input, Output](/codex-pricing-how-codex-credits-work-en.jpg)

Credits are how you keep going after the included allowance runs out. Your plan's included usage is spent first; after that, Codex draws from your credit balance.

OpenAI's rate card lists credits per million tokens for each model at standard speed:

| Model | Input | Cached input | Output |
|---|---:|---:|---:|
| GPT-6 Astra | 250 | 25 | 1,250 |
| GPT-6.1 Sol | 50 | 2.5 | 250 |
| GPT-6 Sol | 50 | 5 | 250 |
| GPT-6 Luna | 2.5 | 0.25 | 12.5 |
| GPT-5.6 Sol | 100 | 10 | 500 |
| GPT-5.6 Luna | 5 | 0.5 | 30 |

- **Who can buy credits.** Plus and Pro users see an option to add credits when they hit a Codex limit, and can also buy them in Settings > Usage in ChatGPT or Usage & Billing in the Codex app. Business, Edu and Enterprise workspaces with flexible pricing buy workspace credits. Free and Go purchases are limited to a test group.
- **Credits expire after 12 months.** Unused credits don't roll over past that date.
- **There is no charge for cache writes.** Codex bills input, cached input and output only.
- **Fast and Ultrafast cost more.** When you pay with credits, Fast mode is charged at 200% of the standard rate and Ultrafast at 600%.
- **A typical task is a few credits.** OpenAI says a typical GPT-5.6 Sol task may use 2 to 15 credits.

### What does one Codex credit cost?

OpenAI doesn't publish a fixed dollar price for credits on personal plans. The help center says purchase amounts and prices can vary by account, region and plan, and are shown in the purchase flow.

What we can say is how the credit rates line up with OpenAI's API prices. For the three models we checked, the credit rate is exactly 25 credits for every dollar of the API list price:

| Model | API price per 1M input / output | Credits per 1M input / output | Credits per $1 of API price |
|---|---|---|---:|
| GPT-6 Luna | $0.10 / $0.50 | 2.5 / 12.5 | 25 |
| GPT-6.1 Sol | $2 / $10 | 50 / 250 | 25 |
| GPT-6 Astra | $10 / $50 | 250 / 1,250 | 25 |

In our reading, that means a credit is designed to be worth about $0.04 of API usage. If your purchase flow shows credits at that price, buying credits costs about the same as using an API key. This is our arithmetic, not an OpenAI price, so check the actual number before you buy.

## Codex API pricing

If you would rather pay per token, you can sign in to the Codex CLI or IDE extension with an API key. You are then billed at standard API rates, with no plan limits:

| Model | Input per 1M | Cached input per 1M | Output per 1M |
|---|---:|---:|---:|
| GPT-6 Luna | $0.10 | $0.01 | $0.50 |
| GPT-6.1 Sol | $2 | $0.10 | $10 |
| GPT-6 Astra | $10 | $1 | $50 |

- **No cloud features.** The API key route covers the CLI, SDK and IDE extension only.
- **You can mix both.** API key users can keep running local chats at API rates after they reach their plan limits.
- **Coding agents read far more than they write.** Every step sends the instructions, tool definitions, files and earlier steps back to the model, so input tokens usually dominate the bill. Cached input is 90% to 95% cheaper than fresh input on these models, which is why long sessions cost less per step than you might expect.

To compare a month of API use with a plan, enter your task size and tasks per day in the [coding agent cost calculator](/agents).

## We tested Codex on the free plan

Published limits only tell you so much, so we ran a small test on October 11, 2026.

- **Plan:** ChatGPT Free.
- **Model:** GPT-6 Luna, the model the free plan offers in Codex.
- **Prompt:** the same brick-breaker prompt from our [Claude Opus 5.5 effort test](/blog/claude-opus-5-5-effort): a browser game in a single index.html file, with 2 levels, a score display and 3 lives, playable with the keyboard and the mouse.
- **Runs:** two, one at medium reasoning effort and one at extra high. Each run built its own file.

![Codex free plan test: the medium and extra high games side by side](/codex-pricing-free-plan-test-games-en.jpg)

| | Medium | Extra high |
|---|---|---|
| Time to finish | 39 s | 39 s |
| Game code | 398 lines | 273 lines |
| Title Codex chose | Brick Breaker | Neon Breakout |
| Levels | 2 (5×10 bricks, then 7×12) | 2 (5×10, then 6×11 with a shaped layout) |
| Effects | None | Particle bursts when a brick breaks, neon glow |
| Tokens (Codex's own estimate) | About 4,000–5,000 | About 4,000-something |
| Free-plan usage | Both runs together: 1% of the monthly meter | |

Both games met every requirement in the prompt: two levels, a score, three lives, and keyboard and mouse controls. Both have a title screen, a pause control and win and game-over screens.

### What playing them felt like

The person who ran the test played both games. In his words, translated from Korean:

- **Medium:** "It feels kind of smooth, but there are no game effects, so the hits feel a bit weak."
- **Extra high:** "The particles aren't flashy, but it's better than having none. I couldn't really tell the other features apart."

### What the numbers mean (our reading)

- **Higher effort changed the polish, not the time.** Both runs took 39 seconds. The extra high version wrote 31% fewer lines but added particle effects, a glowing visual style and a collision check that splits each frame into small steps so a fast ball doesn't pass through bricks. That last part is invisible when you play, which fits with not noticing the other differences.
- **The token figures are Codex's own estimate, not a measurement.** When asked, Codex said it couldn't know the exact count but put each run at roughly 4,000 to 5,000 tokens, with extra high in the 4,000s. That is close to the size of the code it wrote, so it most likely counts output only. The instructions, the reasoning and the context Codex sends at each step are not in that number.
- **The free plan handled this comfortably.** Two complete games used 1% of the free plan's monthly meter, which then showed 99% remaining until the reset a month later. Taken at face value, that is room for roughly 200 games this size a month, though we only measured two and the meter rounds to whole percents. A small, self-contained task like this one is clearly within what OpenAI means by "quick coding tasks." A larger task on a real codebase reads more files and runs more steps, so expect it to use more.
- **At API prices, this task is cheap on Luna.** Codex didn't report its full token count, so here is an assumption: if a run used as many total tokens as Claude Sonnet 5.5 did on the same prompt (115,073, almost all of it input), GPT-6 Luna's API prices would put it at just over one cent, even with no caching. This is an estimate under that assumption, not a measured cost.

For comparison, the same prompt in Claude Code took 37 seconds and $0.25 on Sonnet 5.5 at medium effort, and 1 min 50 s and $0.75 on Opus 5.5 at high effort, measured with ccusage. Those runs are in [Claude Sonnet 5.5 vs Opus 5.5](/blog/claude-sonnet-5-5-vs-opus-5-5). The Claude figures are measured and the Codex token figures are self-reported, so treat the comparison as rough.

## What a bigger Codex task costs

Our test was small on purpose. Real work usually means more steps, and every step re-sends the growing context.

- **A typical feature task is much bigger.** In [Codex usage limits explained](/blog/codex-usage-limits) we estimated that a 25-step feature task sends around 1.6 million input tokens. At API prices that is about $0.72 on a Sol-class model and about $3.60 on GPT-6 Astra.
- **The same task on Luna costs far less.** GPT-6 Luna's input price is 95% lower than GPT-6.1 Sol's ($0.10 against $2 per million), so a task Luna can handle costs a small fraction as much.
- **Effort settings add reasoning tokens.** Higher effort can mean more tokens per step. In our test the extra high run didn't take longer, but on a harder task the gap is usually larger.

The practical upshot: the model you pick matters more than the plan you are on. A Plus user who sends routine work to Luna can go much further than a Pro user who sends everything to Astra.

## Codex pricing changes in 2026

Codex pricing has changed several times this year, which is why older guides disagree with each other. The changes that matter, from OpenAI's own release notes and help center:

| Date | Change |
|---|---|
| April 2, 2026 | Codex moved from per-message pricing to credits based on API token usage, for Plus, Pro, Business and new Enterprise plans |
| April 23, 2026 | The same token-based rate card extended to all existing Enterprise, Edu, Health, Gov and ChatGPT for Teachers plans |
| Late July 2026 | GPT-5.6 Terra became 20% cheaper and GPT-5.6 Luna 80% cheaper |
| September 29, 2026 | Pro split into Pro 100, Pro 200 and Pro 500; new Pro 200 subscribers get a smaller allowance than before, and Ultrafast is Pro 500 only |
| October 14, 2026 | GPT-5.5 retires from ChatGPT, ChatGPT Work and Codex on all plans (the API is not affected) |

- **Guides written before April describe message counts, not tokens.** If a page quotes a fixed number of messages per plan without a model attached, it is probably out of date.
- **If you still use GPT-5.5 in Codex, switch before October 14.** On the credit rate card, GPT-5.5 costs 125 credits per million input tokens; GPT-6.1 Sol costs 50.

## Which Codex plan should you pick?

![Which Codex plan should you pick?: You..., Pick, Why](/codex-pricing-which-codex-plan-should-you-pick-en.jpg)

| You... | Pick | Why |
|---|---|---|
| Want to try Codex on small tasks | Free | GPT-6 Luna in the desktop app at no cost |
| Code a few times a week and want cloud tasks | Plus ($20) | Full GPT-6 line, cloud tasks, GitHub review |
| Hit the 5-hour window several times a week | Pro 100 | No 5-hour limit, a larger weekly allowance |
| Run Codex most of the day | Pro 200 or Pro 500 | Larger weekly allowance; Ultrafast on Pro 500 |
| Use Codex now and then, in your own tools | API key | Pay only for what you use, no cloud features |
| Need it for a team | Business | Plus-level limits per seat, workspace credit plans |

- **Start on the free plan if you're unsure.** It costs nothing, and our test shows it can finish a small project.
- **Go is not a Codex upgrade.** At $8 it adds general ChatGPT usage, but the published Codex access is the same GPT-6 Luna as Free.
- **Plus is the first plan that changes how you work.** It adds the stronger models, cloud tasks and code review.
- **Upgrade to Pro for the time, not the models.** Pro has the same models as Plus. What it buys is the end of the 5-hour wait.

## Codex vs Claude Code vs Copilot: entry prices

| Tool | Free option | Entry paid plan | Next step |
|---|---|---|---|
| Codex (ChatGPT) | Yes, GPT-6 Luna | Plus $20 | Pro 100 $100 |
| Claude Code | No (Claude Free has no Claude Code) | Claude Pro $20 | Max 5x $100 |
| GitHub Copilot | Yes, 2,000 completions and limited chat | Pro $10 | Pro+ $39 |

- **Codex has the most usable free tier for agent work.** Claude's free plan doesn't include Claude Code, and Copilot Free is mostly autocomplete with a small chat allowance.
- **At $20, Codex and Claude Code are priced the same,** and both use allowances that reset on a schedule rather than a dollar balance.
- **Copilot is the cheapest paid entry** at $10, but its credits are tied to API prices. See [GitHub Copilot pricing](/blog/github-copilot-pricing).

For a monthly cost comparison by workload, see [Claude Code vs Codex vs Cursor: cost](/blog/claude-code-vs-codex-vs-cursor-cost).

## How to make your Codex usage last longer

1. **Match the model to the task.** Use GPT-6 Luna for small edits, explanations and boilerplate, GPT-6.1 Sol for normal feature work, and GPT-6 Astra only when the others get stuck.
2. **Keep tasks small and specific.** A clear request about one file costs less than "look through the project and improve it," because the agent reads less.
3. **Avoid Fast mode unless you need it.** It uses included usage at 250% of the standard rate.
4. **Check your remaining usage.** In the Codex CLI, /status shows the current session's token usage, and /usage shows your account's token activity by day, week or in total, and lets you apply a rate-limit reset if one is available. In the ChatGPT desktop app, Settings > Usage shows when your limit resets. Check before starting a long job.
5. **Use resets and credits deliberately.** When you hit a limit, the options can include adding credits, applying a reset, upgrading or waiting. If you only hit the wall once in a while, credits or waiting are cheaper than a bigger plan.

## Verdict

- **Codex comes with every ChatGPT plan,** including Free. You don't pay for it separately.
- **The free plan is enough to try it on real but small tasks.** In our test it built a complete two-level game in 39 seconds, twice, for 1% of its monthly allowance.
- **Plus at $20 is where Codex becomes a daily tool,** with the full GPT-6 line, cloud tasks and GitHub code review.
- **Pro is for removing the 5-hour wait,** not for better models.
- **Model choice moves your costs more than plan choice.** GPT-6 Luna's published message range starts at 7,000% of GPT-6 Astra's, and its API price is a small fraction of Astra's.

## FAQ

**Is Codex free?**
Yes, in a limited form. Codex is included in the ChatGPT Free plan with GPT-6 Luna at standard speed in the desktop app. OpenAI doesn't publish the free plan's limits. On our account, Codex showed one monthly usage meter rather than 5-hour or weekly windows. Cloud tasks need Plus or higher.

**How much does Codex cost?**
Codex has no separate price. It comes with ChatGPT plans: Free $0, Go $8, Plus $20, Pro $100, $200 or $500, and Business $20 per user billed annually. You can also use it with an API key at standard API rates.

**Is Codex included in ChatGPT Plus?**
Yes. Plus includes Codex on the web, CLI, IDE extension and iOS, cloud tasks and the GPT-6 models, within a rolling 5-hour window.

**How much is one Codex credit?**
OpenAI doesn't publish a fixed price for personal plans; it is shown in the purchase flow and can vary by region and plan. The credit rates equal 25 credits per dollar of API list price, which works out to about $0.04 per credit of API-equivalent usage.

**What is Codex API pricing?**
With an API key you pay standard API rates, for example $0.10 input and $0.50 output per million tokens on GPT-6 Luna, $2 and $10 on GPT-6.1 Sol, and $10 and $50 on GPT-6 Astra.

**What happens when I hit the Codex limit?**
Codex can finish the turn it is on. After that, depending on your plan, you can add credits, apply an available reset, upgrade, or wait for the 5-hour or weekly window to reset.

## Run the numbers

The [coding agent cost calculator](/agents) estimates a month of agent work on GPT-6, Claude Opus 5.5 and Sonnet 5.5 from your task size and tasks per day, and compares the API cost with each plan. For one prompt, the [token counter](/) shows the exact cost on each model.

*Plan details and credit rates checked on OpenAI's pricing page and help center on October 11, 2026. The free-plan test is one run per effort level on October 11, 2026; Codex's token figures are its own estimates.*

## Sources

- [OpenAI: Pricing (ChatGPT Learn)](https://learn.chatgpt.com/docs/pricing)
- [OpenAI Help: Codex rate card](https://help.openai.com/en/articles/20001106-codex-rate-card-2)
- [OpenAI: What's new in ChatGPT](https://learn.chatgpt.com/docs/whats-new)
- [OpenAI: Slash commands in Codex CLI](https://learn.chatgpt.com/docs/cli/slash-commands/)
- [OpenAI Help: ChatGPT Pro plans](https://help.openai.com/en/articles/9793128)
- [OpenAI Help: Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)
- [OpenAI Help: Using credits for flexible usage in ChatGPT](https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-freegopluspro-sora)
- [OpenAI Help: ChatGPT rate card (Business, Enterprise/Edu)](https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu)
- [OpenAI: ChatGPT pricing](https://chatgpt.com/pricing)
- [OpenAI: API pricing](https://developers.openai.com/api/docs/pricing)
<!-- autoimg -->
