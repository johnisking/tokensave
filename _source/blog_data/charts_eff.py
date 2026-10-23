import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'
COL={"gemini":"#34d399","gpt":"#60a5fa","claude45":"#c084fc","claude55":"#f59e0b"}
NAME={"gemini":"Gemini 3.x","gpt":"GPT-4o and later (o200k)","claude45":"Claude Haiku 4.5","claude55":"Claude Opus/Sonnet 5.5"}

# 3. effort
import statistics
e0 = json.load(open('blog_data/effortdata/combined.json'))["rows"]
e = []
for m in ["Opus 5.5", "Sonnet 5.5", "Haiku 5.5"]:
    for lv in ["low", "medium", "high", "xhigh", "max"]:
        rs = [r for r in e0 if r["model_name"] == m and r["effort"] == lv and r.get("measured") != "2026-10-09"]
        if rs: e.append(dict(model_name=m, effort=lv, output_tokens=round(statistics.mean(r["output_tokens"] for r in rs)), cost_usd=statistics.mean(r["cost_usd"] for r in rs)))
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
fig.text(0.02, 0.92, "Claude Code 2.1.295, one browser game per run, average of 3 runs · Opus and Sonnet 2026-10-23, Haiku 2026-10-21 · tokensave.app/data · CC BY 4.0", fontsize=11, color=MUTED)
plt.subplots_adjust(left=0.235, right=0.98, top=0.86, bottom=0.1, wspace=0.08)
plt.savefig("src/static/claude-effort-cost-chart.png", facecolor=BG); plt.close(fig)
print("ok")
