# How many tokens does Blender MCP really use? 72 Claude Code runs, and a racing scene for $0.47

People say hooking Blender up to Claude through MCP eats tokens. I couldn't find a single measurement, so I took the most popular server, MCP for Blender, and ran it 72 times in Claude Code: describing scenes, building furniture, recolouring and checking with screenshots, two worst cases, and one showcase, a racing car with a chase camera. I also ran every task through the small proxy I built for browser MCP, now version 0.3, to see whether it helps here.

## How I measured

- Claude Code 2.1.295, Opus 5.5, effort medium, Windows 11 with a GTX 1650 (2026-10-22)
- Blender 5.2.2 LTS, MCP for Blender via `uvx mcp-for-blender` (add-on 1.8, telemetry off)
- Only the Blender server attached; web, file and shell tools disabled, and the server's 3D-generation and asset-download tools too
- Scenes made by my own script, identical every run: a room with 13 objects, a city block with 580 objects, and an empty scene
- Every run checked afterwards by reading the saved .blend file: the table and four chairs exist, the chairs are really red, the animation is 120 frames, the camera follows the car. 72 of 72 passed.

## Result 1: everyday tasks cost $0.16 to $0.23

| Task (5 runs each) | Input tokens | Cost |
|---|---:|---:|
| Describe a small room | 69,606 | $0.16 |
| Describe a 580-object city block | 115,868 | $0.19 |
| Build a low-poly table and four chairs | 125,563 | $0.23 |
| Make the chairs red, then check with a screenshot | 124,649 | $0.20 |
| Look at the table from four sides | 112,118 | $0.21 |

(Cost at Opus 5.5 API prices, as reported by Claude Code.)

The largest text result in these 25 runs was 2,347 characters. The current MCP for Blender is already careful: scene info lists 20 objects per call by default and screenshots default to 768 pixels. Most of each request (about 25,000 tokens) is Claude Code's own instructions, sent again at every step.

## Result 2: a racing scene cost $0.47

![Six frames from the racing scenes](race_all_6_runs.png)

I asked for a low-poly racing car of its own design, a circuit with a corner, a 5-second animation through the corner and a chase camera. Claude did it in about 10 requests and 93 seconds, for $0.47 on average ($0.42 to $0.56 over 5 runs). All 10 runs, with and without the proxy, produced a working animation. I rendered them afterwards in EEVEE; that took about 90 seconds per clip on the GTX 1650 and is not part of the measured cost.

## Result 3: the one expensive case is a long script output

I asked Claude to print every property of all 580 objects. The script returned 122,373 characters. Claude Code refused it as too large, so Claude ran it again in four chunks of about 32,000 characters each, and all four stayed in the context:

- 242,782 input tokens, $0.87 per task, more than four times an everyday task

Printing all 19,042 vertices of a sphere did not get that far: Claude Code refused it, and Claude reported that the vertices were printed and stopped there: $0.17.

## The proxy: tokensave-mcp-diet 0.3

It sits in front of the server and passes every tool through. For Blender, version 0.3 does two things:

1. **Long text results** (over 8,000 characters) keep their first 2,000 and last 1,000 characters plus a summary of the hidden middle. On the property dump it read: "568 lines (132,418 characters) hidden ... 568 lines like: `name=Building ## | type=MESH | location=(#, #, #) ...`". The full text stays in memory, and a new tool `result_detail` returns any part by line range or search.
2. **Smaller images by default**: tools with a `max_size` get 512 pixels unless the model asks for more than 1,000.

Setup:

```json
{
  "mcpServers": {
    "blender": {
      "command": "npx",
      "args": ["-y", "github:johnisking/tokensave-mcp-diet", "--", "uvx", "mcp-for-blender"]
    }
  }
}
```

| Task | Cost, as shipped | With the proxy | Change |
|---|---:|---:|---:|
| Print every property of 580 objects (3 runs) | $0.873 | $0.166 | −81% |
| Racing scene (5 runs) | $0.471 | $0.445 | −6% |
| Everyday tasks (5 runs each) | $0.16 to $0.23 | $0.15 to $0.21 | −4% to −8% |

To be honest about the rest: the proxy cut image tokens on the racing scene by 62%, but images were a small part of the input, so the scene cost only 6% less, and that is within run-to-run noise. The small-room description, where the proxy changed nothing at all, came out 4% cheaper too. So the everyday differences are noise. The proxy is a safety net for the long-output case, not a discount on every task.

One bug I hit on the way: MCP for Blender also returns each result as `structuredContent`, and Claude Code shows that instead of the text, so my first diet runs of the long-output task were not shortened at all. Version 0.3 now shortens those fields too, and I re-ran those tasks after the fix.

## What to take away

- Blender MCP in Claude Code is not a token hog for normal work. Cost follows the number of steps, and most of each step is Claude Code itself.
- Watch out for scripts that print a lot. One property dump cost more than four normal tasks. Ask for counts, summaries or a file instead of "print everything".
- If you use a client that passes large tool results straight through, the same dump would land in the context in one piece. That is where a proxy like this pays off most.

## Limits

- One model, one machine, one client. 5 runs per task (3 for the two worst cases).
- Costs vary by run because Claude takes a different number of steps each time.
- Image tokens are estimated from image size (width × height / 750); the input totals are exact.
- MCP for Blender changes fast; this is the 2026-10 version.

## Data

- Full data, method and per-run CSV (CC BY 4.0): https://tokensave.app/data/blender-mcp-token-cost
- tokensave-mcp-diet (MIT): https://github.com/johnisking/tokensave-mcp-diet
- The same test for browser MCP: https://tokensave.app/data/browser-mcp-token-cost
