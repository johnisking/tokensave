import json, statistics, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'
R = json.load(open('blog_data/agylang/rows.json', encoding='utf-8'))
tools = [("claude_code", "Claude Code\n+ Opus 5.5", '#fb923c'), ("antigravity_opus", "Antigravity\n+ Opus 5.5", '#a78bfa'),
         ("antigravity_gemini", "Antigravity\n+ Gemini 4 Argon", '#34d399'), ("codex", "Codex\n+ gpt-6-luna", '#60a5fa')]
langs = [("en", "EN"), ("ko", "KO"), ("ja", "JA"), ("es", "ES"), ("uk", "UK")]
fig, ax = plt.subplots(figsize=(12, 6.4), dpi=100); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
w = 0.15
for i, (t, lab, col) in enumerate(tools):
    for j, (l, ll) in enumerate(langs):
        v = statistics.mean(r["output_tokens_per_1000_chars"] for r in R if r["tool"] == t and r["lang"] == l)
        x = i + (j - 2) * w
        ax.bar(x, v, width=w * 0.9, color=col, alpha=0.55 + 0.09 * j)
        ax.text(x, v + 8, ll, ha='center', va='bottom', color=MUTED, fontsize=8)
    avg = statistics.mean(r["output_tokens_per_1000_chars"] for r in R if r["tool"] == t)
    top = max(statistics.mean(r["output_tokens_per_1000_chars"] for r in R if r["tool"] == t and r["lang"] == l) for l, _ in langs)
    ax.text(i, top + 40, f"{avg:.0f}", ha='center', color=FG, fontsize=15, fontweight='bold')
ax.set_xticks(range(len(tools))); ax.set_xticklabels([l for _, l, _ in tools]); ax.set_ylim(0, 760)
ax.set_ylabel("output tokens per 1,000 characters of code", color=MUTED)
ax.tick_params(axis='x', colors=FG, labelsize=11, length=0); ax.tick_params(axis='y', colors=MUTED)
for s in ax.spines.values(): s.set_visible(False)
ax.grid(axis='y', color=GRID); ax.set_axisbelow(True)
fig.text(0.02, 0.95, "Same code, about 60% more output tokens on Claude", fontsize=17, fontweight='bold', color=FG)
fig.text(0.02, 0.905, "Output tokens per 1,000 characters of the game each tool wrote · same task in 5 prompt languages · 80 runs · 2026-10-18 to 23 · tokensave.app/data · CC BY 4.0", fontsize=9.5, color=MUTED)
fig.text(0.02, 0.87, "Bars per tool: English, Korean, Japanese, Spanish, Ukrainian prompt. Big number: average over all languages.", fontsize=9.5, color=MUTED)
plt.subplots_adjust(left=0.08, right=0.98, top=0.82, bottom=0.12)
plt.savefig('src/static/output-tokens-per-character-by-model-chart.png', facecolor=BG); plt.close(fig)
