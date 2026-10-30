"""ds26 dataset: 504 Claude Code runs, 21 real bugs, Haiku 5.5 and Opus 5.5, 4 conditions, 3 runs each.
Inputs: /home/claude/b26 (scores, baseline, runs). Writes dataset/claude-edge-case-prompts.{csv,json}."""
import csv, io, json, os, re, random, statistics, subprocess, sys
B26 = '/home/claude/b26'; sys.path.insert(0, B26)
import analyze26 as A, meta26
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset')
DS25 = json.load(open('/home/claude/token-cost-by-language/claude-real-bugs/claude-haiku-vs-opus-real-bugs.json'))['bugs']
REPOS = {'cachetools': 'https://github.com/tkem/cachetools', 'Python-Markdown': 'https://github.com/Python-Markdown/markdown', 'anyio': 'https://github.com/agronholm/anyio',
         'dateutil': 'https://github.com/dateutil/dateutil', 'zod': 'https://github.com/colinhacks/zod', 'fastify': 'https://github.com/fastify/fastify',
         'p-queue': 'https://github.com/sindresorhus/p-queue', 'undici': 'https://github.com/nodejs/undici', 'js-yaml': 'https://github.com/nodeca/js-yaml',
         'marked': 'https://github.com/markedjs/marked', 'qs': 'https://github.com/ljharb/qs', 'tomlkit': 'https://github.com/python-poetry/tomlkit'}
LOCAL = {'cachetools': 'cachetools', 'Python-Markdown': 'markdown', 'anyio': 'anyio', 'dateutil': 'dateutil', 'zod': 'zod', 'fastify': 'fastify', 'p-queue': 'p-queue',
         'undici': 'undici', 'js-yaml': 'js-yaml', 'marked': 'marked', 'qs': 'qs', 'tomlkit': 'tomlkit'}
NEW = {}  # tag -> (project, fix commit)
for line in open('/home/claude/hb26/map.txt'):
    t, repo, fix, *_ = line.split()
    NEW[t] = ({'markdown': 'Python-Markdown'}.get(repo, repo), fix)
src = open(f'{B26}/prompts_ds26.py', encoding='utf-8').read()
TITLES = {m.group(1): m.group(2).strip() for m in re.finditer(r"P\['(\w+)'\] = \(\w+, \"\"\"(.+)", src)}
K_FIX = {'ct435': 'aa73a19', 'jy791': 'e5e6f62', 'pm1643': '0bf535b', 'z6495': '84e416fb', 'z6496': 'eab51ff3', 'mk4051': 'e250e31f', 'q629': 'b43b1cf', 't336': 'f466807'}
COND = {'C0': 'baseline (symptom-only report, effort medium)', 'C1': 'effort high', 'C2': 'edge-case prompt', 'C3': 'edge-case prompt + read the existing tests first'}
MODEL = {'haiku': 'claude-haiku-5-5', 'opus': 'claude-opus-5-5'}

def full(repo, c):
    return subprocess.run(['git', '-C', f'/home/claude/hb26/repos/{repo}', 'rev-parse', c], capture_output=True, text=True).stdout.strip()

bugs = {}
for t in A.GROUP:
    if t in DS25:
        p = DS25[t]['project']; fix = full(LOCAL[p], K_FIX[t]); title = DS25[t]['title']
    else:
        p, fx = NEW[t]; fix = full(LOCAL[p], fx); title = TITLES[t]
    parent = full(LOCAL[p], fix + '^')
    bugs[t] = dict(group=A.GROUP[t], project=p, repo=REPOS[p], title=title, fix_commit=fix, parent_commit=parent)

runs = []
for m in ('haiku', 'opus'):
    for l in open(f'{B26}/scores_{m}.jsonl'):
        s = json.loads(l); r = A.row(s); md = meta26.meta(f'{B26}/runs_{m}/{s["run"]}')
        runs.append(dict(run=s['run'], model=MODEL[m], condition=r['cond'], condition_text=COND[r['cond']], bug=r['tag'], group=r['group'],
                         project=bugs[r['tag']]['project'], rep=int(s['run'].split('_')[3][1:]),
                         reported_cases=r['R'], reported_passed=r['Rp'], unreported_cases=r['U'], unreported_passed=r['Up'],
                         unreported_target_cases=r['Ut'], unreported_target_passed=r['Utp'], other_tests_broken=r['broke'],
                         clean_fix=r['clean'], api_cost_usd=md['cost'], seconds=md['seconds'], api_seconds=round(md['api_ms'] / 1000, 1) if md['api_ms'] else None,
                         turns=int(md['turns']) if md['turns'] is not None else None, output_tokens=int(md['out_tokens']) if md['out_tokens'] is not None else None))
runs.sort(key=lambda r: (r['model'], r['condition'], r['bug'], r['rep']))

def bugmean(rs, num, den):
    d = {}
    for r in rs:
        if r[den]: d.setdefault(r['bug'], []).append(r[num] / r[den])
    return {b: sum(v) / len(v) for b, v in d.items()}

def boot(a, b, n=10000, seed=1):
    bs = sorted(set(a) & set(b)); rnd = random.Random(seed); ds = []
    for _ in range(n):
        s = [rnd.choice(bs) for _ in bs]; ds.append(sum(b[x] - a[x] for x in s) / len(s))
    ds.sort(); return [round(ds[int(.025 * n)], 4), round(ds[int(.975 * n)], 4)]

stats = {}
for scope in ('all', 'K', 'N', 'H'):
    S = stats[scope] = {}
    for m in MODEL.values():
        rs0 = [r for r in runs if r['model'] == m and (scope == 'all' or r['group'] == scope)]
        base_u = bugmean([r for r in rs0 if r['condition'] == 'C0'], 'unreported_passed', 'unreported_cases')
        S[m] = {}
        for c in COND:
            rs = [r for r in rs0 if r['condition'] == c]
            u = bugmean(rs, 'unreported_passed', 'unreported_cases'); ut = bugmean(rs, 'unreported_target_passed', 'unreported_target_cases')
            x = dict(runs=len(rs), bugs=len({r['bug'] for r in rs}), unreported_pass_rate=round(sum(u.values()) / len(u), 4),
                     unreported_target_pass_rate=round(sum(ut.values()) / len(ut), 4) if ut else None,
                     clean_fix=sum(r['clean_fix'] for r in rs), runs_with_broken_tests=sum(r['other_tests_broken'] > 0 for r in rs),
                     mean_cost_usd=round(statistics.mean(r['api_cost_usd'] for r in rs), 4), median_seconds=round(statistics.median(r['seconds'] for r in rs)),
                     mean_output_tokens=round(statistics.mean(r['output_tokens'] for r in rs)))
            if c != 'C0':
                x['diff_vs_C0'] = round(x['unreported_pass_rate'] - S[m]['C0']['unreported_pass_rate'], 4)
                x['diff_vs_C0_ci95_bug_bootstrap'] = boot(base_u, u)
                x['cost_change_vs_C0'] = round(x['mean_cost_usd'] / S[m]['C0']['mean_cost_usd'] - 1, 4)
            S[m][c] = x
per_bug = {}
for b in bugs:
    per_bug[b] = {}
    for m in MODEL.values():
        per_bug[b][m] = {}
        for c in COND:
            rs = [r for r in runs if r['bug'] == b and r['model'] == m and r['condition'] == c]
            per_bug[b][m][c] = dict(unreported_pass_rate=round(sum(r['unreported_passed'] for r in rs) / max(1, sum(r['unreported_cases'] for r in rs)), 4) if rs[0]['unreported_cases'] else None,
                                    clean_fix=sum(r['clean_fix'] for r in rs))
for b in bugs:
    r0 = next(r for r in runs if r['bug'] == b); bugs[b].update(reported_cases=r0['reported_cases'], unreported_cases=r0['unreported_cases'], unreported_target_cases=r0['unreported_target_cases'])
tot = {m: dict(runs=sum(1 for r in runs if r['model'] == m), total_cost_usd=round(sum(r['api_cost_usd'] for r in runs if r['model'] == m), 2),
               mean_cost_usd=round(statistics.mean(r['api_cost_usd'] for r in runs if r['model'] == m), 4), clean_fix=sum(r['clean_fix'] for r in runs if r['model'] == m)) for m in MODEL.values()}
D = dict(measured='2026-10-25 to 2026-10-29', runs=runs, bugs=bugs, conditions=COND, stats=stats, per_bug=per_bug, totals=tot,
         prereg='https://github.com/johnisking/token-cost-by-language/blob/main/claude-report-edge-cases/PREREG.md',
         scoring=dict(unreported='maintainer test cases whose input or variant the bug report does not show; includes cases that already pass before the fix (guards)',
                      primary='share of unreported cases passed, averaged per bug, per model and condition; 95% interval from resampling bugs; an effect counts only if it is 20 points or more and the interval excludes 0',
                      clean_fix='every reported and unreported case passes and no other maintainer test breaks'))
os.makedirs(OUT, exist_ok=True)
json.dump(D, open(f'{OUT}/claude-edge-case-prompts.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
buf = io.StringIO(); w = csv.writer(buf); cols = ['run', 'model', 'condition', 'condition_text', 'bug', 'group', 'project', 'repo', 'parent_commit', 'fix_commit', 'rep',
      'reported_cases', 'reported_passed', 'unreported_cases', 'unreported_passed', 'unreported_target_cases', 'unreported_target_passed', 'other_tests_broken', 'clean_fix',
      'api_cost_usd', 'seconds', 'api_seconds', 'turns', 'output_tokens']
w.writerow(cols)
for r in runs:
    b = bugs[r['bug']]; w.writerow([r.get(c, b.get(c)) for c in cols])
open(f'{OUT}/claude-edge-case-prompts.csv', 'w', encoding='utf-8', newline='').write(buf.getvalue())
for scope in ('all', 'K', 'N', 'H'):
    for m in MODEL.values():
        print(scope, m.split('-')[1], ' | '.join(f"{c} U{stats[scope][m][c]['unreported_pass_rate']*100:.0f} clean{stats[scope][m][c]['clean_fix']}/{stats[scope][m][c]['runs']} ${stats[scope][m][c]['mean_cost_usd']:.3f}"
                                                + (f" d{stats[scope][m][c]['diff_vs_C0']*100:+.0f}{[round(v*100) for v in stats[scope][m][c]['diff_vs_C0_ci95_bug_bootstrap']]} cost{stats[scope][m][c]['cost_change_vs_C0']*100:+.0f}%" if c != 'C0' else '') for c in COND))
print(tot)
