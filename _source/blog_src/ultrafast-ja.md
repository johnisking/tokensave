![GPT-6.1 Sol Ultrafast の料金と速度まとめ](/gpt-6-1-sol-ultrafast-ryoukin-ja.jpg)

GPT-6.1 Sol **Ultrafast**（ウルトラファスト）は、GPT-6.1 Sol をずっと速く動かすモードです。OpenAI は2026年10月8日（米国時間）から API・Codex・ChatGPT Work で提供を始めました。API 料金は **100万トークンあたり入力 $12、出力 $60** で、通常の GPT-6.1 Sol（$2 / $10）より500%高く、GPT-6 Astra（$10 / $50）よりも20%高くなります。どれくらい速いのか、実際のリクエスト1回でいくらかかるのか、いつ使う価値があるのかをまとめました。

## GPT-6.1 Sol Ultrafast とは

OpenAI は Ultrafast を、Astra に近い知能を保ちながら、通常の Sol より速度が最大700%速いモードと紹介しています。報道（WinCentral）では毎秒約300トークンという数字も出ています。いずれも OpenAI の発表と報道によるもので、実際の速度はリクエストの長さや混雑によって変わります。

OpenAI は Ultrafast を新しいモデルではなく、GPT-6.1 Sol の処理モードとして紹介しています。同じモデルを選び、速度と料金の違うモードを選ぶ形です。

## 料金：通常・Fast・Ultrafast の比較

![料金：通常・Fast・Ultrafast の比較: モード, 入力, キャッシュ入力, 出力](/gpt-6-1-sol-ultrafast-ryoukin-fastultrafast-ja.jpg)

100万トークンあたりの価格です（OpenAI の料金ページより）。

| モード | 入力 | キャッシュ入力 | 出力 |
|---|---:|---:|---:|
| GPT-6.1 Sol 通常 | $2.00 | $0.10 | $10.00 |
| GPT-6.1 Sol Fast | $4.00 | $0.20 | $20.00 |
| **GPT-6.1 Sol Ultrafast** | **$12.00** | **$0.60** | **$60.00** |
| GPT-6 Astra（通常） | $10.00 | $1.00 | $50.00 |

- **Fast** は通常より100%高くなります（OpenAI のモデルページより）。
- **Ultrafast** は通常より500%高く、キャッシュ入力も同じ割合で $0.60 になります。
- 27万2,000トークンを超える長い入力は、リクエスト全体に割増がかかります。料金表では Ultrafast と思われる行に入力 $24、出力 $90 とありますが、表にモード名が書かれていないため推定です。

## 実際にいくらかかるか

![実際にいくらかかるか: モード, リクエスト1回, 月1万回](/gpt-6-1-sol-ultrafast-ryoukin-ja-3.jpg)

**よくあるリクエスト**1回を、入力2,000トークン、出力500トークン（キャッシュなし）としました。

| モード | リクエスト1回 | 月1万回 |
|---|---:|---:|
| GPT-6.1 Sol 通常 | $0.009 | $90 |
| GPT-6.1 Sol Fast | $0.018 | $180 |
| **GPT-6.1 Sol Ultrafast** | **$0.054** | **$540** |
| GPT-6 Astra | $0.045 | $450 |

**コーディングエージェントの1ステップ**は前の会話を読み直すので、キャッシュの割合が大きくなります。入力5万トークンのうち4万5,000トークンがキャッシュ、出力1,000トークンとすると：

| モード | 1ステップの費用 |
|---|---:|
| GPT-6.1 Sol 通常 | $0.0245 |
| GPT-6.1 Sol Fast | $0.049 |
| **GPT-6.1 Sol Ultrafast** | **$0.147** |
| GPT-6 Astra | $0.145 |

計算：Ultrafast = 新しい入力5,000 × $12 + キャッシュ45,000 × $0.60 + 出力1,000 × $60（すべて100万トークンあたり）。エージェント作業では Ultrafast と Astra の費用がほぼ同じ（約1%差）になります。同じ費用なら「Astra の知能」と「6.1 Sol の速さ」のどちらが必要かで選びます。

## どこで、誰が使えるか

![どこで、誰が使えるか: API： GPT-6.1 Sol で Ultrafast モードを選びます。OpenAI のドキュメントは WebSocket 接続を基本とし、HTTP の方法も案内しています。; Codex・ChatGPT Work：](/gpt-6-1-sol-ultrafast-ryoukin-ja-4.jpg)

- **API：** GPT-6.1 Sol で Ultrafast モードを選びます。OpenAI のドキュメントは WebSocket 接続を基本とし、HTTP の方法も案内しています。
- **Codex・ChatGPT Work：** **Pro 500**、従量制の **Enterprise**（管理者が有効化する必要あり）、クレジット制の **Edu** プランで使えます。Pro 100・200 と Plus にはありません。
- **地域：** 米国・EU のデータ保管を含む、すべての対応地域で提供されます。

## 長所と短所

**長所**

- **待ち時間が大きく減る：** 長いコードや文書の生成が、OpenAI の発表では最大700%速くなります。
- **Astra に近い性能を Astra に近い費用で：** キャッシュを多く使うエージェント作業では、費用が Astra とほぼ同じです。
- **人が見ている作業向け：** OpenAI は障害対応のデバッグ、アプリを操作するエージェント、リアルタイムのサービスを例に挙げています。

**短所**

- **高い：** 通常の GPT-6.1 Sol より500%高く、待てる作業に使うと費用が増えるだけです。
- **ChatGPT では Pro 500 から：** 個人が Codex・Work で使うには月$500のプランが必要です。
- **速度は「最大」の発表値：** 自分の作業で実際にどれだけ速くなるか測ってから使いましょう。

## いつ Ultrafast を使うか

- **使うと良い場合：** 人が画面の前で結果を待つ作業、リアルタイムのチャットや音声サービス、数分が惜しい障害対応、ステップの多いエージェントを早く終わらせたいとき。
- **使わなくて良い場合：** 夜間の一括処理、要約や分類などの大量作業、応答速度があまり重要でないサービス。こうした作業は通常モードや [Batch API（英語）](/blog/batch-api-half-price) のほうがずっと安くなります。

## よくある質問

**GPT-6.1 Sol Ultrafast の料金は？**
API では100万トークンあたり入力 $12、キャッシュ入力 $0.60、出力 $60 です。通常の GPT-6.1 Sol より500%高くなります。

**ChatGPT Plus や Pro 100 でも使えますか？**
いいえ。Codex と ChatGPT Work では Pro 500、従量制 Enterprise、クレジット制 Edu プランのみです。API はプランに関係なく使った分だけ支払います。

**GPT-6 Astra との違いは？**
Astra はより賢い上位モデルで、Ultrafast は 6.1 Sol を速く動かすモードです。キャッシュを多く使うエージェント作業では費用がほぼ同じなので、知能と速さのどちらを重視するかで選びます。

## 自分のプロンプトで計算する

[トークンカウンター](/ja/) にプロンプトを貼り付けると、GPT-6.1 Sol と30以上のモデルの費用を一度に確認できます。Codex をプランで使うか API で使うかは、[ChatGPT Pro 100・200・500 の比較](/ja/blog/chatgpt-pro-ryokin-hikaku) と [コーディングエージェント費用計算機](/ja/agents) を参考にしてください。

*2026年10月9日時点の料金です。料金と提供範囲はよく変わるため、使う前に OpenAI の料金ページを確認してください。*

## 出典

- [OpenAI 開発者コミュニティ：GPT-6.1 Sol Ultrafast 提供開始のお知らせ（2026年10月8日）](https://community.openai.com/t/ultrafast-is-rolling-out-today-for-gpt-6-1-sol-in-the-api-codex-and-chatgpt-work/1404475)
- [OpenAI API 料金](https://developers.openai.com/api/docs/pricing)
- [OpenAI：GPT-6.1 Sol モデルページ](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
- [OpenAI：GPT-6 Astra モデルページ](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [WinCentral：GPT-6.1 Sol Ultrafast の速度に関する報道](https://thewincentral.com/gpt-6-1-sol-ultrafast-openai-dots-ai-agents/)
<!-- autoimg -->
