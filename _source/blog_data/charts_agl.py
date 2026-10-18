import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'
d = json.load(open('blog_data/agentsearchlang/combined.json', encoding='utf-8'))
LANGS = [("uk", "Ukrainian"), ("es", "Spanish"), ("ja", "Japanese"), ("ko", "Korean")]
EN, LOC, OTH = '#60a5fa', '#f59e0b', '#71717a'
def tot(l, f): return sum(r[f] for r in d['rows'] if r['language'] == l)
fig, axes = plt.subplots(1, 2, figsize=(12, 6.2), dpi=100); fig.patch.set_facecolor(BG)
panels = [("Web searches Claude ran", [("searches_in_english", "In English", EN), ("searches_in_question_language", "In the question's language", LOC)]),
          ("Links cited in the answer", [("cited_links", "English pages", EN), ("cited_in_question_language", "Question's language", LOC), ("cited_other_language", "Other language", OTH)])]
for ax, (title, parts) in zip(axes, panels):
    ax.set_facecolor(BG)
    for i, (l, name) in enumerate(LANGS):
        left = 0
        vals = []
        for f, lab, col in parts:
            v = tot(l, f)
            if f == "cited_links": v = v - tot(l, "cited_in_question_language") - tot(l, "cited_other_language")
            vals.append((v, lab, col))
        for v, lab, col in vals:
            ax.barh(i, v, left=left, color=col, height=0.6, label=lab if i == 0 else None)
            if v: ax.text(left + v / 2, i, str(v), ha='center', va='center', color='#0f0f12', fontsize=11, fontweight='bold')
            left += v
    ax.set_yticks(range(len(LANGS))); ax.set_yticklabels([f"{n} question" for _, n in LANGS], color=FG, fontsize=12)
    ax.set_title(title, color=FG, fontsize=13, loc='left', pad=10)
    ax.tick_params(axis='x', colors=MUTED)
    for s in ax.spines.values(): s.set_visible(False)
    ax.grid(axis='x', color=GRID); ax.set_axisbelow(True)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=len(parts) if len(parts)<3 else 2, facecolor=BG, edgecolor=BG, labelcolor=FG, fontsize=9.5)
axes[1].set_yticklabels([])
fig.text(0.02, 0.955, "Ask Claude in another language, it still searches the English web", fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.915, "Claude Code (Opus 5.5) with web search, 4 questions x 2 runs per language · measured 2026-10-18 · tokensave.app/data · CC BY 4.0", fontsize=10.5, color=MUTED)
plt.subplots_adjust(left=0.165, right=0.98, top=0.82, bottom=0.2, wspace=0.08)
plt.savefig('src/static/claude-web-search-by-language-chart.png', facecolor=BG); plt.close(fig)
