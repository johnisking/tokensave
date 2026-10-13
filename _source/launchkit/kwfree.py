#!/usr/bin/env python3
"""Free keyword research: autocomplete expansion + (optional) Naver search-ad volumes.

  python3 kwfree.py "클로드 요금" --lang ko
  python3 kwfree.py "claude pricing" --lang en --sources google,youtube,bing,ddg
  python3 kwfree.py "クロード 料金" --lang ja --out ../launchkit/kw/claude-ja.csv

How it works (no paid tools):
  1. Ask each free autocomplete (Google, YouTube, Bing, DuckDuckGo, Naver for ko) for
     the seed, the seed + question words (가격, 무료, vs, …) and the seed + a..z / 가..하.
  2. Score every suggestion: how many sources and queries returned it, and how high.
     More sources + higher rank = more people type it. This is a demand signal, not a volume.
  3. Mark suggestions we already cover in _source/blog_src/*-<lang>.md.
  4. If NAVER_AD_API_KEY, NAVER_AD_SECRET, NAVER_AD_CUSTOMER are set (free Naver search-ad
     account → 도구 → API 사용 관리), add real monthly Naver search volumes (PC + mobile).
"""
import argparse, base64, csv, hashlib, hmac, json, os, re, sys, time, urllib.parse, urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'}

MODIFIERS = {
    'ko': ['가격', '요금', '요금제', '무료', '얼마', '비교', '차이', 'vs', '한도', '사용법', '추천', '할인', '결제', '해지', 'api'],
    'ja': ['料金', '価格', '無料', '比較', '違い', 'vs', '制限', '使い方', 'おすすめ', '安く', '支払い', '解約', 'api'],
    'en': ['price', 'pricing', 'cost', 'free', 'vs', 'limit', 'how to', 'alternative', 'cheap', 'discount', 'per month', 'api', 'worth it'],
    'tr': ['fiyat', 'fiyatı', 'ücretsiz', 'ücretli', 'kaç tl', 'tl', 'abonelik', 'vs', 'farkı', 'limit', 'nasıl kullanılır', 'indirim', 'iptal', 'öğrenci', 'api'],
}
LETTERS = {
    'ko': list('가나다라마바사아자차카타파하'),
    'ja': list('あかさたなはまやらわ'),
    'en': list('abcdefghijklmnopqrstuvwxyz'),
    'tr': list('abcçdefgğhıijklmnoöprsştuüvyz'),
}
HL = {'ko': ('ko', 'kr', 'ko-KR'), 'ja': ('ja', 'jp', 'ja-JP'), 'en': ('en', 'us', 'en-US'), 'tr': ('tr', 'tr', 'tr-TR')}


def _get(url, timeout=8):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
    for enc in ('utf-8', 'cp949', 'euc-kr', 'shift_jis'):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            pass
    return raw.decode('utf-8', 'replace')


def google(q, lang, ds=''):
    hl, gl, _ = HL[lang]
    url = 'https://suggestqueries.google.com/complete/search?' + urllib.parse.urlencode(
        {'client': 'firefox', 'hl': hl, 'gl': gl, 'q': q, **({'ds': ds} if ds else {})})
    return json.loads(_get(url))[1]


def youtube(q, lang):
    return google(q, lang, ds='yt')


def bing(q, lang):
    url = 'https://api.bing.com/osjson.aspx?' + urllib.parse.urlencode({'query': q, 'mkt': HL[lang][2]})
    return json.loads(_get(url))[1]


def ddg(q, lang):
    url = 'https://duckduckgo.com/ac/?' + urllib.parse.urlencode({'q': q, 'kl': f'{HL[lang][1]}-{HL[lang][0]}'})
    return [x['phrase'] for x in json.loads(_get(url))]


def naver(q, lang):
    url = 'https://ac.search.naver.com/nx/ac?' + urllib.parse.urlencode(
        {'q': q, 'st': 100, 'r_format': 'json', 'r_enc': 'UTF-8', 'q_enc': 'UTF-8', 'frm': 'nv'})
    data = json.loads(_get(url))
    return [item[0] for group in data.get('items', []) for item in group]


SOURCES = {'google': google, 'youtube': youtube, 'bing': bing, 'ddg': ddg, 'naver': naver}


def queries(seed, lang, letters=True):
    qs = [seed] + [f'{seed} {m}' for m in MODIFIERS[lang]]
    if letters:
        qs += [f'{seed} {c}' for c in LETTERS[lang]]
    return qs


def norm(s):
    return re.sub(r'\s+', ' ', s.strip().lower())


def collect(seed, lang, sources, letters=True, workers=6, delay=0.15):
    """Returns {suggestion: {'sources': set, 'hits': int, 'best': int, 'score': float}}, errors."""
    jobs = [(name, q) for name in sources for q in queries(seed, lang, letters)]
    errors = defaultdict(int)

    def run(job):
        name, q = job
        time.sleep(delay)
        try:
            return name, q, SOURCES[name](q, lang)
        except Exception:
            errors[name] += 1
            return name, q, []

    out = {}
    with ThreadPoolExecutor(workers) as ex:
        for name, q, sugg in ex.map(run, jobs):
            for rank, s in enumerate(sugg[:10]):
                k = norm(s)
                if not k or k == norm(q):  # an echo of our own query is not a suggestion
                    continue
                d = out.setdefault(k, {'sources': set(), 'hits': 0, 'best': 99, 'score': 0.0})
                d['sources'].add(name)
                d['hits'] += 1
                d['best'] = min(d['best'], rank + 1)
                d['score'] += 1.0 / (rank + 1)
    for d in out.values():
        d['score'] = round(d['score'] * len(d['sources']), 2)
    return out, dict(errors), len(jobs)


def covered(lang):
    """Text of our existing posts in this language, lower-cased, spaces removed."""
    d = os.path.join(ROOT, 'blog_src')
    txt = []
    for f in os.listdir(d):
        if f.endswith(f'-{lang}.md'):
            txt.append(open(os.path.join(d, f), encoding='utf-8').read())
    return re.sub(r'\s+', '', ' '.join(txt).lower())


def naver_volumes(keywords):
    """Real monthly Naver search volumes via the free search-ad keyword tool API."""
    key, secret, cust = (os.environ.get(k) for k in ('NAVER_AD_API_KEY', 'NAVER_AD_SECRET', 'NAVER_AD_CUSTOMER'))
    if not (key and secret and cust):
        return {}
    vols = {}
    hints = [k.replace(' ', '') for k in keywords]
    for i in range(0, len(hints), 5):  # API takes at most 5 hint keywords per call
        ts = str(int(time.time() * 1000))
        sig = base64.b64encode(hmac.new(secret.encode(), f'{ts}.GET./keywordstool'.encode(), hashlib.sha256).digest()).decode()
        url = 'https://api.naver.com/keywordstool?' + urllib.parse.urlencode({'hintKeywords': ','.join(hints[i:i + 5]), 'showDetail': 1})
        req = urllib.request.Request(url, headers={'X-Timestamp': ts, 'X-API-KEY': key, 'X-Customer': cust, 'X-Signature': sig})
        try:
            data = json.loads(urllib.request.urlopen(req, timeout=10).read())
        except Exception as e:
            print(f'naver volume error: {e}', file=sys.stderr)
            break
        for row in data.get('keywordList', []):
            n = lambda v: 5 if isinstance(v, str) else int(v)  # "< 10" -> 5
            vols[row['relKeyword'].lower()] = n(row['monthlyPcQcCnt']) + n(row['monthlyMobileQcCnt'])
        time.sleep(0.3)
    return vols


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('seed')
    ap.add_argument('--lang', default='ko', choices=list(MODIFIERS))
    ap.add_argument('--sources', help='comma list; default google,youtube,bing (+naver for ko)')
    ap.add_argument('--no-letters', action='store_true', help='skip a..z / 가..하 expansion (faster)')
    ap.add_argument('--top', type=int, default=60)
    ap.add_argument('--out', help='also write CSV here')
    a = ap.parse_args()

    sources = a.sources.split(',') if a.sources else ['google', 'youtube', 'bing'] + (['naver'] if a.lang == 'ko' else [])
    res, errors, njobs = collect(a.seed, a.lang, sources, letters=not a.no_letters)
    for name in sources:
        if errors.get(name, 0) * 2 > njobs / len(sources):
            print(f'warning: {name} failed for {errors[name]} queries (blocked or rate-limited?)', file=sys.stderr)
    if not res:
        sys.exit('no suggestions: every source failed (network blocked?)')

    rows = sorted(res.items(), key=lambda kv: -kv[1]['score'])[:a.top]
    ours = covered(a.lang)
    vols = naver_volumes([k for k, _ in rows]) if a.lang == 'ko' else {}

    header = ['keyword', 'score', 'sources', 'hits', 'best_rank', 'naver_monthly', 'we_cover']
    table = []
    for k, d in rows:
        table.append([k, d['score'], '+'.join(sorted(d['sources'])), d['hits'], d['best'],
                      vols.get(k.replace(' ', ''), ''), 'yes' if k.replace(' ', '') in ours else ''])

    print(f'# {a.seed} ({a.lang}) — {len(res)} suggestions from {", ".join(sources)}; top {len(table)}')
    print('| ' + ' | '.join(header) + ' |')
    print('|' + '---|' * len(header))
    for r in table:
        print('| ' + ' | '.join(str(x) for x in r) + ' |')
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        with open(a.out, 'w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerows([header] + table)
        print(f'\nwrote {a.out}', file=sys.stderr)


if __name__ == '__main__':
    main()
