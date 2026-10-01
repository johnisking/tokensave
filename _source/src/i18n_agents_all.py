# -*- coding: utf-8 -*-
"""Coding agent cost page (/agents) strings for all 41 languages.
Shared labels (input/output/API/per month/tokens per month) are reused from the Subscription-vs-API page."""
from i18n_agents_a import A
from i18n_agents_b import B
from i18n_agents_c import C
from i18n_plans_all import PL
from i18n_crosslink import X

AG, AGNAV, AGMETA = {}, {}, {}
for _src in (A, B, C):
    for _t, _d in _src.items():
        _d = dict(_d)
        AGNAV[_t] = _d.pop("nav")
        AGMETA[_t] = (_d.pop("title"), _d.pop("desc"))
        for _k in ("tokMonth", "inTok", "outTok", "apiLabel", "perMonth"):
            _d[_k] = PL[_t][_k]
        AG[_t] = _d

for _t in AG:
    AG[_t]["toPlans"] = X[_t][1]
    PL[_t]["toAgents"] = X[_t][0]
