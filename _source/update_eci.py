#!/usr/bin/env python3
"""Refresh src/eci_scores.json from Epoch AI's Capabilities Index CSV (CC BY 4.0).

Keeps only rows whose model name matches a model the site lists (perf.ECI_MAP).
Exit code 0 = nothing changed, 10 = scores changed (caller rebuilds and deploys).
A model whose score moves by more than 15 points in one step is not applied, only reported.
"""
import csv, io, json, os, sys, urllib.request, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "src"))
import perf

URL = "https://epoch.ai/data/eci_scores.csv"

def main():
    old = perf.load()
    req = urllib.request.Request(URL, headers={"User-Agent": "tokensave.app price/score updater"})
    text = urllib.request.urlopen(req, timeout=60).read().decode("utf-8")
    rows = []
    for r in csv.DictReader(io.StringIO(text)):
        name = (r.get("Model") or "").strip()
        if not name or not perf.wanted(name):
            continue
        try:
            rows.append([name, round(float(r["eci"]), 2), round(float(r["eci_ci_low"]), 2), round(float(r["eci_ci_high"]), 2), r["date"][:10]])
        except (KeyError, ValueError):
            continue
    if len(rows) < 10:
        print(f"Only {len(rows)} matching rows; the CSV format may have changed. Not applying.")
        return 1
    prev = {r[0]: r for r in old["rows"]}
    skipped = []
    for r in rows:
        p = prev.get(r[0])
        if p and abs(p[1] - r[1]) > 15:
            skipped.append(f"{r[0]}: {p[1]} -> {r[1]}"); r[1:4] = p[1:4]
    rows.sort(key=lambda r: -r[1])
    changed = rows != old["rows"]
    added = sorted(set(r[0] for r in rows) - set(prev))
    summary = [f"ECI rows: {len(rows)}", f"New: {', '.join(added) or 'none'}"] + [f"Skipped (big jump): {s}" for s in skipped]
    print("\n".join(summary))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        open(os.environ["GITHUB_STEP_SUMMARY"], "a").write("## Epoch Capabilities Index\n\n" + "\n".join(f"- {s}" for s in summary) + "\n")
    if not changed:
        return 0
    old.update(rows=rows, checked=datetime.date.today().isoformat())
    json.dump(old, open(perf.DATA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return 10

if __name__ == "__main__":
    sys.exit(main())
