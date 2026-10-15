#!/usr/bin/env python3
"""Search Console + GA4 analysis from CSV exports (see _source/seo/README.md).

  python3 _source/seo/analyze.py                       # uses _source/seo/data/
  python3 _source/seo/analyze.py --prev data/prev      # also compare with an older export

Reads:
  data/gsc/Queries.csv, Pages.csv, Countries.csv, Devices.csv, Dates.csv
      (Search Console > Performance > Export > CSV, unzipped; English or Korean UI)
  data/gsc/query_page.csv   optional: query,page,clicks,impressions,ctr,position (API / Looker Studio)
  data/ga4/*.csv            any GA4 report download (Reports > Share > Download CSV)
Prints a Markdown report. Stdlib only.
"""
import argparse, csv, glob, io, math, os, re, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
# expected CTR by rounded position (rough industry curve; used only to flag outliers)
CTR_CURVE = {1: .28, 2: .15, 3: .10, 4: .07, 5: .05, 6: .04, 7: .03, 8: .025, 9: .02, 10: .018}


def num(v):
    v = (v or "").strip().replace(",", "").replace("%", "").replace(" ", "")
    try:
        return float(v)
    except ValueError:
        return None


def read_rows(path):
    """Return (header, rows) skipping GA4 '#' comment lines and blank lines."""
    raw = open(path, encoding="utf-8-sig", errors="ignore").read()
    lines = [l for l in raw.splitlines() if l.strip() and not l.startswith("#")]
    r = list(csv.reader(io.StringIO("\n".join(lines))))
    return (r[0], r[1:]) if r else ([], [])


def gsc_table(path):
    """GSC export: dimension, clicks, impressions, CTR, position (positional, so any UI language works)."""
    if not os.path.exists(path):
        return None
    _, rows = read_rows(path)
    out = []
    for r in rows:
        if len(r) < 5:
            continue
        c, i, ctr, pos = num(r[1]), num(r[2]), num(r[3]), num(r[4])
        if i is None:
            continue
        out.append({"key": r[0], "clicks": c or 0, "impr": i, "ctr": (ctr or 0) / 100, "pos": pos or 0})
    return out


def find(d, *names):
    for n in names:
        for cand in (n, n.lower()):
            p = os.path.join(d, cand)
            if os.path.exists(p):
                return p
    return os.path.join(d, names[0])


def gsc_load(d):
    return {
        "queries": gsc_table(find(d, "Queries.csv", "검색어 수.csv", "쿼리.csv", "검색어.csv")),
        "pages": gsc_table(find(d, "Pages.csv", "페이지.csv")),
        "countries": gsc_table(find(d, "Countries.csv", "국가.csv")),
        "devices": gsc_table(find(d, "Devices.csv", "기기.csv")),
        "dates": gsc_table(find(d, "Dates.csv", "차트.csv", "날짜.csv")),
    }


def min_impr(rows, floor, cap=None):
    """Impression threshold scaled to the export: the 75th percentile, at least `floor` (young sites have tiny numbers)."""
    v = sorted(r["impr"] for r in rows)
    t = max(floor, v[int(len(v) * 0.75)] if v else floor)
    return min(t, cap) if cap else t


def p_at_most(clicks, impr, exp_ctr):
    """Poisson probability of getting at most `clicks` clicks if the true CTR were the expected one for the position."""
    lam = impr * exp_ctr
    term = total = math.exp(-lam)
    for k in range(1, int(clicks) + 1):
        term *= lam / k
        total += term
    return total


def expected_ctr(pos):
    return CTR_CURVE.get(max(1, round(pos)), 0.01 if pos <= 20 else 0.003)


def fmt(n):
    return f"{n:,.0f}"


def table(head, rows):
    if not rows:
        print("_none_\n")
        return
    print("| " + " | ".join(head) + " |")
    print("|" + "---|" * len(head))
    for r in rows:
        print("| " + " | ".join(str(x).replace("|", "/") for x in r) + " |")
    print()


def short(u):
    return re.sub(r"^https?://(www\.)?tokensave\.app", "", u) or "/"


def lang_of(u):
    p = short(u).strip("/").split("/")
    return p[0] if p and 2 <= len(p[0]) <= 5 and p[0] not in ("blog", "press", "image", "video", "plans") else "en"


def gsc_report(g, prev):
    q, p = g["queries"], g["pages"]
    if not (q or p):
        print("_No Search Console export found in data/gsc/._\n")
        return
    base = p or q
    clicks, impr = sum(r["clicks"] for r in base), sum(r["impr"] for r in base)
    print("## 1. Search Console overview\n")
    rows = [["Clicks", fmt(clicks)], ["Impressions", fmt(impr)], ["CTR", f"{clicks / impr:.2%}" if impr else "-"]]
    if q:
        w = sum(r["impr"] for r in q)
        rows.append(["Avg position (impression-weighted, queries)", f"{sum(r['pos'] * r['impr'] for r in q) / w:.1f}" if w else "-"])
    if prev and (prev.get("pages") or prev.get("queries")):
        pb = prev["pages"] or prev["queries"]
        pc, pi = sum(r["clicks"] for r in pb), sum(r["impr"] for r in pb)
        rows += [["Clicks vs previous", f"{clicks - pc:+,.0f} ({(clicks - pc) / pc:+.0%})" if pc else "-"],
                 ["Impressions vs previous", f"{impr - pi:+,.0f} ({(impr - pi) / pi:+.0%})" if pi else "-"]]
    if q and p:
        qi = sum(r["impr"] for r in q)
        rows.append(["Impressions covered by the query table", f"{qi / impr:.0%} (the rest are anonymized queries)" if impr else "-"])
    table(["Metric", "Value"], rows)
    if p and impr:
        for r in p:
            if r["impr"] / impr > 0.25:
                oc, oi = clicks - r["clicks"], impr - r["impr"]
                print(f"**One page dominates:** {short(r['key'])} has {r['impr'] / impr:.0%} of all impressions "
                      f"at {r['ctr']:.2%} CTR. Without it: {fmt(oc)} clicks / {fmt(oi)} impressions, CTR {oc / oi:.2%}.\n" if oi else "")

    if g["dates"]:
        d = sorted(g["dates"], key=lambda r: r["key"])
        half = len(d) // 2
        if half >= 3:
            a, b = d[:half], d[half:]
            ca, cb = sum(r["clicks"] for r in a), sum(r["clicks"] for r in b)
            ia, ib = sum(r["impr"] for r in a), sum(r["impr"] for r in b)
            print(f"Trend inside the export ({d[0]['key']} → {d[-1]['key']}): first half {fmt(ca)} clicks / {fmt(ia)} impressions, "
                  f"second half {fmt(cb)} / {fmt(ib)}"
                  + (f" ({(cb - ca) / ca:+.0%} clicks)" if ca else "") + ".\n")

    if p:
        print("### Top pages by clicks\n")
        table(["Page", "Clicks", "Impr.", "CTR", "Pos."],
              [[short(r["key"]), fmt(r["clicks"]), fmt(r["impr"]), f"{r['ctr']:.1%}", f"{r['pos']:.1f}"]
               for r in sorted(p, key=lambda r: -r["clicks"])[:20]])
        by_lang = defaultdict(lambda: [0, 0, 0])
        for r in p:
            x = by_lang[lang_of(r["key"])]
            x[0] += r["clicks"]; x[1] += r["impr"]; x[2] += 1
        print("### By site language (from page URLs)\n")
        table(["Lang", "Pages w/ impr.", "Clicks", "Impr.", "CTR"],
              [[k, v[2], fmt(v[0]), fmt(v[1]), f"{v[0] / v[1]:.1%}" if v[1] else "-"]
               for k, v in sorted(by_lang.items(), key=lambda x: -x[1][1])])
        sect = defaultdict(lambda: [0, 0])
        for r in p:
            s = short(r["key"])
            k = "blog" if "/blog/" in s else "compare" if "/compare/" in s else "tool/home"
            sect[k][0] += r["clicks"]; sect[k][1] += r["impr"]
        table(["Section", "Clicks", "Impr."], [[k, fmt(v[0]), fmt(v[1])] for k, v in sect.items()])

    if p or q:
        print("## 2. Opportunities\n")
    if p:
        t = min_impr(p, 20)
        print(f"Page tables use pages with at least {fmt(t)} impressions (75th percentile, minimum 20).\n")
        low = []
        for r in p:
            e = expected_ctr(r["pos"])
            if r["impr"] >= t and r["pos"] <= 20:
                pr = p_at_most(r["clicks"], r["impr"], e)
                if pr < 0.10:
                    low.append((r, e, pr))
        low.sort(key=lambda x: x[2])
        print("### Pages with too few clicks for their position (title/description candidates)\n")
        print("Flagged when this few clicks would happen less than 10% of the time at a typical CTR for the position.\n")
        table(["Page", "Impr.", "Clicks", "Pos.", "Expected CTR", "Chance"],
              [[short(r["key"]), fmt(r["impr"]), fmt(r["clicks"]), f"{r['pos']:.1f}", f"{e:.0%}", f"{pr:.0%}"] for r, e, pr in low[:20]])
        striking = sorted([r for r in p if 4 <= r["pos"] <= 20 and r["impr"] >= t], key=lambda r: -r["impr"])
        print("### Pages in striking distance (position 4–20) — strengthen to reach the top 3\n")
        table(["Page", "Impr.", "Clicks", "CTR", "Pos."],
              [[short(r["key"]), fmt(r["impr"]), fmt(r["clicks"]), f"{r['ctr']:.1%}", f"{r['pos']:.1f}"] for r in striking[:20]])
        deep = sorted([r for r in p if r["pos"] > 20 and r["impr"] >= t], key=lambda r: -r["impr"])
        print("### Pages shown but ranked below 20 — content too thin for the query, or the wrong page ranks\n")
        table(["Page", "Impr.", "Pos."], [[short(r["key"]), fmt(r["impr"]), f"{r['pos']:.1f}"] for r in deep[:20]])
    if q:
        tq = min_impr(q, 5, cap=20)
        print(f"Query tables use queries with at least {fmt(tq)} impressions.\n")
        striking = sorted([r for r in q if 4 <= r["pos"] <= 20 and r["impr"] >= tq], key=lambda r: -r["impr"])
        print("### Queries in striking distance (position 4–20) — improve the ranking page\n")
        table(["Query", "Impr.", "Clicks", "CTR", "Pos."],
              [[r["key"], fmt(r["impr"]), fmt(r["clicks"]), f"{r['ctr']:.1%}", f"{r['pos']:.1f}"] for r in striking[:25]])
        low = []
        for r in q:
            e = expected_ctr(r["pos"])
            if r["impr"] >= tq and r["pos"] <= 20:
                pr = p_at_most(r["clicks"], r["impr"], e)
                if pr < 0.10:
                    low.append((r, e, pr))
        low.sort(key=lambda x: x[2])
        print("### Queries with too few clicks for their position\n")
        table(["Query", "Impr.", "Clicks", "Pos.", "Expected CTR", "Chance"],
              [[r["key"], fmt(r["impr"]), fmt(r["clicks"]), f"{r['pos']:.1f}", f"{e:.0%}", f"{pr:.0%}"] for r, e, pr in low[:20]])
        deep = sorted([r for r in q if r["pos"] > 20 and r["impr"] >= tq], key=lambda r: -r["impr"])
        print("### Demand we barely rank for (position >20) — new or deeper content\n")
        table(["Query", "Impr.", "Pos."], [[r["key"], fmt(r["impr"]), f"{r['pos']:.1f}"] for r in deep[:25]])
        if prev and prev.get("queries"):
            old = {r["key"]: r for r in prev["queries"]}
            moves = []
            for r in q:
                o = old.get(r["key"])
                if o and o["impr"] >= 20:
                    moves.append((r["clicks"] - o["clicks"], r, o))
            moves.sort(key=lambda x: x[0])
            print("### Biggest query losers vs previous export\n")
            table(["Query", "Clicks Δ", "Pos. before → now"],
                  [[r["key"], f"{d:+.0f}", f"{o['pos']:.1f} → {r['pos']:.1f}"] for d, r, o in moves[:10] if d < 0])
            print("### Biggest query winners vs previous export\n")
            table(["Query", "Clicks Δ", "Pos. before → now"],
                  [[r["key"], f"{d:+.0f}", f"{o['pos']:.1f} → {r['pos']:.1f}"] for d, r, o in moves[::-1][:10] if d > 0])

    qp = os.path.join(GSC_DIR, "query_page.csv")
    if os.path.exists(qp):
        _, rows = read_rows(qp)
        pages_for = defaultdict(list)
        for r in rows:
            if len(r) >= 4 and num(r[3]) is not None:
                pages_for[r[0]].append((short(r[1]), num(r[3])))
        cannib = [(k, v) for k, v in pages_for.items() if len(v) > 1 and sum(i for _, i in v) >= 50]
        cannib.sort(key=lambda x: -sum(i for _, i in x[1]))
        print("### Possible cannibalization (one query, several pages)\n")
        table(["Query", "Pages (impr.)"],
              [[k, "; ".join(f"{u} ({fmt(i)})" for u, i in sorted(v, key=lambda x: -x[1])[:4])] for k, v in cannib[:15]])

    if g["countries"]:
        print("## 3. Countries and devices\n")
        table(["Country", "Clicks", "Impr.", "CTR", "Pos."],
              [[r["key"], fmt(r["clicks"]), fmt(r["impr"]), f"{r['ctr']:.1%}", f"{r['pos']:.1f}"]
               for r in sorted(g["countries"], key=lambda r: -r["impr"])[:15]])
    if g["devices"]:
        table(["Device", "Clicks", "Impr.", "CTR", "Pos."],
              [[r["key"], fmt(r["clicks"]), fmt(r["impr"]), f"{r['ctr']:.1%}", f"{r['pos']:.1f}"] for r in g["devices"]])


def ga4_report(d):
    files = sorted(glob.glob(os.path.join(d, "*.csv")))
    print("## 4. Google Analytics 4\n")
    if not files:
        print("_No GA4 export found in data/ga4/._\n")
        return
    for f in files:
        head, rows = read_rows(f)
        if not head or not rows:
            continue
        numeric = [i for i in range(len(head)) if sum(num(r[i]) is not None for r in rows if i < len(r)) >= len(rows) * 0.8]
        dims = [i for i in range(len(head)) if i not in numeric]
        if not numeric:
            continue
        rows = [r for r in rows if len(r) == len(head) and not (dims and r[dims[0]].strip().lower() in ("", "grand total", "총계", "합계"))]
        sort_i = next((i for i in numeric if re.search(r"session|세션", head[i], re.I)), numeric[0])
        rows.sort(key=lambda r: -(num(r[sort_i]) or 0))
        total = sum(num(r[sort_i]) or 0 for r in rows)
        print(f"### {os.path.basename(f)} — {len(rows)} rows, sorted by “{head[sort_i]}” (total {fmt(total)})\n")
        show = dims[:2] + numeric[:6]
        out = []
        for r in rows[:20]:
            cells = []
            for i in show:
                v = num(r[i]) if i in numeric else None
                cells.append(r[i] if v is None else (f"{v:.2f}" if v < 10 and v != int(v) else fmt(v)))
            share = (num(r[sort_i]) or 0) / total if total else 0
            out.append(cells + [f"{share:.0%}"])
        table([head[i] for i in show] + ["share"], out)


GSC_DIR = os.path.join(HERE, "data", "gsc")


def main():
    global GSC_DIR
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=os.path.join(HERE, "data"))
    ap.add_argument("--prev", help="folder with an older export (same layout as data/)")
    a = ap.parse_args()
    GSC_DIR = os.path.join(a.data, "gsc")
    g = gsc_load(GSC_DIR)
    prev = gsc_load(os.path.join(a.prev, "gsc")) if a.prev else None
    print("# TokenSave Search Console + GA4 analysis\n")
    gsc_report(g, prev)
    ga4_report(os.path.join(a.data, "ga4"))


if __name__ == "__main__":
    main()
