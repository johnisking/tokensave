Google が Gemini アプリでプランごとに使えるモデルを変えます。**10月9日から無料ユーザーは一番小さいモデルの Flash-Lite だけ**になり、月725円の AI Plus もまもなく Pro モデルが使えなくなります。これまで無料でも Pro モデルや Deep Research をかなり使えたので、体感の変化は大きいはずです。何が変わるのか、プラン別の日本円の料金、そして無料のまま Pro 級を安く使う方法まで、日本語のトークン数で計算してまとめました。

## プラン別に使えるモデル

| プラン | 月額 | Flash-Lite | Flash | Pro | Deep Think |
|---|---:|:---:|:---:|:---:|:---:|
| 無料 | 0円 | ✓ | ✗ | ✗ | ✗ |
| AI Plus | 725円 | ✓ | ✓ | **✗（廃止）** | ✗ |
| AI Pro | 2,900円 | ✓ | ✓ | ✓ | ✓ |
| AI Ultra 5x | 14,500円 | ✓ | ✓ | ✓ | ✓ |
| AI Ultra 20x | 32,000円 | ✓ | ✓ | ✓ | ✓ |

日本の月額は2026年10月6日時点で確認したものです。個人の Google アカウントが対象で、仕事用・学校用アカウントは別のルールになります。

## いつから変わる？

- **無料:** 10月9日から Flash-Lite のみになります。
- **AI Plus:** 一斉の切り替え日はなく、加入者ごとに適用日がメールで届きます。
- **AI Pro・Ultra:** Flash-Lite・Flash・Pro をすべて使え、Deep Think も使えます。

使えるモデルでは、考える深さを「低・中・高」から選べます。ただし高くするほど上限を早く使い切ります。上限はメッセージ数ではなく計算量で決まり、5時間ごとに回復します。Pro モデル、Deep Research、画像や動画の生成は、簡単な質問より多く上限を消費します。報道によると、無料プランのコンテキストウィンドウは32,000トークンです。

## なぜ変えるのか

Google は9月30日に最上位モデル「Gemini 4 Argon」を公開しました。計算量の多い高性能モデルを有料プラン中心に回し、上位プランへの加入を増やす狙いだと見られています。

## どうすればいい？

- **ちょっとした検索・翻訳・要約が中心:** 無料（Flash-Lite）で足りることが多いです。まず使ってみて、答えに物足りなさを感じてから決めても遅くありません。
- **Pro モデル目当てで AI Plus にしていた人:** 適用日以降は725円では Pro を使えません。Pro が必要なら AI Pro（2,900円）に上げることになります。
- **学生:** 18歳以上の大学生は、2026年12月31日までの申し込みで AI Plus を1年間無料で使えます。支払い方法の登録が必要で、期間後は自動で課金されるので注意してください。
- **月2,900円が高いと感じるなら:** 同じ価格帯の ChatGPT Plus（3,000円）や Claude Pro（月$22・税込、約3,480円）と比べてみる価値があります。ChatGPT は無料でも GPT-5.6 Luna で普段の会話は無制限です。プラン別の料金は[生成AIのサブスク料金比較](/ja/blog/ai-subscription-ryoukin-hikaku)にまとめました。

## Pro 級を安く使う方法：API

Gemini のモデルは、Google AI Studio や API から使った分だけ払うこともできます。日本語は英語よりトークンが約79%多く出るので、日本語のトークン数で計算しました。1回の質問を入力1,500トークン・出力700トークンとして、**1日20回・30日使った場合**:

| モデル | 1か月の API 料金 |
|---|---:|
| Gemini 3.5 Flash-Lite | 約210円 |
| Gemini 3.8 Flash | 約360円 |
| Gemini 3.1 Pro | 約1,080円 |

1ドル＝158円で計算。会話が長くなると、毎回それまでの会話も送るので料金は増えます。

**Pro モデルでも1日20回なら AI Pro（2,900円）より安く済みます。** ただしアプリの便利な機能（画像生成、Deep Research、Gmail や Docs との連携など）は使えず、API キーに対応したチャットアプリが別に必要です。自分の使い方だとどちらが安いかは、[サブスク vs API 計算機](/ja/plans)ですぐ比べられます。日本語のトークンについては[日本語は英語よりトークンが多い？](/ja/blog/nihongo-tokens-gpt)で詳しく測っています。

*出典: [Helentech](https://helentech.jp/news-gemini-app-limits-model-access-by-plan-92116/)、[THE BRIDGE](https://thebridge.jp/2026/10/google-gemini-app-model-access-flash-lite-october)、[Notebookcheck](https://www.notebookcheck.net/Google-Gemini-drops-Flash-and-Pro-for-free-users-on-October-9.1415964.0.html)、日本の月額は[AIツール料金](https://www.aitool-ryokin.com/tools/gemini)・[はてなベース](https://hatenabase.jp/blog/gemini-pricing-guide-2026/)の確認値。2026年10月6日確認。適用日や上限は変わることがあるので、契約前に Google の公式ページを確認してください。*
