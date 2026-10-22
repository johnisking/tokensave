"""Prototype snapshot slimmer: keeps refs (needed to click) and visible text, drops noise."""
import re,sys
def slim(t):
    out=[]
    for l in t.split('\n'):
        s=l.strip()
        if s.startswith('- /url:'): continue                      # link targets
        l=l.replace(' [cursor=pointer]','')
        if re.fullmatch(r'\s*- generic \[ref=e\d+\]:?',l): continue  # empty wrappers
        if re.fullmatch(r'\s*- (img|separator|generic) \[ref=e\d+\]',l): continue
        out.append(l)
    # de-indent: 2 spaces -> 1
    out=[re.sub(r'^( +)',lambda m:' '*(len(m.group(1))//2),l) for l in out]
    return '\n'.join(out)
if __name__=='__main__':
    for f in sys.argv[1:]:
        open(f.replace('.txt','.slim.txt'),'w').write(slim(open(f,encoding='utf-8').read()))

def outline(t, maxlen=60):
    """Outline mode: headings and interactive elements only, text cut short; full text on request."""
    keep=re.compile(r'\b(heading|button|textbox|searchbox|combobox|checkbox|radio|link|tab|menuitem|option)\b')
    out=[]
    for l in t.split('\n'):
        if not keep.search(l): continue
        l=re.sub(r' url="[^"]*"','',l); l=re.sub(r' description="[^"]*"','',l); l=l.replace(' [cursor=pointer]','')
        l=re.sub(r'"([^"]{%d})[^"]*"'%maxlen, r'"\1…"', l)
        out.append(l.strip())
    return '\n'.join(out)
