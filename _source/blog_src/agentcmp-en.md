![Claude Code vs Codex vs Cursor: What Each Costs in 2026](/claude-code-vs-codex-vs-cursor-cost-en.jpg)

Claude Code, OpenAI's Codex and Cursor all sell a $20 plan and a $200 plan, so they look interchangeable on the pricing page. They are not. Claude Code and Codex give you a usage allowance that refills every five hours and every week; Cursor gives you a dollar budget of model usage and bills you for more. Here is what each plan actually buys, and which is cheapest for the way you code.

## The plans

![The plans: Price, Claude Code (Anthropic), Codex (OpenAI), Cursor](/claude-code-vs-codex-vs-cursor-cost-the-plans-en.jpg)

US monthly prices, October 2026:

| Price | Claude Code (Anthropic) | Codex (OpenAI) | Cursor |
|---|---|---|---|
| Free | – | – | Hobby: limited agent requests |
| $20 | Claude Pro | ChatGPT Plus | Pro: ~$20 of model usage |
| $60 | – | – | Pro+: ~$60 of model usage |
| $100 | Max 5× (5× Pro) | Pro 100 (5× Plus) | – |
| $200 | **Max 20× (20× Pro)** | Pro 200 (10× Plus) | **Ultra: ~$400 of model usage** |
| $500 | – | Pro 500 (25× Plus, faster mode) | – |

The ChatGPT Pro multiples come from OpenAI's Thibault Sottiaux on X and press reports (WinBuzzer, Windows Report), not from OpenAI's pricing page. New Pro 200 subscribers get 10× Plus; anyone with an active Pro 200 subscription between September 22 and September 29, 2026 keeps the previous allowance until October 29.

Claude Code comes with the Claude app; Codex comes with ChatGPT and ChatGPT Work. Cursor is an editor with an agent built in, and it lets you pick models from several companies, including Claude and GPT.

## Two different ways of counting

**Claude Code and Codex: usage limits.** You get an allowance per 5-hour window and per week, shared with the chat app. When it runs out, you wait for the reset (or buy extra usage). Neither company publishes the allowance in tokens. See [Claude Code usage limits](/blog/claude-code-usage-limits) and [Codex usage limits](/blog/codex-usage-limits).

**Cursor: a dollar budget.** Each paid plan includes roughly its price in model usage, billed at the model's API rates (Ultra includes usage worth about 100% more than its price). Past that, usage is billed at the same rates unless you set a spending cap, in which case it stops. That makes Cursor easy to predict: a task that would cost $0.50 on the API uses about $0.50 of your budget.

## Which gives the most for $200?

![Which gives the most for $200?: Claude Max 20× gives 20× Pro's usage for $200 against Pro's $20, so each unit of usage costs half as much as on ](/claude-code-vs-codex-vs-cursor-cost-which-gives-the-most-for-200-en.jpg)

- **Claude Max 20×** gives 20× Pro's usage for $200 against Pro's $20, so each unit of usage costs half as much as on Pro. Measured in Claude Code, a Max 20× week came to about 1.9 billion tokens, roughly **$1,800 of API usage** at the same model mix. See [how many tokens you get with Claude Pro and Max](/blog/claude-pro-max-how-many-tokens).
- **ChatGPT Pro 200** is 10 times Plus for 10 times the price: no bulk discount, but Codex comes with all of ChatGPT's Pro features.
- **Cursor Ultra** includes about **$400 of model usage** for $200, double the money, and lets you spread it across Claude, GPT and other models.

If you use one agent all day, the flat allowances from Anthropic and OpenAI usually go much further than a dollar budget, because they are priced well below API rates for heavy users. Cursor wins on flexibility (any model, one editor) and on predictability (you always know what a task cost).

## What a month costs on the API, for reference

![What a month costs on the API, for reference: How you use it, API with Claude Sonnet 5.5, API with Claude Opus 5.5, Cheapest plan that usually fits](/claude-code-vs-codex-vs-cursor-cost-what-a-month-costs-on-the-api-for-refere-en.jpg)

From our [Claude Code cost per month](/blog/claude-code-cost-per-month) model, 22 working days:

| How you use it | API with Claude Sonnet 5.5 | API with Claude Opus 5.5 | Cheapest plan that usually fits |
|---|---|---|---|
| Light: 3 small fixes a day | ~$10 | ~$20 | API, or any $20 plan |
| Regular: 5 features a day | ~$79 | ~$158 | $20–$100 plan |
| Heavy: 15 features a day | ~$236 | ~$473 | $100–$200 plan |
| Agents all day | ~$466 | ~$932 | $200 plan |

On Cursor, the API column is roughly what you would use from your budget: a regular Sonnet user fits in Pro+ ($60) plus a little overage, while a heavy Opus user would need Ultra and probably more.

## How to choose

- **You mostly use one company's models and code for hours a day:** Claude Max 20× (Claude) or ChatGPT Pro (GPT). The flat allowance is the cheapest way to buy a lot of agent time.
- **You want to switch between Claude, GPT and others in one editor:** Cursor. Start on Pro and move to Pro+ or Ultra only if you keep running past the budget.
- **You code with AI a few times a week:** any $20 plan, or pay per token through the API. At light use the API can cost less than $20 a month.
- **You keep hitting limits:** go up one tier before adding a second subscription; two $20 plans rarely beat one $100 plan.

## Estimate your own month

Put in your task size and tasks per day in the [coding agent cost calculator](/agents) to see the API cost next to every Claude and ChatGPT plan.

*Cursor plan details from [CloudZero's Cursor pricing guide](https://www.cloudzero.com/blog/cursor-ai-pricing/) (updated September 2026). Prices and limits change often; check each company's pricing page before you subscribe.*

## Sources

- [Claude plans and pricing (Anthropic)](https://claude.com/pricing)
- [Using Claude Code with your Pro or Max plan (Claude Help Center)](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [Codex pricing and plans (OpenAI)](https://learn.chatgpt.com/docs/pricing)
- [About ChatGPT Pro tiers (OpenAI Help Center)](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
- [Cursor pricing](https://cursor.com/pricing)
<!-- autoimg -->
