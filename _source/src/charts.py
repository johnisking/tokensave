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
CHART_EN = dict(s_title="AI model capability vs API price", s_sub="Epoch Capabilities Index (Epoch AI, CC BY) vs blended price per 1M tokens",
                s_x="Blended API price per 1M tokens (USD, log scale) → cheaper on the left", s_y="Capability (ECI) ↑",
                s_front="Best value (frontier)", s_other="Other",
                t_title="Most capable AI models", t_sub="Epoch Capabilities Index with 90% range (Epoch AI, CC BY)",
                c_title="Cheapest AI models", c_sub="Blended API price per 1M tokens (log scale), with capability score")

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

def scatter_chart(points, checked, tx=None):
    tx = dict(CHART_EN, **(tx or {}))
    """Capability (y) vs blended price (x, log scale). points: [{id,name,x,y,front}].
    Frontier points are joined by a line; labels are placed greedily to avoid overlaps."""
    import math
    WS, HS = 760, 680
    L, R, T, B = 70, 24, 100, 70
    pw, ph = WS - L - R, HS - T - B
    xs = [p["x"] for p in points]; ys = [p["y"] for p in points]
    def nice_up(v):
        e = 10 ** math.floor(math.log10(v))
        return next(m * e for m in (1, 2, 5, 10) if m * e >= v * 1.15)
    x0 = 10 ** math.floor(math.log10(min(xs))); x1 = nice_up(max(xs))
    y0 = math.floor((min(ys) - 2) / 10) * 10; y1 = math.ceil((max(ys) + 2) / 5) * 5
    X = lambda v: L + (math.log10(v) - math.log10(x0)) / (math.log10(x1) - math.log10(x0)) * pw
    Y = lambda v: T + (1 - (v - y0) / (y1 - y0)) * ph
    out = [f'<text x="24" y="40" font-size="24" font-weight="700" fill="{FG}">{esc(tx["s_title"])}</text>',
           f'<text x="24" y="68" font-size="15" fill="{MUTED}">{esc(tx["s_sub"])} · {esc(checked)}</text>']
    # grid + axes
    d = x0
    while d <= x1 * 1.0001:
        for m in (1, 2, 5):
            v = d * m
            if x0 <= v <= x1 * 1.0001:
                gx = X(v)
                out.append(f'<line x1="{gx:.1f}" y1="{T}" x2="{gx:.1f}" y2="{T + ph}" stroke="{GRID}" stroke-width="{1 if m == 1 else 0.5}"/>'
                           f'<text x="{gx:.1f}" y="{T + ph + 20}" text-anchor="middle" font-size="14" fill="{MUTED}">${v:g}</text>')
        d *= 10
    for v in range(int(y0), int(y1) + 1, 5):
        gy = Y(v)
        out.append(f'<line x1="{L}" y1="{gy:.1f}" x2="{L + pw}" y2="{gy:.1f}" stroke="{GRID}" stroke-width="0.5"/>'
                   f'<text x="{L - 8}" y="{gy + 4:.1f}" text-anchor="end" font-size="14" fill="{MUTED}">{v}</text>')
    out.append(f'<text x="{L + pw / 2:.0f}" y="{HS - 22}" text-anchor="middle" font-size="15" fill="{MUTED}">{esc(tx["s_x"])}</text>'
               f'<text x="18" y="{T + ph / 2:.0f}" transform="rotate(-90 18 {T + ph / 2:.0f})" text-anchor="middle" font-size="15" fill="{MUTED}">{esc(tx["s_y"])}</text>')
    fr = sorted((p for p in points if p.get("front")), key=lambda p: p["x"])
    if len(fr) > 1:
        path = " ".join(f"{X(p['x']):.1f},{Y(p['y']):.1f}" for p in fr)
        out.append(f'<polyline points="{path}" fill="none" stroke="{C_B}" stroke-width="2" stroke-dasharray="6 4" opacity="0.8"/>')
    boxes = []
    def free(bx):
        x, y, w, h = bx
        if x < L or x + w > WS - 4 or y < T - 4 or y + h > T + ph:
            return False
        return all(x + w < a or a + c < x or y + h < b or b + e < y for a, b, c, e in boxes)
    for p in points:  # reserve dots first so labels avoid them
        boxes.append((X(p["x"]) - 8, Y(p["y"]) - 8, 16, 16))
    for p in sorted(points, key=lambda p: -p["y"]):
        cx, cy = X(p["x"]), Y(p["y"])
        col = C_B if p.get("front") else C_A
        out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="8" fill="{col}" stroke="{BG}" stroke-width="2"/>')
        fs = 15
        w = len(p["name"]) * 8.1 + 4
        cands = [(12, 5, "start"), (-12, 5, "end"), (12, -9, "start"), (-12, -9, "end"), (12, 19, "start"), (-12, 19, "end"),
                 (0, -14, "middle"), (0, 26, "middle")]
        for dy in (-28, 40, -42, 54, -56, 68):  # farther slots get a leader line
            cands += [(12, dy, "start"), (-12, dy, "end"), (0, dy, "middle")]
        for dx, dy, anchor in cands:
            bx = cx + dx if anchor == "start" else cx + dx - w if anchor == "end" else cx - w / 2
            box = (bx, cy + dy - fs + 2, w, fs + 2)
            if free(box):
                boxes.append(box)
                lx = cx + dx if anchor != "middle" else cx
                if abs(dy) > 27:
                    ly = cy + dy - fs / 2 + 2 if dy > 0 else cy + dy + 3
                    ly = cy + dy - fs + 3 if dy > 0 else cy + dy + 3
                    out.append(f'<line x1="{cx:.1f}" y1="{cy + (8 if dy > 0 else -8):.1f}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="{MUTED}" stroke-width="1" opacity="0.7"/>')
                out.append(f'<text x="{lx:.1f}" y="{cy + dy:.1f}" text-anchor="{anchor}" font-size="{fs}" '
                           f'font-weight="{700 if p.get("front") else 400}" fill="{FG}">{esc(p["name"])}</text>')
                break
    out.append(f'<circle cx="{WS - 262}" cy="{84}" r="7" fill="{C_B}"/><text x="{WS - 250}" y="89" font-size="15" fill="{FG}">{esc(tx["s_front"])}</text>'
               f'<circle cx="{WS - 84}" cy="{84}" r="7" fill="{C_A}"/><text x="{WS - 72}" y="89" font-size="15" fill="{FG}">{esc(tx["s_other"])}</text>')
    desc = "; ".join(f"{p['name']}: ECI {p['y']:.1f}, ${p['x']:.2f} per 1M tokens" for p in sorted(points, key=lambda p: -p["y"]))
    body = "".join(out)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WS} {HS}" width="{WS}" height="{HS}" role="img" font-family="{FONT}">'
            f'<title>{esc(tx["s_title"])}</title><desc>{esc(desc)}</desc>'
            f'<rect width="{WS}" height="{HS}" rx="16" fill="{BG}"/>{body}'
            f'<text x="{WS - 24}" y="{HS - 6}" text-anchor="end" font-size="12" font-weight="600" fill="{MUTED}">tokensave.app</text></svg>\n')

def rank_chart(points, mode, checked, tx=None):
    """mode 'top': capability dot plot with 90% range, sorted by ECI.
    mode 'cheap': blended price bars (log scale), sorted cheapest first, ECI shown."""
    import math
    tx = dict(CHART_EN, **(tx or {}))
    WS = 760; rowh = 32; T = 100; L = 210; R = 120
    pts = sorted(points, key=(lambda p: -p["y"]) if mode == "top" else (lambda p: p["x"]))
    HS = T + rowh * len(pts) + 56
    pw = WS - L - R
    if mode == "top":
        lo = math.floor((min(p["lo"] for p in pts) - 1) / 10) * 10; hi = math.ceil((max(p["hi"] for p in pts) + 1) / 5) * 5
        X = lambda v: L + (v - lo) / (hi - lo) * pw
        ticks = [(v, f"{v}") for v in range(int(lo), int(hi) + 1, 10)]
        title, sub = tx["t_title"], tx["t_sub"]
    else:
        x0 = 10 ** math.floor(math.log10(min(p["x"] for p in pts))); x1 = 10 ** math.ceil(math.log10(max(p["x"] for p in pts)))
        X = lambda v: L + (math.log10(v) - math.log10(x0)) / (math.log10(x1) - math.log10(x0)) * pw
        ticks = []
        d = x0
        while d <= x1 * 1.0001:
            for m in (1, 2, 5):
                if x0 <= d * m <= x1 * 1.0001: ticks.append((d * m, f"${d * m:g}"))
            d *= 10
        title, sub = tx["c_title"], tx["c_sub"]
    out = [f'<text x="24" y="40" font-size="24" font-weight="700" fill="{FG}">{esc(title)}</text>',
           f'<text x="24" y="68" font-size="15" fill="{MUTED}">{esc(sub)} · {esc(checked)}</text>']
    for v, lab in ticks:
        gx = X(v)
        out.append(f'<line x1="{gx:.1f}" y1="{T - 8}" x2="{gx:.1f}" y2="{T + rowh * len(pts)}" stroke="{GRID}" stroke-width="0.6"/>'
                   f'<text x="{gx:.1f}" y="{T + rowh * len(pts) + 20}" text-anchor="middle" font-size="14" fill="{MUTED}">{lab}</text>')
    for i, p in enumerate(pts):
        cy = T + i * rowh + rowh / 2
        col = C_B if p.get("front") else C_A
        out.append(f'<text x="{L - 12}" y="{cy + 4:.1f}" text-anchor="end" font-size="15" font-weight="{700 if p.get("front") else 400}" fill="{FG}">{esc(p["name"])}</text>')
        if mode == "top":
            out.append(f'<line x1="{X(p["lo"]):.1f}" y1="{cy:.1f}" x2="{X(p["hi"]):.1f}" y2="{cy:.1f}" stroke="{col}" stroke-width="4" opacity="0.35" stroke-linecap="round"/>'
                       f'<circle cx="{X(p["y"]):.1f}" cy="{cy:.1f}" r="7.5" fill="{col}"/>'
                       f'<text x="{X(p["hi"]) + 8:.1f}" y="{cy + 5:.1f}" font-size="14" fill="{FG}">{p["y"]:.1f}</text>')
        else:
            w = max(3, X(p["x"]) - L)
            out.append(f'<rect x="{L}" y="{cy - 10:.1f}" width="{w:.1f}" height="20" rx="4" fill="{col}"/>'
                       f'<text x="{L + w + 8:.1f}" y="{cy + 5:.1f}" font-size="14" fill="{FG}">${p["x"]:.2f} · ECI {p["y"]:.0f}</text>')
    desc = "; ".join(f"{p['name']}: ECI {p['y']:.1f}, ${p['x']:.2f}" for p in pts)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WS} {HS}" width="{WS}" height="{HS}" role="img" font-family="{FONT}">'
            f'<title>{esc(title)}</title><desc>{esc(desc)}</desc><rect width="{WS}" height="{HS}" rx="16" fill="{BG}"/>{"".join(out)}'
            f'<text x="{WS - 24}" y="{HS - 10}" text-anchor="end" font-size="12" font-weight="600" fill="{MUTED}">tokensave.app</text></svg>\n')
