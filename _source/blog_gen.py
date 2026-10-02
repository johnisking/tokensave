#!/usr/bin/env python3
"""Generate the per-language token-study articles from measured data + localized strings.

  blog_data/langdata.json  measured tokens (o200k + cl100k) for one prompt in every site language
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
import i18n_guides as GI

D = json.load(open(os.path.join(ROOT, "blog_data", "langdata.json"), encoding="utf-8"))
EN, TOTAL = D["_en"], D["_total"]
NATIVE = {tag: nat for _, tag, nat, *_ in LANGS}
SLUG = {tag: slug for slug, tag, *_ in LANGS}
EN_PATH = "/blog/token-cost-by-language"
DATE = "2026-10-02"
COMPARE = ["en", "zh-CN", "es", "de", "ko", "hi", "ja", "cs", "el", "pa"]
ENGLISH_NAME = {v["name"]: k for k, v in D.items() if not k.startswith("_")}


def num(x, dec):
    s = f"{x:.2f}"
    return s.replace(".", ",") if dec == "," else s


def saving(t):
    return round((1 - 1 / D[t]["ro"]) * 100)


def table(tag, dec, head, rows_tags, bold):
    rows = sorted(rows_tags, key=lambda t: D[t]["o"])
    out = [f"| {head[0]} | {head[1]} | {head[2]} | {head[3]} |", "|---|---:|---:|---:|"]
    for t in rows:
        cells = [NATIVE[t], str(D[t]["o"]), num(D[t]["ro"], dec) + "×", ("–" if t == "en" else f"{saving(t)}%")]
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
        "## " + s["h2"], "", table(tag, dec, list(s["th"][:3]) + [GI.strings(tag)["th3"]], set(COMPARE + [tag]), tag), "",
        f"![{s['h2']}](/blog-language-tax-chart-v4.png)", "",
        "## " + s["h3"], "", s["why"], "", splits_md(tag), "",
        "## " + GI.strings(tag)["feat_h"], "", GI.fill(tag, "feat" if GI.CTX[tag]["supported"] else "featx"), "",
        "## " + s["h5"], "", f("cost"), "",
        "## " + s["h6"], "", "\n".join("- " + t for t in s["tips"]), "",
        "## " + s["h7"], "", "\n".join("- " + t for t in s["limits"]), "",
        f("full"), "",
    ]
    return "\n".join(md)


def english():
    rows = sorted((k for k in D if not k.startswith("_")), key=lambda t: D[t]["o"])
    tbl = ["| Language | Tokens | vs English | Saved if sent in English |", "|---|---:|---:|---:|"]
    for t in rows:
        tbl.append(f"| {D[t]['name']} | {D[t]['o']} | {D[t]['ro']:.2f}× | {'–' if t == 'en' else str(saving(t)) + '%'} |")
    drops = sorted((t for t in rows if t != "en"), key=lambda t: D[t]["rc"] / D[t]["ro"], reverse=True)[:5]
    reads = [f"[{NATIVE[t]}]({p})" for t, p in PATHS.items() if t != "en"]
    top = rows[-1]
    md = f"""I translated one ordinary customer-support prompt into {TOTAL} languages and counted tokens with **o200k_base**, the tokenizer behind GPT-4o and every newer OpenAI model English needs {EN} tokens. The same request costs anywhere from **1.03×** (Simplified Chinese) to **{D[top]['ro']:.2f}×** ({D[top]['name']}).

The English prompt:

> {D['en']['prompt']}

## All {TOTAL} languages

{chr(10).join(tbl)}

![Extra tokens per language vs English](/blog-language-tax-chart-v4.png)

## Why some languages cost more

Tokenizers are trained mostly on English, so common English words are a single token (" polite", " customer"). Words in other languages are split into pieces, and endings or diacritics often become tokens of their own:

- Czech: {D['cs']['splits'][0]['w']} → `{' | '.join(D['cs']['splits'][0]['parts'])}`
- Polish: {D['pl']['splits'][0]['w']} → `{' | '.join(D['pl']['splits'][0]['parts'])}`
- Hindi: {D['hi']['splits'][1]['w']} → `{' | '.join(D['hi']['splits'][1]['parts'])}`

## Send it in English and save

Current models understand English instructions perfectly well and answer in your language if you ask, so the simplest saving is to send the prompt in English: about 31% fewer tokens for Korean, 44% for Japanese and 50% for Czech. In the [token counter](/), paste a prompt and press **💸 Save tokens**: it cleans up spaces, translates to English with the translator built into desktop Chrome 138+ / Edge 148+ (on your device; nothing is uploaded), trims filler and adds a line asking for the reply in your language. How the gap has changed over time is covered in [How GPT's new tokenizer cut costs in 40 languages](/blog/gpt-tokenizer-cl100k-vs-o200k).

## What it costs

With a model at $2 per million input tokens, sending this prompt one million times costs ${EN * 2} in English, ${D['ko']['o'] * 2} in Korean, ${D['ja']['o'] * 2} in Japanese and ${D['cs']['o'] * 2} in Czech. If the model also answers in that language, the same multiplier applies to output tokens, which usually cost 4–5× more.

## How to spend fewer tokens

- Send the prompt in English and ask for the answer in your language (the Save tokens button does this in one click).
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
                 title=f"Same prompt, {TOTAL} languages: GPT token cost compared",
                 desc=f"One prompt in {TOTAL} languages on GPT's o200k tokenizer: from 1.03× (Chinese) to {max(v['ro'] for k, v in D.items() if not k.startswith('_')):.2f}× the tokens of English.",
                 byline="Jonhisking · Oct 1, 2026 (updated Oct 2)",
                 cta="Measure your own text: see how many tokens and dollars your prompt costs, in any language.",
                 ctaBtn="Open the token counter")]
    open(os.path.join(out_dir, "en.md"), "w", encoding="utf-8").write(english())
    for tag in T:
        open(os.path.join(out_dir, tag + ".md"), "w", encoding="utf-8").write(article(tag))
        s = T[tag]
        desc = GI.fill(tag, "desc").replace("**", "")
        assert len(desc) <= 160, (tag, len(desc), desc)
        meta.append(dict(tag=tag, path=PATHS[tag], date=DATE, title=s["title"], desc=desc,
                         byline="Jonhisking · " + DATE, cta=s["cta"], ctaBtn=s["btn"]))
    json.dump(meta, open(os.path.join(ROOT, "blog_data", "auto.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # point the hand-written articles at the on-site overview instead of DEV
    for tag in MANUAL:
        p = os.path.join(out_dir, tag + ".md")
        md = open(p, encoding="utf-8").read()
        md = re.sub(r"\(https://dev\.to/[^)]+\)", f"({EN_PATH})", md)
        md = md.replace("[dev.to](" + EN_PATH, "[" + {"cs": "srovnání 41 jazyků", "pl": "porównanie 41 języków"}.get(tag, "dev.to") + "](" + EN_PATH)
        open(p, "w", encoding="utf-8").write(md)
    print("wrote", len(meta), "generated articles")
