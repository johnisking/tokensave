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
  return { cost, save: fullRead - rd * pr / 1e6 * mult, inp, out, cw, rd, w1, oc: out * po / 1e6 * mult };
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
  return { cost, save: cached * (p[0] - p[1]) / 1e6, inp: fresh, out, cw: wr, rd: cached, w1: 0, oc: out * p[3] / 1e6 };
}

// ---- Reading files ----
let RECS = [], UNPRICED = new Set(), state = { period: 'all', plan: '' }, FILES = 0, SESS = new Set();
const status = s => { $('#ccStatus').textContent = s; };
const projOf = (cwd, rel) => (cwd || '').split(/[\\/]/).filter(Boolean).pop() || (rel.split('/').slice(-2, -1)[0] || '?');

// ---- Deep analysis helpers: tokens of tool results are estimated from their size ----
const txtTok = x => { if (!x) return 0; const s = String(x), non = (s.match(/[^\x00-\x7f]/g) || []).length; return Math.ceil((s.length - non) / 4 + non); };
function imgTok(b64) {
  try {
    const s = atob(String(b64).slice(0, 65536)), b = i => s.charCodeAt(i);
    let w = 0, h = 0;
    if (b(0) === 0x89 && b(1) === 0x50) { w = ((b(16) << 24) | (b(17) << 16) | (b(18) << 8) | b(19)) >>> 0; h = ((b(20) << 24) | (b(21) << 16) | (b(22) << 8) | b(23)) >>> 0; }
    else if (b(0) === 0xff && b(1) === 0xd8) {
      let i = 2;
      while (i < s.length - 9) {
        if (b(i) !== 0xff) { i++; continue; }
        const m = b(i + 1);
        if (m >= 0xc0 && m <= 0xcf && m !== 0xc4 && m !== 0xc8 && m !== 0xcc) { h = (b(i + 5) << 8) | b(i + 6); w = (b(i + 7) << 8) | b(i + 8); break; }
        i += 2 + ((b(i + 2) << 8) | b(i + 3));
      }
    }
    if (!w || !h) return 1600;
    const sc = Math.min(1, 1568 / Math.max(w, h), Math.sqrt(1150000 / (w * h))); // Claude downsizes large images
    return Math.ceil(w * h * sc * sc / 750);
  } catch (_) { return 1600; }
}
function resultSize(c) {
  if (c == null) return [0, 0, 0];
  if (typeof c === 'string') return [txtTok(c), 0, 0];
  if (!Array.isArray(c)) return [txtTok(JSON.stringify(c)), 0, 0];
  let tok = 0, img = 0, itok = 0;
  for (const x of c) {
    if (!x) continue;
    if (x.type === 'image') { const k = imgTok(x.source && x.source.data); img++; itok += k; tok += k; }
    else if (x.type === 'text') tok += txtTok(x.text);
    else if (x.type !== 'tool_reference') tok += txtTok(JSON.stringify(x));
  }
  return [tok, img, itok];
}
const base = p => String(p || '').split(/[\\/]/).filter(Boolean).pop() || '';
function detailOf(name, inp) {
  inp = inp || {};
  if (inp.file_path || inp.notebook_path || inp.path) return base(inp.file_path || inp.notebook_path || inp.path);
  if (inp.command || inp.cmd) return String(inp.command || inp.cmd).replace(/\s+/g, ' ').slice(0, 60);
  if (inp.url) return String(inp.url).replace(/^https?:\/\//, '').slice(0, 60);
  if (inp.pattern) return String(inp.pattern).slice(0, 60);
  if (inp.query) return String(inp.query).slice(0, 60);
  if (inp.description) return String(inp.description).slice(0, 60);
  if (inp.action) return String(inp.action);
  return '';
}
const toolLabel = n => { const m = /^mcp__(.+?)__(.+)$/.exec(n || ''); return m ? 'MCP · ' + m[1] : (n || '?'); };
let SESSIONS = [], DEEP = [];

function parseClaude(text, rel, seen, resSeen) {
  const S = { rel, kind: 'claude', sub: /\/subagents\/|(^|\/)agent-[^/]*\.jsonl$/.test(rel), steps: new Map(), uses: new Map(), results: [] };
  for (const line of text.split('\n')) {
    const hasU = line.indexOf('"usage"') >= 0, hasT = line.indexOf('"tool_use"') >= 0, hasR = line.indexOf('"tool_result"') >= 0;
    if (!hasU && !hasT && !hasR) continue;
    let d; try { d = JSON.parse(line); } catch (_) { continue; }
    const m = d.message;
    if (!m) continue;
    if (d.type === 'assistant' && m.model && m.model !== '<synthetic>') {
      if (Array.isArray(m.content)) for (const c of m.content) if (c && c.type === 'tool_use' && c.id && !S.uses.has(c.id))
        S.uses.set(c.id, { name: c.name, ts: Date.parse(d.timestamp), inTok: txtTok(JSON.stringify(c.input || {})), model: m.model, detail: detailOf(c.name, c.input), path: (c.input && (c.input.file_path || c.input.notebook_path)) || '' });
      if (m.usage) {
        const key = m.id || d.requestId ? (m.id || '') + ':' + (d.requestId || '') : d.uuid;
        const prev = seen.get(key);
        // streamed replies repeat the same usage; keep the line with the most output tokens
        if (!prev || (prev.u.output_tokens || 0) < (m.usage.output_tokens || 0))
          seen.set(key, { u: m.usage, model: m.model, ts: d.timestamp, cwd: d.cwd || '', rel, sid: d.sessionId });
        const ps = S.steps.get(key);
        if (!ps || (ps.u.output_tokens || 0) < (m.usage.output_tokens || 0)) S.steps.set(key, { u: m.usage, model: m.model, ts: Date.parse(d.timestamp) });
      }
    } else if (d.type === 'user' && Array.isArray(m.content)) {
      for (const c of m.content) if (c && c.type === 'tool_result' && c.tool_use_id && !resSeen.has(c.tool_use_id)) {
        resSeen.add(c.tool_use_id);
        const [tok, img, itok] = resultSize(c.content);
        S.results.push({ id: c.tool_use_id, ts: Date.parse(d.timestamp), tok, img, itok });
      }
    }
  }
  // per-step prices for the carry estimate
  const st = [];
  for (const r of S.steps.values()) {
    const fam = family(r.model), p = fam && P[fam];
    if (!p || isNaN(r.ts)) continue;
    const u = r.u, inp = u.input_tokens || 0, cw = u.cache_creation_input_tokens || 0, rd = u.cache_read_input_tokens || 0;
    st.push({ ts: r.ts, ctx: inp + cw + rd, cw, rd, pr: p[2], wp: p[0] * 1.25, po: p[1], inCost: (inp * p[0] + cw * p[0] * 1.25 + rd * p[2]) / 1e6 });
  }
  S.steps = st;
  SESSIONS.push(S);
}

// Codex rollout: token_count events carry the running session total; bill the difference between events.
function parseCodex(text, rel, out) {
  let model = '', cwd = '', prev = null;
  const sid = rel.split('/').pop();
  const S = { rel, kind: 'codex', sub: false, steps: [], uses: new Map(), results: [] };
  for (const line of text.split('\n')) {
    if (!line) continue;
    let d; try { d = JSON.parse(line); } catch (_) { continue; }
    const p = d.payload || {};
    if (d.type === 'turn_context' || d.type === 'session_meta') { if (p.model) model = p.model; if (p.cwd) cwd = p.cwd; continue; }
    if (d.type === 'response_item' && /^(custom_tool_call|function_call|local_shell_call)$/.test(p.type) && p.call_id) {
      const raw = p.input != null ? String(p.input) : p.arguments != null ? String(p.arguments) : JSON.stringify(p.action || {});
      let name = p.name || 'shell';
      const inner = /tools\.(\w+)\(/.exec(raw); if (inner) name = inner[1];
      const cmd = /"(?:cmd|command)"\s*:\s*"((?:[^"\\]|\\.){1,80})/.exec(raw);
      S.uses.set(p.call_id, { name: 'Codex · ' + name, ts: Date.parse(d.timestamp), inTok: txtTok(raw), model: model || 'gpt-5', detail: cmd ? cmd[1].replace(/\\(.)/g, '$1').slice(0, 60) : '', path: '' });
      continue;
    }
    if (d.type === 'response_item' && /^(custom_tool_call_output|function_call_output)$/.test(p.type) && p.call_id) {
      const o = p.output;
      S.results.push({ id: p.call_id, ts: Date.parse(d.timestamp), tok: txtTok(typeof o === 'string' ? o : JSON.stringify(o)), img: 0, itok: 0 });
      continue;
    }
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
    const k = openaiKey(p.info.model || model || 'gpt-5'), q = k && OP[k];
    if (q) {
      const inp = u.input_tokens || 0, cached = Math.min(inp, u.cached_input_tokens || 0), wr = Math.min(inp - cached, u.cache_write_input_tokens || 0);
      const ctx = (last && last.input_tokens) || inp;
      S.steps.push({ ts: Date.parse(d.timestamp), ctx, cw: wr, rd: cached, pr: q[1], wp: q[2] || q[0], po: q[3], inCost: ((inp - cached - wr) * q[0] + cached * q[1] + wr * (q[2] || q[0])) / 1e6 });
    }
  }
  for (const x of S.uses.values()) { const k = openaiKey(x.model); x.model = k || x.model; }
  SESSIONS.push(S);
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
  const seen = new Map(), codex = [], cursor = [], codexSeen = new Set(), resSeen = new Set();
  UNPRICED = new Set(); SESS = new Set(); FILES = files.length; SESSIONS = [];
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
    parseClaude(text, rel, seen, resSeen);
  }
  RECS = [];
  for (const r of seen.values()) {
    const fam = family(r.model);
    const p = fam && price(r.u, fam, r.u.speed, r.u.inference_geo);
    if (!p) { UNPRICED.add(r.model); continue; }
    const day = (r.ts || '').slice(0, 10);
    if (!day) continue;
    if (r.sid) SESS.add(r.sid);
    RECS.push({ tool: 'claude', day, ts: Date.parse(r.ts), proj: projOf(r.cwd, r.rel), fam: NAME(fam), fk: fam, sub: /\/subagents\/|(^|\/)agent-[^/]*\.jsonl$/.test(r.rel), ...p });
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
  analyze();
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

// ---- Deep analysis: attribute the cost of each session to its starting context, tool results and output ----
// A tool result is written to the cache once and then re-read on every later reply until the session is cleared
// or compacted, so its cost is estimated as tokens × (cache-write price + the cache-read prices of the later replies).
function analyze() {
  DEEP = [];
  for (const S of SESSIONS) {
    const st = S.steps.sort((a, b) => a.ts - b.ts);
    if (!st.length) continue;
    let sg = 0;
    st.forEach((x, i) => { if (i && st[i - 1].ctx > 20000 && x.ctx < st[i - 1].ctx * 0.5) sg++; x.seg = sg; }); // /compact or /clear
    for (let i = st.length - 1; i >= 0; i--) st[i].suf = st[i].pr + (i + 1 < st.length && st[i + 1].seg === st[i].seg ? st[i + 1].suf : 0);
    const nextSuf = j => (j + 1 < st.length && st[j + 1].seg === st[j].seg ? st[j + 1].suf : 0);
    const after = T => { let lo = 0, hi = st.length; while (lo < hi) { const m = (lo + hi) >> 1; if (st[m].ts <= T) lo = m + 1; else hi = m; } return lo < st.length ? lo : -1; };
    const carry = (tok, T) => { const j = after(T); return j < 0 ? 0 : tok * (st[j].wp + nextSuf(j)) / 1e6; };
    let i0 = 0;
    for (let i = 1; i <= st.length; i++) {
      if (i < st.length && st[i].seg === st[i0].seg) continue;
      const f = st[i0], n = i - i0;
      let ctx = 0, rd = 0;
      for (let k = i0; k < i; k++) { ctx += st[k].ctx; rd += st[k].rd * st[k].pr / 1e6; }
      DEEP.push({ k: 'base', tool: S.kind, ts: f.ts, tok: f.ctx, cost: f.inCost + f.ctx * nextSuf(i0) / 1e6, n, ctxAvg: ctx / n, rdCost: rd, sub: S.sub });
      i0 = i;
    }
    for (let i = 1; i < st.length; i++) {
      const x = st[i];
      if (x.seg === st[i - 1].seg && x.ctx > 20000 && x.cw > x.ctx * 0.5)
        DEEP.push({ k: 'reb', tool: S.kind, ts: x.ts, tok: x.cw, cost: x.cw * (x.wp - x.pr) / 1e6, gap: (x.ts - st[i - 1].ts) / 6e4 });
    }
    for (const r of S.results) {
      const u = S.uses.get(r.id) || { name: '?', detail: '', path: '' };
      DEEP.push({ k: 'res', tool: S.kind, name: S.kind === 'claude' ? toolLabel(u.name) : u.name, raw: u.name, ts: r.ts, tok: r.tok, img: r.img, itok: r.itok,
        cost: carry(r.tok, r.ts), detail: u.detail, path: u.path, sess: S.rel, sub: S.sub });
    }
    for (const u of S.uses.values()) {
      const po = S.kind === 'claude' ? (P[family(u.model)] || [0, 0])[1] : (OP[u.model] || [0, 0, 0, 0])[3];
      DEEP.push({ k: 'use', tool: S.kind, name: S.kind === 'claude' ? toolLabel(u.name) : u.name, ts: u.ts, tok: u.inTok, cost: u.inTok * po / 1e6 });
    }
  }
}

function inPeriod(ts) {
  const p = state.period;
  if (p === 'all') return true;
  if (p === 'month') return new Date(ts).toISOString().slice(0, 7) === new Date().toISOString().slice(0, 7);
  return ts >= Date.now() - Number(p) * 864e5;
}
const pct = (a, b) => (b ? Math.round(a / b * 100) : 0).toLocaleString(LOC) + '%';
const SHELL = new Set(['Bash', 'PowerShell', 'Codex · exec_command', 'Codex · shell', 'Codex · exec', 'Codex · write_stdin', 'Codex · wait', 'Codex · local_shell']);
const WEB = new Set(['WebFetch', 'WebSearch', 'Codex · web_search']);

function deep(rs) {
  const wrap = $('#ccDeep');
  const recs = rs.filter(r => r.tool !== 'cursor');
  const items = DEEP.filter(x => inPeriod(x.ts));
  const total = sum(recs, 'cost');
  wrap.hidden = !total || !items.length;
  if (wrap.hidden) return;
  const outCost = recs.reduce((a, r) => a + (r.oc || 0), 0), ctxCost = total - outCost;
  const of = k => items.filter(x => x.k === k);
  const base = of('base'), res = of('res'), use = of('use'), reb = of('reb');
  const baseCost = sum(base, 'cost'), resCost = sum(res, 'cost'), useCost = sum(use, 'cost');
  const f = baseCost + resCost > ctxCost * 0.95 ? ctxCost * 0.95 / (baseCost + resCost) : 1; // keep the estimate inside the real total
  const g = useCost > outCost * 0.95 ? outCost * 0.95 / useCost : 1;
  const tools = new Map();
  const T0 = n => tools.get(n) || (tools.set(n, { name: n, n: 0, tok: 0, cost: 0, img: 0, itok: 0, big: 0 }), tools.get(n));
  for (const x of res) { const o = T0(x.name); o.n++; o.tok += x.tok; o.cost += x.cost * f; o.img += x.img; o.itok += x.itok; if (x.tok >= 10000) o.big++; }
  for (const x of use) T0(x.name).cost += x.cost * g;
  const rows = [...tools.values()].filter(o => o.cost > 0);
  rows.push({ name: t('dBase'), n: base.length, tok: sum(base, 'tok'), cost: baseCost * f });
  rows.push({ name: t('dText'), n: null, tok: null, cost: Math.max(0, outCost - useCost * g) });
  rows.push({ name: t('dRest'), n: null, tok: null, cost: Math.max(0, ctxCost - (baseCost + resCost) * f) });
  rows.sort((a, b) => b.cost - a.cost);
  $('#ccDeepTable').innerHTML = table(rows, total, t('thCalls'));

  // heaviest single tool results
  const heavy = res.slice().sort((a, b) => b.cost - a.cost).slice(0, 10);
  $('#ccHeavy').innerHTML = `<table class="w-full text-xs"><thead><tr class="text-zinc-500"><th class="text-start font-semibold py-1">${esc(t('thName'))}</th><th class="text-start font-semibold ps-2">${esc(t('thDetail'))}</th><th class="text-end font-semibold whitespace-nowrap ps-2">${esc(t('thTok'))}</th><th class="text-end font-semibold whitespace-nowrap ps-2">${esc(t('thCost'))}</th><th class="text-end font-semibold whitespace-nowrap ps-2">${esc(t('thDay'))}</th></tr></thead><tbody>` +
    heavy.map(x => `<tr class="border-t border-zinc-800"><td class="py-1.5 pe-2 whitespace-nowrap text-zinc-200">${esc(x.name)}</td><td class="ps-2 max-w-[16rem] truncate text-zinc-400 ltr" title="${esc(x.detail)}">${esc(x.detail || '–')}${x.img ? ` <span class="text-amber-300/80">🖼${x.img}</span>` : ''}</td><td class="text-end tabular-nums text-zinc-400 ps-2">${fmtTok(x.tok)}</td><td class="text-end tabular-nums font-semibold text-zinc-100 ps-2">${money(x.cost * f)}</td><td class="text-end tabular-nums text-zinc-500 ps-2 whitespace-nowrap">${new Date(x.ts).toISOString().slice(5, 10)}</td></tr>`).join('') + '</tbody></table>';

  // ---- Solutions: rule-based, each with the cost it touches ----
  const cards = [];
  const add = (id, cost, v, extra = [], save = null) => cards.push({ id, cost, v, extra, save });
  const pick = names => { const o = { n: 0, tok: 0, cost: 0, img: 0, itok: 0, big: 0 }; for (const r of tools.values()) if (names(r.name)) for (const k in o) o[k] += r[k]; return o; };
  const main = base.filter(b => !b.sub);
  if (main.length) {
    const avgTok = sum(main, 'tok') / main.length;
    if (baseCost * f / total >= 0.12 || avgTok >= 25000) add('base', baseCost * f, { tok: fmtTok(avgTok) });
  }
  const rd = pick(n => n === 'Read');
  if (rd.cost / total >= 0.08) {
    const g2 = new Map();
    for (const x of res) if (x.raw === 'Read' && x.path) { const k = x.sess + '|' + x.path; const o = g2.get(k) || { n: 0 }; o.n++; g2.set(k, o); }
    const rep3 = [...g2.values()].filter(o => o.n >= 3).length;
    const ex = rd.itok ? [t('c_read_img', { img: rd.img.toLocaleString(LOC), itok: fmtTok(rd.itok) })] : [];
    add('read', rd.cost, { n: rd.n.toLocaleString(LOC), tok: fmtTok(rd.tok), rep: rep3 ? t('c_read_rep', { files: rep3.toLocaleString(LOC) }) : '' }, ex);
  }
  const sh = pick(n => SHELL.has(n));
  if (sh.cost / total >= 0.06 || sh.big >= 5) add('shell', sh.cost, { n: sh.n.toLocaleString(LOC), big: sh.big ? t('c_shell_big', { big: sh.big.toLocaleString(LOC) }) : '', tok: fmtTok(sh.tok) });
  const mcp = [...tools.values()].filter(o => o.name.startsWith('MCP · ')).sort((a, b) => b.cost - a.cost)[0];
  if (mcp && mcp.cost / total >= 0.06) add('mcp', mcp.cost, { name: mcp.name.slice(6), n: mcp.n.toLocaleString(LOC), tok: fmtTok(mcp.tok), img: mcp.img ? t('c_mcp_img', { img: mcp.img.toLocaleString(LOC), itok: fmtTok(mcp.itok) }) : '' });
  const web = pick(n => WEB.has(n));
  if (web.cost / total >= 0.06) add('web', web.cost, { n: web.n.toLocaleString(LOC), tok: fmtTok(web.tok) });
  const rebCost = sum(reb, 'cost');
  if (reb.length >= 3 && rebCost / total >= 0.03) add('reb', rebCost, { n: reb.length.toLocaleString(LOC), tok: fmtTok(sum(reb, 'tok') / reb.length), n5: reb.filter(x => x.gap > 5).length.toLocaleString(LOC) });
  if (main.length) {
    const reps = sum(main, 'n'), avgN = reps / main.length, avgCtx = main.reduce((a, b) => a + b.ctxAvg * b.n, 0) / reps, rdc = sum(main, 'rdCost');
    if ((avgN >= 100 || avgCtx >= 100000) && rdc / total >= 0.15) add('long', rdc, { n: Math.round(avgN).toLocaleString(LOC), ctx: fmtTok(avgCtx), rd: money(rdc) });
  }
  const big = recs.filter(r => r.tool === 'claude' && /^(opus|fable|mythos)/.test(r.fk || ''));
  if (big.length) {
    const bc = sum(big, 'cost');
    const alt = big.reduce((a, r) => a + (r.inp * 2 + (r.cw - (r.w1 || 0)) * 2.5 + (r.w1 || 0) * 4 + r.rd * 0.10 + r.out * 10) / 1e6, 0); // Sonnet 5.5 rates
    if (bc / total >= 0.4 && bc - alt >= total * 0.1)
      add('model', bc - alt, { pct: pct(bc, total), models: [...new Set(big.map(r => r.fam))].join(', '), alt: money(alt) }, [], bc - alt);
  }
  const subCost = sum(recs.filter(r => r.sub), 'cost');
  if (subCost / total >= 0.15) add('sub', subCost, { cost: money(subCost) });
  const txt = Math.max(0, outCost - useCost * g);
  if (txt / total >= 0.2) add('text', txt, { cost: money(txt) });
  cards.sort((a, b) => b.cost - a.cost);
  $('#ccCards').innerHTML = cards.length ? cards.slice(0, 6).map((c, i) => {
    const steps = (C['c_' + c.id + '_s'] || []).concat(c.extra);
    const chip = c.save != null ? t('cSave', { save: money(c.save) }) : t('cCost', { cost: money(c.cost), pct: pct(c.cost, total) });
    return `<div class="rounded-xl bg-zinc-950/60 border border-zinc-800 p-4 min-w-0"><div class="flex items-start gap-3"><span class="shrink-0 w-6 h-6 rounded-full bg-violet-600 text-white text-xs font-bold grid place-items-center">${i + 1}</span><div class="min-w-0 flex-1">` +
      `<div class="flex flex-wrap items-baseline justify-between gap-x-3 gap-y-1"><h4 class="font-bold text-zinc-100">${esc(t('c_' + c.id + '_t', c.v))}</h4><span class="text-[11px] font-semibold ${c.save != null ? 'text-emerald-300 bg-emerald-500/10 border-emerald-500/30' : 'text-amber-200 bg-amber-500/10 border-amber-500/30'} border rounded-full px-2 py-0.5 tabular-nums">${esc(chip)}</span></div>` +
      `<p class="text-sm text-zinc-400 mt-1">${esc(t('c_' + c.id + '_f', c.v))}</p><ul class="mt-2 space-y-1 text-sm text-zinc-200">${steps.map(x => `<li class="flex gap-2"><span class="text-violet-400">→</span><span>${esc(x)}</span></li>`).join('')}</ul></div></div></div>`;
  }).join('') : `<p class="text-sm text-emerald-300">${esc(t('cNone'))}</p>`;
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

function table(rows, total, nHead) {
  const top = rows.slice(0, 12), rest = rows.slice(12);
  if (rest.length) top.push({ name: t('m_other') + ` (${rest.length})`, n: rest.reduce((a, r) => a + (r.n || 0), 0), tok: rest.reduce((a, r) => a + (r.tok || 0), 0), cost: sum(rest, 'cost') });
  return `<table class="w-full text-xs"><thead><tr class="text-zinc-500"><th class="text-start font-semibold py-1">${esc(t('thName'))}</th><th class="text-end font-semibold whitespace-nowrap ps-2">${esc(nHead || t('thReq'))}</th><th class="text-end font-semibold whitespace-nowrap ps-2">${esc(t('thTok'))}</th><th class="text-end font-semibold whitespace-nowrap ps-2">${esc(t('thCost'))}</th><th class="w-24 ps-3 font-semibold text-start">${esc(t('thShare'))}</th></tr></thead><tbody>` +
    top.map(r => { const pct = total ? r.cost / total * 100 : 0; return `<tr class="border-t border-zinc-800"><td class="py-1.5 pe-2 max-w-[12rem] truncate text-zinc-200" title="${esc(r.name)}">${esc(r.name)}</td><td class="text-end tabular-nums text-zinc-400">${r.n == null ? '–' : r.n.toLocaleString(LOC)}</td><td class="text-end tabular-nums text-zinc-400">${r.tok == null ? '–' : fmtTok(r.tok)}</td><td class="text-end tabular-nums font-semibold text-zinc-100">${money(r.cost)}</td><td class="ps-3"><div class="h-1.5 rounded bg-zinc-800"><div class="h-1.5 rounded bg-violet-500" style="width:${pct.toFixed(1)}%"></div></div></td></tr>`; }).join('') + '</tbody></table>';
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
  deep(rs);
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
window.__cc = { family, price, readAll, deepData: () => DEEP };
