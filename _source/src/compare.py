# -*- coding: utf-8 -*-
"""Model-vs-model API cost comparison pages (/compare/<a>-vs-<b>) and the /compare/ hub.

Prices come from token.js (model list, names, tokenizer ratios) overridden by src/llm_prices.json
(refreshed daily), so every page stays current on each rebuild. Only hand-picked pairs people
actually compare are generated; each page is computed from the two models' own numbers.
"""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
esc = lambda s: html.escape(str(s), quote=True)

PROVIDER = {"openai": "OpenAI", "claude": "Anthropic", "gemini": "Google"}

def load_models(llm):
    src = open(os.path.join(HERE, "token.js"), encoding="utf-8").read()
    models, prov = {}, None
    for line in src.splitlines():
        m = re.match(r"\s*(openai|claude|gemini|other):\s*\[", line)
        if m:
            prov = m.group(1)
        m = re.search(r"id:\s*'([^']+)'.*?(?:group:\s*'([^']+)'.*?)?name:\s*'([^']+)'.*?in:\s*([\d.]+).*?out:\s*([\d.]+).*?ratio:\s*([\d.]+)", line)
        if m and prov:
            mid, group, name, i, o, r = m.groups()
            models[mid] = dict(id=mid, name=name, maker=PROVIDER.get(prov) or {"Moonshot": "Moonshot AI"}.get(group, group),
                               inp=float(i), out=float(o), ratio=float(r), ctx=None)
    for mid, v in llm["models"].items():
        if mid in models:
            models[mid].update(inp=v["in"], out=v["out"], ctx=v.get("ctx"))
    return models

PAIRS = [
    ("gpt-6-sol", "claude-sonnet-5-5"), ("gpt-6-astra", "claude-opus-5-5"), ("gpt-6-astra", "claude-fable-5-1"),
    ("gpt-6-astra", "gemini-4-argon"), ("gemini-4-argon", "claude-opus-5-5"), ("gemini-4-argon", "claude-fable-5-1"),
    ("gemini-4-argon", "gemini-3-1-pro"), ("gemini-3-1-pro", "gpt-6-sol"), ("gemini-3-1-pro", "claude-sonnet-5-5"),
    ("gpt-6-sol", "gpt-6-astra"), ("gpt-6-luna", "gpt-6-sol"), ("gpt-6-luna", "gemini-3-8-flash"),
    ("gpt-6-luna", "claude-haiku-4-5"), ("gemini-3-8-flash", "claude-haiku-4-5"), ("claude-sonnet-5-5", "claude-opus-5-5"),
    ("claude-haiku-4-5", "claude-sonnet-5-5"), ("claude-opus-5-5", "claude-fable-5-1"), ("deepseek-v4-pro", "gpt-6-sol"),
    ("deepseek-v4-pro", "claude-sonnet-5-5"), ("deepseek-v4-flash", "gpt-6-luna"), ("grok-4-7", "gpt-6-sol"),
    ("kimi-k3", "claude-sonnet-5-5"), ("qwen3-8-max", "gpt-6-sol"), ("gpt-5-6", "gpt-6-sol"),
]

# Typical workloads: (label, what it is, input tokens, output tokens) — English-text token counts
WORKLOADS = [
    ("Chatbot reply", "short question plus some chat history", 1500, 400),
    ("Document Q&A (RAG)", "retrieved passages plus a question", 8000, 500),
    ("Coding agent step", "large working context, short edit", 25000, 800),
    ("Summarize a long report", "long input, short summary", 20000, 300),
    ("Write an article", "short brief, long draft", 800, 2000),
]

def slug(m):
    return m["id"].replace(".", "-")

def path(a, b):
    return f"/compare/{slug(a)}-vs-{slug(b)}"

def cost(m, i, o):
    return (i * m["ratio"] * m["inp"] + o * m["ratio"] * m["out"]) / 1e6

def money(x):
    if x >= 100: return f"${x:,.0f}"
    if x >= 1: return f"${x:,.2f}"
    if x >= 0.01: return f"${x:.3f}"
    return f"${x:.4f}"

def per_m(x):
    return f"${x:g}" if x >= 1 else f"${x:.2f}".rstrip("0").rstrip(".") if x >= 0.1 else f"${x:g}"

def ctx_txt(c):
    if not c: return "—"
    return f"{round(c / 1e6, 2):g}M tokens" if c >= 1e6 else f"{round(c / 1000):,}K tokens"

def times(x):
    return f"{x:.1f}×" if x < 10 else f"{x:.0f}×"

def cheaper_line(a, b, ca, cb):
    if abs(ca - cb) / max(ca, cb) < 0.03:
        return f"about the same as {b['name']}"
    lo, hi = (a, b) if ca < cb else (b, a)
    r = max(ca, cb) / min(ca, cb)
    return f"{lo['name']} is {times(r)} cheaper" if r >= 1.5 else f"{lo['name']} is {round((1 - min(ca, cb) / max(ca, cb)) * 100)}% cheaper"

def build_page(a, b, models, checked, related):
    title = f"{a['name']} vs {b['name']}: API Cost Comparison"
    base_a, base_b = cost(a, 1500, 400), cost(b, 1500, 400)
    lead = cheaper_line(a, b, base_a, base_b)
    desc = (f"{a['name']} vs {b['name']} API prices per 1M tokens, cost per request for chat, RAG, coding agents and writing, "
            f"and which is cheaper. Updated {checked}.")
    if len(desc) > 160:
        desc = f"{a['name']} vs {b['name']}: API prices, cost per request for 5 workloads, and which is cheaper. Updated {checked}."

    # Price table
    def row(label, fa, fb):
        return f"<tr><td>{label}</td><td>{fa}</td><td>{fb}</td></tr>"
    tok_note = lambda m: "baseline (GPT o200k count)" if m["ratio"] == 1 else f"~{round(m['ratio'] * 100)}% of GPT's count (estimate)"
    price_tbl = ("<table><thead><tr><th></th>" f"<th>{esc(a['name'])}</th><th>{esc(b['name'])}</th></tr></thead><tbody>"
                 + row("Maker", esc(a["maker"]), esc(b["maker"]))
                 + row("Input / 1M tokens", per_m(a["inp"]), per_m(b["inp"]))
                 + row("Output / 1M tokens", per_m(a["out"]), per_m(b["out"]))
                 + row("Output vs input price", f"{a['out'] / a['inp']:.1f}×", f"{b['out'] / b['inp']:.1f}×")
                 + row("Context window", ctx_txt(a["ctx"]), ctx_txt(b["ctx"]))
                 + row("Tokens for the same English text", tok_note(a), tok_note(b))
                 + "</tbody></table>")

    # Workload table (per 1,000 requests)
    wl_rows, wins_a, wins_b = [], 0, 0
    for label, what, i, o in WORKLOADS:
        ca, cb = cost(a, i, o) * 1000, cost(b, i, o) * 1000
        if ca < cb * 0.97: wins_a += 1
        elif cb < ca * 0.97: wins_b += 1
        r = max(ca, cb) / min(ca, cb)
        verdict = "≈ same" if r < 1.03 else f"{esc((a if ca < cb else b)['name'])} {times(r)} cheaper" if r >= 1.5 else f"{esc((a if ca < cb else b)['name'])} {round((1 - 1 / r) * 100)}% cheaper"
        wl_rows.append(f"<tr><td><strong>{label}</strong><br><span class=\"text-xs\">{what} · {i:,} in / {o:,} out</span></td>"
                       f"<td>{money(ca)}</td><td>{money(cb)}</td><td>{verdict}</td></tr>")
    wl_tbl = (f"<table><thead><tr><th>Workload (per 1,000 requests)</th><th>{esc(a['name'])}</th><th>{esc(b['name'])}</th><th>Cheaper</th></tr></thead><tbody>"
              + "".join(wl_rows) + "</tbody></table>")

    # Crossover: one is cheaper on input, the other on output
    ea_in, ea_out = a["inp"] * a["ratio"], a["out"] * a["ratio"]
    eb_in, eb_out = b["inp"] * b["ratio"], b["out"] * b["ratio"]
    cross = ""
    if (ea_in - eb_in) * (ea_out - eb_out) < 0:
        # cost equal when i*ea_in + o*ea_out = i*eb_in + o*eb_out  ->  o/i = (eb_in-ea_in)/(ea_out-eb_out)
        k = (eb_in - ea_in) / (ea_out - eb_out)
        in_cheap, out_cheap = (a, b) if ea_in < eb_in else (b, a)
        cross = (f"<p>The two trade places depending on the job. {esc(in_cheap['name'])} is cheaper per input token and "
                 f"{esc(out_cheap['name'])} per output token, so they cost the same when a request produces about "
                 f"<strong>{k:.2f} output tokens per input token</strong>. Input-heavy work (RAG, long documents, agents) favors "
                 f"{esc(in_cheap['name'])}; output-heavy work (long writing, code generation) favors {esc(out_cheap['name'])}.</p>")
    else:
        lo, hi = (a, b) if ea_in <= eb_in else (b, a)
        cross = (f"<p>{esc(lo['name'])} is cheaper on both input and output, so it costs less for every kind of request. "
                 f"The gap is {times(max(ea_in, eb_in) / min(ea_in, eb_in))} on input and {times(max(ea_out, eb_out) / min(ea_out, eb_out))} on output"
                 f"{' once the tokenizer difference is included' if a['ratio'] != b['ratio'] else ''}.</p>")

    tok_p = ""
    if a["ratio"] != b["ratio"]:
        more, less = (a, b) if a["ratio"] > b["ratio"] else (b, a)
        tok_p = (f"<p><strong>Same text, different token counts.</strong> Each company uses its own tokenizer. By our estimate "
                 f"{esc(more['name'])} counts about {round((more['ratio'] / less['ratio'] - 1) * 100)}% more tokens than "
                 f"{esc(less['name'])} for the same English text, and the costs above already include that. "
                 f"Paste your own prompt into the <a href=\"/\">token counter</a> to see both counts.</p>")

    # Monthly
    month = "".join(f"<tr><td>{n:,} chatbot replies / month</td><td>{money(cost(a, 1500, 400) * n)}</td><td>{money(cost(b, 1500, 400) * n)}</td></tr>"
                    for n in (10_000, 100_000, 1_000_000))
    month_tbl = f"<table><thead><tr><th>Monthly volume</th><th>{esc(a['name'])}</th><th>{esc(b['name'])}</th></tr></thead><tbody>{month}</tbody></table>"

    if wins_a and wins_b:
        summary = f"It depends on the workload: {esc(a['name'])} is cheaper in {wins_a} of the 5 workloads below and {esc(b['name'])} in {wins_b}."
    elif wins_a or wins_b:
        w = a if wins_a else b
        summary = f"{esc(w['name'])} is cheaper in every workload below."
    else:
        summary = "They cost about the same in every workload below."

    calc_id = "cmp"
    data = json.dumps({"a": [a["name"], a["inp"], a["out"], a["ratio"]], "b": [b["name"], b["inp"], b["out"], b["ratio"]]})
    calc = f"""<div class="not-prose mt-4 rounded-xl border border-zinc-800 bg-zinc-950/60 p-4 text-sm">
  <div class="grid grid-cols-3 gap-3">
    <label class="block"><span class="text-zinc-400 text-xs">Input tokens</span><input id="{calc_id}I" type="number" min="0" value="1500" class="mt-1 w-full bg-zinc-900 border border-zinc-700 rounded-md px-2 py-1 text-zinc-100"></label>
    <label class="block"><span class="text-zinc-400 text-xs">Output tokens</span><input id="{calc_id}O" type="number" min="0" value="400" class="mt-1 w-full bg-zinc-900 border border-zinc-700 rounded-md px-2 py-1 text-zinc-100"></label>
    <label class="block"><span class="text-zinc-400 text-xs">Requests / month</span><input id="{calc_id}N" type="number" min="0" value="10000" class="mt-1 w-full bg-zinc-900 border border-zinc-700 rounded-md px-2 py-1 text-zinc-100"></label>
  </div>
  <div id="{calc_id}R" class="mt-4 grid grid-cols-2 gap-3"></div>
  <p class="mt-3 text-xs text-zinc-500">Token counts are for English text measured with GPT's tokenizer; each model's own tokenizer difference is applied automatically.</p>
</div>
<script>(function(){{var D={data};var $=function(i){{return document.getElementById(i)}};
function f(x){{return x>=100?'$'+Math.round(x).toLocaleString('en-US'):x>=1?'$'+x.toFixed(2):'$'+x.toFixed(4)}}
function u(){{var i=+$('{calc_id}I').value||0,o=+$('{calc_id}O').value||0,n=+$('{calc_id}N').value||0;
var c=[D.a,D.b].map(function(m){{return (i*m[3]*m[1]+o*m[3]*m[2])/1e6}});var lo=Math.min(c[0],c[1]);
$('{calc_id}R').innerHTML=[D.a,D.b].map(function(m,k){{var best=c[k]===lo&&c[0]!==c[1];return '<div class="rounded-lg p-3 border '+(best?'border-emerald-500/50 bg-emerald-500/10':'border-zinc-800')+'"><div class="text-xs text-zinc-400">'+m[0]+'</div><div class="text-lg font-bold text-zinc-100">'+f(c[k]*n)+'<span class="text-xs text-zinc-500"> / month</span></div><div class="text-xs text-zinc-500">'+f(c[k])+' per request</div></div>'}}).join('')}}
['I','O','N'].forEach(function(s){{$('{calc_id}'+s).addEventListener('input',u)}});u()}})();</script>"""

    rel = "".join(f'<li><a href="{p}">{esc(t)}</a></li>' for p, t in related)
    faq = [
        (f"Which is cheaper, {a['name']} or {b['name']}?",
         f"For a typical chatbot reply (1,500 input and 400 output tokens), {a['name']} costs {money(base_a)} and {b['name']} costs {money(base_b)} per request, so {lead}. {re.sub('<[^>]+>', '', summary)}"),
        (f"How much do {a['name']} and {b['name']} cost per million tokens?",
         f"{a['name']} costs {per_m(a['inp'])} per 1M input tokens and {per_m(a['out'])} per 1M output tokens. {b['name']} costs {per_m(b['inp'])} input and {per_m(b['out'])} output. Prices checked {checked}."),
        ("Do both models count the same text as the same number of tokens?",
         "No. Each model family has its own tokenizer, so the same text can be a different number of tokens. The costs on this page already include that difference (estimated from GPT's tokenizer)."),
    ]
    faq_html = "".join(f"<h3>{esc(q)}</h3><p>{esc(ans)}</p>" for q, ans in faq)

    body = f"""    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <p class="text-xs text-zinc-500"><a href="/compare/">All comparisons</a> · Prices checked {checked}</p>
      <h1 class="text-2xl sm:text-3xl font-extrabold text-white leading-snug">{esc(a['name'])} vs {esc(b['name'])}: API cost comparison</h1>
      <p>For a typical chatbot reply, {esc(a['name'])} costs <strong>{money(base_a)}</strong> and {esc(b['name'])} costs <strong>{money(base_b)}</strong> per request: {esc(lead)}. {summary}</p>
      <h2>API prices</h2>
      <div class="overflow-x-auto">{price_tbl}</div>
      <h2>Cost by workload</h2>
      <div class="overflow-x-auto">{wl_tbl}</div>
      {cross}
      {tok_p}
      <h2>Monthly cost</h2>
      <div class="overflow-x-auto">{month_tbl}</div>
      <h2>Calculate your own</h2>
      <p>Enter your typical request size and volume.</p>
      {calc}
      <h2>Questions</h2>
      {faq_html}
      <h2>Related comparisons</h2>
      <ul>{rel}</ul>
      <div class="not-prose mt-8 rounded-xl border border-violet-500/30 bg-violet-500/10 p-5 text-center">
        <p class="text-zinc-200">Paste a real prompt to see its exact tokens and cost on {esc(a['name'])}, {esc(b['name'])} and 30+ other models.</p>
        <a href="/" class="mt-3 inline-block tab-active rounded-lg px-4 py-2 font-semibold no-underline" style="text-decoration:none">Open the token counter →</a>
      </div>
      <p class="text-xs text-zinc-500 mt-6">Standard API list prices, short-context tier, no caching or batch discounts. Prices change; check each provider's pricing page before large jobs.</p>
    </article>"""
    faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in faq]}
    return dict(path=path(a, b), title=title, desc=desc, body=body, faq_ld=faq_ld)

def build_all(llm):
    models = load_models(llm)
    checked = llm.get("checked", "")
    pages = []
    for x, y in PAIRS:
        a, b = models[x], models[y]
        related = [(path(models[p], models[q]), f"{models[p]['name']} vs {models[q]['name']}")
                   for p, q in PAIRS if (p, q) != (x, y) and ({p, q} & {x, y})][:6]
        pages.append(build_page(a, b, models, checked, related))
    hub_items = "".join(f'<li><a href="{p["path"]}">{esc(p["title"].split(":")[0])}</a></li>' for p in pages)
    hub = f"""    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <h1 class="text-2xl sm:text-3xl font-extrabold text-white">AI model API cost comparisons</h1>
      <p>Side-by-side API costs for the models people compare most: price per million tokens, cost per request for chat, RAG, coding agents and writing, and monthly totals. Prices update automatically (last checked {checked}).</p>
      <ul>{hub_items}</ul>
      <p>Want the full list in one table? See <a href="/blog/llm-api-pricing-comparison">LLM API pricing compared</a>, or paste your own prompt into the <a href="/">token counter</a>.</p>
    </article>"""
    return pages, dict(path="/compare/", title="AI Model API Cost Comparisons | TokenSave",
                       desc="Compare API costs of GPT-6, Claude, Gemini, DeepSeek, Grok and more, side by side: price per 1M tokens and cost per request.",
                       body=hub)
