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
// Pages that exist in several languages (blog posts, game calculator...) list their translations as
// hreflang links: point the switcher at the same page in the other language instead of that language's home.
if (langSelect) {
  const alt = {};
  document.querySelectorAll('link[rel="alternate"][hreflang]').forEach(l => {
    const code = l.getAttribute('hreflang').toLowerCase();
    if (code === 'x-default') return;
    try { const u = new URL(l.href, location.href); if (u.hostname === location.hostname || u.hostname === 'tokensave.app') alt[code] = u.pathname; } catch (_) {}
  });
  if (Object.keys(alt).length) {
    [...langSelect.options].forEach(o => { const c = o.dataset.code; if (c && alt[c]) o.value = alt[c]; });
    try { const all = JSON.parse(langSelect.dataset.all || '{}'); Object.assign(all, alt); langSelect.dataset.all = JSON.stringify(all); } catch (_) {}
  }
}
if (langSelect) {
  // Language switcher — remembers the choice
  langSelect.addEventListener('change', e => {
    const opt = e.target.selectedOptions[0];
    if (opt.dataset.code) store.set(opt.dataset.code);
    location.href = opt.value;
  });

}

if (langSelect && !T.static) {
  // The menu shows only the main languages; data-all has the URL of every language page
  let all = {};
  try { all = JSON.parse(langSelect.dataset.all || '{}'); } catch (_) {}
  const here = (langSelect.selectedOptions[0] || {}).dataset?.code || 'en';
  const optFor = code => all[code] && { value: all[code] };
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

// ---- Local currency by page language -------------------------------------------------
// API and plan prices are set in USD; we show an approximate conversion ("≈") in the visitor's
// currency. Rates: ExchangeRate-API (open.er-api.com), 2026-10-09 00:02 UTC — refresh with the weekly price check.
export const FX_DATE = '2026-10-09';
const FX = { KRW: 1342.34, JPY: 158.03, EUR: 0.8923, GBP: 0.7565, AUD: 1.4379, CAD: 1.4231, NZD: 1.7855,
  PLN: 3.9086, SEK: 9.988, BRL: 5.018, CNY: 6.715, TWD: 31.96, RUB: 85.43, UAH: 44.85, CZK: 21.79,
  HUF: 326.7, RON: 4.779, DKK: 6.680, NOK: 9.567, TRY: 49.28, ILS: 3.068, INR: 96.88, BDT: 123.0,
  PKR: 277.0, IDR: 17892, VND: 25868, THB: 33.67 };
const LANG_CUR = { ko: 'KRW', ja: 'JPY', de: 'EUR', fr: 'EUR', es: 'EUR', nl: 'EUR', it: 'EUR', el: 'EUR',
  fi: 'EUR', sk: 'EUR', pl: 'PLN', sv: 'SEK', pt: 'BRL', 'zh-cn': 'CNY', 'zh-tw': 'TWD', ru: 'RUB',
  uk: 'UAH', cs: 'CZK', hu: 'HUF', ro: 'RON', da: 'DKK', no: 'NOK', tr: 'TRY', he: 'ILS', hi: 'INR',
  gu: 'INR', kn: 'INR', ml: 'INR', mr: 'INR', pa: 'INR', ta: 'INR', te: 'INR', bn: 'BDT', ur: 'PKR',
  id: 'IDR', vi: 'VND', th: 'THB' };
// English (and Portuguese) pages serve several countries: use the browser's region.
const REGION_CUR = { 'en-gb': 'GBP', 'en-au': 'AUD', 'en-ca': 'CAD', 'en-nz': 'NZD', 'en-in': 'INR',
  'en-ie': 'EUR', 'pt-pt': 'EUR' };
const curStore = {
  get() { try { return localStorage.getItem('ts_cur'); } catch (_) { return null; } },
  set(v) { try { v ? localStorage.setItem('ts_cur', v) : localStorage.removeItem('ts_cur'); } catch (_) {} },
};
const pageLang = (document.documentElement.lang || 'en').toLowerCase();
const browserLang = ((navigator.languages && navigator.languages[0]) || navigator.language || '').toLowerCase();
const localCode = (pageLang === 'en' || pageLang === 'pt') ? (REGION_CUR[browserLang] || LANG_CUR[pageLang] || null) : (LANG_CUR[pageLang] || null);
const numLocale = pageLang === 'en' ? 'en-US' : document.documentElement.lang;
export const LC = localCode && FX[localCode] && curStore.get() !== 'USD' ? { code: localCode, rate: FX[localCode], locale: numLocale } : null;

// Format a USD amount in the local currency; falls back to the USD string the caller already built.
export function fx(n, usdStr) {
  if (!LC || !isFinite(n)) return usdStr;
  const v = n * LC.rate, a = Math.abs(v);
  const opt = { style: 'currency', currency: LC.code };
  if (a === 0) Object.assign(opt, { maximumFractionDigits: 0 });
  else if (a < 1) Object.assign(opt, { maximumSignificantDigits: 3 });
  else if (a < 100) { let d = 2; try { d = Math.min(2, new Intl.NumberFormat(LC.locale, opt).resolvedOptions().maximumFractionDigits); } catch (_) {} Object.assign(opt, { minimumFractionDigits: 0, maximumFractionDigits: d }); }
  else Object.assign(opt, { maximumFractionDigits: 0 });
  try { return '≈' + new Intl.NumberFormat(LC.locale, opt).format(v); } catch (_) { return usdStr; }
}

// Small switch under the page title: local currency <-> USD.
if (localCode && FX[localCode] && document.body.dataset.fx !== 'off') {
  const h1 = document.querySelector('main h1');
  if (h1 && document.querySelector('script[type="module"][src*="token"],script[type="module"][src*="image"],script[type="module"][src*="video"],script[type="module"][src*="agents"]')) {
    const rate = new Intl.NumberFormat(numLocale, { maximumFractionDigits: FX[localCode] >= 100 ? 0 : 2 }).format(FX[localCode]);
    const chip = document.createElement('div');
    chip.className = 'mt-3 inline-flex flex-wrap items-center gap-2 text-xs text-zinc-400';
    chip.innerHTML = `<span></span><button type="button" class="rounded-md border border-zinc-700 px-2 py-0.5 text-zinc-200 hover:border-violet-400 hover:text-white"></button>`;
    chip.querySelector('span').textContent = `1 USD ≈ ${rate} ${localCode} · ${FX_DATE}`;
    const btn = chip.querySelector('button');
    btn.textContent = LC ? 'USD' : localCode;
    btn.addEventListener('click', () => { curStore.set(LC ? 'USD' : null); location.reload(); });
    h1.insertAdjacentElement('afterend', chip);
  }
}
