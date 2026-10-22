# 同じOpus 5.5でトークンが68〜88%少なかった：Antigravity CLI vs Claude Code vs Codexを実測

Googleは2026年6月18日に個人アカウントでのGemini CLIの提供を終え、新しいAntigravity CLI（`agy`）への移行を案内しています。Antigravity CLIはClaudeモデルも動かせます。おかげで珍しい比較ができるようになりました。同じモデル（Claude Opus 5.5）を別々のコーディングツールに入れると、トークンはどれだけ変わるのか。Antigravity CLI、Claude Code、Codexを同じプロンプトで計44回動かし、作られたゲームはすべてブラウザで確認しました。

## 測り方

- Windows 11、2026-10-22。実行ごとに空のフォルダを用意し、1つずつ順番に実行
- Claude Code 2.1.295 + Opus 5.5（Maxプラン）
- Codex CLI 0.162 + gpt-6-luna（ChatGPTプラン）
- Antigravity CLI 1.4.5 + Gemini 4 Argon、および + Claude Opus 5.5（個人のGoogleアカウント）
- 起動時のコスト：「Reply with the single word OK.」にダミーのMCPツールを0、1、10、30個つけて各2回
- タスク：2ステージ、スコア、残機3のブロック崩しをindex.html 1ファイルで、effort medium、各3回
- トークン数は各ツールがJSONで報告した値

## 結果1：何もしないときのトークン

| ツール | 「OK」だけの入力トークン |
|---|---:|
| Claude Code + Opus 5.5 | 35,781 |
| Codex + gpt-6-luna | 14,818 |
| Antigravity + Gemini 4 Argon | 6,745 |
| Antigravity + Opus 5.5 | 5,326（+キャッシュ読み取り5,167） |

ほとんどはツール自身の指示文とツール定義で、リクエストのたびに送られます。

## 結果2：同じコーディングタスク

| ツール | 入力 | 出力 | 秒 | 行数 | 動いたゲーム |
|---|---:|---:|---:|---:|---:|
| Claude Code + Opus 5.5 | 78,671 | 7,313 | 58 | 451 | 3/3 |
| Codex + gpt-6-luna | 55,680 | 4,563 | 68 | 42（圧縮コード） | 3/3 |
| Antigravity + Gemini 4 Argon | 13,041（+キャッシュ6,796） | 6,373 | 81 | 608 | 3/3 |
| Antigravity + Opus 5.5 | 9,822（+キャッシュ15,381） | 4,378 | 42 | 236 | 3/3 |

同じOpus 5.5でも、Antigravity CLIではClaude Codeより入力トークンが68〜88%少なく、出力は40%少なく、27%早く終わりました。その代わりClaude Codeのゲームのほうが長めでした（451行対236行）。Claude CodeはAPI価格で1回$0.37（約58円）と報告し、AntigravityとCodexはサブスクリプションなので価格が出ません。

ゲーム12本はすべて動きました。ブロックを壊すとスコアが上がり、ステージ2が出て、残機が3、2、1、0と減ります。Codexの2本は自動チェックがスコアを読めなかったので手で確認し、どちらもスコアが上がりました。

## なぜ1つの数字ではなく範囲なのか

Antigravity CLIは`input_tokens`と`cache_read_tokens`を別々に報告しますが、片方がもう片方に含まれるかはドキュメントに書かれていません。Opusの実行ではキャッシュ読み取り（15,381）が入力（9,822）より大きいので、少なくともここでは入力に含まれていません。そこで両方を載せました。報告された入力だけなら88%少なく、キャッシュ読み取りを足すと68%少なくなります。足した側で見てもClaude Codeよりずっと少ないです。

## MCPツールはもうほとんど関係ない

| | MCPツール30個をつけたとき |
|---|---:|
| Claude Code | +388トークン |
| Codex | +0 |
| Antigravity + Gemini | +582 |
| Antigravity + Opus | +417 |

Antigravity CLIではツール1個で約280〜460トークン増え、残り29個ではほとんど増えませんでした。4つともツールの詳しい定義は使うときだけ読み込んでいるようです。

## まとめ

- モデルと同じくらい、それを包むコーディングツールが大事です。同じOpus 5.5が、Antigravity CLIでは入力を数分の1しか読みませんでした。
- トークンが少ないことと結果が良いことは別です。Claude Codeのほうが長いゲームを作り、ゲームはどのツールでもすべて動きました。
- 個人アカウントでGemini CLIを使っていた人には、Antigravity CLIが後継で、かなり軽量です。

## 今回の限界

- 起動時は2回、ゲームは3回ずつ。タスク1つ、PC1台、1日で測った値です
- ツールごとにキャッシュの数え方が違うので、直接比べるときは注意が必要です
- Antigravityが`claude-opus-5-5-medium`という名前の裏でOpus 5.5をどう設定しているかはわかりません

## データ

- 全データ、実行ごとのCSV、方法（CC BY 4.0）：https://tokensave.app/data/antigravity-cli-vs-claude-code-vs-codex
- 以前のClaude Code vs Codex：https://tokensave.app/data/claude-code-vs-codex-tokens
