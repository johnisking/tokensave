![Codex 사용량 한도 정리: 5시간·주간 한도와 초기화](/codex-sayongnyang-hando-ko.jpg)

OpenAI의 코딩 에이전트 Codex는 ChatGPT Plus, Pro, Business 요금제에 포함되어 있고, 요즘 사용량 한도에 가장 많이 걸리는 곳이기도 합니다. Codex는 ChatGPT Work와 사용량을 함께 쓰고, Plus와 Business에는 5시간 단위 한도가 있고(주간 한도가 추가로 적용될 수 있음), 어떤 모델을 쓰느냐에 따라 소진 속도가 크게 다릅니다. 어떻게 돌아가는지, 어떻게 하면 더 오래 쓸 수 있는지 정리했습니다.

## Codex가 포함된 요금제

Codex(와 ChatGPT Work) 사용량은 **Plus**($20), **Pro**($100, $200, $500), **Business** Standard·Premium 좌석에 포함됩니다. 무제한은 아닙니다. 요금제마다 포함된 사용량이 정해져 있습니다.

## 한도는 두 가지가 동시에

**5시간 단위 한도.** 첫 요청부터 시작되는 롤링 방식의 사용량입니다. 다 쓰면 구간이 초기화될 때까지 기다려야 합니다. Pro 100, Pro 200, Pro 500은 현재 Work와 Codex에 5시간 단위 한도가 없습니다. 포함된 사용량은 따로 있습니다.

**주간 한도.** OpenAI는 그 위에 주간 한도가 추가로 적용될 수 있다고 안내합니다. 여기에 걸리면 5시간 단위가 새로 시작됐더라도 초기화까지 기다려야 합니다.

Codex와 ChatGPT Work는 **같은 사용량**에서 차감됩니다.

## 모델별로 쓸 수 있는 양

![모델별로 쓸 수 있는 양: 모델, Plus, Business (Standard)](/codex-sayongnyang-hando-ko-2.jpg)

OpenAI 고객센터는 Plus와 Standard Business 기준으로 5시간 단위당 예상 로컬 메시지 수를 안내합니다. 어떤 모델을 고르느냐에 따라 숫자가 크게 달라집니다.

| 모델 | Plus | Business (Standard) |
|---|---|---|
| GPT-6 Astra | 약 5–45 | 약 5–45 |
| GPT-6.1 Sol | 약 15–160 | 약 15–160 |
| GPT-6 Sol | 약 15–150 | 약 15–150 |
| GPT-6 Luna | 약 350–3,000 | 약 350–3,000 |

범위의 아래쪽은 큰 코드베이스에서 길고 여러 단계를 거치는 작업, 위쪽은 짧고 간단한 요청 기준입니다. Pro 요금제는 현재 5시간 단위 한도가 없고, 포함된 사용량이 더 많습니다. Pro 100은 Plus의 5배, 신규 구독자 기준으로 Pro 200은 Plus의 10배, Pro 500은 Plus의 25배입니다(2026년 9월 22일~9월 29일 사이에 Pro 200 구독이 활성 상태였다면 10월 29일까지 예전 사용량이 유지됩니다). 배수는 OpenAI 공식 페이지가 아니라 OpenAI 티보 소티오(Thibault Sottiaux)의 X 글과 보도(WinBuzzer, Windows Report) 기준입니다.

**Ultrafast**는 Pro 500에서만 쓸 수 있는 더 빠른 모드로, 포함된 사용량과 크레딧을 더 빨리 소진합니다.

## Codex가 사용량을 빨리 쓰는 이유

다른 코딩 에이전트와 마찬가지로 Codex는 단계별로 일하고, 단계마다 작업 맥락 전체를 모델에 다시 보냅니다. 지시문, 도구 정의, 읽은 파일, 이전 단계까지 전부입니다. 25단계짜리 일반적인 기능 구현 작업이면 입력 토큰이 약 160만 개 들어갑니다. 같은 작업을 API로 하면 Sol급 모델로는 약 $0.72, GPT-6 Astra로는 약 $3.60이 드는데, 그래서 Astra의 사용량이 훨씬 적게 책정되어 있습니다. [AI 코딩 에이전트는 작업당 얼마가 드나요?](/blog/ai-coding-agent-cost) (영어)를 참고하세요.

## 사용량 확인하는 법

OpenAI 고객센터는 ChatGPT의 **Settings → Usage**를 안내합니다. 남은 사용량과 초기화 시각을 볼 수 있습니다. Codex도 한도에 가까워지면 경고를 띄웁니다.

## 한도에 걸렸을 때

![한도에 걸렸을 때: 초기화를 기다립니다. 5시간 단위 한도는 몇 시간 안에 다시 채워집니다.; 적립된 리셋을 쓰거나 즉시 리셋을 구매합니다. 자격이 되는 Plus와 Pro 계정에서 가능합니다.; 크레딧을 써서 계속 작](/codex-sayongnyang-hando-ko-3.jpg)

1. **초기화를 기다립니다.** 5시간 단위 한도는 몇 시간 안에 다시 채워집니다.
2. **적립된 리셋을 쓰거나 즉시 리셋을 구매합니다.** 자격이 되는 Plus와 Pro 계정에서 가능합니다.
3. **크레딧을 써서** 계속 작업합니다. 크레딧을 지원하는 요금제에 해당합니다.
4. 더 높은 Pro 등급으로 **업그레이드합니다.**
5. 넘치는 작업은 종량제 결제의 **API 키로** 처리합니다.

## 더 오래 쓰는 법

![더 오래 쓰는 법: 기본은 GPT-6.1 Sol이나 GPT-6 Sol로 두세요. GPT-6 Astra는 차이가 눈에 보이는 어려운 문제에만 쓰세요. 사용량을 훨씬 많이 씁니다.; 간단한 수정, 이름 바꾸기, 보일러플레이트에는](/codex-sayongnyang-hando-ko-4.jpg)

- **기본은 GPT-6.1 Sol이나 GPT-6 Sol로 두세요.** GPT-6 Astra는 차이가 눈에 보이는 어려운 문제에만 쓰세요. 사용량을 훨씬 많이 씁니다.
- **간단한 수정**, 이름 바꾸기, 보일러플레이트에는 **Luna를 쓰세요.**
- **작업을 작고 구체적으로 나누세요.** 단계가 줄면 다시 보내는 맥락도 줄어듭니다.
- **관련 없는 작업 사이에는 새로 시작하세요.** 이전 기록을 계속 끌고 가지 않도록요.
- 저장소 전체를 뒤지게 두지 말고 **Codex에 필요한 파일을 짚어 주세요.**
- **지시문 파일은 짧게 유지하고**, 평소 다른 언어를 쓴다면 영어로 작성하세요. GPT 토크나이저에서 한국어는 영어보다 토큰이 약 44%, 일본어는 79% 더 듭니다.

같은 습관 상당수가 Claude Code에도 통합니다. [Claude Code에서 토큰 아끼는 법](/ko/blog/claude-code-token-jeolyak)을 참고하세요.

## Codex냐 Claude Code냐

둘 다 $20, $100, $200 요금제에 포함되어 있고 한도 구조도 비슷합니다. 차이점은 [ChatGPT Pro vs Claude Max 비교](/ko/blog/chatgpt-pro-vs-claude-max)에 정리했고, [코딩 에이전트 계산기](/ko/agents)로 월 API 비용을 모든 요금제와 비교할 수 있습니다.

*한도는 자주 바뀝니다. 최신 수치는 OpenAI의 [Codex·Work 사용량 도움말](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)에서 확인하세요.*

## 출처

- [OpenAI 도움말: Work·Codex 사용량 관리](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)
- [OpenAI 도움말: Codex 저장된 리셋](https://help.openai.com/en/articles/20001498-how-banked-codex-resets-work)
- [ChatGPT 요금제와 Codex 가격](https://learn.chatgpt.com/docs/pricing)
- [OpenAI 도움말: ChatGPT Pro 등급 안내](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
<!-- autoimg -->
