#!/usr/bin/env python3
"""Pre-publish checklist for blog articles (see launchkit/BLOG_CHECKLIST.md).

  python3 check_post.py muse13-ko indiecost-ko      # md names in blog_src/
Prints a PASS / WARN / FAIL table per article plus the manual questions.
Exit code 1 if any FAIL.
"""
import os, re, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
import autoimg as A

CJK = {'ko', 'ja', 'zh-CN', 'zh-TW'}
TOOL_PATHS = ('/image', '/video', '/plans', '/agents', 'ai-game-cost-calculator', 'claude-token-counter')
MULT = re.compile(r'(\d+(?:[.,]\d+)?\s*(?:배|倍|×|گنا|गुना|पट|ಪಟ್ಟು|மடங்கு|రెట్లు|ਗੁਣਾ|katı|razy|raza|fois|veces|vezes|times|krát|kertaa|φορές|gånger|برابر|ضعف|เท่า|lần)|gấp\s*\d|\b\d+(?:[.,]\d+)?x\b)', re.I)
MULT_OK = re.compile(r'(?-i:Max|Ultra|Pro)\s*\d+\s*[x×]|\d+\s*[x×]\s*(plan|요금제|プラン|Plus)|[x×]\s*\d|(?-i:Plus)|사용량|利用量|usage|^\s*\||\d\s*×\s*\(|×\s*\$|(times|razy)\s+(a |per |each |every |dzienn|w |co )|\*\*\d+\s*(times|razy)\*\*', re.I)  # counts and formulas, not ratios
PLAN_CTX = re.compile(r'(?-i:Plus|Max\b|Ultra)|Pro ?\d|사용량|利用量|倍率|요금제', re.I)
IMG_WORDS = {'ko': '이미지', 'ja': '画像', 'en': 'image'}
VID_WORDS = {'ko': '영상', 'ja': '動画', 'en': 'video'}
FAQ = re.compile(r'^## .*(FAQ|자주 묻는|よくある|Frequently|Preguntas|Perguntas|Sık|Częste|Häufig|Questions)', re.M | re.I)
SRC = re.compile(r'^[*_ ]*(## .*(Sources|출처|出典|Kaynaklar|Fuentes|Fontes|Fonti|Źródła|Quellen|Bronnen|Джерела|Источники|Kilder|Lähteet|Källor|Zdroje|Források|Surse|Πηγές|المصادر|منابع|स्रोत|উৎস|ذرائع|מקורות|แหล่งที่มา|Nguồn|Sumber|Mga sanggunian|来源|來源|ಮೂಲಗಳು|സ്രോതസ്സുകൾ|ஆதாரங்கள்|మూలాలు|ਸਰੋਤ|સ્રોતો)|(Sources?|출처|出典|Źródło|Źródła|Fuente|Fuentes|Fonte|Fontes|Quelle|Quellen|Source|Kaynak|Kaynaklar|Bron|Bronnen|Джерело|Джерела|来源|來源|資料來源|Nguồn|Sumber|स्रोत|المصدر|منبع|מקור|แหล่งที่มา|Zdroj|Πηγή|Kilde|Lähde|Källa|Forrás|Sursă|Fonte)\s*[:：])', re.M | re.I)


def meta_for(src):
    for b in A.groups():
        if b.get('src', b['tag']) == src:
            return b
    return None


def check(src):
    rows = []
    def r(group, name, status, note=''):
        rows.append((group, name, status, note))
    b = meta_for(src)
    md = open(os.path.join(ROOT, 'blog_src', src + '.md'), encoding='utf-8').read()
    if not b:
        r('SEO', 'blog_meta 등록', 'FAIL', 'blog_meta.py에 없음')
        return rows
    tag = b['tag']
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', md)
    plain = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    # --- SEO
    tl = len(b['title'])
    lim = 40 if tag in CJK else 65
    r('SEO', '제목 길이', 'PASS' if tl <= lim else 'WARN', f'{tl}자 (권장 {lim} 이하)')
    dl = len(b['desc'])
    r('SEO', '설명 길이', 'PASS' if 70 <= dl <= 160 else ('FAIL' if dl > 160 else 'WARN'), f'{dl}자 (70~160)')
    kw = re.split(r'[:：|?？(（]', b['title'])[0].strip()
    kw_words = [w for w in re.split(r'[\s·・,]+', kw) if len(w) >= 2][:3]
    first = plain.split('\n## ')[0][:600].lower()
    hit = sum(1 for w in kw_words if w.lower() in first)
    r('SEO', '첫 문단에 핵심 검색어', 'PASS' if kw_words and hit >= max(1, len(kw_words) - 1) else 'WARN', f'"{kw}"')
    h2 = len(re.findall(r'^## ', md, re.M))
    r('SEO', '소제목(H2) 4개 이상', 'PASS' if h2 >= 4 else 'FAIL', f'{h2}개')
    tables = len(re.findall(r'^\|\s*-', md, re.M)) + len(re.findall(r'^\|---', md, re.M))
    r('SEO', '표 1개 이상', 'PASS' if tables else 'WARN', f'{tables}개')
    links = re.findall(r'\]\((/[^)]*)\)', text)
    internal = [l for l in links if not l.endswith(('.jpg', '.png', '.svg'))]
    tool = [l for l in internal if any(t in l for t in TOOL_PATHS) or re.fullmatch(r'/([a-z]{2,3}(-[a-z]{2})?/)?', l)]
    r('SEO', '내부 링크 2개 이상', 'PASS' if len(internal) >= 2 else 'FAIL', f'{len(internal)}개')
    r('SEO', '계산기 링크', 'PASS' if tool else 'FAIL', ', '.join(sorted(set(tool)))[:80])
    lw = IMG_WORDS.get(tag); vw = VID_WORDS.get(tag)
    if lw and lw in plain.lower() and not any('/image' in l for l in internal):
        r('SEO', '이미지 언급 → /image 링크', 'WARN', '이미지 이야기가 있는데 이미지 계산기 링크 없음')
    if vw and vw in plain.lower() and not any('/video' in l for l in internal):
        r('SEO', '영상 언급 → /video 링크', 'WARN', '영상 이야기가 있는데 영상 계산기 링크 없음')
    ext = re.findall(r'\]\((https?://[^)]*)\)', text)
    r('SEO', '출처 섹션', 'PASS' if SRC.search(md) else 'FAIL', '')
    r('SEO', '외부 출처 링크 2개 이상', 'PASS' if len(ext) >= 2 else 'FAIL', f'{len(ext)}개')
    r('SEO', 'FAQ 섹션', 'PASS' if FAQ.search(md) else 'WARN', '권장')
    bad = []
    alts = re.findall(r'!\[([^\]]*)\]\(', md)
    for line in plain.split('\n') + [b['title'], b['desc']] + alts:
        if PLAN_CTX.search(line):
            continue  # plan usage tiers (Plus 대비 5배, Max 5x) keep the company's wording
        for m in MULT.finditer(line):
            ctx = line[max(0, m.start() - 12): m.end() + 8]
            if not MULT_OK.search(ctx):
                bad.append(ctx.strip())
    r('SEO', '배수 표현 없음', 'PASS' if not bad else 'FAIL', '; '.join(bad[:3]))
    # --- Images
    imgs = re.findall(r'!\[([^\]]*)\]\(/([^)]+)\)', md)
    r('이미지', '이미지 3장 이상', 'PASS' if len(imgs) >= 3 else 'FAIL', f'{len(imgs)}장')
    r('이미지', '맨 위 대표 이미지', 'PASS' if md.lstrip().startswith('![') else 'WARN', '')
    og = b.get('og') or A.json.load(open(A.MAPF)).get(b['path']) if os.path.exists(A.MAPF) else b.get('og')
    r('이미지', '공유용 대표 이미지(og)', 'PASS' if og else 'WARN', og or '그룹 기본 이미지 사용')
    for alt, f in imgs:
        if f.startswith('img/'):
            continue  # charts generated at build time
        p = os.path.join(ROOT, 'src', 'static', f)
        issues = []
        if not os.path.exists(p):
            issues.append('파일 없음')
        else:
            kb = os.path.getsize(p) // 1024
            if kb > (600 if f.endswith('.gif') else 200):
                issues.append(f'{kb}KB')
        if len(alt) < 15:
            issues.append('alt 짧음')
        if not re.fullmatch(r'[a-z0-9][a-z0-9\-]*\.(jpg|png|webp|svg|gif)', f):
            issues.append('파일명 형식')
        if f.endswith(('.jpg', '.png')) and not re.search(r'-(%s)(-\d+)?\.' % '|'.join(map(re.escape, {tag.lower(), tag.lower().replace('-', '')})), f) and 'blog-' not in f:
            issues.append('언어 코드 없음')
        r('이미지', f[:48], 'PASS' if not issues else 'FAIL', ', '.join(issues))
    # --- Depth
    body = re.sub(r'[#>*|`\-]', '', plain)
    if tag in CJK:
        n = len(re.sub(r'\s', '', body)); need = 2500; unit = '자'
    else:
        n = len(body.split()); need = 700; unit = '단어'
    r('깊이', '분량', 'PASS' if n >= need else 'WARN', f'{n}{unit} (권장 {need} 이상)')
    dated = re.search(r'20\d\d', plain)
    r('깊이', '확인 날짜·연도 표기', 'PASS' if dated else 'WARN', '')
    return rows


MANUAL = [
    '검색 의도에 맞는 답을 첫 화면(30초 요약/첫 문단)에서 바로 주는가?',
    '상위 글과 다른 우리만의 차별점이 있는가? (계산기 데이터, 직접 측정, 실제 경험)',
    '가격·수치를 공식 자료로 확인했고, 확인 날짜를 적었는가?',
    '확인 못 한 내용은 빼거나 "보도 기준"으로 출처를 밝혔는가?',
    '회사 주장(벤치마크 등)은 "○○에 따르면"으로 구분했는가?',
    '경험담은 재현이 실제로 말한 내용만 썼는가?',
    '이미지 속 숫자가 본문과 같고, 글자 잘림이 없는가? (미리보기 확인)',
    '재현에게 원고·이미지·이 체크 결과를 보여 주고 "올려"를 받았는가?',
]


def main():
    names = sys.argv[1:]
    fail = False
    for n in names:
        rows = check(n)
        print(f'\n### {n}\n')
        print('| 구분 | 항목 | 결과 | 비고 |\n|---|---|---|---|')
        for g, name, st, note in rows:
            mark = {'PASS': '✅', 'WARN': '⚠️', 'FAIL': '❌'}[st]
            print(f'| {g} | {name} | {mark} {st} | {note} |')
            fail |= st == 'FAIL'
    print('\n### 사람이 확인할 항목\n')
    for q in MANUAL:
        print(f'- [ ] {q}')
    sys.exit(1 if fail else 0)


if __name__ == '__main__':
    main()
