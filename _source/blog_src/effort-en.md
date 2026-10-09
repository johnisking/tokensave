![Claude Opus 5.5 Effort Levels Tested: Low to Max](/claude-opus-5-5-effort-en.jpg)

Claude **Opus 5.5** has an **effort** setting that controls how deeply it thinks, with five levels: low, medium, high, xhigh and max. Higher levels are supposed to give better results, but the official docs give no numbers for how much extra time and money each level costs. So on October 9, 2026 we ran the same game-building request once at each level and compared time, tokens, cost and the result. The fastest level took 32 seconds and the slowest took 22 minutes. Here is what changed at each level and which level to use for which task, along with hands-on experience.

## What effort is

- **It sets how much the model thinks.** Thinking can't be turned off on Opus 5.5; effort controls how deep it goes. Thinking tokens are billed as output tokens.
- **The default is medium.** Opus 5 defaulted to high; Opus 5.5 defaults to one level lower, medium (per Anthropic's docs).
- **How to change it:** in Claude Code use the `--effort` option (low to max); in the API set the `effort` value.

## How we measured

- **Model:** Claude Opus 5.5 in Claude Code on a Windows PC
- **Prompt (verbatim):** "Make a brick-breaker game that runs in the browser as a single file named index.html in the current folder. It needs 2 levels, a score display and 3 lives, and it must be playable with the keyboard and the mouse. Write the file and finish."
- **Method:** the same prompt five times, changing only effort. Each level ran in its own folder so runs could not affect each other.
- **Measurement:** tokens and cost with the free tool ccusage, time from start and end timestamps. Cost is converted at API prices.

## Results: time, tokens and cost

![Results: time, tokens and cost: Effort, Time, Output tokens, Total tokens, Cost, Game code](/claude-opus-5-5-effort-results-time-tokens-and-cost-en.jpg)

| Effort | Time | Output tokens | Total tokens | Cost | Game code |
|---|---:|---:|---:|---:|---:|
| low | 32 s | 3,368 | 129,315 | $0.48 | 138 lines |
| medium (default) | 52 s | 6,299 | 133,428 | $0.56 | 358 lines |
| high | 1 min 50 s | 12,376 | 222,854 | $0.75 | 523 lines |
| xhigh | 4 min 32 s | 32,435 | 472,082 | $1.36 | 639 lines |
| max | 22 min 22 s | 160,033 | 2,504,957 | $5.25 | 1,121 lines |

- **Low and medium are almost the same.** Low cost 14% less and took 38% less time, but that is 8 cents.
- **High cost only 34% more than medium.** Time went from 52 seconds to 1 minute 50 seconds.
- **xhigh is where costs jump.** It cost 143% more than medium and took 4 minutes 32 seconds.
- **Max is in a league of its own.** Medium took 52 seconds and $0.56; max took 22 minutes 22 seconds and $5.25. Output tokens went from 6,299 to 160,033.

![Time and cost by effort level: from low at 32 s and $0.48 to max at 22 min 22 s and $5.25](/claude-opus-5-5-effort-en-6.jpg)

![ccusage measurement record: tokens and cost for the five Opus 5.5 effort levels](/claude-opus-5-5-effort-en-7.jpg)

## The five games side by side

![The five brick-breaker games built at each Opus 5.5 effort level, side by side](/claude-opus-5-5-effort-en-5.jpg)

All five games ran without errors and met the request: 2 levels, score, 3 lives, keyboard and mouse controls. The differences are in what each level added on top.

| Effort | What it added |
|---|---|
| low | Single-color bricks, the plainest screen, no pause |
| medium | Rainbow bricks, pause, restart |
| high | + particle effects, saved best score |
| xhigh | Particle effects, more polished design (no saved best score) |
| max | + sound effects, level names, an invader-shaped level 2, screen shake, victory fireworks |

- **From high up, the model tried to check its own work.** High and xhigh tried a code syntax check, and max tried an automated play test. All three needed permission to run, so none actually ran; each says it re-read the code instead. Low and medium finished without checking.
- **Bricks that take two hits** appeared at every level even though we did not ask for them.

## Level-by-level review

We played each game and checked it against the summary the model left at the end and the code itself.

### low: 32 seconds, $0.48

![Start screen and gameplay of the game built at effort low](/claude-opus-5-5-effort-en-11.jpg)

- **What it built:** level 1 is four rows of blue bricks; level 2 mixes orange bricks that take two hits with gaps, and the ball is faster. It has level-clear, game-over and win screens and a restart.
- **Good:** every requested feature is there, and where the ball hits the paddle changes its angle. Done in 32 seconds.
- **Weak:** black background and single-color bricks make it the plainest. No pause, and at 138 lines the shortest code.
- **Use it when:** you just need to check that something works and will polish it later.

### medium: 52 seconds, $0.56 (default)

![Start screen and gameplay of the game built at effort medium](/claude-opus-5-5-effort-en-12.jpg)

- **What it built:** level 1 is a 5×10 rainbow grid; level 2 has gaps and bricks that take 2 or 3 hits, showing hits left and fading as they take damage.
- **Good:** pause (P or Esc), restart (Enter) and auto-pause when the window loses focus. Scoring depends on brick strength and level.
- **Weak:** no sound or particle effects.
- **Use it when:** most of the time. It costs 8 cents more than low and is a clear step up.

### high: 1 minute 50 seconds, $0.75

![Start screen and gameplay of the game built at effort high](/claude-opus-5-5-effort-en-13.jpg)

- **What it built:** level 2 is a diamond pattern of bricks that take 2 or 3 hits, and bricks throw particles when they break.
- **Good:** a level-clear bonus, a bonus for lives left, a saved best score and touch controls. It also tried a syntax check on its own code.
- **Weak:** it took 112% longer than medium (52 seconds to 1 minute 50 seconds).
- **Use it when:** you need a prototype to show people or coding where quality matters. It cost only 34% more than medium.

### xhigh: 4 minutes 32 seconds, $1.36

![Start screen and gameplay of the game built at effort xhigh](/claude-opus-5-5-effort-en-14.jpg)

- **What it built:** level 2 is a diamond ringed with steel bricks that crack after the first hit. Bricks are worth 10 to 50 points by color.
- **Good:** the tidiest-looking screen, and mixing mouse and keyboard works smoothly: whichever you used last moves the paddle.
- **Weak:** it dropped the saved best score and touch controls that high had. It cost 143% more than medium without adding features over high.
- **Use it when:** not for small tasks like this. Per Anthropic, it suits long-running work.

### max: 22 minutes 22 seconds, $5.25

![Start screen and gameplay of the game built at effort max](/claude-opus-5-5-effort-en-15.jpg)

- **What it built:** named levels ("Rainbow Wall", "Space Invader"), an invader-shaped level 2 whose 14 silver bricks take two hits, and a narrower paddle on level 2.
- **Good:** sound effects (M to toggle), saved best score, touch controls, screen shake, victory fireworks and auto-pause: the most of any level. It looks like a finished game.
- **Weak:** by far the slowest, partly because it tried to run an automated play test that needed permission.
- **Use it when:** quality matters most and you have time and limits to spare, or nothing else solves the problem.

## Hands-on: medium day to day, high for coding

I (Jaehyun) use Opus 5.5 on the Claude Max 20x plan to build games. This is how it feels in daily use, not a measurement.

- **My setting:** I leave effort on auto. It usually runs at medium and goes up to high when I'm coding.
- **low:** it felt sluggish, so I used it a few times and stopped.
- **high:** the results are clearly better.
- **xhigh and max:** I tried them about once and rarely have a reason to use them.

Compared with the measurements, low was actually the fastest but gave the plainest result, so the sluggish feeling was about the output rather than speed. The sense that high gives better results, and that xhigh and max are rarely needed, matched the numbers.

## What Anthropic recommends

- **Medium is strong.** In Anthropic's testing, Opus 5.5 at medium matched or beat Opus 5 at high on coding and knowledge work.
- **Low comes close to medium on coding,** at much lower cost, according to Anthropic. In our test the difference in output was noticeable.
- **Reserve xhigh and max for work where you've measured a quality gain.**
- **Changing effort mid-conversation can break the prompt cache.** In the API, use a per-message effort change to keep the cache.
- **Independent testing agrees.** Artificial Analysis found Opus 5.5 at max effort used 63% more output tokens per task than Opus 5 (per press reports).

## Which effort for which task

![Which effort for which task: Task, Recommended effort, Why](/claude-opus-5-5-effort-which-effort-for-which-task-en.jpg)

Our recommendations, combining the measurements, Jaehyun's experience and Anthropic's guidance:

| Task | Recommended effort | Why |
|---|---|---|
| Simple edits, renaming, tidying files | low or medium | Fast and cheap, but low's output is plain |
| Everyday coding and new features | medium (default) | Usable results in 52 seconds for $0.56 |
| Game or app prototypes, coding where quality matters | high | 34% more cost for clearly better output |
| Runs over 30 minutes, big refactors | xhigh | Per Anthropic's guidance |
| Hard problems nothing else solves | max | Only when needed: time and cost jump |

- **Start at medium.** Move only the tasks where the result falls short up to high.
- **On a plan, think in limits.** The higher the API-equivalent cost, the faster your Max or Pro limit drains. One max run used more than nine medium runs.
- **Caveat:** one run per level on a fairly small task. Bigger projects may show different gaps.

## Conclusion: medium by default, high when it matters

- **Default: medium.** Usable results in 52 seconds for $0.56.
- **When quality matters: high.** Only 34% more than medium for clearly better output. The best value of the five.
- **xhigh: skip it for small tasks.** 143% more than medium but no more features than high. Worth it only for long runs.
- **max: only when you need it.** The flashiest result, but 22 minutes and $5.25.
- **low: not recommended.** Saving 8 cents over medium just gets you a plainer result.

## FAQ

**What is Opus 5.5's default effort?**
Medium. Opus 5 defaulted to high. API requests that don't set effort run at medium on Opus 5.5.

**Is max always better?**
In our test it added the most features and polish, but took 22 minutes and $5.25 versus 52 seconds and $0.56 for medium. Too much for simple work.

**Does low save a lot?**
In our test low was only 14% cheaper than medium. Given the plainer result, medium is the better choice.

## Calculate it for your own work

In the [coding agent cost calculator](/agents), enter task size and tasks per day to see a month on Opus 5.5. Check a single prompt's cost in the [token counter](/). For price and performance differences between Opus 5 and 5.5, see [Claude Opus 5 vs 5.5](/blog/claude-opus-5-vs-5-5).

*Measured October 9, 2026. Cost is ccusage's conversion at API prices; results may change with model and Claude Code updates.*

## Sources

- [Anthropic: Effort](https://platform.claude.com/docs/en/build-with-claude/effort#recommended-effort-levels-for-claude-opus-5-5)
- [Anthropic: Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- [Anthropic: Migrating from Claude Opus 5 to Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)
- [OfficeChai: Artificial Analysis Intelligence Index report](https://officechai.com/ai/claude-opus-5-5-creates-5-point-lead-over-gpt-6-astra-jumps-to-top-spot-on-artificial-analysis-intelligence-index/)
- [ccusage: Claude Code usage tool (GitHub)](https://github.com/ryoppippi/ccusage)
<!-- autoimg -->
