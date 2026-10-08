![How to Save Tokens in Claude Code: 9 Habits That Matter](/claude-code-save-tokens-en.jpg)

Claude Code is powerful, and hungry. A single task can send over a million tokens to the model, which either burns through your Pro or Max limits or shows up on your API bill. The good news: most of that is waste you can cut without changing what Claude Code does for you. Here are the habits that matter most, roughly in order of impact.

## Why the tokens add up

Claude Code works in steps, and at every step it resends its **whole working context**: your instructions, tool definitions, every file it has read, and everything that happened in earlier steps. A 25-step feature task that starts with 22,000 tokens of context and grows by 3,500 tokens a step sends around **1.6 million input tokens** in total. Anything that makes the context smaller, or the task shorter, pays off at every step.

## 1. Keep tasks small and specific

The number of steps is the biggest multiplier. Compare:

- "Clean up the auth module" → open-ended, dozens of steps.
- "Fix the failing test in tests/auth_test.py; the token expiry check is off by one" → a handful of steps.

Breaking a large job into clear sub-tasks often uses far fewer tokens in total than one vague request, and gives better results.

## 2. Start fresh between unrelated tasks

A long session carries its whole history into every new step. When you switch to something unrelated, run **/clear**. If you want to keep going on the same work but the session has grown long, run **/compact** to replace the history with a summary.

## 3. Tell Claude where to look

Searching costs steps, and every file read stays in the context. If you know the relevant files, name them: "the bug is in src/billing/invoice.ts, around calculateTax". Claude reads one file instead of ten.

## 4. Keep CLAUDE.md short

Your project instructions are sent with **every step of every task**. A 2,000-token CLAUDE.md in a 25-step task adds 50,000 input tokens. Keep it to the rules Claude actually needs: build and test commands, conventions it would otherwise get wrong. Move long background documentation into separate files Claude can read when needed.

## 5. Don't paste huge logs

A full test run or build log can be thousands of lines. The first error and its stack trace usually carry all the information. Paste that, or ask Claude to run the specific failing test.

## 6. Ask for changes, not whole files

Output tokens are the most expensive kind: $10 per million on Sonnet 5.5 versus $2 for input. Asking for a full file to be rewritten after a two-line fix pays output prices for every unchanged line.

## 7. Pick the model for the task

On the API, Claude Opus 5.5 costs twice as much per token as Sonnet 5.5, and on a plan it uses your allowance faster. Use **/model** to switch: Sonnet for most coding, Opus for hard design problems and tricky bugs, Haiku for simple, repetitive edits.

## 8. Write instructions in English

If you normally write prompts in another language, this is an easy win. On GPT's tokenizer the same text takes about 1.44× the tokens in Korean and 1.79× in Japanese compared with English, so instructions written in English use roughly 31% and 44% fewer tokens. Claude's tokenizer is different, but non-English text costs more there too. Write CLAUDE.md and long instructions in English and ask for replies in your language. Our [token counter](/) can translate a prompt to English on your device with one click and shows the saving.

## 9. Let caching work

Claude Code caches the repeated part of its context automatically, and cached input costs about 10% of the normal price. You help it by keeping things stable: don't edit CLAUDE.md mid-session and avoid restarting sessions just to continue the same task. See [Prompt caching explained](/blog/prompt-caching-explained).

## How much difference does it make?

On our [coding agent cost model](/agents), a typical feature task on Sonnet 5.5 costs about $0.72 with caching. Cutting it from 25 steps to 15 by giving a precise task and pointing to the right files brings it to roughly $0.40, and starting each task in a fresh session keeps the starting context small. Across 100 tasks a month, that is the difference between hitting your weekly limit and not.

## Check your usage

Run **/status** in Claude Code to see how much of your allowance is left. To understand the limits themselves, read [Claude Code usage limits explained](/blog/claude-code-usage-limits), and to compare plans with the API, [Claude Code cost per month](/blog/claude-code-cost-per-month).
<!-- autoimg -->
