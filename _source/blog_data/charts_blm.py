import json, statistics, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'; GREEN='#34d399'
R = json.load(open('blog_data/blendermcp/rows.json', encoding='utf-8'))
tasks = [("infoS", "Describe a small room"), ("infoL", "Describe a 580-object city"), ("build", "Build a table + 4 chairs"),
         ("red", "Make the chairs red, look"), ("sides", "Look from 4 sides"), ("race", "Racing scene + chase camera"),
         ("verts", "Probe: print 19,042 vertices"), ("props", "Probe: print every property")]
cost = lambda t, m: statistics.mean(r["api_cost_usd"] for r in R if r["task"] == t and r["mode"] == m)
fig, ax = plt.subplots(figsize=(12, 6.4), dpi=100); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
top = max(cost(t, m) for t, _ in tasks for m in ("base", "diet"))
for i, (t, lab) in enumerate(tasks):
    b, d = cost(t, "base"), cost(t, "diet")
    ax.barh(i, b, color=MUTED, height=0.36); ax.text(b + top*0.01, i, f"${b:.2f}  as shipped", va='center', color=FG, fontsize=10.5)
    ax.barh(i + 0.4, d, color=GREEN, height=0.36)
    ch = round((d / b - 1) * 100)
    ax.text(d + top*0.01, i + 0.4, f"${d:.2f}  with tokensave-mcp-diet 0.3 ({'+' if ch > 0 else '−' if ch < 0 else ''}{abs(ch)}%)", va='center', color=FG, fontsize=10.5)
ax.set_yticks([i + 0.2 for i in range(len(tasks))]); ax.set_yticklabels([l for _, l in tasks]); ax.invert_yaxis()
ax.set_xlim(0, top * 1.55)
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"${v:.2f}"))
ax.tick_params(axis='x', colors=MUTED); ax.tick_params(axis='y', colors=FG, labelsize=10.5, length=0)
for s in ax.spines.values(): s.set_visible(False)
ax.grid(axis='x', color=GRID); ax.set_axisbelow(True)
fig.text(0.02, 0.95, "What one task costs with MCP for Blender in Claude Code", fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.905, "Average API cost per task · Claude Code 2.1.295 · Opus 5.5 · Blender 5.2.2 · 72 runs · measured 2026-10-22 · tokensave.app/data · CC BY 4.0", fontsize=9.5, color=MUTED)
fig.text(0.02, 0.87, "Differences under about 8% are within run-to-run noise; the property dump is the one case the diet clearly fixes", fontsize=9.5, color=MUTED)
plt.subplots_adjust(left=0.2, right=0.98, top=0.83, bottom=0.07)
plt.savefig('src/static/blender-mcp-token-cost-chart.png', facecolor=BG); plt.close(fig)
