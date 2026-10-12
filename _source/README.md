# TokenSave source

Folders starting with `_` are not published by GitHub Pages, so the source lives here.

- `src/base.html` — layout shared by every page (top bar, tool menu, language menu, FAQ, footer)
- `src/token_body.html`, `src/video_body.html`, `src/image_body.html` — the body of each tool page
- `src/i18n.py` — languages + Token Counter text; `src/i18n_video.py` — tool menu + Video Cost text; `src/i18n_image.py` — Image Cost text
- `src/token.js` — token counter logic and LLM prices; `src/video.js` — video models and per-second prices; `src/image.js` — image models and per-image prices
- `src/common.js` — shared translated-string helper and language switcher
- `build.py` — `python3 build.py` writes 81 pages into `dist/` (English at `/` and `/video`, others at `/<lang>/` and `/<lang>/video`, plus `/image` versions); copy `dist/*` to the repo root to publish

## Build settings (top of `build.py`)
- `ADSENSE_PUB` — AdSense publisher id (`ca-pub-…`). When set, every page gets the AdSense script and `ads.txt` is generated.
- `VERIFY` — Google / Naver / Bing site-verification values.
- CSS is compiled with Tailwind (`tw/`, `src/styles.css`); the first build runs `npm install` there.
- `src/static/` — favicon, touch icon and share images, copied to the site root.

## Articles (`src/blog_meta.py`, `blog_src/*.md`)
- **Revised an article?** Set `"updated": "YYYY-MM-DD"` on its entry (e.g. `CC_COST[0]["updated"] = "2026-10-12"`). The byline then shows "Updated …" (en/ko/ja wording in `build.py` `_UPD`; add a language there before using it), and `dateModified`, the sitemap `lastmod` and `llms.txt` use that date. Only set it when the content really changed.
- **Same article in several languages:** give each version the same `src` stem with a language suffix (`gogo-en`, `gogo-ko`, …). The build links them with hreflang even when they are listed in different groups.
- **Build needs:** `pip install markdown pillow playwright` and the Noto CJK fonts (`fonts-noto-cjk`) for share images.
