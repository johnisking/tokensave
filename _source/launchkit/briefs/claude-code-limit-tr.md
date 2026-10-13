# 리서치 브리프: claude code limit (tr)

작성 2026-10-13 · `/research` 리서칭팀 (keyword · price · overlap · serp)

> **먼저 볼 것**
> - **사이트 데이터**
>   - 가격 불일치는 없음. token.js, plans.js, agents.js의 Claude 가격은 공식과 같음.
>   - 누락 하나: `token.js`에 **Haiku 5.5가 없음** (2026-10-07 출시, 입력 $0.10 / 출력 $0.50, 프롬프트 10만 토큰 초과 시 $0.50 / $2.50). `llm_prices.json:217`에 검토 대기로만 올라 있음.
> - **기존 영어 원문(`cc-limits-en`) 점검**
>   - 5시간 창 시작 시점과 "2025년 8월 도입" 문장은 공식 문서로 확인하지 못함.
>   - 2026년 한도 변경 날짜(5/6, 9/14)도 공식 문서로 확인하지 못함.
>   - 지원 문서 링크 슬러그 두 개가 오래됐을 수 있음 (`:72`, `:76`, `:78`).
> - **이 환경의 한계**
>   - 경쟁 글 본문, google.com.tr 실제 순위, 앱스토어 TL 가격 페이지가 모두 열리지 않았음.
>   - 그래서 분량 중앙값, 검색량, TL 공식가는 **미확인**.

## 판단
**새 글 하나**로 쓴다.
- 핵심은 한도(limit), 가격은 보조.
- 터키어 Claude Code 글은 아직 없음.
- 뼈대는 `cc-limits-en`. 가격 부분은 `cc-cost-en`의 "What a month costs"와 "How to decide"를 붙인다.

**등록**
- 메타 위치: `blog_meta.py`의 `CC_LIMITS` 그룹 (nl 항목 아래)
  - `tag="tr"`, `path="/tr/blog/claude-code-limit"`, `src="cc-limits-tr"`, `date="2026-10-13"`
  - byline 형식: `"Jonhisking · 13 Ekim 2026"`
- CTA 버튼은 build.py가 `/tr/agents`로 자동 연결한다. hreflang도 자동.

**겹침 방지**
- `subs-tr`가 Claude Pro·Max 가격과 KDV를 이미 다룸.
- 이 글은 가격을 요약 표로만 쓰고, 일반 구독 비교는 `subs-tr`로 링크한다.
- `subs-tr`에도 이 글로 가는 링크를 한 줄 추가한다.

## 키워드 (검색량은 모두 미확인, 난이도는 추정)
- **핵심**: `claude code limit` (변형: limiti / limitleri / kullanım limiti)
  - 터키어 상위는 번역·자동 생성 글(DataCamp tr, Apidog, Verdent, SSD Nodes, pasqualepillitteri.it)
  - 터키 현지 매체는 안 보였음 → 난이도 **낮음~중간**

| 보조 검색어 | 뜻 | 의도 | 위치 |
|---|---|---|---|
| claude code 5 saatlik limit | 5시간 한도 | 정보 | H2 |
| claude code haftalık limit | 주간 한도 | 정보 | H2 |
| claude code limit doldu / limite takıldım | 한도 소진 | 방법 | H2, SSS |
| claude code limit ne zaman sıfırlanır | 언제 초기화 | 정보 | SSS |
| claude code fiyatı / kaç TL | 가격 | 정보 | 가격 H2(표) |
| claude code pro mu max mı | Pro냐 Max냐 | 비교 | H2 |
| claude code ücretsiz mi | 무료인가 | 정보 | SSS |
| claude code api mi abonelik mi | API냐 구독이냐 | 비교 | H2 (+ /tr/agents, /tr/plans) |

- **다른 글에 맡길 것**
  - yapay zeka abonelik fiyatları, claude pro fiyatı TL 일반 → `subs-tr`
  - effort → `effort-tr`
  - türkçe token → `tr.md`

## 제목 · 설명 (게시 전 길이 재검사)
- **제목**: `Claude Code Limiti: 5 Saatlik ve Haftalık Limit Rehberi 2026`
- **meta**: `Claude Code limiti nasıl çalışır? 5 saatlik pencere, haftalık limit, Pro 20$ ve Max 100$/200$ planları, /status ile kontrol ve limit dolunca çözümler.`

## 목표 분량
- 미측정. 경쟁 글을 하나도 열지 못했음.
- 임시 목표는 2,000단어 이상. `length_bench.json`에는 측정 후 넣는다.

## 경쟁 글이 놓친 것 (검색 요약 기준)
- TL 가격이 없음. 다들 USD 그대로.
- 2026년 한도 변경 날짜가 글마다 흩어져 있고 서로 어긋남.
- 공식 한도 숫자가 없다는 점을 밝힌 글이 드묾. 대신 예전 숫자(예: 5시간당 45개)를 단정함.
- 계산기, 공유 한도의 실제 예, 한도 소진 시 대처법이 거의 없음.

**차별점**: 공식 문서 기준으로 정리한 Claude Code 한도 글
- 5시간·주간 한도와 Max의 Fable 주간 한도
- 앱과 공유하는 한도, `/status`로 확인
- Pro·Max 가격(USD + 보도 기준 TL), API 비교 계산기

## 추천 H2 (터키어)
1. Claude Code limiti nedir? 5 saatlik pencere ve haftalık limit
2. Planlara göre kullanım ve fiyat: Pro, Max 5x, Max 20x (USD + yaklaşık TL)
3. 2026'da limitlerde neler değişti? (공식 확인된 것만, 날짜 미확인은 "haberlere göre")
4. Limitinizi nasıl kontrol edersiniz? (`/status`)
5. Limit dolduğunda ne yapmalı? (bekle / kullanım kredisi / Max'e geç / API)
6. Limit neden hızlı doluyor? (uygulama ile ortak havuz, Opus vs Sonnet, uzun bağlam, Türkçe token)
7. Limiti uzatmanın yolları (cc-save 요약 + 링크)
8. Abonelik mi, API mi? (/tr/agents, /tr/plans)
9. Sık Sorulan Sorular
10. Kaynaklar

## 확인된 사실 (2026-10-13, 공식)

| 항목 | 값 | 출처 |
|---|---|---|
| Free | Claude Code **미포함** | claude.com/pricing |
| Pro | 월 $20, 연 결제 시 월 $17 ($200) | claude.com/pricing |
| Max 5x / 20x | 월 $100 / $200 (월 결제만, 사용량은 Pro 대비 500% / 2000%) | support.claude.com 11049741 |
| 한도 종류 | 5시간 세션 + 주간. Max는 별도 Fable 주간 한도 | support.claude.com 11145838 |
| 앱과 공유 | Claude Code·Claude 앱·IDE가 같은 한도를 씀 | 같은 문서 |
| 한도 초과 | 사용 크레딧을 켜면 계속 사용 가능 (Pro, Max) | 같은 문서 |
| 잔여 확인 | `/status` (제3자 글은 `/usage`라고 함, 공식은 /status) | 같은 문서 |
| 한도 숫자 | 공식 숫자 없음, Pro 대비 비율만 공개 | 같은 문서 |
| 모바일 가격 | "web 가격이며 앱 가격은 다를 수 있음" | support.claude.com 11049741 |

| API (1M 토큰) | 입력 | 출력 | 캐시 읽기 |
|---|---|---|---|
| Haiku 4.5 | $1 | $5 | $0.10 |
| Sonnet 5.5 | $2 | $10 | $0.10 |
| Opus 5.5 | $4 | $20 | $0.20 |
| Haiku 5.5 (≤10만 / >10만) | $0.10 / $0.50 | $0.50 / $2.50 | $0.01 / $0.05 |

출처: platform.claude.com/docs/en/about-claude/pricing
- Haiku 5.5를 Claude Code에서 쓸 수 있는지는 미확인.

## 미확인 · "haberlere göre"로 표시할 것
- **앱스토어 TL 가격** (Webtekno 보도): Pro 999,99 TL, Max 5x 6.999,99 TL, Max 20x 12.999,99 TL. 기사 날짜도 미확인.
  - 본문에 보도로 인용하고, Kaynaklar 목록에는 넣지 않는다.
- **웹 결제 통화(USD)와 KDV 20% 추가 여부**: 공식 문서는 "청구 주소 기준 세금"이라고만 함.
  - `subs-tr`와 같은 표기·환율(1 USD ≈ 49 TL)로 맞춘다.
- **2026년 한도 변경 날짜**: 5/6 증가, 8월 연장, 9월 soft stop, 9/14 주간 25% 상향은 모두 제3자 보도. 공식 확인 전에는 "haberlere göre"로 표시하거나 뺀다.
- **Max의 월 API 크레딧 금액**: 미확인. 다만 공식 문서는 이 크레딧을 Claude Code나 앱에서 쓸 수 없다고 명시함.

## 링크
- **계산기**: `/tr/agents` (앵커: "Kodlama ajanı maliyet hesaplayıcısını aç")
- **내부 링크**
  - `/tr/blog/yapay-zeka-abonelik-fiyatlari`: "Türkiye'de yapay zeka abonelik fiyatları"
  - `/tr/blog/token-turkce-gpt`: "Türkçe metinler neden daha fazla token harcar"
  - `/tr/blog/claude-opus-5-5-effort`: "Opus 5.5 effort seviyeleri"
  - `/tr/plans`: "abonelik mi API mi hesaplayıcısı"

## SSS 후보
1. Claude Code ücretsiz mi? (아니다. Free 플랜에 없음)
2. 5 saatlik limit nedir, ne zaman sıfırlanır?
3. Haftalık limit ne zaman sıfırlanır?
4. Limite takılınca ne yapmalıyım?
5. Claude Code ve Claude uygulaması aynı limiti mi kullanıyor? (그렇다)
6. Pro mu Max mı almalıyım?
7. Türkiye'de Claude Pro kaç TL? (보도 기준 + USD, KDV 표시)
8. /clear limiti sıfırlar mı? (아니다. 제3자 기준이므로 공식 확인 후 사용)

## 출처 초안 (Kaynaklar)
- [Claude planları ve fiyatlandırma](https://claude.com/pricing)
- [Max planı nedir?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- [Claude Code'u Pro veya Max planıyla kullanma](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
- [Claude API fiyatlandırması](https://platform.claude.com/docs/en/about-claude/pricing)
- [Claude Haiku 5.5](https://anthropic.com/claude-haiku-5-5)
- [Faturalandırma ve vergi](https://support.claude.com/en/articles/12997130)
