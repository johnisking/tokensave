# TokenSave source

Folders starting with `_` are not published by GitHub Pages, so the source lives here.

- `src/template.html` — page layout shared by every language
- `src/i18n.py` — all UI text for the 21 languages
- `src/app.js` — calculator logic and model prices (update prices here)
- `build.py` — `python3 build.py` regenerates the pages into `dist/`; copy `dist/*` to the repo root to publish
