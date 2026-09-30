# usage: python3 check.py tag [tag...]   (run from src/i18n_plans)
import sys, re, importlib.util, os
D = os.path.dirname(os.path.abspath(__file__))
def load(t):
    s = importlib.util.spec_from_file_location("p_" + t.replace("-", "_"), os.path.join(D, t + ".py")); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
en = load("en"); PH = re.compile(r"\{[a-z]+\}")
for t in sys.argv[1:]:
    m = load(t); err = []
    if set(m.P) != set(en.P): err.append(f"keys differ: missing {set(en.P)-set(m.P)} extra {set(m.P)-set(en.P)}")
    for k in en.P:
        if k in m.P and sorted(PH.findall(m.P[k])) != sorted(PH.findall(en.P[k])): err.append(f"{k}: placeholders {PH.findall(m.P[k])} != {PH.findall(en.P[k])}")
    if len(m.META[0]) > 40: err.append(f"META title {len(m.META[0])}>40")
    if len(m.META[1]) > 80: err.append(f"META desc {len(m.META[1])}>80")
    if not m.NAV or len(m.NAV) > 16: err.append(f"NAV too long ({len(m.NAV)} chars, max 16)")
    print(t, "OK" if not err else err)
