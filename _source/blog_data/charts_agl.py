import json, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'
d = json.load(open('blog_data/agentsearchlang/combined.json', encoding='utf-8'))
R = d['rows']
EN, LOC, OTH = '#60a5fa', '#f59e0b', '#71717a'
T = lambda rs, f: sum((r[f] or 0) for r in rs)
groups = [
  ("AI topic · asked in KO/JA/ES/UK\nCodex", [r for r in R if r['topic'] == 'ai' and r['tool'] == 'codex' and r['ask_language'] != 'en'], 'ask'),
  ("AI topic · asked in KO/JA/ES/UK\nClaude Code", [r for r in R if r['topic'] == 'ai' and r['tool'] == 'claude_code' and r['ask_language'] != 'en'], 'ask'),
  ("Local topic · asked in English\nClaude Code", [r for r in R if r['topic'] == 'local' and r['ask_language'] == 'en'], 'topic'),
  ("Local topic · asked in local language\nClaude Code", [r for r in R if r['topic'] == 'local' and r['ask_language'] != 'en'], 'topic'),
]
fig, axes = plt.subplots(1, 2, figsize=(12, 6.4), dpi=100); fig.patch.set_facecolor(BG)
for ax, (title, tot, en_f, loc_f) in zip(axes, [("Search queries", "search_queries_count", "queries_in_english", None), ("Links cited in the answer", "cited_links", "cited_english", None)]):
    ax.set_facecolor(BG)
    for i, (lab, rs, kind) in enumerate(groups):
        n = T(rs, tot); en = T(rs, en_f)
        if tot == "search_queries_count":
            loc = T(rs, "queries_in_ask_language" if kind == 'ask' else "queries_in_topic_language")
        else:
            loc = T(rs, "cited_in_ask_language" if kind == 'ask' else "cited_in_topic_language")
        oth = n - en - loc
        left = 0
        for v, col in [(en, EN), (loc, LOC), (oth, OTH)]:
            w = v / n * 100
            ax.barh(i, w, left=left, color=col, height=0.6)
            if w >= 7: ax.text(left + w / 2, i, f"{round(w)}%", ha='center', va='center', color='#0f0f12', fontsize=11, fontweight='bold')
            left += w
    ax.set_xlim(0, 100); ax.set_yticks(range(len(groups)))
    ax.set_yticklabels([g[0] for g in groups], color=FG, fontsize=10.5)
    ax.set_title(title, color=FG, fontsize=13, loc='left', pad=10)
    ax.tick_params(axis='x', colors=MUTED); ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{int(v)}%"))
    for s in ax.spines.values(): s.set_visible(False)
    ax.grid(axis='x', color=GRID); ax.set_axisbelow(True)
axes[1].set_yticklabels([])
from matplotlib.patches import Patch
fig.legend(handles=[Patch(color=EN, label='English'), Patch(color=LOC, label="The question's language (AI topic) / the country's language (local topic)"), Patch(color=OTH, label='Other')],
           loc='lower center', ncol=3, facecolor=BG, edgecolor=BG, labelcolor=FG, fontsize=10)
fig.text(0.02, 0.955, "AI agents search in English, unless the topic is local", fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.915, "Claude Code (Opus 5.5) and Codex with web search, questions in Korean, Japanese, Spanish, Ukrainian and English · measured 2026-10-18 · tokensave.app/data · CC BY 4.0", fontsize=9.5, color=MUTED)
plt.subplots_adjust(left=0.25, right=0.98, top=0.83, bottom=0.17, wspace=0.12)
plt.savefig('src/static/claude-web-search-by-language-chart.png', facecolor=BG); plt.close(fig)
