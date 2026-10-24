# How many tokens does browser MCP really cost? 68 runs of Playwright MCP and Chrome DevTools MCP, and a proxy I built to cut them

You often hear that hooking a browser MCP server up to Claude Code burns tokens, and some posts put it at 10,000 to 50,000 tokens every time the agent looks at a page. I wanted to know whether that holds up, and whether it can be reduced, so I measured the two most popular servers: Microsoft's Playwright MCP and Google's Chrome DevTools MCP. Along the way I ended up building a small tool to cut the cost, so the results for that are here too.

## How I measured

- Claude Code 2.1.295, Opus 5.5, effort medium, Windows 11 (2026-10-22)
- Exactly one MCP server per run; web search, web fetch, file tools and shell were disabled, so only the browser tools could be used
- Playwright MCP 0.0.83 and Chrome DevTools MCP 1.11.0, both headless
- 7 tasks: 2 runs each for everyday tasks, 5 runs each for snapshot tasks (3 for the full-snapshot probe), 68 runs in total
- Tokens come from the per-request usage in Claude Code's log (all input: uncached, cache read and cache write)

## Result 1: everyday tasks were lighter than expected

| Task | Playwright input tokens | Cost | Chrome DevTools input tokens | Cost |
|---|---:|---:|---:|---:|
| TodoMVC: add 3 items, complete 1 | 178,408 | $0.19 | 199,737 | $0.22 |
| Wikipedia: who designed Python, first year | 115,888 | $0.17 | 117,240 | $0.17 |
| Hacker News: top 5 stories | 90,006 | $0.16 | 93,496 | $0.17 |
| Wikipedia table: 5 release dates | 91,350 | $0.16 | 93,683 | $0.16 |

(Average of 2 runs, cost at Opus 5.5 API prices.)

All 16 runs got the right answer, and the largest single tool result was 6,012 characters. Opus 5.5 did not read whole pages. It ran short scripts that pulled out just what it needed, or used Playwright's find tool.

So where did the tokens go? Each request carried about 23,000 tokens, and most of that was Claude Code's own instructions and tool definitions, not the browser. Browser work takes many small steps, and that fixed amount is sent again with every step. The to-do task was the most expensive not because the page was big but because it took the most clicks and keystrokes.

## Result 2: reading a long page in one go is over 200,000 tokens

Then I forced the worst case: open the English Wikipedia article "Python (programming language)" and take one accessibility snapshot of the whole page.

- Playwright MCP: 504,168 characters
- Chrome DevTools MCP: 427,400 characters

I sent that text to Opus 5.5 to count it: **205,642 and 208,926 tokens**. That is about $1.65 for one snapshot at Opus list price. OpenAI's o200k tokenizer counts 133,668 and 138,745, so the same text comes out more than 50% bigger on Claude. Text full of link targets and element ids is especially expensive for Claude's tokenizer.

The good news: Claude Code already stops this. Every time, it refused the result as too large, saved it to a file and told the model to read it in pieces. So 200,000 tokens never landed in the context in Claude Code. A client without that guard could take the whole page in one go. I only measured Claude Code, so I can't say which other clients do that.

## Result 3: medium pages get straight through

Pages Claude Code does not block are the real issue. The Hacker News front page snapshot came straight in and grew the next request by:

- Playwright MCP: 18,407 tokens
- Chrome DevTools MCP: 14,115 tokens

Most of that is noise: a URL line under every link, "clickable" markers, empty layout cells, "|" separators and deep indentation.

## So I built a proxy: tokensave-mcp-diet

It sits in front of Playwright MCP or Chrome DevTools MCP and does three things:

1. **Compact:** if a snapshot is large, strip link targets, cursor markers, separators and empty wrappers, and shrink the indentation. Element refs stay, so clicking and typing work as before.
2. **Outline:** if it is still too big, send only headings, form fields, buttons and links, with long runs of links (like Wikipedia's references) collapsed.
3. **Read on demand:** keep the full snapshot in memory and add a `snapshot_detail` tool that returns any part of it by ref or by text.

Setup is one change in your MCP config. No npm account or API key:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "github:johnisking/tokensave-mcp-diet", "--", "npx", "-y", "@playwright/mcp@latest"]
    }
  }
}
```

Same tasks, with and without it:

| Task | Server | Snapshot tokens, as shipped | With the diet | Task cost |
|---|---|---:|---:|---:|
| Hacker News top 5 | Playwright | 18,407 | 6,792 (−63%) | $0.298 → $0.205 (−31%) |
| Hacker News top 5 | Chrome DevTools | 14,115 | 8,066 (−43%) | $0.271 → $0.224 (−18%) |
| Wikipedia facts | Playwright | refused in 3 of 5 runs | 9,193 | $0.181 → $0.236 (+30%) |
| Wikipedia facts | Chrome DevTools | refused every time | 8,479 | $0.230 → $0.237 (+3%) |
| Wikipedia full snapshot | Playwright | about 205,600 (refused by Claude Code) | 9,193 (−96%) | $0.154 → $0.222 (+44%) |
| Wikipedia full snapshot | Chrome DevTools | about 208,900 (refused by Claude Code) | 8,479 (−96%) | $0.160 → $0.221 (+38%) |

(Cost is the average of 5 runs, 3 for the full snapshot. On Hacker News the 5 runs were within one cent of each other, and snapshot tokens varied by at most 4% between runs.)

On Hacker News, snapshot tokens fell 43% to 63% and the task cost 18% to 31% less, with the same answer in all 5 runs.

To be honest about Wikipedia: inside Claude Code the proxy lost money. Where Claude Code would have sent a short refusal note, the proxy sent a 9,000-token outline, and the task cost 3% to 44% more. In a client that passes large results through, the same outline turns 200,000 tokens into 9,000, a 96% cut. The tool pays off on medium-size pages, and in clients that don't have Claude Code's guard.

> **Update (same day): version 0.2 fixes the Wikipedia loss.** Pages over 60,000 characters now get only a table of contents (headings with their refs, about 1,100 tokens), and a heading ref returns that whole section. Re-measured with 5 runs each: finding facts on the Wikipedia article now costs $0.181 → $0.173 (−4%) on Playwright and $0.230 → $0.178 (−23%) on Chrome DevTools, a bare full snapshot costs about the same as Claude Code's own refusal (+2% and +3%), and Hacker News stays at −30% and −17%. The full Wikipedia snapshot goes from about 205,600 Claude tokens to about 1,140 (−99%). The install command above now gets 0.2.

## What to take away

- In Claude Code, most of the browser-MCP bill is the number of steps, not the pages. Saying clearly what you want, so the agent finishes in fewer steps, helps most.
- The expensive request is "read the whole page". Ask for a specific element, a search or a short script instead.
- If your client passes large tool results straight through, put a proxy like tokensave-mcp-diet in front, or have the model save snapshots to a file: Chrome DevTools MCP's `take_snapshot` and `evaluate_script` take a `filePath` parameter (in 3 of my 5 full-snapshot runs, Opus used it without being asked).

## Limits

- 2 runs per everyday task, 5 per snapshot task (3 for the full snapshot), one model, one machine. Hacker News is live, so points changed between runs.
- Only Claude Code was measured. I did not check whether Claude Desktop, Cursor or Codex pass a 200,000-token result through.
- Snapshot formats change between server versions. Playwright MCP already saves the snapshot to a file on navigation.
- The outline drops body text, so the model has to ask for details, which can add steps.

## Conclusion

Browser MCP does not burn huge numbers of tokens on every step. Opus 5.5 mostly read only what it needed, and the cost was driven by Claude Code's fixed per-request block and the number of steps. But one full read of a long page is over 200,000 tokens, and medium pages get through even in Claude Code. tokensave-mcp-diet is a free tool for those two cases.

- Full data (CSV, CC BY 4.0): https://tokensave.app/data/browser-mcp-token-cost
- tokensave-mcp-diet (MIT): https://github.com/johnisking/tokensave-mcp-diet
- Count the tokens in your own prompt: https://tokensave.app/
