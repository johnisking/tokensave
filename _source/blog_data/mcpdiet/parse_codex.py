"""Summarise Codex exec --json runs of the browser-MCP diet test.
usage: parse_codex.py <runs dir> [out.json]"""
import json, sys, glob, os, re, statistics as st

def rd(p):
    usage = None; tools = {}; big = 0; total_res = 0; ans = ''; errs = 0
    for l in open(p, encoding='utf-8', errors='replace'):
        if not l.startswith('{'): continue
        try: j = json.loads(l)
        except Exception: continue
        if j.get('type') == 'turn.completed': usage = j['usage']
        it = j.get('item') or {}
        if j.get('type') == 'item.completed' and it.get('type') == 'mcp_tool_call':
            tools[it['tool']] = tools.get(it['tool'], 0) + 1
            if it.get('error'): errs += 1
            r = it.get('result') or {}
            n = sum(len(c.get('text', '')) for c in r.get('content', []) if isinstance(c, dict))
            total_res += n; big = max(big, n)
        if j.get('type') == 'item.completed' and it.get('type') == 'command_execution':
            tools['SHELL'] = tools.get('SHELL', 0) + 1
        if j.get('type') == 'item.completed' and it.get('type') == 'agent_message': ans = it['text']
    return usage, tools, big, total_res, ans, errs

def ok(task, ans, tools):
    if not any(k.startswith(('browser_', 'take_', 'new_page', 'navigate')) for k in tools): return False
    if task == 'probe': return 'done' in ans.lower()
    if task == 'snapread': return 'Guido' in ans and '1991' in ans
    if task == 'hnsnap': return len(re.findall(r'\d+\s*points?', ans)) >= 5
    return True

out = {}
for d in sorted(glob.glob(os.path.join(sys.argv[1], 'codex_*_r[1-9]'))):
    name = os.path.basename(d)
    _, srv, mode, task, rep = name.split('_')
    u, tools, big, tres, ans, errs = rd(os.path.join(d, 'run.jsonl'))
    sec = int(open(os.path.join(d, 'seconds.txt')).read().strip() or 0) if os.path.exists(os.path.join(d, 'seconds.txt')) else None
    out[name] = dict(srv=srv, mode=mode, task=task, run=rep, input_tokens=u['input_tokens'] if u else None,
                     cached_input_tokens=u['cached_input_tokens'] if u else None, output_tokens=u['output_tokens'] if u else None,
                     reasoning_output_tokens=u.get('reasoning_output_tokens') if u else None,
                     seconds=sec, tools=tools, tool_errors=errs, largest_result_chars=big, result_chars=tres,
                     correct=ok(task, ans, tools), answer=ans[:200])
if len(sys.argv) > 2: json.dump(out, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)

print(f"{'srv':4} {'task':9} {'base in (median)':>17} {'diet in':>9} {'change':>7}  ok base/diet")
for srv in ('pw', 'cdt'):
    for task in ('probe', 'snapread', 'hnsnap'):
        b = [r for r in out.values() if r['srv'] == srv and r['task'] == task and r['mode'] == 'base' and r['input_tokens']]
        v = [r for r in out.values() if r['srv'] == srv and r['task'] == task and r['mode'] == 'v3' and r['input_tokens']]
        if not b or not v: continue
        mb = st.median(r['input_tokens'] for r in b); mv = st.median(r['input_tokens'] for r in v)
        print(f"{srv:4} {task:9} {mb:17,.0f} {mv:9,.0f} {100*(mv-mb)/mb:+6.0f}%  {sum(r['correct'] for r in b)}/{len(b)} {sum(r['correct'] for r in v)}/{len(v)}")
