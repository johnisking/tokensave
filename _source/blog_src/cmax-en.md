![Claude Max vs Pro: Is the $100 or $200 Plan Worth It?](/claude-max-vs-pro-en.jpg)

Claude Pro costs $20 a month. Claude Max costs $100 or $200. Both include the Claude app and Claude Code, so the real question is simple: is the extra usage worth five or ten times the price? For many people it is not. For heavy Claude Code users, Max 20× is the best value Anthropic sells.

## The plans

![The plans: Plan, Price, Usage, Price per "Pro-worth" of usage](/claude-max-vs-pro-the-plans-en.jpg)

US prices, checked October 2026:

| Plan | Price | Usage | Price per "Pro-worth" of usage |
|---|---|---|---|
| Pro | $20 a month ($17 with annual billing) | base | $20 |
| Max 5× | $100 a month | 5× Pro | $20 |
| Max 20× | $200 a month | 20× Pro | $10 |

All three include Claude Code, and the Claude app and Claude Code share the same allowance.

## The key point: Max 5× is not cheaper per unit, Max 20× is

Max 5× gives you five times Pro's usage for five times the price. It is the same deal, just more of it.

Max 20× gives you twenty times Pro's usage for ten times the price. **Each unit of usage costs half as much as on Pro.** If you would otherwise need more than ten Pro accounts' worth of usage, it is the clear choice; if you regularly need more than Max 5× gives you, it is better value than adding API credits on top.

## How the limits work

Every plan has two limits at once:

- **A 5-hour session limit**, a rolling window from your first message. Anthropic doubled Claude Code's 5-hour limits on May 6, 2026.
- **A weekly limit** across all your usage. On September 14, 2026, Anthropic permanently raised standard weekly limits in Claude Code by 25%, replacing a temporary 50% boost.

Max multiplies both. Run **/status** in Claude Code to see where you are. Full details in [Claude Code usage limits explained](/blog/claude-code-usage-limits).

## Who should stay on Pro

![Who should stay on Pro: You use Claude a few times a day, mostly in the app.; You use Claude Code for occasional tasks, not hours at a](/claude-max-vs-pro-who-should-stay-on-pro-en.jpg)

- You use Claude a few times a day, mostly in the app.
- You use Claude Code for occasional tasks, not hours at a time.
- You rarely or never see the limit message.

If that is you, $20 is plenty. Occasional extra usage can be covered by usage credits or a short wait.

## Who should get Max 5×

![Who should get Max 5×: You hit the Pro limit most weeks.; You use Claude Code for real work several times a day.; You want to use Opu](/claude-max-vs-pro-who-should-get-max-5-en.jpg)

- You hit the Pro limit most weeks.
- You use Claude Code for real work several times a day.
- You want to use Opus more, which uses the allowance faster than Sonnet.

## Who should get Max 20×

- You run Claude Code for hours a day, or several sessions in parallel.
- You keep hitting Max 5×'s weekly limit.
- You use Opus as your default model.

At this level, the API would usually cost far more. On our cost model, a heavy user running 15 feature-sized tasks a day would spend around $236 a month on the API with Sonnet, or about $473 with Opus. Max 20× is $200. See [Claude Code cost per month](/blog/claude-code-cost-per-month).

## Things that make the allowance go further on any plan

- Start a new session (**/clear**) between unrelated tasks; use **/compact** on long ones.
- Keep your CLAUDE.md short; it is sent with every step.
- Use Sonnet for routine work and Opus only for hard problems.
- Write instructions in English if you normally write in another language.

More in [How to save tokens in Claude Code](/blog/claude-code-save-tokens).

## Can you get Claude Max for free?

Only in one case. In February 2026 Anthropic opened **Claude for Open Source**: six months of free Claude Max 20× for maintainers and core contributors of large open-source projects. The bar is high: a project with 5,000+ GitHub stars or 1 million+ monthly npm downloads, active maintenance in the last three months, and a primary or core-team role. Anthropic said it would accept up to 10,000 contributors and review applications on a rolling basis; check [claude.com](https://claude.com/contact-sales/claude-for-oss) to see whether it is still open.

## Claude Max or ChatGPT Pro?

At $200, Claude Max 20× is now 20× its base plan, while ChatGPT Pro 200 is 10× its base plan for new subscribers. The two companies' base plans are not the same size, so compare what you actually use. See [ChatGPT Pro vs Claude Max](/blog/chatgpt-pro-vs-claude-max).

## Check your own numbers

Use the [coding agent calculator](/agents) to compare Pro, Max and the API for the way you use Claude Code, or the [Subscription vs API calculator](/plans) for chat use.

*Prices and limits change. Check [claude.com/pricing](https://claude.com/pricing) before you upgrade.*

## Sources

- [Claude plans and pricing (Anthropic)](https://claude.com/pricing)
- [Using Claude Code with your Pro or Max plan (Claude Help Center)](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [Extra usage for paid Claude plans (Claude Help Center)](https://support.claude.com/en/articles/12429409-extra-usage-for-max-20x-plans)
- [Claude API pricing (Anthropic docs)](https://platform.claude.com/docs/en/about-claude/pricing)
<!-- autoimg -->
