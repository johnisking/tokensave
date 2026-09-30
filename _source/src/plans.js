// TokenSave — Subscription vs API page (tokensave.app/plans)
// Estimates what your chat usage would cost on the API and compares it with the monthly plans.
// Plan prices: official US monthly prices, checked 2026-10-01:
//   ChatGPT  chatgpt.com/pricing           Go $8, Plus $20, Pro 100 $100, Pro 200 $200, Pro 500 $500
//   Claude   claude.com/pricing            Pro $20, Max 5x $100, Max 20x $200
//   Google   one.google.com/about/ai-premium  AI Plus $4.99, AI Pro $19.99, AI Ultra 5x $99.99, AI Ultra 20x $199.99
// API prices come from src/llm_prices.json (updated daily), injected by build.py as T.prices.

import { T, tr } from './common.js';

const PRICES = T.prices || {};
const LANGS = T.langs || [];           // [tag, native name, token ratio vs English]
const PAGE_TAG = T.pageTag || 'en';

// Tokens per message in English: [your message, reply]
const SIZES = { short: [60, 300], chat: [150, 500], long: [2000, 700] };

const PROVIDERS = [
  { name: 'ChatGPT', models: [['gpt-6-sol', 'GPT-6 Sol', 1.0], ['gpt-6-luna', 'GPT-6 Luna', 1.0]],
    plans: [['Go', 8], ['Plus', 20], ['Pro 100', 100], ['Pro 200', 200], ['Pro 500', 500]], main: 1 },
  { name: 'Claude', models: [['claude-sonnet-5-5', 'Claude Sonnet 5.5', 1.3], ['claude-haiku-4-5', 'Claude Haiku 4.5', 1.05]],
    plans: [['Pro', 20], ['Max 5×', 100], ['Max 20×', 200]], main: 0 },
  { name: 'Gemini', models: [['gemini-3-1-pro', 'Gemini 3.1 Pro', 0.95], ['gemini-3-8-flash', 'Gemini 3.8 Flash', 0.95]],
    plans: [['AI Plus', 4.99], ['AI Pro', 19.99], ['AI Ultra 5×', 99.99], ['AI Ultra 20×', 199.99]], main: 1, prefix: 'Google ' },
];

const $ = id => document.getElementById(id);
const els = { msgs: $('pMsgs'), msgsNum: $('pMsgsNum'), turns: $('pTurns'), turnsVal: $('pTurnsVal'),
  lang: $('pLang'), langNote: $('pLangNote'), tokIn: $('pTokIn'), tokOut: $('pTokOut'), cards: $('pCards') };
const state = { size: 'chat' };

const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const money = n => '$' + (n >= 100 ? Math.round(n).toLocaleString('en-US') : n >= 1 ? n.toFixed(2) : n.toFixed(3));
const planMoney = n => Number.isInteger(n) ? money(n) : '$' + n.toFixed(2);
const big = n => n >= 1e9 ? (n / 1e9).toFixed(2) + 'B' : n >= 1e6 ? (n / 1e6).toFixed(1) + 'M' : n >= 1e3 ? Math.round(n / 1e3) + 'K' : String(Math.round(n));

// Language menu: every site language with its measured ratio
els.lang.innerHTML = LANGS.map(([tag, name, r]) => `<option value="${tag}"${tag === PAGE_TAG ? ' selected' : ''}>${esc(name)} · ${r.toFixed(2)}×</option>`).join('');

// A chat model re-reads the whole conversation on every message:
// message k sends k of your messages and k-1 replies as input.
function monthlyTokens() {
  const perDay = Math.max(1, Math.min(2000, Math.round(+els.msgsNum.value || 1)));
  const turns = +els.turns.value;
  const ratio = (LANGS.find(l => l[0] === els.lang.value) || [0, '', 1])[2];
  const [p, r] = SIZES[state.size].map(x => x * ratio);
  const inPerChat = p * turns * (turns + 1) / 2 + r * turns * (turns - 1) / 2;
  const outPerChat = r * turns;
  const chats = perDay * 30 / turns;
  return { perDay, ratio, tin: inPerChat * chats, tout: outPerChat * chats };
}

function render() {
  els.turnsVal.textContent = els.turns.value;
  const { perDay, ratio, tin, tout } = monthlyTokens();
  els.tokIn.textContent = big(tin);
  els.tokOut.textContent = big(tout);
  const langName = (LANGS.find(l => l[0] === els.lang.value) || [0, ''])[1];
  els.langNote.textContent = ratio > 1.05 ? tr('langNote', { lang: langName, x: ratio.toFixed(2) }) : '';

  els.cards.innerHTML = PROVIDERS.map(pv => {
    const api = pv.models.map(([id, name, tokRatio]) => {
      const pr = PRICES[id] || { in: 0, out: 0 };
      return { name, cost: (tin * tokRatio / 1e6) * pr.in + (tout * tokRatio / 1e6) * pr.out };
    });
    const [planName, planPrice] = pv.plans[pv.main];
    const fullPlan = (pv.prefix || pv.name + ' ') + planName;
    const main = api[0].cost, diff = Math.abs(planPrice - main);
    const apiWins = main < planPrice;
    const breakEven = main > 0 ? Math.max(1, Math.round(planPrice / (main / perDay))) : 0;
    const row = (label, value, strong, dim) => `<li class="flex items-center justify-between gap-3 py-2 ${dim ? 'text-zinc-500' : ''}">
        <span class="min-w-0 text-sm ${strong ? 'font-semibold text-zinc-100' : ''}">${label}</span>
        <span class="ltr tabular-nums whitespace-nowrap shrink-0 ${strong ? 'text-lg font-bold' : 'text-sm'}">${value}<span class="text-[11px] text-zinc-500"> ${esc(tr('perMonth'))}</span></span></li>`;
    return `<article class="bg-zinc-900/70 backdrop-blur border border-zinc-800 rounded-2xl p-5 flex flex-col">
      <h2 class="text-lg font-bold">${esc(pv.name)}</h2>
      <ul class="mt-2 divide-y divide-zinc-800/80">
        ${api.map((a, i) => row(`<span class="text-[11px] font-bold px-1.5 py-0.5 rounded bg-sky-500/15 text-sky-300 me-1.5">${esc(tr('apiLabel'))}</span><span class="ltr inline-block">${esc(a.name)}</span>`, money(a.cost), i === 0)).join('')}
        ${pv.plans.map(([n, price], i) => row(`<span class="ltr inline-block">${esc((pv.prefix || pv.name + ' ') + n)}</span>`, planMoney(price), i === pv.main, i !== pv.main)).join('')}
      </ul>
      <p class="mt-4 rounded-xl px-3 py-2.5 text-sm font-semibold ${apiWins ? 'bg-sky-500/10 text-sky-200 border border-sky-500/30' : 'bg-emerald-500/10 text-emerald-200 border border-emerald-500/30'}">
        ${esc(apiWins ? tr('cheaperApi', { d: money(diff) }) : tr('cheaperPlan', { plan: fullPlan, d: money(diff) }))}
        <span class="block text-[11px] font-normal text-zinc-400 mt-1">${api[0].name} vs ${esc(fullPlan)}</span>
      </p>
      ${breakEven ? `<p class="mt-2 text-[11px] text-zinc-500">${esc(tr('breakEven', { plan: fullPlan, n: breakEven.toLocaleString('en-US') }))}</p>` : ''}
    </article>`;
  }).join('');
}

// Events
els.msgs.addEventListener('input', () => { els.msgsNum.value = els.msgs.value; render(); });
els.msgsNum.addEventListener('input', () => { els.msgs.value = Math.min(300, +els.msgsNum.value || 1); render(); });
document.querySelectorAll('#pMsgPresets button').forEach(b => b.addEventListener('click', () => {
  els.msgs.value = els.msgsNum.value = b.dataset.n; render();
}));
const sizeBtns = document.querySelectorAll('#pSize button');
sizeBtns.forEach(b => b.addEventListener('click', () => {
  state.size = b.dataset.size;
  sizeBtns.forEach(x => x.classList.toggle('tab-active', x === b));
  render();
}));
sizeBtns.forEach(x => x.classList.toggle('tab-active', x.dataset.size === state.size));
els.turns.addEventListener('input', render);
els.lang.addEventListener('change', render);
render();
