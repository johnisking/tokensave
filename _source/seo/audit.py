#!/usr/bin/env python3
"""Technical SEO audit of the published site (repo root HTML files).

  python3 _source/seo/audit.py            # prints a Markdown report
  python3 _source/seo/audit.py > _source/seo/reports/audit-$(date +%F).md

Checks every page for title/description length, canonical, hreflang, h1, og:image,
img alt, noindex, sitemap membership, duplicate titles/descriptions and pages
that nothing links to. Stdlib only.
"""
import collections, html, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SITE = "https://tokensave.app/"
CJK = {"ko", "ja", "zh-cn", "zh-tw"}
VERIFY = re.compile(r"^(google|yandex)[0-9a-f_]+\.html$")


def pages():
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if not d.startswith(("_", "."))]
        for f in fn:
            if f.endswith(".html") and not VERIFY.match(f) and f != "404.html":
                yield os.path.relpath(os.path.join(dp, f), ROOT)


def url(rel):
    r = rel[:-5]
    if r == "index" or r.endswith("/index"):
        r = r[:-5]
    return SITE + r


def lang(rel):
    top = rel.split("/")[0]
    return top if "/" in rel and len(top) <= 5 and top not in ("blog", "press") else "en"


def main():
    sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
    locs = {l.rstrip("/") for l in re.findall(r"<loc>(.*?)</loc>", sm)}
    issues = collections.defaultdict(list)
    titles, descs = collections.defaultdict(list), collections.defaultdict(list)
    inlinks, words, all_rels = collections.Counter(), {}, list(pages())
    for rel in all_rels:
        s = open(os.path.join(ROOT, rel), encoding="utf-8", errors="ignore").read()
        head = s[: s.find("</head>")] if "</head>" in s else s[:20000]
        u, lg = url(rel), lang(rel)
        cjk = lg in CJK
        t = re.search(r"<title>(.*?)</title>", head, re.S)
        t = html.unescape(t.group(1).strip()) if t else ""
        d = re.search(r'<meta name="description" content="(.*?)"', head)
        d = html.unescape(d.group(1)) if d else ""
        c = re.search(r'<link rel="canonical" href="(.*?)"', head)
        noindex = re.search(r'<meta name="robots" content="[^"]*noindex', head)
        if noindex:
            issues["noindex (check it is intended)"].append(rel)
            continue
        titles[t].append(rel)
        descs[d].append(rel)
        tmax, tmin, dmin, dmax = (40, 12, 40, 110) if cjk else (65, 25, 70, 165)
        if not t:
            issues["missing <title>"].append(rel)
        elif len(t) > tmax:
            issues["title too long (>65 chars; >40 for CJK)"].append(f"{rel} ({len(t)})")
        elif len(t) < tmin:
            issues["title too short (<25 chars; <12 for CJK)"].append(f"{rel}: {t}")
        if not d:
            issues["missing meta description"].append(rel)
        elif len(d) < dmin:
            issues["meta description too short (<70; <40 for CJK)"].append(f"{rel} ({len(d)})")
        elif len(d) > dmax:
            issues["meta description too long (>165; >110 for CJK)"].append(f"{rel} ({len(d)})")
        if not c:
            issues["missing canonical"].append(rel)
        elif c.group(1).rstrip("/") != u.rstrip("/"):
            issues["canonical points elsewhere"].append(f"{rel} -> {c.group(1)}")
        if u.rstrip("/") not in locs:
            issues["indexable page not in sitemap.xml"].append(rel)
        h1 = len(re.findall(r"<h1[\s>]", s))
        if h1 != 1:
            issues[f"h1 count is {h1}"].append(rel)
        if "og:image" not in head:
            issues["missing og:image"].append(rel)
        noalt = [i for i in re.findall(r"<img\b[^>]*>", s) if not re.search(r'alt="[^"]+"', i)]
        if noalt:
            issues["<img> without alt"].append(f"{rel} ({len(noalt)})")
        body = re.sub(r"<script.*?</script>|<style.*?</style>|<header.*?</header>|<footer.*?</footer>|<[^>]+>", " ", s, flags=re.S)
        words[rel] = len(body) // 2 if (cjk or lg == "th") else len(body.split())
        for h in re.findall(r'href="(?:https://tokensave\.app)?(/[^"#?]*)"', s):
            inlinks[h.rstrip("/") or "/"] += 1
    for t, v in titles.items():
        if t and len(v) > 1:
            issues["duplicate title"].append(f'"{t}" x{len(v)}: {", ".join(v[:4])}')
    for d, v in descs.items():
        if d and len(v) > 1:
            issues["duplicate meta description"].append(f'x{len(v)}: {", ".join(v[:4])}')
    for rel in all_rels:
        path = "/" + url(rel)[len(SITE):]
        if inlinks[path.rstrip("/") or "/"] == 0 and rel not in issues["noindex (check it is intended)"]:
            issues["orphan page (no internal link)"].append(rel)
    sitemap_missing = [l for l in locs if not any(l == url(r).rstrip("/") for r in all_rels)]
    for l in sitemap_missing:
        issues["sitemap URL with no page (404)"].append(l)

    print(f"# Technical SEO audit — {len(all_rels)} pages, {len(locs)} sitemap URLs\n")
    print("| Check | Pages |\n|---|---|")
    for k, v in sorted(issues.items(), key=lambda x: -len(x[1])):
        print(f"| {k} | {len(v)} |")
    if not issues:
        print("| (no issues) | 0 |")
    for k, v in sorted(issues.items(), key=lambda x: -len(x[1])):
        print(f"\n## {k} ({len(v)})\n")
        for e in v[:15]:
            print(f"- {e}")
        if len(v) > 15:
            print(f"- … and {len(v) - 15} more")
    thin = sorted(words.items(), key=lambda x: x[1])[:10]
    print("\n## Thinnest indexable pages (approx. words)\n")
    for rel, n in thin:
        print(f"- {rel}: {n}")


if __name__ == "__main__":
    sys.exit(main())
