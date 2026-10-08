![Why Output Tokens Cost More (and 6 Ways to Use Fewer)](/why-output-tokens-cost-more-en.jpg)

Look at any AI API price list and you will see two prices per model: one for input tokens and a higher one for output tokens. The gap is not small. On most current models, every token the model writes costs 300–500% more than every token you send. If you want a lower bill, the answer is usually not a shorter prompt. It is a shorter answer.

## How big is the gap?

![How big is the gap?: Model, Input, Output, Output vs input](/why-output-tokens-cost-more-how-big-is-the-gap-en.jpg)

API prices per million tokens, checked October 1, 2026:

| Model | Input | Output | Output vs input |
|---|---|---|---|
| GPT-6 Sol | $2.00 | $10.00 | +400% |
| GPT-5.5 | $5.00 | $30.00 | +500% |
| Claude Opus 5.5 | $4.00 | $20.00 | +400% |
| Claude Haiku 4.5 | $1.00 | $5.00 | +400% |
| Gemini 3.1 Pro | $2.00 | $12.00 | +500% |
| DeepSeek V4 Pro | $1.32 | $3.96 | +200% |
| Grok 4.20 | $1.25 | $2.50 | +100% |

## Why output costs more

**Input is read in parallel; output is written one token at a time.** When you send a prompt, the model processes all of it in one large, efficient pass. When it answers, it has to generate the first token, then run again to produce the second, then the third. Each output token needs its own pass through the model, which ties up expensive hardware for longer.

**Output also holds memory.** While generating, the model keeps a growing cache of everything it has read and written so far. Long answers keep that memory occupied, which limits how many requests a server can handle at once.

Providers price output higher to reflect that cost.

## The hidden output: reasoning tokens

Reasoning models think before they answer. That thinking is made of tokens, it is usually not shown to you, and it is **billed at the output price**. A two-paragraph answer can sit on top of thousands of reasoning tokens. If a reasoning model feels expensive, this is usually why.

## Six ways to use fewer output tokens

![Six ways to use fewer output tokens: Ask for the length you need. "Answer in 3 bullet points" or "under 100 words" works well. Models follow length](/why-output-tokens-cost-more-six-ways-to-use-fewer-output-tokens-en.jpg)

1. **Ask for the length you need.** "Answer in 3 bullet points" or "under 100 words" works well. Models follow length instructions better than most people expect.
2. **Set a maximum output length.** In the API, set a token limit so a runaway answer cannot cost more than you planned.
3. **Ask for the change, not the whole thing.** When editing code or a document, ask for only the changed lines or a diff instead of the full file again.
4. **Use structured output.** Ask for JSON with exactly the fields you need. It removes greetings, recaps and closing summaries.
5. **Turn reasoning down when it is not needed.** Many APIs let you set a lower reasoning effort. Simple extraction, classification and formatting tasks rarely need deep thinking.
6. **Pick the model per task.** A small model for short, routine answers and a large one only for hard problems can cut the bill by well over half.

## A quick example

A request with 2,000 input tokens and 1,000 output tokens on GPT-6 Sol costs $0.004 for input and $0.010 for output: output is 71% of the bill even though it is only a third of the tokens. Cut the answer to 400 tokens and the request drops from $0.014 to $0.008, a 43% saving without touching the prompt.

## Measure it

Paste a typical prompt and a typical answer into the [token counter](/) to see how many tokens each side uses and what that costs on 30+ models. To trim the input side as well, see [how to write shorter prompts](/blog/write-shorter-prompts).

## Sources

- [GPT-6 Sol model page (OpenAI)](https://developers.openai.com/api/docs/models/gpt-6-sol)
- [GPT-5.5 model page (OpenAI)](https://developers.openai.com/api/docs/models/gpt-5.5)
- [Claude API pricing (Anthropic)](https://platform.claude.com/docs/en/about-claude/pricing)
- [Gemini Developer API pricing (Google)](https://ai.google.dev/gemini-api/docs/pricing)
- [DeepSeek API models and pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [xAI API pricing](https://docs.x.ai/developers/pricing)
- [Reasoning models guide (OpenAI)](https://developers.openai.com/api/docs/guides/reasoning)
<!-- autoimg -->
