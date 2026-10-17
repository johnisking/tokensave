import math,json
def fit(w,h,maxdim):
    s=min(1,maxdim/max(w,h)); return (int(w*s),int(h*s)) if s<1 else (w,h)
def patches(w,h): return math.ceil(w/32)*math.ceil(h/32)
def budget(w,h,b):
    if patches(w,h)<=b: return patches(w,h)
    sf=math.sqrt(32**2*b/(w*h))
    adj=sf*min(math.floor(w*sf/32)/(w*sf/32), math.floor(h*sf/32)/(h*sf/32))
    return patches(int(w*adj),int(h*adj))
def gpt6_auto(w,h): w,h=fit(w,h,65535); return math.ceil(patches(w,h)*1.2)
def gpt6_high(w,h): w,h=fit(w,h,65535); return math.ceil(budget(w,h,2500)*1.2)
def gpt55_auto(w,h): w,h=fit(w,h,6000); return math.ceil(budget(w,h,10000)*1.2)
sizes=[(256,256),(512,512),(768,768),(1024,1024),(1280,720),(1920,1080),(1080,1920),(2560,1440),(3840,2160),(4032,3024)]
out={f"{w}x{h}":{"gpt6_auto":gpt6_auto(w,h),"gpt6_high":gpt6_high(w,h),"gpt55_auto":gpt55_auto(w,h)} for w,h in sizes}
# sanity vs doc examples
assert gpt6_high(1024,1024)==1229 and gpt6_high(2048,2048)==3000 and gpt6_high(4096,512)==2458
json.dump(out,open('gpt.json','w'),indent=1); print(json.dumps(out))
