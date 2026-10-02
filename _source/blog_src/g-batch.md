Not every AI request needs an answer in two seconds. Tagging a product catalog, summarizing yesterday's support tickets, translating a help center or running an evaluation can all wait a few hours. For that kind of work, most major AI providers offer a **batch API** at a large discount, commonly half the normal price.

## How batch processing works

Instead of sending requests one by one and waiting for each answer, you:

1. Write all your requests into one file, one request per line.
2. Upload the file and start a batch job.
3. Come back later, typically within 24 hours and often much sooner, and download a file with all the results.

The provider runs your requests when it has spare capacity. In return for giving up the instant response, you pay less, commonly about 50% of the standard price on both input and output tokens. The exact discount, time window and limits depend on the provider, so check its documentation.

## What it saves

A store wants AI-written descriptions for 100,000 products. Each request sends about 400 input tokens (product data and instructions) and gets back about 250 output tokens.

That is 40 million input tokens and 25 million output tokens. At list prices checked October 1, 2026:

| Model | Standard price | With a 50% batch discount |
|---|---|---|
| GPT-6 Sol ($2 / $10 per M) | $330 | $165 |
| Claude Sonnet 5.5 ($2 / $10 per M) | $330 | $165 |
| Gemini 3.8 Flash ($0.75 / $3.75 per M) | $124 | $62 |

For jobs that run every day or every week, the saving adds up quickly.

## Good fits for batch

- **Bulk content:** product descriptions, alt text for images, meta descriptions, translations.
- **Classification and tagging:** support tickets, reviews, documents, transactions.
- **Data extraction:** pulling fields out of invoices, contracts, emails or scraped pages.
- **Evaluations:** running a test set through several prompts or models to compare quality.
- **Embeddings and backfills:** processing an archive once, then switching to real-time for new items.
- **Nightly reports:** summarizing the day's logs, feedback or sales notes.

## Poor fits

- Anything a user is waiting for.
- Multi-step agents, where each step depends on the previous answer.
- Very small jobs, where the setup is not worth a few cents of savings.

## Tips

1. **Test on a small sample first.** Run 20–50 requests normally and check the outputs before submitting 100,000. A mistake in the prompt is repeated in every result.
2. **Give every request an ID.** Results may not come back in the order you sent them. Use your own ID in each request to match them up.
3. **Plan for some failures.** A few requests in a large batch may fail or return something unusable. Collect them and resubmit.
4. **Combine with caching where supported.** If every request starts with the same long instructions, some providers apply prompt-caching discounts inside batches too. See [Prompt caching explained](/blog/prompt-caching-explained).
5. **Keep outputs short.** Output is the expensive side. Ask for exactly the fields you need, ideally as compact JSON.

## Price your job

Measure one typical request and response with the [token counter](/), multiply by the number of items, and halve it for a batch estimate. The [API cost guide](/blog/how-to-estimate-ai-api-cost) walks through the method step by step.
