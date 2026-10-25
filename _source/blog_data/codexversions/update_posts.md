# Update sections for the Claude Code baseline posts (append above "Data")

## EN (Dev.to, Hashnode)

## Update (October 25): Codex CLI over the same weeks

I ran the same test on OpenAI's Codex CLI: all 18 releases from 0.155.0 (September 17) to 0.164.0 (October 23), the prompt "a" with `codex exec`, gpt-6-luna, reasoning effort low, 3 runs each.

| | Sep 17 | Oct 23 | Change | Releases where it changed |
|---|---:|---:|---:|---:|
| Codex CLI | 13,147 | 13,019 | −1% | 3 of 17 |
| Claude Code | 28,906 | 18,841 | −35% | 12 of 21 measured steps |

- Codex barely moved: three small changes of 4 to 100 tokens.
- Don't compare the two totals directly. They use different tokenizers, and for the same code Claude's counts about 55% more tokens than OpenAI's. The point is how each changes from release to release.
- Older Codex versions could not be measured: with a ChatGPT plan login the server refuses every model they can use.

Codex CSV: https://tokensave.app/data/codex-cli-baseline-tokens-by-version.csv

## JA (Qiita)

## 追記（10月25日）：同じ期間のCodex CLI

OpenAIのCodex CLIでも同じテストをしました。0.155.0（9月17日）から0.164.0（10月23日）までの全18リリースに、`codex exec` で「a」だけを送信（gpt-6-luna、推論レベルlow、各3回）。

| | 9月17日 | 10月23日 | 変化 | 数字が変わったリリース |
|---|---:|---:|---:|---:|
| Codex CLI | 13,147 | 13,019 | −1% | 17回中3回 |
| Claude Code | 28,906 | 18,841 | −35% | 測った21区間中12回 |

- Codexはほとんど変わりませんでした。変化は3回、4〜100トークンずつです。
- 2つの合計をそのまま比べないでください。トークナイザーが違い、同じコードでもClaudeのほうが約55%多く数えます。見るべきは、リリースごとの変わり方です。
- それより古いCodexは測れませんでした。ChatGPTプランでログインすると、それらが使えるモデルをサーバーがすべて拒否します。

Codex CSV：https://tokensave.app/data/codex-cli-baseline-tokens-by-version.csv

## KO (velog)

## 추가 (10월 25일): 같은 기간의 Codex CLI

OpenAI Codex CLI로도 같은 테스트를 했습니다. 0.155.0(9월 17일)부터 0.164.0(10월 23일)까지 18개 릴리스 전부에 `codex exec`로 "a"만 보냈습니다(gpt-6-luna, 추론 수준 low, 버전마다 3회).

| | 9월 17일 | 10월 23일 | 변화 | 숫자가 바뀐 릴리스 |
|---|---:|---:|---:|---:|
| Codex CLI | 13,147 | 13,019 | −1% | 17번 중 3번 |
| 클로드 코드 | 28,906 | 18,841 | −35% | 잰 21구간 중 12번 |

- Codex는 거의 그대로였습니다. 바뀐 건 세 번, 4~100토큰씩입니다.
- 두 합계를 그대로 비교하면 안 됩니다. 토크나이저가 달라서, 같은 코드라도 클로드 쪽이 약 55% 더 많이 셉니다. 봐야 할 건 릴리스마다 어떻게 바뀌느냐입니다.
- 그보다 오래된 Codex는 잴 수 없었습니다. ChatGPT 요금제로 로그인하면 그 버전들이 쓸 수 있는 모델을 서버가 전부 거부합니다.

Codex CSV: https://tokensave.app/data/codex-cli-baseline-tokens-by-version.csv
