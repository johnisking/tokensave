![Context Windows Explained: Why Long Chats Get Worse and Cost More](/context-window-explained-en.jpg)

Have you noticed that a long chat with an AI assistant starts to go wrong? It forgets a detail you gave it an hour ago, mixes up two topics, or repeats a mistake you already corrected. That is not your imagination. It is how context windows work, and the same mechanism is why long conversations cost more on the API.

## What a context window is

![What a context window is: Model, Context window](/context-window-explained-what-a-context-window-is-en.jpg)

A model's **context window** is the maximum amount of text, measured in tokens, it can consider at once. It includes everything: the system instructions, every earlier message in the chat, any files you attached, and the answer it is writing.

Current models have very large windows:

| Model | Context window |
|---|---|
| Claude Opus 5.5 / Sonnet 5.5 | 1,000,000 tokens |
| Gemini 3.1 Pro | about 1,050,000 tokens |
| GPT-6 Sol | 922,000 tokens |
| Claude Haiku 4.5 | 200,000 tokens |
| GPT-4o | 128,000 tokens |

A million tokens is roughly 750,000 English words. So why do long chats still go wrong?

## The model re-reads the whole chat every time

A chat model has no memory between messages. To answer your 30th message, the app sends all 29 earlier messages back to the model together with the new one. The model reads the whole conversation from the top, every single time.

That has two consequences.

**Cost grows faster than the chat.** On the API, message 30 is billed for the tokens of messages 1 to 30. The total cost of a conversation grows roughly with the square of its length: a chat 100% longer costs about 300% more.

**Quality drops in the middle.** Research on long contexts, starting with the 2023 paper *Lost in the Middle* by Liu and colleagues, found that models use information at the beginning and the end of their input much better than information buried in the middle. Newer models are better at this, but a fact from 40 messages ago, surrounded by unrelated topics, is still easy to miss.

## Fitting is not the same as using

A window of a million tokens means the text fits. It does not mean the model gives every part equal attention. Mixed topics make it worse: if one chat covers a trip plan, a Python bug and an email to your boss, the model has to work out which earlier parts still matter for your new question.

## What to do instead

![What to do instead: One topic, one chat. When the subject changes, start a new conversation.; Carry a summary, not the history. Be](/context-window-explained-what-to-do-instead-en.jpg)

1. **One topic, one chat.** When the subject changes, start a new conversation.
2. **Carry a summary, not the history.** Before leaving a long chat, ask: *"Summarize what we decided in 5 lines."* Paste that summary into a fresh chat and continue from there.
3. **Put important instructions at the start or the end.** Not in the middle of a long paste.
4. **Attach only what is relevant.** A 3-page excerpt beats a 300-page manual when you need one answer from it.
5. **On the API, trim old turns.** Keep the last few messages in full and replace older ones with a running summary.

## See it in numbers

The [token counter](/) shows how much of each model's context window your text fills, and the [Subscription vs API calculator](/plans) includes the cost of re-sending chat history in its monthly estimate.

## Sources

- [Claude Opus 5.5 overview (Claude docs)](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- [Claude Haiku 4.5 overview (Claude docs)](https://platform.claude.com/docs/en/models/haiku-4-5/overview)
- [Gemini 3.1 Pro Preview model page (Google)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview)
- [GPT-6 Sol model page (OpenAI)](https://developers.openai.com/api/docs/models/gpt-6-sol)
- [GPT-4o model page (OpenAI)](https://developers.openai.com/api/docs/models/gpt-4o)
- [Liu et al., Lost in the Middle (arXiv, 2023)](https://arxiv.org/abs/2307.03172)
<!-- autoimg -->
