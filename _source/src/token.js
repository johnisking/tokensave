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
    { id: 'gpt-6-astra',  name: 'GPT-6 Astra',   in: 10.00, out: 50.00, ratio: 1.00, exact: false },
    { id: 'gpt-6-1-sol',  name: 'GPT-6.1 Sol',   in: 2.00,  out: 10.00, ratio: 1.00, exact: false },
    { id: 'gpt-6-sol',    name: 'GPT-6 Sol',     in: 2.00,  out: 10.00, ratio: 1.00, exact: false },
    { id: 'gpt-6-luna',   name: 'GPT-6 Luna',    in: 0.10,  out: 0.50,  ratio: 1.00, exact: false },
    { id: 'gpt-5-6',      name: 'GPT-5.6',       in: 4.00,  out: 20.00, ratio: 1.00, exact: false },
    { id: 'gpt-5-5',      name: 'GPT-5.5',       in: 5.00,  out: 30.00, ratio: 1.00, exact: false },
    { id: 'gpt-5-4-mini', name: 'GPT-5.4 mini',  in: 0.75,  out: 4.50,  ratio: 1.00, exact: false },
    { id: 'gpt-5-mini',   name: 'GPT-5 mini',    in: 0.25,  out: 2.00,  ratio: 1.00, exact: true  },
    { id: 'gpt-5-nano',   name: 'GPT-5 nano',    in: 0.05,  out: 0.40,  ratio: 1.00, exact: true  },
    { id: 'gpt-4-1',      name: 'GPT-4.1',       in: 2.00,  out: 8.00,  ratio: 1.00, exact: true  },
    { id: 'gpt-4-1-mini', name: 'GPT-4.1 mini',  in: 0.40,  out: 1.60,  ratio: 1.00, exact: true  },
    { id: 'gpt-4o',       name: 'GPT-4o',        in: 2.50,  out: 10.00, ratio: 1.00, exact: true  },
    { id: 'gpt-4o-mini',  name: 'GPT-4o mini',   in: 0.15,  out: 0.60,  ratio: 1.00, exact: true  },
  ],
  claude: [
    // Claude 4.7+ uses a newer tokenizer (~30% more tokens for the same text)
    { id: 'claude-fable-5-1',  name: 'Claude Fable 5.1',  in: 10.00, out: 50.00, ratio: 1.30 },
    { id: 'claude-opus-5-5',   name: 'Claude Opus 5.5',   in: 4.00,  out: 20.00, ratio: 1.30 },
    { id: 'claude-sonnet-5-5', name: 'Claude Sonnet 5.5', in: 2.00,  out: 10.00, ratio: 1.30 },
    { id: 'claude-haiku-4-5',  name: 'Claude Haiku 4.5',  in: 1.00,  out: 5.00,  ratio: 1.05 },
  ],
  gemini: [
    // Gemini 4 Argon (2026-09-30): standard $4/$20; introductory $2/$10 for a limited time
    { id: 'gemini-4-argon',        name: 'Gemini 4 Argon',        in: 4.00, out: 20.00, ratio: 0.95 },
    { id: 'gemini-3-1-pro',       name: 'Gemini 3.1 Pro',        in: 2.00, out: 12.00, ratio: 0.95 },
    { id: 'gemini-3-8-flash',      name: 'Gemini 3.8 Flash',      in: 0.75, out: 3.75,  ratio: 0.95 },
    { id: 'gemini-3-5-flash-lite', name: 'Gemini 3.5 Flash-Lite', in: 0.30, out: 2.50,  ratio: 0.95 },
    { id: 'gemini-3-1-flash-lite', name: 'Gemini 3.1 Flash-Lite', in: 0.25, out: 1.50,  ratio: 0.95 },
  ],
  // Other providers: their tokenizers are not o200k, so counts are estimates
  other: [
    { id: 'deepseek-v4-pro',    group: 'DeepSeek', name: 'DeepSeek V4 Pro',    in: 1.32, out: 3.96,  ratio: 1.00 },
    { id: 'deepseek-v4-flash',  group: 'DeepSeek', name: 'DeepSeek V4.1 Flash', in: 0.30, out: 1.20,  ratio: 1.00 }, // peak price; off-peak is half (/blog/deepseek-v4-1-flash-api-pricing)
    { id: 'grok-4-7',           group: 'xAI',      name: 'Grok 4.7',           in: 2.00, out: 6.00,  ratio: 1.00 },
    { id: 'grok-4-20',          group: 'xAI',      name: 'Grok 4.20',          in: 1.25, out: 2.50,  ratio: 1.00 },
    { id: 'grok-code-fast-1',   group: 'xAI',      name: 'Grok Code Fast 1',   in: 1.00, out: 2.00,  ratio: 1.00 },
    { id: 'mistral-medium-3-5', group: 'Mistral',  name: 'Mistral Medium 3.5', in: 1.50, out: 7.50,  ratio: 1.05 },
    { id: 'mistral-large-3',    group: 'Mistral',  name: 'Mistral Large 3',    in: 0.50, out: 1.50,  ratio: 1.05 },
    { id: 'mistral-small',      group: 'Mistral',  name: 'Mistral Small',      in: 0.15, out: 0.60,  ratio: 1.05 },
    { id: 'qwen3-8-max',        group: 'Qwen',     name: 'Qwen 3.8 Max',       in: 2.00, out: 6.00,  ratio: 1.00 },
    { id: 'qwen3-8-flash',      group: 'Qwen',     name: 'Qwen 3.8 Flash',     in: 0.15, out: 0.47,  ratio: 1.00 },
    { id: 'kimi-k3',            group: 'Moonshot', name: 'Kimi K3',            in: 3.00, out: 15.00, ratio: 1.00 },
    { id: 'muse-spark-1-3',     group: 'Meta',     name: 'Muse Spark 1.3',     in: 1.25, out: 4.25,  ratio: 1.00 }, // Meta Model API 2026-09; tokenizer not public, estimate
    { id: 'kimi-k2-6',          group: 'Moonshot', name: 'Kimi K2.6',          in: 0.95, out: 4.00,  ratio: 1.00 },
  ],
};
// Latest prices from src/llm_prices.json (refreshed daily by GitHub Actions), injected by build.py
const LIVE = (window.T && window.T.prices) || {};
const PAGE_LANG = { 'zh-CN': 'zh', 'zh-TW': 'zh-Hant' }[document.documentElement.lang] || document.documentElement.lang;
for (const list of Object.values(PROVIDERS)) for (const m of list) {
  if (LIVE[m.id]) { m.in = LIVE[m.id].in; m.out = LIVE[m.id].out; m.ctx = LIVE[m.id].ctx || m.ctx; }
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
  greek:    /[\u0370-\u03FF\u1F00-\u1FFF]/,
  gurmukhi: /[\u0A00-\u0A7F]/,
  gujarati: /[\u0A80-\u0AFF]/,
  tamil:    /[\u0B80-\u0BFF]/,
  telugu:   /[\u0C00-\u0C7F]/,
  kannada:  /[\u0C80-\u0CFF]/,
  malayalam: /[\u0D00-\u0D7F]/,
  emoji:    /\p{Extended_Pictographic}/u,
};
// Tokens per character, calibrated on o200k (2026-09-30, same 34-token English prompt in 41 languages)
const WEIGHT = { hangul: 0.8, kana: 0.9, cjk: 0.9, cyrillic: 0.4, arabic: 0.42, thai: 0.45, devan: 0.4, bengali: 0.4, hebrew: 0.5, greek: 0.42,
  gurmukhi: 0.65, gujarati: 0.43, tamil: 0.35, telugu: 0.43, kannada: 0.37, malayalam: 0.34, emoji: 2.5 };

function analyze(text) {
  const counts = { hangul: 0, kana: 0, cjk: 0, cyrillic: 0, arabic: 0, thai: 0, devan: 0, bengali: 0, hebrew: 0, greek: 0, gurmukhi: 0, gujarati: 0, tamil: 0, telugu: 0, kannada: 0, malayalam: 0, emoji: 0 };
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
  return { tokens: Math.round(latinTokens + symbolTokens + scriptTokens), counts, nonLatinChars, latinTokens };
}

// =========================================================
// 4) Language efficiency — token waste vs. English for the same meaning
// =========================================================
// Measured token overhead vs the same text in English (o200k): ko 1.44, ja 1.79, zh 1.03-1.35, ru 1.32 / uk 1.88, ar 1.26 / fa 1.24 / ur 1.59, th 1.74, hi 1.50, bn 1.68, he 1.56,
// mr 1.65, gu 1.59, kn 1.79, ml 1.85, ta 1.97, te 2.03, pa 2.44
const PENALTY = { hangul: 1.45, kana: 1.8, cjk: 1.2, cyrillic: 1.6, arabic: 1.35, thai: 1.75, devan: 1.5, bengali: 1.7, hebrew: 1.55, greek: 2.06,
  gurmukhi: 2.44, gujarati: 1.59, tamil: 1.97, telugu: 2.03, kannada: 1.79, malayalam: 1.85, emoji: 1.0 };
// Latin-script languages: measured overhead of the page language (o200k, same prompt as English).
// Applied to Latin letters only when the text doesn't look like English.
const LATIN_TAX = { no: 1.32, da: 1.35, fi: 1.44, ro: 1.53, hu: 1.74, sk: 2.0, id: 1.15, es: 1.18, pt: 1.21, de: 1.26, fr: 1.29, nl: 1.29, sv: 1.32, vi: 1.35, it: 1.38, tr: 1.47, fil: 1.53, pl: 1.88, cs: 2.0 };
const EN_WORDS = /\b(the|and|to|of|is|in|that|for|you|with|are|this|it|be|on|please)\b/gi;
// Telltale letters of Latin-script languages, used when the page language doesn't say (e.g. Polish pasted on the English page)
const LATIN_MARKS = [['ro', /[ăâîșțşţ]/gi], ['hu', /[őű]/gi], ['sk', /[ľĺŕ]/gi], ['da', /[æø]/gi], ['pl', /[ąęłńśźż]/gi], ['cs', /[řěůťďň]/gi], ['tr', /[ğış]/gi], ['de', /[äöüß]/gi], ['es', /[ñ¿¡]/gi],
  ['pt', /[ãõ]/gi], ['fr', /[èêëàâîïôûœ]/gi], ['sv', /[å]/gi], ['it', /[ìò]/gi],
  ['vi', /[ơưđạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹ]/gi]];
// Very common function words, for Latin-script text without telltale letters (e.g. Spanish on the English page)
const LATIN_WORDS = [['es', /\b(el|los|las|que|y|del|para|con|por|una|como|pero|muy|est[aá]|son)\b/gi],
  ['pt', /\b(os|que|e|em|um|uma|para|com|n[aã]o|do|da|dos|das|voc[eê]|como)\b/gi],
  ['fr', /\b(le|les|des|et|est|une|pour|dans|que|avec|pas|vous|sur|du|au)\b/gi],
  ['de', /\b(der|die|das|und|ist|nicht|ein|eine|mit|f[uü]r|zu|auf|sie|den|dem)\b/gi],
  ['it', /\b(il|gli|che|di|per|una|con|non|del|della|sono|come|questo)\b/gi],
  ['nl', /\b(het|een|en|van|niet|met|voor|dat|zijn|ook|je|wat|naar)\b/gi]];
function guessLatin(text) {
  let best = null, n = 1;
  for (const [tag, re] of LATIN_MARKS) { const c = (text.match(re) || []).length; if (c > n) { best = tag; n = c; } }
  if (best) return best;
  const words = (text.match(/\p{Script=Latin}+/gu) || []).length;
  if (words < 4) return null;
  const en = (text.match(EN_WORDS) || []).length;
  let top = null, m = 0;
  for (const [tag, re] of LATIN_WORDS) { const c = (text.match(re) || []).length; if (c > m) { top = tag; m = c; } }
  return top && m / words >= 0.15 && m > en * 1.5 ? top : null;
}
function latinTax(text) {
  const L = LATIN_TAX[PAGE_LANG] || LATIN_TAX[guessLatin(text)];
  if (!L) return { L: 1, latin: 0 };
  const latin = (text.match(/\p{Script=Latin}/gu) || []).length;
  const words = (text.match(/\p{L}+/gu) || []).length;
  const english = words && (text.match(EN_WORDS) || []).length / words > 0.12;
  return english ? { L: 1, latin: 0 } : { L, latin };
}

// Scripts shared by several languages: use the page language's measured ratio when we know it
const PAGE_PENALTY = { zh: { cjk: 1.03 }, 'zh-Hant': { cjk: 1.35 }, ru: { cyrillic: 1.32 }, uk: { cyrillic: 1.88 },
  ar: { arabic: 1.26 }, fa: { arabic: 1.24 }, ur: { arabic: 1.59 }, mr: { devan: 1.65 } };

function efficiency(a, text) {
  // Waste = tokens now ÷ tokens the same text would need in English.
  // Measured by tokens, not characters: one Hangul/Kana/Greek… character carries more meaning (and tokens)
  // than one Latin letter, so a character share undercounts the non-English part of mixed text.
  const { L } = latinTax(text);
  const pen = { ...PENALTY, ...(PAGE_PENALTY[PAGE_LANG] || {}) };
  if (a.counts.kana) pen.cjk = PENALTY.cjk; // kanji inside Japanese text
  let foreignTok = 0, extra = 0;
  for (const k in WEIGHT) {
    const t = a.counts[k] * WEIGHT[k];
    if (!t || pen[k] <= 1) continue;
    foreignTok += t; extra += t * (1 - 1 / pen[k]);
  }
  if (L > 1 && a.latinTokens) { foreignTok += a.latinTokens; extra += a.latinTokens * (1 - 1 / L); }
  const total = Math.max(a.tokens, foreignTok, 1);
  if (!foreignTok || total - extra <= 0) return { waste: 1, pct: 100, share: 0 };
  const waste = total / (total - extra);
  return { waste, pct: Math.round(100 / waste), share: Math.min(1, foreignTok / total) };
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
  tokSaved: $('tokSaved'), monthSaved: $('monthSaved'),
  ctxPct: $('ctxPct'), ctxBar: $('ctxBar'), ctxText: $('ctxText'),
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

  // Context window: how much of the model's maximum input this text uses
  const ctx = model.ctx || 128000;
  const ctxShort = n => n >= 1e6 ? +(n / 1e6).toFixed(n % 1e6 ? 2 : 0) + 'M' : Math.round(n / 1000) + 'K';
  const used = tokens / ctx * 100;
  const tone2 = used > 100 ? 'rose' : used > 75 ? 'amber' : 'emerald';
  els.ctxPct.textContent = (used > 0 && used < 1 ? '<1' : fmt(Math.round(used))) + '%';
  els.ctxPct.className = 'ltr text-xs font-bold tabular-nums ' + { emerald: 'text-emerald-400', amber: 'text-amber-400', rose: 'text-rose-400' }[tone2];
  els.ctxBar.style.width = Math.min(100, used) + '%';
  els.ctxBar.className = 'h-full rounded-full transition-all ' + { emerald: 'bg-emerald-400', amber: 'bg-amber-400', rose: 'bg-rose-500' }[tone2];
  els.ctxText.textContent = used > 100
    ? tr('ctxOver', { name: model.name, max: ctxShort(ctx), n: fmt(tokens - ctx) })
    : tr('ctxFits', { p: used > 0 && used < 1 ? '<1' : Math.round(used), name: model.name, max: ctxShort(ctx) });

  // After "Save tokens": keep showing what was saved until the text is edited or restored
  const o = original !== null && mode === 'text' ? countTokens(original).tokens : 0;
  if (o > tokens) {
    const d = o - tokens;
    els.tokSaved.textContent = '↓' + fmt(d) + ' (−' + Math.round(d / o * 100) + '%)';
    els.monthSaved.textContent = tr('monthSaved', {
      a: moneyBig((o / 1e6 * model.in + cOut) * reqs), b: moneyBig(cReq * reqs), s: moneyBig(d / 1e6 * model.in * reqs) });
  }
  els.tokSaved.classList.toggle('hidden', !(o > tokens));
  els.monthSaved.classList.toggle('hidden', !(o > tokens));

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
  }
  updateTranslateBtn(e);
  renderTokView(text);
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
  const list = PROVIDERS[provider], groups = [...new Set(list.map(m => m.group).filter(Boolean))];
  const opt = m => `<option value="${m.id}">${m.name}</option>`;
  els.select.innerHTML = groups.length
    ? groups.map(g => `<optgroup label="${g}">${list.filter(m => m.group === g).map(opt).join('')}</optgroup>`).join('')
    : list.map(opt).join('');
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

([...tabs].find(b => b.dataset.provider === (window.T && window.T.defaultProvider)) || tabs[0]).click();
{ const dm = window.T && window.T.defaultModel && PROVIDERS[provider].find(m => m.id === window.T.defaultModel); if (dm) { model = dm; els.select.value = dm.id; } }

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

// "Save tokens": clean spaces -> translate to English (non-English, on-device) -> trim English filler. One undo.
const canTranslate = 'Translator' in self;
const FOREIGN = 1.1; // overhead above which text is treated as non-English (Indonesian is ~1.15x)
let saveCache = { key: null };
function savePreview(text, e) {
  const key = model.id + '\u0000' + text;
  if (saveCache.key !== key) {
    const before = countTokens(text).tokens;
    let after, foreign = e.waste >= FOREIGN;
    if (looksLikeCode(text)) {                                   // code: only comments are translated, layout kept
      const com = commentParts(text).map(p => p.body).filter(b => FOREIGN_RE.test(b)).join('\n');
      const ce = com ? efficiency(analyze(com), com) : { waste: 1 };
      foreign = ce.waste >= FOREIGN;
      const ct = com ? countTokens(com).tokens : 0;
      after = countTokens(cleanCode(text)).tokens - (foreign ? ct - ct / ce.waste : 0);
    } else {
      const clean = cleanText(text);
      if (foreign) after = countTokens(clean).tokens / e.waste;   // translation estimated from measured overhead
      else after = countTokens(shortenEnglish(clean)).tokens;                          // exact for English
    }
    const saved = Math.max(0, Math.round(before - after));
    saveCache = { key, saved, pct: before ? Math.round(saved / before * 100) : 0, needsChrome: foreign && !canTranslate };
  }
  return saveCache;
}

function updateTranslateBtn(e) {
  if (original !== null) {
    trBtn.classList.remove('hidden');
    trLabel.textContent = '↩ ' + tr('undo');
    trSave.textContent = '';
    return;
  }
  const text = els.input.value;
  const sp = mode === 'text' && text.trim() && text.length < 30000 ? savePreview(text, e) : null;
  const show = sp && sp.saved >= 1 && sp.pct >= 3;
  trBtn.classList.toggle('hidden', !show);
  if (show) {
    trLabel.textContent = '💸 ' + tr('saveTok');
    trSave.textContent = '−' + sp.pct + '%' + (sp.needsChrome ? ' · Chrome/Edge' : '');
  }
}

// Script-based guess, used when the browser's language detector isn't ready
function guessLang(text) {
  const c = analyze(text).counts;
  const top = Object.keys(c).filter(k => k !== 'emoji').sort((a, b) => c[b] - c[a])[0];
  if (!top || !c[top]) return LATIN_TAX[PAGE_LANG] ? PAGE_LANG : guessLatin(text) || PAGE_LANG;
  const bySite = (list, dflt) => (list.includes(PAGE_LANG) ? PAGE_LANG : dflt);
  return { hangul: 'ko', kana: 'ja', cjk: bySite(['zh', 'zh-Hant', 'ja'], 'zh'), thai: 'th', devan: bySite(['hi', 'mr'], 'hi'), bengali: 'bn',
           hebrew: 'he', greek: 'el', gurmukhi: 'pa', gujarati: 'gu', tamil: 'ta', telugu: 'te', kannada: 'kn', malayalam: 'ml', arabic: bySite(['ar', 'fa', 'ur'], 'ar'), cyrillic: bySite(['ru', 'uk'], 'ru') }[top] || PAGE_LANG;
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

// On-device translation (Chrome Translator API). Returns null when not possible on this browser/language.
// English name of a language code for the "Reply in …" line ('ko' -> 'Korean'); null if unknown or English
function langName(code) {
  try {
    const base = String(code).split('-')[0];
    if (base === 'en') return null;
    const n = new Intl.DisplayNames(['en'], { type: 'language' }).of(code);
    return n && n.toLowerCase() !== String(code).toLowerCase() ? n : null;
  } catch (_) { return null; }
}

// Code mode: which parts of each line are comments. Returns [{ line, pre, body }] where only body may be translated.
const FOREIGN_RE = /[^\u0000-\u024f\u1e00-\u1eff\s\p{P}\p{S}\d]/u;
function commentParts(text) {
  let inBlock = null; // '*/' or '"""' while inside a block comment / docstring
  return text.split('\n').map(line => {
    let pre = line, body = '';
    if (inBlock) {
      const end = line.indexOf(inBlock);
      if (end < 0) { const m = line.match(/^(\s*\*?\s*)(.*)$/); return { line, pre: m[1], body: m[2] }; }
      inBlock = null; return { line, pre: line, body: '' };
    }
    const m = line.match(/^(\s*(?:\/\/+|#+|--|\*|\/\*+|<!--|"""|''')\s?)(.*)$/);
    if (m) {
      if (/^\s*\/\*/.test(line) && !line.includes('*/')) inBlock = '*/';
      if (/^\s*("""|''')/.test(line) && (line.match(/"""|'''/g) || []).length === 1) inBlock = line.trim().slice(0, 3);
      return { line, pre: m[1], body: m[2] };
    }
    const c = line.search(/(?<![:\w])\/\/|\s#\s/);           // trailing comment after code (not "https://")
    if (c > 0 && !FOREIGN_RE.test(line.slice(0, c))) { pre = line.slice(0, c); body = line.slice(c); const mm = body.match(/^(\s*(?:\/\/+|#)\s?)(.*)$/); if (mm) { pre += mm[1]; body = mm[2]; } }
    return { line, pre: body ? pre : line, body };
  });
}
// Looks like source code rather than prose: many lines with code punctuation / keywords
function looksLikeCode(text) {
  const lines = text.split('\n').filter(l => l.trim());
  if (lines.length < 4) return false;
  const code = lines.filter(l => /[;{}=]\s*$|^\s*(import|package|class|def|fun|val|var|const|let|function|return|if|for|while|public|private|override|#include|from)\b|\)\s*\{|=>/.test(l)).length;
  return code / lines.length >= 0.25;
}
// Code-safe cleanup: keep indentation, only trim line ends and squeeze long blank runs
const cleanCode = t => t.replace(/\r\n/g, '\n').replace(/[ \t]+$/gm, '').replace(/\n{3,}/g, '\n\n').trim();

async function translateToEnglish(text, onlyComments = false) {
  if (!canTranslate) return { text: null, why: tr('tNoSupport') };
  const parts = onlyComments ? commentParts(text) : null;
  const sample = parts ? parts.filter(p => FOREIGN_RE.test(p.body)).map(p => p.body).join('\n') : text;
  if (!sample.trim()) return { text: null, why: tr('tAlready') };
  const sourceLanguage = await detectLang(sample);
  const opts = { sourceLanguage, targetLanguage: 'en' };
  const avail = sourceLanguage === 'en' ? 'unavailable' : await Translator.availability(opts);
  if (avail === 'unavailable') return { text: null, why: tr('tLangNA') };
  const t = await withTimeout(Translator.create({
    ...opts,
    monitor(m) { m.addEventListener('downloadprogress', ev => toast(tr('tDownloading', { p: Math.round(ev.loaded * 100) }), 60000)); },
  }), avail === 'available' ? 15000 : 300000);
  const out = [];
  if (parts) {
    for (const p of parts) out.push(p.body.trim() && FOREIGN_RE.test(p.body) ? p.pre + (await t.translate(p.body)) : p.line);
  } else {
    for (const line of text.split('\n')) out.push(line.trim() ? await t.translate(line) : line);
  }
  return { text: out.join('\n'), lang: sourceLanguage };
}

trBtn.addEventListener('click', async () => {
  if (original !== null) {
    els.input.value = original;
    original = null;
    render();
    return toast(tr('tRestored'));
  }
  const src = els.input.value;
  if (!src.trim()) return;
  const before = measure().tokens;
  const code = looksLikeCode(src);
  const scope = code ? commentParts(src).map(p => p.body).join('\n') : src;   // code: only comments get translated
  const foreign = efficiency(analyze(scope), scope).waste >= FOREIGN;
  const steps = [];
  let t = code ? cleanCode(src) : cleanText(src), note = '', replyLang = null;
  if (t !== src) steps.push(tr('stepSpaces'));
  trBtn.disabled = true;
  try {
    if (foreign) {
      toast(tr('tTranslating'), 60000);
      try {
        const r = await translateToEnglish(t, code);
        if (r.text && countTokens(r.text).tokens < countTokens(t).tokens) { t = r.text; steps.push(tr('stepEn')); replyLang = r.lang; }
        else if (!r.text) note = r.why;
      } catch (_) { note = tr('tFail'); }
    }
    if (!code && (!foreign || steps.includes(tr('stepEn')))) {
      const s2 = cleanText(shortenEnglish(t));
      if (s2 !== t) { t = s2; steps.push(tr('stepShort')); }
    }
  } finally {
    trBtn.disabled = false;
  }
  // Keep the answer in the user's language: the prompt is now English, so ask for the reply in the original one
  const replyName = replyLang && langName(replyLang);
  if (replyName && !/\breply in\b|\brespond in\b|\banswer in\b/i.test(t)) t = t.replace(/\s+$/, '') + '\n\nReply in ' + replyName + '.';
  if (t === src || !steps.length || countTokens(t).tokens >= before) return toast(note || tr('tAlready'), 3500);
  original = src;
  els.input.value = t;
  render();
  const saved = Math.max(0, before - measure().tokens);
  toast('💸 ' + tr('tSavedAll', { n: fmt(saved), p: before ? Math.round(saved / before * 100) : 0, steps: steps.join(' + ') }) + (note ? ' · ' + note : ''), 6000);
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

// =========================================================
// 7) Token split view — every o200k token as a coloured box
// =========================================================
const tv = { det: $('tokView'), box: $('tokViewBox'), more: $('tokViewMore') };
const TV_MAX = 1500;
function renderTokView(text) {
  if (!tv.det.open) return;
  if (!enc) { tv.box.textContent = tr('viewTokWait'); tv.more.textContent = ''; return; }
  let ids;
  try { ids = enc.encode(text); } catch (_) { return; }
  const shown = ids.slice(0, TV_MAX), frag = document.createDocumentFragment();
  for (let i = 0, k = 0; i < shown.length; k++) {
    // A character can span several tokens (bytes): merge until it decodes cleanly
    let n = 1, piece = enc.decode([shown[i]]);
    while (piece.includes('�') && n < 4 && i + n < shown.length) { n++; piece = enc.decode(shown.slice(i, i + n)); }
    const sp = document.createElement('span');
    sp.className = 't' + (k % 5) + (n > 1 ? ' tm' : '');
    if (n > 1) sp.title = n + ' tokens';
    sp.textContent = piece.replace(/\n/g, '↵\n');
    frag.appendChild(sp);
    i += n;
  }
  tv.box.replaceChildren(frag);
  tv.more.textContent = ids.length > TV_MAX ? tr('viewTokMore', { n: fmt(TV_MAX) }) : '';
}
tv.det.addEventListener('toggle', () => { if (tv.det.open) render(); });

// =========================================================
// 8) Share link — the text is compressed into the URL fragment (#...), which browsers never send to a server
// =========================================================
const toB64 = u8 => { let s = ''; for (let i = 0; i < u8.length; i += 8192) s += String.fromCharCode(...u8.subarray(i, i + 8192));
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, ''); };
const fromB64 = s => Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/')), c => c.charCodeAt(0));
const pipe = async (u8, stream) => new Uint8Array(await new Response(new Blob([u8]).stream().pipeThrough(stream)).arrayBuffer());
async function pack(text) {
  const u8 = new TextEncoder().encode(text);
  if ('CompressionStream' in self) { try { return 'z' + toB64(await pipe(u8, new CompressionStream('deflate-raw'))); } catch (_) {} }
  return 'u' + toB64(u8);
}
async function unpack(s) {
  const u8 = fromB64(s.slice(1));
  return new TextDecoder().decode(s[0] === 'z' ? await pipe(u8, new DecompressionStream('deflate-raw')) : u8);
}
const SHARE_MAX = 16000; // URL length that chat apps and browsers handle reliably
$('btnShare').addEventListener('click', async () => {
  if (!els.input.value) return toast(tr('tNothing'));
  const q = new URLSearchParams({ t: await pack(els.input.value) });
  if (mode !== 'text') q.set('m', mode);
  if (provider !== 'openai' || model !== PROVIDERS.openai[0]) { q.set('p', provider); q.set('id', model.id); }
  const url = location.origin + location.pathname + '#' + q.toString();
  if (url.length > SHARE_MAX) return toast(tr('tShareLong'), 3500);
  try { await navigator.clipboard.writeText(url); } catch (_) {}
  toast('🔗 ' + tr('tShareCopied'), 4000);
});
async function openShared() {
  const raw = window.__share || location.hash.slice(1);
  window.__share = null;
  if (/(^|&)t=/.test(raw) && location.hash) history.replaceState(null, '', location.pathname + location.search);
  const q = new URLSearchParams(raw);
  const t = q.get('t');
  if (!t) return;
  try {
    const text = await unpack(t);
    const m = [...modeTabs].find(b => b.dataset.mode === q.get('m'));
    if (m) m.click();
    const p = [...tabs].find(b => b.dataset.provider === q.get('p'));
    if (p) {
      p.click();
      const found = PROVIDERS[provider].find(x => x.id === q.get('id'));
      if (found) { model = found; els.select.value = found.id; }
    }
    els.input.value = text;
    render();
  } catch (e) { console.warn('Could not open shared text', e); }
}
openShared();
window.addEventListener('hashchange', openShared);

render();
