import json, csv, io, yaml
from xml.sax.saxutils import escape
rows = [
 (1,"Wireless Mouse","Electronics",24.99,True,4.5,"office;wireless"),
 (2,"Mechanical Keyboard","Electronics",89.0,True,4.7,"office;gaming"),
 (3,"USB-C Hub","Electronics",34.5,False,4.2,"office;travel"),
 (4,"Desk Lamp","Home",42.0,True,4.4,"office;lighting"),
 (5,"Coffee Mug","Kitchen",12.99,True,4.8,"gift"),
 (6,"Notebook A5","Stationery",7.5,True,4.6,"office;school"),
 (7,"Water Bottle","Outdoor",19.95,False,4.3,"travel;sport"),
 (8,"Backpack","Outdoor",64.0,True,4.5,"travel;school"),
 (9,"Phone Stand","Electronics",15.0,True,4.1,"office"),
 (10,"Noise-Cancelling Headphones","Electronics",199.0,True,4.6,"travel;music"),
 (11,"Yoga Mat","Sport",29.99,True,4.4,"sport;home"),
 (12,"French Press","Kitchen",27.5,False,4.7,"coffee;gift"),
 (13,"LED Strip Lights","Home",22.0,True,4.0,"lighting;gaming"),
 (14,"Gel Pens (10 pack)","Stationery",9.99,True,4.5,"school;gift"),
 (15,"Portable Charger","Electronics",39.0,True,4.3,"travel"),
 (16,"Cast Iron Pan","Kitchen",45.0,True,4.8,"cooking"),
 (17,"Running Shoes","Sport",120.0,False,4.4,"sport;running"),
 (18,"Plant Pot","Home",14.5,True,4.2,"garden;gift"),
 (19,"Webcam 1080p","Electronics",59.0,True,4.1,"office;streaming"),
 (20,"Travel Pillow","Outdoor",18.0,True,4.0,"travel"),
]
keys=["id","name","category","price","in_stock","rating","tags"]
recs=[dict(id=r[0],name=r[1],category=r[2],price=r[3],in_stock=r[4],rating=r[5],tags=r[6].split(";")) for r in rows]
def flat(r): return [r["id"],r["name"],r["category"],r["price"],str(r["in_stock"]).lower(),r["rating"],";".join(r["tags"])]
out={}
out["json_pretty"]=json.dumps({"products":recs},indent=2)
out["json_minified"]=json.dumps({"products":recs},separators=(",",":"))
out["yaml"]=yaml.safe_dump({"products":recs},sort_keys=False,allow_unicode=True)
x=["<products>"]
for r in recs:
    x.append("  <product>")
    for k in keys:
        v=r[k]
        if k=="tags": x.append("    <tags>"+"".join(f"<tag>{escape(t)}</tag>" for t in v)+"</tags>")
        else: x.append(f"    <{k}>{escape(str(v).lower() if isinstance(v,bool) else str(v))}</{k}>")
    x.append("  </product>")
x.append("</products>")
out["xml"]="\n".join(x)
b=io.StringIO(); w=csv.writer(b,lineterminator="\n"); w.writerow(keys); [w.writerow(flat(r)) for r in recs]; out["csv"]=b.getvalue()
out["tsv"]="\t".join(keys)+"\n"+"\n".join("\t".join(map(str,flat(r))) for r in recs)+"\n"
md="| "+" | ".join(keys)+" |\n|"+"---|"*len(keys)+"\n"+"\n".join("| "+" | ".join(map(str,flat(r)))+" |" for r in recs)+"\n"
out["markdown_table"]=md
# TOON (token-oriented object notation) tabular form
def tq(s): s=str(s); return f'"{s}"' if ("," in s or ":" in s) else s
toon=f"products[{len(recs)}]{{{','.join(keys)}}}:\n"+"\n".join("  "+",".join(tq(c) for c in [r["id"],r["name"],r["category"],r["price"],str(r["in_stock"]).lower(),r["rating"],"|".join(r["tags"])]) for r in recs)+"\n"
out["toon"]=toon
json.dump(out,open("formats.json","w"),indent=1)
for k,v in out.items(): print(k,len(v),"chars")
print(out["toon"][:300])
