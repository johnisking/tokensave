![Codex Usage Limits Explained: 5-Hour Window, Weekly Cap and Resets](/codex-usage-limits-en.jpg)

Codex, OpenAI's coding agent, is included in ChatGPT Plus, Pro and Business plans, and it is where most people now run into usage limits. Codex shares its allowance with ChatGPT Work, uses a 5-hour window on Plus and Business (weekly limits may also apply), and burns through it at very different speeds depending on the model. Here is how it works, what one task actually uses in our own measurements, and how to get more out of it. Limits checked October 19, 2026.

## Which plans include Codex

Codex (and ChatGPT Work) usage is included with **Plus** ($20), **Pro** ($100, $200 or $500) and **Business** Standard and Premium seats. Usage is not unlimited: each plan gets an included allowance.

## Two limits at once

**The 5-hour window.** A rolling allowance that starts with your first request. Use it up and you wait until the window resets. Pro 100, Pro 200 and Pro 500 currently have no five-hour usage limit in Work and Codex; they still have an included allowance.

**The weekly limit.** OpenAI says weekly limits may also apply on top. Hit one and you wait for its reset, even if your 5-hour window is fresh.

Codex and ChatGPT Work draw from the **same allowance**.

## How much you get, by model

![How much you get, by model: Model, Plus, Business (Standard)](/codex-usage-limits-how-much-you-get-by-model-en.jpg)

OpenAI's help center gives estimated local messages per 5-hour window for Plus and Standard Business. The model you pick changes the number enormously:

| Model | Plus | Business (Standard) |
|---|---|---|
| GPT-6 Astra | about 5–45 | about 5–45 |
| GPT-6.1 Sol | about 15–160 | about 15–160 |
| GPT-6 Sol | about 15–150 | about 15–150 |
| GPT-6 Luna | about 350–3,000 | about 350–3,000 |

The low end of each range is long, multi-step tasks on a large codebase; the high end is short, simple requests. Pro plans currently have no 5-hour limit, but a larger included allowance: Pro 100 is 5× Plus, Pro 200 is 10× Plus for new subscribers (anyone with an active Pro 200 subscription between September 22 and September 29, 2026 keeps the previous allowance until October 29), and Pro 500 is 25× Plus. These multiples come from OpenAI's Thibault Sottiaux on X and press reports (WinBuzzer, Windows Report), not from OpenAI's pricing page.

**Ultrafast**, available only on Pro 500 among the Pro plans, is a faster mode that uses your included usage at 800% of the Standard rate (Fast mode uses 250%). Since October 8, 2026 it works with GPT-6.1 Sol as well as GPT-6 Astra.

## What changed in October 2026

- **October 8:** Ultrafast extended to GPT-6.1 Sol in Codex, ChatGPT Work and the API.
- **October 9:** Codex message predictions (beta, personal Pro, GPT-6 Astra or GPT-6.1 Sol). Generating a suggested next message does not count toward Codex limits or credits; the messages you send still do.
- **October 29:** the last day of the old Pro 200 allowance for subscribers who qualified for the grace period. From October 30 they move to the new, lower Pro 200 allowance at the same price.

The five-hour ranges for Plus and Business Standard did not change in October.

## Why Codex uses the allowance so fast

Like every coding agent, Codex works in steps and sends its whole working context back to the model at each step: instructions, tool definitions, files it has read and earlier steps. A typical 25-step feature task sends around 1.6 million input tokens. On the API that task would cost about $0.72 on a Sol-class model and around $3.60 on GPT-6 Astra, which is why Astra's allowance is so much smaller. See [What does an AI coding agent cost per task?](/blog/ai-coding-agent-cost)

## What one task uses: our measurements

We ran Codex CLI 0.162 with GPT-6 Luna on a ChatGPT plan and logged every token:

| What we ran | Input tokens | Notes |
|---|---:|---|
| A one-word reply, no work | 14,678 | The harness alone: instructions and tool definitions |
| The same, with 10 or 30 idle MCP tools connected | 14,678 | Unchanged: Codex loads MCP tools only when a task needs them |
| A small coding task (a brick-breaker game in one HTML file), 25 runs | median 48,600 (47,677–64,581) | Most of it read from the cache |

Two practical results. First, even a tiny task sends tens of thousands of tokens, because the agent re-sends its context at every step; a long session on a real codebase multiplies that. Second, the language of a short prompt hardly matters: asking for the same game in Korean, Japanese, Spanish or Ukrainian moved Codex's median input by no more than 1.2% compared with English. The raw logs are in [Claude Code vs Codex tokens](/data/claude-code-vs-codex-tokens) and [prompt language and coding cost](/data/ai-coding-prompt-language).

## How to check your usage

OpenAI's help center points to **Settings → Usage** in ChatGPT, which shows your remaining allowance and reset times. Codex also warns you as you approach the limit.

![ChatGPT Usage & billing screen on the Free plan, where Codex shares one monthly usage limit (99% left)](/codex-usage-limits-usage-billing-en.jpg)

Here is that screen on a ChatGPT Free account in the Windows desktop app on October 13, 2026 (the menu is named **Usage & billing**). It confirms that Codex shares its allowance with Work, workspace agents and ChatGPT for Excel, while Chat conversations are not counted. On Free there is no five-hour or weekly meter, just one monthly bar: 99% left, resetting in 27 days 17 hours. A switch lets Codex use a saved usage reset, but only when you ask for it in a conversation and less than 10% of your limit is left; it never happens automatically. The **Usage limit resets** section counts the resets you hold (0 here) and says each one restores your five-hour limit, weekly limit or both.

## When you hit the limit

![When you hit the limit: Wait for the reset. The 5-hour window refills within hours.; Use a banked reset or buy an instant reset, avail](/codex-usage-limits-when-you-hit-the-limit-en.jpg)

1. **Wait for the reset.** The 5-hour window refills within hours.
2. **Use a banked reset or buy an instant reset**, available on eligible Plus and Pro accounts.
3. **Use credits** to keep going on plans that support them.
4. **Upgrade** to a higher Pro tier.
5. **Use an API key** with pay-as-you-go billing for overflow work.

## How to stretch it

![How to stretch it: Default to GPT-6.1 Sol or GPT-6 Sol. Use GPT-6 Astra only for the hard problems where you can see the difference; ](/codex-usage-limits-how-to-stretch-it-en.jpg)

- **Default to GPT-6.1 Sol or GPT-6 Sol.** Use GPT-6 Astra only for the hard problems where you can see the difference: it uses much more of the allowance.
- **Use Luna for simple edits**, renames and boilerplate.
- **Keep tasks small and specific.** Fewer steps means less context resent.
- **Start fresh between unrelated tasks** so old history is not carried along.
- **Point Codex at the right files** instead of letting it search the whole repo.
- **Keep your instruction file short.** AGENTS.md is sent with every request, and in our test Codex silently dropped everything past 32 KiB of it: a code word at the end of a 50 KB file was never seen. If you write it in another language, it also costs more: on GPT's tokenizer, Korean takes about 44% more tokens than English and Japanese 79% more. Details in [CLAUDE.md and AGENTS.md size](/data/claude-md-agents-md-size).

Many of the same habits apply to Claude Code: see [How to save tokens in Claude Code](/blog/claude-code-save-tokens).

## Codex or Claude Code?

Both are included in $20, $100 and $200 plans with similar limit systems. The [ChatGPT Pro vs Claude Max comparison](/blog/chatgpt-pro-vs-claude-max) covers the differences, and the [coding agent calculator](/agents) compares monthly API costs with every plan.

## FAQ

**How many Codex messages do you get on ChatGPT Plus?**
OpenAI's estimate per 5-hour window is about 15–160 local messages with GPT-6.1 Sol, 15–150 with GPT-6 Sol, 5–45 with GPT-6 Astra and 350–3,000 with GPT-6 Luna. A weekly cap applies on top, and long multi-step tasks sit at the low end of each range.

**Does ChatGPT Pro have a Codex limit?**
Pro 100, 200 and 500 have no five-hour window, but each has an included allowance. It is reported as 5×, 10× and 25× Plus; OpenAI's own page only says each tier includes more than the one below.

**When does the Codex limit reset?**
The five-hour window starts with your first request after the previous one ends, so it is not a fixed clock time. The weekly limit resets on its own date. Settings → Usage in ChatGPT shows both, and `/status` shows them in the Codex CLI.

**Does writing prompts in another language use more Codex allowance?**
Barely, for short prompts: in our test the same task asked in Korean, Japanese, Spanish or Ukrainian changed Codex's median input by no more than 1.2% compared with English. Long instruction files are different, because they are sent with every request and other languages need more tokens for the same text.

*Limits change often. OpenAI's [Codex and Work usage help page](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex) has the current numbers.*

## Sources

- [OpenAI Help: Managing usage with GPT-6 Astra in Work and Codex](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)
- [OpenAI Help: How banked Codex resets work](https://help.openai.com/en/articles/20001498-how-banked-codex-resets-work)
- [ChatGPT plans and Codex pricing](https://learn.chatgpt.com/docs/pricing)
- [OpenAI Help: About ChatGPT Pro tiers](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [OpenAI Help: ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
<!-- autoimg -->
