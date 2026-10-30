"""Blog images for the edge-case post (run from _source/): cover + pass-rate chart + cost chart, per language."""
import json, sys, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from PIL import Image
BG = '#0f0f12'; FG = '#e4e4e7'; MUTED = '#a1a1aa'; GRID = '#27272a'; H = '#38bdf8'; O = '#a78bfa'; RED = '#f87171'
D = json.load(open('blog_data/edgecases/dataset/claude-edge-case-prompts.json', encoding='utf-8'))
S = D['stats']['all']; C = ['C0', 'C1', 'C2', 'C3']; hm, om = 'claude-haiku-5-5', 'claude-opus-5-5'
T = {
 'ko': dict(font='Noto Sans CJK KR', conds=['기본', 'effort high', '엣지 케이스\n프롬프트', '엣지 케이스\n+ 테스트 읽기'],
            cover_t='클로드 코드에 "엣지 케이스 챙겨"\n한 줄 넣었더니', cover_big='비용만 +134%', cover_sub='하이쿠 기준 · 통과율은 4점도 안 움직였다 · 504회 실측 · 실제 버그 21개',
            p_title='신고문에 없는 경우를 통과한 비율', p_sub='버그별 평균 · 하이쿠 5.5와 오퍼스 5.5 · 조건마다 63회',
            c_title='1회 API 비용', c_sub='클로드 코드가 알려 준 API 정가 환산 · 조건마다 63회', haiku='하이쿠 5.5', opus='오퍼스 5.5', src='tokensave.app/data · CC BY 4.0'),
}

def fig_base(w=12, h=6.3):
    f = plt.figure(figsize=(w, h), dpi=100); f.patch.set_facecolor(BG); return f

def save(f, path):
    tmp = path + '.png'; f.savefig(tmp, facecolor=BG); plt.close(f)
    Image.open(tmp).convert('RGB').save(path, 'JPEG', quality=86, optimize=True)
    import os; os.remove(tmp)

def bars(lang, key, title, sub, fmt, out, pct):
    t = T[lang]; plt.rcParams['font.family'] = t['font']
    f = fig_base(); ax = f.add_axes([0.07, 0.15, 0.9, 0.62]); ax.set_facecolor(BG); w = 0.38
    for i, (m, lab, col) in enumerate(((hm, t['haiku'], H), (om, t['opus'], O))):
        v = [S[m][c][key] for c in C]; xs = [j + (i - 0.5) * w for j in range(4)]
        ax.bar(xs, v, w * 0.92, color=col, label=lab)
        top = 1 if pct else max(S[om][c][key] for c in C)
        for x, y, c in zip(xs, v, C):
            s = fmt(y)
            if not pct and c != 'C0': s += f"\n+{round(S[m][c]['cost_change_vs_C0'] * 100)}%"
            ax.text(x, y + top * 0.015, s, ha='center', va='bottom', color=FG, fontsize=11, linespacing=1.2)
    ax.set_xticks(range(4)); ax.set_xticklabels(t['conds'], color=FG, fontsize=12)
    ax.tick_params(colors=MUTED, length=0); ax.yaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
    for s in ax.spines.values(): s.set_visible(False)
    if pct:
        ax.set_ylim(0, 1.12); ax.set_yticks([0, .25, .5, .75, 1]); ax.set_yticklabels(['0', '25%', '50%', '75%', '100%'], color=MUTED)
    else:
        mx = max(S[om][c][key] for c in C); ax.set_ylim(0, mx * 1.28); ticks = [0, .2, .4, .6, .8, 1.0]
        ax.set_yticks([x for x in ticks if x <= mx * 1.28]); ax.set_yticklabels([f'${x:.2f}' for x in ticks if x <= mx * 1.28], color=MUTED)
    ax.legend(loc='upper left', facecolor=BG, edgecolor=GRID, labelcolor=FG, fontsize=11, ncol=2)
    f.text(0.04, 0.9, title, fontsize=21, fontweight='bold', color=FG); f.text(0.04, 0.845, sub + ' · ' + t['src'], fontsize=11, color=MUTED)
    save(f, out)

def cover(lang, out):
    t = T[lang]; plt.rcParams['font.family'] = t['font']
    f = fig_base(12, 6.3)
    f.text(0.06, 0.70, t['cover_t'], fontsize=36, fontweight='bold', color=FG, va='center', linespacing=1.35)
    f.text(0.06, 0.40, t['cover_big'], fontsize=64, fontweight='bold', color=RED, va='center')
    f.text(0.06, 0.20, t['cover_sub'], fontsize=17, color=MUTED, va='center')
    f.text(0.06, 0.08, 'TokenSave · ' + t['src'], fontsize=12, color=MUTED, va='center')
    save(f, out)

for lang in sys.argv[1:] or ['ko']:
    t = T[lang]; base = f'src/static/claude-edge-case-prompt-{lang}'
    cover(lang, base + '.jpg')
    bars(lang, 'unreported_pass_rate', t['p_title'], t['p_sub'], lambda v: f'{v*100:.0f}%', base + '-2.jpg', True)
    bars(lang, 'mean_cost_usd', t['c_title'], t['c_sub'], lambda v: f'${v:.3f}' if v < 0.1 else f'${v:.2f}', base + '-3.jpg', False)
    print(lang, 'ok')
