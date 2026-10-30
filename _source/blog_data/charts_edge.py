"""Chart for /data/claude-edge-case-prompts (run from _source/): pass rate flat, cost up, by condition and model."""
import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG = '#0f0f12'; FG = '#e4e4e7'; MUTED = '#a1a1aa'; GRID = '#27272a'
COL = {'claude-haiku-5-5': '#38bdf8', 'claude-opus-5-5': '#a78bfa'}
D = json.load(open('blog_data/edgecases/dataset/claude-edge-case-prompts.json', encoding='utf-8'))
S = D['stats']['all']; C = ['C0', 'C1', 'C2', 'C3']
LAB = ['Baseline', 'Effort high', 'Edge-case\nprompt', 'Edge-case prompt\n+ read tests']
fig, axs = plt.subplots(1, 2, figsize=(12, 6.3), dpi=100); fig.patch.set_facecolor(BG)
w = 0.38
for ax, key, title, fmt, top in ((axs[0], 'unreported_pass_rate', 'Unreported cases passed', lambda v: f'{v*100:.0f}%', 1.0),
                                 (axs[1], 'mean_cost_usd', 'API cost per run', lambda v: f'${v:.2f}', None)):
    ax.set_facecolor(BG)
    for i, (m, lab) in enumerate((('claude-haiku-5-5', 'Haiku 5.5'), ('claude-opus-5-5', 'Opus 5.5'))):
        vals = [S[m][c][key] for c in C]
        xs = [j + (i - 0.5) * w for j in range(4)]
        ax.bar(xs, vals, w * 0.92, color=COL[m], label=lab)
        for x, v in zip(xs, vals):
            ax.text(x, v + (top or max(S['claude-opus-5-5'][c][key] for c in C)) * 0.015, fmt(v), ha='center', va='bottom', color=FG, fontsize=9.5)
    ax.set_xticks(range(4)); ax.set_xticklabels(LAB, color=FG, fontsize=9.5)
    ax.set_title(title, color=FG, fontsize=13, fontweight='bold', loc='left', pad=12)
    ax.tick_params(colors=MUTED, length=0); ax.yaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
    for s in ax.spines.values(): s.set_visible(False)
    if top: ax.set_ylim(0, 1.08); ax.set_yticks([0, .25, .5, .75, 1]); ax.set_yticklabels(['0', '25%', '50%', '75%', '100%'], color=MUTED)
    else:
        mx = max(S['claude-opus-5-5'][c][key] for c in C); ax.set_ylim(0, mx * 1.15)
        ax.set_yticklabels([f'${t:.2f}' for t in ax.get_yticks()], color=MUTED)
axs[0].legend(loc='lower left', facecolor=BG, edgecolor=GRID, labelcolor=FG, fontsize=10)
fig.text(0.02, 0.95, 'Asking Claude for edge cases raised the cost, not the pass rate', fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.913, '504 Claude Code runs on 21 real bugs · cases the bug report left out, scored by the maintainers’ tests · tokensave.app/data · CC BY 4.0', fontsize=9.5, color=MUTED)
plt.subplots_adjust(left=0.06, right=0.98, top=0.8, bottom=0.14, wspace=0.18)
plt.savefig('src/static/claude-edge-case-prompts-chart.png', facecolor=BG); plt.close(fig)
print('ok')
