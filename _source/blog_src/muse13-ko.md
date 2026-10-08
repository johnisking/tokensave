![메타 Muse Spark 1.3 API 가격: Claude·GPT-6·Gemini와 비용 비교](/muse-spark-1-3-api-gagyeok-ko.jpg)

메타(Meta)의 Muse Spark 1.3 API 가격은 **입력 100만 토큰당 $1.25, 출력 $4.25**입니다. 캐시 입력은 $0.15이고, 100만 토큰 컨텍스트를 꽉 채워도 추가 요금이 없습니다. 메타가 데이터를 학습에 쓰는 대신 훨씬 싼 "기여자(contributor)" 버전도 있습니다. Claude Sonnet 5.5, GPT-6 Sol, Gemini 3.1 Pro, DeepSeek, Grok과 비교해 실제로 얼마인지 정리했습니다.

## Muse Spark 1.3 API 가격

![Muse Spark 1.3 API 가격: 모델 이름, 입력, 캐시 입력, 출력](/muse-spark-1-3-api-gagyeok-muse-spark-1-3-api-ko.jpg)

메타 공식 가격 페이지 기준, 100만 토큰당 가격입니다.

| 모델 이름 | 입력 | 캐시 입력 | 출력 |
|---|---:|---:|---:|
| `muse-spark-1.3` (일반) | $1.25 | $0.15 | $4.25 |
| `muse-spark-1.3-contributor` (기여자) | $0.10 | $0.002 | $0.20 |

- **1.1·1.2·1.3 가격이 같습니다.** 일반 버전은 같은 가격이라 최신으로 올려도 비용이 늘지 않습니다.
- **긴 컨텍스트 할증 없음:** 100만 토큰 창이 거의 비어 있든 꽉 차 있든 같은 요금입니다.
- **기여자 버전:** 내 프롬프트와 답변이 메타의 다음 모델 학습에 쓰입니다. 싸지만 개인정보나 고객 데이터는 넣지 마세요.
- **사용 한도(일반):** 팀당 분당 요청 3,000회, 분당 토큰 400만 개입니다.

## 다른 모델과 가격 비교

![다른 모델과 가격 비교: 모델, 입력, 출력](/muse-spark-1-3-api-gagyeok-ko-3.jpg)

100만 토큰당 정가입니다.

| 모델 | 입력 | 출력 |
|---|---:|---:|
| **Muse Spark 1.3** | $1.25 | $4.25 |
| DeepSeek V4 Pro | $1.32 | $3.96 |
| Grok 4.7 | $2.00 | $6.00 |
| GPT-6 Sol | $2.00 | $10.00 |
| Claude Sonnet 5.5 | $2.00 | $10.00 |
| Gemini 3.1 Pro | $2.00 | $12.00 |

## 실제 작업 비용

일반적인 요청 하나를 입력 2,000 토큰, 출력 500 토큰으로 잡았습니다. 같은 영어 문장에서 모델마다 토큰 수가 다른 점도 반영했습니다. Claude는 약 30% 더 나오고, 메타의 토크나이저는 공개되지 않아 GPT와 같다고 가정했습니다.

| 작업 | Muse Spark 1.3 | Claude Sonnet 5.5 | GPT-6 Sol | Gemini 3.1 Pro | DeepSeek V4 Pro | Grok 4.7 |
|---|---:|---:|---:|---:|---:|---:|
| 요청 1번 | $0.0046 | $0.0117 | $0.0090 | $0.0095 | $0.0046 | $0.0070 |
| 한 달 1만 번 | $46 | $117 | $90 | $95 | $46 | $70 |

- 같은 요청에서 Claude Sonnet 5.5는 Muse Spark 1.3보다 **153% 더**, GPT-6 Sol은 **95% 더**, Gemini 3.1 Pro는 **105% 더** 듭니다.
- DeepSeek V4 Pro는 거의 같고, Grok 4.7은 **51% 더** 듭니다.

## 메타가 밝힌 강점

메타에 따르면 Muse Spark 1.3은 여러 단계를 이어 가는 에이전트 작업에 맞춰 학습했고, 코딩에서 "불필요한 턴이 적고 결과가 깔끔하다"고 합니다. 이미지·영상·문서도 바로 읽는다고 밝혔습니다. 모두 메타의 주장이니, 바꾸기 전에 내 작업으로 직접 테스트해 보세요.

## 장점과 단점

![Muse Spark 1.3 장단점: 싼 가격, 100만 토큰, 코딩 개선 vs 긴 출력, 에이전트 작업은 Claude Opus 5가 근소하게 앞섬](/muse-spark-1-3-pros-cons-ko.jpg)

**장점**

- **가격:** 100만 토큰당 $1.25 / $4.25로 Claude Sonnet 5.5, GPT-6 Sol보다 쌉니다.
- **긴 문서:** 100만 토큰을 할증 없이 씁니다. 메타의 긴 문서 기억력 테스트(MRCR, 51만~100만 토큰)에서 98.1점으로 GPT-5.6 Sol(73.8)보다 높습니다.
- **코딩:** 메타 발표 기준 DeepSWE v1.1 75.4점(1.2는 55.0), Terminal-Bench 2.1 88.8점으로 GPT-5.6 Sol과 같습니다. 메타 엔지니어 비교로는 1.2보다 도구 호출이 약 20%, 토큰이 약 25% 줄었습니다.
- **독립 평가 순위:** 최고 설정(max) 기준 Artificial Analysis 지수 62점, 636개 모델 중 6위입니다.

**단점**

- **말이 많음:** Artificial Analysis 측정에서 출력 토큰을 1억 2천만 개 썼습니다. 다른 모델 중간값은 7천 2백만 개라 **약 67% 더 많습니다.** 토큰 단가는 싸도 실제 청구액은 더 나올 수 있으니 내 프롬프트로 직접 재 보세요.
- **에이전트 작업은 1등이 아님:** 메타 자체 표에서도 OSWorld 2.0 같은 에이전트 벤치마크는 Claude Opus 5가 근소하게 앞서고(68.3 vs 66.9), 검색·지시 따르기는 GPT-5.6 Sol이 앞섭니다.
- **최고 모드는 나중에:** 6위 점수를 낸 max 모드는 안전성 테스트로 출시 때 빠졌고, 일반 공개된 xhigh는 61점입니다.
- **생각 과정이 안 보임:** 추론 과정을 보여 주지 않아 디버깅이 불편하다는 사용자 의견이 있습니다.
- **폐쇄형, 제공처 한 곳:** 오픈 가중치가 아니고 메타에서만 쓸 수 있습니다.

## 갈아탈 만할까

![갈아탈 만할까: 비용 때문에 Claude Sonnet 5.5·GPT-6 Sol·Gemini 3.1 Pro를 쓰는 중이라면; DeepSeek V4 Pro를 쓰는 중이라면; 민감하지 않은 대량 작업](/muse-spark-1-3-api-gagyeok-ko-4.jpg)

- **비용 때문에 Claude Sonnet 5.5·GPT-6 Sol·Gemini 3.1 Pro를 쓰는 중이라면:** 요청당 훨씬 쌉니다. 실제 프롬프트로 작게 테스트해서 품질을 비교해 보세요.
- **DeepSeek V4 Pro를 쓰는 중이라면:** 가격이 거의 같아서 품질, 속도, 데이터 처리 위치로 고르면 됩니다.
- **민감하지 않은 대량 작업:** 기여자 버전($0.10 / $0.20)은 가장 싼 선택지 중 하나입니다. 메타가 그 데이터를 학습해도 괜찮을 때만 쓰세요.
- **커서(Cursor)에서 쓴다면:** 커서도 Muse Spark 1.3을 같은 $1.25 / $4.25로 "다른 모델" 사용량에서 차감합니다.

## 내 프롬프트로 계산해 보기

내 프롬프트를 [토큰 계산기](/ko/)에 붙여 넣으면 Muse Spark 1.3과 30개 넘는 모델의 비용을 한 번에 볼 수 있습니다. [Muse Spark 1.3 vs Claude Sonnet 5.5](/compare/muse-spark-1-3-vs-claude-sonnet-5-5) 비교 페이지(영어)도 있습니다.

*2026년 10월 9일 가격 기준. 쓰기 전에 메타 가격 페이지를 한 번 더 확인하세요.*

## 출처

- [Meta Model API: 가격과 사용 한도](https://dev.meta.ai/docs/pricing-rate-limits)
- [Meta Model API: Muse Spark 1.3](https://dev.meta.ai/models/muse-spark)
- [Cursor: 모델 가격](https://cursor.com/docs/models-and-pricing)
- [Artificial Analysis 수치 인용: eesel 리뷰](https://www.eesel.ai/blog/meta-muse-spark-13-review)
- [DataCamp: Muse Spark 1.3](https://www.datacamp.com/blog/muse-spark-1-3)
<!-- autoimg -->
