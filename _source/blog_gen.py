#!/usr/bin/env python3
"""Generate the per-language token-study articles from measured data + localized strings.

  blog_data/langdata.json  measured tokens (o200k + cl100k) for one prompt in 27 languages
  blog_data/strings.py     localized sentences (23 languages)
  -> blog_src/<tag>.md     article bodies (then run make_blog.py to render HTML)
  -> blog_data/auto.json   page metadata read by src/blog_meta.py

Run:  python3 _source/blog_gen.py && python3 _source/make_blog.py
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "blog_data"))
sys.path.insert(0, os.path.join(ROOT, "src"))
from strings import T
from i18n import LANGS

D = json.load(open(os.path.join(ROOT, "blog_data", "langdata.json"), encoding="utf-8"))
EN, TOTAL = D["_en"], D["_total"]
NATIVE = {tag: nat for _, tag, nat, *_ in LANGS}
SLUG = {tag: slug for slug, tag, *_ in LANGS}
EN_PATH = "/blog/token-cost-27-languages"
DATE = "2026-10-01"
COMPARE = ["en", "zh-CN", "es", "de", "ko", "ja", "cs"]
ENGLISH_NAME = {v["name"]: k for k, v in D.items() if not k.startswith("_")}


def num(x, dec):
    s = f"{x:.2f}"
    return s.replace(".", ",") if dec == "," else s


def table(tag, dec, head, rows_tags, bold):
    rows = sorted(rows_tags, key=lambda t: D[t]["o"])
    out = [f"| {head[0]} | {head[1]} | {head[2]} | {head[3]} |", "|---|---:|---:|---:|"]
    for t in rows:
        cells = [NATIVE[t], str(D[t]["o"]), num(D[t]["ro"], dec) + "×", num(D[t]["rc"], dec) + "×"]
        if t == bold:
            cells = [f"**{c}**" for c in cells]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def splits_md(tag):
    lines = []
    for s in D[tag]["splits"]:
        parts = " | ".join(p.replace("|", "¦") for p in s["parts"])
        lines.append(f"- {s['w']} → `{parts}` · {len(s['parts'])}")
    return "\n".join(lines)


def article(tag):
    s, d = T[tag], D[tag]
    dec = s["dec"]
    v = dict(L=s["L"], o=d["o"], en=EN, ro=num(d["ro"], dec), rc=num(d["rc"], dec), rank=d["rank"], total=TOTAL,
             cost=d["o"] * 2, encost=EN * 2, enlink=EN_PATH)
    assert num(d["ro"], dec) in s["title"], (tag, "ratio missing from title")
    f = lambda k: s[k].format(**v)
    md = [
        f("intro"), "", s["plabel"], "", "> " + d["prompt"], "",
        "## " + s["h2"], "", table(tag, dec, s["th"], set(COMPARE + [tag]), tag), "",
        f"![{s['h2']}](/blog-language-tax-chart-v2.png)", "",
        "## " + s["h3"], "", s["why"], "", splits_md(tag), "",
        "## " + s["h4"], "", f("old"), "",
        "## " + s["h5"], "", f("cost"), "",
        "## " + s["h6"], "", "\n".join("- " + t for t in s["tips"]), "",
        "## " + s["h7"], "", "\n".join("- " + t for t in s["limits"]), "",
        f("full"), "",
    ]
    return "\n".join(md)


def english():
    rows = sorted((k for k in D if not k.startswith("_")), key=lambda t: D[t]["o"])
    tbl = ["| Language | Tokens | vs English | Old GPT-4 |", "|---|---:|---:|---:|"]
    for t in rows:
        tbl.append(f"| {D[t]['name']} | {D[t]['o']} | {D[t]['ro']:.2f}× | {D[t]['rc']:.2f}× |")
    drops = sorted((t for t in rows if t != "en"), key=lambda t: D[t]["rc"] / D[t]["ro"], reverse=True)[:5]
    reads = [f"[{NATIVE[t]}]({p})" for t, p in PATHS.items() if t != "en"]
    md = f"""I translated one ordinary customer-support prompt into 27 languages and counted tokens with **o200k_base**, the tokenizer behind GPT-4o and every newer OpenAI model (the last column uses cl100k, the GPT-4-era tokenizer). English needs {EN} tokens. The same request costs anywhere from **1.03×** (Simplified Chinese) to **2.00×** (Czech).

The English prompt:

> {D['en']['prompt']}

## All 27 languages

{chr(10).join(tbl)}

![Extra tokens per language vs English](/blog-language-tax-chart-v2.png)

## Why some languages cost more

Tokenizers are trained mostly on English, so common English words are a single token (" polite", " customer"). Words in other languages are split into pieces, and endings or diacritics often become tokens of their own:

- Czech: {D['cs']['splits'][0]['w']} → `{' | '.join(D['cs']['splits'][0]['parts'])}`
- Polish: {D['pl']['splits'][0]['w']} → `{' | '.join(D['pl']['splits'][0]['parts'])}`
- Hindi: {D['hi']['splits'][1]['w']} → `{' | '.join(D['hi']['splits'][1]['parts'])}`

## The old tokenizer was much worse

On the GPT-4-era tokenizer (cl100k), the gap was far larger. The biggest improvements:

{chr(10).join(f"- {D[t]['name']}: {D[t]['rc']:.2f}× → {D[t]['ro']:.2f}×" for t in drops)}

That is why the common advice "Korean costs 2–3× English" is out of date: Korean went from 2.50× to 1.44×.

## What it costs

With a model at $2 per million input tokens, sending this prompt one million times costs ${EN * 2} in English, ${D['ko']['o'] * 2} in Korean, ${D['ja']['o'] * 2} in Japanese and ${D['cs']['o'] * 2} in Czech. If the model also answers in that language, the same multiplier applies to output tokens, which usually cost 4–5× more.

## How to spend fewer tokens

- Write the system prompt and fixed instructions in English; keep only user input in the user's language.
- Ask for intermediate steps (classification, extraction, tool calls) in English or JSON, and only the final answer in the user's language.
- Cache the fixed part of the prompt (prompt caching).

## Limitations

- One prompt only; with other text the ratios move by about ±0.1–0.2.
- Claude and Gemini use different tokenizers, so these numbers apply to OpenAI models.
- Translations started from machine translation and were checked.

## Read it in your language

{' · '.join(reads)}

The original write-up and discussion are on [DEV](https://dev.to/jaehyun_cho_0dff271e0d2e5/i-sent-the-same-prompt-in-27-languages-czech-costs-2x-english-chinese-costs-the-same-420m).
"""
    return md


# Paths of every article (hand-written ones are listed in src/blog_meta.py)
MANUAL = {"cs": "/cs/blog/cestina-tokeny-gpt", "pl": "/pl/blog/polski-tokeny-gpt",
          "ja": "/ja/blog/nihongo-tokens-gpt", "ko": "/ko/blog/korean-tokens-gpt"}
PATHS = {"en": EN_PATH, **MANUAL, **{t: f"/{SLUG[t]}/blog/{T[t]['slug']}" for t in T}}

if __name__ == "__main__":
    out_dir = os.path.join(ROOT, "blog_src")
    meta = [dict(tag="en", path=EN_PATH, date=DATE,
                 title="Same prompt, 27 languages: GPT token cost compared",
                 desc="One prompt measured in 27 languages with GPT's o200k tokenizer: from 1.03× (Chinese) to 2.00× (Czech) the tokens of English.",
                 byline="Jonhisking · Oct 1, 2026",
                 cta="Measure your own text: see how many tokens and dollars your prompt costs, in any language.",
                 ctaBtn="Open the token counter")]
    open(os.path.join(out_dir, "en.md"), "w", encoding="utf-8").write(english())
    for tag in T:
        open(os.path.join(out_dir, tag + ".md"), "w", encoding="utf-8").write(article(tag))
        s = T[tag]
        meta.append(dict(tag=tag, path=PATHS[tag], date=DATE, title=s["title"], desc=s["desc"],
                         byline="Jonhisking · " + DATE, cta=s["cta"], ctaBtn=s["btn"]))
    json.dump(meta, open(os.path.join(ROOT, "blog_data", "auto.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # point the hand-written articles at the on-site overview instead of DEV
    for tag in MANUAL:
        p = os.path.join(out_dir, tag + ".md")
        md = open(p, encoding="utf-8").read()
        md = re.sub(r"\(https://dev\.to/[^)]+\)", f"({EN_PATH})", md)
        md = md.replace("[dev.to](" + EN_PATH, "[" + {"cs": "srovnání 27 jazyků", "pl": "porównanie 27 języków"}.get(tag, "dev.to") + "](" + EN_PATH)
        open(p, "w", encoding="utf-8").write(md)
    print("wrote", len(meta), "generated articles")
