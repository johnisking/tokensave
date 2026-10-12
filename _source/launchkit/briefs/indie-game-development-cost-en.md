# 리서치 브리프: indie game development cost (en)

작성 2026-10-12 · `/research` 리서칭팀 (keyword · price · overlap · serp)

> **먼저 볼 것**
> - **사이트 데이터와 다른 값** (사이트 파일은 고치지 않았음)
>   - `gamecost.js:115` Google AI Pro $20 → 공식 $19.99. 반올림 차이.
>   - `gamecost.js:113` Max 20× $200 → 가격 페이지에 금액이 명시돼 있지 않음.
>   - `indiecost-ko.md:28,48` Unity Personal "20만 달러 미만" → 공식은 "up to $200,000"(이하).
>   - `indiecost-ko.md:30,42` Unreal 5% → 정확히는 "제품별 평생 총매출 $1M 초과분". EGS 결제분 면제와 3.5% 프로그램 언급이 빠져 있음.
> - **이 환경의 한계**
>   - 경쟁 글 본문, 키워드 도구, 자동완성이 모두 막혔음.
>   - 그래서 상위 글 분량, 검색량, H2 구조는 **미측정**. 체크리스트 5번(분량 목표)은 열리는 환경에서 다시 재야 함.
>   - 가격 대부분은 공식 도메인으로 한정한 검색 요약에서 가져왔음. 원문을 직접 연 것은 Apple, Claude, GitHub뿐.

## 판단
**새 글 + 상호 링크.**
- 영어로 된 인디 개발 비용 전체(엔진·스토어·외주 vs 직접) 글은 없음.
- `indiecost-ko`의 영어 쌍(hreflang)으로 만든다.

**`game-en`과의 경계**
- `game-en`이 계속 맡는 말: "how much does it cost to make a game with AI", AI 도구 스택별 비용
- 이 글이 맡는 말: indie, solo, 엔진·스토어 등록비, 외주 vs 직접
- AI 비용은 한 단락 요약만 쓰고, 상세는 `game-en`과 계산기로 링크한다.

## 키워드
- **핵심 검색어**: indie game development cost
  - 상위 글 제목에 그대로 쓰임.
  - "indie"가 들어가 `game-en`과 의도가 갈림.
- **보조 검색어** (검색량은 모두 미확인)

| 검색어 | 의도 | 넣을 위치 |
|---|---|---|
| how much does it cost to make an indie game | 정보 | 첫 문단, 첫 H2 |
| solo indie game development cost / how much does it cost to make a game by yourself | 정보 | 본문, FAQ |
| indie game budget / cost breakdown | 정보·계획 | 비용 4분류 표 |
| Unity vs Godot vs Unreal cost / is Godot free | 비교 | 엔진 H2, FAQ |
| cost to publish a game on Steam / Steam Direct fee | 절차 | 출시 비용 H2, FAQ |
| hidden costs of indie game development | 정보 | 숨은 비용 H2 |
| indie game outsourcing cost vs solo | 비교 | 외주 vs AI H2 |

## 제목 · 설명
- **제목** (63자): `Indie Game Development Cost: Solo Dev Budget, Fees, Real $45 Case`
  - 대안 (56자): `Indie Game Development Cost: What a Solo Dev Really Pays`
- **meta description** (약 150자):
  `Indie game development cost for solo devs: engines from $0, store fees ($25 Google Play, $100 Steam, $99/yr Apple), outsourcing vs AI, and a real $45 game.`
- **$45의 근거**: `devlog-spermrace-1-en.md:85`, `gamecalc-review-en.md:22`. Claude Pro $20 + Google Play $25.

## 목표 분량
- **미확정**. 상위 글 실측에 실패했음.
- 임시 목표는 2,000단어 이상. 기존 영어 글 기준값이 1,650~2,150이고, 한국어 원문 구조를 따르면 2,000단어대가 됨.
- 측정되면 아래 조각을 채워 `length_bench.json`에 넣는다.

```json
"indiecost-en": {
  "keyword": "indie game development cost",
  "checked": "2026-10-12",
  "median": null,
  "samples": {"blog.prolificstudio.co": null, "juegostudio.com": null, "gamemaker.io": null, "pixune.com": null, "ilogos.biz": null}
}
```

## 경쟁 글 (본문은 못 열었음, 검색 스니펫 기준)
- **상위 글 구성**: 거의 다 외주 개발사 블로그
  - prolificstudio, juegostudio, pixune, ilogos, ediiie, gamemaker.io
- **놓친 것**
  - 견적이 $10K~$1M이라 1인 개발자에게는 쓸모가 없음.
  - 엔진 무료 조건, 스토어 등록비를 한 표로 모은 글이 드묾.
  - "외주 vs AI로 혼자" 비교, 계산기, 실제 영수증이 없음.
- **차별점**: 견적서가 아니라 영수증으로 말하는 인디 비용 글
  - 엔진 $0, 등록비 표, 외주 vs AI 비교, 실제 출시작 $45 내역 + 계산기

## 추천 H2 목차
1. What indie game development costs: the four buckets (engine, art & audio, code, release)
2. Engine costs: Unity, Godot, Unreal are free to start (with the exact limits)
3. Release fees: Google Play $25, Steam $100, Apple $99/year (+ store revenue shares)
4. Outsourcing vs building it yourself with AI (계산기 + `game-en` 링크, AI 구독표 중복 금지)
5. Real case: our released game for $45
6. Hidden costs people forget (time, testing, devices, marketing, taxes)
7. How to cut costs without cutting quality
8. FAQ
9. Sources

## 확인된 가격 (2026-10-12)
표시 기준: ◎ 원문 직접 확인 / ○ 공식 도메인 검색 요약 (게시 전 원문 재확인)

| 항목 | 값 | 출처 | 확인 |
|---|---|---|---|
| Unity Personal | 무료, 매출·투자금 연 $200,000 이하 | unity.com/products/pricing-updates | ○ |
| Unity Pro | 연 $2,310 / 월 $210 (1인당) | unity.com/products | ○ |
| Unity 런타임 수수료 | 2024-09 취소 | unity.com/blog/unity-is-canceling-the-runtime-fee | ○ |
| Unreal | 제품별 평생 총매출 $1M 초과분 5%. EGS 결제분 제외, 조건 충족 시 3.5% | unrealengine.com/en-US/faq | ○ |
| Godot | 무료 (MIT) | godotengine.org/license | ○ |
| GameMaker | Free(비상업), Professional 1회 $99.99, Enterprise 연 $799.99 | gamemaker.io | ○ |
| Steam Direct | 앱당 $100. 해당 앱 매출 $1,000 이후 정산금에서 회수 | partner.steamgames.com/doc/gettingstarted/appfee | ○ |
| Google Play | 1회 $25 | support.google.com/googleplay/android-developer/answer/6112435 | ○ |
| Apple Developer Program | 연 $99 | developer.apple.com/programs | ◎ |
| itch.io | 기본 10% (판매자 조정 가능) + 결제 수수료 | itch.io/docs/creators/payments | ○ |
| Epic Games Store | 88/12. 제품당 연 첫 $1M은 100% 지급 | store.epicgames.com 뉴스 | ○ |
| Claude Pro | 월 $20 (연 결제 시 월 $17) | claude.com/pricing | ◎ |
| GitHub Copilot | Pro 월 $10, Pro+ 월 $39 | github.com/features/copilot/plans | ◎ |
| Cursor Pro | 월 $20 | cursor.com | ○ |
| Midjourney | 월 $10 / $30 / $60 / $120 | docs.midjourney.com | ○ |
| Suno | Pro 월 $10, Premier 월 $30 | suno.com/pricing | ○ |
| ElevenLabs | 월 $6 / $22 / $99 | elevenlabs.io/pricing | ○ |

## 우리만의 데이터·계산
- **실제 출시작 $45**: 첫 버전 3일, Google Play 출시까지 약 14일
  - 근거: devlog-spermrace-1, gamecalc-review
- **계산기 예측 vs 실제**: 예측 $47–102, 실제 $45 (gamecalc-review)
- **계산기로 뽑을 비교**
  - 외주 견적: 경쟁 글의 $10K+ 범위를 "보도 기준"으로 인용
  - AI로 혼자 만들 때: 소형 $128–181, 최저가 스택 $53–75 (`game-en` 수치와 일치시킬 것)
- **엔진 4종 + 스토어 4곳 비용 한 표**: 경쟁 글에 없는 구성

## 링크
- **계산기**: `/ai-game-cost-calculator` (앵커: "Open the AI game cost calculator")
- **내부 링크**
  - `/blog/ai-game-development-cost` (`game-en`): "AI game development cost by size and genre"
  - `/blog/vibe-coding-a-game-beginner`: "a beginner who vibe-coded a game for $45"
  - `/blog/ai-game-cost-calculator-review`: "I checked the calculator against my released game"
  - `/blog/google-play-closed-testing-14-days`: Google Play 등록 절
- **역방향 링크**: `game-en` → 새 글

## 등록 방법
- 메타 위치: `_source/src/blog_meta.py`의 `INDIECOST`(644~647행)에 en 항목을 추가한다.
  - 예: `_gm("en", "/blog/indie-game-development-cost", ...)`
  - 그다음 `src="indiecost-en"`과 게시일을 update한다.
  - 같은 그룹에 넣으면 build.py가 ko와 hreflang으로 자동 연결한다.
- 원고 파일: `_source/blog_src/indiecost-en.md`
- 검사: `python3 check_post.py indiecost-en`

## 미확인 · 빼거나 "reportedly"로 표시할 것
- Steam 매출 분배 단계 (30% / 25% / 20%): 공식 확인 실패. "standard 30%"만 쓴다.
- 경쟁 글의 외주 견적 ($10K~$1M, Auroch $50K 등): 개발사 주장이므로 "according to …"로 쓴다.
- 2025년 Steam 중위 매출 $249: 2차 출처. 원문 확인 전에는 쓰지 않는다.
- 상위 글 분량·구조, 키워드 검색량: Keyword Planner와 Search Console로 확인한다.

## 출처 초안 (공식)
- [Unity pricing](https://unity.com/products) · [Unity pricing updates](https://unity.com/products/pricing-updates) · [Unity cancels runtime fee](https://unity.com/blog/unity-is-canceling-the-runtime-fee)
- [Unreal Engine FAQ](https://www.unrealengine.com/en-US/faq) · [Godot license](https://godotengine.org/license/) · [GameMaker licences](https://gamemaker.io/en/help/articles/how-to-upgrade-your-gamemaker-licence)
- [Steam Direct fee](https://partner.steamgames.com/doc/gettingstarted/appfee) · [Google Play Console](https://support.google.com/googleplay/android-developer/answer/6112435?hl=en) · [Apple Developer Program](https://developer.apple.com/programs/)
- [itch.io payments](https://itch.io/docs/creators/payments) · [Epic Games Store revenue share](https://store.epicgames.com/en-US/news/epic-games-store-updates-revenue-share-keep-100-of-the-first-1m-per-product-per-year)
- [Claude pricing](https://claude.com/pricing) · [GitHub Copilot plans](https://github.com/features/copilot/plans)

## FAQ 후보
1. How much does it cost to make an indie game?
2. Can one person make an indie game for free?
3. How much does it cost to release a game on Steam, Google Play and the App Store?
4. Is Godot really free? Do Unity and Unreal charge royalties?
5. What is the biggest cost of solo indie game development?
6. Is it cheaper to make a game yourself or hire an outsourcing studio?
7. What hidden costs do indie developers forget?
8. How long does it take to make an indie game alone?
