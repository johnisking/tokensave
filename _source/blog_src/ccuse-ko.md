![Claude Code·Codex·Cursor 사용량 확인법과 실제 비용](/claude-code-sayongnyang-hwagin-ko.jpg)

Claude Code는 내가 요금제 한도에 얼마나 가까운지는 알려 주지만, 토큰이 어디에 쓰였는지는 잘 알려 주지 않습니다. 세션 안에서 `/usage`를 입력하면 5시간 한도와 주간 한도가 퍼센트 막대로 나오고, API로 쓰는 경우엔 지금 세션의 예상 금액이 나옵니다. 하지만 "지난 화요일엔 얼마를 썼는지", "이번 달 어떤 프로젝트가 가장 많이 썼는지", "Max 요금제가 토큰당 결제보다 정말 이득이었는지" 같은 기록은 보여 주지 않습니다.

그런데 이 정보는 이미 내 컴퓨터에 있습니다. Claude Code는 대화를 모두 기록 파일로 남기고, 응답마다 모델 이름과 토큰 수를 정확히 적어 둡니다. ccusage나 CodeBurn 같은 명령줄 도구가 이 파일을 읽어 합산하는 방식입니다. 저는 설치 없이 같은 답을 보고 싶어서, 브라우저 안에서 기록을 읽는 [Claude Code 사용량 분석기](/ko/claude-code-usage)를 만들었습니다. Codex 기록과 Cursor 사용량 CSV도 함께 읽습니다.

이 글에서는 사용량 기록이 어디에 있는지, 확인하는 방법은 무엇이 있는지, 그리고 제 실제 기록을 분석기에 넣었더니 무엇이 나왔는지 정리했습니다. 아래 숫자는 모두 그 기록과 2026년 10월 15일에 확인한 공식 요금표에서 나온 것입니다.

## Claude Code 사용량은 어디에 기록될까?

Claude Code는 세션마다 대화 기록을 `~/.claude/projects/` 아래에 저장합니다. 프로젝트마다 폴더가 하나씩 생기고, 세션 하나가 `.jsonl` 파일 하나입니다(한 줄에 JSON 하나). 서브에이전트 대화는 그 세션 옆의 `subagents/` 폴더에 들어갑니다.

| 운영체제 | 폴더 |
|---|---|
| Windows | `%USERPROFILE%\.claude\projects` |
| Mac | `~/.claude/projects` |
| Linux | `~/.claude/projects` (CLAUDE_CONFIG_DIR을 바꿨다면 그 안의 `projects/`) |

모델의 응답마다 `usage` 항목이 있고, 비용에 영향을 주는 값은 다섯 가지입니다.

- **입력 토큰**: 캐시되지 않은 새 입력
- **캐시 쓰기 토큰**: 프롬프트 캐시에 새로 저장한 입력(5분용·1시간용으로 나뉨)
- **캐시 읽기 토큰**: 캐시에서 다시 읽은 입력
- **출력 토큰**: 모델이 쓴 답(생각 과정 포함)
- **모델**: 예를 들어 `claude-opus-5-5`

여기서 자주 헷갈리는 점이 두 가지 있습니다. 첫째, 같은 응답이 스트리밍되는 동안 여러 줄에 나눠 기록되고, 세션을 이어서 열면 다시 복사되기도 합니다. 그냥 더하면 같은 응답을 여러 번 세게 됩니다. 분석기는 메시지 ID와 요청 ID로 응답 하나를 한 번만 셉니다. 둘째, 기록은 영원히 남지 않습니다. Claude Code 공식 문서에 따르면 `cleanupPeriodDays`보다 오래된 기록을 지우는데, **기본값이 30일**입니다. 더 오래 보고 싶다면 기록이 지워지기 전에 `~/.claude/settings.json`에서 이 값을 늘려 두세요.

## Claude Code 사용량을 확인하는 방법 4가지

![Claude Code 사용량을 확인하는 방법 4가지: 방법, 보이는 것, 설치, 날짜·프로젝트별 기록, 요금제 vs API, Codex·Cursor](/claude-code-sayongnyang-hwagin-claude-code-4-ko.jpg)

![Claude Code 사용량을 확인하는 방법 4가지: 방법, 보이는 것, 설치, 날짜·프로젝트별 기록, 요금제 vs API, Codex·Cursor](/claude-code-sayongnyang-hwagin-claude-code-4-ko.jpg)

![Claude Code 사용량을 확인하는 방법 4가지: 방법, 보이는 것, 설치, 날짜·프로젝트별 기록, 요금제 vs API, Codex·Cursor](/claude-code-sayongnyang-hwagin-claude-code-4-ko.jpg)

| 방법 | 보이는 것 | 설치 | 날짜·프로젝트별 기록 | 요금제 vs API | Codex·Cursor |
|---|---|---|---|---|---|
| Claude Code 안의 `/usage` | 요금제 한도 막대, 현재 세션, 한도를 쓰는 항목 | 필요 없음 | 없음 | 없음 | 없음 |
| ccusage (`npx ccusage`) | 터미널에서 일별·월별·세션별 보고서 | Node.js | 있음 | 없음 | Claude Code 중심 |
| CodeBurn (`npx codeburn`) | 터미널 대시보드, 여러 도구 | Node.js | 있음 | 없음 | 있음(Cursor는 추정) |
| [토큰세이브 사용량 분석기](/ko/claude-code-usage) | 날짜·프로젝트·모델·도구별 비용, CSV | 필요 없음(브라우저) | 있음 | 있음 | 있음 |

한도에 걸릴 것 같은지 확인하는 데는 `/usage`가 맞습니다. Pro·Max 요금제에서는 서브에이전트, MCP 서버, 캐시 미스처럼 한도를 많이 쓰는 항목도 보여 줍니다. 다만 몇 주치를 돌아보는 용도는 아닙니다. 터미널에 익숙하다면 ccusage나 CodeBurn이 좋고, 둘 다 같은 `.jsonl` 파일을 읽습니다. 브라우저 분석기는 Node.js를 설치하고 싶지 않거나, 요금제와 API 비교를 한 화면에서 보고 싶은 분을 위한 것입니다.

## 분석기 사용법

![파일 선택 화면과 Claude Code·Codex·Cursor 기록 위치 안내](/claude-code-usage-analyzer-pick-ko.jpg)

1. [tokensave.app/ko/claude-code-usage](/ko/claude-code-usage)를 엽니다.
2. **폴더 선택**을 누르고 `projects` 폴더를 고릅니다. Windows는 폴더 선택 창 위쪽 주소창에 `%USERPROFILE%\.claude\projects`를 붙여 넣고 Enter를 누르면 됩니다. Mac은 ⌘ + Shift + G를 누르고 `~/.claude/projects`를 붙여 넣습니다.
3. 원하면 Codex의 `~/.codex/sessions` 폴더와 Cursor 사용량 CSV(Cursor 대시보드 → Usage → Export CSV)도 함께 넣습니다.
4. 결과를 봅니다. 기간을 전체·7일·30일·이번 달로 바꿀 수 있고, 내 요금제를 고르면 비교가 나옵니다.

폴더를 고를 때 Chrome이 "이 사이트에 파일을 업로드할까요?"라고 물을 수 있습니다. 폴더를 열 때 나오는 브라우저의 고정 문구입니다. 페이지는 브라우저의 파일 기능으로 파일을 읽어 숫자만 더하고, 프롬프트나 코드는 탭 밖으로 나가지 않습니다. 서버로 보내는 것도 없습니다.

## 제 실제 기록을 넣어 보니

![분석기 결과: API 환산 비용, 토큰, 캐시로 아낀 돈, 도구별 비용](/claude-code-usage-analyzer-result-ko.jpg)

세 가지 기록을 넣었습니다. 이 사이트를 만들고 관리하는 데 쓴 Claude 에이전트 세션(Claude Code와 같은 형식으로 기록됩니다), 제 PC에 있던 Codex 세션, 그리고 제 계정의 Cursor 사용량 CSV입니다.

| 도구 | 응답 | 토큰 | API 환산 비용 | 쓰던 요금제 |
|---|---|---|---|---|
| Claude Code (Opus 5.5) | 1,636 | 2억 7,750만 | $145.90 (약 19만 6천 원) | Max 5× |
| Codex (GPT-5.6 Terra, GPT-6 Luna) | 108 | 650만 | $1.98 | 무료 |
| Cursor (Grok 4.6) | 2 | 37만 9천 | $0.29 | 무료 |

Claude Code 기록은 9월 29일부터 10월 15일 사이, 실제로 쓴 날은 10일입니다. 가장 많이 쓴 10월 8일 하루가 API 요금으로 약 $39였습니다.

가장 놀란 건 토큰의 구성이었습니다. 2억 7,750만 토큰 가운데 새 입력은 약 3천 토큰뿐이었습니다. 캐시 읽기가 약 2억 6,400만, 캐시 쓰기가 약 1,080만, 출력이 약 180만 토큰이었습니다. 즉 **Claude Code가 "쓴" 토큰의 95% 이상은 같은 맥락을 캐시에서 다시 읽은 것**입니다. 에이전트는 단계마다 지금까지의 대화, 열어 본 파일, 도구 결과를 다시 보내고, 캐시가 그걸 싸게 만들어 주는 구조입니다.

그렇다고 공짜는 아닙니다. Opus 5.5 요금으로 $145.90가 어디에 쓰였는지 나누면 이렇습니다.

| 항목 | 100만 토큰당 가격 | 비용 비중 |
|---|---|---|
| 캐시 읽기 | $0.20 | 약 36% |
| 5분 캐시 쓰기 | $5.00 | 약 34% |
| 출력 | $20.00 | 약 25% |
| 1시간 캐시 쓰기 | $8.00 | 약 4% |
| 새 입력 | $4.00 | 1% 미만 |

Opus 5.5의 캐시 읽기는 일반 입력보다 95% 싸지만, 양이 워낙 많아서 비용 비중은 가장 컸습니다. 캐시 쓰기도 거의 비슷한데, 새 파일이나 도구 결과, 긴 답은 먼저 캐시에 써야 그다음부터 싸게 읽을 수 있기 때문입니다. 출력은 180만 토큰밖에 안 되지만 100만 토큰당 $20이라 전체의 4분의 1을 차지했습니다.

캐시가 없었다면 같은 캐시 읽기를 일반 입력 가격으로 내야 해서 약 $1,017(약 137만 원)가 더 들었을 겁니다. 화면의 "캐시로 아낀 돈"이 이 금액입니다.

## Claude Max는 이득일까? 요금제와 API 비교

![요금제 비교: Claude Max 5× 17일 요금과 같은 사용량의 API 비용](/claude-code-usage-analyzer-plan-ko.jpg)

분석기는 고른 요금제와, 같은 기간 같은 도구의 API 비용을 비교합니다. 제 Claude 기록은 17일에 걸쳐 있습니다. Max 5×는 부가세 별도 월 $100이라 17일이면 약 $56.67(약 7만 6천 원)입니다. 같은 토큰을 API로 냈다면 $145.90였으니, **낸 요금의 약 257%만큼 API 가치를 쓴 셈**입니다. 에이전트로 작업을 많이 한다면 토큰당 결제보다 구독이 확실히 쌌습니다.

내 결과를 볼 때 주의할 점이 두 가지 있습니다.

- **요금제에는 한도가 있습니다.** Pro·Max는 5시간마다 초기화되고 주간 한도도 있습니다. API 환산 금액이 요금의 몇 배나 된다면 이미 한도에 자주 걸리고 있을 가능성이 높고, 그때 선택지는 기다리기, 상위 요금제, 추가 사용량 결제입니다.
- **적게 쓰면 요금제가 손해일 수 있습니다.** 제 Codex·Cursor 사용량은 무료 요금제였고 각각 $1.98, $0.29였습니다. 이 정도 Codex 사용에 ChatGPT Plus(월 $20)를 냈다면 요금보다 적게 쓴 것이 됩니다. 분석기는 이런 경우를 주황색으로 보여 줍니다.

아직 Claude Code를 써 보지 않아서 기록 대신 예상 비용을 보고 싶다면, 작업 크기와 하루 작업 수로 한 달 비용을 계산하는 [코딩 에이전트 비용 계산기](/ko/agents)를 쓰면 됩니다.

## Codex와 Cursor 사용량

**Codex**는 `~/.codex/sessions/년/월/일/` 아래에 세션마다 `rollout-….jsonl` 파일을 남깁니다. 응답마다 사용량을 적는 대신, 단계마다 세션 전체의 누적 합계를 적습니다. 분석기는 단계 사이에 늘어난 만큼을 OpenAI API 요금으로 계산하고, 캐시 입력은 캐시 단가로 계산합니다. 제 기록의 GPT-5.6 Terra는 100만 토큰당 입력 $2, 캐시 입력 $0.20, 출력 $12이고, GPT-6 Luna는 각각 $0.10, $0.01, $0.50입니다. 보관된 세션은 같은 이름으로 `archived_sessions/`로 옮겨지기 때문에, 같은 파일 이름은 한 번만 셉니다.

**Cursor**는 사정이 다릅니다. 제 PC의 Cursor 로컬 데이터베이스를 열어 봤더니 대화마다 토큰 수가 0으로 저장돼 있었습니다. 최신 Cursor는 내 컴퓨터에 토큰 수를 남기지 않고, 그래서 명령줄 도구도 Cursor는 글자 수로 추정할 수밖에 없습니다. 정확한 자료는 Cursor 대시보드의 사용량 내보내기입니다. Usage 화면에서 **Export CSV**를 누르면 날짜, 모델, 캐시 쓰기 포함·제외 입력, 캐시 읽기, 출력, Cursor가 매긴 금액이 요청마다 나옵니다. 분석기는 이 금액을 그대로 씁니다.

## 비용을 줄이려면

비용의 대부분이 캐시와 출력이라는 걸 알면 줄이는 방법도 보입니다.

- **새 작업은 새 세션에서 시작하세요.** `/clear`로 이전 맥락을 비우면 다음 단계부터 그걸 다시 읽지 않습니다. 세션이 길어질수록 앞의 내용 전체에 캐시 읽기 비용이 계속 붙습니다.
- **일상적인 작업은 Sonnet으로.** Sonnet 5.5는 100만 토큰당 $2/$10, Opus 5.5는 $4/$20이라 같은 세션이 API 기준 약 50% 쌉니다.
- **비싼 날을 확인하세요.** 날짜별 그래프를 보면 어느 날, 어떤 종류의 작업에서 비용이 튀었는지 바로 보입니다.
- **안 쓰는 도구는 정리하세요.** 요금제를 쓴다면 `/usage`에서 어떤 MCP 서버와 서브에이전트가 한도를 쓰는지 볼 수 있습니다.

더 많은 방법은 [Claude Code 토큰 절약법](/ko/blog/claude-code-token-jeolyak)에, 한도 자체는 [Claude Code 사용량 한도 정리](/ko/blog/claude-code-sayongnyang-hando)에 정리해 두었습니다.

## 자주 묻는 질문

**Claude Code 사용 기록은 어떻게 보나요?**
[사용량 분석기](/ko/claude-code-usage)에서 `~/.claude/projects` 폴더를 열거나, 터미널에서 `npx ccusage`를 실행하면 됩니다. Claude Code 안의 `/usage`는 기록이 아니라 현재 한도를 보여 줍니다.

**분석기가 제 코드를 업로드하나요?**
아니요. 브라우저 탭 안에서 파일을 읽고 토큰 숫자만 더합니다. 어디로도 보내지 않습니다.

**API 환산 비용이 왜 요금제보다 훨씬 크게 나오나요?**
에이전트는 단계마다 전체 맥락을 다시 읽어서 캐시 토큰이 엄청나게 쌓입니다. 요금제는 정액이라 실제로 그만큼 내지 않고, 이 숫자는 같은 토큰을 토큰당 요금으로 냈을 때의 금액입니다.

**왜 최근 한 달 정도만 나오나요?**
Claude Code가 기본적으로 30일 지난 기록을 지우기 때문입니다. `settings.json`에서 `cleanupPeriodDays`를 늘리면 더 오래 남습니다.

**Gemini CLI, Copilot, Windsurf도 되나요?**
아직은 안 됩니다. 지금은 Claude Code, Codex, Cursor CSV를 읽습니다.

## 마무리

Claude Code는 이미 쓴 토큰을 하나도 빠짐없이 기록하고 있고, 어려운 건 그걸 읽는 일입니다. `/usage`는 한도에 얼마나 가까운지를, `~/.claude/projects`의 기록은 돈이 어디로 갔는지를 알려 줍니다. 제 17일 치 에이전트 작업에서는 토큰 대부분이 캐시 읽기였고, 캐시 관련 비용이 API 환산 비용의 약 4분의 3을 차지했으며, Max 5×는 요금의 약 257%만큼 값을 했습니다. 무료 요금제로 쓴 Codex와 Cursor는 합쳐도 몇 달러였습니다. 내 숫자가 궁금하다면 [사용량 분석기](/ko/claude-code-usage)에 폴더를 넣고 내 요금제와 비교해 보세요.

## 출처

- [Claude Code 문서: .claude 디렉터리(기록 위치와 30일 정리)](https://code.claude.com/docs/en/claude-directory)
- [Claude Code 문서: 비용 관리(/usage)](https://code.claude.com/docs/en/costs)
- [Anthropic API 요금(프롬프트 캐시 단가)](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI API 요금](https://developers.openai.com/api/docs/pricing)
- [Claude 요금제](https://claude.com/pricing) · [Cursor 요금제](https://cursor.com/pricing)
- [ccusage](https://github.com/ryoppippi/ccusage) · [CodeBurn](https://github.com/getagentseal/codeburn)
<!-- autoimg -->
