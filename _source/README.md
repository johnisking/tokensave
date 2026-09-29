# TokenSave source

Folders starting with `_` are not published by GitHub Pages, so the source lives here.

- `src/base.html` — layout shared by every page (top bar, tool menu, language menu, FAQ, footer)
- `src/token_body.html`, `src/video_body.html` — the body of each tool page
- `src/i18n.py` — languages + Token Counter text; `src/i18n_video.py` — tool menu + Video Cost text
- `src/token.js` — token counter logic and LLM prices; `src/video.js` — video models and per-second prices
- `src/common.js` — shared translated-string helper and language switcher
- `build.py` — `python3 build.py` writes 42 pages into `dist/` (English at `/` and `/video`, others at `/<lang>/` and `/<lang>/video`); copy `dist/*` to the repo root to publish
