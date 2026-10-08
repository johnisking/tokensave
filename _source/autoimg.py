#!/usr/bin/env python3
"""Explanatory images for blog articles, made from the article's own text.

For every article with fewer than 3 images:
  * a cover (1200x630, also used as og:image) from the article title
  * up to 3 section cards: a table section becomes a table card, a list section a points card
Text comes straight from the markdown (no new numbers), so every language is localized.
Images go to src/static/, markdown links are inserted into blog_src/*.md,
and src/autoimg.json maps article path -> cover file (build.py uses it for og:image).

  python3 autoimg.py                # all articles
  python3 autoimg.py --only gogo-ko # some md names
  python3 autoimg.py --dry          # render to scratch dir, don't touch md
"""
import os, re, sys, json, html, unicodedata
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "src"))
import blog_meta as M

STATIC = os.path.join(ROOT, "src", "static")
FD = os.path.join(ROOT, "src", "fonts")
MAPF = os.path.join(ROOT, "src", "autoimg.json")

SCRIPT = {'ar': 'arabic', 'fa': 'arabic', 'ur': 'arabic', 'he': 'hebrew', 'th': 'thai',
          'bn': 'bengali', 'hi': 'devanagari', 'mr': 'devanagari', 'gu': 'gujarati',
          'pa': 'gurmukhi', 'kn': 'kannada', 'ml': 'malayalam', 'ta': 'tamil', 'te': 'telugu'}
CJK = {'ja': 'Noto Sans CJK JP', 'ko': 'Noto Sans CJK KR', 'zh-CN': 'Noto Sans CJK SC', 'zh-TW': 'Noto Sans CJK TC'}
RTL = {'ar', 'fa', 'ur', 'he'}
SKIP_H = re.compile(r'FAQ|Q&A|Source|Sources|출처|자주|참고|よくある|出典|参考|常见|常見|来源|來源|資料|Джерел|Джерела|Часті|Źródła|Często|Bronnen|Veelgestelde|Quellen|Häufig|Fuentes|Preguntas|Fontes|Perguntas|Fonti|Domande|Kaynak|Sık|Nguồn|Câu hỏi|Sumber|Pertanyaan|Источник|Частые|स्रोत|सवाल|प्रश्न|مصادر|الأسئلة|Read more|더 읽|関連|Related', re.I)

def groups():
    G = [M.BLOG, M.PRO, M.MISTRAL_FR, M.PROMPT_PL, M.GUIDES] + [getattr(M, n) for n in (
        'CC_COST CC_LIMITS CC_SAVE CMP GPT6 API_CMP TPW COUNT CHLIM CXLIM CMAX AISITE GEM4 RANK GAME GAME_HOWTO '
        'DEVLOG1 DEVLOG2 CHEAP CTOK SUBS GPT61 DS41 AGCMP GOPLUS RBX KO6 JA6 RBX_JA TW6 GCREV FREEPAID INDIECOST MUSE13').split() if hasattr(M, n)]
    G += list(M.EU6) + list(M.NL6) + list(M.RBX_PL)
    return [b for g in G for b in g]

def ascii_slug(s, n=48):
    s = s.replace('ı', 'i').replace('İ', 'I')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()
    return s[:n].strip('-')

def inline(s):
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s)
    s = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', s)
    s = s.replace('`', '')
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'\1', s)
    return s.strip()

def plain(s):
    return re.sub(r'<[^>]+>', '', html.unescape(inline(s)))

def cut(s, n):
    p = plain(s)
    return s if len(p) <= n else html.escape(p[:n - 1].rstrip()) + '…'

def sections(md):
    """[(heading, start_line_index_of_heading, body_lines)]"""
    lines = md.split('\n')
    out, cur = [], None
    for i, l in enumerate(lines):
        if l.startswith('## '):
            cur = [l[3:].strip(), i, []]
            out.append(cur)
        elif l.startswith('# '):
            cur = None
        elif cur is not None:
            cur[2].append(l)
    return lines, out

def parse_table(body):
    rows, started = [], False
    for l in body:
        if l.strip().startswith('|'):
            started = True
            cells = [c.strip() for c in l.strip().strip('|').split('|')]
            if all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c):
                continue
            rows.append(cells)
        elif started:
            break
    return rows if len(rows) >= 3 else None

def parse_list(body):
    items = []
    for l in body:
        m = re.match(r'\s{0,3}(?:[-*]|\d+[.)])\s+(.*)', l)
        if m:
            items.append(m.group(1))
        elif items and l.strip() and not l.startswith(' '):
            if len(items) >= 3:
                break
            items = []
    return items if len(items) >= 3 else None

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#0b0a10;color:#f4f2fb}
.card{width:1200px;background:#14121c;padding:56px 60px 44px;position:relative}
.kick{font-size:20px;font-weight:700;color:#a78bfa;letter-spacing:.5px;margin-bottom:14px}
h2{font-size:44px;font-weight:900;line-height:1.25;letter-spacing:-.5px}
.foot{display:flex;justify-content:space-between;font-size:20px;color:#7d7891;margin-top:30px}
.foot b{color:#a78bfa}
table{width:100%;border-collapse:separate;border-spacing:0;margin-top:34px;border:2px solid #2d2a3d;border-radius:18px;overflow:hidden}
th{background:#2a2145;color:#ddd3ff;font-weight:800;text-align:start;padding:16px 18px;vertical-align:bottom}
td{padding:15px 18px;border-top:1px solid #26233a;color:#e7e4f3;vertical-align:top;font-variant-numeric:tabular-nums}
tr:nth-child(even) td{background:#191626}
td:first-child{font-weight:800;color:#fff}
td b,th b{color:#ffd166}
.more{font-size:20px;color:#7d7891;margin-top:12px}
.pts{display:flex;flex-direction:column;gap:16px;margin-top:34px}
.pt{display:flex;gap:20px;align-items:flex-start;background:#1c1928;border:2px solid #2d2a3d;border-radius:18px;padding:20px 24px}
.n{flex:none;width:46px;height:46px;border-radius:12px;background:#a78bfa;color:#14121c;font-weight:900;font-size:24px;display:flex;align-items:center;justify-content:center}
.pt .t{font-size:27px;line-height:1.45;color:#ece9f7}
.pt .t b{color:#ffd166}
#cover{width:1200px;height:630px;padding:64px 70px;background:radial-gradient(circle at 88% 8%,#4c2f8f 0,#1a1430 38%,#100e17 72%);overflow:hidden}
#cover .ring{position:absolute;inset-inline-end:-120px;bottom:-160px;width:520px;height:520px;border-radius:50%;border:56px solid rgba(167,139,250,.13)}
#cover .tiles{position:absolute;inset-inline-end:70px;top:150px;display:grid;grid-template-columns:repeat(4,46px);gap:10px;opacity:.9}#cover .tiles i{display:block;height:46px;border-radius:10px;background:rgba(167,139,250,.18)}#cover .tiles i.h{background:#a78bfa}#cover .tiles i.y{background:#ffd166}
#cover .brand{display:inline-flex;align-items:center;gap:12px;font-size:26px;font-weight:800;color:#c4b5fd}
#cover .dot{width:18px;height:18px;border-radius:5px;background:#a78bfa}
#cover h1{text-wrap:balance;font-weight:900;line-height:1.18;letter-spacing:-1px;margin-top:40px;max-width:800px}
#cover h1 .a{color:#ffd166}
#cover .sec{position:absolute;inset-inline-start:70px;bottom:56px;display:flex;gap:12px;flex-wrap:wrap;max-width:900px}
#cover .chip{font-size:21px;font-weight:700;color:#d9d3ef;border:2px solid #3a3452;border-radius:999px;padding:7px 18px;background:rgba(20,18,28,.6)}
"""

def font_css(tag):
    fam = []
    if tag in CJK:
        fam.append(f'"{CJK[tag]}"')
    if tag in SCRIPT:
        s = SCRIPT[tag]
        fam.append('"Scr"')
        face = (f'@font-face{{font-family:"Scr";src:url("file://{FD}/{s}-400.ttf");font-weight:400 600}}'
                f'@font-face{{font-family:"Scr";src:url("file://{FD}/{s}-700.ttf");font-weight:700 900}}')
    else:
        face = ''
    face += (f'@font-face{{font-family:"Base";src:url("file://{FD}/base-400.ttf");font-weight:400 600}}'
             f'@font-face{{font-family:"Base";src:url("file://{FD}/base-700.ttf");font-weight:700 900}}')
    fam = ['"Base"'] + fam + ['"Noto Sans CJK KR"', 'sans-serif'] if tag not in CJK else fam + ['"Base"', 'sans-serif']
    return face + f'body{{font-family:{",".join(fam)}}}' + ('body{word-break:keep-all}' if tag == 'ko' else '')

FOOT_L = {'ko': '무료 AI 토큰·비용 계산기', 'ja': '無料のAIトークン・費用計算機', 'zh-CN': '免费 AI Token 与费用计算器',
          'zh-TW': '免費 AI Token 與費用計算機', 'en': 'Free AI token & cost calculators'}

TILES = ['', 'h', '', '', 'h', 'y', 'h', '', '', 'h', 'h', 'y', '', '', 'h', '']
def cover_html(b, chips):
    t = html.escape(b['title'])
    m = re.match(r'(.+?[:：?？])\s*(.+)$', b['title'])
    if m and len(m.group(1)) > 6:
        t = f'{html.escape(m.group(1))}<br><span class="a">{html.escape(m.group(2))}</span>'
    n = len(b['title'])
    wide = b['tag'] in CJK
    size = (62 if n <= 20 else 54 if n <= 30 else 48 if n <= 42 else 42) if wide else (66 if n <= 30 else 58 if n <= 46 else 50 if n <= 62 else 44 if n <= 80 else 40)
    if b['tag'] in SCRIPT:
        size = int(size * 0.86)
    ch = ''.join(f'<span class="chip">{c}</span>' for c in chips)
    return f'<div id="cover" class="card"><div class="ring"></div><div class="tiles">'+''.join('<i class="%s"></i>' % c for c in TILES)+f'</div><div class="brand"><span class="dot"></span>tokensave.app</div><h1 style="font-size:{size}px">{t}</h1><div class="sec">{ch}</div></div>'

def foot(b):
    return f'<div class="foot"><span>{html.escape(FOOT_L.get(b["tag"], ""))}</span><b>tokensave.app</b></div>'

def table_html(b, head, rows):
    ncol = min(6, max(len(r) for r in rows))
    rows = [(r + [''] * ncol)[:ncol] for r in rows]
    hdr, data = rows[0], rows[1:]
    more = ''
    if len(data) > 10:
        more = f'<div class="more">+{len(data) - 10}</div>'
        data = data[:10]
    longest = max(len(plain(c)) for r in rows for c in r)
    fs = 26 if ncol <= 3 and longest < 40 else 23 if ncol <= 4 else 20
    lim = 70 if ncol <= 3 else 48 if ncol <= 4 else 34
    th = ''.join(f'<th>{cut(inline(c), lim)}</th>' for c in hdr)
    tb = ''.join('<tr>' + ''.join(f'<td>{cut(inline(c), lim)}</td>' for c in r) + '</tr>' for r in data)
    return (f'<div class="card"><div class="kick">{html.escape(short_title(b))}</div><h2>{inline(head)}</h2>'
            f'<table style="font-size:{fs}px"><tr>{th}</tr>{tb}</table>{more}{foot(b)}</div>')

def list_html(b, head, items):
    items = items[:6]
    pts = ''
    for i, it in enumerate(items, 1):
        pts += f'<div class="pt"><div class="n">{i}</div><div class="t">{point(it)}</div></div>'
    return (f'<div class="card"><div class="kick">{html.escape(short_title(b))}</div><h2>{inline(head)}</h2>'
            f'<div class="pts">{pts}</div>{foot(b)}</div>')

def first_sentence(s):
    m = re.match(r'(.+?[.!?。！？])(\s|$)', s)
    return m.group(1) if m else s

def point(it):
    h = inline(it)
    m = re.match(r'(<b>.+?</b>)\s*[:：.。—-]?\s*(.*)$', h)
    if m:
        lead, rest = m.group(1), m.group(2)
        rest = first_sentence(rest) if rest else ''
        room = 120 - len(plain(lead))
        if len(plain(rest)) > room:
            pr = plain(rest)[:room]
            pr = pr.rsplit(' ', 1)[0] if ' ' in pr else pr
            rest = html.escape(pr.rstrip(',;:')) + '…'
        return f'{lead} {rest}'.strip()
    t = first_sentence(h)
    if len(plain(t)) > 120:
        words = plain(t)[:118].rsplit(' ', 1)[0] if ' ' in plain(t)[:118] else plain(t)[:118]
        return html.escape(words) + '…'
    return t

def short_title(b):
    t = re.split(r'[:：|]', b['title'])[0].strip()
    return t if len(t) <= 70 else t[:68] + '…'

def page(tag, inner):
    d = 'rtl' if tag in RTL else 'ltr'
    return f'<!doctype html><html lang="{tag}" dir="{d}"><head><meta charset="utf-8"><style>{CSS}{font_css(tag)}</style></head><body>{inner}</body></html>'

def plan(b, md):
    """Return (cover?, [(section_heading, heading_line, kind, payload)])"""
    n_img = len(re.findall(r'!\[', md))
    lines, secs = sections(md)
    cands = []
    for h, li, body in secs:
        if SKIP_H.search(h):
            continue
        if any('![' in l for l in body):
            continue
        t = parse_table(body)
        if t:
            cands.append((0, h, li, 'table', t))
            continue
        l = parse_list(body)
        if l:
            cands.append((1, h, li, 'list', l))
    has_top_img = '![' in md.split('\n## ')[0]
    want = max(0, 4 - n_img - (0 if has_top_img else 1))
    pick = [x for x in os.environ.get('AUTOIMG_PICK', '').split('|') if x]
    if pick:
        cands = [c for c in cands if any(x in c[1] for x in pick)]
        want = len(cands)
    tables = [c for c in cands if c[0] == 0][:2 if not pick else 9]
    lists = [c for c in cands if c[0] == 1]
    chosen = (tables + lists)[:min(3 if not pick else 9, want)]
    chosen.sort(key=lambda c: c[2])
    return (not has_top_img), [(h, li, k, p) for _, h, li, k, p in chosen], secs

def main():
    args = sys.argv[1:]
    dry = '--dry' in args
    only = args[args.index('--only') + 1].split(',') if '--only' in args else None
    outdir = args[args.index('--out') + 1] if '--out' in args else STATIC
    os.makedirs(outdir, exist_ok=True)
    mp = json.load(open(MAPF)) if os.path.exists(MAPF) else {}
    jobs = []
    for b in groups():
        src = b.get('src', b['tag'])
        if only and src not in only:
            continue
        mdp = os.path.join(ROOT, 'blog_src', src + '.md')
        md = open(mdp, encoding='utf-8').read()
        if '--covers' in args:
            if b['tag'] in RTL and b['path'] in mp:
                _, secs = sections(md)
                chips = [cut(inline(h), 30) for h, _, _ in secs if not SKIP_H.search(h)][:3]
                jobs.append((b, mdp, md, [('cover', None, mp[b['path']], b['title'], cover_html(b, chips))]))
            continue
        if len(re.findall(r'!\[', md)) >= 3 or 'autoimg' in md:
            continue
        cover, chosen, secs = plan(b, md)
        if not cover and not chosen:
            continue
        slug = b['path'].rstrip('/').split('/')[-1]
        tg = b['tag'].lower()
        base = f'{slug}-{tg}' if not slug.endswith('-' + tg) else slug
        items = []
        if cover:
            chips = [cut(inline(h), 30) for h, _, _ in secs if not SKIP_H.search(h)][:3]
            items.append(('cover', None, f'{base}.jpg', b['title'], cover_html(b, chips)))
        used = set()
        for h, li, k, p in chosen:
            hs = ascii_slug(plain(h), 40)
            name = f'{slug}-{hs}-{tg}.jpg' if hs and len(hs) > 5 else f'{base}-{len(items) + 1}.jpg'
            if name in used:
                name = name[:-4] + f'-{len(items)}.jpg'
            used.add(name)
            alt_bits = plain(h)
            if k == 'table':
                alt_bits += ': ' + ', '.join(plain(c) for c in p[0] if plain(c))[:110]
            else:
                alt_bits += ': ' + '; '.join(plain(x).split(':')[0] for x in p[:3])[:110]
            inner = table_html(b, h, p) if k == 'table' else list_html(b, h, p)
            items.append(('sec', li, name, alt_bits, inner))
        jobs.append((b, mdp, md, items))
    print('articles', len(jobs), 'images', sum(len(j[3]) for j in jobs))
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={'width': 1200, 'height': 800}, device_scale_factor=1)
        for b, mdp, md, items in jobs:
            for kind, li, name, alt, inner in items:
                pg.set_content(page(b['tag'], inner), wait_until='load')
                pg.evaluate('document.fonts.ready')
                tmp = os.path.join(outdir, '_tmp.png')
                pg.locator('.card').first.screenshot(path=tmp)
                Image.open(tmp).convert('RGB').save(os.path.join(outdir, name), 'JPEG', quality=82, optimize=True, progressive=True)
            os.remove(os.path.join(outdir, '_tmp.png')) if items else None
            if dry or '--covers' in args:
                continue
            lines = md.split('\n')
            for kind, li, name, alt, inner in sorted(items, key=lambda x: -(x[1] if x[1] is not None else -1)):
                altx = alt.replace('[', '(').replace(']', ')').replace('\n', ' ')
                tag_line = f'![{altx}](/{name})'
                if kind == 'cover':
                    lines = [tag_line, ''] + lines
                    mp[b['path']] = name
                else:
                    lines[li + 1:li + 1] = ['', tag_line]
            new = '\n'.join(lines)
            new = re.sub(r'\n{3,}', '\n\n', new)
            open(mdp, 'w', encoding='utf-8').write(new.rstrip('\n') + '\n<!-- autoimg -->\n')
            print('ok', os.path.basename(mdp), [i[2] for i in items])
        br.close()
    if not dry:
        json.dump(mp, open(MAPF, 'w'), ensure_ascii=False, indent=0, sort_keys=True)

if __name__ == '__main__':
    main()
