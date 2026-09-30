# -*- coding: utf-8 -*-
"""Strings for the 7 Indian languages added on 2026-10-01 (mr, gu, kn, ml, ta, te, pa).
Each src/i18n_in7/<tag>.py defines B (budget/chat UI), F (measured fact), TR (Save-tokens button, in
i18n_eu7._TR_KEYS order) and T (blog article strings, merged into blog_data/strings.py)."""
import importlib.util, os
from i18n_eu7 import _TR_KEYS

ORDER = ["mr", "gu", "kn", "ml", "ta", "te", "pa"]
_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "i18n_in7")
B_IN, F_IN, TR_IN, T_IN = {}, {}, {}, {}
for _t in ORDER:
    _s = importlib.util.spec_from_file_location("i18n_in7_" + _t, os.path.join(_DIR, _t + ".py"))
    _m = importlib.util.module_from_spec(_s)
    _s.loader.exec_module(_m)
    assert len(_m.TR) == len(_TR_KEYS), _t
    B_IN[_t], F_IN[_t], TR_IN[_t], T_IN[_t] = _m.B, _m.F, dict(zip(_TR_KEYS, _m.TR)), _m.T
