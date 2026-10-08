![How Many Tokens Do You Get with Claude Pro and Max?](/claude-pro-max-how-many-tokens-en.jpg)

Anthropic does not say how many tokens Claude Pro or Max include. Its plans are described as usage multiples ("5× Pro", "20× Pro") with a 5-hour limit and a weekly limit, never as a token number. But people have measured it. Here is what the numbers look like, why they are so large, and how to turn them into something useful: what your usage would cost on the API.

## The short answer

![The short answer: Plan, Price, Per 5-hour window, Per week](/claude-pro-max-how-many-tokens-the-short-answer-en.jpg)

Measured in Claude Code in September 2026, on Claude Opus 5:

| Plan | Price | Per 5-hour window | Per week |
|---|---|---|---|
| Pro | $20 | ~8 million tokens *(estimate)* | ~95 million *(estimate)* |
| Max 5× | $100 | **~39 million tokens** (median) | at least 1.3 billion |
| Max 20× | $200 | ~155 million *(estimate)* | **~1.9 billion tokens** |

**Bold** figures were measured by [FinOps LLM](https://finopsllm.com/research/claude-pro-max-tokens-limit), which logged one heavy user's Claude Code sessions until the limits stopped them: the 5-hour limit on Max 5× twelve times, and the weekly limit on Max 20× twice. The other figures are our estimates, scaled from those measurements using Anthropic's own multiples (Max 5× = 5× Pro, Max 20× = 20× Pro). Treat them as orders of magnitude, not guarantees.

## Why the numbers are so big

Thirty-nine million tokens in five hours sounds like a lot of text. It is not. In the measured sessions, **96% of the tokens were cache reads**: Claude Code re-reading its own context (your files, the conversation so far, the tool results) at every step of a task. Only about 0.6% of the tokens were output, Claude actually writing something.

Cache reads are cheap on the API, about a tenth of the normal input price, so Anthropic's limits clearly do not count every token equally. They behave more like a **cost budget**. The median Max 5× window corresponded to roughly **$37 of API usage**, which puts a Pro window at around $7 and a Max 20× window at around $150 on the same scale.

That is why a token count tells you less than you would think. Two sessions with the same number of tokens can use very different shares of your limit, depending on how much is fresh input and output and which model you use.

## What uses your allowance fastest

![What uses your allowance fastest: Opus instead of Sonnet. Opus 5.5 costs 100% more per token than Sonnet 5.5 on the API, and it uses your plan](/claude-pro-max-how-many-tokens-what-uses-your-allowance-fastest-en.jpg)

- **Opus instead of Sonnet.** Opus 5.5 costs 100% more per token than Sonnet 5.5 on the API, and it uses your plan's allowance faster too.
- **Long sessions.** Every step re-sends the whole context. A session that has grown to 150,000 tokens costs far more per step than a fresh one. Use **/clear** between unrelated tasks and **/compact** on long ones.
- **A big CLAUDE.md or many tools.** They are sent with every step.
- **Writing in another language.** Korean uses about 44% more tokens than English for the same meaning, Japanese about 79% more.

## How many messages is that?

Anthropic does not publish message counts for Claude Code either. Community estimates put Pro at roughly **90 prompts per 5-hour window on Sonnet** after Anthropic doubled the 5-hour limits in May 2026, and Max 20× at **200 to 900 prompts** per window, depending heavily on how large each task is ([source](https://fast.io/resources/claude-code-usage-limits-guide/)). The Claude app and Claude Code share the same allowance.

## Per day?

There is no daily limit. You have a rolling 5-hour window, which starts with your first message, and a weekly limit on top. If you hit the weekly limit, spreading heavy work more evenly across the week is the only fix short of upgrading.

## Is a subscription cheaper than the API for you?

Almost certainly yes if you use Claude Code heavily: a Max 20× week measured at about 1.9 billion tokens works out to roughly $1,800 at API prices for the same mix of models and cache reads, against $200 a month for the plan. For lighter use the answer can flip. Put in your own task size and tasks per day in the [coding agent cost calculator](/agents), or use the [Subscription vs API calculator](/plans) for chat.

Related: [Claude Max vs Pro](/blog/claude-max-vs-pro) · [Claude Code usage limits explained](/blog/claude-code-usage-limits) · [How to save tokens in Claude Code](/blog/claude-code-save-tokens) · [Claude token counter](/claude-token-counter)

*Anthropic changes limits often and does not publish token quotas. Run **/status** in Claude Code to see where you stand.*

## Sources

- [Using Claude Code with your Pro or Max plan (Claude Help Center)](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [Claude plans and pricing (Anthropic)](https://claude.com/pricing)
- [Claude API pricing (Anthropic docs)](https://platform.claude.com/docs/en/about-claude/pricing)
<!-- autoimg -->
