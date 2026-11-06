"""Chart for /data/claude-subagent-effort (run from _source/): recall flat, cost up, by condition and model."""
import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG = '#0f0f12'; FG = '#e4e4e7'; MUTED = '#a1a1aa'; GRID = '#27272a'
COL = {'haiku': '#38bdf8', 'opus': '#a78bfa'}
S = json.load(open('blog_data/subagent/dataset/claude-subagent-effort.json', encoding='utf-8'))['summary']
C = ['C0', 'C1', 'C2', 'C3']
LAB = ['No instruction', 'Subagents\neffort low', 'Subagents\neffort medium', 'Subagents\neffort high']
fig, axs = plt.subplots(1, 2, figsize=(12, 6.3), dpi=100); fig.patch.set_facecolor(BG)
w = 0.38
for ax, k, title, fmt, top in ((axs[0], 'recall_pct', 'Share of the right answers found', lambda v: f'{v:.0f}%', 100),
                               (axs[1], 'cost_change_pct', 'API cost per run vs no instruction', lambda v: f'+{v:.0f}%', None)):
    ax.set_facecolor(BG)
    for i, (m, lab) in enumerate((('haiku', 'Haiku 5.5'), ('opus', 'Opus 5.5'))):
        vals = [S[f'{m}_{c}'][k] for c in C]
        xs = [j + (i - 0.5) * w for j in range(4)]
        ax.bar(xs, vals, w * 0.92, color=COL[m], label=lab)
        for x, v in zip(xs, vals):
            ax.text(x, v + (top or 230) * 0.015, fmt(v), ha='center', va='bottom', color=FG, fontsize=9.5)
    ax.set_xticks(range(4)); ax.set_xticklabels(LAB, color=FG, fontsize=9.5)
    ax.set_title(title, color=FG, fontsize=13, fontweight='bold', loc='left', pad=12)
    ax.tick_params(colors=MUTED, length=0); ax.yaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
    for s in ax.spines.values(): s.set_visible(False)
    if top: ax.set_ylim(0, 108); ax.set_yticks([0, 25, 50, 75, 100]); ax.set_yticklabels(['0', '25%', '50%', '75%', '100%'], color=MUTED)
    else: ax.set_ylim(0, 255); ax.set_yticks([0, 50, 100, 150, 200, 250]); ax.set_yticklabels(['0', '+50%', '+100%', '+150%', '+200%', '+250%'], color=MUTED)
axs[0].legend(loc='lower left', facecolor=BG, edgecolor=GRID, labelcolor=FG, fontsize=10)
fig.text(0.02, 0.95, 'Subagents in Claude Code raised the cost, not what it found', fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.913, '288 Claude Code 2.1.318 runs on 12 code-search questions · subagent effort low / medium / high · tokensave.app/data · CC BY 4.0', fontsize=9.5, color=MUTED)
plt.subplots_adjust(left=0.06, right=0.98, top=0.8, bottom=0.14, wspace=0.18)
plt.savefig('src/static/claude-subagent-effort-chart.png', facecolor=BG); plt.close(fig)
print('ok')
