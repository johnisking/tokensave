![Claude の料金プラン比較｜Free・Pro・Max と日本での価格](/claude-ryoukin-plan-ja.jpg)

Claude の料金プランは、一覧表だけを見るとシンプルです。無料の Free、月$20の Pro、その上に Max 5x と Max 20x、法人向けの Team と Enterprise、そして使った分だけ払う API があります。ところが実際に選ぼうとすると、「日本では税込いくらなのか」「Pro で何回使えるのか」「Max に上げる価値はあるのか」といった疑問が次々に出てきます。この記事では、2026年10月時点の公式情報をもとに、各プランの料金と中身、使用量の上限の仕組み、日本での支払い、API 料金の基本までをまとめ、最後に私自身がプランを移ってきた経験も紹介します。

## Claude の料金プラン一覧（2026年10月）

![Claude の料金プラン一覧（2026年10月）: プラン, 月払い, 年払い, 主な対象](/claude-ryoukin-plan-claude-202610-ja.jpg)

Anthropic の料金ページに掲載されている価格です（米ドル、税抜）。

| プラン | 月払い | 年払い | 主な対象 |
|---|---:|---:|---|
| Free | $0 | $0 | まず試したい人 |
| **Pro** | **$20** | **月$17（年$200）** | 個人で日常的に使う人 |
| Max 5x | $100 | なし | Pro の上限によく当たる人 |
| Max 20x | $200 | なし | 一日中ヘビーに使う人 |
| Team Standard（1シート） | $25 | $20 | 2〜150人のチーム |
| Team Premium（1シート） | $125 | $100 | チームのヘビーユーザー |
| Enterprise（1シート） | – | $20＋API 料金での従量課金 | 大企業 |

- **Pro は年払いにすると約17%安くなります。** 1年で$240のところ、前払いで$200です。
- **Max は月払いのみ**で、年払いの割引はありません。
- **Team は2シートから150シートまで**です。
- **料金ページの価格は税抜**で、「表示価格には該当する税は含まれない」と明記されています。

## 日本での支払い：ドル建てに消費税10%

![日本での支払い：ドル建てに消費税10%: プラン, 税抜, 消費税10%込み](/claude-ryoukin-plan-ja-3.jpg)

ここは日本の利用者がいちばん気になる点だと思います。

- **Anthropic は日本円の公式価格を公開していません。** 料金ページの表示は米ドルで、日本や日本円についての記載はありません。ヘルプセンターの Pro の料金ページも「米国で$20、英国で£18に地域の税を加えた額」と書かれているだけです。
- **2026年4月1日から、日本の顧客には消費税（JCT）10%が加算されています。** Claude ヘルプセンターのお知らせによると、すべてのプラン価格に10%の消費税が加わり、請求通貨は変わりません。適格請求書には消費税額が日本円で記載され、Anthropic は適格請求書発行事業者として登録されています（登録番号 T7700150134388）。
- **個人と法人で扱いが違います。** 課税事業者の法人は、Anthropic の適格請求書で仕入税額控除を受けられます。個人はこの控除を使えないため、消費税分はそのまま負担になります。

ドル建ての価格に10%を加えると、次のようになります（私たちの計算です）。

| プラン | 税抜 | 消費税10%込み |
|---|---:|---:|
| Pro（月払い） | $20 | $22 |
| Pro（年払い） | 月$17（年$200） | 月$18.70（年$220） |
| Max 5x | $100 | $110 |
| Max 20x | $200 | $220 |

円での引き落とし額は、カード会社の為替レートと手数料によって毎月変わります。円で書かれた「Claude Pro は約○○円」という数字は、どれも記事ごとの為替換算で、公式の円価格ではない点に注意してください。

**アプリから契約すると価格が違うことがあります。** Anthropic のヘルプセンターには「モバイルの価格はアプリのプラットフォームによって異なる場合がある」とあり、アプリでの価格は公開されていません。iPhone や Android のアプリ内で契約する前に、Web 版の価格と見比べましょう。

## 無料プラン（Free）でできること

![無料プラン（Free）でできること: Web・デスクトップ・モバイルでのチャット; Web 検索、メモリ、コネクタ; Artifacts、ファイル作成とコード実行](/claude-ryoukin-plan-ja-4.jpg)

Free は「お試し版」と思われがちですが、できることは意外と多くあります。

- Web・デスクトップ・モバイルでのチャット
- Web 検索、メモリ、コネクタ
- Artifacts、ファイル作成とコード実行
- プロジェクト（5つまで）
- 使えるモデルは Sonnet と Haiku

Free で**できない**ことは、Opus の利用、Claude Code、そして使用量の多さです。Claude が自分に合うかを確かめるには十分ですが、コーディングエージェントを試したいなら Pro が必要です。

## Claude Pro（月$20）で増えるもの

Anthropic の料金ページによると、Pro には Free のすべてに加えて次のものが含まれます。

- **Free より多い使用量。** ピーク時でも Free の500%以上とされています。
- **Claude Code。** ターミナル、IDE、デスクトップアプリで使えるコーディングエージェントです。
- **Opus を含むすべてのモデル**（Opus・Sonnet・Haiku）。Fable は Pro では有料の使用量クレジット経由でのみ使えます。
- **プロジェクト数の制限なし**（Free は5つまで）
- **Research**（複数ステップの Web リサーチ）
- **Claude in Chrome と Microsoft 365 連携**
- **ダッシュボード（ベータ）、タスクの引き継ぎとスケジュール実行**

メモリ、コネクタ、Web 検索、Artifacts、ファイル作成、コード実行は Free にもあるので、Pro で増えるのは機能そのものより「使える量」です。

注意したいのは、**Pro には API の利用が含まれない**ことです。Claude API と Console は、トークン単位で別に課金されます。

## 使用量の上限の仕組み

Pro と Max には、2つの上限が同時にかかります。

| 上限 | 仕組み |
|---|---|
| セッションの上限 | 5時間ごとにリセット |
| 週の上限 | すべてのモデルにまたがってかかり、週ごとにリセット（Settings > Usage で確認） |

- **決まったメッセージ数はありません。** どこまで使えるかは、モデル、会話の長さ、添付ファイル、Claude Code を使うかどうかで変わります。
- **決まったメッセージ数は公開されていません。** ヘルプセンターも「5時間で何通」という数字は出していません。長いチャット、大きなファイル、Opus を使うと、ずっと早く上限に近づきます。リセット時刻の確認方法は [Claude の使用量上限まとめ](/ja/blog/claude-shiyouryou-jougen) へ。
- **Claude アプリと Claude Code は同じ上限を共有します。** 長いコーディングをするとチャットに使える分が減り、その逆も同じです。
- **上限を超えても、有料の使用量クレジットをオンにすれば続けられます。**
- ヘルプセンターによると、**月単位の上限が加わる場合もあります。**

2026年には上限の変更もありました。5月6日に、Pro・Max・Team・シート制 Enterprise の Claude Code の5時間上限が100%引き上げられ、Pro と Max ではピーク時間帯の追加の制限も撤廃されました。また、5月13日〜7月19日には有料プランの Claude Code の週の上限が50%引き上げられていましたが、このキャンペーンは終了しています。

Claude Code での上限の詳細は [Claude Code の使用量上限まとめ](/ja/blog/claude-code-shiyouryou-jougen)で解説しています。

## Max 5x と Max 20x

| | Pro | Max 5x | Max 20x |
|---|---|---|---|
| 月額 | $20 | $100 | $200 |
| 使用量 | 基準 | Pro の500% | Pro の2,000% |
| Fable | 有料クレジットで利用 | 週の上限の最大50%まで | 週の上限の最大50%まで |
| 出力の上限 | 標準 | 高い | 高い |
| Claude Platform の API クレジット | なし | 月$100 | 月$200 |

Max ではほかに、新機能への早期アクセスと、混雑時の優先アクセスが付きます。

使用量あたりの価格を計算すると、2つの Max の性格がはっきり分かれます（私たちの計算です）。

- **Max 5x は、使用量あたりの単価が Pro と同じです。** 料金は Pro より400%高く、使用量も400%多いからです。
- **割安になるのは Max 20x だけです。** 料金は Pro より900%高いのに対し、使用量は1,900%多いので、使用量あたりの単価は Pro より50%安くなります。
- **Max に上げる目安は「ほぼ毎週上限に当たるかどうか」です。** たまに当たる程度なら、リセットを待つか少しクレジットを買うほうが、毎月$80多く払うより安く済みます。

Pro と Max の違いをもっと詳しく知りたい方は [Claude Max と Pro の比較](/ja/blog/claude-max-vs-pro)を、ChatGPT の上位プランとの比較は [ChatGPT Pro vs Claude Max](/ja/blog/chatgpt-pro-vs-claude-max) をご覧ください。

## Team と Enterprise（法人向け）

- **Team Standard：** 1シート月$25（年払いなら$20）。Pro より多い使用量とすべての Claude 機能に加え、一括請求、SSO、デフォルトで学習に使われないといった管理機能が付きます。2〜150シートが対象です。
- **Team Premium：** 1シート月$125（年払いなら$100）。Standard シートの500%の使用量で、それ以外は Standard と同じです。
- **Team の API クレジット：** 料金ページでは、チーム全体で月最大$500のプール型 API クレジットが記載されています。
- **Enterprise：** 1シート月$20（年払い）に加えて、使用量を API 料金で支払います。Team の機能に加えて、管理者による支出上限、ロールベースのアクセス、SCIM、監査ログ、Compliance API、データ保持期間の設定、IP 許可リストなどが使えます。

個人で Pro や Max を契約している人が Team プランに移ると、個人のサブスクリプションは解約され、日割りで返金されます。

## Claude API の料金の基本

API は、プランとは別に使ったトークンの分だけ払う方式です。Anthropic の公式価格は100万トークンあたりで、次のとおりです。

| モデル | 入力 | 出力 | キャッシュ書き込み（5分） | キャッシュ書き込み（1時間） | キャッシュ読み込み |
|---|---:|---:|---:|---:|---:|
| Fable 5.1 | $10 | $50 | $12.50 | $20 | $0.25 |
| Opus 5.5 | $4 | $20 | $5 | $8 | $0.20 |
| Sonnet 5.5 | $2 | $10 | $2.50 | $4 | $0.10 |
| Haiku 5.5（10万トークン以下） | $0.10 | $0.50 | $0.125 | $0.20 | $0.01 |
| Haiku 5.5（10万トークン超） | $0.50 | $2.50 | $0.625 | $1 | $0.05 |

- **出力は、どのモデルでも入力より400%高く**設定されています。
- **モデル間の差がいちばん大きな価格差です。** Opus 5.5 は Sonnet 5.5 より100%高く、Haiku 5.5 は Sonnet 5.5 より95%安くなっています（10万トークン以下の場合）。
- **キャッシュ読み込みが最も安いトークンです。** Opus 5.5 と Sonnet 5.5 では通常の入力価格の5%です。
- **Batch API を使うと入力・出力が50%割引**になり、キャッシュとの併用もできます。
- **思考（thinking）トークンは出力として課金されます。** effort を上げると、そのぶん費用も増えます。

### 日本語はトークンが多くなりやすい

API の費用はトークン数で決まるので、言語の違いも無視できません。私たちが同じ内容で測定したところ、日本語は英語より約79%多いトークンになりました。これは GPT のトークナイザーでの測定です。同じプロンプトを現行の Claude で測ると、日本語は英語より約51%多くなりました（[データセット](/data/token-cost-by-language-claude-gemini)）。また Anthropic によると、Claude 4.7 以降のモデルは新しいトークナイザーを使っており、同じテキストでも以前のモデルより約30%多いトークンになります。日本語のプロンプトを大量に送るなら、英語の目安で見積もらず、実際の文章で数えてみてください。

### サブスクと API、どちらが安いか

Pro や Max はトークン単位では課金されず、5時間ごとと週ごとにリセットされる使用枠の方式です。Anthropic は使用枠をトークン数では公開していません。

一般的には、**毎日使う人、特に Claude Code を使う人はプランのほうが割安**になりやすく、**自分のアプリから呼び出す人や週に数回しか使わない人は API のほうが月$20より安く済む**こともあります。費用分析サイトの FinOps LLM が記録したあるユーザーの例では、Max 5x の典型的な5時間枠が API 換算で約$37分でした（第三者による1ユーザーの記録です）。自分の使い方でどちらが得かは、記事の最後の計算機で確かめられます。

## 無料体験・返金・解約

- **無料体験は現在ありません。** 料金ページにトライアルはなく、ヘルプセンターのキャンペーンページに載っている2つのオファー（2025年10月の Pro 1か月無料など）はどちらも終了しています。常設の割引もないとされています。
- **お試しなら Free プランで。** Sonnet、Haiku、プロジェクト、メモリ、Web 検索が使えるので、払う前に Claude が合うか確かめられます。ただし Claude Code と Opus は Free では試せません。
- **返金は原則なし。** 規約や法律で定めがある場合を除き、支払いは返金されません（EEA と英国には14日間の例外があります）。iPhone で契約した場合の返金は Apple が、Android の場合は Anthropic のサポートが窓口です。
- **解約は更新日の24時間前までに。** Web・デスクトップでは Settings → Billing → Cancel から手続きでき、支払い済みの期間の終わりまでは使えます。

## ほかの$20プランとの比較

| プラン | 月額 | 含まれるコーディングエージェント | 上限の方式 |
|---|---:|---|---|
| Claude Pro | $20 | Claude Code | 5時間と週の上限 |
| ChatGPT Plus | $20 | Codex | Codex に5時間枠、週の上限がかかる場合も |
| Cursor Premium | $30 | Cursor のエージェント | Grok・Composer は週ごとの使用量、Claude・GPT は API 価格で別料金 |
| GitHub Copilot Pro | $10 | Copilot エージェント | 月$15分の AI クレジット |

- **$20で直接競合するのは Claude Pro と ChatGPT Plus** です。どちらもコーディングエージェントとチャットアプリが同じ上限を共有します。
- **Claude にはコーディングエージェントの無料枠がありません。** ChatGPT は Free でも Codex が使え、Copilot にも無料版がありますが、Claude Code は Pro 以上が必要です。Codex の料金は [Codex の使用量上限まとめ](/ja/blog/codex-shiyouryou-jougen) や [Codex pricing](/blog/codex-pricing)（英語）で解説しています。
- ChatGPT・Gemini を含めた円での比較は[生成AIのサブスク料金比較](/ja/blog/ai-subscription-ryoukin-hikaku)にまとめています。

## 使い方別のプランの選び方

| こんな人 | おすすめ | 理由 |
|---|---|---|
| 週に数回、調べものや文章作成に使う | Free | Sonnet と Haiku、Web 検索、メモリまで無料で使える |
| ほぼ毎日使う、Opus や Claude Code を試したい | Pro（$20） | Opus、Claude Code、Research が加わり、使用量は Free の500%以上 |
| Claude Code や重い作業でほぼ毎週上限に当たる | Max 5x（$100） | Pro の500%の使用量。単価は Pro と同じ |
| 一日中エージェントを動かす | Max 20x（$200） | Pro の2,000%の使用量。使用量あたりの単価が Pro より50%安い |
| 自分のアプリやツールから呼び出したい | API | 使った分だけ。プランには API 利用は含まれない |
| 社内でまとめて導入したい | Team・Enterprise | 一括請求、SSO、学習に使われない設定などの管理機能 |

迷ったときは、Free で始めて、足りなくなったら1段ずつ上げるのが無難です。上限に当たる頻度は、Settings → Usage で週の使用状況を見ながら判断できます。

## 私の使い方：Free から Pro、そして Max 5x へ

私は Free プランから始めて Pro に移り、今は Max 5x を使っています。作業はひとつの PC で、Claude のデスクトップアプリから行っています。

コーディングの作業と、外部の MCP ツールを使う作業はトークンを多く使ったので、そういう作業については Pro より Max のほうが合っていると感じました。それ以外の作業だけなら、Pro で十分だと感じました。

Opus 5 がメインだった頃は、上限を使い切っていました。Opus 5.5 になってからは上限に当たっていませんが、最近のある週は週の上限の93%まで使いました。

## まとめ

- **Claude のプランは Free（$0）、Pro（$20）、Max 5x（$100）、Max 20x（$200）、Team、Enterprise** で、API は別料金です。
- **日本では、ドル建ての価格に2026年4月から消費税10%が加わります。** Pro は月払いで$22です（私たちの計算）。Anthropic は円の公式価格を出しておらず、アプリ内課金の価格は Web と違う場合があります。
- **まず Free で試し、毎日使うなら Pro** が基本です。Pro で Opus、Claude Code、Research が使えるようになります。
- **Max に上げるのは、ほぼ毎週上限に当たる場合だけ**で十分です。Max 5x は使用量あたりの単価が Pro と同じで、割安になるのは Max 20x です。
- **API はプランとは別で、モデル選びが費用を最も大きく左右します。** Sonnet 5.5 は100万トークンあたり入力$2・出力$10です。

## よくある質問

**Claude Pro は月いくらですか？**
米ドルで月$20（月払い）、年払いなら月$17（年$200）です。日本では2026年4月1日から消費税10%が加わるため、月払いで$22になります（私たちの計算）。円での請求額はカード会社の為替レートで決まります。

**Claude の料金は日本円で払えますか？**
Anthropic は日本円の公式価格を公開しておらず、料金ページはドル表示です。消費税のお知らせによると請求通貨はこれまでと変わらず、適格請求書には消費税額が円で記載されます。アプリ内で契約する場合は、ストアに表示される価格を確認してください。

**無料プランでも Claude Code は使えますか？**
使えません。Claude Code は Pro 以上のプランに含まれています。Free では Sonnet と Haiku によるチャット、Web 検索、プロジェクト（5つまで）などが使えます。

**Claude Pro で何回メッセージを送れますか？**
決まった回数はありません。Anthropic は、メッセージの長さ、ファイル、会話の長さ、モデルによって変わると案内しています。長い会話や Opus、Claude Code を使うと、より早く上限に近づきます。

**Pro と Max はどちらを選べばいいですか？**
週に何日か使う程度なら Pro で十分です。ほぼ毎週上限に当たるようなら Max 5x（Pro の500%の使用量）を検討しましょう。一日中使うなら、使用量あたりの単価が Pro より50%安い Max 20x が候補になります。

**Claude Pro に無料体験はありますか？**
現在はありません。2025年10月に実施された1か月無料のキャンペーンは終了しています。払う前に試したい場合は Free プランを使ってください。

## 自分で計算してみる

サブスクとトークン単位の API のどちらが得かは、[AI サブスク vs API 計算機](/ja/plans)で自分の使い方と各プランを比べられます。Claude Code の1か月の費用を API 価格で見積もるなら[コーディングエージェント費用計算機](/ja/agents)、プロンプトのトークン数と各モデルでの費用を知りたいときは[トークンカウンター](/ja/)をどうぞ。Claude Code に絞った料金の解説は [Claude Code の料金は月いくら？](/ja/blog/claude-code-ryoukin)、Opus 5.5 の effort 設定による違いは [Claude Opus 5.5 の effort 比較](/ja/blog/claude-opus-5-5-effort)にあります。

これまでに実際に使ったトークンと費用を知りたいときは、[Claude Code 使用量アナライザー](/ja/claude-code-usage)に記録フォルダを入れてみてください。日付・プロジェクト・モデル別のトークンと API 換算の費用を、ブラウザ内だけで計算して表示します。

*料金とプランの内容は、2026年10月12日に Anthropic の料金ページとヘルプセンターで確認しました。API 価格は2026年10月11日に確認したものです。*

## 出典

- [Anthropic: Claude のプランと料金](https://claude.com/pricing)
- [Claude ヘルプセンター: 日本の顧客向け消費税（JCT）に関するお知らせ](https://support.claude.com/ja/articles/14051822)
- [Claude ヘルプセンター: How much does Claude Pro cost?](https://support.anthropic.com/en/articles/8325610-how-much-does-claude-pro-cost)
- [Claude ヘルプセンター: What is the Pro plan?](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan)
- [Claude ヘルプセンター: About Claude's Pro plan usage](https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage)
- [Claude ヘルプセンター: How much does the Max plan cost?](https://support.claude.com/en/articles/11049744-how-much-does-the-max-plan-cost)
- [Claude ヘルプセンター: About Claude's Max plan usage](https://support.claude.com/en/articles/11014257-about-claude-s-max-plan-usage)
- [Claude ヘルプセンター: Claude Pro and Max promotions](https://support.claude.com/en/articles/12660862-claude-pro-and-max-promotions)
- [Claude ヘルプセンター: Request a refund](https://support.claude.com/en/articles/12386328-request-a-refund-for-a-paid-claude-plan)
- [Claude ヘルプセンター: Cancel your Pro or Max subscription](https://support.claude.com/en/articles/8325617-cancel-your-pro-or-max-subscription)
- [Anthropic: 上限引き上げのお知らせ（2026年5月）](https://www.anthropic.com/news/higher-limits-spacex)
- [Claude ヘルプセンター: May–July 2026 weekly limits promotion](https://support.claude.com/en/articles/15910845-claude-code-may-july-2026-weekly-limits-promotion)
- [Anthropic: API の料金](https://platform.claude.com/docs/en/about-claude/pricing)
- [Anthropic: プロンプトキャッシュ](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [OpenAI: Codex の料金](https://learn.chatgpt.com/docs/pricing)
- [Cursor: Pricing](https://cursor.com/pricing)
- [GitHub: Copilot のプラン](https://github.com/features/copilot/plans)
- [FinOps LLM: Claude Pro and Max token limits](https://finopsllm.com/research/claude-pro-max-tokens-limit)
<!-- autoimg -->
