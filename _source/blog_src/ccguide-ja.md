![Claude Code の使い方｜インストールから最初の指示まで実画面で解説](/claude-code-tsukaikata-ja.jpg)

Claude Code の使い方を調べると、最初の一歩でつまずいたという声をよく見かけます。インストールのコマンドは1行なのに、Windows では PowerShell と CMD で書き方が違い、インストール方法によっては実行した瞬間に赤いエラーが出ることもあります。この記事では、Windows の PowerShell で実際にインストールの確認からテーマ選択、最初の指示、使用量の確認までを進めた画面を使いながら、公式ドキュメントに沿って Claude Code の始め方と基本の使い方を順番に説明します。途中で出たエラーとその直し方もそのまま載せています。

## Claude Code とは

Claude Code は、Anthropic が提供する AI コーディングエージェントです。ターミナル（PowerShell や macOS のターミナル）で `claude` と入力すると対話画面が開き、日本語で「このファイルを直して」「テストを書いて」と頼むと、Claude がプロジェクトのファイルを読み、コードを書き換え、コマンドを実行するところまで進めます。チャットの画面にコードを貼り付けてやり取りするのではなく、**自分のパソコンのフォルダの中で直接作業してくれる**のが大きな違いです。

公式ドキュメントによると、Claude Code はターミナルのほかに、Web（claude.ai/code）、デスクトップアプリ、VS Code と JetBrains の拡張機能、Slack、GitHub Actions などからも使えます。この記事では、いちばん基本になるターミナル版（CLI）の使い方を扱います。ターミナルに慣れていない場合は、デスクトップアプリから使う方法もあります。

## 始める前に必要なもの

### 対応 OS とパソコンの条件

公式ドキュメントの「Advanced setup」に書かれている動作条件は次のとおりです（2026年10月12日確認）。

| 項目 | 条件 |
|---|---|
| OS | macOS 13.0 以降、Windows 10 1809 以降または Windows Server 2019 以降、Ubuntu 20.04 以降、Debian 10 以降、Alpine Linux 3.19 以降 |
| ハードウェア | メモリ 4GB 以上、x64 または ARM64 のプロセッサ |
| ネットワーク | インターネット接続が必要 |
| シェル | Bash、Zsh、PowerShell、CMD |
| 地域 | Anthropic のサービス提供国（日本は対象） |

Windows では管理者として実行する必要はありません。Git for Windows は必須ではありませんが、入れておくと Claude Code が Git Bash を使ってコマンドを実行できます。入っていない場合は PowerShell が代わりに使われます。

### 有料プランかコンソールのアカウント

ここは見落としやすい点です。**Claude Code は Claude の無料プランでは使えません。** 公式ドキュメントには、Pro、Max、Team、Enterprise、または Claude Console（API）のアカウントが必要だと書かれています。

| アカウント | Claude Code | 支払い方 |
|---|:---:|---|
| Free（無料） | × | – |
| Pro | ○ | 月額 $20（年払いなら月 $17） |
| Max 5x / Max 20x | ○ | 月額 $100 / $200 |
| Team・Enterprise | ○ | 1席ごとの契約 |
| Claude Console（API） | ○ | 使ったトークンの分だけ従量課金 |

サブスクリプションの場合、Claude Code と Claude アプリ（Web・デスクトップ・モバイル）は**同じ使用量の上限を共有**します。料金と上限の詳しい比較は [Claude の料金プラン比較](/ja/blog/claude-ryoukin-plan) と [Claude Code の料金は月いくら？](/ja/blog/claude-code-ryoukin) にまとめています。

## Claude Code のインストール方法

### 公式の推奨はネイティブインストール

公式ドキュメントが「推奨」としているのは、ネイティブインストーラーです。使っている環境に合わせて、次のどれか1行をターミナルに貼り付けて実行します。

**macOS・Linux・WSL**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD**

```batch
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

PowerShell か CMD かは、プロンプトの先頭で見分けられます。`PS C:\Users\ユーザー名>` のように **PS が付いていれば PowerShell**、付いていなければ CMD です。公式ドキュメントには、次のようなエラーが出たときは使うコマンドを取り違えていると書かれています。

- `The token '&&' is not a valid statement separator` → PowerShell で CMD 用のコマンドを実行している
- `'irm' is not recognized as an internal or external command` → CMD で PowerShell 用のコマンドを実行している

なお、インストール中は進行状況が表示されないので、終わるまで少し待ちます。

### そのほかのインストール方法

| 方法 | コマンド | 自動アップデート |
|---|---|:---:|
| ネイティブ（推奨） | 上の3つ | ○（バックグラウンドで自動） |
| Homebrew（macOS） | `brew install --cask claude-code` | ×（`brew upgrade` が必要） |
| WinGet（Windows） | `winget install Anthropic.ClaudeCode` | ×（`winget upgrade` が必要） |
| npm | `npm install -g @anthropic-ai/claude-code` | 条件つき |

npm でインストールする場合は Node.js 22 以降が必要です。中身はネイティブインストーラーと同じバイナリですが、`sudo npm install -g` は権限の問題を起こすので使わないよう公式ドキュメントで注意されています。npm 版は Windows で次に説明するエラーが出やすいので、これから入れるならネイティブインストーラーを選ぶのが無難です。

## インストールを確認する（Windows で出たエラーと直し方）

インストールが終わったら、**新しいターミナルのウィンドウを開いて**、次のコマンドでバージョンを確認します。

```powershell
claude --version
```

正しく入っていれば、バージョン番号のあとに `(Claude Code)` と表示されます。

### 「running scripts is disabled」と出た場合

実際に Windows の PowerShell で `claude --version` を実行したところ、バージョンではなく赤いエラーが出ました。

![PowerShell で claude --version を実行したときの実行ポリシーのエラー画面](/claude-code-tsukaikata-ps1-error-ja.jpg)

エラーの中に `npm\claude.ps1 cannot be loaded because running scripts is disabled on this system` とあります。このパソコンには npm で Claude Code が入っていました。公式のトラブルシューティングによると、npm は各コマンドの起動用に `.ps1` というスクリプトファイルを作り、PowerShell の**実行ポリシー**がそのスクリプトの実行を止めているのが原因です。PowerShell のインストーラー（`irm ... | iex`）はスクリプトファイルを使わないので、この影響を受けません。

公式ドキュメントが挙げている直し方は3つです。

1. **自分のユーザーだけローカルのスクリプトを許可する**

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

2. **`.cmd` の起動ファイルを使う**。`claude.cmd` は同じ働きをし、実行ポリシーの対象外です。
3. **npm ではなく PowerShell のインストーラーで入れ直す**。スクリプトではなくバイナリが入ります。

今回は設定を変えずに済む2つめの方法で確認しました。`claude.cmd --version` と打つと、バージョンが表示されました。

![claude.cmd --version で 2.1.295 (Claude Code) と表示された画面](/claude-code-tsukaikata-version-ja.jpg)

表示は `2.1.295 (Claude Code)` でした。インストールの状態をもっと詳しく調べたいときは、`claude doctor` を実行すると、インストールの状態、設定ファイルのエラー、修正案などが表示されます。

### 「claude が見つからない」と出た場合

`command not found: claude` や `'claude' is not recognized` と表示されるのは、インストール先のフォルダがまだ PATH に入っていないためです。まずターミナルを閉じて開き直し、それでも直らなければ公式の「Troubleshoot installation and login」の「Fix your PATH」の手順に従います。

## 最初のセッションを始める

### 作業用フォルダを作って移動する

Claude Code は、**起動したフォルダ**を作業場所として扱います。いきなりユーザーフォルダ全体で起動するより、練習用のフォルダを作ってその中で起動するほうが安心です。

```powershell
mkdir claude-test
cd claude-test
```

![PowerShell で mkdir と cd を使って claude-test フォルダを作り移動した画面](/claude-code-tsukaikata-mkdir-ja.jpg)

実際の開発では、作業したいプロジェクトのフォルダに `cd` で移動してから起動します。

### claude で起動し、テーマを選ぶ

フォルダの中で `claude`（npm 版で実行ポリシーのエラーが出る場合は `claude.cmd`）と入力すると、Claude Code が起動します。初回は文字の配色（テーマ）を選ぶ画面が出ます。

![Claude Code の初回起動時に表示されるテーマ選択画面](/claude-code-tsukaikata-theme-ja.jpg)

選択肢は Auto（ターミナルに合わせる）、Dark mode、Light mode と、それぞれの色覚多様性対応版、ANSI カラーのみの版です。画面の下に差分表示の見本が出るので、読みやすいものを矢印キーで選んで Enter を押します。あとから `/theme` で変更できます。

### ログインする

続いてログインです。公式ドキュメントでは、初回起動時にブラウザが開き、案内に従って Claude のアカウントで認証する流れになっています。一度ログインすれば認証情報が保存され、次回からは不要です。アカウントを切り替えたいときは、起動中の画面で `/login` と入力します。

今回のパソコンでは、すでに Claude のデスクトップアプリを使っている状態で、ログインはそのまますぐにできました。

### 起動画面の見方

ログインが終わると、次のような画面になります。

![Claude Code の起動画面。バージョン、モデル、作業フォルダ、auto mode の表示](/claude-code-tsukaikata-start-ja.jpg)

左上に、Claude Code のバージョン（v2.1.295）、使っているモデルとプラン（Opus 5.5 · Claude Max）、作業フォルダ（~\claude-test）が表示されています。いちばん下の `❯` の行が入力欄です。

その上の黄色い行は、使っている MCP サーバー（外部ツールとの接続）の認証を求める案内で、`/mcp` から設定できます。MCP を使っていなければ表示されません。

画面のいちばん下にある **auto mode on** は、権限モードの表示です。これについては後の章で説明します。

## 最初の指示を出してみる

入力欄に、やってほしいことを日本語でそのまま書いて Enter を押します。今回は練習として、ファイルを1つ作ってもらいました。

![Claude Code に hallo.txt を作るよう頼み、3秒で書き込みが終わった画面](/claude-code-tsukaikata-hello-ja.jpg)

1回目は何も入力しないまま Enter を押してしまい、Claude から「メッセージが空でした。何をしましょうか」という返事と、今のフォルダが Git のリポジトリではないことが返ってきました。そこで「hallo.txt というファイルを作って、中に『こんにちは』と書いて」という内容を頼むと、`Write(hallo.txt)` と表示されてファイルが作られ、作業時間は「Brewed for 3s」、つまり約3秒でした。

Claude は指示に書いたとおりの名前でファイルを作り、完了の報告も指示と同じ言語で返してきました。名前や場所はそのまま使われるので、正確に書くのが大事です。

### 慣れてきたら試したい頼み方

公式のクイックスタートでは、実際のプロジェクトで次のような指示を試すよう勧めています（日本語に置き換えています）。

- 「このプロジェクトは何をするもの？」「フォルダ構成を説明して」
- 「メインのファイルに hello world の関数を追加して」
- 「変更したファイルを教えて」「わかりやすいメッセージでコミットして」
- 「空のフォームを送信できてしまうバグを直して」
- 「電卓の関数のユニットテストを書いて」

公式のコツは、**具体的に頼むこと**です。「バグを直して」より「間違ったパスワードを入れると画面が真っ白になるログインのバグを直して」のほうが、狙いどおりの結果になります。大きな作業は「1. テーブルを作る 2. API を作る 3. 画面を作る」のように手順に分けて頼むのも効果的です。

## 権限モードと auto mode

![権限モードと auto mode: モード, 確認なしで実行されるもの, 向いている使い方](/claude-code-tsukaikata-auto-mode-ja.jpg)

Claude Code が勝手にファイルを書き換えたりコマンドを実行したりしてよいかは、**権限モード**で決まります。起動画面に出ていたとおり、公式ドキュメントによると、v2.1.283 以降ではターミナルの対話セッションは **auto mode** で始まります。auto mode では、分類器が一つひとつの操作の危険性を確認し、リスクが低いと判断したものはそのまま実行し、それ以外は止めます。

| モード | 確認なしで実行されるもの | 向いている使い方 |
|---|---|---|
| default | 読み取りだけ | すべての操作を自分で確認したいとき |
| acceptEdits | 読み取り、ファイル編集、一般的なファイル操作コマンド | 変更を見ながら進めたいとき |
| plan | 読み取り（auto mode が使えるときは承認されたコマンドも） | 変更の前にコードを調べさせたいとき |
| auto | ほぼすべて（裏で安全確認あり） | 長い作業、確認の手間を減らしたいとき |
| dontAsk | 作業フォルダ内の読み取りと事前に許可したツールだけ | CI やスクリプト |

モードは **Shift+Tab** で切り替えられます。初めてで不安なら、Shift+Tab で default か acceptEdits にしてから使い始めると、変更のたびに確認が出ます。練習用フォルダで動きに慣れてから、普段のプロジェクトで使うのがおすすめです。

## 覚えておきたい基本コマンド

### ターミナルで使うコマンド

| コマンド | 働き |
|---|---|
| `claude` | 対話モードで起動 |
| `claude "タスク"` | 最初の指示を付けて起動 |
| `claude -p "質問"` | 1回だけ答えて終了 |
| `claude -c` | このフォルダでの直近の会話を続ける |
| `claude -r` | 過去の会話を選んで再開 |
| `claude --version` | バージョンを表示 |
| `claude doctor` | インストールと設定を診断 |
| `claude update` | すぐにアップデート |

### Claude Code の中で使うコマンド

起動した画面の入力欄で `/` を打つと、使えるコマンドの一覧が出ます。よく使うものをまとめました。

| コマンド | 働き |
|---|---|
| `/help` | ヘルプと使えるコマンドを表示 |
| `/init` | プロジェクトの説明書 `CLAUDE.md` を作る |
| `/clear` | 会話をリセットして新しく始める |
| `/compact` | これまでの会話を要約して文脈を空ける |
| `/context` | 文脈（コンテキスト）の使用状況を表示 |
| `/model` | モデルを切り替える |
| `/effort` | 考える量（effort）を変える |
| `/resume` | 過去の会話を再開 |
| `/rewind` | 会話やコードを前の状態に戻す |
| `/memory` | `CLAUDE.md` を編集する |
| `/usage` | 使用量と上限を表示（`/cost` も同じ） |
| `/exit` | 終了（Ctrl+D を2回でも可） |

ここで注意したいのは、**`/` で始まるコマンドは Claude Code の中で入力するもの**だという点です。PowerShell のプロンプト（`PS C:\...>`）で `/usage` と打っても、PowerShell のコマンドとして扱われてエラーになります。

### /init で CLAUDE.md を作る

本格的にプロジェクトで使うなら、最初に `/init` を実行しておくと便利です。Claude がプロジェクトを調べて、構成やビルド方法などをまとめた `CLAUDE.md` を作ります。このファイルは毎回の会話の最初に読み込まれるので、同じ説明を何度も繰り返さずに済みます。

## 使用量を確認する（/usage）

サブスクリプションで使う場合、気になるのが使用量の上限です。Claude Code の中で `/usage` と入力すると、設定画面の Usage タブが開きます。

![Claude Code の /usage 画面。現在のセッション24%、今週45%、Fable 0%](/claude-code-tsukaikata-usage-ja.jpg)

この画面では、次の3つのメーターが確認できました。

- **Current session（現在のセッション）**：24%。5時間ごとにリセットされる上限です。
- **Current week (all models)（今週・全モデル）**：45%。週ごとにリセットされる上限です。
- **Current week (Fable)（今週・Fable）**：0%。Fable モデル専用の週の枠です。

この数字は、Claude Code だけでなく、同じアカウントで使った Claude アプリの分も含んだものです。下には、使用量の内訳のヒントと、上限を超えたあとも有料で使い続けられる「Usage credits」の設定（`/usage-credits`）が表示されています。上限の仕組みと節約の方法は、[Claude Code の使用量上限まとめ](/ja/blog/claude-code-shiyouryou-jougen) と [Claude Code のトークン節約術](/ja/blog/claude-code-token-setsuyaku) で詳しく解説しています。

## 実際に使ってみて

私は Free から Pro に、そして今の Max 5x へと移ってきました。普段は1台の PC で Claude のデスクトップアプリを使って作業しています。コーディング作業や外部の MCP を使う作業ではトークンを多く使うので、Pro より Max のほうが合っていると感じました。それ以外の作業だけなら、Pro でも十分だと感じています。

## アップデートとアンインストール

ネイティブインストールの場合、Claude Code は起動時と実行中に更新を確認し、バックグラウンドで自動アップデートされます。すぐに最新にしたいときは `claude update` を実行します。Homebrew や WinGet で入れた場合は自動では更新されないので、`brew upgrade claude-code` や `winget upgrade Anthropic.ClaudeCode` を定期的に実行します。

アンインストールは、入れた方法に合わせて行います。

| 入れた方法 | アンインストール |
|---|---|
| ネイティブ（macOS・Linux・WSL） | `~/.local/bin/claude` と `~/.local/share/claude` を削除 |
| ネイティブ（Windows） | `%USERPROFILE%\.local\bin\claude.exe` と `%USERPROFILE%\.local\share\claude` を削除 |
| Homebrew | `brew uninstall --cask claude-code` |
| WinGet | `winget uninstall Anthropic.ClaudeCode` |
| npm | `npm uninstall -g @anthropic-ai/claude-code` |

設定や会話の履歴は `~/.claude` フォルダと `~/.claude.json` に残ります。これらを消すと、設定、許可したツール、MCP サーバーの設定、セッションの履歴がすべて消えるので注意してください。

## まとめ

- **Claude Code は有料プラン（Pro・Max・Team・Enterprise）か Claude Console のアカウントで使えます。** 無料プランでは使えません。
- **インストールはネイティブインストーラーの1行が推奨**です。Windows は PowerShell なら `irm https://claude.ai/install.ps1 | iex` です。
- **npm 版で `running scripts is disabled` が出たら**、`claude.cmd` を使うか、実行ポリシーを `RemoteSigned`（CurrentUser）にするか、ネイティブ版で入れ直します。
- **作業したいフォルダで `claude` を起動し、日本語でそのまま頼むだけ**です。今回の練習では、ファイル1つの作成が約3秒で終わりました。
- **auto mode が初期設定**です。不安なら Shift+Tab で確認が出るモードに切り替えます。使用量は `/usage` で確認できます。

## よくある質問

**Claude Code は無料で使えますか？**
使えません。公式ドキュメントでは、Claude の無料プランには Claude Code が含まれないと明記されています。Pro 以上のプランか、Claude Console（API の従量課金）のアカウントが必要です。

**Claude Code は日本語で使えますか？**
はい。指示は日本語でそのまま書けます。画面のメニューや表示は英語ですが、Claude は指示と同じ言語で答えます。

**Windows でも WSL は必要ですか？**
必要ありません。PowerShell か CMD からそのままインストールして使えます。Linux のツールを使いたい場合や、サンドボックス機能を使いたい場合は WSL 2 を選びます。

**`claude` と打つと「running scripts is disabled」と出ます。**
npm で入れた場合に出る PowerShell の実行ポリシーのエラーです。`claude.cmd` で起動するか、`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` を実行するか、ネイティブインストーラーで入れ直してください。

**Claude Code とデスクトップアプリの使用量は別ですか？**
同じです。サブスクリプションでは、Claude Code と Claude アプリ（Web・デスクトップ・モバイル）は同じ上限を共有します。

**VS Code の中で使えますか？**
使えます。公式に VS Code と JetBrains の拡張機能があり、エディタの中から Claude Code を使えます。

## 費用を計算してみる

Claude Code をサブスクリプションで使うか API の従量課金で使うかで迷ったら、[コーディングエージェント費用計算機](/ja/agents) で1か月の API 費用を試算し、Pro や Max と比べてみてください。サブスクと API のどちらが安いかは [サブスク vs API 計算機](/ja/plans) でも確認できます。

*インストール方法と動作条件は2026年10月12日に Claude Code の公式ドキュメントで確認しました。画面は Windows の PowerShell、Claude Code v2.1.295 のものです。*

## 出典

- [Claude Code Docs: Advanced setup](https://code.claude.com/docs/en/setup)
- [Claude Code Docs: Quickstart](https://code.claude.com/docs/en/quickstart)
- [Claude Code Docs: Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install)
- [Claude Code Docs: Commands](https://code.claude.com/docs/en/commands)
- [Claude Code Docs: Choose a permission mode](https://code.claude.com/docs/en/permission-modes)
- [Anthropic: Claude plans and pricing](https://claude.com/pricing)
- [Microsoft Learn: about_Execution_Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies)
<!-- autoimg -->
