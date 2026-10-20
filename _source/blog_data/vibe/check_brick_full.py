"""Deeper check of the 15 archived brick-breaker games: 3 lives, score, and a second level.
The games are not modified. A small init script only *observes* canvas drawing calls:
- fillText/strokeText texts (HUD, banners) and DOM text,
- arc() calls, to find the ball so a scripted player can follow it with the mouse.
Time is fast-forwarded with Playwright's fake clock.
usage: python3 check_brick_full.py <runs_dir> > brick_full.json"""
import json, os, re, sys, random
from playwright.sync_api import sync_playwright

RUNS = sys.argv[1]
INIT = r"""
(() => {
  window.__texts = []; window.__arcs = [];
  const P = CanvasRenderingContext2D.prototype;
  for (const fn of ['fillText', 'strokeText']) {
    const o = P[fn];
    P[fn] = function (t, ...r) { window.__texts.push(String(t)); if (window.__texts.length > 3000) window.__texts.splice(0, 1500); return o.call(this, t, ...r); };
  }
  const oa = P.arc;
  P.arc = function (x, y, rad, ...a) {
    if (rad >= 2 && rad <= 20) { const T = this.getTransform(); window.__arcs.push([T.a * x + T.e, T.d * y + T.f, rad, this.canvas.width, this.canvas.height]); if (window.__arcs.length > 200) window.__arcs.splice(0, 100); }
    return oa.call(this, x, y, rad, ...a);
  };
})();
"""
TXT = "(() => { const t = window.__texts.splice(0); return t.concat([document.body ? document.body.innerText : '']); })()"
BALL = """(() => {
  const c = document.querySelector('canvas'); if (!c) return null; const r = c.getBoundingClientRect();
  const a = window.__arcs.splice(0).filter(v => v[1] > v[4] * 0.12);
  if (!a.length) return null; const b = a[a.length - 1];
  return [r.x + b[0] * r.width / b[3], r.y + b[1] * r.height / b[4], r.x, r.width, r.y + r.height, b[1] / b[4]];
})()"""

NUM = lambda s: [int(x) for x in re.findall(r'\d+', s)]


def hud(texts):
    out = {'score': [], 'lives': [], 'level': set(), 'gameover': False, 'win': False}
    for t in texts:
        for line in t.split('\n'):
            l = line.lower()
            if 'score' in l and NUM(l): out['score'].append(NUM(l)[0])
            if re.search(r'li(ves|fe)', l) and NUM(l): out['lives'].append(NUM(l)[0])
            if '♥' in line or '❤' in line: out['lives'].append(line.count('♥') + line.count('❤'))
            m = re.search(r'(level|lvl|stage)\s*:?\s*(\d)', l)
            if m: out['level'].add(int(m.group(2)))
            if 'game over' in l or 'gameover' in l: out['gameover'] = True
            if re.search(r'you win|victory|you won|cleared all|congrat', l): out['win'] = True
    return out


def start(page):
    c = page.evaluate("(() => { const c = document.querySelector('canvas'); if (!c) return null; const r = c.getBoundingClientRect(); return [r.x + r.width/2, r.y + r.height*0.6]; })()")
    if c: page.mouse.click(*c)
    for k in ('Space', 'Enter'):
        page.keyboard.press(k)


def run_game(pw, path, mode):
    b = pw.chromium.launch(); page = b.new_page(viewport={'width': 1200, 'height': 900})
    errors = []; page.on('pageerror', lambda e: errors.append(str(e)[:120]))
    page.add_init_script(INIT); page.clock.install()
    page.goto('file://' + path); page.clock.run_for(500)
    first = hud(page.evaluate(TXT))
    start(page)
    seen = {'score': [], 'lives': [], 'level': set(), 'gameover': False, 'win': False}
    for k in ('score', 'lives'): seen[k] += first[k]
    seen['level'] |= first['level']
    rnd = random.Random(1); drops = 0; low = False
    steps = 1500 if mode == 'play' else 600       # 100 ms each: 150 s / 60 s of game time
    for i in range(steps):
        ball = page.evaluate(BALL)
        if ball:
            x, y, cx, cw, bottom, fy = ball
            if fy > 0.95: low = True
            elif low and fy < 0.8: drops += 1; low = False
            if mode == 'play':
                page.mouse.move(x + rnd.uniform(-12, 12), bottom - 5)
            else:                                   # stay away from the ball
                page.mouse.move(cx + 5 if x > cx + cw / 2 else cx + cw - 5, bottom - 5)
        page.clock.run_for(100)
        if i % 10 == 0:
            for k in ('Space',): page.keyboard.press(k)   # re-serve after a lost ball
            if mode == 'play' and i % 50 == 0: page.mouse.click(*(page.evaluate("(() => { const r = document.querySelector('canvas').getBoundingClientRect(); return [r.x + r.width/2, r.y + r.height*0.6]; })()")))
        if i % 5 == 0:
            h = hud(page.evaluate(TXT))
            seen['score'] += h['score']; seen['lives'] += h['lives']; seen['level'] |= h['level']
            seen['gameover'] |= h['gameover']; seen['win'] |= h['win']
            if mode == 'lose' and seen['gameover']: break
            if mode == 'play' and (2 in seen['level'] and max(seen['score'] or [0]) > 0 and i > 300) or seen['win']: break
    b.close()
    seen['drops'] = drops + (1 if low else 0)
    return first, seen, errors


def main():
    out = {}
    with sync_playwright() as pw:
        for d in sorted(os.listdir(RUNS)):
            if not d.startswith('brick_'): continue
            f = os.path.join(RUNS, d, 'work', 'index.html')
            first, lose, e1 = run_game(pw, f, 'lose')
            _, play, e2 = run_game(pw, f, 'play')
            lives0 = first['lives'][0] if first['lives'] else None
            out[d] = dict(
                lives_start=lives0,
                lives_seen=sorted(set(lose['lives'])),
                balls_lost_until_game_over=lose['drops'] if lose['gameover'] else None,
                lives_ok=lose['gameover'] and lose['drops'] == 3,
                gameover=lose['gameover'],
                score_ok=max(play['score'] or [0]) > 0,
                max_score=max(play['score'] or [0]),
                levels_seen=sorted(play['level']),
                level2=2 in play['level'],
                win=play['win'],
                errors=(e1 + e2)[:3])
            print(d, out[d], file=sys.stderr, flush=True)
    print(json.dumps(out, indent=1))


main()
