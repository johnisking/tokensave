// TokenSave — AI coding agent cost page (tokensave.app/agents)
// Estimates the monthly API cost of coding agents (Claude Code, Codex, Gemini CLI…) and compares it with plans.
// An agent re-sends its whole working context on every step, so input tokens grow with each step.
// Plan prices: official US monthly prices, checked 2026-10-01 (Claude Pro/Max include Claude Code,
// ChatGPT Plus/Pro include Codex). API prices come from src/llm_prices.json, injected by build.py as T.prices.

import { T, tr } from './common.js';

const PRICES = T.prices || {};
const CACHE_RATE = 0.1;   // cached input billed at ~10% of the normal input price
const CTX_CAP = 180000;   // agents compact their context before it grows past this

// Per task: steps, starting context (system prompt + tools + first files), context added per step, output per step
const SIZES = {
  small:   { steps: 8,  start: 18000, grow: 2500, out: 500 },
  feature: { steps: 25, start: 22000, grow: 3500, out: 700 },
  big:     { steps: 60, start: 25000, grow: 4000, out: 900 },
};

const GROUPS = [
  { name: 'Claude', tool: 'Claude Code', main: 'claude-sonnet-5-5',
    models: [['claude-sonnet-5-5', 'Claude Sonnet 5.5'], ['claude-opus-5-5', 'Claude Opus 5.5'], ['claude-haiku-4-5', 'Claude Haiku 4.5']],
    plans: [['Claude Pro', 20], ['Claude Max 5×', 100], ['Claude Max 20×', 200]] },
  { name: 'OpenAI', tool: 'Codex', main: 'gpt-6-sol',
    models: [['gpt-6-sol', 'GPT-6 Sol'], ['gpt-6-astra', 'GPT-6 Astra'], ['gpt-6-luna', 'GPT-6 Luna']],
    plans: [['ChatGPT Plus', 20], ['ChatGPT Pro 100', 100], ['ChatGPT Pro 200', 200], ['ChatGPT Pro 500', 500]] },
  { name: 'Gemini · DeepSeek · Grok', tool: 'Gemini CLI · Cline · Aider', main: 'gemini-3-1-pro',
    models: [['gemini-3-1-pro', 'Gemini 3.1 Pro'], ['gemini-3-8-flash', 'Gemini 3.8 Flash'], ['deepseek-v4-pro', 'DeepSeek V4 Pro'], ['grok-code-fast-1', 'Grok Code Fast 1']],
    plans: [] },
];

const $ = id => document.getElementById(id);
const els = { tasks: $('aTasks'), tasksNum: $('aTasksNum'), days: $('aDays'), daysVal: $('aDaysVal'),
  tokIn: $('aTokIn'), tokOut: $('aTokOut'), cards: $('aCards') };
const state = { size: 'feature', cache: true };

const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const planMoney = n => Number.isInteger(n) ? '$' + n.toLocaleString('en-US') : '$' + n.toFixed(2);
const money = n => '$' + (n >= 100 ? Math.round(n).toLocaleString('en-US') : n >= 1 ? n.toFixed(2) : n.toFixed(3));
const big = n => n >= 1e9 ? (n / 1e9).toFixed(2) + 'B' : n >= 1e6 ? (n / 1e6).toFixed(1) + 'M' : n >= 1e3 ? Math.round(n / 1e3) + 'K' : String(Math.round(n));

// Tokens for one task: full input, the part that would be read from cache, and output
function perTask() {
  const z = SIZES[state.size];
  let input = 0, fresh = 0;
  for (let k = 0; k < z.steps; k++) {
    const ctx = Math.min(z.start + z.grow * k, CTX_CAP);
    input += ctx;
    fresh += k === 0 ? z.start : z.grow + z.out;   // new tokens this step; the rest is the cached prefix
  }
  fresh = Math.min(fresh, input);
  return { input, fresh, cached: input - fresh, out: z.steps * z.out };
}

function taskCost(id, t) {
  const p = PRICES[id] || { in: 0, out: 0 };
  const billedIn = state.cache ? t.fresh + t.cached * CACHE_RATE : t.input;
  return (billedIn / 1e6) * p.in + (t.out / 1e6) * p.out;
}

function render() {
  els.daysVal.textContent = els.days.value;
  const tasks = Math.max(1, Math.min(500, Math.round(+els.tasksNum.value || 1)));
  const n = tasks * +els.days.value;
  const t = perTask();
  els.tokIn.textContent = big(t.input * n);
  els.tokOut.textContent = big(t.out * n);

  els.cards.innerHTML = GROUPS.map(g => {
    const rows = g.models.map(([id, name]) => ({ id, name, task: taskCost(id, t), month: taskCost(id, t) * n }));
    const main = rows.find(r => r.id === g.main) || rows[0];
    const row = (label, value, sub, strong, dim) => `<li class="flex items-center justify-between gap-3 py-2 ${dim ? 'text-zinc-500' : ''}">
        <span class="min-w-0 text-sm ${strong ? 'font-semibold text-zinc-100' : ''}">${label}${sub ? `<span class="block text-[11px] text-zinc-500 font-normal">${sub}</span>` : ''}</span>
        <span class="ltr tabular-nums whitespace-nowrap shrink-0 ${strong ? 'text-lg font-bold' : 'text-sm'}">${value}<span class="text-[11px] text-zinc-500"> ${esc(tr('perMonth'))}</span></span></li>`;
    // Largest plan priced below the API cost = the plan worth comparing against
    const below = g.plans.filter(([, price]) => price < main.month).pop();
    let verdict = '';
    if (g.plans.length) {
      verdict = below
        ? `<p class="mt-4 rounded-xl px-3 py-2.5 text-sm font-semibold bg-emerald-500/10 text-emerald-200 border border-emerald-500/30">${esc(tr('planCheaper', { plan: below[0], price: planMoney(below[1]), d: money(main.month - below[1]), api: money(main.month) }))}</p>`
        : `<p class="mt-4 rounded-xl px-3 py-2.5 text-sm font-semibold bg-sky-500/10 text-sky-200 border border-sky-500/30">${esc(tr('apiCheaper', { api: money(main.month), plan: g.plans[0][0], price: planMoney(g.plans[0][1]) }))}</p>`;
      verdict += `<p class="mt-1.5 text-[11px] text-zinc-500 ltr">${esc(main.name)} · ${esc(g.tool)}</p>`;
    }
    return `<article class="bg-zinc-900/70 backdrop-blur border border-zinc-800 rounded-2xl p-5 flex flex-col">
      <h2 class="text-lg font-bold">${esc(g.name)} <span class="text-xs font-normal text-zinc-500 ltr">${esc(g.tool)}</span></h2>
      <ul class="mt-2 divide-y divide-zinc-800/80">
        ${rows.map(r => row(`<span class="text-[11px] font-bold px-1.5 py-0.5 rounded bg-sky-500/15 text-sky-300 me-1.5">${esc(tr('apiLabel'))}</span><span class="ltr inline-block">${esc(r.name)}</span>`,
          money(r.month), esc(tr('perTask', { c: money(r.task) })), r === main)).join('')}
        ${g.plans.map(([name, price]) => row(`<span class="ltr inline-block">${esc(name)}</span>`, planMoney(price), '', below && below[0] === name, !(below && below[0] === name))).join('')}
      </ul>
      ${verdict}
    </article>`;
  }).join('');
}

// Events
els.tasks.addEventListener('input', () => { els.tasksNum.value = els.tasks.value; render(); });
els.tasksNum.addEventListener('input', () => { els.tasks.value = Math.min(60, +els.tasksNum.value || 1); render(); });
document.querySelectorAll('#aTaskPresets button').forEach(b => b.addEventListener('click', () => {
  els.tasks.value = els.tasksNum.value = b.dataset.n; render();
}));
const bind = (sel, key, parse) => {
  const btns = document.querySelectorAll(sel + ' button');
  btns.forEach(b => b.addEventListener('click', () => {
    state[key] = parse(b.dataset.v);
    btns.forEach(x => x.classList.toggle('tab-active', x === b));
    render();
  }));
  btns.forEach(x => x.classList.toggle('tab-active', parse(x.dataset.v) === state[key]));
};
bind('#aSize', 'size', v => v);
bind('#aCache', 'cache', v => v === '1');
els.days.addEventListener('input', render);
render();
