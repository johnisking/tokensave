---
name: seo-report
description: TokenSave SEO 팀 주간 실행. 서치콘솔·GA4 데이터 분석 + 기술 점검 + 콘텐츠/다국어/AI 검색 제안을 모아 한국어 보고서(_source/seo/reports/)와 백로그를 갱신합니다. "/seo-report", "SEO 보고서", "이번 주 SEO".
---

# /seo-report

1. `_source/seo/README.md`를 읽고 `_source/seo/data/` 상태를 확인한다. 새 서치콘솔·GA4 CSV가 없으면 사용자에게 넣는 법을 3줄로 알려 주고, 데이터 없이 진행할지 묻는다.
2. `seo-lead` 에이전트를 호출해 팀 전체를 돌린다(팀장이 5명의 팀원을 병렬 호출). 인자로 받은 초점(예: "ko만", "콘텐츠만")이 있으면 그대로 전달한다.
3. 결과 보고서 경로와 핵심 요약 3줄, 이번 주 할 일 Top 5를 사용자에게 보여 준다.
4. 사용자가 원하면 Top 5 중 코드 수정 항목을 실행한다(`_source/` 원본 수정 → `python3 _source/build.py` → `dist/` 결과를 루트로 복사 → `python3 _source/seo/audit.py`로 재확인 → 커밋).
