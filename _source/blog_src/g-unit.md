![AI Cost per User: How to Price an App Built on an LLM](/ai-cost-per-user-en.jpg)

If you are building a product on top of an AI model, the most important number in your business plan is not the price per million tokens. It is **AI cost per user per month**. That number decides whether a free tier is affordable, what you can charge, and whether your heaviest users make or lose you money. Here is how to estimate it.

## Step 1: describe a typical user

![Step 1: describe a typical user: Active on 15 days a month; 10 messages on each active day, so 150 messages a month; Each message sends about 2](/ai-cost-per-user-step-1-describe-a-typical-user-en.jpg)

Start with behavior, not tokens. For a chat-style assistant, for example:

- Active on 15 days a month
- 10 messages on each active day, so 150 messages a month
- Each message sends about 2,500 input tokens (system prompt, recent conversation, the new message)
- Each answer is about 400 output tokens

Measure these from a prototype if you can. Paste a real system prompt and a real conversation into the [token counter](/) rather than guessing.

## Step 2: cost per message

![Step 2: cost per message: Model, Input $/M, Output $/M, Cost per message](/ai-cost-per-user-step-2-cost-per-message-en.jpg)

At API prices checked October 1, 2026:

| Model | Input $/M | Output $/M | Cost per message |
|---|---|---|---|
| GPT-6 Luna | 0.10 | 0.50 | $0.00045 |
| Gemini 3.8 Flash | 0.75 | 3.75 | $0.0034 |
| GPT-6 Sol | 2.00 | 10.00 | $0.0090 |
| Claude Opus 5.5 | 4.00 | 20.00 | $0.0180 |

## Step 3: cost per user per month

![Step 3: cost per user per month: Model, Typical user / month](/ai-cost-per-user-step-3-cost-per-user-per-month-en.jpg)

Multiply by 150 messages:

| Model | Typical user / month |
|---|---|
| GPT-6 Luna | $0.07 |
| Gemini 3.8 Flash | $0.51 |
| GPT-6 Sol | $1.35 |
| Claude Opus 5.5 | $2.70 |

On a $9.99 monthly subscription, even the most expensive model leaves room for a profit on a typical user. But typical users are not the problem.

## Step 4: plan for the heavy tail

Usage in AI products is very uneven. A small share of users often accounts for a large share of messages. Suppose the top 5% of users send 900% more than the typical user, with longer conversations that increase input size by 100%:

- 1,500 messages a month at 5,000 input and 400 output tokens
- On GPT-6 Sol: 1,500 × ($0.010 + $0.004) = **$21 a month**

On a $9.99 plan, that user loses you money every month. This is why most AI products have usage limits, even on paid plans.

## Step 5: price the free tier

Free users cost money too. If free users average 30 messages a month on Gemini 3.8 Flash, each costs about $0.10. With 10,000 free users that is around $1,000 a month, before any of them pay. Decide what conversion rate makes that worthwhile.

## Levers that change the numbers

1. **Model routing.** Send most messages to a small model and only hard ones to a large model. If 80% of messages can go to a model 90% cheaper, the blended cost drops by roughly 70%.
2. **Prompt caching.** If your system prompt is long, caching can cut the cost of that part by around 90%. See [Prompt caching explained](/blog/prompt-caching-explained).
3. **History limits.** Summarize old turns instead of resending whole conversations. Input per message stops growing.
4. **Output limits.** Shorter default answers, with "tell me more" for people who want detail.
5. **Usage caps per plan.** Generous enough for typical users, firm enough to protect against the heavy tail.
6. **Language.** If most of your users write in Japanese or Korean, expect 40–80% more tokens than English for the same conversations.

## A simple model to start from

    monthly cost per user = messages per month
                          × (input tokens × input price + output tokens × output price) / 1,000,000

Calculate it for a typical user, a heavy user and a free user, and check each one against what that user pays. Then revisit the numbers every few months: model prices tend to fall, and your users' behavior will change.

## Related

- [How to estimate your AI API bill before you build](/blog/how-to-estimate-ai-api-cost)
- [ChatGPT Plus or the API: which is cheaper?](/blog/chatgpt-subscription-vs-api)
- [Why output tokens cost more](/blog/why-output-tokens-cost-more)

## Sources

- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [GPT-6 Sol model page (OpenAI)](https://developers.openai.com/api/docs/models/gpt-6-sol)
- [Gemini Developer API pricing (Google)](https://ai.google.dev/gemini-api/docs/pricing)
- [Claude API pricing (Anthropic)](https://platform.claude.com/docs/en/about-claude/pricing)
- [Prompt caching (Claude docs)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
<!-- autoimg -->
