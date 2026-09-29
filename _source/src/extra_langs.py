# Loads the extra language files in i18n_extra/*.py (one file per language) in a fixed order.
import importlib.util, os
ORDER = ["bn", "ur", "fil", "cs", "sv", "he"]
_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "i18n_extra")
EXTRA = []
for _name in ORDER:
    _path = os.path.join(_DIR, _name + ".py")
    if os.path.exists(_path):
        _spec = importlib.util.spec_from_file_location("i18n_extra_" + _name.replace("-", "_"), _path)
        _mod = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_mod)
        EXTRA.append(_mod)
