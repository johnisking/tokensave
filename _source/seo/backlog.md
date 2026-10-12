# SEO 백로그 (우선순위순)

상태: `[ ]` 할 일 · `[~]` 진행 중 · `[x]` 완료. 각 팀원은 작업 후 이 파일을 갱신합니다.
근거는 `reports/2026-10-12-baseline.md` 참고.

## P0 — 데이터 확보 (이게 없으면 나머지 우선순위가 추측)
- [ ] 서치콘솔 28일 CSV를 `data/gsc/`에 넣기 (README 1번)
- [ ] GA4 트래픽 획득 + 방문 페이지 CSV를 `data/ga4/`에 넣기 (README 2번)
- [ ] 서치콘솔 "페이지 색인" 화면에서 '크롤링됨 - 현재 색인이 생성되지 않음' / '발견됨 - 현재 색인이 생성되지 않음' 개수 확인
- [ ] GA4 → BigQuery 내보내기 켜기 (이후 자동 분석)

## P1 — 지금 바로 할 수 있는 개선
- [ ] 코딩 에이전트 도구 페이지(`/xx/agents`) 41개 언어 중 40개(영어·한국어 포함) title에 제품명 없음("Coût des agents de code") → "Claude Code·Codex 월 비용 계산기"처럼 검색어(제품명) 넣기 — `src/i18n_agents_*.py`
- [ ] 메타 설명 70자 미만 49개 페이지 보강 (대부분 소수 언어 도구 페이지) — `src/i18n*.py`
- [ ] 영어 title 65자 초과(예: `blog/ai-game-cost-calculator-review` 80자, `blog/chatgpt-free-vs-paid` 75자) 줄이기 — `src/blog_meta.py`
- [ ] 일본어·중국어 블로그 title 40자 초과 다수 → 핵심 키워드를 앞 25자 안에
- [ ] 태국어 도구 페이지 본문이 얇음(150~250단어 수준) → FAQ/설명 보강 또는 우선순위 하향

## P1 — 글 구조 (근거: `reports/2026-10-12-content.md`)
- [ ] hreflang 재그룹: `gogo`·`subs`·`gemgp`·`rbxtrend`·`rbxhow` 5개 주제 39페이지가 언어끼리 연결 안 됨 — `src/blog_meta.py`, `build.py` 712~724행
- [ ] `updated` 필드 추가 → byline "Updated …"·`dateModified`·sitemap lastmod (지금은 dateModified = 발행일) — `build.py` 765행, `update_prices.py`
- [ ] 같은 검색어를 노리는 4쌍 정리: `compare/performance`↔`best-value-llm-october-2026`(en·ko·ja), Sonnet vs Opus compare↔blog, `chatgpt-plus-vs-pro`↔`chatgpt-pro-100-vs-200-vs-500`, Claude Pro/Max 3종 상호 링크

## P2 — 글 업그레이드 (2세대 형식: 첫 문장에 답·실측·표 3+·출처·질문형 H2)
- [ ] Claude Code 요금 en·ko·ja (`claude-code-cost-per-month` 877단어 / `claude-code-yogeum` / `claude-code-ryoukin`)
- [ ] 사용량 한도 3종 (Claude Code·Codex·ChatGPT) en·ko·ja
- [ ] Claude Max vs Pro en·ko·ja, LLM API 가격 비교 en·ko·ja, OpenAI API 가격, 토큰 세는 법(표 0개)
- [ ] 1세대 영어 제목에 검색어·2026 넣기, `claude-token-cost` → "Claude API Pricing 2026…"
- [ ] `/compare/` 29쌍: 수요 있는 쌍만 실측·출처 보강, 4주 노출 0인 쌍은 합치거나 noindex

## P2 — 콘텐츠 확장 (서치콘솔 데이터로 순서 재조정)
- [ ] Gemini 요금제 총정리(Google AI Plus·Pro·Ultra) + Gemini API 가격 — en·ko·ja 모두 없음
- [ ] GitHub Copilot 요금 한국어판 (en·ja만 있음)
- [ ] 영어 전용인 핵심 글 한국어판: `what-is-a-token`, `cheapest-llm-api`, `deepseek-api-pricing`, `claude-code-vs-codex-vs-cursor-cost`, `prompt-caching-explained`, `batch-api-half-price`
- [ ] 한·일에서 성과 좋은 글 → es/pt/de/fr로 확장 (사용자 많은 언어 우선)
- [ ] 새 모델 출시 당일 가격 글 + compare 페이지 (지금까지 가장 빠르게 반응하는 형식)

## P3 — 외부 유입·AI 검색
- [ ] `_source/outreach/`의 dev.to·Qiita·DOU·4programmers 원고 게시 → 백링크
- [ ] llms.txt "Key facts" 블록을 매주 가격 갱신과 같이 업데이트
- [ ] ChatGPT·Perplexity·Google AI 개요에서 "token counter", "claude code 가격" 등 질의 시 인용되는지 월 1회 확인
