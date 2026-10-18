import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.ticker
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'
d = json.load(open('blog_data/tasklang/combined.json', encoding='utf-8'))
L = [("en", "English"), ("ko", "Korean"), ("ja", "Japanese"), ("es", "Spanish"), ("uk", "Ukrainian")]
fig, ax = plt.subplots(figsize=(12, 6.2), dpi=100); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
w = 0.36
for i, (tool, name, col) in enumerate([("claude_code", "Claude Code (Opus 5.5)", "#f59e0b"), ("codex", "Codex (gpt-6-luna)", "#60a5fa")]):
    for j, (l, _) in enumerate(L):
        rs = [r["input_tokens"] for r in d["rows"] if r["tool"] == tool and r["prompt_language"] == l]
        x = j + (i - 0.5) * w
        ax.bar(x, sum(rs) / len(rs), width=w, color=col, label=name if j == 0 else None)
        for v in rs: ax.plot(x, v, 'o', color=FG, ms=4)
        ax.text(x, sum(rs)/len(rs) + 2500 if l != "en" or tool != "claude_code" else sum(rs)/len(rs) + 2500, f"{round(sum(rs)/len(rs)):,}", ha='center', color=FG, fontsize=9.5)
ax.annotate('run 1 took an extra\nagent step', xy=(-0.18, 123666), xytext=(0.25, 128000), color=MUTED, fontsize=9.5, arrowprops=dict(arrowstyle='-', color=MUTED))
ax.set_xticks(range(len(L))); ax.set_xticklabels([f"{n} prompt" for _, n in L], color=FG, fontsize=11.5)
ax.tick_params(axis='y', colors=MUTED); ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f'{int(v):,}'))
ax.set_ylabel("Input tokens for the whole task (bar = average, dots = each run)", color=MUTED, fontsize=10.5)
for s in ax.spines.values(): s.set_visible(False)
ax.grid(axis='y', color=GRID); ax.set_axisbelow(True); ax.set_ylim(0, 140000)
ax.legend(loc='upper right', facecolor='#18181b', edgecolor=GRID, labelcolor=FG, fontsize=11)
fig.text(0.02, 0.955, "The same coding task, prompted in 5 languages", fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.915, "Brick-breaker game in one HTML file · Claude Code and Codex at medium effort · measured 2026-10-18 · tokensave.app/data · CC BY 4.0", fontsize=10, color=MUTED)
plt.subplots_adjust(left=0.09, right=0.98, top=0.86, bottom=0.09)
plt.savefig('src/static/ai-coding-prompt-language-chart.png', facecolor=BG); plt.close(fig)
