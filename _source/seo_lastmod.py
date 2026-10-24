"""Sitemap lastmod from real content changes (2026-10-23).

The text of each page's <main> (without <nav>, scripts, styles and the footer) is hashed. seo/lastmod.json keeps
{url: {"hash": ..., "date": ...}}. A page keeps its date while its text is unchanged and gets today's date when the
text changes, so menu or template edits no longer move every lastmod at once.
seed(): one-time fill from the git history of the published files (oldest commit with the current text)."""
import datetime, hashlib, html, json, os, re, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(ROOT, "seo", "lastmod.json")
BASE = "https://tokensave.app"
REL_H = ["More articles", "다른 글", "関連記事", "Más artículos", "Autres articles", "Więcej artykułów", "Weitere Artikel", "Mais artigos",
         "Altri articoli", "Інші статті", "Другие статьи", "更多文章"]


def text_of(src):
    m, e = src.find("<main"), src.find("</main>")
    s = src[m:e] if m >= 0 and e > m else src
    s = re.sub(r"<(script|style|nav|footer)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<h2>(?:%s)</h2>\s*<ul>.*?</ul>" % "|".join(map(re.escape, REL_H)), " ", s, flags=re.S)  # rotating "More articles" list
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"\s+", " ", s).strip()


def digest(src):
    return hashlib.sha1(text_of(src).encode("utf-8")).hexdigest()[:16]


def file_for(dist, url):
    p = url[len(BASE):] if url.startswith(BASE) else url
    p = p.lstrip("/")
    for c in (p + ".html", os.path.join(p, "index.html"), p) if p else ("index.html",):
        f = os.path.join(dist, c)
        if os.path.isfile(f):
            return f
    return None


def load():
    try:
        return json.load(open(MANIFEST, encoding="utf-8"))
    except Exception:
        return {}


def apply(dist, today=None):
    today = today or datetime.date.today().isoformat()
    man = load()
    path = os.path.join(dist, "sitemap.xml")
    sm = open(path, encoding="utf-8").read()

    def fix(m):
        url, old = m.group(1), m.group(2)
        f = file_for(dist, url)
        if not f:
            return m.group(0)
        h = digest(open(f, encoding="utf-8").read())
        e = man.get(url)
        if e and e["hash"] == h:
            d = e["date"]
        else:
            d = today if e else old
            man[url] = {"hash": h, "date": d}
        return f"<loc>{url}</loc>\n    <lastmod>{d}</lastmod>"

    sm = re.sub(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", fix, sm)
    open(path, "w", encoding="utf-8").write(sm)
    # data pages: fill the "Updated" date and JSON-LD dateModified (placeholder kept out of the hash, see build.DATA_BYLINE)
    for f in sorted(os.listdir(os.path.join(dist, "data"))):
        if not f.endswith(".html"):
            continue
        fp = os.path.join(dist, "data", f)
        src = open(fp, encoding="utf-8").read()
        if "__DATA_UPDATED__" in src:
            e = man.get(f"{BASE}/data/{f[:-5]}")
            open(fp, "w", encoding="utf-8").write(src.replace("__DATA_UPDATED__", e["date"] if e else today))
    json.dump(man, open(MANIFEST, "w", encoding="utf-8"), indent=0, sort_keys=True)


def seed(dist, repo):
    """Date of each URL = date of the oldest commit whose published file has the same text as now."""
    man = {}
    sm = open(os.path.join(dist, "sitemap.xml"), encoding="utf-8").read()
    for url, old in re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", sm):
        f = file_for(dist, url)
        if not f:
            continue
        h = digest(open(f, encoding="utf-8").read())
        rel = os.path.relpath(f, dist)
        log = subprocess.run(["git", "log", "--format=%H %cs", "--", rel], cwd=repo, capture_output=True, text=True).stdout.split("\n")
        date = None
        for line in log:
            if not line.strip():
                continue
            sha, d = line.split()
            src = subprocess.run(["git", "show", f"{sha}:{rel}"], cwd=repo, capture_output=True, text=True).stdout
            if src and digest(src) == h:
                date = d
            else:
                break
        man[url] = {"hash": h, "date": date or old}
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    json.dump(man, open(MANIFEST, "w", encoding="utf-8"), indent=0, sort_keys=True)
    return man
