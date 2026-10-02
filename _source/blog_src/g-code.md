Coding assistants and agents send a lot of code to AI models: whole files, test output, stack traces, diffs. How many tokens does code actually use, and do things like indentation, comments or minified files make a difference? We measured real snippets on GPT's o200k tokenizer. Some results are surprising.

## Indentation is almost free

We took a 16-line Python file with two functions and wrote it three ways: with 4-space indentation, 2-space indentation, and tabs.

| Version | Tokens | Characters |
|---|---|---|
| 4 spaces | 135 | 485 |
| 2 spaces | 135 | 455 |
| Tabs | 133 | 440 |

Changing indentation saved at most two tokens. Modern tokenizers have single tokens for runs of spaces, so eight spaces of indentation cost about the same as four. Reformatting code to save tokens is not worth the trouble.

## Comments and docstrings do cost

Removing the one-line docstring from the same file took it from 135 to 123 tokens, a 9% saving. Comments are written in natural language, so they cost about the same per word as prose.

That does not mean you should strip comments before asking a model for help. Comments often explain intent, which helps the model give a better answer. But large blocks of commented-out code, license headers repeated at the top of every file, and auto-generated documentation are worth removing.

## Minified code is half the tokens, and much harder to read

A 10-line JavaScript function took 92 tokens. The same function minified, with short variable names and no whitespace, took 47: 49% fewer.

That sounds like a great saving, but minified code throws away exactly what helps a model understand it: meaningful names like `subtotal` and `taxRate`. If you need the model to reason about the code, send the readable version. Minified bundles in a prompt are almost always a mistake: they are long, unreadable and rarely relevant to the question.

## Where coding tokens really go

In practice, indentation and comments are small. These are the big costs:

- **Whole files when one function matters.** A 1,000-line file is often around 10,000 tokens. If the question is about one function, send that function and the types it uses.
- **Full logs and stack traces.** Test runners and build tools print hundreds of lines. The first error and its stack trace usually carry all the information.
- **Lock files and generated files.** `package-lock.json`, build output, snapshots and vendored libraries are huge and almost never useful in a prompt.
- **Re-sending unchanged context.** Agents re-send their working context on every step. Ten steps over the same 20,000 tokens of files is 200,000 input tokens, unless the tool uses prompt caching.
- **Rewriting whole files.** Asking the model to return a full file after a two-line change pays output prices for every unchanged line. Ask for a diff or only the changed function.

## Code vs prose

In our sample, Python averaged about 3.6 characters per token and the JavaScript 3.5. Ordinary English prose is usually around 4 characters per token. Code is slightly denser in tokens because of symbols, operators and identifiers split into pieces: `calculate_total` is several tokens, while a common English word is usually one.

## A practical checklist

1. Send the smallest piece of code that answers the question, plus the types and signatures it depends on.
2. Trim logs to the first error and its stack trace.
3. Exclude lock files, build output and minified bundles from anything your tools send automatically.
4. Ask for diffs or changed functions, not whole files.
5. Keep readable names and useful comments. They cost little and improve answers.
6. Use a coding tool that supports prompt caching. See [Prompt caching explained](/blog/prompt-caching-explained).

## Measure your own code

Paste a file into the [token counter](/) to see its token count and what it costs to send on each model, and use the [coding agent calculator](/agents) to estimate a month of agent use.
