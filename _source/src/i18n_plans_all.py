# -*- coding: utf-8 -*-
"""Loads the Subscription-vs-API page strings from i18n_plans/<tag>.py (one file per language)."""
import importlib.util, os
_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "i18n_plans")
PL, PNAV, PMETA = {}, {}, {}
for _f in sorted(os.listdir(_DIR)):
    if not _f.endswith(".py") or _f == "check.py":
        continue
    _t = _f[:-3]
    _s = importlib.util.spec_from_file_location("i18n_plans_" + _t.replace("-", "_"), os.path.join(_DIR, _f))
    _m = importlib.util.module_from_spec(_s)
    _s.loader.exec_module(_m)
    PL[_t], PNAV[_t], PMETA[_t] = _m.P, _m.NAV, _m.META
