![ChatGPT の使用量上限まとめ：まだ制限があるものとリセットのタイミング](/chatgpt-shiyouryou-jougen-ja.jpg)

「上限に達しました」は、かつて ChatGPT でいちばん多い不満でした。2026年にルールは大きく変わり、普段のテキストチャットは Free と Go で上限がなくなり、Plus も上限が拡大されました。ただし、最新モデル、ChatGPT Work と Codex、ファイルのアップロード、画像、音声には今も上限があります。プランごとに何が制限されているのか、上限がどうリセットされるのか、残りをどう確認するのかをまとめました。

## テキストチャット：2026年8月から Free・Go は上限なし

2026年8月6日、OpenAI は翌週から **Free・Go** のテキストチャットを無制限にし、難しい質問向けの「Think」ボタンを加えると発表しました。Plus はメッセージとアップロードが「拡大」されていますが、上限はあります。2026年10月7日からは、チャットのモデルは Plus・Pro・Business・Enterprise が GPT-6 Sol、Free と Go が GPT-6 Luna です。ただし無制限でも不正利用を防ぐための仕組みは残っているので、自動化された利用や極端な使い方は制限されることがあります。

つまり、普通のテキストメッセージを送るだけなら、もうメッセージ数の上限を見ることはないはずです。

## 今も上限があるもの

![今も上限があるもの: 機能, 上限は？](/chatgpt-shiyouryou-jougen-ja-2.jpg)

| 機能 | 上限は？ |
|---|---|
| 普段のテキストチャット | Free・Go はなし（2026年8月から）、Plus は拡大されたが上限あり |
| ファイルのアップロード、画像生成、音声 | あり（プランごとに別々の上限） |
| 高い思考レベルと Pro モデル | あり（プランによる） |
| ChatGPT Work と Codex（GPT-6 Astra を含む） | あり：含まれる使用枠、Plus・Business は5時間枠 |

**プラン別の思考レベル。** Plus は GPT-6 の高度な推論モデルを使えます。Pro ではさらに、GPT-6 Astra を使う Pro 推論オプションと、Pro 専用の GPT-5.6 Sol Pro が加わります。

## GPT-6 Astra の上限

![GPT-6 Astra の上限: プラン, 5時間あたりの GPT-6 Astra メッセージ数](/chatgpt-shiyouryou-jougen-gpt-6-astra-ja.jpg)

OpenAI のフラッグシップモデルである GPT-6 Astra は、ChatGPT Work と Codex から使います。OpenAI のヘルプセンターでは、5時間枠あたりのローカルメッセージ数の目安を次のように示しています。

| プラン | 5時間あたりの GPT-6 Astra メッセージ数 |
|---|---|
| Plus | 約5〜45 |
| Standard Business | 約5〜45 |
| Pro 100・200・500 | 現在5時間枠なし |

幅が大きいのは、長く複数ステップにわたるタスクは、短いタスクよりはるかに多くの枠を使うからです。週の上限がかかる場合もあります。Pro プランには現在 Work と Codex での5時間枠がありませんが、含まれる使用枠はあり、上位プランほど大きくなります。新規加入者の Pro 200 は Plus の10倍、Pro 500 は Plus の25倍です（2026年9月22日〜9月29日に Pro 200 を契約していた人は、10月29日まで以前の枠が維持されます）。倍率は OpenAI の公式ページではなく、OpenAI のティボー・ソティオ（Thibault Sottiaux）氏の X 投稿と報道（WinBuzzer、Windows Report）に基づく数値です。詳しくは [ChatGPT Pro 料金比較：Pro 100・200・500](/ja/blog/chatgpt-pro-ryokin-hikaku) をご覧ください。

## 上限のリセット方法

![上限のリセット方法: 5時間枠： 決まった時刻ではなく、その枠で最初にリクエストを送った時点から数える方式です。Plus と Business に適用され、Pro 100・Pro 200・Pro 500 には現在、Work と Codex での5時間枠がありません。](/chatgpt-shiyouryou-jougen-ja-4.jpg)

- **5時間枠：** 決まった時刻ではなく、その枠で最初にリクエストを送った時点から数える方式です。Plus と Business に適用され、Pro 100・Pro 200・Pro 500 には現在、Work と Codex での5時間枠がありません。
- **週の上限：** OpenAI によると、週の上限がかかる場合もあります。
- **ファイル・画像・音声：** それぞれに別々の枠があります。

## 使用量の確認方法

OpenAI のヘルプセンターによると、**Settings → Usage** で Work と Codex の残りの使用量とリセット時刻を確認できます。上限に当たったときは、いつから再開できるかも ChatGPT が表示します。

## 上限に当たったときの対処法

1. **リセットを待つ。** 5時間枠なら、長くても数時間です。
2. **リセットやクレジットを使う。** 対象の Plus・Pro アカウントは、貯まっているリセットを使ったり、即時リセットを購入したりできます。プランによってはクレジットで使い続けることもできます。
3. **モデルを切り替える。** 日常的な作業に GPT-6 Astra が必要なことはまれです。GPT-6 Sol や GPT-6 Luna なら、使う枠がずっと少なくて済みます。
4. **アップグレードする。** Pro 100 は Plus の5倍、Pro 200 は10倍、Pro 500 は25倍です。
5. **API を使う。** 特定のモデルを継続的にヘビーに使うなら、トークン単位の従量課金のほうがシンプルなこともあります。GPT-6 Astra は入力100万トークンあたり$10、出力100万トークンあたり$50です。[GPT-6 API 料金](/ja/blog/gpt-6-api-ryoukin)をご覧ください。

## チャットごとの「トークン上限」はある？

どのモデルにもコンテキストウィンドウ、つまり一度に扱えるテキスト量の上限があります。非常に長い会話や文書はいずれこれに達しますし、モデルはメッセージのたびに会話全体を読み直すため、その手前から品質が落ちていきます。短い要約を添えて新しいチャットを始めるだけで、思った以上に改善します。日本語は英語よりトークンを多く使うため、長い指示を英語で書けばトークンは約44%減ります。[トークンカウンター](/ja/)の 💸 トークン節約 ボタンを使うと、自分の端末の中でプロンプトを英語に変換できます（デスクトップ版 Chrome 138以降 / Edge 148以降）。詳しくは[コンテキストウィンドウとは](/blog/context-window-explained)（英語）をご覧ください。

## プランか API か

主にチャットで使うなら、8月の変更で Free と Go のプランは以前よりずっと使いやすくなりました。Codex や GPT-6 Astra をヘビーに使うなら、[サブスク vs API 計算機](/ja/plans)や[コーディングエージェント費用計算機](/ja/agents)で、プランの料金と同じ作業を API で行った場合の費用を比べてみてください。料金はドル建てなので、円での支払額は為替によって変わります。

*上限は頻繁に変わります。最新の数値は OpenAI の [GPT-6 Astra 使用量ヘルプページ](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)（英語）で確認してください。*

## 出典

- [Work と Codex での GPT-6 Astra の使用量管理（OpenAI ヘルプセンター）](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)
- [ChatGPT リリースノート（OpenAI ヘルプセンター）](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [ChatGPT の料金](https://chatgpt.com/pricing)
- [ChatGPT Pro の各プランについて（OpenAI ヘルプセンター）](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
- [GPT-6 Astra のモデルと API 料金（OpenAI ドキュメント）](https://developers.openai.com/api/docs/models/gpt-6-astra)
<!-- autoimg -->
