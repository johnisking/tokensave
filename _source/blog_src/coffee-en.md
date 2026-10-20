![Claude Code Cache Lasts 1 Hour: What a Break Costs (Measured)](/claude-code-cache-break-cost-en.jpg)

You work in Claude Code all morning, go to lunch, come back and send one more message. The first reply is slow, and your usage bar jumps more than a one-line request should cost. The usual explanation is the prompt cache: Claude Code keeps your conversation in Anthropic's cache for a while, and once that cache expires, the next message has to process the whole conversation again.

What nobody quite agrees on is how long "a while" is. Some guides say five minutes, others say an hour. In April 2026 a user analysis claiming the cache lifetime had dropped from one hour to five minutes set off a wave of complaints, and Anthropic replied that the main conversation uses a one-hour cache. Plenty of posts say an expired cache makes things far more expensive, but we couldn't find anyone who had simply waited and measured it.

So we did. We had Claude Code build the same small game, waited anywhere from 0 to 65 minutes, then sent the same small change request and recorded how much of the next message was read from the cache, how much had to be written again, and what it cost. Measured on October 20, 2026 with Claude Code 2.1.295 and Claude Opus 5.5.

## How we measured

Claude Code ran in headless mode (`-p`), signed in with a Claude subscription, on Opus 5.5 at medium effort with no MCP servers. Turn 1 asked for a brick-breaker game in a single `index.html`, playable with keyboard and mouse. After the pause, turn 2 resumed the same session (`--resume`) with a small edit: "Make the ball red and slightly faster."

We tested seven pauses: 0, 4, 6, 15, 30, 55 and 65 minutes. With a five-minute cache, the cost should jump between 4 and 6 minutes. With a one-hour cache, it should jump between 55 and 65. Each pause got its own session, all started within a minute of each other, and the whole experiment ran twice. Token counts come from the per-call usage in Claude Code's stream-json log; cost is the API list-price estimate Claude Code reports (`total_cost_usd`).

## Results: nothing changes for 55 minutes, then +507%

![Results: nothing changes for 55 minutes, then +507%: Pause, Read from cache, Written to cache, Cost of the next message, Cache](/claude-code-cache-break-cost-results-nothing-changes-for-55-minutes-t-en.jpg)

Cache reads and writes on the first model call after the pause, and the cost of that whole message. Mean of two runs.

| Pause | Read from cache | Written to cache | Cost of the next message | Cache |
|---|---:|---:|---:|---|
| 0 min | 41,436 | 496 | $0.039 | still cached |
| 4 min | 43,232 | 466 | $0.042 | still cached |
| 6 min | 42,440 | 496 | $0.042 | still cached |
| 15 min | 43,076 | 502 | $0.041 | still cached |
| 30 min | 42,636 | 494 | $0.043 | still cached |
| 55 min | 43,183 | 502 | $0.043 | still cached |
| 65 min | 15,925 | 27,460 | **$0.253** | expired |

**Up to 55 minutes, nothing changed.** Whether we waited 0 minutes or 55, the first call read about 43,000 tokens from the cache and wrote only a few hundred new ones. The message cost $0.042 on average.

**At 65 minutes the cache was gone.** The first call had to write 27,460 tokens to the cache again, and the same message cost $0.253, 507% more. Both runs agreed. The 6- and 15-minute pauses, which would have missed a five-minute cache, cost nothing extra.

## Why one hour

![Why one hour: How you sign in, Main conversation, Subagents, compaction and other requests](/claude-code-cache-break-cost-why-one-hour-en.jpg)

Every cache write in these runs was labelled `ephemeral_1h` in the usage report: a one-hour cache. The Anthropic API's default is five minutes, but Claude Code asks for an hour in some situations. According to Claude Code's documentation, the defaults are:

| How you sign in | Main conversation | Subagents, compaction and other requests |
|---|---|---|
| Claude subscription, within included usage | 1 hour | 5 minutes |
| Claude subscription, drawing on usage credits | 5 minutes | 5 minutes |
| API key or cloud provider | 5 minutes | 5 minutes |

Note the second row: once you pass your plan's included usage and start paying with usage credits, the main conversation drops to five minutes too, which the docs say is because five-minute cache writes are cheaper. During the April controversy, Anthropic also said it picks the cache lifetime per request and uses one hour for the main conversation (as reported by Byline Network).

The longer cache isn't free. On Opus 5.5:

| Token type | Price per million | vs normal input |
|---|---:|---:|
| Normal input | $4 | – |
| Cache write, 5 minutes | $5 | +25% |
| Cache write, 1 hour | $8 | +100% |
| Cache read | $0.20 | -95% |

A one-hour write costs more up front, but then every read for the next hour is 95% cheaper than normal input. If you tend to stop and think, test or review between messages, that beats a five-minute cache.

## How much an expired cache costs on a bigger session

Our test conversation was small, about 40,000 tokens. What you pay after an expiry grows with the size of the conversation, because all of it has to be written to the cache again. Here is the cost of re-reading versus re-writing the whole conversation at Opus 5.5 prices (output and any new file reads not included):

| Conversation size | Cache still warm (read) | Cache expired (write again) |
|---|---:|---:|
| 40,000 tokens | $0.008 | $0.32 |
| 100,000 tokens | $0.02 | $0.80 |
| 200,000 tokens | $0.04 | $1.60 |

In a separate long-chat test on the same day, 30 change requests in one session pushed the conversation past 200,000 tokens. Leave a session like that for more than an hour and your first message back carries about $1.60 of cache writes before it does anything else. For a small session, an expiry costs cents and isn't worth worrying about.

## What you can do before a long break

![What you can do before a long break: Under an hour, do nothing. On a subscription, pauses up to 55 minutes cost nothing extra.; Long break, same ta](/claude-code-cache-break-cost-what-you-can-do-before-a-long-break-en.jpg)

You can't make lunch shorter, but you can prepare for it. We only measured pause lengths; the effects below come from Claude Code's documentation, not from our tests.

- **Under an hour, do nothing.** On a subscription, pauses up to 55 minutes cost nothing extra.
- **Long break, same task afterwards: run `/compact` before you leave.** The docs explain that `/compact` reads the conversation from the cache while it is warm, so summarizing is cheap then, and expensive after an expiry. The summary is also much smaller to re-cache when you return.
- **Long break, different task afterwards: `/clear`.** The docs say `/clear` costs nothing when you want a fresh start. You can also ask Claude to write a short handoff note to a file first and have the new session read it.
- **Check the cache when you come back.** From v2.1.251, `/usage` shows a "Prompt cache (main)" line with your hit rate and whether the cache is warm or cold, plus the TTL. Cold means your next message rewrites the whole conversation.
- **Idle compaction may do it for you.** The docs say that if you leave a long conversation idle in a terminal session on the one-hour TTL, Claude Code can compact it shortly before the cache expires (the `idleCompaction` setting, v2.1.290+). Our runs used headless mode, so this did not apply.

## Choosing the cache lifetime yourself

Since v2.1.242 you can set the cache lifetime. Use the `promptCacheTtl` setting or the `CLAUDE_CODE_PROMPT_CACHE_TTL` environment variable for the main conversation, and `subagentPromptCacheTtl` for everything else. Each accepts `5m` or `1h` only.

If you use Claude Code with an API key and often leave more than five minutes between messages, setting `promptCacheTtl` to `1h` is worth considering. If you work in short bursts and finish, the cheaper five-minute writes are the better deal. To see which lifetime your cache writes use right now:

```
claude -p "hello" --output-format json
```

In `usage.cache_creation`, tokens under `ephemeral_1h_input_tokens` mean a one-hour cache; tokens under `ephemeral_5m_input_tokens` mean five minutes.

## The long-chat test from the same day

We also sent 30 change requests to the same game three ways. One long session cost $4.16 on average; adding a `/compact` after request 15 cost 13% more; a fresh session for every request cost 129% more. Fresh sessions were expensive for the same reason as the 65-minute pause: each one had to build its cache from scratch. The numbers are in our [long chat vs new chat dataset](/data/long-chat-vs-new-chat-cost).

To see what your own sessions actually cost by day and project, drop your `~/.claude/projects` folder into the [Claude Code usage analyzer](/claude-code-usage). To compare a subscription with API pricing for your workload, try the [coding agent cost calculator](/agents).

## Limitations

- **One small project.** The conversation was about 40,000 tokens. The bigger-session costs above are calculated from list prices, not measured.
- **Sessions ran at the same time.** All seven sessions started within a minute of each other, so part of the shared prefix may have stayed cached through the others. Even after 65 minutes, 15,925 tokens were still read from the cache. A lone session may pay a little more.
- **Subscription login and Opus 5.5 only.** With an API key or usage credits the cache lasts five minutes and the picture changes completely. We also started Codex runs, but they stalled on file writes when many ran in parallel, so they are left out.
- **Costs are API list-price estimates.** On a subscription you are not billed these amounts; the same difference shows up in how fast you reach your usage limit.

## FAQ

**How long does the Claude Code prompt cache last?**
On a Claude subscription within your included usage, the main conversation's cache lasts one hour. In our test it survived 55 minutes and was gone at 65. With an API key, a cloud provider, or while drawing on usage credits, the default is five minutes.

**Is it one hour from my last message?**
The docs say each request that hits the cache resets the timer. As long as you keep working, the cache stays warm; it expires after an hour with no requests.

**Does running /compact before a break save money?**
According to the docs, compacting while the cache is warm is cheap and leaves only a short summary to re-cache. We didn't measure this case. In our same-day test, a `/compact` in the middle of active work with no break cost 13% more, so it pays to use it for a reason, like an upcoming long break.

**I'm on a subscription. Does cache expiry matter?**
You won't get a bill for it, but it uses more of your usage limit. In our small game, one message went from $0.042 worth of usage to $0.253, and the gap grows with the size of the session.

**Do subagents get the one-hour cache?**
No. Per the docs, subagents, compaction and other requests outside the main conversation default to five minutes even on a subscription. You can change that with `subagentPromptCacheTtl`.

## Bottom line

With Claude Code on a subscription, pausing the same conversation for anywhere from 0 to 55 minutes left the next message's cost unchanged at about $0.042. After 65 minutes the cache had expired and the same message cost $0.253, 507% more. The usage log confirmed a one-hour cache.

Breaks under an hour are free. For longer ones on a big session, shrink it with `/compact` before you leave or start fresh with `/clear` when you return. These are two runs on one small project, so your numbers will vary with conversation size and Claude Code version. The raw logs and CSV are free to use under CC BY 4.0 in our [coffee-break cache dataset](/data/ai-coffee-break-cache-cost).

## Sources

- [Claude Code docs: How Claude Code uses prompt caching (cache lifetime, promptCacheTtl, /compact, idleCompaction)](https://code.claude.com/docs/en/prompt-caching)
- [Claude Code docs: Manage costs effectively (/usage cache line, /clear)](https://code.claude.com/docs/en/costs)
- [Anthropic docs: Prompt caching (cache write and read pricing)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [Anthropic API pricing (Opus 5.5)](https://platform.claude.com/docs/en/about-claude/pricing)
- [Byline Network: Claude Code token drain report, April 14, 2026 (Korean)](https://byline.network/2026/04/14-555/)
- [TokenSave: Coffee-break cache dataset (CSV, CC BY 4.0)](/data/ai-coffee-break-cache-cost)
<!-- autoimg -->
