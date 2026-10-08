![Write Shorter Prompts Without Losing Quality: Measured Before and After](/write-shorter-prompts-en.jpg)

Polite, chatty prompts feel natural, but every extra word is billed, and in an app the same system prompt is sent thousands of times a day. We rewrote two typical prompts to say the same thing in fewer words and measured them on GPT's o200k tokenizer. Both shrank by roughly 70–80%, without losing anything the model needs.

## Example 1: a one-off request

**Before (98 tokens):**

> Hello! I hope you're doing well today. I was wondering if you could possibly help me out with something. I have a customer email here that I need to deal with, and I would really appreciate it if you could take a look at it and summarize the main points for me. If it's not too much trouble, could you also please suggest a polite and professional reply that I could send back to the customer? Thank you so much in advance for your help, I really appreciate it!

**After (20 tokens):**

> Summarize this customer email in 3 bullet points, then draft a polite, professional reply.

That is 80% fewer tokens, and the short version is actually *more* specific: it says how many bullet points and in what order to do things.

For a single request in a chat app, 78 tokens hardly matters. Where it matters is in prompts that repeat.

## Example 2: a system prompt sent with every request

**Before (122 tokens):**

> You are a helpful, friendly, and knowledgeable customer support assistant working for an online electronics store. Your job is to help customers with their questions. You should always be polite and professional. You should always try to be as helpful as possible. Please make sure that your answers are accurate. Please do not make things up. If you do not know the answer to a question, you should say that you do not know rather than guessing. You should keep your answers reasonably short and to the point, but you should also make sure that they are complete. Please always answer in the same language that the customer used.

**After (35 tokens):**

> You are customer support for an online electronics store.
> - Be polite, accurate and brief.
> - If unsure, say so; never guess.
> - Reply in the customer's language.

The rewrite keeps every instruction and saves 87 tokens per request.

At one million requests a month, that is 87 million fewer input tokens. At $2 per million (GPT-6 Sol), about **$174 a month** saved from four lines of editing. With a larger model or longer system prompts, the savings scale up accordingly.

## What to cut

**Greetings and thanks.** Models do not need "Hello", "I hope you're well" or "Thank you so much". They do not change the answer.

**Hedging.** "I was wondering if you could possibly..." becomes "Please..." or just the verb.

**Repetition.** "Be helpful", "be as helpful as possible" and "make sure your answers are complete" say the same thing three times.

**Instructions the model already follows.** Current models are polite and try to be accurate by default. Instructions like "be helpful" add tokens without changing behavior. Keep instructions that change what the model would otherwise do.

**Filler words.** "Basically", "actually", "just", "really", "in order to" (use "to").

## What to keep, or add

![What to keep, or add: Specific constraints; Context the model cannot guess; Examples, when the output must follow an exact pattern. ](/write-shorter-prompts-what-to-keep-or-add-en.jpg)

Shorter is not always better. These are worth their tokens:

- **Specific constraints:** length, format, number of items, audience, reading level.
- **Context the model cannot guess:** who the user is, what the product does, what has already been tried.
- **Examples,** when the output must follow an exact pattern. One good example often replaces a paragraph of description.
- **What to do when unsure.** A clear fallback ("say you don't know") prevents made-up answers.

The goal is not the fewest possible tokens. It is no tokens that do not change the answer.

## Lists beat paragraphs

The rewritten system prompt uses short bullet points. That style is cheaper and also easier to maintain: you can see each rule, check whether it is still needed, and add one without rewriting a paragraph.

## Before you ship a shorter prompt

Test it. Run the old and new prompts on the same 20–50 real inputs and compare the answers. A shorter prompt that occasionally drops an important behavior is not a saving. Usually, though, the tighter prompt gives the same or better results, because the instructions that matter are no longer buried.

## Measure your prompts

Paste a prompt into the [token counter](/) to see its token count and cost per request on 30+ models. The *Save tokens* button also cleans up extra spaces and filler, and can translate non-English prompts to English on your device.
<!-- autoimg -->
