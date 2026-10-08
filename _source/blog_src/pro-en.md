On September 29, 2026 OpenAI split ChatGPT Pro into three plans: **Pro 100**, **Pro 200** and a new **Pro 500**. It also quietly cut how much you get on Pro 200. If you are deciding between them, or wondering whether you need Pro at all, here is what actually changed and how to pick.

**Short answer:** pick the smallest plan you don't hit the limit on. Pro 100, 200 and 500 all cost the same $20 per Plus-worth of usage; the only differences are how much usage you get (5x, 10x, 25x Plus) and Ultrafast, which is Pro 500 only.

![ChatGPT Pro 500 vs 200 vs 100: Pro 500 $500/month, 25× Plus usage plus Ultrafast; Pro 200 $200, 10× Plus; Pro 100 $100, 5× Plus](/chatgpt-pro-500-200-100-en.jpg)

## The plans side by side

![The plans side by side: Plan, Price / month, Usage vs Plus, Price per "Plus-worth" of usage, Ultrafast](/chatgpt-pro-100-vs-200-vs-500-the-plans-side-by-side-en.jpg)

| Plan | Price / month | Usage vs Plus | Price per "Plus-worth" of usage | Ultrafast |
|---|---:|---:|---:|:---:|
| Go | $8 | lower | – | – |
| Plus | $20 | 1× | $20 | – |
| Pro 100 | $100 | 5× | $20 | – |
| Pro 200 | $200 | 10× | $20 | – |
| Pro 500 | $500 | 25× | $20 | ✓ |

US prices. OpenAI's help page only says that Pro 200 includes more usage than Pro 100 and Pro 500 the most; the 5×, 10× and 25× Plus figures come from OpenAI's Thibault Sottiaux on X (5× and 10×, as reported by WinBuzzer) and press reports (25×, Windows Report), not from OpenAI's pricing page.

All three Pro plans include the same features: Pro models, Codex, deep research, image creation, memory and file uploads. The only feature difference is **Ultrafast**, a faster mode for GPT-6 Astra, which is Pro 500 only. Buying extra credits on Pro 100 or Pro 200 does not unlock it.

## The part most people miss: there is no bulk discount any more

Divide each price by the usage you get and every plan lands on the same number: **$20 per Plus-worth of usage**. Pro 500 is not a better deal than Pro 100; it is just more of the same thing, plus speed.

That used to be different. Until this change Pro 200 gave **20×** Plus usage, which worked out to $10 per unit, half the price of everything else. New Pro 200 subscribers now get **10×**. If you had an active Pro 200 subscription at any point from September 22 to September 29, 2026, you keep the old 20× allowance until **October 29, 2026**, then drop to 10× at the same $200.

So the rule is simple: **buy the smallest plan you don't hit the limit on.** Paying for headroom you never use is the only way to overpay.

## Pro 500: pros and cons

![ChatGPT Pro 500 pros and cons: most usage, Ultrafast, computer-use agents vs $500 a month, no bulk discount](/chatgpt-pro-500-pros-cons-en.jpg)

**Pros**

- **The most usage:** 25× Plus usage (as reported by Windows Report). Running Codex or agents all day rarely hits the limit.
- **Ultrafast is Pro 500 only:** a mode that runs GPT-6 Astra at up to 300 tokens per second in ChatGPT Work and Codex (per DevDay).
- **Computer-use agents:** per DevDay, Pro 500 is the individual plan that gets the computer-use agent in Codex and ChatGPT Work (otherwise Enterprise).
- **No penalty for buying big:** it costs the same $20 per Plus-worth of usage as Pro 100 and 200.

**Cons**

- **$500 a month:** the most expensive individual plan. Unused usage is wasted money.
- **No bulk discount:** the unit price equals Pro 100 and 200, so buying more does not make it cheaper.
- **Ultrafast burns your allowance faster:** faster output uses the limit faster too.
- **Ultrafast is Astra-only for now:** Ultrafast for GPT-6.1 Sol was only announced as "coming soon."
- **Exact limits are not published:** OpenAI's help page only says Pro 500 has the most.

How and when each plan's limits reset is covered in [ChatGPT usage limits](/blog/chatgpt-usage-limits).

**Good for:** people who hit the Pro 200 limit every week, who run Codex or agents all day, or for whom waiting time costs money.

## Which one should you pick?

![Which one should you pick?: You rarely hit the Plus limit; You hit the Plus limit a few times a week; You regularly run out on Pro 100](/chatgpt-pro-100-vs-200-vs-500-which-one-should-you-pick-en.jpg)

- **You rarely hit the Plus limit:** stay on Plus ($20). None of the Pro plans give you a smarter answer for everyday chat; they give you more of it.
- **You hit the Plus limit a few times a week:** Pro 100. Five times the usage for five times the price, and the jump from $20 to $100 is the smallest step up.
- **You regularly run out on Pro 100:** Pro 200. Same price per unit, twice the room.
- **You run Codex or agents most of the day, or waiting on output costs you money:** Pro 500. It is the only plan with Ultrafast, but note that faster generation uses your allowance faster too.
- **You're on the old Pro 200:** keep it until October 29; it is the best deal OpenAI sells right now. After that, look at how much you actually used. If you stayed under about a quarter of your old allowance, Pro 100 does the same job for $100 less.

## What about just using the API?

![What about just using the API?: Your usage, GPT-6 Sol API, GPT-6 Astra API](/chatgpt-pro-100-vs-200-vs-500-what-about-just-using-the-api-en.jpg)

If you mostly send short or medium messages, paying per token is often much cheaper than any Pro plan. Here is roughly what a month of chat costs through the API, assuming conversations of 6 messages and English text:

| Your usage | GPT-6 Sol API | GPT-6 Astra API |
|---|---:|---:|
| 30 normal messages a day | ≈ $8 | ≈ $39 |
| 80 normal messages a day | ≈ $21 | ≈ $103 |
| 80 long messages a day (pasting documents) | ≈ $59 | ≈ $294 |
| 200 long messages a day | ≈ $147 | ≈ $735 |

"Normal" = about 150 tokens in and 500 out per message; "long" = about 2,000 in and 700 out. API prices: Sol $2 / $10 and Astra $10 / $50 per million input / output tokens.

Two things push the numbers up fast. First, every new message re-sends the whole conversation, so long chats cost far more than short ones. Second, languages other than English need more tokens for the same text: Korean needs about 44% more tokens than English and Japanese about 79% more, so the API bill grows by the same percentage.

The takeaway: light and medium users of the everyday model are usually better off on Plus or the API. Pro starts to pay off when you use the top models heavily, work with long documents, or live in Codex.

## Check your own numbers

Everyone's usage is different. The [Subscription vs API calculator](/plans) lets you enter how many messages you send, how long they are and which language you write in, and shows what the same month would cost on the API next to ChatGPT, Claude and Gemini plans.

*Prices as of October 1, 2026. OpenAI may change allowances again; check chatgpt.com/pricing before you buy.*
Sources: [OpenAI DevDay 2026 recap](https://openai.com/index/devday-2026-recap/) · [Every DevDay announcement with prices and availability (DEV Community)](https://dev.to/axrisi/openai-devday-2026-every-announcement-with-prices-and-availability-1mbh) · [About ChatGPT Pro tiers (OpenAI Help Center)](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers) · [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/) · [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
<!-- autoimg -->
