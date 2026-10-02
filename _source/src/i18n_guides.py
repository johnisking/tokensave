# -*- coding: utf-8 -*-
"""Localized 'how to use / how it works' sections, FAQ answer 4 and article snippets for the
38 non-English languages without hand-written guides (en/ko/ja have src/guides/...).

src/guides_i18n/<tag>.json   translated strings with {placeholders} for UI labels and numbers
src/guides_i18n/_context.json  per-language ratio, saving %, decimal mark, translator support, UI labels
"""
import html, json, os, re

_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guides_i18n")
CTX = json.load(open(os.path.join(_DIR, "_context.json"), encoding="utf-8"))
LNAME = {"zh-CN": "Chinese", "zh-TW": "Traditional Chinese"}
_W = '    <section class="prose-ts mt-12 max-w-3xl mx-auto bg-zinc-900/40 border border-zinc-800 rounded-2xl p-6 sm:p-8">'


def strings(tag):
    return json.load(open(os.path.join(_DIR, tag + ".json"), encoding="utf-8"))


def values(tag):
    c = CTX[tag]
    ro = f"{c['ro']:.2f}"
    if c["decimal"] == ",":
        ro = ro.replace(".", ",")
    return dict(c["ui"], ro=ro, save=str(c["save"]), Lname=LNAME.get(tag, c["english_name"]))


def fill(tag, key):
    s = strings(tag)[key]
    v = values(tag)
    return re.sub(r"\{(\w+)\}", lambda m: v.get(m.group(1), m.group(0)), s)


def md_html(text):
    t = html.escape(text, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)


def _li(tag, keys):
    return "\n".join(f"        <li>{md_html(fill(tag, k))}</li>" for k in keys)


def guide(tag, tool, links=()):
    s, sup = strings(tag), CTX[tag]["supported"]
    h = lambda k: md_html(s[k])
    rel = ""
    if links:
        rel = f'      <h2>{h("h_rel")}</h2>\n      <ul>' + "".join(f'<li><a href="{u}">{html.escape(t)}</a></li>' for u, t in links) + "</ul>\n"
    if tool == "token":
        use = _li(tag, ["g_t1", "g_t2", "g_t3" if sup else "g_t3x", "g_t4", "g_t5", "g_t6"])
        how = _li(tag, ["g_h1", "g_h2", "g_h3", "g_h4"])
        tail = (f'      <h2>{h("h_tr")}</h2>\n      <ul>\n' + _li(tag, ["g_r1", "g_r2", "g_r3", "g_r4"]) + "\n      </ul>\n") if sup else \
               (f'      <h2>{h("h_tip")}</h2>\n      <p>{md_html(fill(tag, "g_tipx"))}</p>\n')
        body = (f'      <h2 style="margin-top:0">{h("h_use")}</h2>\n      <ol>\n{use}\n      </ol>\n'
                f'      <h2>{h("h_how")}</h2>\n      <ul>\n{how}\n      </ul>\n{tail}{rel}')
    else:
        p = {"video": ("v_", ["v_1", "v_2", "v_3"], ["v_h1", "v_h2", "v_h3", "v_h4"], ["v_tip"]),
             "image": ("i_", ["i_1", "i_2", "i_3"], ["i_h1", "i_h2", "i_h3"], ["i_tip"]),
             "plans": ("p_", ["p_1", "p_2", "p_3"], ["p_h"], ["p_n"]),
             "agents": ("a_", ["a_1", "a_2", "a_3"], ["a_h"], ["a_tip"])}[tool]
        _, use, how, tip = p
        how_html = (f"      <p>{md_html(fill(tag, how[0]))}</p>\n" if len(how) == 1 else "      <ul>\n" + _li(tag, how) + "\n      </ul>\n")
        body = (f'      <h2 style="margin-top:0">{h("h_use")}</h2>\n      <ol>\n{_li(tag, use)}\n      </ol>\n'
                f'      <h2>{h("h_how")}</h2>\n{how_html}'
                f'      <h2>{h("h_tip")}</h2>\n      <p>{md_html(fill(tag, tip[0]))}</p>\n{rel}')
    return f"{_W}\n{body}    </section>\n"


def a4(tag):
    return fill(tag, "a4" if CTX[tag]["supported"] else "a4x").replace("**", "")
