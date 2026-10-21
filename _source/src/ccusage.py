# -*- coding: utf-8 -*-
"""Claude Code usage analyzer (/claude-code-usage, /ko/…, /ja/…).

The visitor picks their ~/.claude/projects folder; ccusage.js reads the session JSONL files in the
browser (nothing is uploaded), dedupes the assistant messages and prices every usage block at the
official API rates, then compares that with the Claude plan they pay for.
"""
import html

esc = lambda s: html.escape(str(s), quote=True)
SLUG = "claude-code-usage"
PATH = {"en": f"/{SLUG}", "ko": f"/ko/{SLUG}", "ja": f"/ja/{SLUG}"}
CHECKED = "2026-10-15"
PRICE_SRC = "https://platform.claude.com/docs/en/about-claude/pricing"
PLAN_SRC = "https://claude.com/pricing"
OPENAI_SRC = "https://developers.openai.com/api/docs/pricing"
# (model, input, cached input, output) per 1M tokens, OpenAI pricing page (short context), for Codex logs
OPENAI_ROWS = [("GPT-6 Astra", 10, 1, 50), ("GPT-6.1 Sol", 2, 0.10, 10), ("GPT-6 Sol", 2, 0.20, 10), ("GPT-6 Luna", 0.10, 0.01, 0.50),
               ("GPT-5.6 Sol", 4, 0.40, 20), ("GPT-5.6 Terra", 2, 0.20, 12), ("GPT-5.6 Luna", 0.20, 0.02, 1.20), ("GPT-5.5", 5, 0.50, 30),
               ("GPT-5.4", 2.5, 0.25, 15), ("GPT-5.3 Codex · 5.2", 1.75, 0.175, 14), ("GPT-5.1 · GPT-5", 1.25, 0.125, 10)]

CARD = "bg-zinc-900/70 backdrop-blur border border-zinc-800 rounded-2xl p-4 sm:p-5"
H2 = "text-xs uppercase tracking-wider text-zinc-500 font-semibold mb-4"
SEG_BTN = "tab py-1.5 px-2.5 rounded-md text-xs font-semibold text-zinc-400"

# (model, input, output, 5m write, 1h write, cache read) per 1M tokens, from the official pricing page
PRICE_ROWS = [
    ("Claude Fable 5.1 / Mythos 5.1", 10, 50, 12.5, 20, 0.25),
    ("Claude Fable 5 / Mythos 5", 10, 50, 12.5, 20, 1),
    ("Claude Opus 5.5", 4, 20, 5, 8, 0.20),
    ("Claude Opus 5 · 4.8 · 4.7 · 4.6 · 4.5", 5, 25, 6.25, 10, 0.50),
    ("Claude Opus 4.1 / 4", 15, 75, 18.75, 30, 1.50),
    ("Claude Sonnet 5.5", 2, 10, 2.5, 4, 0.10),
    ("Claude Sonnet 5", 2, 10, 2.5, 4, 0.20),
    ("Claude Sonnet 4.6 · 4.5 · 4", 3, 15, 3.75, 6, 0.30),
    ("Claude Haiku 5.5 (≤100K)", 0.10, 0.50, 0.125, 0.20, 0.01),
    ("Claude Haiku 4.5", 1, 5, 1.25, 2, 0.10),
    ("Claude Haiku 3.5", 0.80, 4, 1, 1.60, 0.08),
]

T = {
"en": dict(
  title="Claude Code Usage Analyzer – Also Codex & Cursor Cost",
  desc="Open your Claude Code or Codex log folder, or a Cursor usage CSV, and see the tokens and API-equivalent cost by day, project and model. Runs in your browser.",
  badge="New · free · nothing uploaded", h1="Usage Analyzer", h1sub="Claude Code · Codex · Cursor analyzer",
  sub="See how many tokens Claude Code, Codex and Cursor really used and what that would cost at API prices, by day, project and model, and whether your plan pays off.",
  privacy="Your files are read inside this browser tab. Nothing is sent to our server or anyone else. Close the tab and it's gone.",
  pickTitle="1. Open your usage logs",
  pickFolder="Choose folder", pickFiles="Choose files (.jsonl, .csv)", drop="or drag the folder here",
  pathTitle="Where the logs are",
  pathCodexTip="Codex (CLI and app) logs: pick the sessions folder. On Windows paste %USERPROFILE%\\.codex\\sessions.",
  pathCursorTip="Cursor doesn't keep token counts on your computer. Open cursor.com/dashboard → Usage → Export CSV and choose that file.",
  toolTitle="By tool",
  pathWin="Windows", pathMac="Mac", pathLinux="Linux",
  pathWinTip="In the folder picker, paste this into the address bar and press Enter.",
  pathMacTip="In the picker press ⌘ + Shift + G, paste the path and press Enter. (⌘ + Shift + . shows hidden folders.)",
  pathLinuxTip="If you set CLAUDE_CONFIG_DIR, use that folder's projects/ instead.",
  uploadNote="Chrome may ask “Upload files to this site?”. That's the browser's standard wording; the files stay on your computer.",
  copy="Copy", copied="Copied",
  reading="Reading {n} files…", readDone="{files} files · {msgs} replies · {sessions} sessions",
  noData="No usage found. Pick ~/.claude/projects or ~/.codex/sessions (.jsonl files), or a Cursor usage CSV.",
  resTitle="2. Your usage",
  pAll="All", p7="7 days", p30="30 days", pMonth="This month",
  kCost="API-equivalent cost", kCostSub="what the same tokens cost on the API",
  kTok="Tokens", kTokSub="{io} in/out · {cache} cache",
  kSave="Saved by caching", kSaveSub="vs paying full input price",
  kDays="Active days", kDaysSub="{from} – {to}",
  dailyTitle="Cost per day", projTitle="By project", modelTitle="By model",
  thName="Name", thReq="Replies", thTok="Tokens", thCost="Cost", thShare="Share",
  planTitle="3. Plan or API?", planPick="Your plan",
  plApi="API only (no plan)",
  planLine="For {days} days, {plan} costs about {fee}. The same usage on the API would be {api}.",
  planWin="Your plan is worth it: you got {pct} of the fee back in API value.",
  planLose="You used less than the fee: on the API this period would have cost {api} instead of {fee}.",
  planApi="On the API you'd pay {api} for this period ({month} per 30 days at this pace).",
  planNote="Plan fees exclude VAT. Plans have 5-hour and weekly usage limits, so heavy use may hit a limit before the API cost reaches this level.",
  csv="Download CSV (per day)", unpriced="Not priced (unknown model): {list}",
  howTitle="How it works",
  how=["Claude Code saves every conversation as a .jsonl file under ~/.claude/projects, one folder per project. Each reply has a usage block with input, output, cache-write and cache-read tokens and the model name.",
       "The same reply is often written on several lines (and copied again when you resume a session), so we count each reply once by its message and request ID.",
       "Each reply is priced at the official API rates for its model: base input, 5-minute and 1-hour cache writes, cache reads and output. Fast mode, US-only inference (1.1×), Haiku 5.5's long-prompt rate and web searches ($10 per 1,000) are included.",
       "By default Claude Code deletes logs older than 30 days. To keep more history, set \"cleanupPeriodDays\" in ~/.claude/settings.json.",
       "Codex writes a running token total into each session file under ~/.codex/sessions. We bill the increase between events at OpenAI's API prices, with cached input at the cached rate.",
       "Cursor no longer stores token counts on your computer, so we use the usage CSV from your Cursor dashboard and show the cost Cursor itself lists for each request."],
  srcTitle="API prices used (per 1M tokens)", thModel="Model", thIn="Input", thOut="Output", th5m="5m write", th1h="1h write", thRead="Cache read", srcOpenai="Codex: OpenAI API prices (per 1M tokens)", thCached="Cached input",
  srcNote=f"Checked {CHECKED} from Anthropic's pricing page. Batch discounts don't apply to Claude Code.",
  faqTitle="FAQ",
  faq=[("How do I check my Claude Code usage?", "Inside Claude Code, /usage (or /cost on the API) shows the current session and plan limits. To see history by day, project and model, open your ~/.claude/projects folder with this page."),
       ("Is my code or chat uploaded?", "No. The page reads the files with your browser's File API and only adds up the usage numbers. Your prompts and code never leave the tab."),
       ("Why is the API-equivalent cost so high on a Max plan?", "Claude Code re-reads your project on every turn, so it moves a lot of cached tokens. On a plan you pay a flat fee; this shows what the same tokens would cost if you paid per token."),
       ("Does it work like ccusage or CodeBurn?", "It reads the same local files those command-line tools read, but runs in the browser with no install, and adds the plan-vs-API comparison."),
       ("Why does it show only the last month?", "Claude Code removes logs older than 30 days unless you raise cleanupPeriodDays in settings.json."),
       ("Can I check Codex or Cursor usage too?", "Yes. For Codex pick ~/.codex/sessions. For Cursor, export the usage CSV from cursor.com/dashboard (Usage → Export CSV) and choose that file. You can load all three at once.")],
  related="Related", rel=[("/agents", "Claude Code monthly cost calculator"), ("/blog/claude-code-usage-limits", "Claude Code usage limits explained"), ("/blog/claude-code-save-tokens", "Ways to save tokens in Claude Code")],
  m_other="Other",
),
"ko": dict(
  title="Claude Code 사용량 분석기 – Codex·Cursor 비용도 확인",
  desc="Claude Code·Codex 기록 폴더나 Cursor 사용량 CSV를 넣으면 쓴 토큰과 API 환산 비용을 날짜·프로젝트·모델별로 보여 줍니다. 브라우저 안에서만 계산합니다.",
  badge="새 기능 · 무료 · 업로드 없음", h1="사용량 분석기", h1sub="Claude Code · Codex · Cursor 분석기",
  sub="Claude Code·Codex·Cursor가 실제로 쓴 토큰과 API 요금으로 환산한 비용을 날짜·프로젝트·모델별로 보고, 내 요금제가 이득인지 확인하세요.",
  privacy="파일은 이 브라우저 탭 안에서만 읽습니다. 저희 서버나 다른 곳으로 아무것도 보내지 않고, 탭을 닫으면 사라집니다.",
  pickTitle="1. 사용 기록 열기",
  pickFolder="폴더 선택", pickFiles="파일 선택 (.jsonl, .csv)", drop="또는 폴더를 여기로 끌어다 놓기",
  pathTitle="기록 위치",
  pathCodexTip="Codex(CLI·앱) 기록은 sessions 폴더를 고르세요. Windows는 %USERPROFILE%\\.codex\\sessions 를 붙여 넣으면 됩니다.",
  pathCursorTip="Cursor는 내 컴퓨터에 토큰 수를 남기지 않습니다. cursor.com/dashboard → Usage → Export CSV로 받은 파일을 고르세요.",
  toolTitle="도구별",
  pathWin="Windows", pathMac="Mac", pathLinux="Linux",
  pathWinTip="폴더 선택 창 위쪽 주소창에 이 경로를 붙여 넣고 Enter를 누르세요.",
  pathMacTip="선택 창에서 ⌘ + Shift + G를 누르고 경로를 붙여 넣은 뒤 Enter. (⌘ + Shift + . 을 누르면 숨김 폴더가 보입니다.)",
  pathLinuxTip="CLAUDE_CONFIG_DIR을 바꿨다면 그 폴더 안의 projects/를 고르세요.",
  uploadNote="Chrome이 \"이 사이트에 파일을 업로드할까요?\"라고 물을 수 있습니다. 브라우저의 기본 문구일 뿐이고, 파일은 내 컴퓨터 밖으로 나가지 않습니다.",
  copy="복사", copied="복사됨",
  reading="파일 {n}개 읽는 중…", readDone="파일 {files}개 · 응답 {msgs}개 · 세션 {sessions}개",
  noData="사용 기록을 찾지 못했습니다. ~/.claude/projects나 ~/.codex/sessions 폴더(.jsonl), 또는 Cursor 사용량 CSV를 골라 주세요.",
  resTitle="2. 내 사용량",
  pAll="전체", p7="7일", p30="30일", pMonth="이번 달",
  kCost="API 환산 비용", kCostSub="같은 토큰을 API로 냈을 때",
  kTok="토큰", kTokSub="입출력 {io} · 캐시 {cache}",
  kSave="캐시로 아낀 돈", kSaveSub="입력 정가로 냈을 때와 비교",
  kDays="사용한 날", kDaysSub="{from} – {to}",
  dailyTitle="날짜별 비용", projTitle="프로젝트별", modelTitle="모델별",
  thName="이름", thReq="응답", thTok="토큰", thCost="비용", thShare="비중",
  planTitle="3. 요금제가 이득일까, API가 이득일까?", planPick="내 요금제",
  plApi="API만 사용 (요금제 없음)",
  planLine="{days}일 동안 {plan} 요금은 약 {fee}이고, 같은 사용량을 API로 냈다면 {api}입니다.",
  planWin="요금제가 이득입니다. 낸 요금의 {pct}만큼 API 가치를 썼습니다.",
  planLose="요금보다 적게 썼습니다. 이 기간은 API로 냈다면 {fee} 대신 {api}였습니다.",
  planApi="이 기간 API 요금은 {api}입니다. 이 속도면 30일에 {month} 정도입니다.",
  planNote="요금제 금액은 부가세 별도입니다. 요금제에는 5시간·주간 사용 한도가 있어서, 많이 쓰면 API 환산 비용이 이만큼 되기 전에 한도에 걸릴 수 있습니다.",
  csv="CSV 내려받기 (날짜별)", unpriced="가격을 모르는 모델이라 빠진 것: {list}",
  howTitle="계산 방법",
  how=["Claude Code는 대화를 프로젝트별로 ~/.claude/projects 아래 .jsonl 파일에 저장합니다. 응답마다 입력·출력·캐시 쓰기·캐시 읽기 토큰과 모델 이름이 적혀 있습니다.",
       "같은 응답이 여러 줄에 나눠 저장되고, 세션을 이어서 열면 다시 복사되기도 해서 메시지 ID와 요청 ID로 응답 하나를 한 번만 셉니다.",
       "응답마다 그 모델의 공식 API 요금으로 계산합니다. 기본 입력, 5분·1시간 캐시 쓰기, 캐시 읽기, 출력 요금을 따로 적용하고 Fast 모드, 미국 전용 추론(1.1배), Haiku 5.5의 긴 프롬프트 요금, 웹 검색(1,000회당 10달러)도 넣었습니다.",
       "Claude Code는 기본적으로 30일이 지난 기록을 지웁니다. 더 오래 남기려면 ~/.claude/settings.json에 \"cleanupPeriodDays\"를 설정하세요.",
       "Codex는 ~/.codex/sessions 아래 세션 파일에 누적 토큰 수를 적습니다. 이벤트 사이에 늘어난 만큼을 OpenAI API 요금으로 계산하고, 캐시 입력은 캐시 단가로 계산합니다.",
       "Cursor는 이제 내 컴퓨터에 토큰 수를 남기지 않아서, Cursor 대시보드에서 받은 사용량 CSV를 읽고 요청마다 Cursor가 적은 금액을 그대로 씁니다."],
  srcTitle="사용한 API 요금 (100만 토큰당, 달러)", thModel="모델", thIn="입력", thOut="출력", th5m="5분 쓰기", th1h="1시간 쓰기", thRead="캐시 읽기", srcOpenai="Codex: OpenAI API 요금 (100만 토큰당, 달러)", thCached="캐시 입력",
  srcNote=f"{CHECKED} Anthropic 공식 요금 페이지 기준. Claude Code에는 배치 할인이 적용되지 않습니다.",
  faqTitle="자주 묻는 질문",
  faq=[("Claude Code 사용량은 어떻게 확인하나요?", "Claude Code 안에서 /usage(API는 /cost)를 입력하면 현재 세션과 요금제 한도가 나옵니다. 날짜·프로젝트·모델별 기록을 보려면 이 페이지에서 ~/.claude/projects 폴더를 열면 됩니다."),
       ("내 코드나 대화 내용이 업로드되나요?", "아니요. 브라우저의 파일 기능으로 읽어서 사용량 숫자만 더합니다. 프롬프트와 코드는 탭 밖으로 나가지 않습니다."),
       ("Max 요금제인데 API 환산 비용이 왜 이렇게 크게 나오나요?", "Claude Code는 매번 프로젝트를 다시 읽어서 캐시 토큰이 아주 많이 쌓입니다. 요금제는 정액이라 실제로 그만큼 내지 않고, 이 숫자는 같은 토큰을 토큰당 요금으로 냈을 때의 금액입니다."),
       ("ccusage나 CodeBurn과 뭐가 다른가요?", "같은 로컬 기록 파일을 읽지만, 설치 없이 브라우저에서 바로 열 수 있고 요금제와 API 비교를 함께 보여 줍니다."),
       ("왜 최근 한 달 정도만 나오나요?", "Claude Code가 30일 지난 기록을 지우기 때문입니다. settings.json에서 cleanupPeriodDays 값을 늘리면 더 오래 남습니다."),
       ("Codex나 Cursor 사용량도 볼 수 있나요?", "네. Codex는 ~/.codex/sessions 폴더를 고르면 됩니다. Cursor는 cursor.com/dashboard의 Usage에서 Export CSV로 받은 파일을 고르세요. 세 가지를 한 번에 넣어도 됩니다.")],
  related="함께 보기", rel=[("/ko/agents", "Claude Code 월 비용 계산기"), ("/ko/blog/claude-code-sayongnyang-hando", "Claude Code 사용량 한도 정리"), ("/ko/blog/claude-code-token-jeolyak", "Claude Code 토큰 절약법")],
  m_other="기타",
),
"ja": dict(
  title="Claude Code 使用量アナライザー – Codex・Cursor の費用も確認",
  desc="Claude Code・Codex の記録フォルダか Cursor の使用量 CSV を入れると、使ったトークンと API 換算の費用を日付・プロジェクト・モデル別に表示。ブラウザ内だけで計算します。",
  badge="新機能 · 無料 · アップロードなし", h1="使用量アナライザー", h1sub="Claude Code・Codex・Cursor アナライザー",
  sub="Claude Code・Codex・Cursor が実際に使ったトークンと、API 料金に換算した費用を日付・プロジェクト・モデル別に確認し、プランがお得か比べられます。",
  privacy="ファイルはこのブラウザのタブの中だけで読み込みます。当サイトのサーバーやほかの場所には何も送らず、タブを閉じれば消えます。",
  pickTitle="1. 使用記録を開く",
  pickFolder="フォルダを選択", pickFiles="ファイルを選択（.jsonl, .csv）", drop="またはフォルダをここにドラッグ",
  pathTitle="記録の場所",
  pathCodexTip="Codex（CLI・アプリ）の記録は sessions フォルダを選びます。Windows では %USERPROFILE%\\.codex\\sessions を貼り付けます。",
  pathCursorTip="Cursor はパソコンにトークン数を残しません。cursor.com/dashboard → Usage → Export CSV でダウンロードしたファイルを選びます。",
  toolTitle="ツール別",
  pathWin="Windows", pathMac="Mac", pathLinux="Linux",
  pathWinTip="フォルダ選択画面の上のアドレス欄にこのパスを貼り付けて Enter を押します。",
  pathMacTip="選択画面で ⌘ + Shift + G を押し、パスを貼り付けて Enter。（⌘ + Shift + . で隠しフォルダが表示されます）",
  pathLinuxTip="CLAUDE_CONFIG_DIR を変えている場合は、そのフォルダ内の projects/ を選びます。",
  uploadNote="Chrome が「このサイトにファイルをアップロードしますか？」と聞くことがあります。ブラウザの決まった文言で、ファイルはパソコンの外に出ません。",
  copy="コピー", copied="コピーしました",
  reading="{n}個のファイルを読み込み中…", readDone="ファイル {files}個 · 応答 {msgs}件 · セッション {sessions}個",
  noData="使用記録が見つかりませんでした。~/.claude/projects か ~/.codex/sessions（.jsonl）、または Cursor の使用量 CSV を選んでください。",
  resTitle="2. あなたの使用量",
  pAll="すべて", p7="7日", p30="30日", pMonth="今月",
  kCost="API 換算の費用", kCostSub="同じトークンを API で払った場合",
  kTok="トークン", kTokSub="入出力 {io} · キャッシュ {cache}",
  kSave="キャッシュで節約", kSaveSub="入力を定価で払った場合との差",
  kDays="使った日数", kDaysSub="{from} – {to}",
  dailyTitle="日別の費用", projTitle="プロジェクト別", modelTitle="モデル別",
  thName="名前", thReq="応答", thTok="トークン", thCost="費用", thShare="割合",
  planTitle="3. プランと API、どちらがお得？", planPick="あなたのプラン",
  plApi="API のみ（プランなし）",
  planLine="{days}日間の {plan} の料金は約 {fee}、同じ使用量を API で払うと {api} です。",
  planWin="プランのほうがお得です。払った料金の {pct} 分の API 価値を使いました。",
  planLose="料金より少ない使用量でした。この期間は API なら {fee} ではなく {api} でした。",
  planApi="この期間の API 料金は {api} です。このペースなら30日で約 {month} です。",
  planNote="プラン料金は税抜きです。プランには5時間・週ごとの使用上限があるため、たくさん使うと API 換算がこの金額になる前に上限に達することがあります。",
  csv="CSV をダウンロード（日別）", unpriced="料金が分からないモデルのため除外：{list}",
  howTitle="計算のしかた",
  how=["Claude Code は会話をプロジェクトごとに ~/.claude/projects の下の .jsonl ファイルに保存します。応答ごとに入力・出力・キャッシュ書き込み・キャッシュ読み込みのトークン数とモデル名が記録されています。",
       "同じ応答が複数の行に分かれて保存され、セッションを再開するとまたコピーされることもあるので、メッセージ ID とリクエスト ID で1つの応答を1回だけ数えます。",
       "応答ごとにそのモデルの公式 API 料金で計算します。基本の入力、5分・1時間のキャッシュ書き込み、キャッシュ読み込み、出力をそれぞれ適用し、Fast モード、米国内推論（1.1倍）、Haiku 5.5 の長いプロンプト料金、ウェブ検索（1,000回で10ドル）も含めています。",
       "Claude Code は初期設定で30日を過ぎた記録を削除します。もっと残すには ~/.claude/settings.json で \"cleanupPeriodDays\" を設定します。",
       "Codex は ~/.codex/sessions の下のセッションファイルに累計のトークン数を書きます。イベントの間に増えた分を OpenAI API 料金で計算し、キャッシュ入力はキャッシュ単価で計算します。",
       "Cursor はパソコンにトークン数を残さなくなったため、Cursor のダッシュボードからダウンロードした使用量 CSV を読み、リクエストごとに Cursor が記載した金額をそのまま使います。"],
  srcTitle="使用した API 料金（100万トークンあたり、ドル）", thModel="モデル", thIn="入力", thOut="出力", th5m="5分書き込み", th1h="1時間書き込み", thRead="キャッシュ読み込み", srcOpenai="Codex：OpenAI API 料金（100万トークンあたり、ドル）", thCached="キャッシュ入力",
  srcNote=f"{CHECKED} Anthropic 公式料金ページ時点。Claude Code にはバッチ割引は適用されません。",
  faqTitle="よくある質問",
  faq=[("Claude Code の使用量はどう確認する？", "Claude Code の中で /usage（API なら /cost）を入力すると、今のセッションとプランの上限が表示されます。日付・プロジェクト・モデル別の履歴を見るには、このページで ~/.claude/projects フォルダを開きます。"),
       ("コードや会話の内容はアップロードされる？", "いいえ。ブラウザのファイル機能で読み込み、使用量の数字だけを合計します。プロンプトやコードはタブの外に出ません。"),
       ("Max プランなのに API 換算の費用がなぜこんなに高い？", "Claude Code は毎回プロジェクトを読み直すので、キャッシュのトークンがとても多くなります。プランは定額なので実際にその額を払うわけではなく、この数字は同じトークンをトークン単位の料金で払った場合の金額です。"),
       ("ccusage や CodeBurn と何が違う？", "同じローカルの記録ファイルを読みますが、インストールなしでブラウザから使え、プランと API の比較も表示します。"),
       ("なぜ最近1か月ほどしか出ない？", "Claude Code が30日を過ぎた記録を削除するためです。settings.json で cleanupPeriodDays を増やすと長く残ります。"),
       ("Codex や Cursor の使用量も見られる？", "はい。Codex は ~/.codex/sessions フォルダを選びます。Cursor は cursor.com/dashboard の Usage で Export CSV からダウンロードしたファイルを選びます。3つ同時に入れても大丈夫です。")],
  related="関連ページ", rel=[("/ja/agents", "Claude Code 月額コスト計算機"), ("/ja/blog/claude-code-shiyouryou-jougen", "Claude Code の使用量上限まとめ"), ("/ja/blog/claude-code-token-setsuyaku", "Claude Code のトークン節約術")],
  m_other="その他",
),
}

from ccusage_i18n import extra as _extra
T.update(_extra(CHECKED))
from ccusage_deep import DEEP as _DEEP, RUNTIME as _DEEP_RT
PATH.update({"tr": f"/tr/{SLUG}", "uk": f"/uk/{SLUG}", "zh-CN": f"/zh-cn/{SLUG}"})

RUNTIME = ["copy", "copied", "reading", "readDone", "noData", "kTokSub", "kDaysSub", "thName", "thReq", "thTok", "thCost", "thShare",
           "plApi", "planLine", "planWin", "planLose", "planApi", "unpriced", "m_other"] + _DEEP_RT
for _l in T:
    T[_l].update(_DEEP[_l])
    T[_l]["planTitle"] = T[_l]["planTitle"].replace("3.", "4.", 1)


def _seg(id_, opts, active):
    btns = "".join(f'<button data-v="{v}" class="{SEG_BTN}{" tab-active" if v == active else ""}">{esc(l)}</button>' for v, l in opts)
    return f'<div id="{id_}" class="inline-flex flex-wrap p-1 bg-zinc-950/70 border border-zinc-800 rounded-lg gap-1">{btns}</div>'


def _path_row(os_, tip, path):
    return (f'<div class="rounded-xl bg-zinc-950/60 border border-zinc-800 p-3 min-w-0">'
            f'<div class="text-xs font-bold text-zinc-200 mb-1.5">{esc(os_)}</div>'
            f'<div class="flex items-center gap-2"><code class="ltr flex-1 min-w-0 truncate text-xs text-violet-200 bg-zinc-900 border border-zinc-800 rounded-md px-2 py-1 select-all">{esc(path)}</code>'
            f'<button data-copy="{esc(path)}" class="shrink-0 text-[11px] font-semibold px-2 py-1 rounded-md border border-zinc-700 text-zinc-300 hover:bg-zinc-800">COPY</button></div>'
            f'<p class="text-[11px] text-zinc-500 mt-1.5">{esc(tip)}</p></div>')


def build_page(lang):
    t = T[lang]
    e = lambda k: esc(t[k])
    paths = (_path_row("Claude Code · " + t["pathWin"], t["pathWinTip"], r"%USERPROFILE%\.claude\projects") +
             _path_row("Claude Code · " + t["pathMac"] + " / " + t["pathLinux"], t["pathMacTip"], "~/.claude/projects") +
             _path_row("Codex", t["pathCodexTip"], "~/.codex/sessions") +
             _path_row("Cursor", t["pathCursorTip"], "https://cursor.com/dashboard"))
    period = _seg("ccPeriod", [("all", t["pAll"]), ("7", t["p7"]), ("30", t["p30"]), ("month", t["pMonth"])], "all")
    plan_opts = [("Claude Code", [("pro", "Claude Pro · $20"), ("max5", "Claude Max 5× · $100"), ("max20", "Claude Max 20× · $200")]),
                 ("Codex", [("plus", "ChatGPT Plus · $20"), ("gpro100", "ChatGPT Pro 100 · $100"), ("gpro200", "ChatGPT Pro 200 · $200")]),
                 ("Cursor", [("cpremium", "Cursor Premium · $30"), ("csuper", "Cursor Super · $100"), ("cultra", "Cursor Ultra · $200"), ("cteams", "Cursor Teams Standard · $40"), ("cteamsp", "Cursor Teams Premium · $120")])]
    plan = ('<select id="ccPlanSel" class="bg-zinc-950/70 border border-zinc-800 rounded-lg px-3 py-1.5 text-sm">' +
            "".join(f'<optgroup label="{esc(g)}">' + "".join(f'<option value="{v}">{esc(l)}</option>' for v, l in o) + '</optgroup>' for g, o in plan_opts) +
            f'<option value="api">{e("plApi")}</option></select>')
    kpi = lambda id_, lab, sub: (f'<div class="rounded-xl bg-zinc-950/60 border border-zinc-800 p-3 min-w-0"><div class="text-[11px] text-zinc-500 font-semibold">{esc(lab)}</div>'
                                 f'<div id="{id_}" class="text-xl sm:text-2xl font-extrabold text-white tabular-nums mt-1 truncate">–</div><div id="{id_}Sub" class="text-[11px] text-zinc-500 mt-0.5 leading-snug">{esc(sub)}</div></div>')
    how = "".join(f"<li>{esc(x)}</li>" for x in t["how"])
    fmt = lambda v: f"${v:g}" if v >= 1 and v == int(v) else "$" + (f"{v:.3f}".rstrip("0") if len(f"{v:.3f}".rstrip("0").split(".")[1]) > 2 else f"{v:.2f}")
    prices = "".join(f'<tr class="border-t border-zinc-800"><td class="py-1.5 pe-3 font-semibold whitespace-nowrap">{esc(n)}</td>' +
                     "".join(f'<td class="py-1.5 pe-3 tabular-nums text-zinc-300">{fmt(v)}</td>' for v in vals) + "</tr>"
                     for n, *vals in PRICE_ROWS)
    oprices = "".join(f'<tr class="border-t border-zinc-800"><td class="py-1.5 pe-3 font-semibold whitespace-nowrap">{esc(n)}</td>' +
                      "".join(f'<td class="py-1.5 pe-3 tabular-nums text-zinc-300">{fmt(v)}</td>' for v in vals) + "</tr>" for n, *vals in OPENAI_ROWS)
    faq = "".join(f'<details class="border-t border-zinc-800 py-3"><summary class="cursor-pointer font-semibold text-zinc-200">{esc(q)}</summary><p class="mt-2 text-zinc-400">{esc(a)}</p></details>' for q, a in t["faq"])
    rel = " · ".join(f'<a href="{p}" class="text-violet-300 hover:text-white underline underline-offset-2">{esc(n)}</a>' for p, n in t["rel"])
    body = f'''    <header class="text-center mb-8">
      <div class="flex justify-center"><div class="inline-flex items-center gap-2 text-xs font-medium text-violet-300 bg-violet-500/10 border border-violet-500/20 rounded-full px-3 py-1 mb-4"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>{e("badge")}</div></div>
      <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight bg-gradient-to-r from-white via-violet-200 to-indigo-300 bg-clip-text text-transparent leading-tight pb-1">{e("h1")}</h1>
      <p class="mt-2 text-base sm:text-lg font-semibold text-violet-300">{e("h1sub")}</p>
      <p class="mt-3 text-zinc-400 text-sm sm:text-base max-w-2xl mx-auto">{e("sub")}</p>
      <p class="mt-4 text-sm text-emerald-200/90 max-w-2xl mx-auto border border-emerald-500/30 bg-emerald-500/5 rounded-xl px-4 py-3 text-start">🔒 {e("privacy")}</p>
    </header>

    <section class="{CARD}">
      <h2 class="{H2}">{e("pickTitle")}</h2>
      <div id="ccDrop" class="rounded-2xl border-2 border-dashed border-zinc-700 bg-zinc-950/40 p-6 text-center transition-colors">
        <div class="flex flex-wrap justify-center gap-2">
          <label class="cursor-pointer text-sm font-semibold px-4 py-2 rounded-lg bg-violet-600 hover:bg-violet-500 text-white">📁 {e("pickFolder")}<input id="ccDir" type="file" webkitdirectory directory multiple class="hidden"></label>
          <label class="cursor-pointer text-sm font-semibold px-4 py-2 rounded-lg border border-zinc-700 text-zinc-200 hover:bg-zinc-800">📄 {e("pickFiles")}<input id="ccFiles" type="file" accept=".jsonl,.csv" multiple class="hidden"></label>
        </div>
        <p class="text-xs text-zinc-500 mt-3">{e("drop")}</p>
        <p id="ccStatus" class="text-sm text-zinc-300 mt-3 min-h-[1.25rem]" aria-live="polite"></p>
      </div>
      <h3 class="text-xs font-semibold text-zinc-400 mt-5 mb-2">{e("pathTitle")}</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3">{paths}</div>
      <p class="text-[11px] text-zinc-500 mt-3">{e("uploadNote")}</p>
    </section>

    <section class="{CARD} mt-5">
      <div class="flex flex-wrap items-center justify-between gap-3">
        <h2 class="text-xs uppercase tracking-wider text-zinc-500 font-semibold">{e("pjTitle")}</h2>
        <div class="flex items-center gap-2"><span class="text-xs text-zinc-500">{e("pjModelLbl")}</span><select id="pjModel" class="bg-zinc-950/70 border border-zinc-800 rounded-lg px-3 py-1.5 text-sm"><option value="opus">Claude Opus 5.5</option><option value="sonnet">Claude Sonnet 5.5</option><option value="terra">GPT-5.6 Terra (Codex)</option></select></div>
      </div>
      <p class="text-sm text-zinc-400 mt-2">{e("pjSub")}</p>
      <div class="flex flex-wrap items-center gap-3 mt-4">
        <label class="cursor-pointer text-sm font-semibold px-4 py-2 rounded-lg border border-violet-500/50 bg-violet-500/10 text-violet-100 hover:bg-violet-500/20">🗂 {e("pjPick")}<input id="pjDir" type="file" webkitdirectory directory multiple class="hidden"></label>
        <p id="pjStatus" class="text-sm text-zinc-300" aria-live="polite"></p>
      </div>
      <div id="pjResult" hidden class="mt-5">
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-3">
          {kpi("pjK1", t["pjK1"], "")}
          {kpi("pjK2", t["pjK2"], "")}
          {kpi("pjK3", t["pjK3"], "")}
          {kpi("pjK4", t["pjK4"], "")}
        </div>
        <h3 class="text-sm font-bold text-zinc-100 mt-6 mb-3">💡 {e("pjCardsTitle")}</h3>
        <div id="pjCards" class="grid grid-cols-1 lg:grid-cols-2 gap-3"></div>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-5 mt-6">
          <div class="min-w-0"><h3 class="text-xs font-semibold text-zinc-400 mb-2">{e("pjFoldTitle")}</h3><div id="pjFolders" class="overflow-x-auto"></div></div>
          <div class="min-w-0"><h3 class="text-xs font-semibold text-zinc-400 mb-2">{e("pjBigTitle")}</h3><div id="pjBig" class="overflow-x-auto"></div></div>
        </div>
        <p class="text-[11px] text-zinc-500 mt-3">{e("pjNote")}</p>
      </div>
    </section>

    <div id="ccResult" hidden>
    <section class="{CARD} mt-5">
      <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
        <h2 class="text-xs uppercase tracking-wider text-zinc-500 font-semibold">{e("resTitle")}</h2>
        {period}
      </div>
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3">
        {kpi("ccKCost", t["kCost"], t["kCostSub"])}
        {kpi("ccKTok", t["kTok"], "")}
        {kpi("ccKSave", t["kSave"], t["kSaveSub"])}
        {kpi("ccKDays", t["kDays"], "")}
      </div>
      <div id="ccToolWrap" hidden class="mt-6"><h3 class="text-xs font-semibold text-zinc-400 mb-2">{e("toolTitle")}</h3><div id="ccTool" class="overflow-x-auto"></div></div>
      <h3 class="text-xs font-semibold text-zinc-400 mt-6 mb-2">{e("dailyTitle")}</h3>
      <div id="ccDaily" class="overflow-x-auto"></div>
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-5 mt-6">
        <div class="min-w-0"><h3 class="text-xs font-semibold text-zinc-400 mb-2">{e("projTitle")}</h3><div id="ccProj" class="overflow-x-auto"></div></div>
        <div class="min-w-0"><h3 class="text-xs font-semibold text-zinc-400 mb-2">{e("modelTitle")}</h3><div id="ccModel" class="overflow-x-auto"></div></div>
      </div>
      <p id="ccUnpriced" class="text-[11px] text-amber-300/80 mt-3" hidden></p>
      <div class="mt-4 flex justify-end"><button id="ccCsv" class="text-xs font-semibold px-3 py-1.5 rounded-lg border border-violet-500/40 bg-violet-500/10 text-violet-200 hover:bg-violet-500/20">⬇ {e("csv")}</button></div>
    </section>

    <section id="ccDeep" class="{CARD} mt-5" hidden>
      <h2 class="text-xs uppercase tracking-wider text-zinc-500 font-semibold">{e("dTitle")}</h2>
      <p class="text-sm text-zinc-400 mt-2 mb-4">{e("dSub")}</p>
      <h3 class="text-sm font-bold text-zinc-100 mb-3">💡 {e("cardsTitle")}</h3>
      <div id="ccCards" class="grid grid-cols-1 lg:grid-cols-2 gap-3"></div>
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-5 mt-6">
        <div class="min-w-0"><h3 class="text-xs font-semibold text-zinc-400 mb-2">{e("dToolTitle")}</h3><div id="ccDeepTable" class="overflow-x-auto"></div></div>
        <div class="min-w-0"><h3 class="text-xs font-semibold text-zinc-400 mb-2">{e("heavyTitle")}</h3><div id="ccHeavy" class="overflow-x-auto"></div></div>
      </div>
      <p class="text-[11px] text-zinc-500 mt-3">{e("dNote")}</p>
      <div id="ccEff" hidden class="mt-8 pt-6 border-t border-zinc-800">
        <h3 class="text-sm font-bold text-zinc-100">⚙️ {e("eTitle")}</h3>
        <p class="text-sm text-zinc-400 mt-1 mb-4">{e("eSub")}</p>
        <div id="ccEffTiles" class="grid grid-cols-2 lg:grid-cols-4 gap-3"></div>
        <div id="ccEffCards" class="grid grid-cols-1 lg:grid-cols-2 gap-3 mt-4"></div>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-5 mt-6">
          <div class="min-w-0"><h3 class="text-xs font-semibold text-zinc-400 mb-2">{e("eSessTitle")}</h3><div id="ccEffSess" class="overflow-x-auto"></div></div>
          <div class="min-w-0"><h3 class="text-xs font-semibold text-zinc-400 mb-2">{e("eFailTitle")}</h3><div id="ccEffFail" class="overflow-x-auto"></div></div>
        </div>
        <p class="text-[11px] text-zinc-500 mt-3">{e("eNote")}</p>
      </div>
    </section>

    <section class="{CARD} mt-5">
      <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
        <h2 class="text-xs uppercase tracking-wider text-zinc-500 font-semibold">{e("planTitle")}</h2>
        <div class="flex items-center gap-2"><span class="text-xs text-zinc-500">{e("planPick")}</span>{plan}</div>
      </div>
      <div id="ccPlanOut" class="text-sm text-zinc-200 space-y-2"></div>
      <p class="text-[11px] text-zinc-500 mt-3">{e("planNote")}</p>
    </section>
    </div>

    <section class="prose-ts mt-12 max-w-3xl mx-auto bg-zinc-900/40 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <h2 style="margin-top:0">{e("howTitle")}</h2>
      <ul>{how}</ul>
      <h2>{e("srcTitle")}</h2>
      <div class="overflow-x-auto"><table class="text-sm w-full"><thead><tr><th class="text-start">{e("thModel")}</th><th class="text-start">{e("thIn")}</th><th class="text-start">{e("thOut")}</th><th class="text-start">{e("th5m")}</th><th class="text-start">{e("th1h")}</th><th class="text-start">{e("thRead")}</th></tr></thead><tbody>{prices}</tbody></table></div>
      <h3>{e("srcOpenai")}</h3>
      <div class="overflow-x-auto"><table class="text-sm w-full"><thead><tr><th class="text-start">{e("thModel")}</th><th class="text-start">{e("thIn")}</th><th class="text-start">{e("thCached")}</th><th class="text-start">{e("thOut")}</th></tr></thead><tbody>{oprices}</tbody></table></div>
      <p class="text-xs text-zinc-500">{e("srcNote")} <a href="{PRICE_SRC}" rel="nofollow noopener" target="_blank">Anthropic pricing</a> · <a href="{OPENAI_SRC}" rel="nofollow noopener" target="_blank">OpenAI pricing</a> · <a href="{PLAN_SRC}" rel="nofollow noopener" target="_blank">Claude plans</a></p>
      <h2>{e("faqTitle")}</h2>
      <div class="text-sm">{faq}</div>
      <p class="text-sm mt-6">{e("related")}: {rel}</p>
    </section>'''
    faq_ld = {"@type": "FAQPage", "inLanguage": lang, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    return dict(path=PATH[lang], title=t["title"], desc=t["desc"], h1=t["h1"], body=body, faq_ld=faq_ld,
                cc={k: t[k] for k in RUNTIME})
