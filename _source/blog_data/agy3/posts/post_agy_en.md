# Same model, 68% to 88% fewer tokens: Antigravity CLI vs Claude Code vs Codex, measured

Google stopped serving Gemini CLI to personal accounts on June 18, 2026 and moved people to its new Antigravity CLI (`agy`). Antigravity can run Claude models too, which makes a rare test possible: the same model, Claude Opus 5.5, in two different coding tools. So I ran Antigravity CLI, Claude Code and Codex on the same prompts, 44 runs in total, and checked every game they built in a headless browser.

## How I measured

- Windows 11, 2026-10-22. Every run in its own empty folder, one after another
- Claude Code 2.1.295 with Opus 5.5 (Max plan)
- Codex CLI 0.162 with gpt-6-luna (ChatGPT plan)
- Antigravity CLI 1.4.5 with Gemini 4 Argon and with Claude Opus 5.5 (personal Google account)
- Startup test: "Reply with the single word OK." with 0, 1, 10 and 30 dummy MCP tools, 2 runs each
- Task: a brick-breaker game in one index.html with 2 levels, a score and 3 lives, medium effort, 3 runs each
- Token counts are what each CLI reports in its JSON output

## Result 1: tokens before doing anything

| Tool | Input tokens for "OK" |
|---|---:|
| Claude Code + Opus 5.5 | 35,781 |
| Codex + gpt-6-luna | 14,818 |
| Antigravity + Gemini 4 Argon | 6,745 |
| Antigravity + Opus 5.5 | 5,326 (+5,167 cache reads) |

Most of this is each tool's own instructions and tool definitions, which go out again with every request.

## Result 2: the same coding task

| Tool | Input | Output | Seconds | Lines | Games working |
|---|---:|---:|---:|---:|---:|
| Claude Code + Opus 5.5 | 78,671 | 7,313 | 58 | 451 | 3 of 3 |
| Codex + gpt-6-luna | 55,680 | 4,563 | 68 | 42 (minified) | 3 of 3 |
| Antigravity + Gemini 4 Argon | 13,041 (+6,796 cache) | 6,373 | 81 | 608 | 3 of 3 |
| Antigravity + Opus 5.5 | 9,822 (+15,381 cache) | 4,378 | 42 | 236 | 3 of 3 |

With the same Opus 5.5, Antigravity read 68% to 88% fewer input tokens than Claude Code, wrote 40% fewer output tokens and finished 27% faster. Claude Code's games were longer (451 lines against 236), and Claude Code put each run at $0.37 at API prices. Antigravity and Codex show no price on a subscription.

All 12 games worked: the score rises when bricks break, level 2 appears, lives go 3, 2, 1, 0. My automatic check could not read the score in two of the Codex games, so I checked those by hand; both scored.

## Why a range, not one number

Antigravity's JSON reports `input_tokens` and `cache_read_tokens` separately, and its documentation does not say whether one contains the other. In the Opus runs the cache reads (15,381) were larger than the input (9,822), so there they cannot be inside it. I show both: the reported input as the low end (88% fewer) and input plus cache reads as the high end (68% fewer). Even the high end is far below Claude Code.

## MCP tools barely matter any more

| | 30 MCP tools added |
|---|---:|
| Claude Code | +388 tokens |
| Codex | +0 |
| Antigravity + Gemini | +582 |
| Antigravity + Opus | +417 |

In Antigravity one tool already added about 280 to 460 tokens and the next 29 added little. All four setups now seem to load a tool's full definition only when it is used.

## What to take away

- The coding tool around the model matters as much as the model. The same Opus 5.5 read a fraction of the input in Antigravity.
- Fewer tokens is not the same as a better result. Claude Code wrote longer games; all of them worked in every tool.
- If you were on Gemini CLI with a personal account, Antigravity CLI is the replacement, and it is lean.

## Limits

- 2 runs per startup test, 3 per game. One task, one machine, one day
- Each tool counts cache differently, so compare within a tool's own column with care
- I cannot see how Antigravity sets up Opus 5.5 behind its `claude-opus-5-5-medium` name

## Data

- Full data, per-run CSV and method (CC BY 4.0, DOI 10.5281/zenodo.23569397): https://tokensave.app/data/antigravity-cli-vs-claude-code-vs-codex
- The earlier Claude Code vs Codex test: https://tokensave.app/data/claude-code-vs-codex-tokens
