// TokenSave — AI Token Counter page (tokensave.app)
// 100% client-side. The text you type never leaves the browser.
// UI strings come from window.T (injected per language page).
// Prices: USD per 1M tokens (standard tier, short context). Last checked: 2026-09-29.

import { tr } from './common.js';

// =========================================================
// 1) MODEL CONFIG
//    ratio: multiplier applied to the heuristic estimate
//    exact: true when o200k is the model's real tokenizer
// =========================================================
const PROVIDERS = {
  openai: [
    { id: 'gpt-6-astra', name: 'GPT-6 Astra', in: 10.00, out: 50.00, ratio: 1.00, exact: false },
    { id: 'gpt-6-sol',   name: 'GPT-6 Sol',   in: 2.00,  out: 10.00, ratio: 1.00, exact: false },
    { id: 'gpt-6-luna',  name: 'GPT-6 Luna',  in: 0.10,  out: 0.50,  ratio: 1.00, exact: false },
    { id: 'gpt-4o',      name: 'GPT-4o',      in: 2.50,  out: 10.00, ratio: 1.00, exact: true  },
  ],
  claude: [
    // Claude 4.7+ uses a newer tokenizer (~30% more tokens for the same text)
    { id: 'claude-opus-5-5',   name: 'Claude Opus 5.5',   in: 4.00, out: 20.00, ratio: 1.30 },
    { id: 'claude-sonnet-5-5', name: 'Claude Sonnet 5.5', in: 2.00, out: 10.00, ratio: 1.30 },
    { id: 'claude-haiku-4-5',  name: 'Claude Haiku 4.5',  in: 1.00, out: 5.00,  ratio: 1.05 },
  ],
  gemini: [
    { id: 'gemini-3-1-pro',   name: 'Gemini 3.1 Pro',   in: 2.00, out: 12.00, ratio: 0.95 },
    { id: 'gemini-3-8-flash', name: 'Gemini 3.8 Flash', in: 0.75, out: 3.75,  ratio: 0.95 },
  ],
};
let provider = 'openai';
let model = PROVIDERS.openai[0];
let enc = null;

// =========================================================
// 2) Load o200k tokenizer from CDN (non-blocking; heuristic until ready)
// =========================================================
(async () => {
  try {
    const mod = await import('https://cdn.jsdelivr.net/npm/js-tiktoken@1/+esm');
    enc = mod.getEncoding('o200k_base');
    update();
  } catch (e) {
    console.warn('js-tiktoken failed to load, using heuristic.', e);
  }
})();

// =========================================================
// 3) Heuristic tokenizer (weighted by script)
// =========================================================
const RE = {
  hangul:   /[가-힯ᄀ-ᇿ㄰-㆏]/,
  kana:     /[぀-ヿㇰ-ㇿ]/,
  cjk:      /[一-鿿㐀-䶿]/,
  cyrillic: /[Ѐ-ӿ]/,
  arabic:   /[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]/,
  thai:     /[฀-๿]/,
  devan:    /[ऀ-ॿ]/,
  emoji:    /\p{Extended_Pictographic}/u,
};
const WEIGHT = { hangul: 2.0, kana: 1.6, cjk: 1.8, cyrillic: 0.55, arabic: 0.6, thai: 0.9, devan: 1.1, emoji: 2.5 };

function analyze(text) {
  const counts = { hangul: 0, kana: 0, cjk: 0, cyrillic: 0, arabic: 0, thai: 0, devan: 0, emoji: 0 };
  let latinBuf = '', latinTokens = 0, symbolTokens = 0;
  const flushLatin = () => {
    if (!latinBuf) return;
    const words = latinBuf.match(/[A-Za-zÀ-ɏ']+/g) || [];
    const nums  = latinBuf.match(/\d+/g) || [];
    latinTokens += words.reduce((s, w) => s + Math.max(1, Math.round(w.length / 4.5 * 1.1 + 0.3)), 0);
    latinTokens += nums.reduce((s, n) => s + Math.ceil(n.length / 3), 0);
    symbolTokens += (latinBuf.match(/[^\sA-Za-zÀ-ɏ'\d]/g) || []).length * 0.8;
    // Whitespace: each line break run and each run of 2+ spaces/tabs is roughly one token
    symbolTokens += (latinBuf.match(/\n+/g) || []).length + (latinBuf.match(/[ \t 　]{2,}/g) || []).length;
    latinBuf = '';
  };
  for (const ch of text) {
    let hit = null;
    for (const k in RE) { if (RE[k].test(ch)) { hit = k; break; } }
    if (hit) { flushLatin(); counts[hit]++; } else latinBuf += ch;
  }
  flushLatin();
  let scriptTokens = 0;
  for (const k in WEIGHT) scriptTokens += counts[k] * WEIGHT[k];
  const nonLatinChars = Object.keys(WEIGHT).reduce((s, k) => s + counts[k], 0);
  return { tokens: Math.round(latinTokens + symbolTokens + scriptTokens), counts, nonLatinChars };
}

// =========================================================
// 4) Language efficiency — token waste vs. English for the same meaning
// =========================================================
const PENALTY = { hangul: 2.4, kana: 2.1, cjk: 1.9, cyrillic: 1.8, arabic: 1.9, thai: 2.6, devan: 2.8, emoji: 1.0 };
function efficiency(a, text) {
  const nonSpace = (text.match(/\S/g) || []).length;
  if (!nonSpace || !a.nonLatinChars) return { waste: 1, pct: 100, share: 0 };
  let weighted = 0;
  for (const k in PENALTY) weighted += a.counts[k] * (PENALTY[k] - 1);
  const share = Math.min(1, a.nonLatinChars / nonSpace);
  const waste = 1 + (weighted / a.nonLatinChars) * share;
  return { waste, pct: Math.round(100 / waste), share };
}

// =========================================================
// 5) DOM + rendering
// =========================================================
const $ = id => document.getElementById(id);
const els = {
  input: $('input'), tokens: $('tokenCount'), chars: $('charCount'), words: $('wordCount'),
  costIn: $('costIn'), costOut: $('costOut'), priceNote: $('priceNote'), badge: $('methodBadge'),
  battery: $('battery'), effPct: $('effPercent'), effText: $('effText'), waste: $('wasteLabel'),
  mix: $('langMix'), toast: $('toast'), select: $('modelSelect'),
};

for (let i = 0; i < 10; i++) {
  const c = document.createElement('div');
  c.className = 'battery-cell rounded-sm bg-zinc-800';
  els.battery.appendChild(c);
}

const fmt = n => n.toLocaleString('en-US');
const money = n => '$' + (n < 0.01 ? n.toFixed(6) : n.toFixed(4));

function countTokens(text) {
  const a = analyze(text);
  if (provider === 'openai' && enc) {
    try { return { tokens: enc.encode(text).length, exact: !!model.exact, based: true, a }; } catch (_) {}
  }
  return { tokens: Math.round(a.tokens * model.ratio), exact: false, based: false, a };
}

let raf = null;
function update() {
  if (raf) cancelAnimationFrame(raf);
  raf = requestAnimationFrame(render);
}

function render() {
  const text = els.input.value;
  const chars = [...text].length;
  const words = (text.trim().match(/\S+/g) || []).length;
  const { tokens, exact, based, a } = countTokens(text);

  els.tokens.textContent = fmt(tokens);
  els.chars.textContent = fmt(chars);
  els.words.textContent = fmt(words);
  els.costIn.textContent = money(tokens / 1e6 * model.in);
  els.costOut.textContent = money(tokens / 1e6 * model.out);
  els.priceNote.textContent = tr('note', { name: model.name, in: model.in, out: model.out });

  els.badge.textContent = exact ? tr('exact') : based ? tr('based') : tr('est');
  els.badge.className = 'text-[10px] font-semibold px-2 py-0.5 rounded-full ' +
    (exact ? 'bg-emerald-500/15 text-emerald-300' : based ? 'bg-sky-500/15 text-sky-300' : 'bg-zinc-800 text-zinc-400');

  const e = efficiency(a, text);
  const filled = Math.round(e.pct / 10);
  const tone = e.pct >= 80 ? 'emerald' : e.pct >= 55 ? 'amber' : 'rose';
  const fill = { emerald: 'bg-emerald-400', amber: 'bg-amber-400', rose: 'bg-rose-500' }[tone];
  [...els.battery.children].forEach((c, i) => {
    c.className = 'battery-cell rounded-sm ' + (i < filled ? fill : 'bg-zinc-800');
  });
  els.effPct.textContent = tr('efficient', { p: e.pct });
  els.effText.textContent = e.pct >= 80 ? tr('great') : e.pct >= 55 ? tr('moderate') : tr('high');
  els.waste.textContent = tr('waste', { x: e.waste.toFixed(1) });
  els.waste.className = 'text-xs font-bold ' + { emerald: 'text-emerald-400', amber: 'text-amber-400', rose: 'text-rose-400' }[tone];
  els.mix.textContent = tr('share', { p: Math.round(e.share * 100) });
}

function toast(msg) {
  els.toast.textContent = msg;
  els.toast.style.opacity = 1;
  clearTimeout(toast.t);
  toast.t = setTimeout(() => (els.toast.style.opacity = 0), 1800);
}

// =========================================================
// 6) Events
// =========================================================
function fillModels() {
  els.select.innerHTML = PROVIDERS[provider].map(m => `<option value="${m.id}">${m.name}</option>`).join('');
  model = PROVIDERS[provider][0];
}

els.input.addEventListener('input', update);

const tabs = document.querySelectorAll('#providerTabs .tab');
tabs.forEach(btn => btn.addEventListener('click', () => {
  provider = btn.dataset.provider;
  tabs.forEach(b => b.classList.toggle('tab-active', b === btn));
  fillModels();
  update();
}));

els.select.addEventListener('change', () => {
  model = PROVIDERS[provider].find(m => m.id === els.select.value);
  update();
});

tabs[0].click();

// Optimize: collapse repeated spaces/tabs, trim line edges, remove blank lines
$('btnOptimize').addEventListener('click', () => {
  const before = countTokens(els.input.value).tokens;
  els.input.value = els.input.value
    .replace(/\r\n/g, '\n')
    .replace(/[ \t 　]+/g, ' ')
    .replace(/ *\n */g, '\n')
    .replace(/\n{2,}/g, '\n')
    .trim();
  render();
  const saved = before - countTokens(els.input.value).tokens;
  toast(saved > 0 ? '✨ ' + tr('tSaved', { n: fmt(saved) }) : tr('tAlready'));
});

$('btnCopy').addEventListener('click', async () => {
  if (!els.input.value) return toast(tr('tNothing'));
  try { await navigator.clipboard.writeText(els.input.value); }
  catch { els.input.select(); document.execCommand('copy'); }
  toast(tr('tCopied'));
});

$('btnClear').addEventListener('click', () => {
  els.input.value = '';
  render();
  els.input.focus();
  toast(tr('tCleared'));
});

render();
