ChatGPT and Claude now have almost mirror-image price ladders: $20, $100, $200, and in ChatGPT's case $500. Both include a coding agent (Codex in ChatGPT, Claude Code in Claude). So which one gives you more for the money? The honest answer depends on what you do with it, but the plans are not as equal as the prices suggest.

## The plans side by side

US monthly prices, checked October 2026:

| Price | ChatGPT | Usage | Claude | Usage |
|---|---|---|---|---|
| $20 | Plus | base | Pro | base |
| $100 | Pro 100 | 5× Plus | Max 5× | 5× Pro |
| $200 | Pro 200 | 10× Plus* | Max 20× | 20× Pro |
| $500 | Pro 500 | 25× Plus + Ultrafast | – | – |

\* Pro 200 was cut from 20× to 10× Plus for new subscribers on September 29, 2026. Existing Pro 200 subscribers keep the old allowance until October 29.

Usage multipliers are relative to each company's own $20 plan, so "5× Plus" and "5× Pro" are not the same amount of work. Neither company publishes exact token numbers.

## What changed the comparison in September 2026

**At $200, Claude now gives a bigger multiplier.** Claude Max 20× is 20 times its base plan; ChatGPT Pro 200 is now 10 times its base plan. For heavy users who were choosing between the two $200 plans, that is the biggest shift.

**ChatGPT has no bulk discount anymore.** Pro 100, 200 and 500 all cost $20 per "Plus-worth" of usage. Claude's Max 20× is the only $200 plan that gives more usage per dollar than the plan below it (20× for twice the price of 5×). Details in [ChatGPT Pro 100 vs 200 vs 500](/blog/chatgpt-pro-100-vs-200-vs-500).

**Claude cut weekly Claude Code limits slightly.** On September 14, a temporary 50% weekly boost was replaced with a permanent 25% increase, which is about 17% less than during the summer. See [Claude Code usage limits explained](/blog/claude-code-usage-limits).

## Models you get

**ChatGPT:** GPT-6 Astra, OpenAI's flagship, is available on Pro plans (and is rolling out to Plus, first in Work and Codex). Pro 500 also gets Ultrafast, a faster mode that uses your allowance more quickly.

**Claude:** the plans center on Claude Sonnet 5.5 and Opus 5.5. Max mainly gives you more room to use Opus, the more expensive of the two.

API prices show how expensive each flagship is to run, which is part of why limits feel different:

| | Input / 1M tokens | Output / 1M tokens |
|---|---|---|
| GPT-6 Astra | $10 | $50 |
| Claude Opus 5.5 | $4 | $20 |
| GPT-6 Sol | $2 | $10 |
| Claude Sonnet 5.5 | $2 | $10 |

GPT-6 Astra costs 2.5 times as much per token as Claude Opus 5.5. If you mostly use the top model, expect a ChatGPT allowance to run out faster for the same amount of work. GPT-6 Sol and Claude Sonnet 5.5 cost exactly the same per token.

## Coding agents: Codex vs Claude Code

Both plans include an agent that works in your terminal or editor, and both agents resend their whole working context at every step, so they use far more tokens than chat. A typical 25-step feature task sends about 1.6 million input tokens. On the API, that task costs about $0.72 on Sonnet 5.5 or GPT-6 Sol, $1.43 on Opus 5.5, and around $3.60 on GPT-6 Astra.

If you code with an agent every day, the plan is almost always cheaper than the API. Our [coding agent calculator](/agents) compares both plans with API costs for your own usage.

## Which should you pick?

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
