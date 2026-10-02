Reasoning models think before they answer. They work through a problem step by step in hidden text, then write a final response. That makes them much better at maths, multi-step coding and planning. It also makes them more expensive in a way that is easy to miss, because most of the thinking is invisible but still billed.

## Where the cost hides

A normal model writes its answer and you pay for those output tokens. A reasoning model first writes **reasoning tokens**: its internal working. You usually see only a short summary, or nothing, but every reasoning token is billed **at the output price**, the most expensive kind of token.

A simple example on a model priced at $10 per million output tokens:

| | Output tokens | Cost |
|---|---|---|
| Direct answer | 300 | $0.003 |
| Same answer after 3,000 reasoning tokens | 3,300 | $0.033 |

The visible answer is identical in length. The bill is 11 times higher.

How much a model reasons varies a lot by question. A simple question may use a few hundred reasoning tokens; a hard maths or coding problem can use tens of thousands.

## Effort settings

Many APIs let you control how much a model thinks, usually with a setting such as low, medium or high effort, or a maximum thinking budget in tokens. Lower effort means fewer reasoning tokens, lower cost and faster answers. For many tasks, low effort gives the same result as high.

If your provider offers it, start low and raise effort only where you can measure an improvement.

## When reasoning is worth paying for

- **Maths and calculations with several steps.**
- **Debugging and non-trivial code changes**, where the model has to trace logic across functions.
- **Planning**, such as breaking a project into steps or scheduling under constraints.
- **Analysis with competing factors**, such as comparing options against several criteria.
- **Problems where a wrong answer is expensive** and a few extra cents to get it right is a bargain.

## When it is usually wasted

- **Extraction:** pulling names, dates or fields out of text.
- **Classification:** sorting messages into categories, sentiment, spam or not.
- **Rewriting and summarizing:** changing tone, shortening, translating.
- **Simple lookups and formatting:** turning a list into JSON, fixing grammar.
- **Chat small talk** and short factual answers.

These tasks rarely improve with more thinking. A fast, non-reasoning model at low cost is usually just as accurate.

## Other side effects

**Speed.** Reasoning takes time. Users may wait several seconds or longer before the first word appears.

**Output limits.** Reasoning tokens count toward the maximum output length. If you set a low limit, the model can run out of room while still thinking and return a short or empty answer.

**Context use.** In long conversations, some APIs keep or summarize earlier reasoning, which adds to the input of later turns.

## A practical approach

1. **Default to a fast model.** Use it for most requests.
2. **Route hard requests to a reasoning model.** Decide by task type, or let a cheap model judge difficulty first.
3. **Set the lowest effort that works.** Measure on real examples rather than assuming high is better.
4. **Watch the reasoning token count** in your API responses. If it is large for simple tasks, lower the effort or switch models.
5. **Set an output limit with headroom** for reasoning, so answers are not cut off.

## Estimate the difference

Paste a typical prompt and answer into the [token counter](/) and set the expected output length several times higher than the visible answer to see what reasoning adds to each request. For coding work, the [agent cost calculator](/agents) shows monthly totals.
