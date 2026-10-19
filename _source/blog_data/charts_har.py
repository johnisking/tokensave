import json, statistics, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.ticker
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'
d = json.load(open('blog_data/harness/combined.json', encoding='utf-8'))
C = [("minimal", "Minimal harness\n(1-line prompt, 2 tools)"), ("safemode", "Safe mode\n(no personal plugins)"), ("default", "Default"),
     ("hook", "+ PostToolUse hook"), ("skill", "+ one project skill"), ("plan", "Plan mode, then build"), ("subagent", "Delegated to a subagent")]
med = lambda c, k: statistics.median(r[k] for r in d["rows"] if r["condition"] == c)
base_in, base_cost = med("default", "input_tokens"), med("default", "api_cost_usd")
fig, axes = plt.subplots(1, 2, figsize=(12, 6.2), dpi=100, sharey=True); fig.patch.set_facecolor(BG)
for ax, key, base, title, fmt, col in [(axes[0], "input_tokens", base_in, "Input tokens (median)", lambda v: f"{round(v):,}", "#a78bfa"),
                                       (axes[1], "api_cost_usd", base_cost, "API cost (median)", lambda v: f"${v:.2f}", "#f59e0b")]:
    ax.set_facecolor(BG)
    ys = range(len(C))
    vals = [med(c, key) for c, _ in C]
    top = max(vals)
    for y, (c, _), v in zip(ys, C, vals):
        ax.barh(y, v, color=col if c != "default" else MUTED, height=0.62)
        pct = "" if c == "default" else f"  {'+' if v >= base else '−'}{abs(round((v / base - 1) * 100))}%"
        runs = [r[key] for r in d["rows"] if r["condition"] == c]
        for rv in runs:
            ax.plot(rv, y, '|', color=FG, ms=12, alpha=0.6)
        ax.text(max(runs + [v]) + top * 0.03, y, fmt(v) + pct, va='center', color=FG, fontsize=10.5)
    ax.set_xlim(0, top * 1.75)
    ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(4))
    ax.set_title(title, color=FG, fontsize=12.5, loc='left')
    ax.tick_params(axis='x', colors=MUTED); ax.tick_params(axis='y', colors=FG, labelsize=10.5, length=0)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _, f=fmt: f(v) if v else "0"))
    for s in ax.spines.values(): s.set_visible(False)
    ax.grid(axis='x', color=GRID); ax.set_axisbelow(True)
axes[0].set_yticks(list(range(len(C)))); axes[0].set_yticklabels([n for _, n in C]); axes[0].invert_yaxis()
fig.text(0.02, 0.955, "The same coding task under 7 Claude Code harness settings", fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.915, "Brick-breaker game in one HTML file · Opus 5.5, medium effort · bar = median, ticks = each of 5 runs · % vs default · measured 2026-10-19 · tokensave.app/data · CC BY 4.0", fontsize=9.5, color=MUTED)
plt.subplots_adjust(left=0.17, right=0.98, top=0.83, bottom=0.07, wspace=0.08)
plt.savefig('src/static/claude-code-harness-cost-chart.png', facecolor=BG); plt.close(fig)
