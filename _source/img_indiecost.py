#!/usr/bin/env python3
"""Images for /ko/blog/indie-game-gaebal-biyong (indiecost-ko.md). Numbers mirror the article."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import autoimg as A
from PIL import Image

OUT = A.STATIC
B = dict(tag='ko', title='인디게임 개발 비용 얼마? 1인 개발 vs 외주, 엔진·스토어 등록비 정리 (2026)')
KICK = '인디게임 개발 비용'
EXTRA = """
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:34px}
.col{border:3px solid;border-radius:20px;padding:24px;background:#1c1928}
.col h3{font-size:32px;font-weight:900}
.col .pr{font-size:24px;font-weight:800;color:#ffd166;margin:8px 0 16px}
.col .lb{font-size:18px;font-weight:800;letter-spacing:.5px;margin-top:12px}
.col ul{list-style:none;margin-top:6px}
.col li{font-size:21px;line-height:1.5;color:#e7e4f3;padding-left:22px;position:relative;margin-top:4px}
.col li:before{position:absolute;left:0;font-weight:900}
.pro li:before{content:"+";color:#4ade80}.con li:before{content:"−";color:#ff7aa8}
.col .fit{margin-top:16px;font-size:20px;color:#c4b5fd;font-weight:700;border-top:1px solid #2d2a3d;padding-top:12px}
.grid4{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:34px}
.st{border:3px solid;border-radius:20px;padding:24px 26px;background:#1c1928}
.st .nm{font-size:30px;font-weight:900}
.st .fee{font-size:44px;font-weight:900;margin:6px 0 12px}
.st .fee small{font-size:22px;color:#b8b3cc;font-weight:700}
.st li{list-style:none;font-size:21px;line-height:1.55;color:#e7e4f3}
.st li:before{content:"· ";color:#7d7891}
.bars{display:flex;flex-direction:column;gap:30px;margin-top:40px}
.bl{display:flex;justify-content:space-between;font-size:25px;margin-bottom:10px}
.bl b{font-size:28px}
.tr{height:54px;border-radius:14px;background:#221e31;overflow:hidden}
.fill{height:100%;border-radius:14px}
.note{font-size:20px;color:#9a95ad;margin-top:26px;line-height:1.5}
"""

def card(inner_h2, body, foot=True):
    return (f'<div class="card"><div class="kick">{KICK}</div><h2>{inner_h2}</h2>{body}'
            + (A.foot(B) if foot else '') + '</div>')

def engines():
    E = [('#a78bfa', 'Unity', '무료 · Pro 연 $2,310',
          ['모바일·PC 출시가 쉬움', '에셋 스토어·강좌·자료가 많음', '언어: C#'],
          ['매출·투자금 연 20만 달러 넘으면 Pro', '콘솔 출시는 Pro부터'], '2D·3D 모바일, 자료로 배우기'),
         ('#4ade80', 'Godot', '완전 무료 (MIT)',
          ['로열티 없음', '가볍고 설치가 빠름', 'GDScript(파이썬과 비슷)·C#'],
          ['콘솔은 외부 이식 업체 필요', '에셋·자료가 Unity보다 적음'], '2D, 엔진 비용 평생 0원'),
         ('#60a5fa', 'Unreal', '무료 · 로열티 5%',
          ['고품질 3D 그래픽', '코딩 없이 블루프린트'],
          ['무겁고 고사양 PC 필요', '총매출 100만 달러 초과분 로열티'], '3D·고사양 PC 게임')]
    cols = ''
    for c, n, pr, pro, con, fit in E:
        cols += (f'<div class="col" style="border-color:{c}"><h3 style="color:{c}">{n}</h3><div class="pr">{pr}</div>'
                 f'<div class="lb" style="color:#4ade80">장점</div><ul class="pro">' + ''.join(f'<li>{x}</li>' for x in pro) + '</ul>'
                 f'<div class="lb" style="color:#ff7aa8">단점</div><ul class="con">' + ''.join(f'<li>{x}</li>' for x in con) + '</ul>'
                 f'<div class="fit">{fit}</div></div>')
    return card('게임 엔진 비교: Unity vs Godot vs Unreal', f'<div class="cols">{cols}</div>')

def stores():
    S = [('#4ade80', 'Google Play', '$25', ' 1회', ['신원 확인', '개인 계정: 테스터 12명, 14일 연속 비공개 테스트', '유료·인앱: 결제 프로필']),
         ('#60a5fa', 'Steam', '$100', ' 게임당', ['실명 가입·신원 확인·정산 계좌', '미국 세금 설문 (영업일 10~15일)', '결제 후 출시까지 21일, 출시 예정 페이지 2주']),
         ('#e5e7eb', 'Apple App Store', '$99', ' 매년', ['2단계 인증 Apple 계정, 실명', '단체 가입은 D-U-N-S 번호', '유료·인앱: 미국 세금 양식·정산 계좌']),
         ('#ffd166', '웹 (itch.io·자체 사이트)', '0원', '', ['등록비 없음', '먼저 내고 반응 보기 좋음'])]
    g = ''
    for c, n, fee, per, items in S:
        g += (f'<div class="st" style="border-color:{c}"><div class="nm" style="color:{c}">{n}</div>'
              f'<div class="fee">{fee}<small>{per}</small></div><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>')
    return card('스토어 등록비와 출시 준비물', f'<div class="grid4">{g}</div><div class="note">공식 문서 기준 · 2026년 10월 확인</div>')

def outsourcing():
    mx = 2940000
    rows = [('외주 개발 평균 견적 (미소)', '약 294만원', 2940000, '#ff7aa8'),
            ('AI로 혼자 · 보통 조합', '약 17만~24만원', 243445, '#a78bfa'),
            ('AI로 혼자 · 가성비 조합', '약 7만~10만원', 100875, '#4ade80')]
    b = ''
    for lab, val, v, c in rows:
        w = max(2.5, v / mx * 100)
        b += f'<div><div class="bl"><span>{lab}</span><b style="color:{c}">{val}</b></div><div class="tr"><div class="fill" style="width:{w:.1f}%;background:{c}"></div></div></div>'
    note = '외주 평균은 미소 안내(2025년 12월) 기준. AI 비용은 소형 2D 머지 게임, tokensave.app 게임 계산기 예상치이며 내 시간은 포함하지 않았습니다. 1달러 = 1,345원.'
    return card('외주 vs AI로 혼자 만들기: 돈은 얼마나 들까', f'<div class="bars">{b}</div><div class="note">{note}</div>')

def main():
    md = os.path.join(A.ROOT, 'blog_src', 'indiecost-ko.md')
    s = open(md, encoding='utf-8').read()
    _, secs = A.sections(s)
    chips = ['엔진 비용·장단점', '스토어 등록비', '외주 vs AI']
    four = next(b for h, li, b in secs if h.startswith('인디게임 비용은'))
    t4 = A.parse_table(four)
    why = next(b for h, li, b in secs if h.startswith('기간은 왜'))
    items = [
        ('indie-game-gaebal-biyong-ko.jpg', B['title'], A.cover_html(B, chips), None),
        ('indie-game-cost-4-items-ko.jpg', '인디게임 비용 네 가지: 엔진, 그래픽·사운드, 코딩, 출시 비용 범위', A.table_html(B, '인디게임 비용은 네 가지로 나뉩니다', t4), '## 인디게임 비용은 네 가지로 나뉩니다'),
        ('unity-vs-godot-vs-unreal-cost-ko.jpg', '게임 엔진 비교: Unity, Godot, Unreal Engine 가격과 장단점', engines(), '### 엔진별 장단점'),
        ('steam-google-play-apple-fee-ko.jpg', '스토어 등록비와 출시 준비물: Google Play $25, Steam $100, Apple 연 $99, 웹 0원', stores(), '## 출시 준비물: 돈 말고도 필요한 것'),
        ('indie-game-outsourcing-vs-ai-cost-ko.jpg', '외주 개발 평균 견적 약 294만원 vs AI로 혼자 만들기 약 7만~24만원 비교', outsourcing(), '## 외주 vs AI로 혼자 만들기'),
        ('indie-game-dev-time-factors-ko.jpg', '개발 기간이 사람마다 다른 이유: 요구 사항의 디테일, 경험, 하루에 쓰는 시간, 기능 추가, 그래픽 수준', A.list_html(B, '기간은 왜 사람마다 다를까', A.parse_list(why)), '## 기간은 왜 사람마다 다를까'),
    ]
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        br = pw.chromium.launch(); pg = br.new_page(viewport={'width': 1200, 'height': 800})
        for name, alt, inner, _ in items:
            html = A.page('ko', inner).replace('</style>', EXTRA + '</style>')
            pg.set_content(html, wait_until='load'); pg.evaluate('document.fonts.ready')
            tmp = os.path.join(OUT, '_t.png'); pg.locator('.card').first.screenshot(path=tmp)
            Image.open(tmp).convert('RGB').save(os.path.join(OUT, name), 'JPEG', quality=82, optimize=True, progressive=True)
            os.remove(tmp); print(name)
        br.close()
    if '--md' in sys.argv and '](/indie-game-gaebal-biyong-ko.jpg)' not in s:
        lines = s.split('\n')
        for name, alt, _, anchor in reversed(items[1:]):
            i = lines.index(anchor)
            lines[i + 1:i + 1] = ['', f'![{alt}](/{name})']
        s = f'![{items[0][1]}](/{items[0][0]})\n\n' + '\n'.join(lines)
        open(md, 'w', encoding='utf-8').write(s)
        import json
        mp = json.load(open(A.MAPF)); mp['/ko/blog/indie-game-gaebal-biyong'] = items[0][0]
        json.dump(mp, open(A.MAPF, 'w'), ensure_ascii=False, indent=0, sort_keys=True)

if __name__ == '__main__':
    main()
