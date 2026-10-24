import json
rows=[json.loads(l) for l in open('/home/claude/b15/scores.jsonl')]
ref={'q624':2,'q629':1}
for r in sorted(rows,key=lambda r:(r['bug'],['haiku','sonnet','opus'].index(r['tool']),r['rep'])):
    d=f"/home/claude/b15/results/{r['run']}"
    res=None
    for l in open(d+'/run.jsonl',encoding='utf-8',errors='replace'):
        if '"type":"result"' in l:
            try: res=json.loads(l)
            except: pass
    cost=res.get('total_cost_usd') if res else None; den=len(res.get('permission_denials',[])) if res else None
    broke=(r['suite_failures'] or 0)-ref.get(r['bug'],0) if r['suite_failures'] is not None else 'NA'
    print(f"{r['bug']:6} {r['tool']:6} r{r['rep']} {r['hidden_passed']}/{r['hidden_total']} broke={broke} src={r['src_changed']} ap={r['applied']} cost={cost and round(cost,3)} den={den} t={open(d+'/seconds.txt').read().strip()}")
