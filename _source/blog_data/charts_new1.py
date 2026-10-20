import json, statistics, sys, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
sys.path.insert(0, 'src')
import data_pages as D
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'; C=['#a78bfa', '#38bdf8', '#f472b6']
def frame(title, sub, foot):
    fig = plt.figure(figsize=(12, 6.2), dpi=100); fig.patch.set_facecolor(BG)
    fig.text(0.02, 0.95, title, fontsize=18, fontweight='bold', color=FG)
    fig.text(0.02, 0.905, sub, fontsize=10, color=MUTED)
    fig.text(0.02, 0.02, foot, fontsize=9.5, color=MUTED)
    return fig
def style(ax):
    ax.set_facecolor(BG); ax.tick_params(colors=MUTED)
    for s in ax.spines.values(): s.set_visible(False)
    ax.grid(axis='y', color=GRID); ax.set_axisbelow(True)

# vibe
d = D._vib(); R = d['rows']
fig = frame("Vibe coding: Claude Haiku vs Sonnet vs Opus 5.5", "Median of 5 runs per game · all 45 games passed automated play tests · Claude Code, effort medium",
            f"{D.VIB_MEASURED} · tokensave.app/data/vibe-coding-by-claude-model · CC BY 4.0")
for k, (key, lab, fmt) in enumerate([("api_cost_usd", "API cost per game (USD)", "${:.2f}"), ("seconds", "Time per game (seconds)", "{:.0f} s")]):
    ax = fig.add_axes([0.06 + k * 0.49, 0.12, 0.42, 0.68]); style(ax)
    for j, (m, mn) in enumerate(D.VIB_MODELS):
        vals = [statistics.median(r[key] for r in R if r['task'] == t and r['model'] == m) for t, _ in D.VIB_TASKS]
        xs = [i + (j - 1) * 0.27 for i in range(3)]
        ax.bar(xs, vals, 0.25, color=C[j], label=mn)
        for x, v in zip(xs, vals):
            ax.text(x, v, (("$%.3f" % v) if key == "api_cost_usd" and v < 0.1 else fmt.format(v)), ha='center', va='bottom', color=FG, fontsize=8.5)
    ax.set_xticks(range(3)); ax.set_xticklabels([tn for _, tn in D.VIB_TASKS], color=FG, fontsize=11)
    ax.set_title(lab, color=FG, fontsize=12, loc='left')
    if k == 0: ax.legend(frameon=False, labelcolor=FG, fontsize=10)
plt.savefig('src/static' + D.VIB_CHART, facecolor=BG); plt.close(fig)

# long chat
d = D._lng(); R = d['rows']; T = D.lng_totals(d)
fig = frame("Long chat or new chat? 30 requests in Claude Code", "API cost per request (mean of 2 runs) · Opus 5.5 · totals in the legend",
            f"{D.LNG_MEASURED} · tokensave.app/data/long-chat-vs-new-chat-cost · CC BY 4.0")
ax = fig.add_axes([0.07, 0.12, 0.9, 0.7]); style(ax)
for j, (v, nm) in enumerate(D.LNG_VARS):
    ys = [statistics.mean(r['cost_usd'] for r in R if r['variant'] == v and r['request'] == i) for i in range(1, 31)]
    tot = (T[(v, 1)]['cost'] + T[(v, 2)]['cost']) / 2
    ax.plot(range(1, 31), ys, color=C[j], lw=2.5, marker='o', ms=4, label=f"{nm}: ${tot:.2f} total")
ax.axvline(15.5, color=MUTED, ls=':', lw=1); ax.text(15.6, ax.get_ylim()[1] * 0.92, "/compact", color=MUTED, fontsize=9)
ax.set_xlabel("Request number", color=MUTED); ax.set_ylabel("USD per request", color=MUTED)
ax.legend(frameon=False, labelcolor=FG, fontsize=11, loc='upper left')
plt.savefig('src/static' + D.LNG_CHART, facecolor=BG); plt.close(fig)

# politeness
S = D.pol_sums(); O = "claude-opus-5-5"
fig = frame("Does being polite to AI cost more?", "Change vs the plain version · sum of 10 requests · Claude Opus 5.5, mean of 2 runs",
            f"{D.POL_MEASURED} · tokensave.app/data/ai-politeness-token-cost · CC BY 4.0")
for k, (key, lab) in enumerate([("prompt", "Prompt tokens"), ("cost", "Total cost (prompt + answer)")]):
    ax = fig.add_axes([0.06 + k * 0.49, 0.12, 0.42, 0.68]); style(ax)
    lvn = ["polite verb", "formal", "formal + greeting/thanks"]
    for j, (L, ln) in enumerate(D.POL_LANGS):
        vals = [(S[(L, O)][i][key] / S[(L, O)][0][key] - 1) * 100 for i in range(1, 4)]
        xs = [i + (j - 1) * 0.27 for i in range(3)]
        ax.bar(xs, vals, 0.25, color=C[j], label=ln)
        for x, v in zip(xs, vals):
            ax.text(x, v if v >= 0 else 0, f"{v:+.0f}%", ha='center', va='bottom', color=FG, fontsize=8.5)
    ax.set_xticks(range(3)); ax.set_xticklabels(lvn, color=FG, fontsize=10)
    ax.set_title(lab, color=FG, fontsize=12, loc='left'); ax.set_ylim(-20, 175)
    ax.axhline(0, color=MUTED, lw=0.8)
    if k == 0: ax.legend(frameon=False, labelcolor=FG, fontsize=10)
plt.savefig('src/static' + D.POL_CHART, facecolor=BG); plt.close(fig)
print('ok')

# coffee break
W = D.cof_waits()
fig = frame("The coffee-break tax", "Cost of the next Claude Code message after a pause · Opus 5.5 · the prompt cache lasted one hour",
            f"{D.COF_MEASURED} · tokensave.app/data/ai-coffee-break-cache-cost · CC BY 4.0")
ax = fig.add_axes([0.07, 0.12, 0.9, 0.7]); style(ax)
ws = list(W); vals = [statistics.mean(r['turn2_cost_usd'] for r in W[w]) for w in ws]
cols = [C[0] if w < 60 else C[2] for w in ws]
ax.bar(range(len(ws)), vals, 0.6, color=cols)
for i, v in enumerate(vals):
    ax.text(i, v, f"${v:.3f}", ha='center', va='bottom', color=FG, fontsize=11)
ax.set_xticks(range(len(ws))); ax.set_xticklabels([f"{w} min" for w in ws], color=FG, fontsize=11)
ax.axvline(len([w for w in ws if w < 60]) - 0.5, color=MUTED, ls=':', lw=1)
ax.text(len([w for w in ws if w < 60]) - 0.55, max(vals) * 0.9, "cache expires\nafter 1 hour", color=MUTED, fontsize=10, ha="right")
ax.set_ylabel("USD for the next message", color=MUTED)
plt.savefig('src/static' + D.COF_CHART, facecolor=BG); plt.close(fig)
print('coffee ok')
