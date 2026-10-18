import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'
CC='#f59e0b'; CX='#60a5fa'
d = json.load(open('blog_data/agentbase/combined.json'))
base = {(r['tool'], r['mcp_tools']): r['avg'] for r in d['rows']}
def avg(tool, f):
    rs = [r for r in d['task']['rows'] if r['tool'] == tool]; return round(sum(r[f] for r in rs) / len(rs))
panels = [
  ("Startup: one-word reply", [base[('codex',0)], base[('claude_code',0)]], "Input tokens"),
  ("Startup with 30 MCP tools", [base[('codex',30)], base[('claude_code',30)]], "Input tokens"),
  ("Same coding task: input", [avg('codex','input_tokens'), avg('claude_code','input_tokens')], "Input tokens"),
  ("Same coding task: output", [avg('codex','output_tokens'), avg('claude_code','output_tokens')], "Output tokens"),
]
fig, axes = plt.subplots(2, 2, figsize=(12, 7.4), dpi=100); fig.patch.set_facecolor(BG)
for ax, (t, vals, xl) in zip(axes.flat, panels):
    ax.set_facecolor(BG); ax.barh([0, 1], vals, color=[CX, CC], height=0.55)
    mx = max(vals)
    for i, v in enumerate(vals): ax.text(v + mx * 0.015, i, f"{v:,}", va='center', fontsize=11, color=FG)
    ax.set_yticks([0, 1]); ax.set_yticklabels(["Codex (gpt-6-luna)", "Claude Code (Opus 5.5)"], color=FG, fontsize=11)
    ax.set_title(t, color=FG, fontsize=13, loc='left', pad=8)
    ax.tick_params(axis='x', colors=MUTED); ax.set_xlabel(xl, color=MUTED, fontsize=10)
    for s in ax.spines.values(): s.set_visible(False)
    ax.grid(axis='x', color=GRID); ax.set_axisbelow(True); ax.set_xlim(0, mx * 1.22)
    ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(4)); ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f'{int(v):,}'))
fig.text(0.02, 0.965, "Claude Code vs Codex: tokens before and during work", fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.93, "Averages of 2 runs · same Windows machine · task: browser brick-breaker at medium effort · measured 2026-10-18 · tokensave.app/data · CC BY 4.0", fontsize=10.5, color=MUTED)
plt.subplots_adjust(left=0.17, right=0.98, top=0.85, bottom=0.08, hspace=0.55, wspace=0.55)
plt.savefig('src/static/claude-code-vs-codex-tokens-chart.png', facecolor=BG); plt.close(fig)
