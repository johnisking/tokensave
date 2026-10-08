![Claude Code Usage Limits Explained: 5-Hour and Weekly Caps](/claude-code-usage-limits-en.jpg)

"Claude usage limit reached" is one of the most common messages Claude Code users see, and one of the most confusing, because there are two different limits working at the same time. Here is how they work, what changed in 2026, and what you can do when you hit one.

## The two limits

**1. The 5-hour session limit.** Your usage is measured over a rolling five-hour window that starts with your first message. When you use up the allowance for that window, you have to wait until it resets.

**2. The weekly limit.** On top of the session limit, there is a cap on total usage over a week. It was introduced in August 2025 to stop a small share of accounts from running Claude Code around the clock. If you hit it, you wait for the weekly reset even if your 5-hour window is fresh.

Both limits are **shared between Claude Code and the Claude app** (web, desktop and mobile). A long chat in the app uses the same allowance as your coding session.

## How much each plan gets

![How much each plan gets: Plan, Price, Usage](/claude-code-usage-limits-how-much-each-plan-gets-en.jpg)

Anthropic describes plan limits relative to each other rather than in exact tokens:

| Plan | Price | Usage |
|---|---|---|
| Pro | $20/month | Base level |
| Max 5× | $100/month | 5× Pro |
| Max 20× | $200/month | 20× Pro |

How far that goes depends heavily on what you do. Large files, long sessions and Opus use the allowance much faster than short tasks on Sonnet, because every step resends the whole working context.

## What changed in 2026

![What changed in 2026: May 6, 2026; Summer 2026; September 14, 2026](/claude-code-usage-limits-what-changed-in-2026-en.jpg)

- **May 6, 2026:** Anthropic **doubled Claude Code's five-hour rate limits** for Pro, Max, Team and seat-based Enterprise plans, and removed the extra limit reduction during peak hours for Pro and Max.
- **Summer 2026:** a temporary **50% increase** to weekly limits was in place.
- **September 14, 2026:** Anthropic **permanently raised standard weekly limits by 25%** for Pro, Max, Team and seat-based Enterprise. Because this replaced the temporary 50% boost, weekly limits ended up about 17% lower than during the summer, though still 25% above the original level.

So if you feel you hit the weekly limit sooner since mid-September, that is expected.

## How to check where you are

Inside Claude Code, the **/status** command shows your remaining allowance. Claude Code also warns you as you approach a limit. Check before starting a long task, not halfway through it.

## What to do when you hit a limit

![What to do when you hit a limit: Wait for the reset. For the 5-hour limit this is usually a matter of hours.; Turn on extra usage. Paid plans c](/claude-code-usage-limits-what-to-do-when-you-hit-a-limit-en.jpg)

1. **Wait for the reset.** For the 5-hour limit this is usually a matter of hours.
2. **Turn on extra usage.** Paid plans can continue with usage credits billed separately, instead of stopping.
3. **Switch to API credits.** Claude Code can run on pay-as-you-go API billing; it asks for your consent before it does.
4. **Upgrade your plan.** Pro to Max 5×, or Max 5× to Max 20×.
5. **Use fewer tokens per task.** Often the cheapest fix. See below.

## Why you hit limits faster than expected

- **Long sessions.** Each step resends everything that happened before. A two-hour session drags a huge context into every new step.
- **Opus.** It uses the allowance faster than Sonnet.
- **Large files and logs.** Reading a 3,000-line file or a full test log adds tens of thousands of tokens.
- **Vague tasks.** "Clean up the project" can take dozens of steps; "fix the failing test in auth.py" takes a few.
- **Using the Claude app at the same time.** Both draw from the same pool.

## Stretch your limits

- Start a fresh session (**/clear**) between unrelated tasks, and use **/compact** to summarize a long one.
- Point Claude to the right files instead of letting it search.
- Keep your CLAUDE.md instructions short: they are sent with every step.
- Use Sonnet for routine work and save Opus for hard problems.

More detail and numbers in [How to save tokens in Claude Code](/blog/claude-code-save-tokens).

## Plan or API?

If you regularly hit the weekly limit, compare what that extra usage would cost on the API with the next plan up. Our [Claude Code cost per month](/blog/claude-code-cost-per-month) guide and [coding agent calculator](/agents) do the maths.

*Limits change. Anthropic's [Claude Code plan help page](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan) and [pricing page](https://claude.com/pricing) have the current rules.*

## Sources

- [Using Claude Code with your Pro or Max plan (Claude Help Center)](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [Claude plans and pricing (Anthropic)](https://claude.com/pricing)
- [Extra usage for paid Claude plans (Claude Help Center)](https://support.claude.com/en/articles/12429409-extra-usage-for-max-20x-plans)
- [Manage costs effectively (Claude Code docs)](https://code.claude.com/docs/en/costs)
<!-- autoimg -->
