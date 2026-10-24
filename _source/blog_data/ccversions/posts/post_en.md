# What Claude Code sends before you type: 58 versions measured, from July 2025 to this week

Every Claude Code request starts with the same fixed block: the system prompt and the definitions of every built-in tool. You pay for it before your own words are counted, and it is a big reason why short sessions and subagents burn through limits faster than you'd expect. I wanted to know how that block has changed over time, so I installed old versions and measured it.

## How I measured

- 58 Claude Code versions installed from npm, one folder each, from 1.0.60 (July 2025) to 2.1.310 (October 23, 2026)
- Each one got the one-letter prompt "a" with `claude -p`, model Claude Haiku 5.5, an empty folder and a fresh config folder (no CLAUDE.md, plugins or settings)
- I recorded the input tokens of the first model request: uncached + cache read + cache write
- MCP off, 3 runs per version. A second pass with my 13 claude.ai connectors left on, 1 run per version
- One Windows laptop. Earlier versions measured on October 21, the 12 newest on October 24 with the same script and login

## Result

| Version | Released | Tokens before you type |
|---|---|---:|
| 1.0.60 | 2025-07-24 | 19,498 |
| 2.0.0 | 2025-09-29 | 19,420 |
| 2.1.0 | 2026-01-07 | 23,957 |
| 2.1.100 | 2026-04-10 | 33,305 |
| 2.1.150 (peak) | 2026-05-23 | 36,309 |
| 2.1.250 | 2026-08-27 | 28,451 |
| 2.1.292 | 2026-10-06 | 29,701 |
| 2.1.293 | 2026-10-07 | 18,055 |
| 2.1.301 | 2026-10-15 | 18,171 |
| 2.1.307 | 2026-10-21 | 18,697 |
| 2.1.310 | 2026-10-23 | 18,841 |

Three things stand out:

1. **Ten months of growth.** From 19,498 to 36,309 tokens (+86%) between July 2025 and May 2026, while built-in tools went from 15 to 27.
2. **One release cut it by 39%.** Version 2.1.293 on October 7 dropped from 29,701 to 18,055 tokens with the same number of tools. That puts it back where it was in mid-2025.
3. **Since then it has been creeping back up.** Over the 15 releases after 2.1.293 it rose to 18,841 (+4%), in steps of 100 to 400 tokens. 2.1.310 added a 25th built-in tool (Monitor).

Every run of the same version gave exactly the same number, so these are not noisy averages.

## The connector surprise

Apps you connect on claude.ai also show up in Claude Code. In versions 2.1.83 to 2.1.140 (late March to mid May 2026), all of their tools were sent with every request. With my 13 connected apps, that was 420 to 426 extra tools and about 395,000 tokens for the prompt "a". Since 2.1.145 they are loaded only when needed, and in every version I measured this month the number is the same with connectors on or off.

## What this means in practice

- After the first request, this block is usually read from the prompt cache at a tenth of the input price or less. It costs the most in short sessions, in subagents (each starts with its own copy), and after the cache expires.
- If your Claude Code is old, updating is the cheapest token saving you can make.
- Your own number will be higher: CLAUDE.md files, MCP servers, plugins and skills all add to it.

## Limits

- One model (Haiku 5.5), one prompt, one Windows machine. Other models and operating systems can get a different system prompt, so absolute numbers will differ; the trend is the point.
- Old versions were run against today's API and account, so features the server switches on per account may change what an old version sends.
- Versions before 1.0.60 would not install on Windows.

## Data

- Full table, per-version CSV, scripts and raw logs (CC BY 4.0, DOI 10.5281/zenodo.23527278): https://tokensave.app/data/claude-code-baseline-tokens-by-version
- Related: what the rest of the harness costs (subagents +128%, minimal setup −64%): https://tokensave.app/data/claude-code-harness-cost
