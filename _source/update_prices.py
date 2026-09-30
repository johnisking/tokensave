#!/usr/bin/env python3
"""Refresh LLM token prices in src/llm_prices.json from LiteLLM's public price list.

Exit code 0 = nothing changed, 10 = prices changed (caller rebuilds and deploys).
Safety: a price that moves more than 3x up or down in one step is NOT applied, only reported.
Writes a Markdown report to $GITHUB_STEP_SUMMARY when running in GitHub Actions.
"""
import json, os, sys, urllib.request, datetime, re

ROOT = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(ROOT, "src", "llm_prices.json")
URL = "https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json"
FAMILIES = re.compile(r"^(gpt-\d[\w.\-]*|claude-(opus|sonnet|haiku)-[\d\-]+|gemini-\d[\w.\-]*)$")

def main():
    data = json.load(open(PATH, encoding="utf-8"))
    remote = json.load(urllib.request.urlopen(URL, timeout=60))
    changed, skipped, missing = [], [], []
    ctx_changed = False
    for mid, m in data["models"].items():
        r = remote.get(m["key"])
        if not r or not r.get("input_cost_per_token"):
            missing.append(mid); continue
        if r.get("max_input_tokens") and r["max_input_tokens"] != m.get("ctx"):
            m["ctx"] = r["max_input_tokens"]; ctx_changed = True
        new_in = round(r["input_cost_per_token"] * 1e6, 4)
        new_out = round((r.get("output_cost_per_token") or 0) * 1e6, 4)
        if (new_in, new_out) == (m["in"], m["out"]):
            continue
        ratios = [a / b for a, b in ((new_in, m["in"]), (new_out, m["out"])) if a and b]
        if not new_in or not new_out or any(x > 3 or x < 1 / 3 for x in ratios):
            skipped.append(f"{mid}: {m['in']}/{m['out']} -> {new_in}/{new_out}"); continue
        changed.append(f"{mid}: {m['in']}/{m['out']} -> {new_in}/{new_out}")
        m["in"], m["out"] = new_in, new_out

    # Models in the same families that the site does not list yet (for a human/Claude to review)
    known = {m["key"] for m in data["models"].values()} | set(data.get("seen", []))
    new_models = sorted(k for k, v in remote.items()
                        if "/" not in k and FAMILIES.match(k) and k not in known
                        and v.get("mode") == "chat" and v.get("litellm_provider") in ("openai", "anthropic", "gemini", "vertex_ai-language-models")
                        and not re.search(r"\d{4}-?\d{2}-?\d{2}|preview-\d|-mini-|audio|realtime|search|transcribe|tts", k))

    if new_models:
        data["seen"] = sorted(set(data.get("seen", [])) | set(new_models))
    if changed:
        data["checked"] = datetime.date.today().isoformat()
    if changed or new_models or ctx_changed:
        json.dump(data, open(PATH, "w", encoding="utf-8"), indent=2)
        open(PATH, "a").write("\n")

    lines = ["## LLM price check", "",
             f"- Changed: {len(changed)}", *[f"  - {c}" for c in changed],
             f"- Skipped (moved more than 3x, check by hand): {len(skipped)}", *[f"  - {s}" for s in skipped],
             f"- Not found in LiteLLM: {', '.join(missing) or 'none'}",
             f"- New models in LiteLLM (not on the site yet): {', '.join(new_models[:30]) or 'none'}"]
    report = "\n".join(lines)
    print(report)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        open(os.environ["GITHUB_STEP_SUMMARY"], "a").write(report + "\n")
    sys.exit(10 if changed or ctx_changed else 0)

if __name__ == "__main__":
    main()
