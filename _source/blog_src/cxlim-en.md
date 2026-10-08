![Codex Usage Limits Explained: 5-Hour Window, Weekly Cap and Resets](/codex-usage-limits-en.jpg)

Codex, OpenAI's coding agent, is included in ChatGPT Plus, Pro and Business plans, and it is where most people now run into usage limits. Codex shares its allowance with ChatGPT Work, uses a 5-hour window and a weekly cap, and burns through them at very different speeds depending on the model. Here is how it works and how to get more out of it.

## Which plans include Codex

Codex (and ChatGPT Work) usage is included with **Plus** ($20), **Pro** ($100, $200 or $500) and **Business** Standard and Premium seats. Usage is not unlimited: each plan gets an allowance, measured over two windows.

## Two limits at once

**The 5-hour window.** A rolling allowance that starts with your first request. Use it up and you wait until the window resets. OpenAI restored the 5-hour window for Plus at the end of August 2026; at the time it said Pro 100 and Pro 200 would not have it for the coming months.

**The weekly limit.** A rolling seven-day cap on top. Hit it and you wait for the weekly reset, even if your 5-hour window is fresh.

Codex and ChatGPT Work draw from the **same allowance**.

## How much you get, by model

![How much you get, by model: Model, Plus, Pro (5× tier)](/codex-usage-limits-how-much-you-get-by-model-en.jpg)

OpenAI's help center gives estimated messages per 5-hour window. The model you pick changes the number enormously:

| Model | Plus | Pro (5× tier) |
|---|---|---|
| GPT-6 Astra | about 5–45 | about 25–225 |
| GPT-5.6 Sol | about 10–100 | about 50–500 |
| GPT-5.6 Terra | about 25–200 | about 125–1,000 |
| GPT-5.6 Luna | about 250–2,000 | about 1,250–10,000 |

The low end of each range is long, multi-step tasks on a large codebase; the high end is short, simple requests. Higher Pro tiers scale up: Pro 200 is 10× Plus for new subscribers since September 29, 2026, and Pro 500 is 25×.

**Ultrafast**, available only on Pro 500, is a faster mode that uses your included usage and credits more quickly.

## Why Codex uses the allowance so fast

Like every coding agent, Codex works in steps and sends its whole working context back to the model at each step: instructions, tool definitions, files it has read and earlier steps. A typical 25-step feature task sends around 1.6 million input tokens. On the API that task would cost about $0.72 on a Sol-class model and around $3.60 on GPT-6 Astra, which is why Astra's allowance is so much smaller. See [What does an AI coding agent cost per task?](/blog/ai-coding-agent-cost)

## How to check your usage

OpenAI's help center points to **Settings → Usage** in ChatGPT, which shows your remaining allowance and reset times. Codex also warns you as you approach the limit.

## When you hit the limit

![When you hit the limit: Wait for the reset. The 5-hour window refills within hours.; Use a banked reset or buy an instant reset, avail](/codex-usage-limits-when-you-hit-the-limit-en.jpg)

1. **Wait for the reset.** The 5-hour window refills within hours.
2. **Use a banked reset or buy an instant reset**, available on eligible Plus and Pro accounts.
3. **Use credits** to keep going on plans that support them.
4. **Upgrade** to a higher Pro tier.
5. **Use an API key** with pay-as-you-go billing for overflow work.

## How to stretch it

![How to stretch it: Default to GPT-5.6 Sol or Terra. Use GPT-6 Astra only for the hard problems where you can see the difference; ](/codex-usage-limits-how-to-stretch-it-en.jpg)

- **Default to GPT-5.6 Sol or Terra.** Use GPT-6 Astra only for the hard problems where you can see the difference: it uses much more of the allowance.
- **Use Luna for simple edits**, renames and boilerplate.
- **Keep tasks small and specific.** Fewer steps means less context resent.
- **Start fresh between unrelated tasks** so old history is not carried along.
- **Point Codex at the right files** instead of letting it search the whole repo.
- **Keep your instruction file short**, and write it in English if you normally use another language: on GPT's tokenizer, Korean takes about 44% more tokens than English and Japanese 79% more.

Many of the same habits apply to Claude Code: see [How to save tokens in Claude Code](/blog/claude-code-save-tokens).

## Codex or Claude Code?

Both are included in $20, $100 and $200 plans with similar limit systems. The [ChatGPT Pro vs Claude Max comparison](/blog/chatgpt-pro-vs-claude-max) covers the differences, and the [coding agent calculator](/agents) compares monthly API costs with every plan.

*Limits change often. OpenAI's [Codex and Work usage help page](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex) has the current numbers.*

## Sources

- [OpenAI Help: Managing usage with GPT-6 Astra in Work and Codex](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)
- [OpenAI Help: How banked Codex resets work](https://help.openai.com/en/articles/20001498-how-banked-codex-resets-work)
- [ChatGPT plans and Codex pricing](https://learn.chatgpt.com/docs/pricing)
- [OpenAI Help: About ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
<!-- autoimg -->
