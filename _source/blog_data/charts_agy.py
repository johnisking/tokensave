import json, statistics, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'; VIO='#a78bfa'; GREEN='#34d399'; ORANGE='#fb923c'; BLUE='#60a5fa'
R = json.load(open('blog_data/agy3/rows.json', encoding='utf-8'))
tools = [("claude", "Claude Code\n+ Opus 5.5", ORANGE), ("codex", "Codex\n+ gpt-6-luna", BLUE), ("agyg", "Antigravity CLI\n+ Gemini 4 Argon", GREEN), ("agyo", "Antigravity CLI\n+ Opus 5.5", VIO)]
m = lambda t, kind, k, n=None: statistics.mean(r.get(k, 0) for r in R if r["tool"] == t and r["kind"] == kind and (n is None or r["n"] == n))
fig, axes = plt.subplots(1, 2, figsize=(12, 6.4), dpi=100, gridspec_kw=dict(width_ratios=[1, 1.35]))
fig.patch.set_facecolor(BG)
for ax, kind, title in ((axes[0], "base", "Before any work (\"Reply OK\")"), (axes[1], "game", "The same brick-breaker game task")):
    ax.set_facecolor(BG)
    top = max(m(t, kind, "inp", 0 if kind == "base" else None) + (m(t, kind, "cache_read", 0 if kind == "base" else None) if t.startswith("agy") else 0) for t, _, _ in tools)
    for i, (t, lab, col) in enumerate(tools):
        n = 0 if kind == "base" else None
        v = m(t, kind, "inp", n); c = m(t, kind, "cache_read", n) if t.startswith("agy") else 0
        ax.barh(i, v, color=col, height=0.6)
        txt = f"{v:,.0f}"
        if c:
            ax.barh(i, c, left=v, color=col, alpha=0.3, height=0.6, hatch='///', edgecolor=col, linewidth=0)
            txt += f"\n+{c:,.0f} cache reads"
        ax.text(v + c + top * 0.02, i, txt, va='center', color=FG, fontsize=10)
    ax.set_yticks(range(len(tools))); ax.set_yticklabels([l for _, l, _ in tools] if kind == "base" else [""] * 4); ax.invert_yaxis()
    ax.set_xlim(0, top * 1.45); ax.set_title(title, color=FG, fontsize=12, loc='left', pad=10)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{x/1000:.0f}k"))
    ax.tick_params(axis='x', colors=MUTED); ax.tick_params(axis='y', colors=FG, labelsize=10.5, length=0)
    for s in ax.spines.values(): s.set_visible(False)
    ax.grid(axis='x', color=GRID); ax.set_axisbelow(True)
fig.text(0.02, 0.95, "Input tokens: Antigravity CLI vs Claude Code vs Codex", fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.905, "Average per run · Claude Code 2.1.295 · Codex CLI 0.162 · Antigravity CLI 1.4.5 · 52 runs · 2026-10-18 to 23 · tokensave.app/data · CC BY 4.0", fontsize=9.5, color=MUTED)
fig.text(0.02, 0.87, "Hatched: cache reads Antigravity reports separately (whether they belong in input is undocumented). All 20 games worked (5 per tool).", fontsize=9.5, color=MUTED)
plt.subplots_adjust(left=0.15, right=0.98, top=0.79, bottom=0.07, wspace=0.08)
plt.savefig('src/static/antigravity-cli-vs-claude-code-vs-codex-chart.png', facecolor=BG); plt.close(fig)
