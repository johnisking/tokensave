#!/usr/bin/env python3
"""New-model launch calculator for tokensave.app.

Reads every model and price from src/token.js, adds the new model you pass in,
and prints ready-to-paste markdown tables for the launch article (TEMPLATE.md).

Example:
  python3 newmodel.py --name "GPT-6.2 Sol" --in 2 --out 10 --cached 0.1 --ratio 1.0 \
      --prev gpt-6-1-sol --vs claude-sonnet-5-5,claude-opus-5-5,gemini-3-1-pro
Prices are USD per 1M tokens. --ratio is tokens per GPT-o200k token for the same
English text (Claude 1.30, Gemini 0.95, most others 1.00; use 1.00 if unknown).
"""
import argparse, re, pathlib

SRC = pathlib.Path(__file__).resolve().parent.parent / "src" / "token.js"
CACHE_DEFAULT = 0.10  # cached input = 10% of input when the provider gives no number

def load_models():
    js = SRC.read_text(encoding="utf-8")
    pat = re.compile(r"\{\s*id:\s*'([^']+)'[^}]*?name:\s*'([^']+)'[^}]*?in:\s*([\d.]+),\s*out:\s*([\d.]+)(?:,\s*ratio:\s*([\d.]+))?")
    return {m[0]: dict(id=m[0], name=m[1], i=float(m[2]), o=float(m[3]), r=float(m[4] or 1), c=None) for m in pat.findall(js)}

# Scenarios: (label, fresh input, cached input, output, repeats)
SCEN = [
    ("Typical request (2,000 in / 500 out)", 2000, 0, 500, 1),
    ("Chatbot with 10k fixed instructions (cached) + 1k new + 500 out", 1000, 10000, 500, 1),
    ("Coding-agent step (24k cached + 1k new + 800 out)", 1000, 24000, 800, 1),
    ("A day of agent coding (300 steps)", 1000, 24000, 800, 300),
    ("10,000 typical requests a month", 2000, 0, 500, 10000),
]

def cost(m, fresh, cached, out, n):
    c = m["c"] if m["c"] is not None else m["i"] * CACHE_DEFAULT
    r = m["r"]
    return n * r * (fresh * m["i"] + cached * c + out * m["o"]) / 1e6

def money(x):
    return f"${x:,.4f}" if x < 0.1 else f"${x:,.2f}"

def pct(a, b):
    d = (a / b - 1) * 100
    return "same" if abs(d) < 0.5 else (f"{d:+.0f}%")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True); ap.add_argument("--in", dest="i", type=float, required=True)
    ap.add_argument("--out", dest="o", type=float, required=True); ap.add_argument("--cached", type=float)
    ap.add_argument("--ratio", type=float, default=1.0); ap.add_argument("--prev", default="")
    ap.add_argument("--vs", default="")
    a = ap.parse_args()
    M = load_models()
    new = dict(id="new", name=a.name, i=a.i, o=a.o, r=a.ratio, c=a.cached)
    others = [M[k] for k in ([a.prev] if a.prev else []) + [x for x in a.vs.split(",") if x] if k in M]
    missing = [k for k in ([a.prev] + a.vs.split(",")) if k and k not in M]
    if missing: print("<!-- unknown ids (check token.js):", ", ".join(missing), "-->")
    rows = [new] + others

    print(f"## {a.name} API pricing\n\nPer million tokens:\n")
    print("| Model | Input | Cached input | Output |\n|---|---:|---:|---:|")
    for m in rows:
        c = m["c"] if m["c"] is not None else m["i"] * CACHE_DEFAULT
        est = "" if m["c"] is not None else "*"
        b = "**" if m is new else ""
        print(f"| {b}{m['name']}{b} | ${m['i']:.2f} | ${c:.2f}{est} | ${m['o']:.2f} |")
    print("\n*Cached price assumed at 10% of input where the provider gives none; replace with the official number.\n")

    print(f"## What it costs on real work\n\nList prices, after each model's tokenizer difference on the same English text:\n")
    print("| Task | " + " | ".join(m["name"] for m in rows) + " |")
    print("|---|" + "---:|" * len(rows))
    for label, f, c, o, n in SCEN:
        vals = [cost(m, f, c, o, n) for m in rows]
        print(f"| {label} | " + " | ".join(money(v) for v in vals) + " |")

    print(f"\n## {a.name} vs the others (typical request)\n")
    base = cost(new, 2000, 0, 500, 1)
    for m in others:
        v = cost(m, 2000, 0, 500, 1)
        print(f"- **{m['name']}**: {money(v)} per request, {pct(v, base)} vs {a.name}")
    print("\n<!-- Percentages only, never multipliers. Quality claims only from the official announcement, attributed. -->")

if __name__ == "__main__":
    main()
