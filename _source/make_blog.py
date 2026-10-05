#!/usr/bin/env python3
"""Render blog_src/<tag>.md -> src/blog/<tag>.html (body fragments used by build.py).

Run after editing an article:  pip install markdown && python3 _source/make_blog.py
"""
import os, re
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DIR, OUT_DIR = os.path.join(ROOT, "blog_src"), os.path.join(ROOT, "src", "blog")
os.makedirs(OUT_DIR, exist_ok=True)

for f in sorted(os.listdir(SRC_DIR)):
    if not f.endswith(".md"):
        continue
    md = open(os.path.join(SRC_DIR, f), encoding="utf-8").read()
    out = markdown.markdown(md, extensions=["tables", "fenced_code"])
    size = ("1200", "630") if ("blog-chatgpt-pro-tiers" in out or "blog-mistral-francais" in out or "blog-prompt-polski" in out) else ("960", "1430")
    def _img(m, size=size):
        w, h = size
        src = re.search(r'src="([^"]+)"', m.group(0))
        p = os.path.join(ROOT, "src", "static", src.group(1).lstrip("/")) if src else ""
        if p and os.path.exists(p):
            try:
                from PIL import Image
                w, h = Image.open(p).size
            except Exception:
                pass
        return m.group(0).replace("<img ", f'<img loading="lazy" width="{w}" height="{h}" ', 1)
    out = re.sub(r'<img [^>]*>', _img, out)
    out = re.sub(r'<a href="(https?://(?!tokensave\.app)[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', out)
    out = out.replace("<table>", '<div class="overflow-x-auto"><table>').replace("</table>", "</table></div>")
    out = out.replace("{{", "{ {")  # never collide with template placeholders
    open(os.path.join(OUT_DIR, f[:-3] + ".html"), "w", encoding="utf-8").write(out + "\n")
    print("wrote", f[:-3] + ".html")
