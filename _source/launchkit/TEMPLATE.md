# New-model launch kit (tokensave.app)

Goal: a pricing + real-cost article live within a few hours of a model announcement,
before the big sites. Proven format: `blog_src/gpt61-en.md` (GPT-6.1 Sol).

## 1. Collect (official sources only, keep the links)
- [ ] Official announcement / blog post URL
- [ ] Official pricing page: input, cached input, output per 1M tokens, long-context surcharge
- [ ] Context window, max output, API model name
- [ ] Plan availability (Free / Plus / Pro / Max …) and any new usage limits
- [ ] Benchmark claims — only quote the company's own numbers, and say they are the company's
- [ ] Tokenizer: public? If yes, measure 41 languages (our own data). If not, reuse the family's ratio and say so.

## 2. Calculate
```
cd _source/launchkit
python3 newmodel.py --name "<Model>" --in <$> --out <$> --cached <$> --ratio <r> \
    --prev <previous-model-id> --vs <id1>,<id2>,<id3>
```
Model ids are the `id:` values in `src/token.js`. Paste the output tables into the article.

## 3. Article skeleton (English first)

Title: `<Model> API Pricing: Cost vs <previous>, <rival 1> and <rival 2>`

Intro (3–4 sentences): who released it, when, list price, what changed, what this article covers.

## <Model> API pricing
<table from newmodel.py> + long-context rule, context window, API model name.

## What it costs on real work
<task table from newmodel.py> + 2 bullets explaining the biggest difference (with %).

## <Model> vs <rivals>
<per-request comparison> + one paragraph on tokenizer differences.
Quality: "According to <company>, …" — never our own claims.

## What changed vs <previous>
3 bullets from the official announcement.

## Should you switch?
One bullet per audience: on the previous model / on a rival for cost / on a bigger model / on a cheaper model.

## Check your own prompt
Links: the provider's token counter page, /compare pages, related blog posts.

*Prices checked <date>. Check <company>'s pricing page before you commit.*

## 4. Ship
- [ ] Add the model to `src/token.js` (price + ratio) and `src/llm_prices.json`
- [ ] Add compare pages if relevant (`src/compare.py`)
- [ ] Add the article to `src/blog_meta.py`; translate ko / ja at minimum
- [ ] Show the manuscript to 재현 and wait for "올려" before publishing
- [ ] Build, push, request indexing in Search Console (article first)
- [ ] X @tokensaveapp (English): 1 table image + 1 line + link
- [ ] Reddit answer in r/ClaudeAI / r/ChatGPTPro / r/OpenAI threads about the launch (answer, then link)
- [ ] Record every place it was posted in memory

## Rules
- Percentages, never multipliers ("30% more", not "1.3x").
- No made-up numbers. Every price links to the official page.
- No performance claims we did not measure.
