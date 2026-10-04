# -*- coding: utf-8 -*-
"""AI game cost estimator page (/ai-game-cost-calculator, /ko/…, /ja/…).

A few questions size a 2D game; gamecost.js turns that into an asset list, cost/time/tokens in three
two scenarios (solo + AI default stack, your own tools) and a ready-to-use prompt pack.
"""
import html

esc = lambda s: html.escape(str(s), quote=True)
SLUG = "ai-game-cost-calculator"
PATH = {"en": f"/{SLUG}", "ko": f"/ko/{SLUG}", "ja": f"/ja/{SLUG}"}
CHECKED = "2026-10-05"

GENRES = ["merge", "puzzle", "racing", "idle", "platformer", "rpg", "novel", "shooter"]
FEATS = ["ads", "iap", "save", "rank", "online"]

T = {
"en": dict(
  title="AI Game Cost Calculator – 2D Game Budget", desc="How much does it cost to make a 2D game with AI? Answer 8 questions and get the asset list, cost, time, tokens and ready-to-use prompts.",
  badge="New · free · no sign-up", h1="AI Game Cost Calculator",
  sub="Answer a few questions about your 2D game. Get the asset list, the cost and time to build it with AI tools, the tokens, and a prompt pack to start building today.",
  qProject="Your game", name="Game name", namePh="e.g. Cat Merge Café", idea="One-line idea", ideaPh="e.g. merge cat furniture to decorate a café",
  qGenre="Genre", qScale="Size", sS="Small", sSsub="≈ 2 weeks solo", sM="Medium", sMsub="≈ 4 weeks", sL="Large", sLsub="≈ 6 weeks",
  qStyle="Art style", stPixel="Pixel art", stIllust="Illustration", stSimple="Simple / vector",
  qDim="Look", d2="2D", d3="2.5D / 3D models",
  qChars="Characters / enemies", qAnim="Animation", aNone="None", aSimple="Simple (3 moves)", aFull="Full (6 moves)",
  qMusic="Music tracks", qSfx="Sound effects", sfFew="Few", sfNormal="Normal", sfMany="Many", qVoice="Voice lines",
  qFeats="Features", qLangs="Languages", qEngine="Engine", qTrailer="Promo trailer", yes="Yes", no="No",
  qTools="Your tools", qImg="Images", qCode="Coding", qModel="API model",
  resTitle="What your game needs", cmpTitle="Cost and time with AI",
  promptTitle="Your prompt pack", promptSub="Built from your answers. Asset prompts are in English because image, music and sound tools work best in English.",
  tDev="Dev kickoff", tArt="Art", tMusic="Music", tSfx="Sound effects", tTrailer="Trailer", copy="Copy", download="Download all (.md)",
  howTitle="How the estimate works",
  how=["Sizes are anchored on real solo builds made with AI coding agents: a small mobile game took about 2 weeks, a medium one about 4 and a large one about 6. Genre, features, languages and 3D change those numbers.",
       "Images = characters × animation frames + backgrounds + items + UI. We assume you keep about 1 in 3 generations, so the number of generations is three times the number of images.",
       "Coding tokens assume an agent like Claude Code works about 70% of the days and reads around 20M tokens a day, most of it cached context. The API cost uses today's list price for the model you pick; subscriptions are charged per month."],
  srcTitle="Tool prices used", srcNote=f"Checked {CHECKED}. Prices change often — check each tool's pricing page before you buy.",
  faqTitle="FAQ",
  faq=[("How much does it cost to make a 2D game with AI?", "For a small mobile game, one person with AI tools usually spends about $100–300 in subscriptions and API fees and 2–3 weeks of work. Use the calculator above for your own genre and size."),
       ("Which AI tools do I need to make a game?", "Usually four: an image tool for sprites and backgrounds (Midjourney, PixelLab, Scenario or an image API), a music tool (Suno), a sound effects tool (ElevenLabs) and a coding agent (Claude Code or Cursor). Meshy helps if you want 3D models, Higgsfield for a promo video."),
       ("How many tokens does it take to code a game with Claude Code?", "Agents re-read your project a lot, so a 2-week build can pass a few hundred million tokens, mostly cached. On a Claude Max plan you pay a flat monthly fee; on the API the calculator shows the cost for the model you choose."),
       ("Are the prompts free to use?", "Yes. Copy them or download the whole pack as a Markdown file and paste them into your tools. Nothing you type is uploaded.")],
  defName="My Game", defIdea="a {genre} game for mobile",
  g_merge="Merge", g_puzzle="Puzzle", g_racing="Racing", g_idle="Idle", g_platformer="Platformer", g_rpg="RPG", g_novel="Visual novel", g_shooter="Shooter",
  f_ads="Ads", f_iap="In-app purchases", f_save="Save / load", f_rank="Leaderboard", f_online="Online multiplayer",
  devIntro="You are a senior game developer. Help me build \"{name}\", a 2D {genre} mobile game in {engine}.",
  devIdea="Idea:", devScope="Scope: {chars} characters, {bg} backgrounds, {items} items, {music} music tracks, {sfx} sound effects, {langs} language(s).",
  devFeats="Features:", devRules="Rules: keep the code simple and modular; one feature per step; after each step tell me how to test it on my phone; use placeholder shapes until I give you the real art.",
  devSteps="Build it in these steps:", st1="Project setup, folder structure, scene flow (title → game → result)", st2="Core gameplay loop with placeholder art",
  st3="Scoring, progression and difficulty curve", st4="UI: menus, HUD, pause, settings", st5="Add: {feats}", st6="Hook up the real art, music and sound effects", st7="Polish, performance check and build for Android",
  devStart="Start with step 1. Ask me anything you need before writing code.",
  rImages="Images", rImagesSub="{chars} chars · {frames} frames · {bg} bg · {items} items · {ui} UI", rAudio="Music + SFX", rAudioSub="tracks + effects",
  rCode="Lines of code", rCodeSub="estimated", rTokens="Coding tokens", rTokensSub="≈ {api} on the API",
  l_art="Art", l_music="Music", l_sfx="SFX / voice", l_code="Code", l_d3="3D models", l_trailer="Trailer",
  cAi="Solo + AI (typical tools)", cMine="Your tools",
  days="{n} days", capWarn="This plan's usage limit is likely too low for daily agent coding — expect waits or extra usage.",
  hireRef="For reference: hiring freelancers for a game this size usually starts at <b>{min}+</b>, and quotes can differ by 10× or more depending on country and quality.",
  noTrailer="Turn on “Promo trailer” to get trailer prompts.",
  copied="Copied ✓", packTitle="prompt pack",
  related="Related", rel=[("/agents", "Claude Code monthly cost"), ("/image", "AI image cost per image"), ("/compare/performance", "AI model capability vs price")],
),
"ko": dict(
  title="AI 게임 제작 비용 계산기 – 2D 게임 견적", desc="AI로 2D 게임 만들면 얼마나 들까? 질문 8개에 답하면 에셋 목록, 비용, 기간, 토큰, 바로 쓰는 프롬프트까지 나옵니다.",
  badge="신규 · 무료 · 가입 없음", h1="AI 게임 제작 비용 계산기",
  sub="만들 2D 게임에 대해 몇 가지만 답하세요. 필요한 에셋 목록, AI 도구로 만들 때의 비용·기간, 토큰, 그리고 바로 시작할 수 있는 프롬프트 묶음을 드립니다.",
  qProject="내 게임", name="게임 이름", namePh="예: 냥냥 머지 카페", idea="한 줄 설명", ideaPh="예: 고양이 가구를 합쳐 카페를 꾸미는 게임",
  qGenre="장르", qScale="규모", sS="소형", sSsub="1인 약 2주", sM="중형", sMsub="약 4주", sL="대형", sLsub="약 6주",
  qStyle="그림 스타일", stPixel="픽셀아트", stIllust="일러스트", stSimple="단순·벡터",
  qDim="표현 방식", d2="2D", d3="2.5D / 3D 모델",
  qChars="캐릭터·적 수", qAnim="애니메이션", aNone="없음", aSimple="간단 (동작 3개)", aFull="풍부 (동작 6개)",
  qMusic="배경음악 곡 수", qSfx="효과음", sfFew="적게", sfNormal="보통", sfMany="많이", qVoice="대사 음성 수",
  qFeats="기능", qLangs="지원 언어 수", qEngine="엔진", qTrailer="홍보 트레일러", yes="필요", no="없음",
  qTools="내가 쓸 도구", qImg="이미지", qCode="코딩", qModel="API 모델",
  resTitle="이 게임에 필요한 것", cmpTitle="AI로 만들 때 비용과 기간",
  promptTitle="프롬프트 묶음", promptSub="답변을 바탕으로 만들었습니다. 그림·음악·효과음 도구는 영어 프롬프트가 가장 잘 먹혀서 에셋 프롬프트는 영어로 드립니다.",
  tDev="개발 시작", tArt="그림", tMusic="음악", tSfx="효과음", tTrailer="트레일러", copy="복사", download="전체 받기 (.md)",
  howTitle="계산 방식",
  how=["규모 기준은 AI 코딩 에이전트로 실제 1인 개발한 게임입니다. 소형 모바일 게임 약 2주, 중형 약 4주, 대형 약 6주가 걸렸고, 장르·기능·언어 수·3D 여부에 따라 늘거나 줄어듭니다.",
       "이미지 수 = 캐릭터 × 애니메이션 프레임 + 배경 + 아이템 + UI입니다. 생성한 것 중 3장에 1장 정도를 쓴다고 보고, 생성 횟수는 이미지 수의 3배로 잡았습니다.",
       "코딩 토큰은 Claude Code 같은 에이전트가 전체 기간의 70% 동안 하루 약 2천만 토큰(대부분 캐시된 맥락)을 읽는다고 가정합니다. API 비용은 고른 모델의 현재 정가, 구독은 월 단위로 계산합니다."],
  srcTitle="사용한 도구 가격", srcNote=f"{CHECKED} 기준. 가격이 자주 바뀌니 결제 전 각 도구의 가격 페이지를 확인하세요.",
  faqTitle="자주 묻는 질문",
  faq=[("AI로 2D 게임을 만들면 비용이 얼마나 드나요?", "소형 모바일 게임이면 혼자 AI 도구를 써서 구독료와 API 비용으로 약 $100~300, 기간은 2~3주 정도입니다. 장르와 규모를 넣어 위 계산기로 확인해 보세요."),
       ("게임 만들 때 어떤 AI 도구가 필요한가요?", "보통 네 가지입니다. 스프라이트·배경용 이미지 도구(Midjourney, PixelLab, Scenario, 이미지 API), 음악 도구(Suno), 효과음 도구(ElevenLabs), 코딩 에이전트(Claude Code, Cursor)입니다. 3D 모델이 필요하면 Meshy, 홍보 영상은 Higgsfield를 씁니다."),
       ("Claude Code로 게임을 만들면 토큰이 얼마나 드나요?", "에이전트는 프로젝트를 반복해서 읽기 때문에 2주짜리 개발에도 수억 토큰이 오가고, 대부분은 캐시입니다. Claude Max 구독이면 월 정액이고, API로 쓰면 고른 모델 기준 비용을 계산기가 보여 줍니다."),
       ("프롬프트는 무료로 써도 되나요?", "네. 복사하거나 전체를 Markdown 파일로 받아 각 도구에 붙여 넣으면 됩니다. 입력한 내용은 어디에도 업로드되지 않습니다.")],
  defName="내 게임", defIdea="모바일 {genre} 게임",
  g_merge="머지", g_puzzle="퍼즐", g_racing="레이싱", g_idle="방치형", g_platformer="플랫포머", g_rpg="RPG", g_novel="비주얼노벨", g_shooter="슈팅",
  f_ads="광고", f_iap="인앱 결제", f_save="저장·불러오기", f_rank="랭킹", f_online="온라인 대전",
  devIntro="당신은 숙련된 게임 개발자입니다. {engine}로 2D 모바일 {genre} 게임 \"{name}\"을 함께 만들어 주세요.",
  devIdea="아이디어:", devScope="규모: 캐릭터 {chars}종, 배경 {bg}장, 아이템 {items}개, 배경음악 {music}곡, 효과음 {sfx}개, 지원 언어 {langs}개.",
  devFeats="기능:", devRules="규칙: 코드는 단순하고 모듈 단위로 나눠 주세요. 한 단계에 기능 하나씩 만들고, 단계가 끝날 때마다 휴대폰에서 테스트하는 방법을 알려 주세요. 진짜 그림을 드리기 전까지는 도형으로 임시 그래픽을 써 주세요.",
  devSteps="다음 순서로 만들어 주세요:", st1="프로젝트 설정, 폴더 구조, 화면 흐름 (타이틀 → 게임 → 결과)", st2="임시 그래픽으로 핵심 게임 루프",
  st3="점수, 진행, 난이도 곡선", st4="UI: 메뉴, 게임 화면 정보, 일시정지, 설정", st5="추가 기능: {feats}", st6="실제 그림·음악·효과음 연결", st7="다듬기, 성능 점검, 안드로이드 빌드",
  devStart="1단계부터 시작해 주세요. 코드를 쓰기 전에 필요한 건 먼저 물어봐 주세요.",
  rImages="이미지", rImagesSub="캐릭터 {chars} · 프레임 {frames} · 배경 {bg} · 아이템 {items} · UI {ui}", rAudio="음악 + 효과음", rAudioSub="곡 + 효과음",
  rCode="코드 줄 수", rCodeSub="추정", rTokens="코딩 토큰", rTokensSub="API로 하면 약 {api}",
  l_art="그림", l_music="음악", l_sfx="효과음·음성", l_code="코딩", l_d3="3D 모델", l_trailer="트레일러",
  cAi="1인 + AI (대표 도구)", cMine="내 도구 조합",
  days="{n}일", capWarn="이 요금제의 사용량 한도는 매일 에이전트로 코딩하기엔 부족할 가능성이 큽니다. 대기 시간이나 추가 사용료를 예상하세요.",
  hireRef="참고: 같은 규모를 외주로 맡기면 보통 <b>{min} 이상</b>이 들며, 나라와 퀄리티에 따라 10배 넘게 차이 납니다.",
  noTrailer="'홍보 트레일러'를 켜면 트레일러 프롬프트가 나옵니다.",
  copied="복사됨 ✓", packTitle="프롬프트 묶음",
  related="함께 보기", rel=[("/ko/agents", "Claude Code 월 비용 계산기"), ("/ko/image", "AI 이미지 장당 비용"), ("/ko/compare/performance", "AI 모델 성능 vs 가격 순위")],
),
"ja": dict(
  title="AIゲーム制作費計算機 – 2Dゲームの見積もり", desc="AIで2Dゲームを作るといくら？8つの質問に答えると、素材リスト・費用・期間・トークン・すぐ使えるプロンプトが出ます。",
  badge="新機能 · 無料 · 登録不要", h1="AIゲーム制作費計算機",
  sub="作りたい2Dゲームについていくつか答えるだけ。必要な素材リスト、AIツールで作る場合の費用・期間、トークン数、すぐ始められるプロンプト集をお届けします。",
  qProject="あなたのゲーム", name="ゲーム名", namePh="例：ねこマージカフェ", idea="一行説明", ideaPh="例：猫の家具を合体させてカフェを飾る",
  qGenre="ジャンル", qScale="規模", sS="小規模", sSsub="1人で約2週間", sM="中規模", sMsub="約4週間", sL="大規模", sLsub="約6週間",
  qStyle="絵柄", stPixel="ドット絵", stIllust="イラスト", stSimple="シンプル・ベクター",
  qDim="表現", d2="2D", d3="2.5D / 3Dモデル",
  qChars="キャラクター・敵の数", qAnim="アニメーション", aNone="なし", aSimple="シンプル（動作3つ）", aFull="豊富（動作6つ）",
  qMusic="BGMの曲数", qSfx="効果音", sfFew="少なめ", sfNormal="普通", sfMany="多め", qVoice="ボイス数",
  qFeats="機能", qLangs="対応言語数", qEngine="エンジン", qTrailer="PRトレーラー", yes="必要", no="なし",
  qTools="使うツール", qImg="画像", qCode="コーディング", qModel="APIモデル",
  resTitle="このゲームに必要なもの", cmpTitle="AIで作る場合の費用と期間",
  promptTitle="プロンプト集", promptSub="回答をもとに作成しました。画像・音楽・効果音ツールは英語のプロンプトが最も効くため、素材用は英語で出します。",
  tDev="開発スタート", tArt="画像", tMusic="音楽", tSfx="効果音", tTrailer="トレーラー", copy="コピー", download="まとめてダウンロード (.md)",
  howTitle="計算の仕組み",
  how=["規模の基準は、AIコーディングエージェントで実際に1人で作ったゲームです。小規模のモバイルゲームで約2週間、中規模で約4週間、大規模で約6週間かかりました。ジャンル・機能・言語数・3Dの有無で増減します。",
       "画像数 = キャラクター × アニメーションのフレーム + 背景 + アイテム + UI。生成した3枚に1枚を使う想定で、生成回数は画像数の3倍としています。",
       "コーディングのトークンは、Claude Code などのエージェントが期間の70%の日に1日約2,000万トークン（大半はキャッシュされた文脈）を読む想定です。APIは選んだモデルの現在の定価、サブスクは月単位で計算します。"],
  srcTitle="使用したツール料金", srcNote=f"{CHECKED}時点。料金はよく変わるので、購入前に各ツールの料金ページを確認してください。",
  faqTitle="よくある質問",
  faq=[("AIで2Dゲームを作るといくらかかりますか？", "小規模なモバイルゲームなら、1人でAIツールを使ってサブスクとAPI代で約$100〜300、期間は2〜3週間ほどです。上の計算機でジャンルと規模を入れて確認してください。"),
       ("ゲーム制作にはどのAIツールが必要ですか？", "主に4つです。スプライト・背景用の画像ツール（Midjourney、PixelLab、Scenario、画像API）、音楽（Suno）、効果音（ElevenLabs）、コーディングエージェント（Claude Code、Cursor）。3DモデルならMeshy、PR動画ならHiggsfieldも使えます。"),
       ("Claude Codeでゲームを作るとトークンはどれくらい？", "エージェントはプロジェクトを何度も読み直すため、2週間の開発でも数億トークンが流れ、その大半はキャッシュです。Claude Maxなら月額固定、APIなら選んだモデルでの費用を計算機が表示します。"),
       ("プロンプトは無料で使えますか？", "はい。コピーするか、まとめてMarkdownファイルでダウンロードして各ツールに貼り付けてください。入力内容はどこにもアップロードされません。")],
  defName="マイゲーム", defIdea="モバイル向け{genre}ゲーム",
  g_merge="マージ", g_puzzle="パズル", g_racing="レース", g_idle="放置", g_platformer="アクション", g_rpg="RPG", g_novel="ノベル", g_shooter="シューティング",
  f_ads="広告", f_iap="アプリ内課金", f_save="セーブ・ロード", f_rank="ランキング", f_online="オンライン対戦",
  devIntro="あなたは経験豊富なゲーム開発者です。{engine}で2Dモバイル{genre}ゲーム「{name}」を一緒に作ってください。",
  devIdea="アイデア：", devScope="規模：キャラクター{chars}種、背景{bg}枚、アイテム{items}個、BGM{music}曲、効果音{sfx}個、対応言語{langs}。",
  devFeats="機能：", devRules="ルール：コードはシンプルにモジュール単位で。1ステップに1機能ずつ作り、各ステップの後にスマホでのテスト方法を教えてください。本番の絵を渡すまでは図形で仮グラフィックを使ってください。",
  devSteps="次の順番で作ってください：", st1="プロジェクト設定、フォルダ構成、画面の流れ（タイトル → ゲーム → 結果）", st2="仮グラフィックでコアゲームループ",
  st3="スコア、進行、難易度カーブ", st4="UI：メニュー、HUD、一時停止、設定", st5="追加機能：{feats}", st6="本番の絵・音楽・効果音を組み込む", st7="仕上げ、パフォーマンス確認、Androidビルド",
  devStart="ステップ1から始めてください。コードを書く前に必要なことは先に質問してください。",
  rImages="画像", rImagesSub="キャラ{chars} · フレーム{frames} · 背景{bg} · アイテム{items} · UI{ui}", rAudio="BGM + 効果音", rAudioSub="曲 + 効果音",
  rCode="コード行数", rCodeSub="推定", rTokens="コーディングのトークン", rTokensSub="APIなら約{api}",
  l_art="画像", l_music="音楽", l_sfx="効果音・ボイス", l_code="コード", l_d3="3Dモデル", l_trailer="トレーラー",
  cAi="1人 + AI（代表的なツール）", cMine="自分のツール",
  days="{n}日", capWarn="このプランの利用上限は、毎日エージェントでコーディングするには足りない可能性が高いです。待ち時間や追加料金を見込んでください。",
  hireRef="参考：同じ規模を外注すると通常<b>{min}以上</b>かかり、国や品質によって10倍以上の差があります。",
  noTrailer="「PRトレーラー」をオンにするとトレーラー用プロンプトが出ます。",
  copied="コピーしました ✓", packTitle="プロンプト集",
  related="関連ページ", rel=[("/ja/agents", "Claude Code 月額コスト計算機"), ("/ja/image", "AI画像の1枚あたりの費用"), ("/ja/compare/performance", "AIモデルの性能と価格ランキング")],
),
}

PRICE_ROWS = [
    ("Midjourney", "Basic $10 · Standard $30 · Pro $60 / month", "https://docs.midjourney.com/docs/plans"),
    ("PixelLab", "≈ $0.01–0.03 per sprite or animation (API)", "https://www.pixellab.ai/pixellab-api"),
    ("Scenario", "≈ $15–45 / month", "https://www.scenario.com/pricing"),
    ("Suno", "Pro $10 (2,500 credits) · Premier $30 (10,000) / month", "https://suno.com/pricing"),
    ("ElevenLabs", "Starter $6 · Creator $22 · Pro $99 / month", "https://elevenlabs.io/pricing"),
    ("Meshy", "Pro $20 (1,000 credits) · Premium $40 · Ultra $100 / month", "https://www.meshy.ai/pricing"),
    ("Higgsfield", "Starter $15 · Plus $39 · Ultra $99 / month", "https://higgsfield.ai/pricing"),
    ("Claude", "Pro $20 · Max 5× $100 · Max 20× $200 / month", "https://claude.com/pricing"),
    ("Cursor", "Pro $20 / month", "https://cursor.com/pricing"),
]

def _seg(id_, opts, cols=None):
    cols = cols or len(opts)
    btns = "".join(f'<button data-v="{v}" class="tab py-1.5 px-2 rounded-md text-xs font-semibold text-zinc-400">{lab}</button>' for v, lab in opts)
    return f'<div id="{id_}" class="grid grid-cols-{cols} p-1 bg-zinc-950/70 border border-zinc-800 rounded-lg gap-1">{btns}</div>'

def _field(label, inner):
    return f'<div><span class="block text-xs text-zinc-400 font-semibold mb-2">{label}</span>{inner}</div>'

NUM = 'class="w-full bg-zinc-950/70 border border-zinc-800 rounded-lg px-3 py-1.5 text-base font-bold tabular-nums focus:outline-none focus:ring-2 focus:ring-violet-500/50"'
TXT_IN = 'class="w-full bg-zinc-950/70 border border-zinc-800 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-violet-500/50"'
CARD = "bg-zinc-900/70 backdrop-blur border border-zinc-800 rounded-2xl p-4 sm:p-5"
H2 = "text-xs uppercase tracking-wider text-zinc-500 font-semibold mb-4"

def build_page(lang, llm):
    t = T[lang]
    e = lambda k: esc(t[k])
    genre_btns = "".join(f'<button data-v="{g}" class="tab py-1.5 px-2 rounded-md text-xs font-semibold text-zinc-400">{esc(t["g_" + g])}</button>' for g in GENRES)
    scale = "".join(f'<button data-v="{v}" class="tab py-2 px-2 rounded-md text-xs font-semibold text-zinc-400 leading-tight">{e(a)}<span class="block text-[10px] font-normal text-zinc-500">{e(b)}</span></button>'
                    for v, a, b in [("s", "sS", "sSsub"), ("m", "sM", "sMsub"), ("l", "sL", "sLsub")])
    feats = "".join(f'<label class="inline-flex items-center gap-1.5 text-xs bg-zinc-950/70 border border-zinc-800 rounded-lg px-2.5 py-1.5 cursor-pointer"><input type="checkbox" data-f="{f}" class="accent-violet-500"{" checked" if f in ("ads", "save") else ""}>{esc(t["f_" + f])}</label>' for f in FEATS)
    models = [("claude-sonnet-5-5", "Claude Sonnet 5.5"), ("claude-opus-5-5", "Claude Opus 5.5"), ("gpt-6-sol", "GPT-6 Sol"), ("gemini-3-8-flash", "Gemini 3.8 Flash"), ("deepseek-v4-flash", "DeepSeek V4 Flash")]
    models = [(k, n) for k, n in models if k in llm["models"]]
    model_opts = "".join(f'<option value="{k}">{esc(n)}</option>' for k, n in models)
    tabs = [("dev", "tDev"), ("art", "tArt"), ("music", "tMusic"), ("sfx", "tSfx"), ("trailer", "tTrailer")]
    tab_btns = "".join(f'<button id="gcTab_{k}" data-v="{k}" class="tab py-1.5 px-3 rounded-md text-xs font-semibold {"tab-active" if k == "dev" else "text-zinc-400"}">{e(lab)}</button>' for k, lab in tabs)
    panes = "".join(f'''<div data-pane="{k}"{"" if k == "dev" else " hidden"}>
        <div class="flex justify-end mb-2"><button data-copy="{k}" class="text-xs font-semibold px-3 py-1.5 rounded-lg bg-violet-600 hover:bg-violet-500 text-white">{e("copy")}</button></div>
        <pre id="gcP_{k}" class="ltr whitespace-pre-wrap break-words text-xs sm:text-[13px] leading-relaxed bg-zinc-950/80 border border-zinc-800 rounded-xl p-4 max-h-[28rem] overflow-auto text-zinc-200"></pre></div>''' for k, _ in tabs)
    how = "".join(f"<li>{esc(x)}</li>" for x in t["how"])
    prices = "".join(f'<tr class="border-t border-zinc-800"><td class="py-1.5 pe-3 font-semibold"><a href="{u}" rel="nofollow noopener" target="_blank" class="hover:text-violet-300">{esc(n)}</a></td><td class="py-1.5 text-zinc-400">{esc(p)}</td></tr>' for n, p, u in PRICE_ROWS)
    faq = "".join(f'<details class="border-t border-zinc-800 py-3"><summary class="cursor-pointer font-semibold text-zinc-200">{esc(q)}</summary><p class="mt-2 text-zinc-400">{esc(a)}</p></details>' for q, a in t["faq"])
    rel = " · ".join(f'<a href="{p}" class="text-violet-300 hover:text-white underline underline-offset-2">{esc(n)}</a>' for p, n in t["rel"])

    body = f'''    <header class="text-center mb-8">
      <div class="flex justify-center"><div class="inline-flex items-center gap-2 text-xs font-medium text-violet-300 bg-violet-500/10 border border-violet-500/20 rounded-full px-3 py-1 mb-4"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>{e("badge")}</div></div>
      <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight bg-gradient-to-r from-white via-violet-200 to-indigo-300 bg-clip-text text-transparent leading-tight pb-1">{e("h1")}</h1>
      <p class="mt-3 text-zinc-400 text-sm sm:text-base max-w-2xl mx-auto">{e("sub")}</p>
    </header>

    <section class="{CARD}">
      <h2 class="{H2}">{e("qProject")}</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-5">
        <div><label for="gcName" class="block text-xs text-zinc-400 font-semibold mb-2">{e("name")}</label><input id="gcName" maxlength="60" placeholder="{e("namePh")}" {TXT_IN}></div>
        <div><label for="gcIdea" class="block text-xs text-zinc-400 font-semibold mb-2">{e("idea")}</label><input id="gcIdea" maxlength="160" placeholder="{e("ideaPh")}" {TXT_IN}></div>
      </div>
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {_field(e("qGenre"), f'<div id="gcGenre" class="grid grid-cols-4 p-1 bg-zinc-950/70 border border-zinc-800 rounded-lg gap-1">{genre_btns}</div>')}
        {_field(e("qScale"), f'<div id="gcScale" class="grid grid-cols-3 p-1 bg-zinc-950/70 border border-zinc-800 rounded-lg gap-1">{scale}</div>')}
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
        {_field(e("qStyle"), _seg("gcStyle", [("pixel", e("stPixel")), ("illust", e("stIllust")), ("simple", e("stSimple"))]))}
        {_field(e("qDim"), _seg("gcDim", [("2d", e("d2")), ("3d", e("d3"))]))}
        {_field(e("qAnim"), _seg("gcAnim", [("none", e("aNone")), ("simple", e("aSimple")), ("full", e("aFull"))]))}
        {_field(e("qSfx"), _seg("gcSfx", [("few", e("sfFew")), ("normal", e("sfNormal")), ("many", e("sfMany"))]))}
        <div><label for="gcChars" class="block text-xs text-zinc-400 font-semibold mb-2">{e("qChars")}</label><input id="gcChars" type="number" min="0" max="200" inputmode="numeric" {NUM}></div>
        <div><label for="gcMusic" class="block text-xs text-zinc-400 font-semibold mb-2">{e("qMusic")}</label><input id="gcMusic" type="number" min="0" max="50" inputmode="numeric" {NUM}></div>
        <div><label for="gcVoice" class="block text-xs text-zinc-400 font-semibold mb-2">{e("qVoice")}</label><input id="gcVoice" type="number" min="0" max="2000" value="0" inputmode="numeric" {NUM}></div>
        <div><label for="gcLangs" class="block text-xs text-zinc-400 font-semibold mb-2">{e("qLangs")}</label><input id="gcLangs" type="number" min="1" max="41" value="1" inputmode="numeric" {NUM}></div>
      </div>
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-4 mt-4">
        {_field(e("qFeats"), f'<div id="gcFeats" class="flex flex-wrap gap-1.5">{feats}</div>')}
        {_field(e("qEngine"), _seg("gcEngine", [("unity", "Unity"), ("godot", "Godot"), ("phaser", "Phaser"), ("flutter", "Flutter")], 4))}
        {_field(e("qTrailer"), _seg("gcTrailer", [("false", e("no")), ("true", e("yes"))]))}
      </div>
      <h2 class="{H2} mt-6">{e("qTools")}</h2>
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
        {_field(e("qImg"), _seg("gcImg", [("mj", "Midjourney"), ("pixel", "PixelLab"), ("scenario", "Scenario"), ("gptimg", "GPT Image")], 2))}
        {_field(e("qCode"), _seg("gcCodeTool", [("pro", "Claude Pro"), ("max5", "Max 5×"), ("max20", "Max 20×"), ("cursor", "Cursor"), ("api", "API")], 3))}
        <div><label for="gcModel" class="block text-xs text-zinc-400 font-semibold mb-2">{e("qModel")}</label><select id="gcModel" class="w-full bg-zinc-950/70 border border-zinc-800 rounded-lg px-3 py-2 text-sm">{model_opts}</select></div>
      </div>
    </section>

    <section class="{CARD} mt-5">
      <h2 class="{H2}">{e("resTitle")}</h2>
      <div id="gcAssets" class="grid grid-cols-2 lg:grid-cols-4 gap-3"></div>
    </section>

    <section class="{CARD} mt-5">
      <h2 class="{H2}">{e("cmpTitle")}</h2>
      <div id="gcCompare" class="grid grid-cols-1 md:grid-cols-2 gap-3"></div>
      <p id="gcRef" class="mt-4 text-center text-xs sm:text-sm text-zinc-400"></p>
    </section>

    <section class="{CARD} mt-5">
      <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
        <h2 class="text-xs uppercase tracking-wider text-zinc-500 font-semibold">{e("promptTitle")}</h2>
        <button id="gcDownload" class="text-xs font-semibold px-3 py-1.5 rounded-lg border border-violet-500/40 bg-violet-500/10 text-violet-200 hover:bg-violet-500/20">⬇ {e("download")}</button>
      </div>
      <p class="text-xs text-zinc-500 mb-3">{e("promptSub")}</p>
      <div id="gcTabs" class="inline-flex flex-wrap p-1 bg-zinc-950/70 border border-zinc-800 rounded-lg gap-1 mb-3">{tab_btns}</div>
      {panes}
    </section>

    <section class="prose-ts mt-12 max-w-3xl mx-auto bg-zinc-900/40 border border-zinc-800 rounded-2xl p-6 sm:p-8">
      <h2 style="margin-top:0">{e("howTitle")}</h2>
      <ul>{how}</ul>
      <h2>{e("srcTitle")}</h2>
      <div class="overflow-x-auto"><table class="text-sm w-full"><tbody>{prices}</tbody></table></div>
      <p class="text-xs text-zinc-500">{e("srcNote")}</p>
      <h2>{e("faqTitle")}</h2>
      <div class="text-sm">{faq}</div>
      <p class="text-sm mt-6">{e("related")}: {rel}</p>
    </section>'''
    faq_ld = {"@type": "FAQPage", "inLanguage": lang, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    runtime_keys = [k for k in t if k.startswith(("g_", "f_", "st", "dev", "r", "l_", "c")) or k in
                    ("defName", "defIdea", "days", "capWarn", "hireRef", "noTrailer", "copied", "packTitle", "tDev", "tArt", "tMusic", "tSfx", "tTrailer")]
    gc = {k: t[k] for k in runtime_keys if isinstance(t[k], str)}
    return dict(path=PATH[lang], title=t["title"], desc=t["desc"], h1=t["h1"], body=body, faq_ld=faq_ld, gc=gc,
                models={k: n for k, n in models})
