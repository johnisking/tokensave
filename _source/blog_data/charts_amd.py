import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.ticker
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'
d = json.load(open('blog_data/agentmd/combined.json'))
R = [r for r in d['rows'] if r['turn'] == 1 and r['run'] == 1]
fig, ax = plt.subplots(figsize=(12, 6.4), dpi=100); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
for tool, name, col in [("claude_code", "Claude Code (CLAUDE.md)", "#f59e0b"), ("codex", "Codex (AGENTS.md)", "#60a5fa")]:
    rs = sorted([r for r in R if r['tool'] == tool], key=lambda r: r['file_bytes'])
    base = rs[0]['input_tokens']
    xs = [r['file_bytes'] / 1024 for r in rs]; ys = [r['input_tokens'] - base for r in rs]
    if tool == 'codex':
        ax.plot(xs[:-1], ys[:-1], marker='o', color=col, lw=2.5, label=name)
        ax.plot(xs[-2:], ys[-2:], color=col, lw=2, ls=':'); ax.plot(xs[-1:], ys[-1:], marker='o', color=col)
    else:
        ax.plot(xs, ys, marker='o', color=col, lw=2.5, label=name)
    ax.text(xs[-1] + 0.8, ys[-1], f"+{ys[-1]:,}", color=col, va='center', fontsize=12, fontweight='bold')
ax.axvline(32, color=MUTED, ls='--', lw=1)
ax.text(32.6, 4500, "Codex stops reading\nAGENTS.md at 32 KiB\n(no sizes measured\nbetween 25 and 50 KB)", color=MUTED, fontsize=10.5, va='top')
ax.set_xlabel("Instruction file size (KB)", color=MUTED, fontsize=11); ax.set_ylabel("Extra input tokens on every request", color=MUTED, fontsize=11)
ax.tick_params(colors=MUTED); ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f'{int(v):,}'))
for s in ax.spines.values(): s.set_visible(False)
ax.grid(color=GRID); ax.set_axisbelow(True); ax.set_xlim(-1, 57); ax.set_ylim(-500, 18000)
ax.legend(loc='upper left', facecolor='#18181b', edgecolor=GRID, labelcolor=FG, fontsize=11)
fig.text(0.02, 0.955, "What a big CLAUDE.md or AGENTS.md costs on every request", fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.915, "Extra input tokens vs no instruction file, first turn · Claude Code (Opus 5.5) and Codex (gpt-6-luna) · measured 2026-10-18 · tokensave.app/data · CC BY 4.0", fontsize=9.5, color=MUTED)
plt.subplots_adjust(left=0.09, right=0.93, top=0.86, bottom=0.1)
plt.savefig('src/static/claude-md-agents-md-size-chart.png', facecolor=BG); plt.close(fig)
