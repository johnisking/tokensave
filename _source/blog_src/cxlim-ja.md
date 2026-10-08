![Codex の使用量上限まとめ：5時間・週の上限とリセット](/codex-shiyouryou-jougen-ja.jpg)

OpenAI のコーディングエージェント Codex は ChatGPT の Plus・Pro・Business プランに含まれており、今いちばん多くの人が使用量の上限に当たる場所になっています。Codex は ChatGPT Work と使用枠を共有し、Plus と Business には5時間枠があり（週の上限がかかる場合もあります）、モデルによって消費の速さが大きく異なります。仕組みと、枠を有効に使う方法をまとめました。

## Codex が使えるプラン

Codex（と ChatGPT Work）の使用量は、**Plus**（$20）、**Pro**（$100・$200・$500）、**Business** の Standard・Premium シートに含まれています。料金はドル建てなので、円での支払額は為替によって変わります。使い放題ではなく、プランごとに含まれる使用枠が決まっています。

## 2つの上限が同時にかかる

**5時間枠。** 最初のリクエストから始まる、ローリング方式の使用枠です。使い切ると、枠がリセットされるまで待つことになります。Pro 100・Pro 200・Pro 500 には現在、Work と Codex での5時間枠がありません。含まれる使用枠は別にあります。

**週の上限。** OpenAI によると、その上に週の上限がかかる場合もあります。これに当たると、5時間枠がリセットされたばかりでも、そのリセットまで待つ必要があります。

Codex と ChatGPT Work は**同じ使用枠**を消費します。

## モデル別の使用量

![モデル別の使用量: モデル, Plus, Business（Standard）](/codex-shiyouryou-jougen-ja-2.jpg)

OpenAI のヘルプセンターでは、Plus と Standard Business について、5時間枠あたりのローカルメッセージ数の目安を示しています。選ぶモデルによって、数は大きく変わります。

| モデル | Plus | Business（Standard） |
|---|---|---|
| GPT-6 Astra | 約5〜45 | 約5〜45 |
| GPT-6.1 Sol | 約15〜160 | 約15〜160 |
| GPT-6 Sol | 約15〜150 | 約15〜150 |
| GPT-6 Luna | 約350〜3,000 | 約350〜3,000 |

各範囲の下限は大きなコードベースでの長い複数ステップのタスク、上限は短く単純なリクエストの場合です。Pro プランには現在5時間枠がなく、含まれる使用枠が大きくなります。Pro 100 は Plus の5倍、新規加入者の Pro 200 は Plus の10倍、Pro 500 は Plus の25倍です（2026年9月22日〜9月29日に Pro 200 を契約していた人は、10月29日まで以前の枠が維持されます）。倍率は OpenAI の公式ページではなく、OpenAI のティボー・ソティオ（Thibault Sottiaux）氏の X 投稿と報道（WinBuzzer、Windows Report）に基づく数値です。

**Ultrafast** は Pro 500 だけで使える高速モードで、含まれている使用量とクレジットをより速く消費します。

## Codex が枠を速く使い切る理由

ほかのコーディングエージェントと同じく、Codex はステップごとに作業し、各ステップで作業中のコンテキスト全体（指示、ツール定義、読み込んだファイル、それまでのステップ）をモデルに送り直します。25ステップほどの典型的な機能追加タスクでは、入力トークンは約160万になります。API ならこのタスクは Sol クラスのモデルで約$0.72、GPT-6 Astra で約$3.60かかります。Astra の枠がずっと小さいのはこのためです。[AI コーディングエージェントの1タスクあたりの費用は？](/blog/ai-coding-agent-cost)（英語）もご覧ください。

## 使用量の確認方法

OpenAI のヘルプセンターによると、ChatGPT の **Settings → Usage** で残りの使用量とリセット時刻を確認できます。上限が近づくと、Codex も警告を表示します。

## 上限に当たったら

![上限に当たったら: リセットを待つ。 5時間枠は数時間以内に回復します。; 貯まっているリセットを使うか、即時リセットを購入する。 対象の Plus・Pro アカウントで利用できます。; クレジットを使う。 対応しているプランなら、クレジッ](/codex-shiyouryou-jougen-ja-3.jpg)

1. **リセットを待つ。** 5時間枠は数時間以内に回復します。
2. **貯まっているリセットを使うか、即時リセットを購入する。** 対象の Plus・Pro アカウントで利用できます。
3. **クレジットを使う。** 対応しているプランなら、クレジットで作業を続けられます。
4. 上位の Pro プランに**アップグレードする。**
5. あふれた作業は、従量課金の **API キーを使う。**

## 枠を長持ちさせるコツ

![枠を長持ちさせるコツ: 基本は GPT-6.1 Sol か GPT-6 Sol に。 GPT-6 Astra は枠を大幅に多く使うので、違いが出る難しい問題にだけ使いましょう。; 簡単な編集、名前の変更、定型コードには Luna を。; タスクは小さく](/codex-shiyouryou-jougen-ja-4.jpg)

- **基本は GPT-6.1 Sol か GPT-6 Sol に。** GPT-6 Astra は枠を大幅に多く使うので、違いが出る難しい問題にだけ使いましょう。
- **簡単な編集**、名前の変更、定型コードには **Luna を。**
- **タスクは小さく具体的に。** ステップが少ないほど、送り直すコンテキストも減ります。
- **関係のないタスクの間では新しく始め直し**、古い履歴を持ち越さないようにしましょう。
- リポジトリ全体を探させるのではなく、**Codex に該当するファイルを指定しましょう。**
- **指示ファイルは短く。** 普段ほかの言語を使っているなら英語で書きましょう。GPT のトークナイザーでは、同じ内容が英語に比べて韓国語で約44%、日本語で約79%多いトークンになります。

同じ習慣の多くは Claude Code にも当てはまります。[Claude Code のトークン節約術](/ja/blog/claude-code-token-setsuyaku)をご覧ください。

## Codex か Claude Code か

どちらも$20・$100・$200のプランに含まれ、上限の仕組みも似ています。違いは [ChatGPT Pro vs Claude Max の比較](/ja/blog/chatgpt-pro-vs-claude-max)で解説しています。[コーディングエージェント費用計算機](/ja/agents)では、月々の API 費用をすべてのプランと比較できます。

*上限は頻繁に変わります。最新の数値は OpenAI の [Codex と Work の使用量ヘルプページ](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)（英語）で確認してください。*

## 出典

- [OpenAI ヘルプ: Work と Codex の使用量管理](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)
- [OpenAI ヘルプ: Codex の保存済みリセット](https://help.openai.com/en/articles/20001498-how-banked-codex-resets-work)
- [ChatGPT のプランと Codex 料金](https://learn.chatgpt.com/docs/pricing)
- [OpenAI ヘルプ: ChatGPT Pro の各プラン](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
<!-- autoimg -->
