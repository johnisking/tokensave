import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.ticker
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'
d = json.load(open('blog_data/agentsearch/combined.json'))
QS = ["q1_fact", "q2_news", "q3_compare", "q4_geo"]
def avg(t, q, s, f='input_tokens'):
    rs = [r for r in d['rows'] if r['tool'] == t and r['question'] == q and r['search'].startswith(s)]; return round(sum(r[f] for r in rs) / len(rs))
labels = [d['questions'][q]['type'] for q in QS][::-1]
series = [("codex", "Codex (gpt-6-luna)", "#60a5fa"), ("claude_code", "Claude Code (Opus 5.5)", "#f59e0b")]
fig, ax = plt.subplots(figsize=(12, 6.6), dpi=100); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
h = 0.36; mx = max(avg(t, q, 'on') for t, _, _ in series for q in QS)
for i, (t, name, col) in enumerate(series):
    vals = [avg(t, q, 'on') for q in QS][::-1]
    ys = [j + (i - 0.5) * h for j in range(len(QS))]
    ax.barh(ys, vals, height=h, color=col, label=name)
    for y, v in zip(ys, vals): ax.text(v + mx * 0.01, y, f"{v:,}", va='center', fontsize=10, color=FG)
ax.set_yticks(range(len(QS))); ax.set_yticklabels(labels, color=FG, fontsize=12)
ax.tick_params(axis='x', colors=MUTED); ax.set_xlabel("Input tokens per question (web search on, average of 2 runs)", color=MUTED, fontsize=11)
ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(5)); ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f'{int(v):,}'))
for s in ax.spines.values(): s.set_visible(False)
ax.grid(axis='x', color=GRID); ax.set_axisbelow(True); ax.set_xlim(0, mx * 1.15)
hh, ll = ax.get_legend_handles_labels(); ax.legend(hh[::-1], ll[::-1], loc='lower right', facecolor='#18181b', edgecolor=GRID, labelcolor=FG, fontsize=11)
fig.text(0.02, 0.955, "What an AI web search costs: input tokens per question", fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.92, "Claude Code vs Codex, medium effort, same Windows machine · measured 2026-10-18 · tokensave.app/data · CC BY 4.0", fontsize=10.5, color=MUTED)
plt.subplots_adjust(left=0.17, right=0.97, top=0.86, bottom=0.1)
plt.savefig('src/static/ai-agent-web-search-tokens-chart.png', facecolor=BG); plt.close(fig)
