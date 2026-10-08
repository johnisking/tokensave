![GPT・Claude・Gemini のトークンの数え方](/token-kazoekata-ja.jpg)

「これは何トークン？」の答えは、どのモデルに聞くかで変わります。OpenAI、Anthropic、Google はそれぞれ独自のトークナイザーを使っているので、同じ段落があるモデルでは100トークン、別のモデルでは130トークンになることもあります。ここでは、それぞれで正確に数える方法と、コードを書かずにすばやく見積もる方法を紹介します。

## なぜ数が違うのか

トークナイザーは、各社が自社の学習データから作った固定の語彙を使って、テキストを分割します。語彙が違えば分け方も違います。GPT では1トークンの単語が Claude では2トークンになることもあれば、その逆もあります。差はふつうの英語なら小さく、コードや数字、他の言語では大きくなります。

Anthropic は、新しい Claude モデルのトークナイザーが、同じテキストに対して以前のものよりはっきり多くのトークンを生成すると説明しています。TokenSave のトークンカウンターでは、現行の Claude Sonnet・Opus モデルについて、GPT より約30%多いトークン数を想定して見積もっています。

API の料金はトークン単位なので、これは実際の費用に影響します。100万トークンあたりの料金が同じ2つのモデルでも、同じプロンプトの費用が変わることがあるのです。

## GPT（OpenAI）：ローカルで数える

OpenAI はトークナイザーを公開しているので、API を呼ばずに自分のマシンで正確に数えられます。

Python では `tiktoken` ライブラリを使います。

```python
import tiktoken
enc = tiktoken.get_encoding("o200k_base")
print(len(enc.encode("Your text here")))
```

JavaScript では `js-tiktoken` を使います。

```js
import { getEncoding } from "js-tiktoken";
const enc = getEncoding("o200k_base");
console.log(enc.encode("Your text here").length);
```

`o200k_base` は GPT-4o 以降のモデルで使われているエンコーディングです。最新の GPT モデルでは少し違う可能性があるので、ローカルでの数は非常に近い見積もりとして扱ってください。また、チャットのリクエストでは書式のためにメッセージごとに数トークンが追加されます。

## Claude（Anthropic）：トークンカウント用エンドポイントを使う

Claude の現行トークナイザーはライブラリとして公開されていませんが、Anthropic の API には**トークンカウント用のエンドポイント**があり、送信する前に、システムプロンプト、ツール、画像を含むメッセージの正確な入力トークン数を返してくれます。レート制限はありますが、無料で使えます。Python SDK では `client.messages.count_tokens(...)` で、引数は `messages.create` に渡すものと同じです。

実際にリクエストを送った後は、どの API レスポンスにも、使われた入力・出力トークンの正確な数が `usage` に含まれています。

## Gemini（Google）：countTokens を使う

Gemini API には `countTokens` メソッドがあり、何も生成せずにプロンプトのトークン数を返します。Anthropic のエンドポイントと同じく本物のトークナイザーを使っており、実際のリクエストのレスポンスにも正確な数を含む `usageMetadata` が付いてきます。

## コードなしですばやく見積もる

![コードなしですばやく見積もる: TokenSave のトークンカウンターに貼り付けます。; GPT モデルは、ブラウザの中で動く本物の o200k トークナイザーで数えられます。; Claude、Gemini などのモデルは、実際のテキストで調整した見](/token-kazoekata-ja-2.jpg)

テキストがおおよそ何トークンで、いくらかかるかを知りたいだけなら、次のとおりです。

1. [TokenSave のトークンカウンター](/ja/)に貼り付けます。
2. GPT モデルは、ブラウザの中で動く本物の o200k トークナイザーで数えられます。
3. Claude、Gemini などのモデルは、実際のテキストで調整した見積もりが表示され、見積もりであることがはっきり示されます。
4. すべてのモデルの費用が並んで表示され、貼り付けた内容はどこにもアップロードされません。

日本語のプロンプトは、英語で送るとトークンが約44%減ります。トークンカウンターの 💸 トークン節約 ボタンを使うと、自分の端末の中でプロンプトを英語に変換できます（デスクトップ版 Chrome 138以降 / Edge 148以降）。

英語なら、現行の GPT モデルで1単語あたり約1.1〜1.3トークンという大まかな目安も使えます。[1単語・1文字は何トークン？実測データ](/ja/blog/token-mojisuu)をご覧ください。

## どの数を信頼すべきか

![どの数を信頼すべきか: 予算を立てるなら： 調整済みの見積もりで十分です。モデル間の差は、アプリがどれだけ使われるかという不確かさより小さいのがふつうです。; 厳密な上限があるなら（コンテキストウィンドウ、最大出力、レート制限）：各社の公式の数](/token-kazoekata-ja-3.jpg)

- **予算を立てるなら：** 調整済みの見積もりで十分です。モデル間の差は、アプリがどれだけ使われるかという不確かさより小さいのがふつうです。
- **厳密な上限があるなら**（コンテキストウィンドウ、最大出力、レート制限）：各社の公式の数え方を使いましょう。上限を1トークンでも超えるとエラーになるからです。
- **請求の確認や正確な費用管理には：** API レスポンスの `usage` の数字を使ってください。実際に請求されるのはその数字です。

## 関連記事

- [トークンとは？](/blog/what-is-a-token)（英語）
- [LLM API 料金比較](/ja/blog/llm-api-ryoukin-hikaku)
- [AI API の請求額を見積もる方法](/blog/how-to-estimate-ai-api-cost)（英語）

## 出典

- [tiktoken（OpenAI）](https://github.com/openai/tiktoken)
- [トークンのカウント（OpenAI API ドキュメント）](https://developers.openai.com/api/docs/guides/token-counting)
- [トークンのカウント（Anthropic ドキュメント）](https://platform.claude.com/docs/en/build-with-claude/token-counting)
- [トークンを理解してカウントする（Gemini API ドキュメント）](https://ai.google.dev/gemini-api/docs/generate-content/tokens)
- [Translator API（Chrome for Developers）](https://developer.chrome.com/docs/ai/translator-api)
- [Translator API を使用してテキストを翻訳する（Microsoft Edge）](https://learn.microsoft.com/ja-jp/microsoft-edge/web-platform/translator-api)
<!-- autoimg -->
