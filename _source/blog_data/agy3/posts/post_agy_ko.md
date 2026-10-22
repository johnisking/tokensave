# 같은 오퍼스 5.5인데 토큰이 68~88% 적었다: Antigravity CLI vs Claude Code vs Codex 실측

구글은 2026년 6월 18일부터 개인 계정에서 Gemini CLI를 막고, 새로 나온 Antigravity CLI(`agy`)로 옮기라고 안내하고 있습니다. 그런데 Antigravity는 Claude 모델도 돌릴 수 있습니다. 덕분에 보기 드문 비교가 가능해졌습니다. 같은 모델(Claude 오퍼스 5.5)을 서로 다른 코딩 도구에 넣으면 토큰이 얼마나 달라질까요? Antigravity CLI, Claude Code, Codex를 같은 프롬프트로 44번 돌리고, 만들어진 게임은 전부 브라우저로 직접 확인했습니다.

## 어떻게 쟀나

- Windows 11, 2026-10-22. 실행마다 빈 폴더를 새로 만들고 하나씩 차례로 돌렸습니다
- Claude Code 2.1.295 + 오퍼스 5.5 (Max 요금제)
- Codex CLI 0.162 + gpt-6-luna (ChatGPT 요금제)
- Antigravity CLI 1.4.5 + Gemini 4 Argon, 그리고 + Claude 오퍼스 5.5 (개인 구글 계정)
- 기본 비용: "Reply with the single word OK."에 가짜 MCP 도구 0, 1, 10, 30개를 붙여 각 2회
- 과제: 2단계, 점수, 목숨 3개가 있는 벽돌깨기 게임을 index.html 한 파일로, effort medium, 각 3회
- 토큰 수는 각 도구가 JSON으로 보고한 값입니다

## 결과 1: 아무것도 안 했을 때의 토큰

| 도구 | "OK" 한 마디의 입력 토큰 |
|---|---:|
| Claude Code + 오퍼스 5.5 | 35,781 |
| Codex + gpt-6-luna | 14,818 |
| Antigravity + Gemini 4 Argon | 6,745 |
| Antigravity + 오퍼스 5.5 | 5,326 (+캐시 읽기 5,167) |

대부분은 도구 자체의 지시문과 도구 설명이고, 요청할 때마다 다시 실립니다.

## 결과 2: 똑같은 코딩 과제

| 도구 | 입력 | 출력 | 시간(초) | 줄 수 | 제대로 된 게임 |
|---|---:|---:|---:|---:|---:|
| Claude Code + 오퍼스 5.5 | 78,671 | 7,313 | 58 | 451 | 3/3 |
| Codex + gpt-6-luna | 55,680 | 4,563 | 68 | 42 (압축된 코드) | 3/3 |
| Antigravity + Gemini 4 Argon | 13,041 (+캐시 6,796) | 6,373 | 81 | 608 | 3/3 |
| Antigravity + 오퍼스 5.5 | 9,822 (+캐시 15,381) | 4,378 | 42 | 236 | 3/3 |

같은 오퍼스 5.5인데 Antigravity에서는 Claude Code보다 입력 토큰이 68~88% 적었고, 출력은 40% 적었고, 27% 빨리 끝났습니다. 대신 Claude Code가 만든 게임이 더 길었습니다(451줄 대 236줄). Claude Code는 한 번에 API 가격 기준 $0.37로 보고했고, Antigravity와 Codex는 구독 요금제라 가격이 나오지 않습니다.

게임 12개는 전부 제대로 돌아갔습니다. 벽돌을 깨면 점수가 오르고, 2단계가 나오고, 목숨이 3, 2, 1, 0으로 줄어듭니다. Codex 게임 2개는 자동 검사가 점수를 못 읽어서 손으로 확인했고, 둘 다 점수가 올라갔습니다.

## 왜 숫자 하나가 아니라 범위인가

Antigravity는 `input_tokens`와 `cache_read_tokens`를 따로 보고하는데, 하나가 다른 하나에 포함되는지는 문서에 나와 있지 않습니다. 오퍼스 실행에서는 캐시 읽기(15,381)가 입력(9,822)보다 커서, 적어도 여기서는 입력 안에 들어 있을 수 없습니다. 그래서 둘 다 적었습니다. 보고된 입력만 보면 88% 적고, 캐시 읽기를 더하면 68% 적습니다. 더한 쪽으로 봐도 Claude Code보다 훨씬 적습니다.

## MCP 도구는 이제 거의 상관없다

| | MCP 도구 30개를 붙였을 때 |
|---|---:|
| Claude Code | +388 토큰 |
| Codex | +0 |
| Antigravity + Gemini | +582 |
| Antigravity + 오퍼스 | +417 |

Antigravity에서는 도구 1개만 붙여도 약 280~460토큰이 늘었고, 나머지 29개는 거의 늘지 않았습니다. 네 경우 모두 도구의 자세한 설명은 실제로 쓸 때만 불러오는 것으로 보입니다.

## 정리

- 모델만큼 그 모델을 감싸는 코딩 도구가 중요합니다. 같은 오퍼스 5.5가 Antigravity에서는 입력을 몇 분의 일만 읽었습니다.
- 토큰이 적다고 결과가 더 좋은 건 아닙니다. Claude Code가 더 긴 게임을 만들었고, 게임은 모든 도구에서 다 돌아갔습니다.
- 개인 계정으로 Gemini CLI를 쓰던 분이라면 Antigravity CLI가 대체품이고, 꽤 가볍습니다.

## 한계

- 기본 비용은 2회, 게임은 3회씩. 과제 하나, 컴퓨터 하나, 하루 동안 잰 값입니다
- 도구마다 캐시를 세는 방식이 달라서 직접 비교할 때는 조심해야 합니다
- Antigravity가 `claude-opus-5-5-medium`이라는 이름 뒤에서 오퍼스 5.5를 어떻게 설정하는지는 알 수 없습니다

## 데이터

- 전체 데이터, 실행별 CSV, 방법(CC BY 4.0): https://tokensave.app/data/antigravity-cli-vs-claude-code-vs-codex
- 앞서 잰 Claude Code vs Codex: https://tokensave.app/data/claude-code-vs-codex-tokens
