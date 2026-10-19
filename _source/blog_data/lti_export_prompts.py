"""Export the 41 index prompts to lti_prompts.json, to copy to the PC that runs Claude Code."""
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(ROOT, "langdata.json"), encoding="utf-8"))
prompts = {k: v["prompt"] for k, v in d.items() if isinstance(v, dict) and "prompt" in v}
json.dump(prompts, open(os.path.join(ROOT, "lti_prompts.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(prompts), "prompts -> lti_prompts.json")
