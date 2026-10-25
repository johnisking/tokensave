![Claude Haiku vs Opus for Coding: 330 Measured Runs](/claude-haiku-vs-opus-en.jpg)

Claude Haiku vs Opus for coding is a choice every Claude Code user makes many times a day. On the API, Haiku 5.5 costs 2.5% of what Opus 5.5 does per input token ($0.10 against $4 per million, for prompts up to 100K tokens), but the usual advice is that the cheap model makes more mistakes. Most comparisons repeat the vendor's benchmark scores, which say little about your own repository.

So I measured it. On October 23 and 24, 2026, on one Windows laptop, I made 330 Claude Code runs with Haiku 5.5, Sonnet 5.5 and Opus 5.5: 63 runs building apps from a spec, 42 runs on real bugs in the marked Markdown parser, and 225 runs on 25 real bugs fixed in open-source projects between August and October 2026, three runs per bug and model. Every run was scored by tests the model could not see, and for real bugs by the tests the maintainers added with their fix.

This post puts the two studies together to answer one question: which coding jobs is Haiku enough for, and when is Opus worth paying for?

## How I measured

![How I measured: Task, What it was, Runs per model, Scored by](/claude-haiku-vs-opus-how-i-measured-en.jpg)

Every run used the same setup:

- Claude Code 2.1.295 in headless mode (`-p`), effort medium.
- A fresh folder for every run. Package installs and the network were blocked.
- Cost is Claude Code's own per-run figure at API prices; the runs were made on a subscription.

There were two kinds of task:

| Task | What it was | Runs per model | Scored by |
|---|---|---:|---|
| Build from a spec | A brick game, a multi-file expense tracker, a 5-module app, a 1,032-line app with 6 planted bugs plus 3 features, a spreadsheet engine | 21 | 9 to 38 hidden checks |
| Fix a real bug | 25 bugs from 13 projects (js-yaml, marked, zod, cachetools, Python-Markdown and others) | 75 | The maintainers' tests for the fix |

For real bugs, each run started from the commit before the fix and got the user's bug report with the cause analysis and suggested fix removed, so only the symptom was left. When scoring, I kept only the run's changes to the library source. Editing the tests could not help.

## Result 1: with a clear spec, Haiku scored full marks

![Result 1: with a clear spec, Haiku scored full marks: Model, Full marks, build from a spec, Average cost per run](/claude-haiku-vs-opus-result-1-with-a-clear-spec-haiku-scored-en.jpg)

| Model | Full marks, build from a spec | Average cost per run |
|---|---:|---:|
| Haiku 5.5 | 21/21 | $0.026 |
| Sonnet 5.5 | 21/21 | $0.19 |
| Opus 5.5 | 21/21 | $0.45 |

When the requirements were clear, Haiku never failed. It built a spreadsheet engine with cycle detection. In someone else's 1,032-line app it found and fixed six bugs from their symptoms alone, added three features and kept all 23 earlier tests passing. Each run cost about 94% less than an Opus run.

## Result 2: on 25 real bugs, almost the same

A "clean fix" means every maintainer test case for the fix passes and no other test breaks.

| Model | Clean fixes, 15 easier bugs | Clean fixes, 10 harder bugs | All | Cost per run |
|---|---:|---:|---:|---:|
| Haiku 5.5 | 40/45 | 12/30 | 52/75 | $0.019 |
| Sonnet 5.5 | 35/45 | 14/30 | 49/75 | $0.14 |
| Opus 5.5 | 38/45 | 16/30 | 54/75 | $0.38 |

Haiku and Opus fixed almost the same number of bugs cleanly, 52 and 54 of 75 runs, and Haiku cost about 95% less. On 22 of the 25 bugs the two models had exactly the same number of clean fixes. All 75 Haiku runs together cost $1.41; the 75 Opus runs cost $28.53.

The easier bugs had the cause close to the symptom: PapaParse crashing on an empty cell, humanize showing one significant figure too many. The harder bugs came with a symptom-only report, and the cause was often in another file or spread over several places.

## Where Opus won: bugs that touch several places

On the harder bugs Opus was ahead, mostly because it broke other tests less often.

| 10 harder bugs | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
|---|---:|---:|---:|
| Clean fixes | 12/30 | 14/30 | 16/30 |
| Runs that broke other tests | 10 | 7 | 5 |
| Test cases passed | 72% | 69% | 82% |

The bugs where it showed:

- **marked, a link inside link text:** Opus fixed it cleanly in 2 of 3 runs, Haiku in none. Every Haiku run broke the spec test for that exact example.
- **markdown-it, an unclosed link label hiding a later code span:** Opus 3 of 3, Haiku 1 of 3. Two Haiku runs fixed the bug but broke two neighbouring tests.
- **zod, numeric record keys in JSON Schema output:** the fix needed changes in several places and no run got all of it, but over three runs Opus passed 14 of 24 cases, Haiku 9 and Sonnet 5.

It went the other way too. On a js-yaml bug with a whitespace-only block scalar, Haiku fixed it cleanly in all 3 runs, Opus in 1 and Sonnet in none.

## What no model did: the case the report left out

![What no model did: the case the report left out: cachetools; js-yaml; Python-Markdown](/claude-haiku-vs-opus-what-no-model-did-the-case-the-report-le-en.jpg)

The most useful result was not a difference between models. It was the place where all three got stuck the same way.

- **cachetools:** the report showed one way of calling a cached method through its class. The maintainers also tested every other variant of the decorator. No run handled them.
- **js-yaml:** the report was about a BOM at the start of a file. The maintainers also tested a BOM before each document in a multi-document stream. No run handled it.
- **Python-Markdown:** every run fixed the reported HTML comment and broke 3 to 5 of the maintainers' tests for comments after other inline HTML.

In my earlier study of one hard marked bug, Sonnet and Opus found the missing edge case far more often than Haiku (8 and 6 of 10 runs against 1 of 10). Across 25 bugs that pattern did not hold. Paying for a bigger model did not buy the case the report left out.

## Is the difference real?

Treat the numbers with care: there were three runs per bug and model.

- Haiku vs Opus on clean fixes: Fisher's exact test p = 0.86, well within chance.
- Resampling whole bugs, the 95% interval for Haiku minus Opus is −11 to +5 percentage points. There is no evidence that Opus fixes more bugs, but a gap of around 10 points cannot be ruled out.
- On the harder bugs alone the interval is −33 to 0 points, so Opus may really be better on bugs like these.

The honest summary is not "Haiku equals Opus" but "25 bugs showed no evidence that Opus fixes more". I will keep adding bugs with the same method.

## Switching models in Claude Code

In Claude Code you can switch during a session with `/model haiku`, `/model sonnet` or `/model opus`, or start with `claude --model haiku`. The `opusplan` alias uses Opus in plan mode and Sonnet for execution. A practical setup is Haiku as the default and Opus only when you see one of these signs. Every case where Haiku fell behind in this data looked like one of them.

- **The fix spans several files or functions:** like the zod bug, where changing one place means changing others to match.
- **Haiku's fix broke an existing test:** like marked and markdown-it, where the fix looked right but broke the behaviour next to it. On the harder bugs this happened in 10 of 30 Haiku runs.
- **A large codebase where breakage is expensive:** once you count review time, not breaking things is cheaper than the roughly 36 cents a run you save.

And since no model found the edge cases the report left out, adding those examples to your request yourself works better than switching models.

To see what your own usage would cost per month on the API or a plan, put your task size and tasks per day into the [coding agent cost calculator](/agents).

## FAQ

**Is Claude Haiku good enough for coding?**
For tasks with clear requirements and bugs whose cause sits near the symptom, yes. In these runs Haiku scored full marks on all 21 spec tasks and fixed 40 of 45 easier bugs cleanly.

**When should I use Opus instead?**
For bugs that need changes in several files or places, and in large codebases where breaking existing tests is costly. On the harder bugs, 5 Opus runs broke other tests against 10 Haiku runs.

**What about Sonnet?**
On these bugs Sonnet did not beat Haiku, and it passed a smaller share of test cases than Opus (paired permutation test p = 0.006). For Sonnet against Opus on a build task, see [Claude Sonnet vs Opus 5.5 for coding](/blog/claude-sonnet-5-5-vs-opus-5-5).

**Does letting Haiku run the tests help?**
Every bug run here could run the project's tests. No model found the cases the report left out anyway.

## Conclusion: default to Haiku, pick Opus on purpose

- **For clear specs and bugs with the cause near the symptom, Haiku is enough.** Same results as Opus at about 95% less cost.
- **For bugs that touch several places, Opus is the safer pick.** It broke other tests in half as many runs.
- **No model finds what the bug report leaves out.** On the harder bugs, 47% to 60% of each model's runs were not clean fixes. Whatever model you use, a human still has to check the edge cases.

All raw data (per-run scores, failing tests, time and cost) is public under CC BY 4.0: [25 real bugs dataset](/data/claude-haiku-vs-opus-real-bugs) and [spec tasks and marked bug dataset](/data/ai-coding-limit-line).

## Sources

- [Claude pricing (Anthropic, checked October 25, 2026)](https://claude.com/pricing)
- [Claude Code model configuration docs](https://code.claude.com/docs/en/model-config)
- [Dataset: 25 real bugs, 225 runs (DOI 10.5281/zenodo.23619927)](https://doi.org/10.5281/zenodo.23619927)
- [Dataset: six levels of coding tasks, 163 runs (DOI 10.5281/zenodo.23600477)](https://doi.org/10.5281/zenodo.23600477)
<!-- autoimg -->
