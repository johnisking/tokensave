![ChatGPT Usage Limits in 2026: What Is Still Capped and When It Resets](/chatgpt-usage-limits-en.jpg)

"You've reached your limit" used to be the most common complaint about ChatGPT. In 2026 the rules changed a lot: everyday text chat no longer has a cap on Free and Go, and Plus has expanded limits, but the newest models, ChatGPT Work and Codex, file uploads, images and voice still do. Here is what is limited on each plan, how the limits reset, and how to check where you stand.

## Text chat: no cap on Free and Go since August 2026

On August 6, 2026, OpenAI announced unlimited text chats for **Free and Go**, starting the following week, with a "Think" button for harder questions. Plus gets "expanded messages and uploads", with limits. Since October 7, 2026, Chat uses GPT-6 Sol on Plus, Pro, Business and Enterprise, and GPT-6 Luna on Free and Go. Unlimited chat is still subject to abuse guardrails, so automated or extreme use can be throttled.

So if you only send ordinary text messages on Free or Go, you should no longer see a message cap.

## What is still limited

![What is still limited: Feature, Limited?](/chatgpt-usage-limits-what-is-still-limited-en.jpg)

| Feature | Limited? |
|---|---|
| Everyday text chat | No on Free and Go (since August 2026); Plus: expanded, limits apply |
| File uploads, image generation, voice | Yes, separate limits per plan |
| Higher thinking levels and Pro models | Yes, by plan |
| ChatGPT Work and Codex (including GPT-6 Astra) | Yes: included allowance, 5-hour window on Plus and Business |

**Thinking levels by plan.** Plus gets advanced reasoning models with GPT-6. Pro adds the Pro reasoning option, powered by GPT-6 Astra, and GPT-5.6 Sol Pro, which only Pro has.

## GPT-6 Astra limits

![GPT-6 Astra limits: Plan, GPT-6 Astra messages per 5 hours](/chatgpt-usage-limits-gpt-6-astra-limits-en.jpg)

GPT-6 Astra, OpenAI's flagship, is used through ChatGPT Work and Codex. OpenAI's help center gives estimated local message ranges per 5-hour window:

| Plan | GPT-6 Astra messages per 5 hours |
|---|---|
| Plus | about 5–45 |
| Standard Business | about 5–45 |
| Pro 100 / 200 / 500 | no 5-hour limit currently |

The range is wide because one long, multi-step task uses far more of the allowance than a short one. Weekly limits may also apply. Pro plans currently have no five-hour limit in Work and Codex but still have an included allowance that grows with the tier: Pro 200 is 10× Plus for new subscribers and Pro 500 is 25× Plus (anyone with an active Pro 200 subscription between September 22 and September 29, 2026 keeps the previous allowance until October 29). These multiples come from OpenAI's Thibault Sottiaux on X and press reports (WinBuzzer, Windows Report), not from OpenAI's pricing page. See [ChatGPT Pro 100 vs 200 vs 500](/blog/chatgpt-pro-100-vs-200-vs-500).

## How the limits reset

![How the limits reset: 5-hour window; Weekly limit; Files, images and voice](/chatgpt-usage-limits-how-the-limits-reset-en.jpg)

- **5-hour window:** rolling, starting from your first request in that window, not at a fixed time of day. It applies to Plus and Business; Pro 100, Pro 200 and Pro 500 currently have no five-hour usage limit in Work and Codex.
- **Weekly limit:** OpenAI says weekly limits may also apply.
- **Files, images and voice:** each has its own allowance.

## How to check your usage

OpenAI's help center points to **Settings → Usage**, which shows your remaining allowance and reset times for Work and Codex. When you hit a limit, ChatGPT also tells you when you can continue.

## What to do when you hit a limit

1. **Wait for the reset.** For the 5-hour window, usually a few hours at most.
2. **Use a reset or credits.** Eligible Plus and Pro accounts can apply banked resets or buy an instant reset, and some plans can continue with credits.
3. **Switch model.** Routine work rarely needs GPT-6 Astra; GPT-6 Sol or GPT-6 Luna use much less of the allowance.
4. **Upgrade.** Pro 100 is 5× Plus, Pro 200 is 10× and Pro 500 is 25×.
5. **Use the API.** For steady heavy use of a specific model, paying per token can be simpler. GPT-6 Astra costs $10 per million input tokens and $50 per million output tokens; see [GPT-6 API pricing](/blog/gpt-6-api-pricing).

## Is there a "token limit" per chat?

Every model has a context window: the maximum amount of text it can consider at once. Very long conversations or documents eventually hit it, and quality drops before that, because the model re-reads the whole conversation with every message. Starting a new chat with a short summary helps more than you might expect. See [Context windows explained](/blog/context-window-explained).

## Plan or API?

If you mostly chat, the August change makes the Free and Go plans much more useful than before. If you use Codex or GPT-6 Astra heavily, compare the plan price with what the same work costs on the API using the [Subscription vs API calculator](/plans) and the [coding agent calculator](/agents).

*Limits change often. OpenAI's [GPT-6 Astra usage help page](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex) has the current numbers.*

## Sources

- [Managing usage with GPT-6 Astra in Work and Codex (OpenAI Help Center)](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)
- [ChatGPT release notes (OpenAI Help Center)](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [ChatGPT pricing](https://chatgpt.com/pricing)
- [About ChatGPT Pro tiers (OpenAI Help Center)](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
- [GPT-6 Astra model and API pricing (OpenAI docs)](https://developers.openai.com/api/docs/models/gpt-6-astra)
<!-- autoimg -->
