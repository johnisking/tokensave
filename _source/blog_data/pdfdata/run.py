import json,subprocess,base64,sys
def run(model,content):
    msg=json.dumps({"type":"user","message":{"role":"user","content":content}})
    p=subprocess.run(["claude","-p","--model",model,"--system-prompt","Reply with the single word OK.","--tools","Read","--input-format","stream-json","--output-format","stream-json","--verbose"],input=msg+"\n",capture_output=True,text=True,timeout=600)
    for line in p.stdout.splitlines():
        try:o=json.loads(line)
        except:continue
        if o.get("type")=="result":
            u=o["usage"];return u["input_tokens"]+u.get("cache_creation_input_tokens",0)+u.get("cache_read_input_tokens",0)
    return ("ERR",p.stdout[-400:],p.stderr[-400:])
m=sys.argv[1]
dot={"type":"text","text":"."}
base=run(m,[dot]);out={"base":base}
for n in ['text_1p','text_5p','text_10p','table_1p','scan_1p']:
    doc={"type":"document","source":{"type":"base64","media_type":"application/pdf","data":base64.b64encode(open(f'pdfs/{n}.pdf','rb').read()).decode()}}
    r=run(m,[doc,dot]); out[n]=r-base if isinstance(r,int) else r
pl=json.load(open('plain.json'))
for k,v in pl.items():
    r=run(m,[{"type":"text","text":v}]); out[k]=r-base if isinstance(r,int) else r
json.dump(out,open(f'claude_{m}.json','w'),indent=1)
print(json.dumps(out))
