ChatGPT Plus, Claude Pro and Google AI Pro all cost about $20 a month. The same companies also sell their models through an API, where you pay only for the tokens you use. For many people the API is far cheaper. For others, a subscription is a bargain. Which one you are depends almost entirely on how much you chat.

## What you pay for in each case

**A subscription** is a flat monthly price with usage limits. It includes the app, file uploads, image generation, voice, memory and other features. Current US prices: ChatGPT Go $8, Plus $20, Pro $100 / $200 / $500; Claude Pro $20, Max $100 / $200; Google AI Plus $4.99, AI Pro $19.99, AI Ultra $99.99 / $199.99.

**The API** charges per token: what you send in, and what the model writes back. There is no app, so you use it through a third-party chat client or your own tool.

## What a month of chat costs on the API

Assume a typical message in an ongoing conversation sends about 3,000 input tokens (your message plus the conversation so far) and gets back 500 output tokens. At API prices checked October 1, 2026:

| Messages per month | GPT-6 Sol | Gemini 3.8 Flash | GPT-6 Luna |
|---|---|---|---|
| 300 (10 a day) | $3.30 | $1.24 | $0.17 |
| 900 (30 a day) | $9.90 | $3.71 | $0.49 |
| 1,800 (60 a day) | $19.80 | $7.42 | $0.99 |
| 6,000 (200 a day) | $66.00 | $24.75 | $3.30 |

On GPT-6 Sol, each message like this costs about $0.011, so $20 buys roughly 1,800 messages a month. Below that, the API is cheaper than Plus. Above it, Plus wins, and the gap grows quickly for heavy users.

## What moves the break-even point

- **Long chats.** Every message re-sends the whole conversation, so a long chat can make each message 5–10 times more expensive. Heavy users of long conversations hit the break-even point much sooner.
- **Documents.** Pasting a 20-page document adds around 10,000 tokens to every message that follows it.
- **Your language.** Korean uses about 1.44× the tokens of English, Japanese about 1.79×. On the API you pay for that; on a subscription you mostly do not.
- **The model.** A small model can be 20 times cheaper per token than a flagship one.
- **Features.** If you rely on image generation, voice mode or deep research, those are included in the plans and cost extra (or are not available) through a plain chat API.

## Rules of thumb

- **A few questions a day:** the API, or a free plan, is cheaper.
- **Daily work, mostly short chats:** a $20 plan and the API are close. Choose by features.
- **Heavy daily use, long documents, coding all day:** a subscription is usually much cheaper than the same usage on the API.
- **Pro and Max tiers:** compare them with each other by usage per dollar. The [ChatGPT Pro 100 vs 200 vs 500 comparison](/blog/chatgpt-pro-100-vs-200-vs-500) shows that the larger plans no longer give a bulk discount.

## Calculate it for yourself

The [Subscription vs API calculator](/plans) takes your number of messages, how long they are, how many turns a chat usually has and your language, and shows the monthly API cost next to every plan for ChatGPT, Claude and Gemini.

*Prices change often. Confirm current prices on each provider's pricing page.*
