// Shared by every TokenSave page: translated strings, language switcher, language suggestion banner.
// UI strings come from window.T, injected into each language page by build.py.

export const T = window.T || {};
export const tr = (key, vars = {}) =>
  (T[key] || key).replace(/\{(\w+)\}/g, (_, k) => (k in vars ? vars[k] : ''));

const store = {
  get() { try { return localStorage.getItem('ts_lang'); } catch (_) { return null; } },
  set(v) { try { localStorage.setItem('ts_lang', v); } catch (_) {} },
};

const langSelect = document.getElementById('langSelect');
if (langSelect) {
  // Language switcher — remembers the choice
  langSelect.addEventListener('change', e => {
    const opt = e.target.selectedOptions[0];
    store.set(opt.dataset.code);
    location.href = opt.value;
  });

}

if (langSelect && !T.static) {
  const options = [...langSelect.options];
  const here = (langSelect.selectedOptions[0] || {}).dataset?.code || 'en';
  const optFor = code => options.find(o => o.dataset.code === code);
  const saved = store.get();

  if (saved) {
    // A language the visitor picked before: only English pages send them back to it.
    if (here === 'en' && saved !== 'en' && optFor(saved)) location.replace(optFor(saved).value);
  } else {
    // First visit: suggest (never force) the browser's language. Search engines always see the page as is.
    const l = ((navigator.languages && navigator.languages[0]) || navigator.language || '').toLowerCase();
    const base = l.split('-')[0];
    const ALIAS = { tl: 'fil', iw: 'he', nb: 'no', nn: 'no' };
    const key = base === 'zh' ? (/-(tw|hk|mo|hant)/.test(l) ? 'zh-tw' : 'zh-cn') : (ALIAS[base] || base);
    const target = key !== here && optFor(key);
    const label = target && (T.viewIn || {})[key];
    if (label) {
      const bar = document.createElement('div');
      bar.className = 'fixed inset-x-0 bottom-0 z-50 flex justify-center p-3 pointer-events-none';
      bar.innerHTML = `<div class="pointer-events-auto flex items-center gap-3 bg-zinc-900/95 backdrop-blur border border-violet-500/40 rounded-xl shadow-2xl ps-4 pe-2 py-2 text-sm">
        <span aria-hidden="true">🌐</span>
        <a class="font-semibold text-violet-200 hover:text-white" href="${target.value}"></a>
        <button type="button" class="w-7 h-7 rounded-lg text-zinc-400 hover:text-white hover:bg-zinc-800" aria-label="Close">✕</button>
      </div>`;
      const a = bar.querySelector('a');
      a.textContent = label;
      a.addEventListener('click', () => store.set(key));
      bar.querySelector('button').addEventListener('click', () => { store.set(here); bar.remove(); });
      document.body.appendChild(bar);
    }
  }
}
