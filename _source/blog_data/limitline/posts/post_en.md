---
title: "I tried to find where Claude Haiku stops being good enough for coding. It took a real bug to find it."
tags: ai, claude, programming, benchmark
---

Most "which model should I use for coding" advice is a guess. I wanted a line: the point where the cheap model (Claude Haiku 5.5) starts failing and you should pay for Sonnet or Opus.

So I ran 136 headless coding runs on one Windows laptop, across five agents, on tasks that get harder level by level, and scored every result with hidden tests.

**Agents:** Claude Code with Haiku 5.5, Sonnet 5.5 and Opus 5.5; Codex with gpt-6-luna; Google's Antigravity CLI with Gemini 4 Argon. All at medium effort, each run in a fresh folder.

## The levels

| Level | Task | Hidden checks |
|---|---|---|
| L2 | Five-level brick game with pause, level skip and saved progress | 9 |
| L3 | Multi-file expense tracker with CSV and summary modules | 12 |
| L4 | Budget app: 5 modules, 3 hash-routed views, budgets, reports, 50-step undo | 23 |
| L5A | An existing 1,032-line app with 6 planted bugs (symptoms only) + 3 new features | 38 |
| L5B | Spreadsheet engine: precedence, functions, cycle detection, $absolute copy, undo | 38 |
| L6 | Three real bugs fixed in the marked Markdown parser in Sep to Oct 2026 | upstream test + full spec suite |

For L6, each run started from the commit before the real fix, got a user-style bug report, and was scored by the test the maintainers added with the fix plus marked's whole spec suite (about 1,900 checks). I copied back only the run's `src/` folder, so editing tests could not help.

## Results: runs with full marks

| Agent | L2 | L3 | L4 | L5A | L5B | L6 easy | L6 medium | L6 hard |
|---|---|---|---|---|---|---|---|---|
| Haiku 5.5 | 5/5 | 5/5 | 5/5 | 4/4 | 2/2 | 2/2 | 2/2 | 0/2 |
| Sonnet 5.5 | 5/5 | 5/5 | 5/5 | 4/4 | 2/2 | 2/2 | 2/2 | 0/2 |
| Opus 5.5 | 5/5 | 5/5 | 5/5 | 4/4 | 2/2 | 2/2 | 2/2 | 0/2 |
| Codex | 5/5 | 4/5 | 4/5 | 3/4 | 1/1 | 2/2 | 1/2 | 0/2 |
| Gemini 4 Argon | 5/5 | 5/5 | 5/5 | 2/2 | 1/1 | 3/4 | 4/4 | 0/3 |

**With a clear spec, Haiku never failed.** It built the spreadsheet engine with cycle detection, and in L5A it fixed all six bugs from symptoms alone, added the features and kept all 23 old tests passing.

**The line showed up on a real bug.** The hard L6 bug: a code span ending in a backslash, like `` `C:\Users\` ``, stopped `**bold**` later on the line from working. Every agent fixed the examples in the bug report. None passed the upstream test, which has 7 cases:

- Opus and Sonnet: 6 of 7 in every run (they missed the double-backtick case)
- Haiku: 5 of 7, and one run broke 15 other spec tests
- Codex and Gemini: 3 of 7, the same as the unfixed code (one Codex run named the right cause, said "I'll fix the masking order", and ended without editing)

So the difference between models was one or two edge cases the bug report did not mention, not whether they could do the job.

## Cost

Claude Code reports an API-price cost for every run. Average per run:

| | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|
| All levels | $0.027 | $0.20 | $0.44 |
| L6 easy bug | $0.005 | $0.081 | $0.20 |

Haiku cost about 94% less per run than Opus and got the same number of full-mark runs. Haiku and Sonnet fixed the easy and medium real bugs in 14 to 20 seconds.

## A note on Antigravity

Antigravity's headless mode ends the whole turn the first time a command is denied. With read-only allow-rules, several Gemini runs read the code for minutes and then stopped on a `node -e` check before editing (on Windows a quoted command needs an exact rule). With full permissions, Gemini solved the easy and medium bugs too, in 2 to 11 minutes; one hard run hit its 30-minute limit without an edit.

## Limitations

- Few runs per cell at the higher levels (1 to 5), and L6 is three bugs from one project.
- L2 to L5 prompts list every id and function name the tests use, which is easier than real work.
- The tools differ in more than the model (Codex can run commands in a sandbox; Claude Code in acceptEdits mode cannot).
- No agent could install packages, so none could run marked's tests while fixing it.

Data (136 runs, scores, time, tokens and cost per run, CC BY 4.0): https://tokensave.app/data/ai-coding-limit-line

Disclosure: I run TokenSave, which publishes these measurements. No funding or credits from Anthropic, OpenAI or Google.
