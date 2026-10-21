import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'
COL={"gemini":"#34d399","gpt":"#60a5fa","claude45":"#c084fc","claude55":"#f59e0b"}
NAME={"gemini":"Gemini 3.x","gpt":"GPT-4o and later (o200k)","claude45":"Claude Haiku 4.5","claude55":"Claude Opus/Sonnet 5.5"}

def hbars(labels, series, rows_vals, title, sub, xlabel, out, xmax, fmt="{:,}", h=0.2, size=(12, 8.4), left=0.17, loc='lower right'):
    fig, ax = plt.subplots(figsize=size, dpi=100); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
    n = len(series)
    for i, (k, name, col) in enumerate(series):
        ys = [j + (i - (n - 1) / 2) * h for j in range(len(labels))]
        vals = [rows_vals[j].get(k) for j in range(len(labels))]
        ax.barh([y for y, v in zip(ys, vals) if v is not None], [v for v in vals if v is not None], height=h, color=col, label=name)
        for y, v in zip(ys, vals):
            if v is not None:
                ax.text(v + xmax * 0.008, y, fmt.format(v), va='center', fontsize=8, color=MUTED)
    ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels, color=FG, fontsize=11)
    ax.tick_params(axis='x', colors=MUTED); ax.set_xlabel(xlabel, color=MUTED, fontsize=12)
    for s in ax.spines.values(): s.set_visible(False)
    ax.grid(axis='x', color=GRID); ax.set_axisbelow(True); ax.set_xlim(0, xmax)
    hh, ll = ax.get_legend_handles_labels(); ax.legend(hh[::-1], ll[::-1], loc=loc, facecolor='#18181b', edgecolor=GRID, labelcolor=FG, fontsize=11)
    fig.text(0.02, 0.965, title, fontsize=17, fontweight='bold', color=FG)
    fig.text(0.02, 0.935, sub, fontsize=11, color=MUTED)
    plt.subplots_adjust(left=left, right=0.98, top=0.89, bottom=0.08)
    plt.savefig(out, facecolor=BG); plt.close(fig)

# 1. programming languages
rows = json.load(open('blog_data/codedata/combined.json'))
rows = rows[::-1]
ser = [(k, NAME[k], COL[k]) for k in ["gemini", "gpt", "claude45", "claude55"]]
hbars([r["name"] for r in rows], ser, rows, "Same two programs in 10 languages: how many tokens each costs",
      "Inventory class + Dijkstra, identical output in every language · measured 2026-10-18 · tokensave.app/data · CC BY 4.0",
      "Tokens for both programs together", "src/static/token-cost-by-programming-language-chart.png", 2650, loc="upper right")

# 2. PDF
p = {r["input"]: r for r in json.load(open('blog_data/pdfdata/combined.json'))}
order = ["table_plain", "text_page_plain", "scan_1p", "table_1p", "text_1p"]
lab = {"text_1p": "Text page as PDF", "table_1p": "Table page as PDF", "scan_1p": "Scanned page as PDF", "text_page_plain": "Same text pasted", "table_plain": "Same table pasted (CSV)"}
ser = [(k, NAME[k], COL[k]) for k in ["gemini", "gpt", "claude45", "claude55"]]
hbars([lab[k] for k in order], ser, [p[k] for k in order], "One page, PDF or pasted: how many tokens it costs",
      "Gemini: flat 560 tokens per PDF page · Claude: text plus an image per page · GPT shown for pasted text only · measured 2026-10-18",
      "Input tokens for one page", "src/static/pdf-token-cost-chart.png", 2900, size=(12, 7.2), left=0.2)

# 3. effort
import statistics
e0 = json.load(open('blog_data/effortdata/combined.json'))["rows"]
e = [r for r in e0 if r["model_name"] != "Haiku 5.5"]
for lv in ["low", "medium", "high", "xhigh", "max"]:
    rs = [r for r in e0 if r["model_name"] == "Haiku 5.5" and r["effort"] == lv]
    if rs: e.append(dict(model_name="Haiku 5.5", effort=lv + " (avg of 3)", output_tokens=round(statistics.mean(r["output_tokens"] for r in rs)), cost_usd=statistics.mean(r["cost_usd"] for r in rs)))
fig, axes = plt.subplots(1, 2, figsize=(12, 8.2), dpi=100); fig.patch.set_facecolor(BG)
labels = [f'{r["model_name"]} · {r["effort"]}' for r in e][::-1]
cols = [{"Opus": "#f59e0b", "Sonnet": "#38bdf8", "Haiku": "#34d399"}[r["model_name"].split()[0]] for r in e][::-1]
for ax, key, xl, fmt in [(axes[0], "output_tokens", "Output tokens", "{:,}"), (axes[1], "cost_usd", "Cost (USD, API prices)", None)]:
    ax.set_facecolor(BG); vals = [r[key] for r in e][::-1]
    ax.barh(range(len(vals)), vals, color=cols, height=0.6)
    mx = max(vals)
    for i, v in enumerate(vals): ax.text(v + mx * 0.01, i, fmt.format(v) if fmt else (f"${v:.2f}" if v >= 0.1 else f"${v:.3f}"), va='center', fontsize=9, color=MUTED)
    ax.set_yticks(range(len(vals))); ax.set_yticklabels(labels if ax is axes[0] else [""] * len(vals), color=FG, fontsize=11)
    ax.tick_params(axis='x', colors=MUTED); ax.set_xlabel(xl, color=MUTED, fontsize=11)
    for s in ax.spines.values(): s.set_visible(False)
    ax.grid(axis='x', color=GRID); ax.set_axisbelow(True); ax.set_xlim(0, mx * 1.18)
fig.text(0.02, 0.955, "Same coding task at every effort level: tokens and cost", fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.92, "Claude Code, one browser game per run · Opus and Sonnet measured 2026-10-09, Haiku 2026-10-21 · tokensave.app/data · CC BY 4.0", fontsize=11, color=MUTED)
plt.subplots_adjust(left=0.235, right=0.98, top=0.86, bottom=0.1, wspace=0.08)
plt.savefig("src/static/claude-effort-cost-chart.png", facecolor=BG); plt.close(fig)
print("ok")
