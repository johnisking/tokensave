import json,sys,os,glob
def rd(p):
    rows=[];res=None;seen=set();results={}
    for l in open(p,encoding='utf-8',errors='replace'):
        try:j=json.loads(l)
        except: continue
        if j.get('type')=='assistant':
            m=j['message'];u=m.get('usage',{})
            mid=m.get('id')
            for c in m.get('content',[]):
                if c.get('type')=='tool_use': rows.append(('use',c['name'],c['id'],u))
            if mid not in seen:
                seen.add(mid); rows.append(('usage',mid,u.get('input_tokens',0)+u.get('cache_read_input_tokens',0)+u.get('cache_creation_input_tokens',0),u.get('output_tokens',0)))
        if j.get('type')=='user':
            for c in j['message'].get('content',[]) if isinstance(j['message'].get('content'),list) else []:
                if c.get('type')=='tool_result':
                    cc=c.get('content'); txt=json.dumps(cc,ensure_ascii=False) if not isinstance(cc,str) else cc
                    imgs=sum(1 for x in cc if isinstance(x,dict) and x.get('type')=='image') if isinstance(cc,list) else 0
                    results[c['tool_use_id']]=(len(txt),imgs)
        if j.get('type')=='result': res=j
    return rows,results,res
for p in sorted(glob.glob(sys.argv[1] if len(sys.argv)>1 else 'baseline/*/run.jsonl')):
    rows,results,res=rd(p)
    name=p.split('/')[-2]
    mu=res.get('modelUsage',{})
    inp=sum(v['inputTokens']+v['cacheReadInputTokens']+v['cacheCreationInputTokens'] for v in mu.values()); out=sum(v['outputTokens'] for v in mu.values())
    print(f"\n== {name} in={inp} out={out} cost={res['total_cost_usd']:.3f} turns={res['num_turns']} ans={res.get('result','')[:60]!r}")
    for r in rows:
        if r[0]=='use': print('   use',r[1],'result_chars',results.get(r[2]))
        else: print('   req in',r[2],'out',r[3])
