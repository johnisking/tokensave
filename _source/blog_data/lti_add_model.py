"""Add a measured model to the Language Tax Index.
Claude:  python blog_data/lti_add_model.py claude-haiku-5-5 "Claude Haiku 5.5" Anthropic 2026-10-25 --res blog_data/lti_runs/res_claude-haiku-5-5.json
Other:   python blog_data/lti_add_model.py gemini-4 "Gemini 4" Google 2026-10-25 --counts counts.json   ({"en": 34, "ko": 48, ...} for all 41 codes)
Then add a line to LTI_HISTORY, bump LTI_VERSION and LTI_DATE in src/data_pages.py, remove the model from LTI_PENDING,
add a CHANGELOG line, run blog_data/charts_lti.py and build."""
import argparse, json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("key"); ap.add_argument("label"); ap.add_argument("family"); ap.add_argument("measured")
ap.add_argument("--res"); ap.add_argument("--counts")
a = ap.parse_args()
codes = [k for k, v in json.load(open(os.path.join(ROOT, "langdata.json"), encoding="utf-8")).items() if isinstance(v, dict) and "prompt" in v]
if a.res:
    r = json.load(open(a.res, encoding="utf-8"))
    base = r["_base"]["total"]
    counts = {c: r[c]["total"] - base for c in codes}
else:
    counts = json.load(open(a.counts, encoding="utf-8"))
missing = [c for c in codes if c not in counts]
assert not missing, f"missing languages: {missing}"
key = a.key.replace("-", "_").replace(".", "_")
json.dump(dict(key=key, label=a.label, family=a.family, measured=a.measured, counts={c: counts[c] for c in codes}),
          open(os.path.join(ROOT, "lti_models", key + ".json"), "w", encoding="utf-8"), indent=1)
print("added", key, "en =", counts["en"], "ko =", counts.get("ko"))
