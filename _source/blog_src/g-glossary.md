![AI Cost Glossary: 30 Terms Explained in Plain Language](/ai-cost-glossary-en.jpg)

AI pricing pages and documentation are full of terms that are rarely explained. This glossary covers the words you need to understand what you are paying for, in plain language, with links to longer guides where they exist.

## Tokens and text

**Token.** A piece of text from the model's vocabulary: a word, part of a word, a number chunk or a symbol. In English, about 4 characters on average. AI usage is measured and billed in tokens. [Full guide](/blog/what-is-a-token).

**Tokenizer.** The program that cuts text into tokens before the model reads it. Each model family has its own, so the same text can be a different number of tokens on different models.

**Vocabulary.** The fixed list of tokens a tokenizer knows. GPT's current o200k tokenizer has about 200,000.

**BPE (byte-pair encoding).** The method most tokenizers use to build their vocabulary: start from bytes and repeatedly merge the most common pairs. [How it affects languages](/blog/gpt-tokenizer-cl100k-vs-o200k).

**o200k / cl100k.** OpenAI's two most recent tokenizers. cl100k was used by GPT-3.5 and GPT-4; o200k by GPT-4o and later models.

**Token ratio.** How many tokens a language needs compared with English for the same meaning. Korean is about 1.44× on o200k, Japanese about 1.79×.

## Prices and billing

**Input tokens.** Everything you send: system prompt, conversation history, documents and the new message.

**Output tokens.** Everything the model writes, including hidden reasoning. Usually 2–6 times the price of input. [Why](/blog/why-output-tokens-cost-more).

**Price per million tokens (per 1M, /MTok).** The standard unit on price lists. $2 per million means $0.000002 per token.

**Cached input.** Input tokens read from the provider's prompt cache, billed at a large discount. [Prompt caching explained](/blog/prompt-caching-explained).

**Batch pricing.** A discounted rate, commonly around half price, for requests you submit as a batch and collect later. [Batch APIs](/blog/batch-api-half-price).

**Reasoning tokens.** Hidden "thinking" a reasoning model does before answering. Billed as output. [When it is worth it](/blog/reasoning-models-cost).

**Rate limit.** The maximum number of requests or tokens you can use per minute or per day on an API account.

**Usage limit.** On a subscription plan, how much you can use in a period before you are slowed down or asked to wait.

## Models and context

**Context window.** The maximum number of tokens a model can consider at once, including the conversation so far and its own answer. [Context windows explained](/blog/context-window-explained).

**Max output tokens.** The longest answer a model can write in one response, often much smaller than the context window.

**System prompt.** Instructions sent before the conversation that set the model's role and rules. Sent with every request, so its length matters. [Writing shorter prompts](/blog/write-shorter-prompts).

**Reasoning model.** A model that works through a problem in hidden steps before answering. Better at hard problems, slower and more expensive.

**Effort level.** A setting on some reasoning models that controls how much they think.

**Flagship / small model.** The largest, most capable and most expensive model in a family, versus faster, cheaper versions for simpler tasks.

## Building with AI

**API.** The programming interface you use to send requests to a model and pay per token, as opposed to a monthly chat subscription. [Plan or API?](/blog/chatgpt-subscription-vs-api)

**Prompt caching.** Reusing the processed start of a prompt across requests, billed at a discount.

**Structured output.** A mode that makes the model return valid JSON matching a schema you provide. [Cheapest data formats](/blog/json-vs-yaml-vs-csv-tokens).

**RAG (retrieval-augmented generation).** Searching your documents for relevant passages and sending only those to the model. [RAG vs long context](/blog/rag-vs-long-context-cost).

**Embedding.** A list of numbers representing the meaning of a text, used to search for similar passages in RAG.

**Agent.** A system where the model takes actions in steps, such as reading files and running commands, and sends its growing context back each time. [What agents cost](/blog/ai-coding-agent-cost).

**Routing.** Sending each request to a different model depending on how hard it is. [Cost per user](/blog/ai-cost-per-user).

## Images and video

**Per-image pricing.** Image models charge a fixed price per generated image, usually higher at larger resolutions and quality settings. [Price per image](/blog/ai-image-cost-per-image).

**Megapixel billing.** Some image models charge per million pixels of output instead of per image.

**Per-second pricing.** Video models charge for each second of generated video, often more with audio or at higher resolution. [One minute of AI video](/blog/ai-video-cost-per-minute).

## Calculate it

The [token counter](/), [video](/video) and [image](/image) cost calculators, [Subscription vs API](/plans) and [agent cost](/agents) tools turn all of these into real numbers for your own use.
<!-- autoimg -->
