import json,subprocess,base64,sys
def run(model,img=None):
    content=[]
    if img:
        content.append({"type":"image","source":{"type":"base64","media_type":"image/png","data":base64.b64encode(open(img,'rb').read()).decode()}})
    content.append({"type":"text","text":"."})
    msg=json.dumps({"type":"user","message":{"role":"user","content":content}})
    p=subprocess.run(["claude","-p","--model",model,"--system-prompt","Reply with the single word OK.","--tools","Read","--input-format","stream-json","--output-format","stream-json","--verbose"],input=msg+"\n",capture_output=True,text=True,timeout=300)
    for line in p.stdout.splitlines():
        try: o=json.loads(line)
        except: continue
        if o.get("type")=="result":
            u=o["usage"]; return u["input_tokens"]+u.get("cache_creation_input_tokens",0)+u.get("cache_read_input_tokens",0)
    return ("ERR",p.stdout[-500:],p.stderr[-500:])
if __name__=="__main__":
    m=sys.argv[1]; imgs=sys.argv[2:]
    base=run(m); out={"base":base}
    for i in imgs: out[i]=run(m,i)
    print(json.dumps(out))
