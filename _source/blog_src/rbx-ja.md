2026年の今、プログラミングができなくても Roblox（ロブロックス）のゲームは作れます。Roblox Studio には AI の「Roblox Assistant」が入っていて、ゲームの計画、制作、Luau スクリプトの作成、3Dモデルの生成までやってくれます。大きな作業には Claude Code や Cursor のような外部のコーディングエージェントもつなげられます。今 Roblox で伸びているジャンル、作り方の手順、かかる費用、そして収益の受け取り方までまとめました。

## 今 Roblox で伸びているジャンル（2026年10月）

2026年10月6日に Roblox の公式チャートで、伸びているゲームを8つの型に分けました。カッコ内は確認時点の同時接続数です。

| ジャンル | 代表的なゲーム | 小規模で作る期間* |
|---|---|---|
| Steal a ___（奪い合い） | Steal An Egg 1.1M・Steal a Brainrot 85K | 2〜3週間 |
| 協力ホラー | Dandy's World 166K・99 Nights in the Forest 157K | 2〜4週間 |
| 1対1対戦 | RIVALS 137K・Murderers VS Sheriffs Duels 86K | 2〜3週間 |
| +1 成長系 | +1 Speed Keyboard Escape 81K・+1 Loot To Forge 32K | 1〜2週間 |
| 運・ガチャ集め（RNG） | Fish It! 70K・Fisch 67K | 2〜3週間 |
| ペット | Adopt Me! 186K・Ride A Pet 78K | 2〜3週間 |
| 単純作業シム | Build the Pyramid! 13K・Peel THE Potato 10K | 1〜2週間 |
| 2人協力アスレ（オビー） | Flee the Facility 30K・Grapple Cart Obby 9K | 1.5〜2.5週間 |

\*1人で AI コーディングエージェントと Roblox Assistant を使った場合。当サイトの[ゲーム制作費計算機](/ja/ai-game-cost-calculator)の見積もりです。

**初めてなら、+1 成長系・単純作業シム・2人協力アスレがおすすめです。** 絵も仕組みも少なく、プレイヤー同士の対戦バランスを考える必要もありません。Steal a ___・RNG・ペットはゲームパスや課金アイテムが売れやすい一方、セーブやショップ、公平さへの配慮が必要です。協力ホラーと対戦はいちばん手間がかかります。どれを選ぶにしても、ヒット作をそのまま真似するのではなく、「Steal a ___」の名詞や単純作業の中身に自分のアイデアを入れましょう。

## 作り方：6つのステップ

**1. Assistant で計画する。** Roblox Studio で新しい Baseplate を開き、Assistant を「Plan」モードにして、ゲームの目的、プレイヤーが毎分すること、成長のしかたを数文で説明します。Assistant が段階的な制作計画を書いてくれます。最初のバージョンは小さく、マップ1つ・メインの行動1つ・成長の仕組み1つに絞りましょう。

**2. 最初のバージョンを作らせる。** 「Build」を押すと、Assistant が計画どおりにパーツ、モデル、スクリプトを作ります。途中で止まったら「Continue」を押します。

**3. 3Dモデルを作る。** Assistant に `/generate_mesh` に続けて説明を書くと、テクスチャ付きの3Dモデルを作ってくれます（例：`/generate_mesh 金の縁取りがあるかわいい宝箱`）。パーツで組んだモデルは `/generate_procedural_model`（24時間で50個まで）、マテリアルは `/generate_material` です。無料で使え、1日の上限があります。毎回同じスタイルの一文を先頭に入れると、モデルの見た目がそろいます。

**4. テストと修正をくり返す。** Play を押して最後まで遊び、「こうなると思ったのに、実際はこうなった」と Assistant に伝えて直してもらいます。Roblox のバグは複数人のときに出ることが多いので、Studio で2人以上でテストしましょう。

**5. 大きな仕組みはコーディングエージェントに。** セーブ、ショップ、ラウンド制、マッチングのような大きな仕組みは、Claude Code や Cursor などの外部エージェントを MCP で Studio につないで任せる方法もあります。どの AI に書かせる場合も、次の基本を守らせてください。
- ゲームのロジックは **ServerScriptService**、画面や操作は **StarterPlayerScripts / StarterGui** に置く。
- サーバーとクライアントのやり取りは **RemoteEvent** だけにして、クライアントを信用しない（チート対策）。
- 進行状況は **DataStoreService** で保存する（リトライ付き）。
- ゲームパスと課金アイテムは **MarketplaceService** で売る。

**6. アイコン・サムネイルを作って公開。** 512×512のアイコンと1920×1080のサムネイルを数枚用意し、メニューの「Roblox に公開」（Publish to Roblox）で名前と説明を入れて、公開設定にします。

## かかる費用

Roblox は公開が無料で、サーバーも Roblox が無料で動かしてくれます。費用はほぼ AI ツール代だけです。小規模なゲームなら、当サイトの計算機で:

| 組み合わせ | 費用 |
|---|---|
| 最安：Gemini、無料の音素材、Google AI Pro、Roblox Assistant | 約$25〜40（約4,000〜6,300円） |
| 標準：Midjourney、Suno、ElevenLabs、Claude Max 5x | 約$110〜150（約1.7万〜2.4万円） |

1ドル＝158円、税抜。費用の大部分は AI コーディングのプランです。

## 収益の受け取り方

ゲームパス、課金アイテム（デベロッパープロダクト）、サブスクリプション、プライベートサーバーの売上と、Premium Payouts（Premium 会員がゲームで過ごした時間に応じた支払い）で **Robux** を稼ぎます。ゲームパスと課金アイテムの売上は70%が自分の取り分です。

Robux は **DevEx（開発者交換）** で現金にできます。
- レート：**1 Robux＝$0.0038**（30,000 Robux＝$114）。対象ゲームで、年齢確認済みの米国の18歳以上のプレイヤーが買った分は $0.0054 です。
- 最低 30,000 Robux から。13歳以上、メール認証、税務書類の提出が必要で、換金は月1回までです。

例：ゲームパスが 10,000 Robux 売れる → 取り分 7,000 Robux → DevEx で約$27（約4,200円）。

## 自分のゲームで計算する

[AIゲーム制作費計算機](/ja/ai-game-cost-calculator)の上にある「いまRobloxで伸びているゲーム」から「これで計算」を押すと、Roblox モードに切り替わります。費用と期間に加えて、Roblox 用のプロンプト集（Studio の開発スタートプロンプト、Assistant 用の3Dモデルのプロンプト、アイコン・サムネイル、音楽、効果音）がそのまま手に入ります。AI でゲームを作った実例は[初心者がバイブコーディングでゲームを作ってみた](/ja/blog/vibe-coding-game-shoshinsha)もどうぞ。

*出典: [Roblox Charts](https://www.roblox.com/charts)、Roblox Creator Hub の [Build your first game with Assistant](https://create.roblox.com/docs/ai/build-with-assistant)・[Assistant for Studio](https://create.roblox.com/docs/assistant/guide)・[Developer Exchange](https://create.roblox.com/docs/production/monetization/developer-exchange)。2026年10月6日確認。*
