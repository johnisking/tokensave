![챗GPT Pro vs Claude Max 요금제 비교: $100·$200 어디가 더 많이 줄까](/chatgpt-pro-vs-claude-max-ko.jpg)

챗GPT와 Claude의 요금제는 이제 거의 똑같은 가격대로 나뉩니다. $20, $100, $200, 그리고 챗GPT에는 $500이 하나 더 있습니다. 둘 다 코딩 에이전트도 들어 있습니다(챗GPT는 Codex, Claude는 클로드 코드). 그럼 같은 돈이면 어느 쪽이 더 많이 줄까요? 쓰는 방식에 따라 다르지만, 가격이 같다고 내용까지 같은 건 아닙니다.

## 요금제 나란히 보기

![요금제 나란히 보기: 가격, 챗GPT, 사용량, Claude, 사용량](/chatgpt-pro-vs-claude-max-ko-2.jpg)

미국 월 가격, 2026년 10월 확인 기준입니다.

| 가격 | 챗GPT | 사용량 | Claude | 사용량 |
|---|---|---|---|---|
| $20 | Plus | 기본 | Pro | 기본 |
| $100 | Pro 100 | Plus의 5배 | Max 5× | Pro의 5배 |
| $200 | Pro 200 | Plus의 10배* | Max 20× | Pro의 20배 |
| $500 | Pro 500 | Plus의 25배 + 초고속(Ultrafast) | – | – |

\* Pro 200은 신규 가입자 기준으로 Plus의 20배에서 10배로 줄었습니다. 2026년 9월 22일~9월 29일 중 한 번이라도 Pro 200 구독이 활성 상태였다면 10월 29일까지 예전 사용량이 유지됩니다. 챗GPT 배수는 OpenAI 공식 페이지가 아니라 OpenAI 티보 소티오(Thibault Sottiaux)의 X 글과 보도(WinBuzzer, Windows Report) 기준입니다.

사용량 배수는 각 회사의 $20 요금제를 기준으로 한 것이라, "Plus의 5배"와 "Pro의 5배"가 같은 작업량은 아닙니다. 두 회사 모두 정확한 토큰 수는 공개하지 않습니다.

## 2026년 9월에 달라진 점

**$200에서는 이제 Claude 쪽 배수가 더 큽니다.** Claude Max 20×는 기본 요금제의 20배, 챗GPT Pro 200은 이제 10배입니다. 두 $200 요금제 사이에서 고민하던 헤비 유저에게는 가장 큰 변화입니다.

**챗GPT는 큰 요금제 할인이 없어졌습니다.** Pro 100·200·500 모두 "Plus 사용량 1배"당 $20입니다. 반면 Claude Max 20×는 Max 5×보다 가격은 100% 높고 사용량은 300% 많아서, 바로 아래 요금제보다 1달러당 사용량이 많은 유일한 $200 요금제입니다. 자세한 내용은 [챗GPT Pro 100 vs 200 vs 500 요금제 비교](/ko/blog/chatgpt-pro-yogeumje-bigyo)를 보세요.

**Claude는 클로드 코드 주간 한도를 조금 줄였습니다.** 9월 14일, 여름 동안의 주간 한도 50% 임시 증량이 25% 영구 증량으로 바뀌면서 여름보다 약 17% 줄었습니다. [클로드 코드 사용량 한도 정리](/ko/blog/claude-code-sayongnyang-hando)를 참고하세요.

## 쓸 수 있는 모델

![쓸 수 있는 모델: 입력 100만 토큰, 출력 100만 토큰](/chatgpt-pro-vs-claude-max-ko-3.jpg)

**챗GPT:** OpenAI의 최상위 모델 GPT-6 Astra를 Pro 요금제에서 쓸 수 있고, Plus에도 Work와 Codex부터 순차 적용 중입니다. Pro 500에는 더 빠른 대신 사용량을 더 빨리 쓰는 초고속(Ultrafast) 모드가 있습니다.

**Claude:** 요금제는 Claude Sonnet 5.5와 Opus 5.5가 중심입니다. Max는 주로 더 비싼 Opus를 넉넉하게 쓸 여유를 줍니다.

API 가격을 보면 각 최상위 모델을 돌리는 데 드는 비용 차이가 보이고, 한도 체감이 다른 이유도 여기 있습니다.

| | 입력 100만 토큰 | 출력 100만 토큰 |
|---|---|---|
| GPT-6 Astra | $10 | $50 |
| Claude Opus 5.5 | $4 | $20 |
| GPT-6 Sol | $2 | $10 |
| Claude Sonnet 5.5 | $2 | $10 |

GPT-6 Astra는 토큰당 Claude Opus 5.5보다 150% 비쌉니다. 주로 최상위 모델을 쓴다면 같은 작업량에서 챗GPT 쪽 한도가 더 빨리 닳는다고 보면 됩니다. GPT-6 Sol과 Claude Sonnet 5.5는 토큰 가격이 똑같습니다.

## 코딩 에이전트: Codex vs 클로드 코드

둘 다 터미널이나 에디터에서 일하는 에이전트가 들어 있고, 둘 다 단계마다 작업 맥락 전체를 다시 보내서 채팅보다 토큰을 훨씬 많이 씁니다. 25단계짜리 일반적인 기능 작업이면 입력 토큰이 약 160만 개입니다. API로 계산하면 Sonnet 5.5나 GPT-6 Sol로 약 $0.72, Opus 5.5로 $1.43, GPT-6 Astra로 약 $3.60입니다.

에이전트로 매일 코딩한다면 거의 항상 요금제가 API보다 쌉니다. [코딩 에이전트 비용 계산기](/ko/agents)에서 내 사용량으로 두 요금제와 API 비용을 비교해 보세요.

## 어느 쪽을 고를까

![어느 쪽을 고를까: GPT-6 Astra를 꼭 써야 하거나, 이미지 생성·음성 등 챗GPT 앱 기능을 많이 쓴다.; 초고속 모드가 필요하고 $500(Pro 500)이 아깝지 않다.; 이미 Codex를 쓰고 있고 만족한](/chatgpt-pro-vs-claude-max-ko-4.jpg)

**챗GPT가 맞는 경우:**
- GPT-6 Astra를 꼭 써야 하거나, 이미지 생성·음성 등 챗GPT 앱 기능을 많이 쓴다.
- 초고속 모드가 필요하고 $500(Pro 500)이 아깝지 않다.
- 이미 Codex를 쓰고 있고 만족한다.

**Claude가 맞는 경우:**
- 주로 클로드 코드로 일하고, $200에서 가장 큰 사용량(Max 20×)을 원한다.
- 긴 문서와 코드를 다루고 Opus 5.5·Sonnet 5.5를 선호한다.
- 최상위 모델의 토큰당 가격이 중요하다(Opus 5.5가 Astra보다 싸다).

**$20에서는** 둘 다 괜찮은 출발점입니다. 마음에 드는 모델 쪽으로 시작해서 한도에 얼마나 자주 걸리는지 보고, 자주 걸릴 때만 올리세요.

## 둘 다 안 쓰는 방법도

하루에 몇 번 쓰는 정도라면 API가 어떤 요금제보다 쌀 수 있습니다. [구독 vs API 계산기](/ko/plans)가 내 사용량의 월 API 비용을 챗GPT·Claude·Gemini 모든 요금제와 나란히 보여줍니다. 한국어로 쓰면 영어보다 토큰이 약 44% 더 들어서 API 비용도 그만큼 늘어난다는 점도 계산에 반영됩니다.

*요금제와 한도는 자주 바뀝니다. 가입 전에 [chatgpt.com/pricing](https://chatgpt.com/pricing)과 [claude.com/pricing](https://claude.com/pricing)을 확인하세요.*

## 출처

- [ChatGPT 요금제와 Codex 가격](https://learn.chatgpt.com/docs/pricing)
- [OpenAI 도움말: ChatGPT Pro 등급 안내](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
- [Claude 도움말: Max 요금제란](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- [Claude 도움말: Pro·Max 요금제로 Claude Code 쓰기](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [OpenAI API 가격](https://developers.openai.com/api/docs/pricing)
- [Claude API 가격](https://platform.claude.com/docs/en/about-claude/pricing)
<!-- autoimg -->
