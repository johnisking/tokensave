# -*- coding: utf-8 -*-
"""Capability vs price: Epoch Capabilities Index (ECI, CC BY) joined with our API prices.

Data: src/eci_scores.json, refreshed by update_eci.py from https://epoch.ai/data/eci_scores.csv.
Each model id maps to a regex over Epoch's model names; when several versions match
(e.g. "DeepSeek V4 Pro 0813" and "DeepSeek-V4-Pro"), the most recent release is used.
Models without a match are shown as "not yet measured".
"""
import html, json, math, os, re
import charts

HERE = os.path.dirname(os.path.abspath(__file__))
esc = lambda s: html.escape(str(s), quote=True)
DATA = os.path.join(HERE, "eci_scores.json")
CREDIT = ('Capability scores: <a href="https://epoch.ai/eci" rel="noopener" target="_blank">Epoch Capabilities Index</a> '
          'by Epoch AI, used under <a href="https://creativecommons.org/licenses/by/4.0/" rel="noopener" target="_blank">CC BY 4.0</a>.')

ECI_MAP = {
    "gpt-6-astra": r"GPT-6 Astra", "gpt-6-1-sol": r"GPT-6\.1 Sol", "gpt-6-sol": r"GPT-6 Sol", "gpt-6-luna": r"GPT-6 Luna",
    "gpt-5-5": r"GPT-5\.5", "gpt-5-mini": r"GPT-5 mini", "gpt-5-nano": r"GPT-5 nano",
    "gpt-4-1": r"GPT-4\.1", "gpt-4-1-mini": r"GPT-4\.1 mini", "gpt-4o": r"GPT-4o( \([A-Za-z]+ \d{4}\))?", "gpt-4o-mini": r"GPT-4o mini",
    "claude-fable-5-1": r"Claude Fable 5\.1", "claude-opus-5-5": r"Claude Opus 5\.5",
    "claude-sonnet-5-5": r"Claude Sonnet 5\.5", "claude-haiku-4-5": r"Claude Haiku 4\.5",
    "gemini-4-argon": r"Gemini 4 Argon", "gemini-3-1-pro": r"Gemini 3\.1 Pro", "gemini-3-8-flash": r"Gemini 3\.8 Flash",
    "gemini-3-5-flash-lite": r"Gemini 3\.5 Flash-Lite", "gemini-3-1-flash-lite": r"Gemini 3\.1 Flash-Lite",
    "deepseek-v4-pro": r"DeepSeek[ -]V4[ -]Pro( \d{4})?", "deepseek-v4-flash": r"DeepSeek[ -]V4[ -]Flash( \d{4})?",
    "grok-4-7": r"Grok 4\.7", "grok-4-20": r"Grok 4\.20",
    "mistral-medium-3-5": r"Mistral Medium 3\.5", "mistral-large-3": r"Mistral Large 3",
    "qwen3-8-max": r"Qwen ?3\.8 Max( \(\d{4}\))?", "kimi-k3": r"Kimi K3", "kimi-k2-6": r"Kimi K2\.6",
}
PATTERNS = {k: re.compile("^(" + v + ")$") for k, v in ECI_MAP.items()}

def wanted(name):
    return any(p.match(name) for p in PATTERNS.values())

def load():
    return json.load(open(DATA, encoding="utf-8"))

def scores(data=None):
    data = data or load()
    out = {}
    for mid, p in PATTERNS.items():
        hits = [r for r in data["rows"] if p.match(r[0])]
        if hits:
            name, eci, lo, hi, date = max(hits, key=lambda r: r[4])
            out[mid] = dict(eci=eci, lo=lo, hi=hi, date=date, src=name)
    return out

def blended(m):
    """USD per 1M tokens at a 3:1 input:output mix, after the model's tokenizer ratio."""
    return (3 * m["inp"] + m["out"]) / 4 * m["ratio"]

def frontier(points):
    """Ids on the price/capability frontier: no other model is both cheaper and more capable."""
    best, out = -1, set()
    for p in sorted(points, key=lambda p: (p["x"], -p["y"])):
        if p["y"] > best:
            out.add(p["id"]); best = p["y"]
    return out

def compare_line(a, b, sc):
    """One sentence for a /compare page, or '' when neither model has a score."""
    sa, sb = sc.get(a["id"]), sc.get(b["id"])
    if not sa and not sb:
        return ""
    if sa and sb:
        d = sa["eci"] - sb["eci"]
        overlap = sa["lo"] <= sb["hi"] and sb["lo"] <= sa["hi"]
        if abs(d) < 0.5:
            verdict = "essentially the same"
        else:
            hi, lo = (a, b) if d > 0 else (b, a)
            verdict = f"{esc(hi['name'])} is {abs(d):.1f} points higher" + (", within the margin of error" if overlap else "")
        txt = (f"On the Epoch Capabilities Index, {esc(a['name'])} scores <strong>{sa['eci']:.1f}</strong> and "
               f"{esc(b['name'])} <strong>{sb['eci']:.1f}</strong>: {verdict}.")
    else:
        has, no = (a, sa) if sa else (b, sb)
        miss = b if sa else a
        txt = (f"On the Epoch Capabilities Index, {esc(has['name'])} scores <strong>{no['eci']:.1f}</strong>; "
               f"{esc(miss['name'])} has not been measured yet.")
    return (f'<p>{txt} See <a href="/compare/performance">capability vs price for all models</a>.</p>'
            f'<p class="text-xs text-zinc-500">{CREDIT}</p>')

def build_page(models, llm):
    data = load()
    sc = scores(data)
    checked = data.get("checked", "")
    pts = [dict(id=mid, name=models[mid]["name"], x=blended(models[mid]), y=s["eci"], lo=s["lo"], hi=s["hi"])
           for mid, s in sc.items() if mid in models]
    front = frontier(pts)
    for p in pts:
        p["front"] = p["id"] in front
    svg = charts.scatter_chart(pts, checked)
    src = "/img/ai-model-capability-vs-price.svg"
    w, h = charts.size_of(svg)
    fig = charts.figure(src, "Scatter chart of AI model capability (Epoch Capabilities Index) against API price per million tokens, with the best-value frontier highlighted",
                        f"Capability (ECI) vs blended API price per 1M tokens, {len(pts)} models. Frontier models are the best value at their price.", w, h)
    top_svg, cheap_svg = charts.rank_chart(pts, "top", checked), charts.rank_chart(pts, "cheap", checked)
    top_src, cheap_src = "/img/most-capable-ai-models.svg", "/img/cheapest-ai-models.svg"
    top_fig = charts.figure(top_src, "Ranking of AI models by Epoch Capabilities Index score with 90% ranges",
                            "AI models ranked by capability (ECI), with the 90% range of each estimate.", *charts.size_of(top_svg))
    cheap_fig = charts.figure(cheap_src, "Ranking of AI models by blended API price per million tokens, cheapest first, with capability scores",
                              "AI models ranked by blended API price, cheapest first, with each model's capability score.", *charts.size_of(cheap_svg))
    # one pick per view
    top_p = max(pts, key=lambda p: p["y"])
    val_p = max((p for p in pts if p["front"] and p["x"] <= top_p["x"] * 0.6), key=lambda p: p["y"], default=top_p)
    cheap_p = min((p for p in pts if p["y"] >= top_p["y"] - 15), key=lambda p: p["x"])
    def card(p, label, why):
        return (f'<div class="perf-pick"><div class="perf-pick-k">{label}</div><div class="perf-pick-n">{esc(p["name"])}</div>'
                f'<div class="perf-pick-v">ECI {p["y"]:.1f} · ${p["x"]:.2f} per 1M tokens</div><p>{why}</p></div>')
    top_card = card(top_p, "Top capability", "The highest score on the Epoch Capabilities Index among the models priced here.")
    val_card = card(val_p, "Best value", f"{top_p['y'] - val_p['y']:.1f} points below the top model for {val_p['x'] / top_p['x'] * 100:.0f}% of its price, and on the best-value frontier.")
    cheap_card = card(cheap_p, "Lowest price", f"The cheapest model within 15 points of the top score: {cheap_p['x'] / top_p['x'] * 100:.0f}% of the top model's price.")
    views = f"""<div class="perf-tabs not-prose" role="tablist">
        <button type="button" role="tab" data-v="top" aria-selected="false">🏆 Top capability</button>
        <button type="button" role="tab" data-v="value" aria-selected="true">💎 Best value</button>
        <button type="button" role="tab" data-v="cheap" aria-selected="false">💸 Lowest price</button>
      </div>
      <div class="perf-view" data-v="top" hidden>{top_card}{top_fig}</div>
      <div class="perf-view" data-v="value">{val_card}{fig}</div>
      <div class="perf-view" data-v="cheap" hidden>{cheap_card}{cheap_fig}</div>
      <script>(function(){{var b=document.querySelectorAll('.perf-tabs button'),v=document.querySelectorAll('.perf-view');
      b.forEach(function(x){{x.addEventListener('click',function(){{b.forEach(function(y){{y.setAttribute('aria-selected',y===x)}});
      v.forEach(function(w){{w.hidden=w.dataset.v!==x.dataset.v}})}})}})}})();</script>"""
    rows = []
    for p in sorted(pts, key=lambda p: -p["y"]):
        m = models[p["id"]]
        tag = ' <span class="text-emerald-400">★ best value</span>' if p["front"] else ""
        rows.append(f"<tr><td><strong>{esc(p['name'])}</strong>{tag}</td><td>{p['y']:.1f}<br><span class=\"text-xs\">{p['lo']:.0f}–{p['hi']:.0f}</span></td>"
                    f"<td>${m['inp']:g} / ${m['out']:g}</td><td>${p['x']:.2f}</td></tr>")
    missing = [models[mid]["name"] for mid in ECI_MAP if mid in models and mid not in sc]
    tbl = ("<table><thead><tr><th>Model</th><th>ECI<br><span class=\"text-xs\">(90% range)</span></th><th>Input / output<br>per 1M</th>"
           "<th>Blended<br>per 1M</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table>")
    top = max(pts, key=lambda p: p["y"])
    cheap_front = sorted((p for p in pts if p["front"]), key=lambda p: p["x"])
    front_names = ", ".join(esc(p["name"]) for p in cheap_front)
    # closest-to-top model at a fraction of the price
    alt = min((p for p in pts if p["id"] != top["id"] and p["y"] >= top["y"] - 3), key=lambda p: p["x"], default=None)
    alt_txt = (f" {esc(alt['name'])} comes within {top['y'] - alt['y']:.1f} points for {alt['x'] / top['x'] * 100:.0f}% of the price."
               if alt and alt["x"] < top["x"] else "")
    title = "AI Model Capability vs Price: Which LLM Gives the Most for the Money"
    desc = f"Capability (Epoch Capabilities Index) against API price for {len(pts)} AI models: the best-value models at every budget. Updated {checked}."
    body = f"""    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <p class="text-xs text-zinc-500"><a href="/compare/">All comparisons</a> · Scores checked {esc(checked)} · Prices {esc(llm.get('checked', ''))}</p>
      <h1 class="text-2xl sm:text-3xl font-extrabold text-white leading-snug">AI model capability vs price</h1>
      <p>A more expensive model is not always a smarter one. This chart puts each model's general capability, measured by the Epoch Capabilities Index (ECI), against what its API costs. The highest score is {esc(top['name'])} at {top['y']:.1f}.{alt_txt}</p>
      {views}
      <h2>The best-value models</h2>
      <p>A model is on the <strong>best-value frontier</strong> when no other model is both cheaper and more capable. From cheapest to most capable: {front_names}. Anything below the line costs more than a frontier model with the same or higher score.</p>
      <h2>All scores and prices</h2>
      <div class="overflow-x-auto">{tbl}</div>
      <p class="text-xs text-zinc-500">Blended price = (3 × input + output) ÷ 4 per million tokens, a typical chat mix, adjusted for each model's tokenizer (how many tokens it uses for the same English text). Standard list prices, no caching or batch discounts.</p>
      {('<p>Not measured yet: ' + esc(', '.join(missing)) + '. They appear here automatically once Epoch AI publishes a score.</p>') if missing else ''}
      <h2>What the score means</h2>
      <p>ECI combines dozens of benchmarks (math, coding, science, reasoning and more) into one scale, so models tested on different benchmarks can still be compared. A gap of a few points is often within the margin of error; the 90% range in the table shows how sure the estimate is. It measures general capability, not your task: for a specific job, test a few frontier models on your own prompts.</p>
      <p>To see what your own prompts cost on each model, paste them into the <a href="/">token counter</a>, or compare two models side by side on the <a href="/compare/">comparison pages</a>.</p>
      <p class="text-xs text-zinc-500">{CREDIT} Prices: TokenSave, updated daily.</p>
    </article>"""
    faq = [
        ("Which AI model is the best value?",
         f"Based on the Epoch Capabilities Index and current API prices, the best-value models (no other model is both cheaper and more capable) are: {', '.join(p['name'] for p in cheap_front)}."),
        ("Which AI model scores highest on the Epoch Capabilities Index?",
         f"{top['name']} has the highest score among the models compared here, {top['y']:.1f} (checked {checked})."),
    ]
    faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    return dict(path="/compare/performance", title=title, desc=desc, body=body, faq_ld=faq_ld,
                chart=(src, svg), image_caption="AI model capability (ECI) vs API price",
                extra_images=[(top_src, top_svg, "Most capable AI models (ECI)"), (cheap_src, cheap_svg, "Cheapest AI models by API price")]), sc
