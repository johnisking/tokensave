# Update notes for the four posts (append at the end, above "Data")

## EN (Dev.to, Hashnode)

## Update (October 24): checked with all three tokenizers

I counted 76 of the game files with each company's own tokenizer, no matter which model wrote them (Claude via Claude Code, Gemini 4 Argon via the Google AI Studio counter, GPT with o200k).

| Code written by | Claude | Gemini | GPT |
|---|---:|---:|---:|
| Opus 5.5 (Claude Code) | 512 | 399 | 334 |
| Gemini 4 Argon | 451 | 346 | 290 |
| gpt-6-luna (Codex) | 534 | 407 | 338 |

Tokens per 1,000 characters. For the same code, Claude's tokenizer needs 55% more tokens than GPT's (every file between +47% and +65%) and 29% more than Gemini's.

- Against GPT, the gap is the tokenizer: both models wrote code of about the same density and added a similar amount beyond the code (14% and 11%).
- Against Gemini, the tokenizer explains about half. The rest is that Gemini's own code needed 13% to 15% fewer tokens per character under all three tokenizers, and it added less beyond the code (7%).

Per-file counts: https://tokensave.app/data/output-tokens-per-character-tokenizer-check.csv

## JA (Qiita)

## 追記（10月24日）：3社のトークナイザーで直接確認

ゲームファイル76個を、どのモデルが書いたかに関係なく、各社のトークナイザーで数えました（ClaudeはClaude Code、Gemini 4 ArgonはGoogle AI Studioのカウンター、GPTはo200k）。

| コードを書いたモデル | Claude | Gemini | GPT |
|---|---:|---:|---:|
| Opus 5.5（Claude Code） | 512 | 399 | 334 |
| Gemini 4 Argon | 451 | 346 | 290 |
| gpt-6-luna（Codex） | 534 | 407 | 338 |

1,000文字あたりのトークン数です。同じコードでも、ClaudeのトークナイザーはGPTより55%（全ファイルで+47〜65%）、Geminiより29%多く数えます。

- GPTとの差は、ほぼトークナイザーです。両モデルのコードの密度は同程度で、コード以外の分（14%と11%）も近い値でした。
- Geminiとの差は、トークナイザーで約半分が説明できます。残りは、Geminiが書いたコード自体が3社どのトークナイザーでも13〜15%少ないトークンで済むことと、コード以外の分が少ないこと（7%）です。

ファイル別の数値：https://tokensave.app/data/output-tokens-per-character-tokenizer-check.csv

## KO (velog)

## 추가 (10월 24일): 세 회사 토크나이저로 직접 확인

게임 파일 76개를, 어느 모델이 썼는지와 상관없이 각 회사 토크나이저로 셌습니다(Claude는 Claude Code, Gemini 4 Argon은 Google AI Studio 계산기, GPT는 o200k).

| 코드를 쓴 모델 | Claude | Gemini | GPT |
|---|---:|---:|---:|
| 오퍼스 5.5 (Claude Code) | 512 | 399 | 334 |
| Gemini 4 Argon | 451 | 346 | 290 |
| gpt-6-luna (Codex) | 534 | 407 | 338 |

1,000자당 토큰입니다. 같은 코드라도 Claude 토크나이저는 GPT보다 55%(모든 파일이 +47~65% 사이), Gemini보다 29% 많이 셉니다.

- GPT와의 차이는 거의 토크나이저 때문입니다. 두 모델이 쓴 코드의 밀도가 비슷했고, 코드 외에 더 붙은 분량(14%, 11%)도 비슷했습니다.
- Gemini와의 차이는 토크나이저로 절반쯤 설명됩니다. 나머지는 Gemini가 쓴 코드 자체가 세 토크나이저 모두에서 글자당 토큰이 13~15% 적었고, 코드 외 분량도 더 작았기(7%) 때문입니다.

파일별 수치: https://tokensave.app/data/output-tokens-per-character-tokenizer-check.csv
