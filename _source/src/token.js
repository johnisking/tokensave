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
    { id: 'gpt-6-1-sol', name: 'GPT-6.1 Sol', in: 2.00,  out: 10.00, ratio: 1.00, exact: false },
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
// Latest prices from src/llm_prices.json (refreshed daily by GitHub Actions), injected by build.py
const LIVE = (window.T && window.T.prices) || {};
const PAGE_LANG = { 'zh-CN': 'zh', 'zh-TW': 'zh-Hant' }[document.documentElement.lang] || document.documentElement.lang;
for (const list of Object.values(PROVIDERS)) for (const m of list) {
  if (LIVE[m.id]) { m.in = LIVE[m.id].in; m.out = LIVE[m.id].out; }
}
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
  bengali:  /[\u0980-\u09FF]/,
  hebrew:   /[\u0590-\u05FF]/,
  emoji:    /\p{Extended_Pictographic}/u,
};
// Tokens per character, calibrated on o200k (2026-09-30, same 34-token English prompt in 27 languages)
const WEIGHT = { hangul: 0.8, kana: 0.9, cjk: 0.9, cyrillic: 0.4, arabic: 0.42, thai: 0.45, devan: 0.4, bengali: 0.4, hebrew: 0.5, emoji: 2.5 };

function analyze(text) {
  const counts = { hangul: 0, kana: 0, cjk: 0, cyrillic: 0, arabic: 0, thai: 0, devan: 0, bengali: 0, hebrew: 0, emoji: 0 };
  let latinBuf = '', latinTokens = 0, symbolTokens = 0;
  const flushLatin = () => {
    if (!latinBuf) return;
    const words = latinBuf.match(/[A-Za-zÀ-ɏḀ-ỿ']+/g) || [];
    const nums  = latinBuf.match(/\d+/g) || [];
    // Calibrated on o200k: ~1 token per 5 letters, plus ~0.4 per accented letter (Czech, Polish, Turkish, Vietnamese...)
    latinTokens += words.reduce((s, w) => s + Math.max(1, Math.round(w.length / 5 - 0.2)) + (w.match(/[À-ɏḀ-ỿ]/g) || []).length * 0.4, 0);
    latinTokens += nums.reduce((s, n) => s + Math.ceil(n.length / 3), 0);
    symbolTokens += (latinBuf.match(/[^\sA-Za-zÀ-ɏḀ-ỿ'\d]/g) || []).length * 0.8;
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
// Measured token overhead vs the same text in English (o200k): ko 1.44, ja 1.79, zh 1.03-1.35, ru 1.32 / uk 1.88, ar 1.26 / fa 1.24 / ur 1.59, th 1.74, hi 1.50, bn 1.68, he 1.56
const PENALTY = { hangul: 1.45, kana: 1.8, cjk: 1.2, cyrillic: 1.6, arabic: 1.35, thai: 1.75, devan: 1.5, bengali: 1.7, hebrew: 1.55, emoji: 1.0 };
// Latin-script languages: measured overhead of the page language (o200k, same prompt as English).
// Applied to Latin letters only when the text doesn't look like English.
const LATIN_TAX = { id: 1.15, es: 1.18, pt: 1.21, de: 1.26, fr: 1.29, nl: 1.29, sv: 1.32, vi: 1.35, it: 1.38, tr: 1.47, fil: 1.53, pl: 1.88, cs: 2.0 };
const EN_WORDS = /\b(the|and|to|of|is|in|that|for|you|with|are|this|it|be|on|please)\b/gi;
function latinTax(text) {
  const L = LATIN_TAX[PAGE_LANG];
  if (!L) return { L: 1, latin: 0 };
  const latin = (text.match(/\p{Script=Latin}/gu) || []).length;
  const words = (text.match(/\p{L}+/gu) || []).length;
  const english = words && (text.match(EN_WORDS) || []).length / words > 0.12;
  return english ? { L: 1, latin: 0 } : { L, latin };
}

function efficiency(a, text) {
  const nonSpace = (text.match(/\S/g) || []).length;
  const { L, latin } = latinTax(text);
  const marked = a.nonLatinChars + latin;
  if (!nonSpace || !marked) return { waste: 1, pct: 100, share: 0 };
  let weighted = latin * (L - 1);
  for (const k in PENALTY) weighted += a.counts[k] * (PENALTY[k] - 1);
  const share = Math.min(1, marked / nonSpace);
  const waste = 1 + (weighted / marked) * share;
  return { waste, pct: Math.round(100 / waste), share };
}

// =========================================================
// 4b) English shortener — filler/politeness removal and verbose-phrase swaps (deterministic, offline)
// =========================================================
const SWAPS = [
  ['in order to', 'to'], ['so as to', 'to'], ['due to the fact that', 'because'], ['owing to the fact that', 'because'],
  ['in spite of the fact that', 'although'], ['despite the fact that', 'although'], ['for the purpose of', 'for'],
  ['at this point in time', 'now'], ['at the present time', 'now'], ['at this moment in time', 'now'],
  ['in the near future', 'soon'], ['in the event that', 'if'], ['in a timely manner', 'promptly'],
  ['a large number of', 'many'], ['a great number of', 'many'], ['a majority of', 'most'], ['the majority of', 'most'],
  ['a small number of', 'a few'], ['with regard to', 'about'], ['with regards to', 'about'], ['in regard to', 'about'],
  ['with respect to', 'about'], ['in relation to', 'about'], ['prior to', 'before'], ['subsequent to', 'after'],
  ['is able to', 'can'], ['are able to', 'can'], ['has the ability to', 'can'], ['have the ability to', 'can'],
  ['each and every', 'every'], ['whether or not', 'whether'], ['in the process of', ''],
  ['it is important to', ''], ['make sure that you', ''], ['make sure to', ''],
  ['i would like you to', ''], ["i'd like you to", ''], ['i want you to', ''], ['i need you to', ''],
  ['would you mind', ''], ['could you please', ''], ['can you please', ''], ['would you please', ''],
  ['please kindly', ''], ['kindly', ''], ['please', ''], ['feel free to', ''],
];
const esc = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/ /g, '\\s+');
const RULES = SWAPS.map(([a, b]) => [new RegExp('\\b' + esc(a) + '\\b', 'gi'), b]);
const LEAD = /(^|[\n.!?]\s*)(could|can|would|will) you\s+(?=[a-z])/gi;      // "Could you summarize" -> "Summarize"
const LEADQ = /(^|[\n.!?]\s*)(could|can|would|will) you\s+([a-z][^?\n]*)\?/gi;  // ...and its "?" becomes "."
const TAIL = /\s*(?:,\s*)?(?:thank you(?: very much)?(?: in advance)?|thanks(?: a lot| in advance)?)\s*[.!]*\s*(?=$|\n)/gi;
const IFPOS = /,?\s*if possible\b/gi;

function shortenPart(text) {
  let t = text.replace(TAIL, '').replace(IFPOS, '').replace(LEADQ, '$1$3.').replace(LEAD, '$1');
  for (const [re, to] of RULES) {
    t = t.replace(re, (m) => (to && /^[A-Z]/.test(m) ? to[0].toUpperCase() + to.slice(1) : to));
  }
  t = t.replace(/[ \t]{2,}/g, ' ').replace(/ +([,.!?;:])/g, '$1').replace(/^[ \t]+|[ \t]+$/gm, '')
       .replace(/(^|[\n.!?]\s*)([,;]\s*)/g, '$1');
  // capitalize sentence starts that lost their first word; drop a trailing "?" left by "Could you ...?"
  t = t.replace(/(^|[\n.!?]\s+)([a-z])/g, (m, p, c) => p + c.toUpperCase());
  return t;
}

// Code blocks are left untouched
function shortenEnglish(text) {
  return text.split(/(```[\s\S]*?```)/).map((p, i) => (i % 2 ? p : shortenPart(p))).join('');
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
  costReq: $('costReq'), costMonth: $('costMonth'), overhead: $('overheadBadge'), inTokNote: $('inTokNote'),
  outRange: $('outTokens'), outNum: $('outTokensNum'), reqs: $('reqs'), chatInfo: $('chatInfo'),
};
let mode = 'text';
let original = null; // text before "To English", so the user can go back
const trBtn = $('btnTranslate'), trLabel = $('trLabel'), trSave = $('trSave');
const TEXT_PLACEHOLDER = els.input.placeholder;
const CHAT_PLACEHOLDER = '[\n  {"role": "system", "content": "You are a helpful assistant."},\n  {"role": "user", "content": "..."}\n]';

for (let i = 0; i < 10; i++) {
  const c = document.createElement('div');
  c.className = 'battery-cell rounded-sm bg-zinc-800';
  els.battery.appendChild(c);
}

const fmt = n => n.toLocaleString('en-US');
const money = n => '$' + (n < 0.01 ? n.toFixed(6) : n.toFixed(4));
const moneyBig = n => '$' + (n >= 100 ? Math.round(n).toLocaleString('en-US') : n >= 1 ? n.toFixed(2) : n < 0.01 ? n.toFixed(6) : n.toFixed(4));
const clamp = (v, lo, hi, d) => { const n = Math.round(+v); return Number.isFinite(n) ? Math.min(hi, Math.max(lo, n)) : d; };

// Chat mode: OpenAI-style messages. Content tokens + ~4 formatting tokens per message + 3 to prime the reply.
function parseChat(text) {
  if (!text.trim()) return { ok: true, parts: [], n: 0 };
  let data;
  try { data = JSON.parse(text); } catch (_) { return { ok: false }; }
  const msgs = Array.isArray(data) ? data : data && Array.isArray(data.messages) ? data.messages : null;
  if (!msgs || !msgs.every(m => m && typeof m === 'object')) return { ok: false };
  const parts = [];
  for (const m of msgs) {
    if (typeof m.content === 'string') parts.push(m.content);
    else if (Array.isArray(m.content)) m.content.forEach(c => { if (c && typeof c.text === 'string') parts.push(c.text); });
    if (typeof m.name === 'string') parts.push(m.name);
  }
  return { ok: true, parts, n: msgs.length, data };
}

function cleanText(t) {
  return t.replace(/\r\n/g, '\n').replace(/[ \t\u00a0\u3000]+/g, ' ').replace(/ *\n */g, '\n').replace(/\n{2,}/g, '\n').trim();
}

// Tokens for whatever is in the box (plain text, or the contents of a chat JSON)
function measure() {
  const raw = els.input.value;
  if (mode === 'text') return { ...countTokens(raw), text: raw, chat: null };
  const c = parseChat(raw);
  if (!c.ok) return { ...countTokens(raw), text: raw, chat: c };
  const text = c.parts.join('\n');
  let tokens = 0, exact = false, based = false;
  for (const part of c.parts) { const r = countTokens(part); tokens += r.tokens; exact = r.exact; based = r.based; }
  const fmtTokens = c.n ? c.n * 4 + 3 : 0;
  return { tokens: tokens + fmtTokens, exact, based, a: analyze(text), text, chat: { ...c, fmtTokens } };
}

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
  const { tokens, exact, based, a, text, chat } = measure();
  const chars = [...text].length;
  const words = (text.trim().match(/\S+/g) || []).length;

  if (chat) {
    els.chatInfo.className = 'mt-2 text-xs ' + (chat.ok ? 'text-zinc-500' : 'text-amber-400');
    els.chatInfo.textContent = !chat.ok ? tr('chatErr') : chat.n ? tr('chatInfo', { n: fmt(chat.n), o: fmt(chat.fmtTokens) }) : '';
  } else {
    els.chatInfo.className = 'hidden';
  }

  els.tokens.textContent = fmt(tokens);
  els.chars.textContent = fmt(chars);
  els.words.textContent = fmt(words);
  const outTok = clamp(els.outNum.value, 0, 128000, 0);
  const reqs = clamp(els.reqs.value, 1, 100000000, 1);
  const cIn = tokens / 1e6 * model.in, cOut = outTok / 1e6 * model.out, cReq = cIn + cOut;
  els.inTokNote.textContent = '(' + fmt(tokens) + ')';
  els.costIn.textContent = money(cIn);
  els.costOut.textContent = money(cOut);
  els.costReq.textContent = moneyBig(cReq);
  els.costMonth.textContent = moneyBig(cReq * reqs);
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

  // Language overhead badge next to the cost: amber from 1.15x, red from 2x
  if (e.waste >= 1.15) {
    const x = e.waste.toFixed(1);
    els.overhead.textContent = '⚠ ' + tr('overhead', { x });
    els.overhead.title = tr('overheadTip', { x });
    els.overhead.className = 'text-[11px] font-bold px-2 py-0.5 rounded-full ' +
      (e.waste >= 1.6 ? 'bg-rose-500/20 text-rose-300 border border-rose-500/40' : 'bg-amber-400/15 text-amber-300 border border-amber-400/40');
  } else {
    els.overhead.className = 'hidden';
  }  updateTranslateBtn(e);
}

function toast(msg, ms = 1800) {
  els.toast.textContent = msg;
  els.toast.style.opacity = 1;
  clearTimeout(toast.t);
  toast.t = setTimeout(() => (els.toast.style.opacity = 0), ms);
}

// =========================================================
// 6) Events
// =========================================================
function fillModels() {
  els.select.innerHTML = PROVIDERS[provider].map(m => `<option value="${m.id}">${m.name}</option>`).join('');
  model = PROVIDERS[provider][0];
}

els.input.addEventListener('input', () => { original = null; update(); });

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
  const before = measure().tokens;
  if (mode === 'chat') {
    const c = parseChat(els.input.value);
    if (!c.ok) { render(); return toast(tr('chatErr')); }
    if (c.data) {
      const msgs = Array.isArray(c.data) ? c.data : c.data.messages;
      for (const m of msgs) {
        if (typeof m.content === 'string') m.content = cleanText(m.content);
        else if (Array.isArray(m.content)) m.content.forEach(p => { if (p && typeof p.text === 'string') p.text = cleanText(p.text); });
      }
      els.input.value = JSON.stringify(c.data, null, 2);
    }
  } else {
    els.input.value = cleanText(els.input.value);
  }
  render();
  const saved = before - measure().tokens;
  toast(saved > 0 ? '✨ ' + tr('tSaved', { n: fmt(saved) }) : tr('tAlready'));
});

// Text / Chat (JSON) mode
const modeTabs = document.querySelectorAll('#modeTabs .tab');
modeTabs.forEach(btn => btn.addEventListener('click', () => {
  mode = btn.dataset.mode;
  original = null;
  modeTabs.forEach(b => b.classList.toggle('tab-active', b === btn));
  els.input.placeholder = mode === 'chat' ? CHAT_PLACEHOLDER : TEXT_PLACEHOLDER;
  els.input.dir = mode === 'chat' ? 'ltr' : 'auto';
  update();
}));
modeTabs[0].classList.add('tab-active');

// Expected output tokens (slider + number stay in sync) and requests per month
els.outRange.addEventListener('input', () => { els.outNum.value = els.outRange.value; update(); });
els.outNum.addEventListener('input', () => { els.outRange.value = Math.min(8000, +els.outNum.value || 0); update(); });
els.reqs.addEventListener('input', update);

// Translate to English on the user's device (Chrome's built-in Translator API).
// No server and no third-party service: the text never leaves the browser.

// One smart button: non-English text -> "To English", English text -> "Shorten", after either -> "Original"
let shortCache = { src: null, out: null, saved: 0, pct: 0 };
function shortenPreview(text) {
  const key = model.id + '\u0000' + text;
  if (shortCache.src !== key) {
    const out = shortenEnglish(text);
    const before = countTokens(text).tokens, after = countTokens(out).tokens;
    shortCache = { src: key, out, saved: before - after, pct: before ? Math.round((before - after) / before * 100) : 0 };
  }
  return shortCache;
}

function updateTranslateBtn(e) {
  trBtn.dataset.act = '';
  if (original !== null) {
    trBtn.classList.remove('hidden');
    trLabel.textContent = '↩ ' + tr('undo');
    trSave.textContent = '';
    trBtn.title = '';
    return;
  }
  const text = els.input.value;
  if (mode === 'text' && e.waste >= 1.15) {
    trBtn.dataset.act = 'translate';
    trLabel.textContent = '🌐 ' + tr('toEn');
    trSave.textContent = '−' + Math.round((1 - 1 / e.waste) * 100) + '%';
    trBtn.title = tr('toEnTip');
  } else if (mode === 'text' && text.trim() && text.length < 30000) {
    const sp = shortenPreview(text);
    if (sp.saved >= 2) {
      trBtn.dataset.act = 'shorten';
      trLabel.textContent = '✂ ' + tr('shorten');
      trSave.textContent = '−' + sp.pct + '%';
      trBtn.title = tr('shortenTip');
    }
  }
  trBtn.classList.toggle('hidden', !trBtn.dataset.act);
}

// Script-based guess, used when the browser's language detector isn't ready
function guessLang(text) {
  const c = analyze(text).counts;
  const top = Object.keys(c).filter(k => k !== 'emoji').sort((a, b) => c[b] - c[a])[0];
  if (!top || !c[top]) return PAGE_LANG;
  const bySite = (list, dflt) => (list.includes(PAGE_LANG) ? PAGE_LANG : dflt);
  return { hangul: 'ko', kana: 'ja', cjk: bySite(['zh', 'zh-Hant', 'ja'], 'zh'), thai: 'th', devan: 'hi', bengali: 'bn',
           hebrew: 'he', arabic: bySite(['ar', 'fa', 'ur'], 'ar'), cyrillic: bySite(['ru', 'uk'], 'ru') }[top] || PAGE_LANG;
}

const withTimeout = (p, ms) => Promise.race([p, new Promise((_, rej) => setTimeout(() => rej(new Error('timeout')), ms))]);

async function detectLang(text) {
  try {
    if ('LanguageDetector' in self && (await LanguageDetector.availability()) === 'available') {
      const d = await withTimeout(LanguageDetector.create(), 3000);
      const [top] = await d.detect(text);
      if (top && top.detectedLanguage !== 'und' && top.confidence >= 0.5) return top.detectedLanguage;
    }
  } catch (_) {}
  return guessLang(text);
}

trBtn.addEventListener('click', async () => {
  if (original !== null) {
    els.input.value = original;
    original = null;
    render();
    return toast(tr('tRestored'));
  }
  if (trBtn.dataset.act === 'shorten') {
    const text = els.input.value, sp = shortenPreview(text);
    original = text;
    els.input.value = sp.out;
    render();
    return toast('✂ ' + tr('tShortened', { n: fmt(sp.saved), p: sp.pct }), 5000);
  }
  if (!('Translator' in self)) return toast(tr('tNoSupport'), 3500);
  const text = els.input.value;
  if (!text.trim()) return;
  trBtn.disabled = true;
  toast(tr('tTranslating'), 60000);
  try {
    const sourceLanguage = await detectLang(text);
    const opts = { sourceLanguage, targetLanguage: 'en' };
    const avail = sourceLanguage === 'en' ? 'unavailable' : await Translator.availability(opts);
    if (avail === 'unavailable') return toast(tr('tLangNA'), 3500);
    const t = await withTimeout(Translator.create({
      ...opts,
      monitor(m) { m.addEventListener('downloadprogress', ev => toast(tr('tDownloading', { p: Math.round(ev.loaded * 100) }), 60000)); },
    }), avail === 'available' ? 15000 : 300000);
    const before = measure().tokens;
    const out = [];
    for (const line of text.split('\n')) out.push(line.trim() ? await t.translate(line) : line);
    original = text;
    els.input.value = out.join('\n');
    render();
    const saved = Math.max(0, before - measure().tokens);
    toast('💸 ' + tr('tTranslated', { n: fmt(saved), p: before ? Math.round(saved / before * 100) : 0 }), 5000);
  } catch (_) {
    toast(tr('tFail'), 3500);
  } finally {
    trBtn.disabled = false;
  }
});

$('btnCopy').addEventListener('click', async () => {
  if (!els.input.value) return toast(tr('tNothing'));
  try { await navigator.clipboard.writeText(els.input.value); }
  catch { els.input.select(); document.execCommand('copy'); }
  toast(tr('tCopied'));
});

$('btnClear').addEventListener('click', () => {
  els.input.value = '';
  original = null;
  render();
  els.input.focus();
  toast(tr('tCleared'));
});

render();
