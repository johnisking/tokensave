// Claude Code usage analyzer: reads ~/.claude/projects/**/*.jsonl in the browser (nothing is uploaded),
// counts each assistant reply once and prices it at the official API rates (checked 2026-10-15,
// platform.claude.com/docs/en/about-claude/pricing). Strings come from window.T.cc.
const C = (window.T && window.T.cc) || {};
const $ = s => document.querySelector(s);
const t = (k, v = {}) => (C[k] || k).replace(/\{(\w+)\}/g, (_, x) => (x in v ? v[x] : ''));
const LANG = document.documentElement.lang;

// ---- Prices per 1M tokens: [input, output, cache read, fast input, fast output] ----
// Cache writes are 1.25× (5 min) and 2× (1 h) of the input price; geo = US-only inference costs 1.1× (Claude 4.6+).
const P = {
  'fable-5-1': [10, 50, 0.25], 'mythos-5-1': [10, 50, 0.25], 'fable-5': [10, 50, 1], 'mythos-5': [10, 50, 1],
  'opus-5-5': [4, 20, 0.20, 8, 40], 'opus-5': [5, 25, 0.50, 10, 50], 'opus-4-8': [5, 25, 0.50, 10, 50],
  'opus-4-7': [5, 25, 0.50], 'opus-4-6': [5, 25, 0.50], 'opus-4-5': [5, 25, 0.50], 'opus-4-1': [15, 75, 1.50], 'opus-4': [15, 75, 1.50],
  'sonnet-5-5': [2, 10, 0.10], 'sonnet-5': [2, 10, 0.20], 'sonnet-4-6': [3, 15, 0.30], 'sonnet-4-5': [3, 15, 0.30], 'sonnet-4': [3, 15, 0.30],
  'sonnet-3-7': [3, 15, 0.30], 'haiku-5-5': [0.10, 0.50, 0.01], 'haiku-4-5': [1, 5, 0.10], 'haiku-3-5': [0.80, 4, 0.08],
};
const HAIKU55_LONG = [0.50, 2.50, 0.05];
const NO_GEO = new Set(['opus-4-5', 'opus-4-1', 'opus-4', 'sonnet-4-5', 'sonnet-4', 'sonnet-3-7', 'haiku-4-5', 'haiku-3-5']);
const NAME = k => 'Claude ' + k.replace(/^(\w+)-(\d+)(?:-(\d+))?$/, (_, f, a, b) => f[0].toUpperCase() + f.slice(1) + ' ' + a + (b ? '.' + b : ''));

// claude-opus-4-1-20250805 -> opus-4-1 ; claude-3-5-haiku-20241022 -> haiku-3-5 ; claude-opus-4-20250514 -> opus-4
function family(model) {
  const m = String(model || '').toLowerCase().replace(/\[.*?\]/g, '').replace(/@.*$/, '');
  let r = m.match(/(fable|mythos|opus|sonnet|haiku)-(\d+)(?:-(\d{1,2}))?(?=-\d{6,}|$|-v\d|:)/);
  if (r) return r[1] + '-' + r[2] + (r[3] ? '-' + r[3] : '');
  r = m.match(/claude-(\d)-(\d)-(sonnet|haiku|opus)/);
  if (r) return r[3] + '-' + r[1] + '-' + r[2];
  return null;
}

function price(u, fam, speed, geo) {
  let p = P[fam];
  if (!p) return null;
  const c5 = (u.cache_creation && u.cache_creation.ephemeral_5m_input_tokens) || 0;
  const c1 = (u.cache_creation && u.cache_creation.ephemeral_1h_input_tokens) || 0;
  const cw = u.cache_creation_input_tokens || 0;
  const w5 = c5 + c1 ? c5 : cw, w1 = c5 + c1 ? c1 : 0; // older logs have no 5m/1h split: treat writes as 5-minute
  const inp = u.input_tokens || 0, out = u.output_tokens || 0, rd = u.cache_read_input_tokens || 0;
  let [pi, po, pr] = p;
  if (fam === 'haiku-5-5' && inp + rd + cw > 100000) [pi, po, pr] = HAIKU55_LONG;
  if (speed === 'fast' && p[3]) { pr = pr * p[3] / pi; pi = p[3]; po = p[4]; }
  const mult = geo === 'us' && !NO_GEO.has(fam) ? 1.1 : 1;
  const web = ((u.server_tool_use && u.server_tool_use.web_search_requests) || 0) * 0.01;
  const cost = (inp * pi + w5 * pi * 1.25 + w1 * pi * 2 + rd * pr + out * po) / 1e6 * mult + web;
  const fullRead = rd * pi / 1e6 * mult; // what the cache reads would cost at the plain input price
  return { cost, save: fullRead - rd * pr / 1e6 * mult, inp, out, cw, rd };
}

// ---- Money: USD for en, local currency (no VAT, matching API pricing) for ko/ja ----
const CUR = ({ ko: ['KRW', 1345, 'ko-KR', 100], ja: ['JPY', 158, 'ja-JP', 1], tr: ['TRY', 49.28, 'tr-TR', 1], uk: ['UAH', 44.6, 'uk-UA', 1], 'zh-CN': ['CNY', 6.72, 'zh-CN', 1] })[LANG] || null; // rates as on the game calculator (2026-10-05)
const LOC = CUR ? CUR[2] : 'en-US';
const money = n => {
  if (!CUR) return '$' + (n >= 1000 ? Math.round(n).toLocaleString('en-US') : n.toFixed(2));
  const v = Math.round(n * CUR[1] / CUR[3]) * CUR[3];
  return new Intl.NumberFormat(CUR[2], { style: 'currency', currency: CUR[0], maximumFractionDigits: 0 }).format(v);
};
const fmtTok = n => n >= 1e9 ? (n / 1e9).toFixed(2) + 'B' : n >= 1e6 ? (n / 1e6).toFixed(1) + 'M' : n >= 1e3 ? Math.round(n / 1e3) + 'K' : String(n);
// Plan fees in USD per month before VAT, checked 2026-10-15 (claude.com/pricing, chatgpt.com/pricing, cursor.com/pricing)
const PLANS = {
  pro: ['claude', 20, 'Claude Pro'], max5: ['claude', 100, 'Claude Max 5×'], max20: ['claude', 200, 'Claude Max 20×'],
  plus: ['codex', 20, 'ChatGPT Plus'], gpro100: ['codex', 100, 'ChatGPT Pro 100'], gpro200: ['codex', 200, 'ChatGPT Pro 200'],
  cpremium: ['cursor', 30, 'Cursor Premium'], csuper: ['cursor', 100, 'Cursor Super'], cultra: ['cursor', 200, 'Cursor Ultra'],
};
const TOOL_NAME = { claude: 'Claude Code', codex: 'Codex', cursor: 'Cursor' };

// ---- OpenAI prices per 1M tokens for Codex: [input, cached input, cache write or null, output] (short context) ----
const OP = {
  'gpt-6-astra': [10, 1, 12.5, 50], 'gpt-6.1-sol': [2, 0.10, 2.5, 10], 'gpt-6-sol': [2, 0.20, 2.5, 10], 'gpt-6-luna': [0.10, 0.01, 0.125, 0.50],
  'gpt-5.6-sol': [4, 0.40, 5, 20], 'gpt-5.6-terra': [2, 0.20, 2.5, 12], 'gpt-5.6-luna': [0.20, 0.02, 0.25, 1.20],
  'gpt-5.5': [5, 0.50, null, 30], 'gpt-5.4': [2.5, 0.25, null, 15], 'gpt-5.4-mini': [0.75, 0.075, null, 4.5], 'gpt-5.4-nano': [0.20, 0.02, null, 1.25],
  'gpt-5.3-codex': [1.75, 0.175, null, 14], 'gpt-5.2': [1.75, 0.175, null, 14], 'gpt-5.1': [1.25, 0.125, null, 10], 'gpt-5': [1.25, 0.125, null, 10],
  'gpt-5-mini': [0.25, 0.025, null, 2], 'gpt-5-nano': [0.05, 0.005, null, 0.40], 'gpt-4.1': [2, 0.50, null, 8], 'o3': [2, 0.50, null, 8], 'o4-mini': [1.10, 0.275, null, 4.40],
};
function openaiKey(model) {
  let m = String(model || '').toLowerCase().trim();
  if (OP[m]) return m;
  m = m.replace(/-\d{4}-\d{2}-\d{2}$/, '');
  if (OP[m]) return m;
  const base = m.replace(/-codex(-max|-mini|-spark)?$/, '');
  return OP[base] ? base : null;
}
function priceCodex(u, key) {
  const p = OP[key];
  const inp = u.input_tokens || 0, cached = Math.min(inp, u.cached_input_tokens || 0), out = u.output_tokens || 0;
  const wr = p[2] ? Math.min(inp - cached, u.cache_write_input_tokens || 0) : 0;
  const fresh = inp - cached - wr;
  const cost = (fresh * p[0] + cached * p[1] + wr * (p[2] || p[0]) + out * p[3]) / 1e6;
  return { cost, save: cached * (p[0] - p[1]) / 1e6, inp: fresh, out, cw: wr, rd: cached };
}

// ---- Reading files ----
let RECS = [], UNPRICED = new Set(), state = { period: 'all', plan: '' }, FILES = 0, SESS = new Set();
const status = s => { $('#ccStatus').textContent = s; };
const projOf = (cwd, rel) => (cwd || '').split(/[\\/]/).filter(Boolean).pop() || (rel.split('/').slice(-2, -1)[0] || '?');

function parseClaude(text, rel, seen) {
  for (const line of text.split('\n')) {
    if (line.indexOf('"usage"') < 0) continue;
    let d; try { d = JSON.parse(line); } catch (_) { continue; }
    const m = d.message;
    if (!m || !m.usage || d.type !== 'assistant') continue;
    if (!m.model || m.model === '<synthetic>') continue;
    const key = m.id || d.requestId ? (m.id || '') + ':' + (d.requestId || '') : d.uuid;
    const prev = seen.get(key);
    // streamed replies repeat the same usage; keep the line with the most output tokens
    if (prev && (prev.u.output_tokens || 0) >= (m.usage.output_tokens || 0)) continue;
    seen.set(key, { u: m.usage, model: m.model, ts: d.timestamp, cwd: d.cwd || '', rel, sid: d.sessionId });
  }
}

// Codex rollout: token_count events carry the running session total; bill the difference between events.
function parseCodex(text, rel, out) {
  let model = '', cwd = '', prev = null;
  const sid = rel.split('/').pop();
  for (const line of text.split('\n')) {
    if (!line) continue;
    let d; try { d = JSON.parse(line); } catch (_) { continue; }
    const p = d.payload || {};
    if (d.type === 'turn_context' || d.type === 'session_meta') { if (p.model) model = p.model; if (p.cwd) cwd = p.cwd; continue; }
    if (p.type !== 'token_count' || !p.info) continue;
    const tot = p.info.total_token_usage, last = p.info.last_token_usage;
    let u;
    if (tot) {
      if (prev && tot.total_tokens === prev.total_tokens) continue; // re-emitted event
      u = {};
      for (const k of ['input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens', 'total_tokens']) u[k] = Math.max(0, (tot[k] || 0) - ((prev && prev[k]) || 0));
      prev = tot;
    } else if (last) u = last; else continue;
    if (!u.input_tokens && !u.output_tokens) continue;
    out.push({ u, model: p.info.model || model || 'gpt-5', ts: d.timestamp, cwd, rel, sid });
  }
}

// Cursor: the usage CSV exported from cursor.com/dashboard (the local database no longer keeps token counts)
function parseCsvLine(l) {
  const r = []; let cur = '', q = false;
  for (let i = 0; i < l.length; i++) {
    const c = l[i];
    if (q) { if (c === '"') { if (l[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += c; }
    else if (c === '"') q = true; else if (c === ',') { r.push(cur); cur = ''; } else cur += c;
  }
  r.push(cur); return r;
}
function parseCursor(text, recs) {
  const lines = text.replace(/^﻿/, '').split(/\r?\n/).filter(Boolean);
  const h = parseCsvLine(lines[0]).map(x => x.trim().toLowerCase());
  const ix = n => h.indexOf(n);
  const iD = ix('date'), iM = ix('model'), iW = ix('input (w/ cache write)'), iI = ix('input (w/o cache write)'), iR = ix('cache read'), iO = ix('output tokens'), iC = ix('cost'), iK = ix('kind');
  if (iD < 0 || iC < 0) return 0;
  let n = 0;
  for (const l of lines.slice(1)) {
    const c = parseCsvLine(l);
    const num = i => (i < 0 ? 0 : Number(String(c[i]).replace(/[^0-9.]/g, '')) || 0);
    const ts = c[iD];
    if (!ts || isNaN(Date.parse(ts))) continue;
    if (/error/i.test(c[iK] || '')) continue;
    recs.push({ tool: 'cursor', day: new Date(ts).toISOString().slice(0, 10), ts: Date.parse(ts), proj: 'Cursor', fam: c[iM] || '?',
      cost: num(iC), save: 0, inp: num(iI), out: num(iO), cw: num(iW), rd: num(iR) });
    n++;
  }
  return n;
}

async function readAll(files) {
  files = files.filter(f => /\.(jsonl|csv)$/i.test(f.name));
  if (!files.length) { status(t('noData')); return; }
  status(t('reading', { n: files.length.toLocaleString(LOC) }));
  const seen = new Map(), codex = [], cursor = [], codexSeen = new Set();
  UNPRICED = new Set(); SESS = new Set(); FILES = files.length;
  for (const f of files) {
    let text;
    try { text = await f.text(); } catch (_) { continue; }
    const rel = f.webkitRelativePath || f.relPath || f.name;
    if (/\.csv$/i.test(f.name)) { parseCursor(text, cursor); continue; }
    if (text.indexOf('"token_count"') >= 0 || text.indexOf('"session_meta"') >= 0) {
      const base = f.name; // Codex moves archived sessions to archived_sessions/ with the same name
      if (codexSeen.has(base)) continue;
      codexSeen.add(base); parseCodex(text, rel, codex); continue;
    }
    parseClaude(text, rel, seen);
  }
  RECS = [];
  for (const r of seen.values()) {
    const fam = family(r.model);
    const p = fam && price(r.u, fam, r.u.speed, r.u.inference_geo);
    if (!p) { UNPRICED.add(r.model); continue; }
    const day = (r.ts || '').slice(0, 10);
    if (!day) continue;
    if (r.sid) SESS.add(r.sid);
    RECS.push({ tool: 'claude', day, ts: Date.parse(r.ts), proj: projOf(r.cwd, r.rel), fam: NAME(fam), ...p });
  }
  for (const r of codex) {
    const k = openaiKey(r.model);
    if (!k) { UNPRICED.add(r.model); continue; }
    const day = (r.ts || '').slice(0, 10);
    if (!day) continue;
    SESS.add('cx:' + r.sid);
    RECS.push({ tool: 'codex', day, ts: Date.parse(r.ts), proj: projOf(r.cwd, r.rel), fam: k.replace(/^gpt/, 'GPT').replace(/-(\w)/g, (_, c) => ' ' + c.toUpperCase()), ...priceCodex(r.u, k) });
  }
  RECS.push(...cursor);
  if (!RECS.length) { status(t('noData')); $('#ccResult').hidden = true; return; }
  status(t('readDone', { files: FILES.toLocaleString(LOC), msgs: RECS.length.toLocaleString(LOC), sessions: SESS.size.toLocaleString(LOC) }));
  // default plan: the plan family of the tool with the most cost
  const byTool = {}; for (const r of RECS) byTool[r.tool] = (byTool[r.tool] || 0) + r.cost;
  const top = Object.keys(byTool).sort((a, b) => byTool[b] - byTool[a])[0];
  if (!state.plan || PLANS[state.plan] && !byTool[PLANS[state.plan][0]]) state.plan = { claude: 'max5', codex: 'plus', cursor: 'cpremium' }[top];
  $('#ccPlanSel').value = state.plan;
  $('#ccResult').hidden = false;
  render();
  $('#ccResult').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Drag & drop of a whole folder
async function walk(entry, out, path = '') {
  if (entry.isFile) {
    if (/\.jsonl$/i.test(entry.name)) out.push(await new Promise(res => entry.file(f => { f.relPath = path + entry.name; res(f); }, () => res(null))));
  } else if (entry.isDirectory) {
    const rd = entry.createReader();
    let batch;
    do {
      batch = await new Promise(res => rd.readEntries(res, () => res([])));
      for (const e of batch) await walk(e, out, path + entry.name + '/');
    } while (batch.length);
  }
}

// ---- Rendering ----
function filtered() {
  const now = Date.now(), p = state.period;
  if (p === 'all') return RECS;
  if (p === 'month') { const ym = new Date().toISOString().slice(0, 7); return RECS.filter(r => r.day.startsWith(ym)); }
  const from = now - Number(p) * 864e5;
  return RECS.filter(r => r.ts >= from);
}
const sum = (rs, k) => rs.reduce((a, r) => a + r[k], 0);
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);

function group(rs, key, label) {
  const g = new Map();
  for (const r of rs) {
    const k = r[key];
    const o = g.get(k) || { name: label ? label(k) : k, n: 0, tok: 0, cost: 0 };
    o.n++; o.tok += r.inp + r.out + r.cw + r.rd; o.cost += r.cost; g.set(k, o);
  }
  return [...g.values()].sort((a, b) => b.cost - a.cost);
}

function table(rows, total) {
  const top = rows.slice(0, 12), rest = rows.slice(12);
  if (rest.length) top.push({ name: t('m_other') + ` (${rest.length})`, n: sum(rest, 'n'), tok: sum(rest, 'tok'), cost: sum(rest, 'cost') });
  return `<table class="w-full text-xs"><thead><tr class="text-zinc-500"><th class="text-start font-semibold py-1">${esc(t('thName'))}</th><th class="text-end font-semibold whitespace-nowrap ps-2">${esc(t('thReq'))}</th><th class="text-end font-semibold whitespace-nowrap ps-2">${esc(t('thTok'))}</th><th class="text-end font-semibold whitespace-nowrap ps-2">${esc(t('thCost'))}</th><th class="w-24 ps-3 font-semibold text-start">${esc(t('thShare'))}</th></tr></thead><tbody>` +
    top.map(r => { const pct = total ? r.cost / total * 100 : 0; return `<tr class="border-t border-zinc-800"><td class="py-1.5 pe-2 max-w-[12rem] truncate text-zinc-200" title="${esc(r.name)}">${esc(r.name)}</td><td class="text-end tabular-nums text-zinc-400">${r.n.toLocaleString(LOC)}</td><td class="text-end tabular-nums text-zinc-400">${fmtTok(r.tok)}</td><td class="text-end tabular-nums font-semibold text-zinc-100">${money(r.cost)}</td><td class="ps-3"><div class="h-1.5 rounded bg-zinc-800"><div class="h-1.5 rounded bg-violet-500" style="width:${pct.toFixed(1)}%"></div></div></td></tr>`; }).join('') + '</tbody></table>';
}

function daily(rs) {
  const g = new Map();
  for (const r of rs) g.set(r.day, (g.get(r.day) || 0) + r.cost);
  const days = [...g.keys()].sort();
  if (!days.length) return '';
  const all = [];
  for (let d = new Date(days[0] + 'T00:00:00Z'); d <= new Date(days[days.length - 1] + 'T00:00:00Z'); d = new Date(d.getTime() + 864e5)) all.push(d.toISOString().slice(0, 10));
  const max = Math.max(...g.values()) || 1;
  const bars = all.map(d => { const v = g.get(d) || 0, h = Math.max(v ? 3 : 0, v / max * 100); return `<div class="flex flex-col items-center justify-end h-full min-w-[10px] flex-1" title="${d}: ${money(v)}"><div class="w-full max-w-[22px] rounded-t bg-gradient-to-t from-violet-600 to-indigo-400" style="height:${h.toFixed(1)}%"></div></div>`; }).join('');
  return `<div class="flex items-end gap-[3px] h-40 px-1" style="min-width:${all.length * 13}px">${bars}</div>` +
    `<div class="flex justify-between text-[10px] text-zinc-500 mt-1 px-1 tabular-nums"><span>${all[0]}</span><span>${money(max)} max</span><span>${all[all.length - 1]}</span></div>`;
}

function render() {
  const rs = filtered();
  const cost = sum(rs, 'cost'), save = sum(rs, 'save'), io = sum(rs, 'inp') + sum(rs, 'out'), cache = sum(rs, 'cw') + sum(rs, 'rd');
  const days = [...new Set(rs.map(r => r.day))].sort();
  $('#ccKCost').textContent = money(cost);
  $('#ccKTok').textContent = fmtTok(io + cache);
  $('#ccKTokSub').textContent = t('kTokSub', { io: fmtTok(io), cache: fmtTok(cache) });
  $('#ccKSave').textContent = money(save);
  $('#ccKDays').textContent = days.length.toLocaleString(LOC);
  $('#ccKDaysSub').textContent = days.length ? t('kDaysSub', { from: days[0], to: days[days.length - 1] }) : '';
  $('#ccDaily').innerHTML = daily(rs);
  $('#ccProj').innerHTML = table(group(rs, 'proj'), cost);
  $('#ccModel').innerHTML = table(group(rs, 'fam'), cost);
  const tools = group(rs, 'tool', k => TOOL_NAME[k]);
  const tb = $('#ccToolWrap'); tb.hidden = tools.length < 2; if (tools.length > 1) $('#ccTool').innerHTML = table(tools, cost);
  const un = $('#ccUnpriced');
  un.hidden = !UNPRICED.size;
  if (UNPRICED.size) un.textContent = t('unpriced', { list: [...UNPRICED].slice(0, 8).join(', ') });
  plan(rs);
}

function plan(all) {
  const out = $('#ccPlanOut');
  const pl = PLANS[state.plan];
  const rs = pl ? all.filter(r => r.tool === pl[0]) : all;
  const cost = sum(rs, 'cost');
  const days = [...new Set((rs.length ? rs : all).map(r => r.day))].sort();
  if (!days.length) { out.innerHTML = ''; return; }
  const span = Math.max(1, Math.round((Date.parse(days[days.length - 1]) - Date.parse(days[0])) / 864e5) + 1);
  const n = state.period === 'all' || state.period === 'month' ? span : Number(state.period);
  const month = cost / n * 30;
  if (!pl) { out.innerHTML = `<p>${esc(t('planApi', { api: money(cost), month: money(month) }))}</p>`; return; }
  const fee = pl[1] * n / 30;
  const ratio = fee ? cost / fee * 100 : 0;
  const pct = Math.round(ratio).toLocaleString(LOC) + '%';
  const win = cost >= fee;
  out.innerHTML = `<p>${esc(t('planLine', { days: n, plan: pl[2], fee: money(fee), api: money(cost) }))} <span class="text-zinc-500">(${esc(TOOL_NAME[pl[0]])})</span></p>` +
    `<p class="text-base font-bold ${win ? 'text-emerald-300' : 'text-amber-300'}">${esc(win ? t('planWin', { pct }) : t('planLose', { api: money(cost), fee: money(fee) }))}</p>` +
    `<div class="mt-2 h-2.5 rounded bg-zinc-800 overflow-hidden"><div class="h-2.5 ${win ? 'bg-emerald-500' : 'bg-amber-500'}" style="width:${Math.min(100, ratio).toFixed(1)}%"></div></div>`;
}

function csv() {
  const g = new Map();
  for (const r of filtered()) {
    const o = g.get(r.day) || { replies: 0, input: 0, output: 0, cache_write: 0, cache_read: 0, cost_usd: 0 };
    o.replies++; o.input += r.inp; o.output += r.out; o.cache_write += r.cw; o.cache_read += r.rd; o.cost_usd += r.cost; g.set(r.day, o);
  }
  const head = 'date,replies,input,output,cache_write,cache_read,cost_usd';
  const rows = [...g.entries()].sort().map(([d, o]) => [d, o.replies, o.input, o.output, o.cache_write, o.cache_read, o.cost_usd.toFixed(4)].join(','));
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([head + '\n' + rows.join('\n') + '\n'], { type: 'text/csv' }));
  a.download = 'claude-code-usage.csv';
  document.body.appendChild(a); a.click(); a.remove();
}

function seg(id, key) {
  const box = $(id);
  box.addEventListener('click', e => {
    const b = e.target.closest('button[data-v]');
    if (!b) return;
    box.querySelectorAll('button').forEach(x => { x.classList.toggle('tab-active', x === b); x.classList.toggle('text-zinc-400', x !== b); });
    state[key] = b.dataset.v;
    if (RECS.length) render();
  });
  box.querySelectorAll('button').forEach(x => x.classList.toggle('text-zinc-400', !x.classList.contains('tab-active')));
}

function init() {
  $('#ccDir').addEventListener('change', e => readAll([...e.target.files]));
  $('#ccFiles').addEventListener('change', e => readAll([...e.target.files]));
  const drop = $('#ccDrop');
  drop.addEventListener('dragover', e => { e.preventDefault(); drop.classList.add('border-violet-500'); });
  drop.addEventListener('dragleave', () => drop.classList.remove('border-violet-500'));
  drop.addEventListener('drop', async e => {
    e.preventDefault(); drop.classList.remove('border-violet-500');
    const items = [...(e.dataTransfer.items || [])].map(i => i.webkitGetAsEntry && i.webkitGetAsEntry()).filter(Boolean);
    const out = [];
    if (items.length) for (const it of items) await walk(it, out);
    else out.push(...e.dataTransfer.files);
    readAll(out.filter(Boolean));
  });
  document.querySelectorAll('[data-copy]').forEach(b => {
    b.textContent = t('copy');
    b.addEventListener('click', () => {
      const done = () => { b.textContent = t('copied'); setTimeout(() => { b.textContent = t('copy'); }, 1200); };
      try { navigator.clipboard.writeText(b.dataset.copy).then(done, done); } catch (_) { done(); }
    });
  });
  seg('#ccPeriod', 'period');
  $('#ccPlanSel').addEventListener('change', e => { state.plan = e.target.value; if (RECS.length) render(); });
  $('#ccCsv').addEventListener('click', csv);
}
init();

// Exposed for tests
window.__cc = { family, price, readAll };
