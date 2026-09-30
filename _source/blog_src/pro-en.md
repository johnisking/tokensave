On September 29, 2026 OpenAI split ChatGPT Pro into three plans: **Pro 100**, **Pro 200** and a new **Pro 500**. It also quietly cut how much you get on Pro 200. If you are deciding between them, or wondering whether you need Pro at all, here is what actually changed and how to pick.

![ChatGPT plans compared by usage and price](/blog-chatgpt-pro-tiers.png)

## The plans side by side

| Plan | Price / month | Usage vs Plus | Price per "Plus-worth" of usage | Ultrafast |
|---|---:|---:|---:|:---:|
| Go | $8 | lower | – | – |
| Plus | $20 | 1× | $20 | – |
| Pro 100 | $100 | 5× | $20 | – |
| Pro 200 | $200 | 10× | $20 | – |
| Pro 500 | $500 | 25× | $20 | ✓ |

US prices. OpenAI's help page only says that Pro 200 includes more usage than Pro 100 and Pro 500 the most; the 5×, 10× and 25× figures are the multipliers reported from OpenAI's announcement.

All three Pro plans include the same features: Pro models, Codex, deep research, image creation, memory and file uploads. The only feature difference is **Ultrafast**, a faster mode for GPT-6 Astra, which is Pro 500 only. Buying extra credits on Pro 100 or Pro 200 does not unlock it.

## The part most people miss: there is no bulk discount any more

Divide each price by the usage you get and every plan lands on the same number: **$20 per Plus-worth of usage**. Pro 500 is not a better deal than Pro 100; it is just more of the same thing, plus speed.

That used to be different. Until this change Pro 200 gave **20×** Plus usage, which worked out to $10 per unit, half the price of everything else. New Pro 200 subscribers now get **10×**. If you were already on Pro 200, you keep the old 20× allowance until **October 29, 2026**, then drop to 10× at the same $200.

So the rule is simple: **buy the smallest plan you don't hit the limit on.** Paying for headroom you never use is the only way to overpay.

## Which one should you pick?

- **You rarely hit the Plus limit:** stay on Plus ($20). None of the Pro plans give you a smarter answer for everyday chat; they give you more of it.
- **You hit the Plus limit a few times a week:** Pro 100. Five times the usage for five times the price, and the jump from $20 to $100 is the smallest step up.
- **You regularly run out on Pro 100:** Pro 200. Same price per unit, twice the room.
- **You run Codex or agents most of the day, or waiting on output costs you money:** Pro 500. It is the only plan with Ultrafast, but note that faster generation uses your allowance faster too.
- **You're on the old Pro 200:** keep it until October 29; it is the best deal OpenAI sells right now. After that, look at how much you actually used. If you stayed under about a quarter of your old allowance, Pro 100 does the same job for $100 less.

## What about just using the API?

If you mostly send short or medium messages, paying per token is often much cheaper than any Pro plan. Here is roughly what a month of chat costs through the API, assuming conversations of 6 messages and English text:

| Your usage | GPT-6 Sol API | GPT-6 Astra API |
|---|---:|---:|
| 30 normal messages a day | ≈ $8 | ≈ $39 |
| 80 normal messages a day | ≈ $21 | ≈ $103 |
| 80 long messages a day (pasting documents) | ≈ $59 | ≈ $294 |
| 200 long messages a day | ≈ $147 | ≈ $735 |

"Normal" = about 150 tokens in and 500 out per message; "long" = about 2,000 in and 700 out. API prices: Sol $2 / $10 and Astra $10 / $50 per million input / output tokens.

Two things push the numbers up fast. First, every new message re-sends the whole conversation, so long chats cost far more than short ones. Second, languages other than English need more tokens for the same text: Korean about 1.4×, Japanese about 1.8×, so the API bill grows by the same factor.

The takeaway: light and medium users of the everyday model are usually better off on Plus or the API. Pro starts to pay off when you use the top models heavily, work with long documents, or live in Codex.

## Check your own numbers

Everyone's usage is different. The [Subscription vs API calculator](/plans) lets you enter how many messages you send, how long they are and which language you write in, and shows what the same month would cost on the API next to ChatGPT, Claude and Gemini plans.

*Prices as of October 1, 2026. OpenAI may change allowances again; check chatgpt.com/pricing before you buy.*
