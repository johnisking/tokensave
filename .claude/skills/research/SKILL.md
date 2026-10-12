---
name: research
description: 리서칭팀을 한 번에 돌려 블로그 글 리서치 브리프를 만든다. "/research <주제> <언어>" 형태로 사용. 원고가 이미 있으면 "/research check <md 이름>"으로 팩트체크만 한다.
---

# 리서칭팀 실행

리서칭팀 구성 (`.claude/agents/`):
- `price-researcher` — 공식 가격·한도 확인
- `serp-researcher` — 검색어·상위 글·분량 중앙값·차별점
- `overlap-checker` — 기존 글 겹침·내부 링크·계산기 링크
- `fact-checker` — 다 쓴 원고 검증

## 1) 새 글 리서치: `/research <주제> <언어>`
언어가 없으면 `ko`로 한다.

1. `price-researcher`, `serp-researcher`, `overlap-checker` 세 명을 **한 메시지에서 동시에** Agent 도구로 띄운다. 각자에게 주제·언어·오늘 날짜를 넘긴다.
2. 세 결과를 모아 `_source/launchkit/briefs/<주제-슬러그>-<언어>.md`에 브리프를 쓴다:
   - 판단: 새 글 / 기존 글 보강 (overlap-checker 결과)
   - 핵심 검색어, 추천 제목, meta description, 목표 분량(상위 글 중앙값의 90% 이상)
   - 추천 H2 목차 (FAQ·출처 포함)
   - 확인된 가격 표 + 확인 날짜 + 출처
   - 우리만의 데이터·계산 아이디어 (계산기 결과, 직접 측정)
   - 내부 링크·계산기 링크
   - 미확인 항목 (글에서 빼거나 "보도 기준"으로 표시할 것)
   - `length_bench.json`에 넣을 조각
3. 사이트 가격 데이터와 다른 값이 있으면 브리프 맨 위에 따로 알린다. 사이트 파일은 고치지 않는다.
4. 사용자에게는 판단·추천 제목·브리프 경로만 짧게 알린다.

## 2) 원고 검증: `/research check <md 이름>`
`fact-checker` 한 명만 띄워 결과를 그대로 요약해 보여 준다. 원고는 사용자가 고치라고 할 때만 고친다.

## 규칙
- 게시는 하지 않는다. 체크리스트(`_source/launchkit/BLOG_CHECKLIST.md`)대로 재현의 "올려"를 받은 뒤에만 게시한다.
