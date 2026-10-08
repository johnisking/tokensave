![GPT-6.1 Sol 울트라패스트 가격·속도 정리](/gpt-6-1-sol-ultrafast-gagyeok-ko.jpg)

GPT-6.1 Sol **Ultrafast**(울트라패스트)는 GPT-6.1 Sol을 훨씬 빠르게 돌리는 모드로, OpenAI가 2026년 10월 8일(미국 시간)부터 API·Codex·ChatGPT Work에 배포하기 시작했습니다. API 가격은 **100만 토큰당 입력 $12, 출력 $60**으로 일반 GPT-6.1 Sol($2 / $10)보다 500% 비싸고, GPT-6 Astra($10 / $50)보다도 20% 비쌉니다. 얼마나 빠른지, 실제 요청 하나에 얼마가 드는지, 언제 쓸 만한지 정리했습니다.

## GPT-6.1 Sol Ultrafast란

OpenAI는 Ultrafast를 Astra에 가까운 지능을 내면서, 일반 Sol보다 속도가 최대 700% 빠른 모드라고 소개했습니다. 보도(WinCentral)에서는 초당 약 300토큰이라는 수치가 나왔습니다. 모두 OpenAI 발표와 보도 기준이며, 실제 속도는 요청 길이와 시간대에 따라 다를 수 있습니다.

OpenAI는 Ultrafast를 새 모델이 아니라 GPT-6.1 Sol의 처리 모드로 소개합니다. 같은 모델을 고르고, 속도와 가격이 다른 모드를 선택하는 방식입니다.

## 가격: 일반·Fast·Ultrafast 비교

![가격: 일반·Fast·Ultrafast 비교: 모드, 입력, 캐시 입력, 출력](/gpt-6-1-sol-ultrafast-gagyeok-fastultrafast-ko.jpg)

100만 토큰당 가격입니다(OpenAI 가격 페이지 기준).

| 모드 | 입력 | 캐시 입력 | 출력 |
|---|---:|---:|---:|
| GPT-6.1 Sol 일반 | $2.00 | $0.10 | $10.00 |
| GPT-6.1 Sol Fast | $4.00 | $0.20 | $20.00 |
| **GPT-6.1 Sol Ultrafast** | **$12.00** | **$0.60** | **$60.00** |
| GPT-6 Astra (일반) | $10.00 | $1.00 | $50.00 |

- **Fast**는 일반 가격보다 100% 비쌉니다(OpenAI 모델 페이지 기준).
- **Ultrafast**는 일반보다 500% 비쌉니다. 캐시 입력도 $0.60으로 같은 비율로 올라갑니다.
- 27만 2천 토큰이 넘는 긴 입력은 요청 전체에 할증이 붙습니다. 가격표에는 Ultrafast 줄로 보이는 항목에 입력 $24, 출력 $90이 적혀 있는데, 표에 모드 이름이 따로 표시돼 있지 않아 이 부분은 추정입니다.

## 실제로 얼마나 들까

![실제로 얼마나 들까: 모드, 요청 1번, 한 달 1만 번](/gpt-6-1-sol-ultrafast-gagyeok-ko-3.jpg)

**일반 요청** 하나를 입력 2,000토큰, 출력 500토큰으로 잡았습니다(캐시 없음).

| 모드 | 요청 1번 | 한 달 1만 번 |
|---|---:|---:|
| GPT-6.1 Sol 일반 | $0.009 | $90 |
| GPT-6.1 Sol Fast | $0.018 | $180 |
| **GPT-6.1 Sol Ultrafast** | **$0.054** | **$540** |
| GPT-6 Astra | $0.045 | $450 |

**코딩 에이전트 한 단계**는 보통 앞의 대화를 다시 읽기 때문에 캐시 비중이 큽니다. 입력 5만 토큰 중 4만 5천 토큰이 캐시, 출력 1,000토큰으로 잡으면:

| 모드 | 한 단계 비용 |
|---|---:|
| GPT-6.1 Sol 일반 | $0.0245 |
| GPT-6.1 Sol Fast | $0.049 |
| **GPT-6.1 Sol Ultrafast** | **$0.147** |
| GPT-6 Astra | $0.145 |

계산: Ultrafast = 새 입력 5,000 × $12 + 캐시 45,000 × $0.60 + 출력 1,000 × $60 (모두 100만 토큰당). 에이전트 작업에서는 Ultrafast와 Astra의 비용이 거의 같아집니다(약 1% 차이). 같은 돈이면 "Astra의 지능"과 "6.1 Sol의 속도" 중 무엇이 더 필요한지가 선택 기준입니다.

## 어디서, 누가 쓸 수 있나

![어디서, 누가 쓸 수 있나: API; Codex·ChatGPT Work; 지역](/gpt-6-1-sol-ultrafast-gagyeok-ko-4.jpg)

- **API:** GPT-6.1 Sol에서 Ultrafast 모드를 고르면 됩니다. OpenAI 문서는 WebSocket 연결을 기본으로 안내하고, HTTP 방식도 제공합니다.
- **Codex·ChatGPT Work:** **Pro 500**, 사용량 기반 **Enterprise**(관리자가 직접 켜야 함), 크레딧 기반 **Edu** 요금제에서 쓸 수 있습니다. Pro 100·200과 Plus에는 없습니다.
- **지역:** 미국·EU 데이터 보관을 포함한 모든 지원 지역에서 제공됩니다.

## 장점과 단점

**장점**

- **기다림이 확 줄어듭니다.** 긴 코드나 문서를 만드는 속도가 OpenAI 발표 기준 최대 700% 빨라집니다.
- **Astra에 가까운 성능을 Astra와 비슷한 값에:** 캐시를 많이 쓰는 에이전트 작업에서는 비용이 Astra와 거의 같습니다.
- **사람이 보고 있는 작업에 맞습니다.** OpenAI는 장애 대응 디버깅, 앱을 조작하는 에이전트, 실시간 서비스를 예로 들었습니다.

**단점**

- **비쌉니다.** 일반 GPT-6.1 Sol보다 500% 비싸서, 기다려도 되는 작업에 쓰면 돈만 더 나갑니다.
- **ChatGPT에서는 Pro 500부터:** 개인이 Codex·Work에서 쓰려면 월 $500 요금제가 필요합니다.
- **속도 수치는 회사 발표 기준:** "최대" 속도라서, 실제로 얼마나 빨라지는지는 내 작업으로 직접 재 봐야 합니다.

## 언제 Ultrafast를 쓸까

- **쓰면 좋은 경우:** 사람이 화면 앞에서 결과를 기다리는 작업, 실시간 채팅·음성 서비스, 장애처럼 몇 분이 아까운 상황, 단계가 많은 에이전트를 빠르게 돌려야 할 때.
- **안 써도 되는 경우:** 밤새 돌리는 일괄 처리, 요약·분류 같은 대량 작업, 응답 속도가 크게 중요하지 않은 서비스. 이런 작업은 일반 모드나 [Batch API(영어)](/blog/batch-api-half-price)가 훨씬 쌉니다.

## 자주 묻는 질문

**GPT-6.1 Sol Ultrafast 가격은 얼마인가요?**
API 기준 100만 토큰당 입력 $12, 캐시 입력 $0.60, 출력 $60입니다. 일반 GPT-6.1 Sol보다 500% 비쌉니다.

**ChatGPT Plus나 Pro 100에서도 쓸 수 있나요?**
아니요. Codex와 ChatGPT Work에서는 Pro 500, 사용량 기반 Enterprise, 크레딧 기반 Edu 요금제에서만 쓸 수 있습니다. API는 요금제와 상관없이 쓴 만큼 냅니다.

**GPT-6 Astra와 무엇이 다른가요?**
Astra는 더 똑똑한 상위 모델이고, Ultrafast는 6.1 Sol을 빠르게 돌리는 모드입니다. 캐시를 많이 쓰는 에이전트 작업에서는 둘의 비용이 거의 같아서, 지능과 속도 중 무엇이 더 중요한지로 고르면 됩니다.

## 내 프롬프트로 계산해 보기

[토큰 계산기](/ko/)에 프롬프트를 붙여 넣으면 GPT-6.1 Sol과 30개 넘는 모델의 비용을 한 번에 볼 수 있습니다. Codex를 요금제로 쓸지 API로 쓸지는 [ChatGPT Pro 100 vs 200 vs 500 비교](/ko/blog/chatgpt-pro-yogeumje-bigyo)와 [코딩 에이전트 비용 계산기](/ko/agents)를 참고하세요.

*2026년 10월 9일 기준. 가격과 제공 범위는 자주 바뀌니 쓰기 전에 OpenAI 가격 페이지를 다시 확인하세요.*

## 출처

- [OpenAI 개발자 커뮤니티: GPT-6.1 Sol Ultrafast 배포 공지 (2026년 10월 8일)](https://community.openai.com/t/ultrafast-is-rolling-out-today-for-gpt-6-1-sol-in-the-api-codex-and-chatgpt-work/1404475)
- [OpenAI API 가격](https://developers.openai.com/api/docs/pricing)
- [OpenAI: GPT-6.1 Sol 모델 페이지](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
- [OpenAI: GPT-6 Astra 모델 페이지](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [WinCentral: GPT-6.1 Sol Ultrafast 속도 보도](https://thewincentral.com/gpt-6-1-sol-ultrafast-openai-dots-ai-agents/)
<!-- autoimg -->
