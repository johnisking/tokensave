"""Add a copyable BibTeX entry under "How to cite" on every /data/ page (2026-10-23).

Reads the page's own Dataset JSON-LD (name, identifier DOI, datePublished, url) so the entry
always matches the page. Pages without a DOI get a url-only entry.
"""
import glob, html, json, os, re

BTN = ('class="not-prose text-xs font-semibold rounded-md border border-violet-500/40 bg-violet-500/10 '
       'px-2.5 py-1 text-violet-200 hover:bg-violet-500/20"')     # same as src/data_pages.py


def _dataset(s):
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            d = json.loads(raw)
        except ValueError:
            continue
        for g in (d.get("@graph", [d]) if isinstance(d, dict) else d):
            if isinstance(g, dict) and g.get("@type") == "Dataset":
                return g
    return None


def _bib_escape(t):
    return t.replace("\\", "").replace("{", "").replace("}", "").replace("%", r"\%").replace("&", r"\&").replace("_", r"\_")


def bibtex(ds, slug):
    doi = ""
    ident = ds.get("identifier")
    if isinstance(ident, str) and "10." in ident:
        doi = ident[ident.index("10."):]
    year = (ds.get("datePublished") or "2026")[:4]
    key = "tokensave_" + re.sub(r"[^a-z0-9]+", "_", slug.lower()).strip("_") + "_" + year
    lines = [f"@misc{{{key},", "  author    = {{TokenSave}},",
             f"  title     = {{{_bib_escape(ds.get('name', slug))}}},", f"  year      = {{{year}}},"]
    if doi:
        lines += ["  publisher = {Zenodo},", f"  doi       = {{{doi}}},", f"  url       = {{https://doi.org/{doi}}},"]
    else:
        lines += [f"  url       = {{{ds.get('url', '')}}},"]
    lines += ["  note      = {Dataset, CC BY 4.0}", "}"]
    return "\n".join(lines)


def apply(dist):
    n = 0
    for f in glob.glob(os.path.join(dist, "data", "*.html")):
        s = open(f, encoding="utf-8").read()
        if 'id="cite-bibtex"' in s or 'id="cite"' not in s:
            continue
        ds = _dataset(s)
        if not ds:
            continue
        i = s.index('data-copy="cite-text"', s.index('id="cite"'))
        j = s.index("</div>", s.index("</div>", i) + 6) + 6       # end of the button div, then of the citation box
        block = ('\n      <p class="mt-4 text-sm text-zinc-400">BibTeX</p>\n'
                 '      <div class="not-prose bg-zinc-950/70 border border-zinc-800 rounded-xl p-4">\n'
                 f'        <pre id="cite-bibtex" class="text-xs text-zinc-200 whitespace-pre-wrap break-words font-mono m-0">{html.escape(bibtex(ds, os.path.basename(f)[:-5]))}</pre>\n'
                 f'        <div class="mt-3"><button type="button" data-copy="cite-bibtex" {BTN}>Copy BibTeX</button></div>\n'
                 '      </div>')
        s = s[:j] + block + s[j:]
        open(f, "w", encoding="utf-8").write(s)
        n += 1
    return n
