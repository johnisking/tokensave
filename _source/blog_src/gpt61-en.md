OpenAI released **GPT-6.1 Sol** at DevDay on September 29, 2026, one week after GPT-6 Sol. The list price did not change: $2 per million input tokens and $10 per million output. What changed is the price of cached input, which halved, and the model itself, which OpenAI says is clearly better at coding, agent work and getting facts right. Here is what it costs, how it compares with Claude Opus 5.5 and Sonnet 5.5, and whether to switch.

## GPT-6.1 Sol API pricing

Per million tokens:

| Model | Input | Cached input | Output |
|---|---:|---:|---:|
| **GPT-6.1 Sol** | $2.00 | **$0.10** | $10.00 |
| GPT-6 Sol | $2.00 | $0.20 | $10.00 |
| GPT-6 Astra | $10.00 | $1.00 | $50.00 |
| GPT-6 Luna | $0.10 | $0.01 | $0.50 |

Prompts with more than 272,000 input tokens are billed at twice the input and cached rates and 1.5 times the output rate. The context window is about 1 million tokens, with up to 128,000 tokens of output. The API model name is `gpt-6.1-sol`.

## What the cheaper cache means in practice

For a single request with no repeated text, GPT-6.1 Sol and GPT-6 Sol cost exactly the same. The difference shows up when you resend the same instructions, documents or conversation, which is most real apps and every coding agent:

- **A chatbot with 10,000 tokens of fixed instructions**, 1,000 new tokens and a 500-token answer: $0.0080 per request on GPT-6.1 Sol, $0.0090 on GPT-6 Sol, **about 11% less**.
- **A coding agent step** that re-reads 24,000 cached tokens, adds 1,000 new ones and writes 800: $0.0124 on GPT-6.1 Sol, $0.0148 on GPT-6 Sol, **about 16% less**.

The more of your prompt is repeated, the bigger the saving. If you are not using prompt caching yet, start there: put fixed content first and changing content last. See [Prompt caching explained](/blog/prompt-caching-explained).

## GPT-6.1 Sol vs Claude Opus 5.5 and Sonnet 5.5

A typical request of 2,000 input and 500 output tokens of English, at list prices with no caching, after each model's tokenizer difference:

| Model | Input / output per 1M | 1 request | 10,000 requests |
|---|---|---:|---:|
| GPT-6.1 Sol | $2 / $10 | $0.0090 | $90 |
| Gemini 3.1 Pro | $2 / $12 | $0.0095 | $95 |
| Claude Sonnet 5.5 | $2 / $10 | $0.0117 | $117 |
| Gemini 4 Argon (standard) | $4 / $20 | $0.0171 | $171 |
| Claude Opus 5.5 | $4 / $20 | $0.0234 | $234 |
| GPT-6 Astra | $10 / $50 | $0.0450 | $450 |

Claude Sonnet 5.5 has the same price per token as GPT-6.1 Sol but costs about 30% more per request, because Claude's tokenizer turns the same English text into about 30% more tokens. **Claude Opus 5.5 costs about 2.6 times as much as GPT-6.1 Sol per request.**

On quality, OpenAI reports GPT-6.1 Sol 2.2 points above Opus 5.5 on AutomationBench (multi-step workflows) at medium effort, and on its Terminal-Bench Science test it spent about $5.47 per task against $23.21 for Opus 5.5. These are OpenAI's own benchmarks; test on your own tasks before you switch a production workload. For an independent view of capability against price, see [AI model capability vs price](/compare/performance).

## What improved over GPT-6 Sol

According to OpenAI:

- **Coding:** 6.4 percentage points higher on the DeepSWE coding benchmark.
- **Accuracy:** about 32% fewer factual errors at low reasoning effort.
- **Computer use:** 7 points higher on OSWorld 2.0.

In ChatGPT it is available in ChatGPT Work and Codex for Plus, Pro, Business, Enterprise and Edu users, not yet in regular chat.

## Should you switch?

- **On GPT-6 Sol: yes.** Same list price, half the cache price, better scores. Change the model name to `gpt-6.1-sol` and run your tests.
- **On Claude Sonnet 5.5 for cost reasons:** GPT-6.1 Sol is about 23% cheaper per request for the same English text. Whether it is as good for your work is the real question; compare on a sample first.
- **On Claude Opus 5.5 or GPT-6 Astra:** GPT-6.1 Sol is worth testing as a cheaper default, keeping the bigger model for the hardest requests.
- **On GPT-6 Luna:** stay unless Luna's answers are not good enough. GPT-6.1 Sol costs 20 times as much per token.

## Check your own prompt

Paste a real prompt into the [OpenAI token counter](/openai-token-counter) to see its cost on GPT-6.1 Sol and every other GPT model, or compare head to head: [GPT-6.1 Sol vs Claude Sonnet 5.5](/compare/gpt-6-1-sol-vs-claude-sonnet-5-5) · [GPT-6.1 Sol vs Claude Opus 5.5](/compare/gpt-6-1-sol-vs-claude-opus-5-5). More on the GPT-6 family: [GPT-6 API pricing](/blog/gpt-6-api-pricing).

*Prices checked October 6, 2026. Check OpenAI's pricing page before you commit.*
