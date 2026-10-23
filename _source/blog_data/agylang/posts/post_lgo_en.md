# Same code, about 60% more output tokens on Claude: 80 runs across Claude Code, Codex and Antigravity in 5 languages

Yesterday I compared Google's new Antigravity CLI with Claude Code and Codex. One number kept bothering me: Claude Opus 5.5 wrote shorter games than Gemini but did not use proportionally fewer output tokens. So I divided output tokens by the size of the file each run wrote, across four tool and model pairs and five prompt languages.

## How I measured

- The same brick-breaker task ("a single index.html with 2 levels, a score and 3 lives, keyboard and mouse"), prompted in English, Korean, Japanese, Spanish and Ukrainian
- Claude Code 2.1.295 + Opus 5.5 and Codex CLI 0.162 + gpt-6-luna: 5 runs per language (from my earlier prompt-language test, same versions)
- Antigravity CLI 1.4.5 with Gemini 4 Argon and with Claude Opus 5.5: 3 runs per language (24 new runs today plus yesterday's English runs)
- Medium effort everywhere, Windows 11, every run in an empty folder
- Every game played by a script in a headless browser: score, level 2, lives 3 to 0

## Result: output tokens per 1,000 characters of code

| Tool + model | EN | KO | JA | ES | UK | Average |
|---|---:|---:|---:|---:|---:|---:|
| Claude Code + Opus 5.5 | 554 | 624 | 581 | 614 | 584 | 591 |
| Antigravity + Opus 5.5 | 574 | 590 | 606 | 612 | 597 | 596 |
| Antigravity + Gemini 4 Argon | 367 | 380 | 370 | 364 | 378 | 372 |
| Codex + gpt-6-luna | 367 | 386 | 385 | 366 | 376 | 376 |

Opus needed about 60% more output tokens per character than Gemini, and about 57% more than GPT. The interesting part is that Opus came out almost the same in two very different tools (591 and 596). That points at the model's tokenizer, not the tool around it. The language of the prompt barely mattered.

Output tokens are the expensive ones. On the API, Opus 5.5 charges five times more for output than for input, so this gap goes straight into the bill, on top of any difference in how much code each model decides to write.

This also fits an earlier test of mine, where the same source code in 10 programming languages needed 43% to 59% more Claude tokens than GPT tokens.

## Prompt language: almost no effect on input

| Input tokens | EN | KO | JA | ES | UK |
|---|---:|---:|---:|---:|---:|
| Claude Code + Opus 5.5 | 96,462* | 78,638 | 79,266 | 79,030 | 79,787 |
| Codex + gpt-6-luna | 51,674 | 48,538 | 48,660 | 48,201 | 48,816 |
| Antigravity + Gemini 4 Argon | 13,041 | 13,289 | 12,408 | 12,629 | 13,447 |
| Antigravity + Opus 5.5 | 9,822 | 11,316 | 9,983 | 9,945 | 10,958 |

*Two of the five English Claude Code runs took an extra step.

The prompt is a few dozen tokens; the rest of every request is the tool's own instructions. Which tool you use decides the input size, not which language you write in.

One more detail: in Antigravity, Opus wrote longer games for Korean and Ukrainian prompts (about 31% and 20% more characters than in English), so its total output rose there. Per character it stayed the same.

## Did the games work?

79 of 80 did, and every game showed its text in the prompt language. The one failure is a Ukrainian Codex game from the earlier test.

## Limits

- One task: a browser game in HTML, CSS and JavaScript. Other code may tokenize differently
- Output tokens include the short final reply and the tool-call wrapping, not only the code
- 3 to 5 runs per cell, measured between 2026-10-18 and 10-23 with the same tool versions

## Data

- Full data, per-run CSV and method (CC BY 4.0): https://tokensave.app/data/output-tokens-per-character-by-model
- Yesterday's three-way comparison: https://tokensave.app/data/antigravity-cli-vs-claude-code-vs-codex
