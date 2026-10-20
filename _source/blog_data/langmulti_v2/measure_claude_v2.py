"""Run on the PC with Claude Code: count input tokens for 10 texts x 41 languages on one Claude model.
Usage: python measure_claude_v2.py claude-haiku-5-5
Same method as dataset 2: claude -p with a fixed one-line system prompt and no MCP servers.
Input = uncached + cache read + cache write, minus the same run with a one-character message ("a").
Results are saved after every text to res_v2_<model>.json, so the script can be stopped and restarted (it resumes).
Runs 3 requests at a time."""
import json, os, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

model = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
corpus = json.load(open(os.path.join(here, "corpus_v2.json"), encoding="utf-8"))  # {lang: {"1": text, ... "10": text}}
SYS = "Reply with OK."
MCP = os.path.join(here, "mcp_empty.json")
open(MCP, "w").write('{"mcpServers": {}}')
OUT = os.path.join(here, f"res_v2_{model}.json")
CLAUDE = shutil.which("claude")


def run(text):
    for attempt in range(3):
        p = subprocess.run([CLAUDE, "-p", "--model", model, "--output-format", "json", "--system-prompt", SYS,
                            "--strict-mcp-config", "--mcp-config", MCP],
                           input=text, capture_output=True, text=True, encoding="utf-8",
                           env=dict(os.environ, CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1"), cwd=here)
        try:
            j = json.loads(p.stdout)
        except Exception:
            continue
        total = 0
        for m, u in j.get("modelUsage", {}).items():
            if model in m:
                total += u.get("inputTokens", 0) + u.get("cacheReadInputTokens", 0) + u.get("cacheCreationInputTokens", 0)
        if total:
            return total
    return None


out = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
if "_base" not in out:
    out["_base"] = [run("a") for _ in range(3)]
    json.dump(out, open(OUT, "w", encoding="utf-8"), indent=1)
print("baseline", out["_base"], flush=True)

jobs = [(lang, k, t) for lang, texts in corpus.items() for k, t in texts.items() if str(out.get(lang, {}).get(k)) in ("None", "")]
print(len(jobs), "texts to measure", flush=True)


def work(job):
    lang, k, t = job
    return lang, k, run(t)


done = 0
with ThreadPoolExecutor(3) as ex:
    for lang, k, total in ex.map(work, jobs):
        out.setdefault(lang, {})[k] = total
        done += 1
        if done % 10 == 0 or done == len(jobs):
            json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(done, "/", len(jobs), flush=True)
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", OUT)
