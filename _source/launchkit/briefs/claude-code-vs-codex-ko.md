# 리서치 브리프: 클로드 코드 vs 코덱스 (ko)

작성 2026-10-14 · `/research` 리서칭팀 (keyword · price · overlap · serp)

> **먼저 볼 것: 사이트 데이터·기존 글 문제** (이번 글과 별개, 파일은 고치지 않았음)
> - `cc-cost-ko.md:133,166`: "/usage는 세션 비용, 잔량은 /status"라고 씀.
>   - 공식 문서(code.claude.com/docs/en/costs)와 재현 님 실제 화면 모두 **잔량은 /usage**.
>   - **틀린 내용이라 수정 필요.**
> - `agents.js:26-27`: Codex 모델이 GPT-6 Sol뿐이고 **GPT-6.1 Sol이 없음**. 글들은 6.1 Sol을 기본 추천으로 씀.
>   - 6.1 Sol을 추가할 때 캐시 요율은 5%(`CACHE_RATE_BY`).
> - `agents.js`, `token.js`, `plans.js`: **Haiku 5.5 없음** ($0.10 / $0.50, 프롬프트 10만 토큰 초과 시 $0.50 / $2.50).
> - `cxlim-ko.md:3,7`: Codex 포함 요금제를 Plus·Pro·Business로만 적음.
>   - `cxprice-ko`와 공식 요약은 **Free·Go에도 포함** (단, 클라우드 작업은 Plus부터).
> - `cursor-ko.md:147`: 영어 비교 글을 "(영어)"로 링크 중 → 새 한국어 글로 바꾸기.
> - 환율 불일치: `cc-cost-ko` 1,340원, `freepaid-ko` 1,345원.
> - **OpenAI 공식 페이지는 이 환경에서 열리지 않음.**
>   - Codex·ChatGPT 값은 공식 URL 검색 요약 기준. 게시 전 원문 대조 필요.
>   - Anthropic 값은 직접 열어 확인함.

## 판단
**새 글 + 상호 링크.**
- 한국어 "클로드 코드 vs 코덱스" 글이 없음.
- 영어 `agentcmp-en`을 현지화한다.
- **두 도구 비교에 집중**하고 커서는 짧은 한 섹션만 둔다 (`cursor-ko`로 링크).
  - "커서 vs 클로드 코드"는 따로 검색되는 다른 의도라서, 나중에 별도 글 후보.

**등록**
- `src="agentcmp-ko"`로 두면 build.py가 `agentcmp-en`과 hreflang을 자동 연결함 (언어 접미사 방식).
- 새 리스트(예: `AGCMP_KO`)를 만들어 아래에 추가한다.
  - `build.py` import와 MULTI (22행)
  - OG 매핑 (777행)
  - `autoimg.py` 36행
- 경로: `/ko/blog/claude-code-vs-codex`
- byline: `Jonhisking · 2026년 10월 14일`, `date="2026-10-14"`
- CTA: `_CTA["ko"]` 문장을 "클로드 코드·코덱스" 기준으로 고친다.

**겹침 처리**
- 같은 테스트 수치가 `cxprice-ko`(코덱스)와 `cursor-ko`(커서)에 이미 있음.
- 본문에 "같은 테스트"라고 밝히고 문장은 새로 쓴다.
- 요금·한도 상세는 기존 글로 링크한다.

## 키워드 (검색량은 모두 미확인, 난이도는 추정)
- **핵심**: `클로드 코드 vs 코덱스`
  - 한국어 상위는 브런치·커뮤니티·번역투 페이지·인프런이고 직접 테스트한 글이 없음 → **쉬움~중간**

| 보조 검색어 | 의도 | 위치 |
|---|---|---|
| 코덱스 vs 클로드 코드 / 클로드 코드 코덱스 비교 | 비교 | 첫 문단, meta |
| 클로드 코드 코덱스 차이 | 정보 | H2 "한눈에 보기" |
| 클로드 코드 코덱스 뭐가 나음 | 선택 | H2 "누구에게 맞나", FAQ |
| 코덱스 클로드 코드 가성비 | 비용 | H2 요금, FAQ |
| 클로드 코드 코덱스 같이 쓰기 | 방법 | H2 또는 FAQ |
| 코덱스 클로드 코드 벤치마크 | 정보 | H2 벤치마크 |
| codex cli vs claude code | 비교 | 본문 |

- **다른 글에 맡길 것** (링크만)
  - 클로드 코드 요금 → `cc-cost-ko`
  - 클로드 코드 한도 → `cc-limits-ko`
  - 코덱스 요금 → `cxprice-ko`
  - 코덱스 한도 → `cxlim-ko`
  - 커서 요금 → `cursor-ko`
  - 챗GPT Pro vs Claude Max → `cmp-ko`

## 제목 · 설명
- **제목**: `클로드 코드 vs 코덱스: 같은 프롬프트 실측·요금 비교`
- **meta**: `클로드 코드와 코덱스에 같은 프롬프트를 주고 직접 돌려 봤습니다. 소요 시간 37초 대 39초, 월 $20·$100·$200 요금제, 5시간·주간 한도, 독립 벤치마크까지 비교합니다.`
- 길이는 게시 전에 검사한다.

## 목표 분량
- 상위 글 미측정 (DNS 차단).
- 잠정 목표는 **공백 제외 5,500자** (허용 5,000~6,500자).
- 근거: 기존 측정값 chlim-ko 6,000, cplan-ko 3,500.

## 경쟁 글이 놓친 것 → 우리 차별점
- 같은 프롬프트로 직접 돌린 테스트가 없음. 다들 체감이나 일반론.
- 요금 구간($20 / $100 / $200 / $500)과 한도 방식을 숫자로 정리한 글이 없음.
- 확인 날짜가 불분명한 글이 섞여 있음.
- 독립 벤치마크와 작업당 비용이 없음.
- 결론이 "코덱스가 낫다"와 "클로드가 낫다"로 갈리기만 함. 우리는 용도별 선택표로 정리.
- 커뮤니티 소재를 소제목 후보로 쓸 수 있음.
  - "클로드는 맞춰 가고, 코덱스는 알아서 나간다" (체감이 갈림)
  - 한도 불만
  - 코덱스로 클로드 토큰 아끼기

## 추천 H2
1. 클로드 코드 vs 코덱스 한눈에 보기 (표: 제작사, 실행 방식, 모델, 무료 여부, 한도 방식)
2. 요금제 비교 2026 ($20 / $100 / $200 / $500. Max는 Pro 대비 500% / 2,000%. ChatGPT Pro 비율은 보도 기준)
3. 사용량은 어떻게 세나 (클로드 5시간·주간 + 앱 공유 / 코덱스 5시간·주간 + 무료 계정의 월 미터)
4. 같은 프롬프트로 직접 돌려 봤다 (벽돌깨기 표 + 재현 님 한국어 원문 평가. 모델 등급이 달라 품질 순위가 아니라는 단서)
5. 독립 벤치마크·회사 발표 수치 (Artificial Analysis는 "독립 평가", 회사 수치는 "회사 발표 기준"으로 구분)
6. 커서는 어디에 맞나 (짧게 + `cursor-ko` 링크)
7. 같이 쓰는 방법 (코덱스로 클로드 한도 아끼기)
8. 누구에게 무엇이 맞나 (용도별 표)
9. 자주 묻는 질문
10. 출처

## 확인된 수치

**Claude (2026-10-14, 직접 확인)**
- Free는 Claude Code 미포함. Pro $20 (연 $200 선결제, 월 약 $17). Max 5x $100 / 20x $200 (Pro 대비 500% / 2,000%).
- 한도: 5시간 + 주간, Max는 Fable 주간 별도, 앱·IDE와 공유. 잔량은 `/usage`.
- 공식 비용 문서: 기업 평균은 활동일당 약 $13, 월 $150~250, 사용자의 90%가 하루 $30 미만.
- API (1M 토큰): Haiku 4.5 $1 / $5, Sonnet 5.5 $2 / $10 (캐시 읽기 $0.10), Opus 5.5 $4 / $20 (캐시 읽기 $0.20), Haiku 5.5 $0.10 / $0.50.

**Codex / ChatGPT (공식 URL 검색 요약, 원문 대조 필요)**
- Free·Go·Plus·Pro·Business·Enterprise·Edu에 포함. 클라우드 작업은 Plus부터.
- 미국 가격: Go $8, Plus $20, Pro $100 / $200 / $500. 연간 결제 없음 (한국어 도움말).
- Pro는 5시간 한도 없음. Plus는 5시간 + 주간 한도가 있을 수 있음. 로컬과 클라우드가 같은 사용량을 씀.
- API (1M 토큰): GPT-6.1 Sol $2 / 캐시 $0.10 / $10, GPT-6 Sol $2 / $0.20 / $10, GPT-6 Luna $0.10 / $0.01 / $0.50, GPT-6 Astra $10 / $1 / $50.
- 원화 가격과 Codex 기본 모델: 미확인.

**우리 실측** (`agentcmp-en`, 2026-10-11)

| 도구 / 모델 | 시간 | 코드 줄 수 | 비용·사용량 |
|---|---|---|---|
| Claude Code Sonnet 5.5 medium | 37초 | 198줄 | $0.25 |
| Claude Code Sonnet 5.5 high | 58초 | 398줄 | $0.30 |
| Claude Code Opus 5.5 medium | 52초 | 358줄 | $0.56 |
| Claude Code Opus 5.5 high | 1분 50초 | 523줄 | $0.75 |
| Codex GPT-6 Luna medium | 39초 | 398줄 | 2회 합쳐 무료 월 사용량의 1% |
| Codex GPT-6 Luna extra high | 39초 | 273줄 | (위와 합산) |
| Cursor Auto (Grok 4.6) | 1분 31초 | 398줄 | 월 사용량의 15% |

**독립 평가** (Artificial Analysis, 제3자)

| 항목 | 클로드 코드 | 코덱스 |
|---|---|---|
| Coding Agent Index | 68 | 63 |
| 작업당 비용 | $14.19 | $1.04 |
| 작업 시간 | 1.5시간 | 15.5분 |
| 토큰 | 27.7M | 3.2M |

**회사 발표 기준**
- Terminal-Bench 4.0: Sonnet 5.5 70.6%, Opus 5.5 66.4%, GPT-6 Astra 57.9%.
- GPT-6.1 Sol의 Terminal-Bench 수치는 발표되지 않음 → 순위로 직접 비교하지 말 것.

## 미확인 · 보도 기준
- OpenAI 수치 전부 (원문 미열람).
- ChatGPT 원화 가격 (기존 글의 13,000 / 29,000 / 159,000원은 재확인 못 함).
- Codex 기본 모델, Codex 사용량 확인 위치.
- ChatGPT Pro의 Plus 대비 비율: 보도·X 글 기준.
- "2026년 5월 6일 클로드 5시간 한도 증가": 공식 확인 못 함.
- inflearn의 "2026년 4월 코덱스 슈퍼앱 전환·사용량 증가 요금제": 2차 요약, 대조 필요.

## 링크
- **계산기**: `/ko/agents` (코딩 에이전트 비용 계산기)
- **내부 링크**
  - `/ko/blog/claude-code-yogeum`
  - `/ko/blog/codex-yogeum`
  - `/ko/blog/claude-code-sayongnyang-hando`
  - `/ko/blog/codex-sayongnyang-hando`
  - `/ko/blog/cursor-pricing`
  - `/ko/blog/claude-sonnet-5-5-vs-opus-5-5`
  - `/ko/blog/claude-opus-5-5-effort`
  - `/ko/blog/claude-code-token-jeolyak`
- **역방향**: `cxprice-ko`, `cursor-ko`에서 새 글로 링크.

## FAQ 후보
1. 클로드 코드와 코덱스 중 뭐가 더 나은가요?
2. 둘의 차이는? (곁에서 조종 vs 맡겨 두기)
3. 코덱스가 더 싼가요?
4. 클로드 코드는 무료인가요? (아니요)
5. 코덱스는 무료인가요? (제한적으로 예, Free·Go)
6. 둘을 같이 써도 되나요?
7. 커서는 뭐가 다른가요?
8. 채팅 앱과 한도를 같이 쓰나요?

## 출처 초안
- [Claude 요금제와 가격](https://claude.com/pricing)
- [Max 요금제 안내](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- [Pro·Max로 Claude Code 사용하기](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
- [Claude API 가격](https://platform.claude.com/docs/en/about-claude/pricing)
- [Claude Code 비용 관리](https://code.claude.com/docs/en/costs)
- [Claude Sonnet 5.5 발표](https://www.anthropic.com/news/claude-sonnet-5-5)
- [Claude Opus 5.5 발표](https://www.anthropic.com/news/claude-opus-5-5)
- [Codex 요금과 한도 (OpenAI)](https://developers.openai.com/codex/pricing) (게시 전 열람 확인)
- [OpenAI API 가격](https://developers.openai.com/api/docs/pricing) (게시 전 열람 확인)
- [ChatGPT 요금제로 Codex 쓰기](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) (게시 전 열람 확인)
- [GPT-6.1 Sol 발표](https://openai.com/index/introducing-gpt-6-1-sol/) (게시 전 열람 확인)
