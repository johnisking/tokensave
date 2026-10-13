# TokenSave SEO 팀 작업 폴더

목표: **tokensave.app 검색 유입(오가닉 트래픽) 확보.** `_`로 시작하는 폴더라 GitHub Pages에 공개되지 않습니다.

| 경로 | 내용 |
|---|---|
| `audit.py` | 공개된 HTML 전체 기술 SEO 점검 (title·description·canonical·hreflang·h1·sitemap·중복·고아 페이지) |
| `analyze.py` | 서치콘솔·GA4 CSV 분석 → 기회 키워드, CTR 낮은 쿼리, 언어별·섹션별 성과 |
| `data/gsc/` | 서치콘솔 내보내기 파일 (아래 방법) |
| `data/ga4/` | GA4 보고서 CSV |
| `data/prev/` | 지난번 데이터 (기간 비교용, 같은 구조) |
| `reports/` | 날짜별 보고서 `YYYY-MM-DD-*.md` |
| `backlog.md` | SEO 팀 할 일 목록 (우선순위순) |

팀 구성과 실행 방법: `.claude/agents/seo-*.md`, 실행 명령 `/seo-report`.

## 데이터 넣는 법 (매주 1회, 5분)

### 1) Search Console
1. search.google.com/search-console → 속성 `tokensave.app` → **실적(검색 결과)**
2. 기간: **지난 28일** (비교하려면 "비교 → 이전 기간"은 쓰지 말고, 지난번 파일을 `data/prev/gsc/`로 옮겨 두기)
3. 오른쪽 위 **내보내기 → CSV 다운로드** → zip 압축 해제
4. 안의 파일(`쿼리.csv`/`Queries.csv`, `페이지.csv`/`Pages.csv`, `국가.csv`, `기기.csv`, `날짜.csv`)을 `_source/seo/data/gsc/`에 그대로 넣기 (한국어·영어 UI 둘 다 인식)
5. 선택: 쿼리×페이지 표(카니발라이제이션 분석용)는 UI에서 안 나오므로 Looker Studio나 API로 뽑아 `query_page.csv`(query,page,clicks,impressions,ctr,position)로 저장

추가로 확인할 화면(스크린샷이나 숫자만 적어줘도 됨): **색인 생성 → 페이지**의 "색인이 생성되지 않은 이유" 목록, **사이트맵** 상태, **코어 웹 바이탈**.

### 2) GA4
GTM 컨테이너 `GTM-KCGSDH87`로 들어가는 GA4 속성에서:
1. **보고서 → 수명 주기 → 획득 → 트래픽 획득** (세션 기본 채널 그룹) → 오른쪽 위 공유 아이콘 → **파일 다운로드 → CSV** → `data/ga4/traffic-acquisition.csv`
2. **참여도 → 방문 페이지(Landing page)** → CSV → `data/ga4/landing-pages.csv`
3. 선택: 같은 화면에서 측정기준을 "국가" / "언어"로 바꿔 각각 CSV
4. 선택: **참여도 → 이벤트** CSV (계산기 사용 이벤트가 있다면 전환 분석)

### 3) 실행
```bash
python3 _source/seo/audit.py   > _source/seo/reports/$(date +%F)-audit.md
python3 _source/seo/analyze.py --prev _source/seo/data/prev > _source/seo/reports/$(date +%F)-data.md
```
또는 Claude Code에서 `/seo-report` → 팀 전체가 돌고 한국어 보고서까지 작성.

### 자동 연동 (선택, 나중에)
- **GA4 → BigQuery 내보내기**를 켜면(GA4 관리 → BigQuery 링크) Claude의 BigQuery 커넥터로 직접 조회 가능. 프로젝트 ID만 알려주면 됨.
- **Search Console 대량 데이터 내보내기**(설정 → 대량 데이터 내보내기 → BigQuery)도 같은 방식.
