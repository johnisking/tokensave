# New-model measurement routine

Goal: every time a major model ships, publish our own measurements within 1–2 days, so TokenSave builds a dated record that cannot be copied after the fact.

## Trigger
A new model from Anthropic, OpenAI or Google that people will use for chat or coding (check the ChatGPT/Claude/Gemini release notes and Artificial Analysis' changelog once a day). Queue it in `LTI_PENDING` in `src/data_pages.py` the day it ships.

## What to measure (in this order, stop when time runs out)
1. **Language Tax Index** (about 30 minutes, no cost on a plan)
   - Does the model have a new tokenizer? If its English count for the index prompt equals an existing column, add a note to the history instead of a new column.
   - Claude: on the PC, `python lti_measure_claude.py <model-id>` (copy `blog_data/lti_prompts.json` and the script into `Downloads\agent-test\lti\`), then copy `res_<model>.json` back to `blog_data/lti_runs/`.
   - Gemini: Google AI Studio token counter, subtract the start token (1), save `{code: tokens}` for the 41 codes.
   - GPT: tiktoken with the new encoding, if OpenAI publishes one.
   - `python blog_data/lti_add_model.py <key> "<label>" <family> <date> --res ...` (or `--counts ...`).
2. **Coding task cost** (about 1 hour): the brick-breaker prompt from dataset 8/12/13, 5 runs, default settings, same scripts (`build_combined.py`, `check_works.py`). Add as a new condition or a new version of the matching dataset.
3. **Optional**: effort levels (dataset 7), web search (datasets 9/10), only if the model changes how these work.

## Publish
- `src/data_pages.py`: bump `LTI_VERSION` (new column = minor, e.g. 1.1; new text set or method = major, 2.0), set `LTI_DATE`, add a line to `LTI_HISTORY`, remove the model from `LTI_PENDING`, add a dated line at the top of `CHANGELOG`.
- `python3 blog_data/charts_lti.py`, build, show the user the page and the history line, deploy only after "올려".
- Zenodo: new version of the matching dataset (user presses Publish). HF/Kaggle/GitHub mirrors as usual.
- Request indexing for /data/language-tax-index and the changed dataset page.
- One short post where it fits (X thread, DOU only with no TokenSave link).

## Rules
- Only our own measurements. No news summaries.
- Same prompts and method as the previous version, or say clearly in the history what changed.
- Percent, not multipliers. Dates on everything.
