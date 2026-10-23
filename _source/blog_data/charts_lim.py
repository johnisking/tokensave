"""Chart for /data/ai-coding-limit-line: full-marks runs per tool and task level (run from _source/)."""
import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG = '#0f0f12'; FG = '#e4e4e7'; MUTED = '#a1a1aa'; GRID = '#27272a'
D = json.load(open('blog_data/limitline/dataset/ai-coding-limit-line.json', encoding='utf-8'))
R = [r for r in D['runs'] if not r['excluded']]
tools = [('haiku', 'Claude Code\n+ Haiku 5.5'), ('sonnet', 'Claude Code\n+ Sonnet 5.5'), ('opus', 'Claude Code\n+ Opus 5.5'),
         ('codex', 'Codex\n+ gpt-6-luna'), ('gemini', 'Antigravity\n+ Gemini 4 Argon')]
tasks = [('2', 'L2\nlevels + save'), ('3', 'L3\nmulti-file app'), ('4', 'L4\n5 modules, 3 views'), ('5a', 'L5A\nfix 6 bugs\n+ 3 features'),
         ('5b', 'L5B\nspreadsheet\nengine'), ('6t1', 'L6 easy\nreal bug'), ('6t2', 'L6 medium\nreal bug'), ('6t3', 'L6 hard\nreal bug')]
fig, ax = plt.subplots(figsize=(12, 6.4), dpi=100); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
for i, (t, _) in enumerate(tools):
    for j, (k, _) in enumerate(tasks):
        rs = [r for r in R if r['tool'] == t and r['task'] == k]
        n = len(rs); ok = sum(bool(r['full_marks']) for r in rs)
        frac = ok / n if n else 0
        col = '#16a34a' if frac == 1 else ('#dc2626' if frac == 0 else '#d97706')
        ax.add_patch(plt.Rectangle((j + 0.04, i + 0.06), 0.92, 0.88, color=col, alpha=0.85))
        ax.text(j + 0.5, i + 0.5, f'{ok}/{n}', ha='center', va='center', color='white', fontsize=15, fontweight='bold')
ax.set_xlim(0, len(tasks)); ax.set_ylim(len(tools), 0)
ax.set_xticks([j + 0.5 for j in range(len(tasks))]); ax.set_xticklabels([l for _, l in tasks], fontsize=9.5, color=FG)
ax.set_yticks([i + 0.5 for i in range(len(tools))]); ax.set_yticklabels([l for _, l in tools], fontsize=10, color=FG)
ax.tick_params(length=0)
for s in ax.spines.values(): s.set_visible(False)
ax.xaxis.tick_top()
fig.text(0.02, 0.955, 'Where AI coding agents first fail', fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.915, f"Runs with full marks / runs, by task level · {len(R)} runs · 2026-10-23 to 24 · tokensave.app/data · CC BY 4.0",
         fontsize=9.5, color=MUTED)
fig.text(0.02, 0.03, 'Levels 2 to 5: hidden-test scores on apps built from a spec or fixed from bug reports. Level 6: real bugs fixed upstream in the marked '
         'Markdown parser (Sep to Oct 2026); a point needs the upstream hidden test to pass with no other test broken.', fontsize=8.5, color=MUTED, wrap=True)
plt.subplots_adjust(left=0.13, right=0.99, top=0.76, bottom=0.08)
plt.savefig('src/static/ai-coding-limit-line-chart.png', facecolor=BG); plt.close(fig)
print('ok')
