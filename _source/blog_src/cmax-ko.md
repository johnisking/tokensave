![Claude Max vs Pro 비교: $100·$200 요금제, 올릴 가치가 있을까](/claude-max-vs-pro-ko.jpg)

Claude Pro는 월 $20, Claude Max는 $100 또는 $200입니다. 둘 다 Claude 앱과 Claude Code가 포함되어 있으니, 진짜 질문은 간단합니다. 늘어나는 사용량이 5배, 10배 가격만큼의 가치가 있느냐는 것이죠. 많은 분들에게는 그렇지 않습니다. 하지만 Claude Code를 많이 쓰는 분이라면 Max 20×가 Anthropic이 파는 요금제 중 가장 가성비가 좋습니다.

## 요금제

![요금제: 요금제, 가격, 사용량, "Pro 1개분" 사용량당 가격](/claude-max-vs-pro-ko-2.jpg)

미국 가격, 2026년 10월 확인 기준:

| 요금제 | 가격 | 사용량 | "Pro 1개분" 사용량당 가격 |
|---|---|---|---|
| Pro | 월 $20 (연간 결제 시 $17) | 기본 | $20 |
| Max 5× | 월 $100 | Pro의 5배 | $20 |
| Max 20× | 월 $200 | Pro의 20배 | $10 |

세 요금제 모두 Claude Code가 포함되어 있고, Claude 앱과 Claude Code는 같은 사용량을 함께 씁니다.

## 핵심: Max 5×는 단위당 더 싸지 않고, Max 20×는 쌉니다

Max 5×는 5배 가격에 Pro의 5배 사용량을 줍니다. 조건은 똑같고, 양만 많을 뿐입니다.

Max 20×는 10배 가격에 Pro의 20배 사용량을 줍니다. **사용량 단위당 가격이 Pro의 절반입니다.** Pro 계정 10개분이 넘는 사용량이 필요하다면 당연히 이쪽이고, Max 5×로는 자주 부족하다면 API 크레딧을 추가하는 것보다 가성비가 좋습니다.

## 한도가 작동하는 방식

모든 요금제에는 한도가 두 가지 동시에 있습니다.

- **5시간 세션 한도.** 첫 메시지부터 시작되는 롤링 방식입니다. Anthropic은 2026년 5월 6일 Claude Code의 5시간 한도를 100% 늘렸습니다.
- **주간 한도.** 모든 사용량을 합쳐서 적용됩니다. 2026년 9월 14일, Anthropic은 Claude Code의 기본 주간 한도를 영구적으로 25% 올렸고, 이는 임시로 적용되던 50% 증량을 대체했습니다.

Max는 두 한도를 모두 배수만큼 늘려 줍니다. Claude Code에서 **/status**를 실행하면 현재 상태를 볼 수 있습니다. 자세한 내용은 [Claude Code 사용량 한도 정리](/ko/blog/claude-code-sayongnyang-hando)에 있습니다.

## Pro로 충분한 분

![Pro로 충분한 분: 하루에 몇 번, 주로 앱에서 Claude를 씁니다.; Claude Code는 몇 시간씩이 아니라 가끔 작업할 때만 씁니다.; 한도 메시지를 거의 또는 전혀 보지 않습니다.](/claude-max-vs-pro-ko-3.jpg)

- 하루에 몇 번, 주로 앱에서 Claude를 씁니다.
- Claude Code는 몇 시간씩이 아니라 가끔 작업할 때만 씁니다.
- 한도 메시지를 거의 또는 전혀 보지 않습니다.

이런 경우라면 $20으로 충분합니다. 가끔 더 필요할 때는 사용량 크레딧을 쓰거나 잠깐 기다리면 됩니다.

## Max 5×가 맞는 분

![Max 5×가 맞는 분: 거의 매주 Pro 한도에 걸립니다.; 하루에도 여러 번 Claude Code로 실제 업무를 합니다.; Sonnet보다 사용량을 빨리 쓰는 Opus를 더 많이 쓰고 싶습니다.](/claude-max-vs-pro-ko-4.jpg)

- 거의 매주 Pro 한도에 걸립니다.
- 하루에도 여러 번 Claude Code로 실제 업무를 합니다.
- Sonnet보다 사용량을 빨리 쓰는 Opus를 더 많이 쓰고 싶습니다.

## Max 20×가 맞는 분

- 하루 몇 시간씩 Claude Code를 돌리거나, 여러 세션을 동시에 돌립니다.
- Max 5×의 주간 한도에 계속 걸립니다.
- Opus를 기본 모델로 씁니다.

이 정도 사용량이면 API로는 보통 훨씬 더 비쌉니다. 저희 비용 모델로 계산하면, 하루에 기능 단위 작업을 15개씩 하는 헤비 유저는 API로 Sonnet을 쓸 때 월 약 $236, Opus를 쓸 때 약 $473이 듭니다. Max 20×는 $200입니다. [Claude Code 월 비용](/ko/blog/claude-code-yogeum)을 참고하세요.

## 어떤 요금제든 사용량을 늘려 쓰는 법

- 관련 없는 작업 사이에는 새 세션을 시작하고(**/clear**), 긴 작업에서는 **/compact**를 쓰세요.
- CLAUDE.md는 짧게 유지하세요. 단계마다 함께 전송됩니다.
- 일상적인 작업은 Sonnet으로, Opus는 어려운 문제에만 쓰세요.
- 평소 다른 언어로 쓴다면 지시문을 영어로 작성하세요. 한국어 지시문을 영어로 바꾸면 토큰이 약 31% 줄어드는데, [토큰 계산기](/ko/)의 💸 토큰 절약 버튼을 누르면 내 기기 안에서 바로 번역해 줍니다(PC용 Chrome 138 이상 또는 Edge 148 이상).

더 많은 방법은 [Claude Code에서 토큰 아끼는 법](/ko/blog/claude-code-token-jeolyak)에 있습니다.

## Claude Max냐 ChatGPT Pro냐

$200 가격대에서 Claude Max 20×는 이제 기본 요금제의 20배이고, ChatGPT Pro 200은 신규 구독자 기준으로 기본 요금제의 10배입니다. 두 회사의 기본 요금제 크기가 같지 않으니, 실제로 쓰는 것을 기준으로 비교하세요. [ChatGPT Pro vs Claude Max](/ko/blog/chatgpt-pro-vs-claude-max)를 참고하세요.

## 내 숫자로 확인하기

[코딩 에이전트 계산기](/ko/agents)로 내 Claude Code 사용 방식에 맞춰 Pro, Max, API를 비교하거나, 대화 위주라면 [구독 vs API 계산기](/ko/plans)를 써 보세요.

*가격과 한도는 바뀝니다. 업그레이드하기 전에 [claude.com/pricing](https://claude.com/pricing)을 확인하세요.*

## 출처

- [Claude 요금제 (Anthropic)](https://claude.com/pricing)
- [Pro·Max 요금제로 클로드 코드 사용하기 (Claude 도움말 센터)](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [유료 Claude 요금제의 추가 사용량 (Claude 도움말 센터)](https://support.claude.com/en/articles/12429409-extra-usage-for-max-20x-plans)
- [Claude API 가격 (Anthropic 문서)](https://platform.claude.com/docs/en/about-claude/pricing)
<!-- autoimg -->
