![What Does an AI Coding Agent Really Cost per Task?](/ai-coding-agent-cost-en.jpg)

Coding agents such as Claude Code, Codex and Gemini CLI do far more than answer a question. They read files, run commands, look at the results, and try again, often dozens of times for a single task. Every one of those steps is a full request to the model. That is why an agent can burn through more tokens in an afternoon than a chat user does in a month, and why the choice between a subscription and the API matters so much.

## Why agents use so many tokens

![Why agents use so many tokens: 25 steps; about 22,000 tokens of context at the start (instructions, tool descriptions, the first files); abou](/ai-coding-agent-cost-why-agents-use-so-many-tokens-en.jpg)

A chat message is one request. An agent task is a loop: plan, read a file, edit, run the tests, read the error, edit again. At each step the agent sends its **whole working context** back to the model: the system prompt, the tool definitions, the files it has read and everything that happened in earlier steps. The context grows with every step, and the agent pays for all of it again each time.

A typical medium-sized task might look like this:

- 25 steps
- about 22,000 tokens of context at the start (instructions, tool descriptions, the first files)
- about 3,500 new tokens added per step
- about 700 output tokens written per step

Add that up and one task sends roughly **1.6 million input tokens** and writes about 17,500 output tokens.

## What one task costs on the API

![What one task costs on the API: Model, Small task (8 steps), Feature (25 steps), Big task (60 steps)](/ai-coding-agent-cost-what-one-task-costs-on-the-api-en.jpg)

Using API prices checked October 1, 2026:

| Model | Small task (8 steps) | Feature (25 steps) | Big task (60 steps) |
|---|---|---|---|
| Claude Haiku 4.5 | $0.08 | $0.36 | $1.33 |
| DeepSeek V4 Pro | $0.09 | $0.43 | $1.61 |
| Claude Sonnet 5.5 | $0.15 | $0.72 | $2.65 |
| GPT-6 Sol | $0.15 | $0.72 | $2.65 |
| Gemini 3.1 Pro | $0.16 | $0.75 | $2.76 |
| Claude Opus 5.5 | $0.31 | $1.43 | $5.30 |

These figures assume **prompt caching**, where the repeated part of the context is billed at about 10% of the normal input price. Without caching, the same feature task on Claude Sonnet 5.5 costs about $3.38 instead of $0.72, almost five times as much. Make sure your agent uses caching.

## From one task to a month

![From one task to a month: Claude Sonnet 5.5 or GPT-6 Sol; Claude Opus 5.5; Claude Haiku 4.5](/ai-coding-agent-cost-from-one-task-to-a-month-en.jpg)

Ten feature-sized tasks a day, on 22 working days, is 220 tasks a month:

- Claude Sonnet 5.5 or GPT-6 Sol: about **$158 a month**
- Claude Opus 5.5: about **$315 a month**
- Claude Haiku 4.5: about **$79 a month**

## Subscription or API?

Both Anthropic and OpenAI include their agents in their consumer plans: Claude Code comes with Claude Pro ($20) and Max ($100 / $200), and Codex with ChatGPT Plus ($20) and Pro ($100 / $200 / $500). Plans have usage limits, but for steady daily use they are usually far cheaper than paying the API rate for the same work.

The API makes sense when you use an agent occasionally, when you need a model that is not in a plan, when you run agents in automated pipelines, or when you need predictable billing for a team.

## How to cut agent costs

1. **Keep tasks small and specific.** "Fix the failing test in auth.py" uses far fewer steps than "clean up the project".
2. **Start fresh sessions.** A long session drags its whole history into every step. Clear or compact it between unrelated tasks.
3. **Point to the right files.** Telling the agent where to look saves the steps it would spend searching.
4. **Use a smaller model for routine work.** Renames, small fixes and boilerplate rarely need the largest model.
5. **Keep project instructions short.** Instruction files are sent with every step of every task.

## Estimate your own usage

The [AI coding agent cost calculator](/agents) lets you set task size, tasks per day and working days, toggles caching, and compares the API cost with every Claude and ChatGPT plan.

*Prices and plan limits change often. Confirm on each provider's pricing page.*
<!-- autoimg -->
