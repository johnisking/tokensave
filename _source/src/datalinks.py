"""Internal links to the data pages (2026-10-27).

The 27 data pages are the site's own measurements, but most had only 1 to 10 internal links.
After the build, every indexable page gets a small "Measured data" box with the most relevant
data pages, chosen by keyword overlap with the page text. The English home page gets the full list.
The box sits inside a <footer> so seo_lastmod's text hash (main content only) does not change.
Noindexed pages and the data hub are skipped."""
import glob, html as H, os, re

# path, short label, keywords (lowercase, matched on the page text)
DATASETS = [
    ("/data/language-tax-index", "Language Tax Index: extra tokens per language", "language korean japanese chinese hindi arabic translate 언어 한국어 일본어 言語 日本語"),
    ("/data/token-cost-by-language-claude-gemini", "Token cost by language on Claude, Gemini and GPT", "language korean japanese tokenizer claude gemini 한국어 토큰 日本語 トークン"),
    ("/data/token-cost-by-language", "Token cost by language: 41 languages on GPT", "language gpt tokenizer chatgpt translate 언어 번역 翻訳"),
    ("/data/token-cost-by-format", "Token cost by data format: JSON, YAML, CSV, TOON", "json yaml csv format table data 포맷 형식 フォーマット"),
    ("/data/image-token-cost", "Image input token cost by resolution", "image picture photo screenshot resolution vision 이미지 사진 画像"),
    ("/data/pdf-token-cost", "PDF token cost per page", "pdf document page file 문서 ドキュメント"),
    ("/data/token-cost-by-programming-language", "Token cost by programming language", "python javascript code programming language 프로그래밍 コード"),
    ("/data/claude-effort-cost", "Claude effort levels: tokens, time and cost", "effort thinking reasoning opus sonnet haiku xhigh 추론 effort"),
    ("/data/claude-code-vs-codex-tokens", "Claude Code vs Codex: startup tokens and MCP tools", "codex claude code mcp agent cli 에이전트 エージェント"),
    ("/data/antigravity-cli-vs-claude-code-vs-codex", "Antigravity CLI vs Claude Code vs Codex", "antigravity gemini cli codex claude code agent"),
    ("/data/ai-agent-web-search-tokens", "Web search in Claude Code and Codex", "search web browse perplexity 검색 検索"),
    ("/data/claude-web-search-by-language", "AI web search by language", "search web language 검색 検索"),
    ("/data/claude-md-agents-md-size", "CLAUDE.md and AGENTS.md size", "claude.md agents.md instruction prompt system memory 지침"),
    ("/data/ai-coding-prompt-language", "Does the prompt language change coding cost?", "prompt language coding korean english 프롬프트 プロンプト"),
    ("/data/claude-code-harness-cost", "What the Claude Code harness costs", "claude code plugin subagent skill hook plan mode harness 플러그인 서브에이전트"),
    ("/data/claude-code-baseline-tokens-by-version", "Claude Code baseline tokens by version", "claude code version baseline system prompt update 버전"),
    ("/data/vibe-coding-by-claude-model", "Vibe coding with Haiku, Sonnet and Opus 5.5", "vibe coding game haiku sonnet opus model choose 바이브 게임 ゲーム"),
    ("/data/long-chat-vs-new-chat-cost", "Long chat or new chat? What 30 requests cost", "chat session conversation compact context long new 대화 세션 会話"),
    ("/data/ai-politeness-token-cost", "Does being polite to AI cost more?", "polite please thank 존댓말 공손 丁寧"),
    ("/data/ai-coffee-break-cache-cost", "The coffee-break tax: cache after a pause", "cache caching pause prompt caching 캐시 キャッシュ"),
    ("/data/text-as-image-token-cost", "Text as images to cut AI tokens", "image text compress pxpipe 이미지 画像"),
    ("/data/browser-mcp-token-cost", "Browser MCP token cost: Playwright vs DevTools", "mcp browser playwright chrome devtools snapshot 브라우저"),
    ("/data/blender-mcp-token-cost", "Blender MCP token cost: 72 runs", "blender mcp 3d game scene 블렌더"),
    ("/data/output-tokens-per-character-by-model", "Output tokens per character by model", "output tokens gpt gemini claude code 출력"),
    ("/data/ai-coding-limit-line", "Where Claude Haiku falls behind Opus", "haiku opus limit coding bug test 하이쿠 오퍼스 한도 limit usage"),
    ("/data/claude-haiku-vs-opus-real-bugs", "Haiku vs Sonnet vs Opus on 25 real bugs", "haiku sonnet opus bug fix coding model 버그 하이쿠 오퍼스 バグ"),
]
HEAD = {"en": "Measured data", "ko": "직접 잰 데이터 (영문)", "ja": "実測データ（英語）"}
SUB = {"en": "Open datasets from our own runs, with CSV and method.", "ko": "우리가 직접 돌려 잰 공개 데이터입니다. CSV와 측정 방법이 함께 있습니다.",
       "ja": "自分たちで計測した公開データです。CSVと計測方法つき。"}
ALL_HEAD = {"en": "All our measurements", "ko": "전체 실측 데이터 (영문)", "ja": "すべての実測データ（英語）"}
MARK = "<!-- datalinks -->"
FOOT = '    <footer class="mt-10 text-center text-xs text-zinc-600 space-y-1">'


def _text(h):
    h = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<footer.*?</footer>", " ", h, flags=re.S)
    return H.unescape(re.sub(r"<[^>]+>", " ", h)).lower()


def _box(items, lang, head):
    li = "\n".join(f'          <li><a href="{p}" class="hover:text-violet-300">{H.escape(t)}</a></li>' for p, t in items)
    return (f'{MARK}\n    <footer class="max-w-3xl mx-auto mt-8 border border-zinc-800 rounded-2xl p-5 bg-zinc-900/40">\n'
            f'      <p class="text-sm font-semibold text-zinc-200">📊 {head}</p>\n'
            f'      <p class="mt-1 text-xs text-zinc-500">{SUB.get(lang, SUB["en"])}</p>\n'
            f'      <ul class="mt-3 space-y-1.5 text-sm text-zinc-300 list-disc pl-5">\n{li}\n      </ul>\n'
            f'      <p class="mt-3 text-xs"><a href="/data/" class="text-violet-300 hover:text-violet-200">/data/ →</a></p>\n    </footer>\n')


def _idf(texts):
    import math
    df = {}
    for t in texts:
        for _, _, kw in DATASETS:
            for k in kw.split():
                if k in t:
                    df[k] = df.get(k, 0) + 1
    n = max(1, len(texts))
    return {k: math.log(n / (1 + v)) for k, v in df.items()}


IDF = {}
CLUSTERS = [
    ["language-tax-index", "token-cost-by-language-claude-gemini", "token-cost-by-language", "ai-coding-prompt-language", "claude-web-search-by-language", "ai-politeness-token-cost"],
    ["token-cost-by-format", "image-token-cost", "pdf-token-cost", "token-cost-by-programming-language", "text-as-image-token-cost"],
    ["claude-code-vs-codex-tokens", "antigravity-cli-vs-claude-code-vs-codex", "claude-code-harness-cost", "claude-code-baseline-tokens-by-version", "claude-md-agents-md-size", "ai-agent-web-search-tokens", "browser-mcp-token-cost", "blender-mcp-token-cost"],
    ["claude-effort-cost", "vibe-coding-by-claude-model", "ai-coding-limit-line", "claude-haiku-vs-opus-real-bugs", "output-tokens-per-character-by-model"],
    ["long-chat-vs-new-chat-cost", "ai-coffee-break-cache-cost", "claude-code-harness-cost", "claude-md-agents-md-size"],
]
TITLE = {p: t for p, t, _ in DATASETS}


def related(self_path, linked, n=4):
    slug = self_path.split("/")[-1]
    out = []
    for c in CLUSTERS:
        if slug in c:
            for x in c:
                p = "/data/" + x
                if x != slug and p not in linked and p in TITLE and (p, TITLE[p]) not in out:
                    out.append((p, TITLE[p]))
    return out[:n]


def pick(text, self_path, linked, n=3):
    scored = []
    for i, (p, t, kw) in enumerate(DATASETS):
        if p == self_path or p in linked:
            continue
        s = sum(min(text.count(k), 5) * max(IDF.get(k, 0), 0) for k in kw.split())
        if s > 0:
            scored.append((-s, i, p, t))
    scored.sort()
    out = [(p, t) for _, _, p, t in scored[:n]]
    for p, t, _ in reversed(DATASETS):
        if len(out) >= n:
            break
        if p != self_path and p not in linked and (p, t) not in out:
            out.append((p, t))
    return out


def apply(dist):
    n = 0
    files = glob.glob(os.path.join(dist, "**", "*.html"), recursive=True)
    IDF.clear(); IDF.update(_idf([_text(open(f, encoding="utf-8").read()) for f in files]))
    for fp in files:
        rel = "/" + os.path.relpath(fp, dist)[:-5].replace(os.sep, "/")
        rel = (rel[:-6] if rel.endswith("/index") else rel) or "/"
        h = open(fp, encoding="utf-8").read()
        if MARK in h or FOOT not in h or re.search(r'<meta name="robots" content="noindex', h) or rel.rstrip("/") == "/data":
            continue
        m = re.search(r'<html[^>]*lang="([a-zA-Z-]+)"', h)
        lang = (m.group(1).lower().split("-")[0] if m else "en")
        linked = {x.rstrip("/") for x in re.findall(r'href="(/data/[^"#?.]+)"', h)}
        if rel in ("/", "/ko", "/ja"):
            items = [(p, t) for p, t, _ in DATASETS]
            box = _box(items, lang if lang in HEAD else "en", ALL_HEAD.get(lang, ALL_HEAD["en"]))
        else:
            self_path = rel if rel.startswith("/data/") else None
            items = related(self_path, linked) if self_path else []
            if len(items) < (4 if self_path else 3):
                items += [x for x in pick(_text(h), self_path, linked | {p for p, _ in items}, (4 if self_path else 3) - len(items)) if x not in items]
            box = _box(items, lang if lang in HEAD else "en", HEAD.get(lang, HEAD["en"]))
        h = h.replace(FOOT, box + FOOT, 1)
        open(fp, "w", encoding="utf-8").write(h)
        n += 1
    print(f"datalinks: added data links to {n} pages")
