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

CREDIT_L = {
    "en": CREDIT,
    "ko": ('성능 점수: Epoch AI의 <a href="https://epoch.ai/eci" rel="noopener" target="_blank">Epoch Capabilities Index</a>, '
           '<a href="https://creativecommons.org/licenses/by/4.0/" rel="noopener" target="_blank">CC BY 4.0</a> 라이선스로 사용.'),
    "ja": ('性能スコア：Epoch AI の <a href="https://epoch.ai/eci" rel="noopener" target="_blank">Epoch Capabilities Index</a>'
           '（<a href="https://creativecommons.org/licenses/by/4.0/" rel="noopener" target="_blank">CC BY 4.0</a>）を使用。'),
}
PATH = {"en": "/compare/performance", "ko": "/ko/compare/performance", "ja": "/ja/compare/performance"}
HOME = {"en": "/", "ko": "/ko/", "ja": "/ja/"}
READ = {"en": 'What the chart means, model by model: <a href="/blog/best-value-llm-october-2026">Best value LLM in October 2026</a>.',
        "ko": '모델별로 자세히 풀어 쓴 글: <a href="/ko/blog/ai-gaseongbi-sunwi-2026-10">2026년 10월 AI 가성비 순위</a>.',
        "ja": 'モデルごとの詳しい解説：<a href="/ja/blog/ai-cospa-ranking-2026-10">2026年10月 AIコスパランキング</a>。'}

T = {
 "en": dict(
    title="AI Model Capability vs Price: Which LLM Gives the Most for the Money",
    desc="Capability (Epoch Capabilities Index) against API price for {n} AI models: the best-value models at every budget. Updated {d}.",
    crumb='<a href="/compare/">All comparisons</a> · Scores checked {d} · Prices {p}',
    h1="AI model capability vs price",
    intro="A more expensive model is not always a smarter one. This chart puts each model's general capability, measured by the Epoch Capabilities Index (ECI), against what its API costs. The highest score is {top} at {ty}.",
    alt=" {a} comes within {d} points for {pct}% of the price.",
    tab_top="🏆 Top capability", tab_val="💎 Best value", tab_cheap="💸 Lowest price",
    k_top="Top capability", k_val="Best value", k_cheap="Lowest price", per1m="per 1M tokens",
    w_top="The highest score on the Epoch Capabilities Index among the models priced here.",
    w_val="{d} points below the top model for {pct}% of its price, and on the best-value frontier.",
    w_cheap="The cheapest model within 15 points of the top score: {pct}% of the top model's price.",
    pend_h="Waiting for a score", pend_p="These models are new, and Epoch AI has not published a capability score for them yet. They join the charts automatically once it does. Their prices today:",
    h_front="The best-value models",
    front="A model is on the <strong>best-value frontier</strong> when no other model is both cheaper and more capable. From cheapest to most capable: {names}. Anything below the line costs more than a frontier model with the same or higher score.",
    h_all="All scores and prices", th=("Model", "ECI", "(90% range)", "Input / output", "per 1M", "Blended", "per 1M"), star="★ best value",
    blend="Blended price = (3 × input + output) ÷ 4 per million tokens, a typical chat mix, adjusted for each model's tokenizer (how many tokens it uses for the same English text). Standard list prices, no caching or batch discounts.",
    h_mean="What the score means",
    mean="ECI combines dozens of benchmarks (math, coding, science, reasoning and more) into one scale, so models tested on different benchmarks can still be compared. A gap of a few points is often within the margin of error; the 90% range in the table shows how sure the estimate is. It measures general capability, not your task: for a specific job, test a few frontier models on your own prompts.",
    cta='To see what your own prompts cost on each model, paste them into the <a href="{home}">token counter</a>, or compare two models side by side on the <a href="/compare/">comparison pages</a>.',
    prices="Prices: TokenSave, updated daily.",
    fig_s=("Scatter chart of AI model capability (Epoch Capabilities Index) against API price per million tokens, with the best-value frontier highlighted",
           "Capability (ECI) vs blended API price per 1M tokens, {n} models. Frontier models are the best value at their price."),
    fig_t=("Ranking of AI models by Epoch Capabilities Index score with 90% ranges", "AI models ranked by capability (ECI), with the 90% range of each estimate."),
    fig_c=("Ranking of AI models by blended API price per million tokens, cheapest first, with capability scores", "AI models ranked by blended API price, cheapest first, with each model's capability score."),
    faq=(("Which AI model is the best value?", "Based on the Epoch Capabilities Index and current API prices, the best-value models (no other model is both cheaper and more capable) are: {names}."),
         ("Which AI model scores highest on the Epoch Capabilities Index?", "{top} has the highest score among the models compared here, {ty} (checked {d}).")),
    chart={}, img="",
 ),
 "ko": dict(
    title="AI 모델 성능 vs 가격: 가성비 좋은 LLM 순위",
    desc="AI 모델 {n}개의 성능(Epoch Capabilities Index)과 API 가격을 한 그래프로 비교했습니다. 최고 성능, 가성비, 최저가 모델을 한눈에. {d} 기준.",
    crumb='<a href="/compare/">전체 비교 (영어)</a> · 점수 {d} 기준 · 가격 {p} 기준',
    h1="AI 모델 성능 vs 가격 순위",
    intro="비싼 모델이 항상 더 똑똑한 건 아닙니다. 이 그래프는 모델마다 종합 성능(Epoch Capabilities Index, ECI)과 API 가격을 함께 보여 줍니다. 가장 높은 점수는 {top}의 {ty}점입니다.",
    alt=" {a}는 {d}점 차이로 따라오는데 가격은 {pct}%입니다.",
    tab_top="🏆 최고 성능", tab_val="💎 가성비", tab_cheap="💸 최저가",
    k_top="최고 성능", k_val="가성비", k_cheap="최저가", per1m="100만 토큰당",
    w_top="여기서 비교한 모델 중 Epoch Capabilities Index 점수가 가장 높습니다.",
    w_val="1위보다 {d}점 낮지만 가격은 {pct}%이고, 가성비 라인 위에 있습니다.",
    w_cheap="1위와 15점 이내 모델 중 가장 쌉니다. 1위 모델 가격의 {pct}%입니다.",
    pend_h="점수 대기 중", pend_p="새로 나온 모델이라 Epoch AI가 아직 성능 점수를 내지 않았습니다. 점수가 나오면 그래프에 자동으로 들어갑니다. 현재 가격:",
    h_front="가성비 좋은 모델",
    front="<strong>가성비 라인</strong> 위의 모델은 \"더 싸면서 더 똑똑한 모델\"이 없는 모델입니다. 싼 순서대로: {names}. 라인 아래에 있는 모델은 같은 점수 이상의 라인 위 모델보다 비쌉니다.",
    h_all="전체 점수와 가격", th=("모델", "ECI", "(90% 범위)", "입력 / 출력", "100만 토큰당", "혼합 가격", "100만 토큰당"), star="★ 가성비",
    blend="혼합 가격 = (입력 × 3 + 출력) ÷ 4, 100만 토큰당. 일반적인 대화 비율이며, 모델별 토크나이저 차이(같은 영어 문장에 쓰는 토큰 수)를 반영했습니다. 정가 기준이며 캐싱·배치 할인은 넣지 않았습니다.",
    h_mean="점수의 의미",
    mean="ECI는 수학, 코딩, 과학, 추론 등 수십 개의 벤치마크를 하나의 척도로 합친 점수입니다. 그래서 서로 다른 벤치마크로 측정된 모델도 비교할 수 있습니다. 몇 점 차이는 오차 범위 안인 경우가 많고, 표의 90% 범위가 추정의 확실성을 보여 줍니다. 종합 성능이지 내 작업 성능은 아니니, 특정 작업에는 가성비 라인 위 모델 몇 개를 내 프롬프트로 직접 시험해 보세요.",
    cta='내 프롬프트가 모델마다 얼마인지는 <a href="{home}">토큰 계산기</a>에 붙여 넣어 보세요. 두 모델을 나란히 비교하려면 <a href="/compare/">비교 페이지(영어)</a>를 보세요.',
    prices="가격: TokenSave, 매일 갱신.",
    fig_s=("AI 모델 성능(Epoch Capabilities Index)과 100만 토큰당 API 가격 점그래프, 가성비 라인 표시",
           "성능(ECI) vs 100만 토큰당 혼합 API 가격, 모델 {n}개. 초록 점은 같은 가격대에서 가성비가 가장 좋은 모델입니다."),
    fig_t=("Epoch Capabilities Index 점수 순 AI 모델 순위와 90% 범위", "성능(ECI) 순 AI 모델 순위. 막대는 추정의 90% 범위입니다."),
    fig_c=("100만 토큰당 혼합 API 가격이 싼 순서의 AI 모델 순위와 성능 점수", "API 가격이 싼 순서의 AI 모델 순위와 각 모델의 성능 점수."),
    faq=(("가성비가 가장 좋은 AI 모델은?", "Epoch Capabilities Index와 현재 API 가격 기준으로, 더 싸면서 더 똑똑한 모델이 없는 가성비 모델은 {names}입니다."),
         ("Epoch Capabilities Index 점수가 가장 높은 AI 모델은?", "여기서 비교한 모델 중 {top}이(가) {ty}점으로 가장 높습니다 ({d} 기준).")),
    chart=dict(s_title="AI 모델 성능 vs API 가격", s_sub="Epoch Capabilities Index (Epoch AI, CC BY) vs 100만 토큰당 혼합 가격",
               s_x="100만 토큰당 혼합 API 가격 (달러, 로그 눈금) → 왼쪽일수록 쌈", s_y="성능 (ECI) ↑", s_front="가성비 라인", s_other="기타",
               t_title="성능이 가장 높은 AI 모델", t_sub="Epoch Capabilities Index와 90% 범위 (Epoch AI, CC BY)",
               c_title="가장 싼 AI 모델", c_sub="100만 토큰당 혼합 API 가격 (로그 눈금)과 성능 점수"),
    img="ko-",
 ),
 "ja": dict(
    title="AIモデルの性能と価格：コスパの良いLLMランキング",
    desc="AIモデル{n}種の性能（Epoch Capabilities Index）とAPI料金を1つのグラフで比較。最高性能・コスパ・最安のモデルがひと目でわかります。{d}時点。",
    crumb='<a href="/compare/">比較一覧（英語）</a> · スコア {d} 時点 · 料金 {p} 時点',
    h1="AIモデルの性能と価格ランキング",
    intro="高いモデルがいつも賢いとは限りません。このグラフは、各モデルの総合性能（Epoch Capabilities Index、ECI）とAPI料金を並べて示します。最高スコアは {top} の {ty} です。",
    alt="{a} は {d} ポイント差で、料金は {pct}% です。",
    tab_top="🏆 最高性能", tab_val="💎 コスパ", tab_cheap="💸 最安",
    k_top="最高性能", k_val="コスパ", k_cheap="最安", per1m="100万トークンあたり",
    w_top="ここで比べたモデルの中で Epoch Capabilities Index のスコアが最も高いモデルです。",
    w_val="1位より {d} ポイント低いだけで料金は {pct}%、コスパのラインに乗っています。",
    w_cheap="1位から15ポイント以内のモデルで最も安く、1位の料金の {pct}% です。",
    pend_h="スコア待ち", pend_p="新しいモデルのため、Epoch AI がまだ性能スコアを公開していません。公開されると自動でグラフに加わります。現在の料金：",
    h_front="コスパの良いモデル",
    front="<strong>コスパのライン</strong>上のモデルは、「もっと安くてもっと賢いモデル」が存在しないモデルです。安い順に：{names}。ラインより下のモデルは、同じかそれ以上のスコアを持つライン上のモデルより高くつきます。",
    h_all="全スコアと料金", th=("モデル", "ECI", "（90%範囲）", "入力 / 出力", "100万あたり", "混合料金", "100万あたり"), star="★ コスパ",
    blend="混合料金 =（入力 × 3 + 出力）÷ 4、100万トークンあたり。一般的なチャットの比率で、モデルごとのトークナイザーの差（同じ英文に使うトークン数）を反映しています。定価で、キャッシュやバッチ割引は含みません。",
    h_mean="スコアの意味",
    mean="ECI は数学、コーディング、科学、推論など数十のベンチマークを1つの尺度にまとめたスコアです。そのため、異なるベンチマークで測られたモデルも比べられます。数ポイントの差は誤差の範囲内のことが多く、表の90%範囲が推定の確かさを示します。総合性能であって自分の作業での性能ではないので、特定の用途にはライン上のモデルをいくつか自分のプロンプトで試してください。",
    cta='自分のプロンプトがモデルごとにいくらかかるかは<a href="{home}">トークンカウンター</a>に貼り付けて確認できます。2つのモデルを並べて比べるなら<a href="/compare/">比較ページ（英語）</a>へ。',
    prices="料金：TokenSave、毎日更新。",
    fig_s=("AIモデルの性能（Epoch Capabilities Index）と100万トークンあたりAPI料金の散布図、コスパのラインを表示",
           "性能（ECI）と100万トークンあたりの混合API料金、{n}モデル。緑の点はその価格帯で最もコスパの良いモデルです。"),
    fig_t=("Epoch Capabilities Index スコア順のAIモデルランキングと90%範囲", "性能（ECI）順のAIモデルランキング。線は推定の90%範囲です。"),
    fig_c=("100万トークンあたり混合API料金が安い順のAIモデルランキングと性能スコア", "API料金が安い順のAIモデルランキングと各モデルの性能スコア。"),
    faq=(("コスパが最も良いAIモデルは？", "Epoch Capabilities Index と現在のAPI料金にもとづくと、もっと安くてもっと賢いモデルが存在しないコスパの良いモデルは {names} です。"),
         ("Epoch Capabilities Index のスコアが最も高いAIモデルは？", "ここで比べたモデルの中では {top} が {ty} で最も高いスコアです（{d}時点）。")),
    chart=dict(s_title="AIモデルの性能とAPI料金", s_sub="Epoch Capabilities Index（Epoch AI, CC BY）と100万トークンあたり混合料金",
               s_x="100万トークンあたり混合API料金（ドル、対数目盛）→ 左ほど安い", s_y="性能（ECI）↑", s_front="コスパのライン", s_other="その他",
               t_title="最も性能が高いAIモデル", t_sub="Epoch Capabilities Index と90%範囲（Epoch AI, CC BY）",
               c_title="最も安いAIモデル", c_sub="100万トークンあたり混合API料金（対数目盛）と性能スコア"),
    img="ja-",
 ),
}

def build_page(models, llm, lang="en"):
    t = T[lang]
    data = load()
    sc = scores(data)
    checked = data.get("checked", "")
    pts = [dict(id=mid, name=models[mid]["name"], x=blended(models[mid]), y=s["eci"], lo=s["lo"], hi=s["hi"])
           for mid, s in sc.items() if mid in models]
    front = frontier(pts)
    for p in pts:
        p["front"] = p["id"] in front
    n = len(pts)
    svg = charts.scatter_chart(pts, checked, t["chart"])
    top_svg, cheap_svg = charts.rank_chart(pts, "top", checked, t["chart"]), charts.rank_chart(pts, "cheap", checked, t["chart"])
    pre = t["img"]
    src, top_src, cheap_src = (f"/img/{pre}ai-model-capability-vs-price.svg", f"/img/{pre}most-capable-ai-models.svg", f"/img/{pre}cheapest-ai-models.svg")
    fig = charts.figure(src, t["fig_s"][0], t["fig_s"][1].format(n=n), *charts.size_of(svg))
    top_fig = charts.figure(top_src, *t["fig_t"], *charts.size_of(top_svg))
    cheap_fig = charts.figure(cheap_src, *t["fig_c"], *charts.size_of(cheap_svg))
    top_p = max(pts, key=lambda p: p["y"])
    val_p = max((p for p in pts if p["front"] and p["x"] <= top_p["x"] * 0.6), key=lambda p: p["y"], default=top_p)
    cheap_p = min((p for p in pts if p["y"] >= top_p["y"] - 15), key=lambda p: p["x"])
    pct = lambda p: f"{p['x'] / top_p['x'] * 100:.0f}"
    def card(p, label, why):
        return (f'<div class="perf-pick"><div class="perf-pick-k">{label}</div><div class="perf-pick-n">{esc(p["name"])}</div>'
                f'<div class="perf-pick-v">ECI {p["y"]:.1f} · ${p["x"]:.2f} {t["per1m"]}</div><p>{why}</p></div>')
    top_card = card(top_p, t["k_top"], t["w_top"])
    val_card = card(val_p, t["k_val"], t["w_val"].format(d=f"{top_p['y'] - val_p['y']:.1f}", pct=pct(val_p)))
    cheap_card = card(cheap_p, t["k_cheap"], t["w_cheap"].format(pct=pct(cheap_p)))
    views = f"""<div class="perf-tabs not-prose" role="tablist">
        <button type="button" role="tab" data-v="top" aria-selected="false">{t['tab_top']}</button>
        <button type="button" role="tab" data-v="value" aria-selected="true">{t['tab_val']}</button>
        <button type="button" role="tab" data-v="cheap" aria-selected="false">{t['tab_cheap']}</button>
      </div>
      <div class="perf-view" data-v="top" hidden>{top_card}{top_fig}</div>
      <div class="perf-view" data-v="value">{val_card}{fig}</div>
      <div class="perf-view" data-v="cheap" hidden>{cheap_card}{cheap_fig}</div>
      <script>(function(){{var b=document.querySelectorAll('.perf-tabs button'),v=document.querySelectorAll('.perf-view');
      b.forEach(function(x){{x.addEventListener('click',function(){{b.forEach(function(y){{y.setAttribute('aria-selected',y===x)}});
      v.forEach(function(w){{w.hidden=w.dataset.v!==x.dataset.v}})}})}})}})();</script>"""
    missing = [mid for mid in ECI_MAP if mid in models and mid not in sc]
    pend = ""
    if missing:
        chips = "".join(f'<li><strong>{esc(models[m]["name"])}</strong><span>${models[m]["inp"]:g} / ${models[m]["out"]:g} · ${blended(models[m]):.2f}</span></li>' for m in missing)
        pend = f'<div class="perf-pend not-prose"><div class="perf-pend-h">⏳ {t["pend_h"]}</div><p>{t["pend_p"]}</p><ul>{chips}</ul></div>'
    th = t["th"]
    rows = []
    for p in sorted(pts, key=lambda p: -p["y"]):
        m = models[p["id"]]
        tag = f' <span class="text-emerald-400">{t["star"]}</span>' if p["front"] else ""
        rows.append(f"<tr><td><strong>{esc(p['name'])}</strong>{tag}</td><td>{p['y']:.1f}<br><span class=\"text-xs\">{p['lo']:.0f}–{p['hi']:.0f}</span></td>"
                    f"<td>${m['inp']:g} / ${m['out']:g}</td><td>${p['x']:.2f}</td></tr>")
    tbl = (f"<table><thead><tr><th>{th[0]}</th><th>{th[1]}<br><span class=\"text-xs\">{th[2]}</span></th><th>{th[3]}<br>{th[4]}</th>"
           f"<th>{th[5]}<br>{th[6]}</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table>")
    cheap_front = sorted((p for p in pts if p["front"]), key=lambda p: p["x"])
    names_plain = ", ".join(p["name"] for p in cheap_front)
    alt = min((p for p in pts if p["id"] != top_p["id"] and p["y"] >= top_p["y"] - 3), key=lambda p: p["x"], default=None)
    alt_txt = t["alt"].format(a=esc(alt["name"]), d=f"{top_p['y'] - alt['y']:.1f}", pct=pct(alt)) if alt and alt["x"] < top_p["x"] else ""
    credit = CREDIT_L[lang]
    body = f"""    <article class="prose-ts max-w-3xl mx-auto bg-zinc-900/60 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <p class="text-xs text-zinc-500">{t['crumb'].format(d=esc(checked), p=esc(llm.get('checked', '')))}</p>
      <h1 class="text-2xl sm:text-3xl font-extrabold text-white leading-snug">{t['h1']}</h1>
      <p>{t['intro'].format(top=esc(top_p['name']), ty=f"{top_p['y']:.1f}")}{alt_txt}</p>
      {views}
      {pend}
      <h2>{t['h_front']}</h2>
      <p>{t['front'].format(names=esc(names_plain))}</p>
      <h2>{t['h_all']}</h2>
      <div class="overflow-x-auto">{tbl}</div>
      <p class="text-xs text-zinc-500">{t['blend']}</p>
      <h2>{t['h_mean']}</h2>
      <p>{t['mean']}</p>
      <p>{t['cta'].format(home=HOME[lang])}</p>
      <p>{READ[lang]}</p>
      <p class="text-xs text-zinc-500">{credit} {t['prices']}</p>
    </article>"""
    faq = [(q, a.format(names=names_plain, top=top_p["name"], ty=f"{top_p['y']:.1f}", d=checked)) for q, a in t["faq"]]
    faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    return dict(path=PATH[lang], lang=lang, title=t["title"], desc=t["desc"].format(n=n, d=checked), body=body, faq_ld=faq_ld,
                chart=(src, svg), image_caption=t["fig_s"][1].format(n=n),
                extra_images=[(top_src, top_svg, t["fig_t"][1]), (cheap_src, cheap_svg, t["fig_c"][1])]), sc
