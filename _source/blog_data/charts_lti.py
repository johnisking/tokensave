import json, sys, os, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
sys.path.insert(0, 'src')
import data_pages as D
BG='#0f0f12'; FG='#e4e4e7'; MUTED='#a1a1aa'; GRID='#27272a'
rows = D._lti_rows(); sm = D._lti_summary(rows)
order = ["gemini_4_argon", "gemini", "gpt", "claude55", "claude45", "cl100k"]
labels = [sm[k]["label"] for k in order]
fig, ax = plt.subplots(figsize=(12, 6.2), dpi=100); fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
for y, k in enumerate(order):
    vals = sorted(r[k + "_tax"] for r in rows if r["code"] != "en")
    p10, p90 = vals[int(len(vals) * .1)], vals[int(len(vals) * .9) - 1]
    col = '#a78bfa' if sm[k]["current"] else MUTED
    ax.plot([p10, p90], [y, y], color=col, alpha=.35, lw=10, solid_capstyle='round')
    for v in vals:
        ax.plot(v, y, '|', color=FG, ms=10, alpha=.35)
    ax.plot(sm[k]["median"], y, 'o', color=col, ms=13)
    ax.text(sm[k]["median"], y - 0.33, f"median +{sm[k]['median']}%", ha='center', color=FG, fontsize=11, fontweight='bold')
ax.set_yticks(range(len(order))); ax.set_yticklabels(labels, fontsize=11, color=FG); ax.invert_yaxis()
ax.set_xlim(0, 300); ax.set_xticks([0, 50, 100, 150, 200, 250, 300]); ax.set_xticklabels(['0', '+50%', '+100%', '+150%', '+200%', '+250%', '+300%'])
ax.tick_params(axis='x', colors=MUTED); ax.tick_params(axis='y', length=0)
for s in ax.spines.values(): s.set_visible(False)
ax.grid(axis='x', color=GRID); ax.set_axisbelow(True)
fig.text(0.02, 0.95, f"TokenSave Language Tax Index v{D.LTI_VERSION}", fontsize=18, fontweight='bold', color=FG)
fig.text(0.02, 0.905, "Extra tokens vs English for the same text · dot = median of 40 languages, band = middle 80%, ticks = each language (axis cut at +300%)", fontsize=10, color=MUTED)
fig.text(0.02, 0.02, f"{D.LTI_DATE} · tokensave.app/data/language-tax-index · CC BY 4.0", fontsize=9.5, color=MUTED)
plt.subplots_adjust(left=0.25, right=0.97, top=0.84, bottom=0.1)
plt.savefig('src/static/language-tax-index-chart.png', facecolor=BG); plt.close(fig)
print('ok')
