import json,statistics as st,sys
R=json.load(open(sys.argv[1]))
from collections import defaultdict
g=defaultdict(list)
for r in R: g[(r['mode'],r['task'])].append(r)
for (mo,t),rs in g.items():
    m=lambda k: st.mean(r[k] for r in rs)
    print(f"{mo} {t:6} n={len(rs)} in={m('input_tokens'):,.0f} out={m('output_tokens'):,.0f} cost=${m('api_cost_usd'):.3f} req={m('requests'):.1f} maxtext={max(r['max_text_result_chars'] for r in rs):,} imgs={m('images'):.1f} imgtok={m('image_tokens_est'):,.0f} up={m('user_prompt_chars'):.0f} refused={sum(r['refused_too_large'] for r in rs)} err={sum(r['tool_errors'] for r in rs)}")
    if '-v' in sys.argv:
        for r in rs: print('    ',r['rep'],r['input_tokens'],r['api_cost_usd'],r['max_text_result_chars'],r['calls'][:14],r['image_sizes'][:4],repr(r['answer'][:80]))
