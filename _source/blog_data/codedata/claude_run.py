import json,subprocess,sys
def run(model,text):
    msg=json.dumps({"type":"user","message":{"role":"user","content":[{"type":"text","text":text}]}})
    p=subprocess.run(["claude","-p","--model",model,"--system-prompt","Reply with the single word OK.","--tools","Read","--input-format","stream-json","--output-format","stream-json","--verbose"],input=msg+"\n",capture_output=True,text=True,timeout=300)
    for line in p.stdout.splitlines():
        try:o=json.loads(line)
        except:continue
        if o.get("type")=="result":
            u=o["usage"];return u["input_tokens"]+u.get("cache_creation_input_tokens",0)+u.get("cache_read_input_tokens",0)
    return None
m=sys.argv[1];files=json.load(open('files.json'))
base=run(m,".");out={"base":base}
for k,v in files.items(): out[k]=run(m,v)-base
json.dump(out,open(f'claude_{m}.json','w'),indent=1)
