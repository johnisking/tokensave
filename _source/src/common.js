// Shared by every TokenSave page: translated strings + language switcher.
// UI strings come from window.T, injected into each language page by build.py.

export const T = window.T || {};
export const tr = (key, vars = {}) =>
  (T[key] || key).replace(/\{(\w+)\}/g, (_, k) => (k in vars ? vars[k] : ''));

// Language switcher — remembers the choice so the English pages stop auto-redirecting
const langSelect = document.getElementById('langSelect');
if (langSelect) {
  langSelect.addEventListener('change', e => {
    const opt = e.target.selectedOptions[0];
    try { localStorage.setItem('ts_lang', opt.dataset.code); } catch (_) {}
    location.href = opt.value;
  });
}
