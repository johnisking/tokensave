# SEO 백로그 (우선순위순)

상태: `[ ]` 할 일 · `[~]` 진행 중/일부 완료 · `[x]` 완료. 각 팀원은 작업 후 이 파일을 갱신합니다.
근거: `reports/2026-10-12-baseline.md`(공개), 실제 검색·분석 숫자는 `private/2026-10-15-report.md`(로컬 전용, 저장소에 올리지 않음).
이 파일은 공개 저장소에 있으므로 트래픽 숫자·검색어 원문·유입 사이트 성과는 적지 않습니다.

## P0 — 데이터 확보
- [x] 서치콘솔 CSV를 `data/gsc/`에 넣기 (2026-10-15, 첫 기준선)
- [x] GA4 트래픽 획득·페이지·이벤트 CSV를 `data/ga4/`에 넣기 (2026-10-15)
- [x] 이번 데이터를 `data/prev/2026-10-12/`에 기준선으로 복사 (2026-10-15) → 다음 내보내기는 **사용자 지정 기간 10/13~**
- [ ] 서치콘솔 "페이지 색인" 화면에서 '크롤링됨/발견됨 - 현재 색인이 생성되지 않음' 개수 확인
- [ ] 서치콘솔 국가 필터 → 페이지 탭 CSV (클릭 없는 상위 노출 국가가 어느 페이지에 걸리는지)
- [ ] 검색어×페이지 표 `query_page.csv` (README 1번 5항)
- [ ] GA4 방문 페이지 CSV(`landing-pages.csv`, 오가닉 필터) — 지금 받은 `pages.csv`는 모든 채널 페이지뷰
- [ ] GA4 Direct 유입 정체 확인(내부 트래픽 필터) — 원인 불명이므로 판단 근거로 쓰지 않음
- [ ] Bing 웹마스터 도구 검색 실적 내보내기
- [ ] GA4 → BigQuery 내보내기 켜기 (이후 자동 분석)

## P1 — 이번 주 (2026-10-15 보고서 Top 5, 효과 × 쉬움 순)
- [ ] **1. 순위 대비 클릭이 적은 페이지 제목 테스트**: `gemini-4-argon-api-pricing` title·description에 가격 숫자 넣기 — `src/blog_meta.py` (GEM4 en). `gpt-6-1-sol-ultrafast-pricing`은 표본 검정 미통과라 관찰만. Gemini 4 Argon 본문의 "아직 사용 불가"(10/03 기준) 상태부터 재확인. 10/11~12 발행 API 가격 글(deepseek·grok·claude-pro-price·claude-token-cost)은 손대지 않고 관찰
- [ ] **2. 한국어 Claude API 가격·결제 글 신규**: 토큰 단가 + 원화 + 결제(크레딧·카드·부가세) — 신규 `blog_src/ctc-ko.md`, `src/blog_meta.py` `CTC.append(_cc("ko", …))`로 ctc-en과 hreflang 연결. `cplan-ko`(구독)·`api-ko`(22개 모델)와 역할 분리 + 상호 링크
- [ ] **3. GPT-6 API 허브 보강**: `blog_src/gpt6-en.md`를 2세대 형식으로(첫 문장 답·표 3+·가장 싼 GPT-6 API 섹션·FAQ·출처), `updated` 갱신. Ultrafast 글·GPT-6 비교 페이지에서 허브로 링크 — `blog_src/ultrafast-en.md`, `src/compare.py`(`IN_DEPTH`처럼 허브 링크). 제목 재변경은 선택
- [ ] **4. Claude Haiku 5.5 비교 페이지**: `src/compare.py` `PAIRS`에 GPT-6 Luna vs Haiku 5.5, Haiku 4.5 vs 5.5 추가, 4.5 페이지 상단에 5.5 링크. 필요 시 `src/perf.py` `ECI_MAP`, `build.py` 차트 목록
- [ ] **5. 코딩 에이전트 도구 페이지(`/xx/agents`) title에 "Claude Code·Codex" 넣기** — en·ko·ja 먼저, 수식어는 "계산기/calculator"(Claude Code 요금 글과 겹치지 않게) — `src/i18n_agents_*.py`

## P1 — 관찰만 (손대지 않음)
- [ ] `blog/chatgpt-usage-limits`: 이미 재작성·제목 변경됨. 다음 보고서에서 이 페이지 포함/제외 지표를 함께 표시
- [ ] 10/12 재작성한 Claude Code 요금 en·ko·ja, Claude Code 사용량 한도 en: 10/13~ 데이터로 기준선 대비 순위 확인
- [ ] 10/11~12 발행 API 가격 글 4개: 노출이 충분히 쌓인 뒤 CTR 판단

## P1 — 기존 개선 (데이터 우선순위 낮음)
- [ ] 메타 설명 70자 미만 49개 페이지 보강 (대부분 소수 언어 도구 페이지) — `src/i18n*.py`
- [ ] 영어 title 65자 초과(예: `blog/ai-game-cost-calculator-review`, `blog/chatgpt-free-vs-paid`) 줄이기 — `src/blog_meta.py`
- [ ] 일본어·중국어 블로그 title 40자 초과 다수 → 핵심 키워드를 앞 25자 안에
- [ ] 태국어 도구 페이지 본문이 얇음 → FAQ/설명 보강 또는 우선순위 하향

## P1 — 글 구조 (근거: `reports/2026-10-12-content.md`)
- [x] hreflang 재그룹 (2026-10-12, `build.py` `alternates()`)
- [x] `updated` 필드 추가 (2026-10-12) → byline "Updated …"·`dateModified`·sitemap lastmod
- [x] 같은 검색어를 노리는 4쌍 정리 (2026-10-12)

## P2 — 글 업그레이드 (2세대 형식: 첫 문장에 답·실측·표 3+·출처·질문형 H2)
- [x] Claude Code 요금 en·ko·ja (2026-10-12 재작성)
- [~] 사용량 한도 3종 en·ko·ja — ChatGPT en·ko·ja 완료(10/13), Claude Code·Codex 남음
- [ ] Claude Max vs Pro en·ko·ja, LLM API 가격 비교 en·ko·ja, 토큰 세는 법(표 0개). OpenAI/GPT-6 API 가격은 P1 #3으로 이동
- [ ] 1세대 영어 제목에 검색어·2026 넣기. `claude-token-cost` 제목 변경은 관찰 결과를 보고 판단
- [ ] `/compare/` 29쌍: 수요 있는 쌍만 실측·출처 보강, 4주 노출 0인 쌍은 합치거나 noindex (판단 시점: 11월 둘째 주)

## P2 — 후속
- [~] Claude Haiku 5.5 반영 — 토큰 카운터·/plans 완료(10/14). `/compare/`(P1 #4), `src/variants.py` Claude 토큰 카운터 설명, `/agents` 남음
- [ ] 게임 계산기 외 도구(토큰 카운터·/plans·/agents·/video·/image)에도 GA4 이벤트 추가 — 지금은 `gamecost.js`만 이벤트를 보내 도구별 비교 불가 (코드 작업, 사용자 요청 시)
- [ ] 굵은 글씨 FAQ(**질문?** 다음 줄 답)도 FAQPage 구조화 데이터로 뽑기 (`build.py` `_qa`)
- [ ] 경쟁 글 분량 측정(`launchkit/length_bench.json`)에 Claude Code 요금 주제 추가

## P2 — 콘텐츠·다국어 확장 (서치콘솔 데이터로 순서 재조정)
- [ ] 스페인어·터키어 ChatGPT 사용량 한도 글 (es는 Codex·Claude Code 한도 글, tr은 Claude Code 한도 글만 있고 ChatGPT 편이 없음)
- [ ] 포르투갈어 사용량 한도 글 — 국가 필터 데이터 확인 후 결정
- [ ] Gemini 요금제 총정리(Google AI Plus·Pro·Ultra) + Gemini API 가격
- [ ] GitHub Copilot 요금 한국어판 (en·ja만 있음)
- [~] 영어 전용인 핵심 글 한국어판: `what-is-a-token`, `cheapest-llm-api`, `deepseek-api-pricing`, `prompt-caching-explained`, `batch-api-half-price` — 코딩 에이전트 비교는 ko `claude-code-vs-codex`(10/14)가 일부 대신함. Claude API 단가는 P1 #2
- [ ] 한·일에서 성과 좋은 글 → es/pt/de/fr로 확장 (사용자 많은 언어 우선)
- [ ] 새 모델 출시·가격 변경 당일 가격 글 + compare 페이지 (첫 데이터에서도 새 가격 글이 빠르게 노출됨)

## P3 — 외부 유입·AI 검색
- [ ] `_source/outreach/`의 미게시 원고 게시 계속 (게임 계산기는 게임 개발 커뮤니티 우선) → 백링크
- [ ] llms.txt "Key facts"에 가격 사실(Claude API 단가, GPT-6 API 단가, Claude Code 요금제, ChatGPT 한도) + 출처 URL 추가, 매주 가격 갱신과 같이 업데이트
- [ ] ChatGPT·Perplexity·Google AI 개요에서 "token counter", "claude code 가격" 등 질의 시 인용되는지 월 1회 확인
