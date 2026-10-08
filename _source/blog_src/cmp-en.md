![ChatGPT Pro vs Claude Max: Which $100 or $200 Plan Gives More?](/chatgpt-pro-vs-claude-max-en.jpg)

ChatGPT and Claude now have almost mirror-image price ladders: $20, $100, $200, and in ChatGPT's case $500. Both include a coding agent (Codex in ChatGPT, Claude Code in Claude). So which one gives you more for the money? The honest answer depends on what you do with it, but the plans are not as equal as the prices suggest.

## The plans side by side

![The plans side by side: Price, ChatGPT, Usage, Claude, Usage](/chatgpt-pro-vs-claude-max-the-plans-side-by-side-en.jpg)

US monthly prices, checked October 2026:

| Price | ChatGPT | Usage | Claude | Usage |
|---|---|---|---|---|
| $20 | Plus | base | Pro | base |
| $100 | Pro 100 | 5× Plus | Max 5× | 5× Pro |
| $200 | Pro 200 | 10× Plus* | Max 20× | 20× Pro |
| $500 | Pro 500 | 25× Plus + Ultrafast | – | – |

\* Pro 200 was cut from 20× to 10× Plus for new subscribers. Anyone with an active Pro 200 subscription at any point from September 22 to September 29, 2026 keeps the old allowance until October 29. The ChatGPT multiples come from OpenAI's Thibault Sottiaux on X and press reports (WinBuzzer, Windows Report), not from OpenAI's pricing page.

Usage multipliers are relative to each company's own $20 plan, so "5× Plus" and "5× Pro" are not the same amount of work. Neither company publishes exact token numbers.

## What changed the comparison in September 2026

**At $200, Claude now gives a bigger multiplier.** Claude Max 20× is 20 times its base plan; ChatGPT Pro 200 is now 10 times its base plan. For heavy users who were choosing between the two $200 plans, that is the biggest shift.

**ChatGPT has no bulk discount anymore.** Pro 100, 200 and 500 all cost $20 per "Plus-worth" of usage. Claude's Max 20× is the only $200 plan that gives more usage per dollar than the plan below it (20× for a price 100% higher than 5×). Details in [ChatGPT Pro 100 vs 200 vs 500](/blog/chatgpt-pro-100-vs-200-vs-500).

**Claude cut weekly Claude Code limits slightly.** On September 14, a temporary 50% weekly boost was replaced with a permanent 25% increase, which is about 17% less than during the summer. See [Claude Code usage limits explained](/blog/claude-code-usage-limits).

## Models you get

![Models you get: Input / 1M tokens, Output / 1M tokens](/chatgpt-pro-vs-claude-max-models-you-get-en.jpg)

**ChatGPT:** GPT-6 Astra, OpenAI's flagship, is available on Pro plans (and is rolling out to Plus, first in Work and Codex). Pro 500 also gets Ultrafast, a faster mode that uses your allowance more quickly.

**Claude:** the plans center on Claude Sonnet 5.5 and Opus 5.5. Max mainly gives you more room to use Opus, the more expensive of the two.

API prices show how expensive each flagship is to run, which is part of why limits feel different:

| | Input / 1M tokens | Output / 1M tokens |
|---|---|---|
| GPT-6 Astra | $10 | $50 |
| Claude Opus 5.5 | $4 | $20 |
| GPT-6 Sol | $2 | $10 |
| Claude Sonnet 5.5 | $2 | $10 |

GPT-6 Astra costs 150% more per token than Claude Opus 5.5. If you mostly use the top model, expect a ChatGPT allowance to run out faster for the same amount of work. GPT-6 Sol and Claude Sonnet 5.5 cost exactly the same per token.

## Coding agents: Codex vs Claude Code

Both plans include an agent that works in your terminal or editor, and both agents resend their whole working context at every step, so they use far more tokens than chat. A typical 25-step feature task sends about 1.6 million input tokens. On the API, that task costs about $0.72 on Sonnet 5.5 or GPT-6 Sol, $1.43 on Opus 5.5, and around $3.60 on GPT-6 Astra.

If you code with an agent every day, the plan is almost always cheaper than the API. Our [coding agent calculator](/agents) compares both plans with API costs for your own usage.

## Which should you pick?

![Which should you pick?: You want GPT-6 Astra specifically, or image generation, voice and the broader ChatGPT app.; You need Ultrafast](/chatgpt-pro-vs-claude-max-which-should-you-pick-en.jpg)

**Choose ChatGPT if:**
- You want GPT-6 Astra specifically, or image generation, voice and the broader ChatGPT app.
- You need Ultrafast and can justify $500 (Pro 500).
- You already use Codex and like it.

**Choose Claude if:**
- You spend most of your time in Claude Code and want the largest allowance for $200 (Max 20×).
- You work with long documents and code and prefer Opus 5.5 or Sonnet 5.5.
- Price per token of the flagship matters to you (Opus 5.5 is cheaper to run than Astra).

**At $20,** both are reasonable starting points. Try the one whose models you prefer, watch how often you hit the limit, and only upgrade when you hit it regularly.

## Or skip both

If you use AI only a few times a day, the API may cost less than any plan. The [Subscription vs API calculator](/plans) shows the monthly API cost of your usage next to every ChatGPT, Claude and Gemini plan.

*Plans and limits change often. Check [chatgpt.com/pricing](https://chatgpt.com/pricing) and [claude.com/pricing](https://claude.com/pricing) before you subscribe.*

## Sources

- [ChatGPT plans and Codex pricing](https://learn.chatgpt.com/docs/pricing)
- [OpenAI Help: About ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
- [Claude Help: What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- [Claude Help: Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing)
<!-- autoimg -->
