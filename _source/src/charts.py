# -*- coding: utf-8 -*-
"""Chart images (SVG) generated at build time from the same price data as the pages.

SVG keeps the build dependency-free (also runs in the daily GitHub Action), stays sharp at any
size and is indexed by Google Images. Labels inside the charts are Latin-only (model names,
numbers) so they render the same for every language; alt text and captions are localized by
the caller.
"""
import html

esc = lambda s: html.escape(str(s), quote=True)

BG, PANEL, FG, MUTED, GRID = "#18181b", "#27272a", "#f4f4f5", "#a1a1aa", "#3f3f46"
C_A, C_B = "#a78bfa", "#34d399"          # two models being compared
C_IN, C_OUT, C_HI = "#60a5fa", "#a78bfa", "#fbbf24"
FONT = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"
W = 560

def _money(x):
    if x >= 100: return f"${x:,.0f}"
    if x >= 1: return f"${x:,.2f}"
    return f"${x:.4f}".rstrip("0") if x >= 0.0001 else "$0"

def _wrap(svg_body, h, title, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" '
            f'font-family="{FONT}"><title>{esc(title)}</title><desc>{esc(desc)}</desc>'
            f'<rect width="{W}" height="{h}" rx="16" fill="{BG}"/>{svg_body}'
            f'<text x="{W - 24}" y="{h - 18}" text-anchor="end" font-size="13" font-weight="600" fill="{MUTED}">tokensave.app</text></svg>\n')

def compare_chart(a, b, rows, checked):
    """rows: [(label, cost_a, cost_b)] cost per 1,000 requests. Bars are scaled within each row,
    because the workloads differ by 100x and a shared scale would hide the small ones."""
    title = f"{a['name']} vs {b['name']}: API cost per 1,000 requests"
    out = [f'<text x="24" y="42" font-size="21" font-weight="700" fill="{FG}">{esc(a["name"])} vs {esc(b["name"])}</text>',
           f'<text x="24" y="66" font-size="14" fill="{MUTED}">API cost per 1,000 requests (USD) · prices checked {esc(checked)}</text>']
    lx = 24
    for name, col in ((a["name"], C_A), (b["name"], C_B)):
        out.append(f'<rect x="{lx}" y="84" width="14" height="14" rx="3" fill="{col}"/>'
                   f'<text x="{lx + 20}" y="96" font-size="14" fill="{FG}">{esc(name)}</text>')
        lx += 34 + len(name) * 8
    y, bar_x, bar_w = 124, 24, W - 24 - 24 - 90
    for label, ca, cb in rows:
        mx = max(ca, cb) or 1
        out.append(f'<text x="24" y="{y + 14}" font-size="15" font-weight="600" fill="{FG}">{esc(label)}</text>')
        for k, (v, col) in enumerate(((ca, C_A), (cb, C_B))):
            by = y + 24 + k * 24
            w = max(3, v / mx * bar_w)
            lo = v <= min(ca, cb) and ca != cb
            out.append(f'<rect x="{bar_x}" y="{by}" width="{w:.1f}" height="18" rx="4" fill="{col}"/>'
                       f'<text x="{bar_x + w + 8:.1f}" y="{by + 14}" font-size="14" font-weight="{700 if lo else 400}" fill="{FG}">{_money(v)}</text>')
        y += 24 + 48 + 18
    out.append(f'<text x="24" y="{y + 4}" font-size="12" fill="{MUTED}">Bars compare the two models within each workload.</text>'
               f'<text x="24" y="{y + 22}" font-size="12" fill="{MUTED}">Standard list prices, no caching or batch discounts.</text>')
    h = y + 62
    desc = "; ".join(f"{l}: {a['name']} {_money(ca)}, {b['name']} {_money(cb)}" for l, ca, cb in rows)
    return _wrap("".join(out), h, title, desc)

def price_chart(models, highlight, checked):
    """Input and output price per 1M tokens, one shared scale, highlighted rows in amber."""
    title = "AI model API prices per 1M tokens (input and output, USD)"
    mx = max(m["out"] for m in models)
    name_w, bar_x = 150, 172
    bar_w = W - bar_x - 24 - 52
    out = [f'<text x="24" y="42" font-size="21" font-weight="700" fill="{FG}">API price per 1M tokens (USD)</text>',
           f'<text x="24" y="66" font-size="14" fill="{MUTED}">Standard list prices · checked {esc(checked)}</text>']
    lx = 24
    for name, col in (("Input", C_IN), ("Output", C_OUT)):
        out.append(f'<rect x="{lx}" y="84" width="14" height="14" rx="3" fill="{col}"/>'
                   f'<text x="{lx + 20}" y="96" font-size="14" fill="{FG}">{name}</text>')
        lx += 90
    # light vertical grid at round values
    step = 10 if mx > 30 else 5 if mx > 10 else 1
    y0, row_h = 120, 42
    y_end = y0 + row_h * len(models)
    v = step
    while v <= mx:
        gx = bar_x + v / mx * bar_w
        out.append(f'<line x1="{gx:.1f}" y1="{y0 - 4}" x2="{gx:.1f}" y2="{y_end}" stroke="{GRID}" stroke-width="1"/>'
                   f'<text x="{gx:.1f}" y="{y_end + 16}" text-anchor="middle" font-size="12" fill="{MUTED}">${v:g}</text>')
        v += step
    for i, m in enumerate(models):
        y = y0 + i * row_h
        hi = m["id"] in highlight
        if hi:
            out.append(f'<rect x="12" y="{y - 2}" width="{W - 24}" height="{row_h - 4}" rx="6" fill="{PANEL}"/>')
        out.append(f'<text x="{name_w + 8}" y="{y + 21}" text-anchor="end" font-size="15" font-weight="{700 if hi else 400}" '
                   f'fill="{C_HI if hi else FG}">{esc(m["name"])}</text>')
        for k, (val, col) in enumerate(((m["inp"], C_IN), (m["out"], C_OUT))):
            by = y + 2 + k * 16
            w = max(2, val / mx * bar_w)
            label = f"${val:.2f}" if val < 1 else f"${val:g}"
            out.append(f'<rect x="{bar_x}" y="{by}" width="{w:.1f}" height="13" rx="3" fill="{col}"/>'
                       f'<text x="{bar_x + w + 6:.1f}" y="{by + 12}" font-size="13" fill="{FG}">{label}</text>')
    h = y_end + 56
    desc = "; ".join(f"{m['name']}: ${m['inp']:g} input, ${m['out']:g} output" for m in models)
    return _wrap("".join(out), h, title, desc)

def figure(src, alt, caption, w, h):
    return (f'<figure class="chart-fig"><img class="chart" src="{src}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async" />'
            f'<figcaption>{esc(caption)}</figcaption></figure>')

def size_of(svg):
    import re
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
    return int(m.group(1)), int(m.group(2))
