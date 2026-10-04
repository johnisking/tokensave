// AI game cost estimator: a few questions -> asset list -> cost/time/tokens with AI tools -> ready-to-use prompts.
// Strings come from window.T.gc (en/ko/ja), model prices from window.T.prices (llm_prices.json).
const G = (window.T && window.T.gc) || {};
const PRICES = (window.T && window.T.prices) || {};
const $ = s => document.querySelector(s);
const t = (k, v = {}) => (G[k] || k).replace(/\{(\w+)\}/g, (_, x) => (x in v ? v[x] : ''));
const usd = n => Number.isInteger(n) && n < 1000 ? '$' + n : n >= 1000 ? '$' + Math.round(n).toLocaleString('en-US') : n >= 100 ? '$' + Math.round(n) : '$' + n.toFixed(n < 10 ? 2 : 0);
const range = (a, b) => `${usd(a)} – ${usd(b)}`;
const fmtTok = n => n >= 1e9 ? (n / 1e9).toFixed(1) + 'B' : n >= 1e6 ? Math.round(n / 1e6) + 'M' : Math.round(n / 1e3) + 'K';

// ---- Size anchors: real solo + AI builds (small ≈ 14 days, medium ≈ 4 weeks, large ≈ 6 weeks) ----
const SCALE = {
  s: { days: 14, loc: 4000, chars: 3, bg: 4, items: 15, ui: 25, music: 3, sfx: 25 },
  m: { days: 28, loc: 9000, chars: 6, bg: 10, items: 40, ui: 50, music: 5, sfx: 45 },
  l: { days: 42, loc: 15000, chars: 10, bg: 18, items: 80, ui: 80, music: 8, sfx: 70 },
};
// Genre multipliers on the anchors
const GENRE = {
  puzzle:     { chars: 0.5, bg: 1.0, items: 1.2, loc: 0.8, days: 0.9 },
  racing:     { chars: 0.8, bg: 1.2, items: 0.8, loc: 1.0, days: 1.0 },
  merge:      { chars: 0.7, bg: 1.0, items: 2.2, loc: 1.1, days: 1.1 },
  idle:       { chars: 0.7, bg: 0.8, items: 1.5, loc: 1.0, days: 1.0 },
  platformer: { chars: 1.0, bg: 1.5, items: 1.0, loc: 1.1, days: 1.1 },
  rpg:        { chars: 1.8, bg: 1.8, items: 1.8, loc: 1.6, days: 1.6 },
  novel:      { chars: 1.2, bg: 2.0, items: 0.4, loc: 0.6, days: 0.9 },
  shooter:    { chars: 1.3, bg: 1.2, items: 1.0, loc: 1.2, days: 1.2 },
};
const ANIM = { none: { actions: 1, frames: 1 }, simple: { actions: 3, frames: 4 }, full: { actions: 6, frames: 8 } };
const SFXLV = { few: 0.6, normal: 1, many: 1.6 };
const FEAT = { ads: { loc: 300, days: 1 }, iap: { loc: 600, days: 2 }, save: { loc: 300, days: 1 }, rank: { loc: 500, days: 2 }, online: { loc: 3000, days: 10 } };

// ---- Tool prices (checked 2026-10-05; verify on each vendor's page) ----
const TOOLS = {
  img: {
    mj:      { name: 'Midjourney', plans: [[10, 200], [30, 900], [60, 1800]], perGen: 4 },      // $/month, fast generations; 4 images per generation
    pixel:   { name: 'PixelLab', perImage: 0.015, perAnim: 0.025 },                               // API, per call
    gptimg:  { name: 'GPT Image (API)', perImage: 0.05 },
    gemini:  { name: 'Gemini (Nano Banana 2)', perImage: 0.067 },                               // API, 1K image
    leonardo:{ name: 'Leonardo', plans: [[12, 8500], [30, 25000], [60, 60000]], perGenCredits: 10 }, // tokens/month; ~10 per image
    scenario:{ name: 'Scenario', plans: [[15, 1500], [45, 5000]], perGenCredits: 5 },             // approx credits per image
  },
  music: { suno: { name: 'Suno', plans: [[10, 500], [30, 2000]] }, none: null },                  // songs/month (2 per generation)
  sfx:   { eleven: { name: 'ElevenLabs', plans: [[6, 30000], [22, 121000], [99, 600000]], perGen: 200, perChar: 1 } },
  code: {
    pro:   { name: 'Claude Pro', monthly: 20, capPerDay: 4e6 },
    max5:  { name: 'Claude Max 5×', monthly: 100, capPerDay: 30e6 },
    max20: { name: 'Claude Max 20×', monthly: 200, capPerDay: 80e6 },
    cursor:{ name: 'Cursor Pro', monthly: 20, capPerDay: 8e6 },
    gemini:{ name: 'Google AI Pro (Gemini)', monthly: 20, capPerDay: 25e6 },
    api:   { name: 'API', monthly: 0 },
  },
  d3:    { meshy: { name: 'Meshy', plans: [[20, 1000], [40, 3000], [100, 8000]], perModel: 20 } },
  video: { higgs: { name: 'Higgsfield', plans: [[15, 200], [39, 1000], [99, 3000]], perClip: 75 } },
};
// Coding with an agent: tokens per active day (mostly cached context re-reads)
const DAY_IN = 20e6, DAY_OUT = 0.4e6, CACHE_HIT = 0.85, CACHE_RATE = 0.1, CODE_SHARE = 0.7;

const state = {
  genre: 'merge', scale: 's', style: 'illust', anim: 'simple', sfx: 'normal', dim: '2d',
  chars: null, music: null, voice: 0, langs: 1, trailer: false,
  feats: new Set(['ads', 'save']), engine: 'unity',
  imgTool: 'mj', codeTool: 'max5', model: 'claude-sonnet-5-5', name: '', idea: '',
};

function plan(plans, need) { // cheapest single plan that covers `need` per month, else the biggest one repeated
  for (const [p, cap] of plans) if (need <= cap) return { price: p, cap };
  const [p, cap] = plans[plans.length - 1];
  return { price: p * Math.ceil(need / cap), cap };
}

function estimate() {
  const S = SCALE[state.scale], g = GENRE[state.genre], a = ANIM[state.anim];
  const chars = state.chars ?? Math.max(1, Math.round(S.chars * g.chars));
  const bg = Math.max(1, Math.round(S.bg * g.bg)), items = Math.round(S.items * g.items), ui = S.ui;
  const music = state.music ?? S.music;
  const sfx = Math.round(S.sfx * SFXLV[state.sfx]);
  let loc = S.loc * g.loc, days = S.days * g.days;
  for (const f of state.feats) { loc += FEAT[f].loc; days += FEAT[f].days; }
  if (state.langs > 1) { days += 0.5 * (state.langs - 1); loc += 150; }
  if (state.dim === '3d') { days *= 1.25; loc *= 1.15; }
  const frames = chars * a.actions * a.frames;
  const images = frames + bg + items + ui;
  const attempts = 3;                                   // keep about 1 of 3 generations
  const gens = images * attempts;
  const codeDays = days * CODE_SHARE;
  const tokIn = codeDays * DAY_IN, tokOut = codeDays * DAY_OUT;
  const months = Math.max(1, Math.ceil(days / 30));

  // --- AI tool costs (scenario 2 = default stack, scenario 3 = user's picks) ---
  const imgCost = tool => {
    const T = TOOLS.img[tool];
    if (T.plans && T.perGen) return plan(T.plans, Math.ceil(gens / T.perGen / months)).price * months;
    if (T.plans) return plan(T.plans, Math.ceil(gens * T.perGenCredits / months)).price * months;
    if (T.perAnim) return (bg + items + ui) * attempts * T.perImage + chars * a.actions * attempts * T.perAnim;
    return gens * T.perImage;
  };
  const musicCost = music ? plan(TOOLS.music.suno.plans, music * 4).price : 0;
  const sfxCredits = sfx * 3 * TOOLS.sfx.eleven.perGen + state.voice * 60 * TOOLS.sfx.eleven.perChar * 2;
  const sfxCost = sfxCredits ? plan(TOOLS.sfx.eleven.plans, sfxCredits).price : 0;
  const p = PRICES[state.model] || { in: 2, out: 10 };
  const apiCode = (tokIn * ((1 - CACHE_HIT) + CACHE_HIT * CACHE_RATE) * p.in + tokOut * p.out) / 1e6;
  const codeCost = tool => {
    const C = TOOLS.code[tool];
    if (tool === 'api') return { cost: apiCode, months: 0, fits: true };
    const perDay = (DAY_IN + DAY_OUT);
    return { cost: C.monthly * months, months, fits: perDay <= C.capPerDay };
  };
  const models3d = state.dim === '3d' ? chars + Math.round(items / 2) + bg : 0;
  const d3Cost = models3d ? plan(TOOLS.d3.meshy.plans, models3d * attempts * TOOLS.d3.meshy.perModel).price : 0;
  const clips = state.trailer ? 8 * attempts : 0;
  const trailerCost = clips ? plan(TOOLS.video.higgs.plans, clips * TOOLS.video.higgs.perClip).price : 0;

  const ai = (img, code) => {
    const c = codeCost(code);
    const lines = [
      ['art', imgCost(img)], ['music', musicCost], ['sfx', sfxCost], ['code', c.cost],
      ...(models3d ? [['d3', d3Cost]] : []), ...(state.trailer ? [['trailer', trailerCost]] : []),
    ];
    const total = lines.reduce((s, [, v]) => s + v, 0);
    return { lines, total, lo: total * 0.7, hi: total * 1.5, codeFits: c.fits };
  };

  return {
    chars, bg, items, ui, frames, images, gens, music, sfx, loc: Math.round(loc / 100) * 100, days: Math.round(days),
    tokIn, tokOut, months, models3d,
    base: ai('mj', 'max5'), mine: ai(state.imgTool, state.codeTool), apiCode,
  };
}

// ---------------- Prompts ----------------
const STYLE_EN = {
  pixel: 'clean 2D pixel art, limited 32-color palette, crisp 1px outlines, no anti-aliasing',
  illust: 'cute 2D hand-drawn illustration, soft cel shading, bold clean outlines, bright friendly colors',
  simple: 'minimal flat vector style, simple geometric shapes, solid colors, no gradients',
};
const GENRE_EN = { puzzle: 'puzzle', racing: 'racing', merge: 'merge', idle: 'idle / incremental', platformer: 'platformer', rpg: 'RPG', novel: 'visual novel', shooter: 'shooter' };
const MOOD = {
  puzzle: ['calm, playful', 95], racing: ['energetic, driving', 140], merge: ['cozy, cheerful', 100], idle: ['relaxed, uplifting', 90],
  platformer: ['bouncy, adventurous', 128], rpg: ['epic, orchestral', 110], novel: ['gentle, emotional piano', 80], shooter: ['intense, electronic', 150],
};
const ENGINE = { unity: 'Unity (C#)', godot: 'Godot 4 (GDScript)', phaser: 'Phaser 3 (TypeScript, web)', flutter: 'Flutter + Flame (Dart)' };

function prompts(e) {
  const name = state.name.trim() || t('defName');
  const idea = state.idea.trim() || t('defIdea', { genre: t('g_' + state.genre) });
  const style = STYLE_EN[state.style] + (state.dim === '3d' ? ', 2.5D low-poly look' : '');
  const feats = [...state.feats].map(f => t('f_' + f)).join(', ') || '-';
  const steps = [t('st1'), t('st2'), t('st3'), t('st4'), ...(state.feats.size ? [t('st5', { feats })] : []), t('st6'), t('st7')];
  const dev = [
    t('devIntro', { name, genre: t('g_' + state.genre), engine: ENGINE[state.engine] }),
    '', t('devIdea') + ' ' + idea,
    t('devScope', { chars: e.chars, bg: e.bg, items: e.items, music: e.music, sfx: e.sfx, langs: state.langs }),
    t('devFeats') + ' ' + feats,
    '', t('devRules'),
    '', t('devSteps'), ...steps.map((s, i) => `${i + 1}. ${s}`),
    '', t('devStart'),
  ].join('\n');

  const head = `Style: ${style}. Game: 2D ${GENRE_EN[state.genre]} mobile game. Transparent background, centered, consistent proportions, no text.`;
  const art = [`# STYLE (use in every prompt)\n${head}\n`];
  const a = ANIM[state.anim];
  const acts = ['idle', 'walk', 'jump', 'attack', 'hurt', 'win'].slice(0, a.actions);
  for (let i = 1; i <= e.chars; i++) {
    art.push(`Character ${i} — full-body game sprite, front 3/4 view. ${head}` +
      (a.actions > 1 ? `\n  Animation sheet: ${acts.map(x => `${x} (${a.frames} frames)`).join(', ')}, same character, evenly spaced on one row each.` : ''));
  }
  for (let i = 1; i <= e.bg; i++) art.push(`Background ${i} — wide 16:9 game background, no characters, leaves space for UI at top and bottom. Style: ${style}.`);
  art.push(`Items (${e.items}) — icon set on a grid, each item a separate 256×256 icon with a soft drop shadow. ${head}`);
  art.push(`UI kit (${e.ui} elements) — buttons (normal/pressed), panels, progress bar, coin and gem icons, close/settings icons, matching the style. ${head}`);
  if (state.imgTool === 'mj') art.push('\nMidjourney: add  --ar 1:1 --style raw  (sprites)  or  --ar 16:9  (backgrounds); use --sref with your first approved image to keep the style.');
  if (state.imgTool === 'leonardo') art.push('\nLeonardo: use a game-asset model with "Transparency" on, and train or pick one Element/style reference from your first approved image to keep every asset consistent.');
  if (state.imgTool === 'gemini') art.push('\nGemini (Nano Banana): paste the STYLE line first, then each asset; attach your first approved image and say "same style as the attached image" to keep it consistent.');
  if (state.imgTool === 'pixel') art.push('\nPixelLab: generate characters at 64×64 or 128×128 with "8 directions" for top-down games, then use "Animate" with the action names above.');

  const [mood, bpm] = MOOD[state.genre];
  const tracks = ['Main menu theme', 'Gameplay loop', 'Gameplay loop (intense)', 'Boss / challenge', 'Shop / break', 'Victory jingle', 'Game over sting', 'Ending theme'].slice(0, e.music);
  const music = tracks.map((tr, i) => `${i + 1}. ${tr} — instrumental, ${mood}, ${bpm + (i === 2 || i === 3 ? 20 : 0)} BPM, ${state.style === 'pixel' ? 'chiptune / 8-bit' : 'light game soundtrack'}, seamless loop, no vocals${i >= 5 ? ', short 5–10 s' : ', 60–90 s'}`).join('\n');

  const sfxBase = ['Button tap', 'Coin pickup', 'Level complete fanfare', 'Fail / lose', 'Item merge pop', 'Power-up', 'Jump', 'Hit', 'Whoosh transition', 'Unlock chime', 'Countdown beep', 'Reward chest open'];
  const sfx = Array.from({ length: Math.min(e.sfx, 40) }, (_, i) => `${i + 1}. ${sfxBase[i % sfxBase.length]}${i >= sfxBase.length ? ` (variation ${Math.floor(i / sfxBase.length) + 1})` : ''} — ${state.style === 'pixel' ? 'retro 8-bit' : 'clean, cartoony'} game sound, ${i % 3 === 0 ? '0.3' : i % 3 === 1 ? '0.6' : '1.2'} s, no music`).join('\n') +
    (e.sfx > 40 ? `\n… +${e.sfx - 40} more in the same format` : '');

  const trailer = state.trailer ? [
    `15-second vertical (9:16) trailer for "${name}", ${GENRE_EN[state.genre]} game. Style: ${style}.`,
    '1. 0–2 s: hook — the most satisfying moment of gameplay, fast zoom in',
    '2. 2–5 s: core loop shown in 2 quick cuts',
    '3. 5–9 s: progression — bigger rewards, new characters/areas',
    '4. 9–12 s: challenge moment, camera shake',
    '5. 12–15 s: logo + "Free on Google Play" end card',
  ].join('\n') : '';
  return { dev, art: art.join('\n\n'), music, sfx, trailer };
}

// ---------------- Render ----------------
function render() {
  const e = estimate();
  const big = (lab, val, sub = '') => `<div class="rounded-xl bg-zinc-950/60 border border-zinc-800 p-3"><div class="text-[11px] uppercase tracking-wider text-zinc-500 font-semibold">${lab}</div><div class="text-xl font-extrabold tabular-nums mt-0.5">${val}</div>${sub ? `<div class="text-xs text-zinc-500 mt-0.5">${sub}</div>` : ''}</div>`;
  $('#gcAssets').innerHTML = [
    big(t('rImages'), e.images.toLocaleString(), t('rImagesSub', { chars: e.chars, frames: e.frames, bg: e.bg, items: e.items, ui: e.ui })),
    big(t('rAudio'), `${e.music} + ${e.sfx}`, t('rAudioSub')),
    big(t('rCode'), '~' + e.loc.toLocaleString(), t('rCodeSub')),
    big(t('rTokens'), fmtTok(e.tokIn + e.tokOut), t('rTokensSub', { api: usd(e.apiCode) })),
  ].join('');

  const lineName = k => t('l_' + k);
  const col = (title, sub, lines, lo, hi, time, hl, note = '') => `
    <div class="rounded-2xl border ${hl ? 'border-violet-500/50 bg-violet-500/5' : 'border-zinc-800 bg-zinc-950/40'} p-4 flex flex-col">
      <div class="text-sm font-bold">${title}</div><div class="text-xs text-zinc-500 mb-3">${sub}</div>
      <div class="text-2xl font-extrabold tabular-nums ${hl ? 'text-violet-200' : ''}">${range(lo, hi)}</div>
      <div class="text-sm text-zinc-400 mb-3">⏱ ${time}</div>
      <table class="w-full text-xs mt-auto"><tbody>${lines.map(([k, v]) => `<tr class="border-t border-zinc-800/70"><td class="py-1.5 text-zinc-400">${lineName(k)}</td><td class="py-1.5 text-end tabular-nums">${Array.isArray(v) ? range(v[0], v[1]) : usd(v)}</td></tr>`).join('')}</tbody></table>
      ${note ? `<p class="text-[11px] text-amber-300/80 mt-2">${note}</p>` : ''}
    </div>`;
  const days = n => t('days', { n });
  const aiTime = `${days(Math.round(e.days * 0.8))} – ${days(Math.round(e.days * 1.3))}`;
  const mineTools = [TOOLS.img[state.imgTool].name, TOOLS.code[state.codeTool].name + (state.codeTool === 'api' ? ` (${(window.T.modelNames || {})[state.model] || state.model})` : '')].join(' + ');
  $('#gcCompare').innerHTML =
    col(t('cAi'), 'Midjourney + Suno + ElevenLabs + Claude Max 5×', e.base.lines, e.base.lo, e.base.hi, aiTime, true) +
    col(t('cMine'), mineTools, e.mine.lines, e.mine.lo, e.mine.hi, aiTime, false, e.mine.codeFits ? '' : t('capWarn'));

  const HIRE_MIN = { s: 5000, m: 15000, l: 30000 };
  $('#gcRef').innerHTML = t('hireRef', { min: usd(HIRE_MIN[state.scale] * (state.dim === '3d' ? 1.5 : 1)) });
  const P = prompts(e);
  window.__gcPrompts = P;
  for (const k of ['dev', 'art', 'music', 'sfx', 'trailer']) {
    const el = document.getElementById('gcP_' + k);
    if (el) el.textContent = P[k] || t('noTrailer');
  }
  document.getElementById('gcTab_trailer').classList.toggle('opacity-40', !state.trailer);
}

// ---------------- Wire up ----------------
function seg(id, key, cast = v => v) {
  const box = document.getElementById(id);
  if (!box) return;
  const paint = () => box.querySelectorAll('button').forEach(b => {
    const on = String(state[key]) === b.dataset.v;
    b.classList.toggle('tab-active', on); b.classList.toggle('text-zinc-400', !on); b.setAttribute('aria-pressed', on);
  });
  box.addEventListener('click', ev => {
    const b = ev.target.closest('button'); if (!b) return;
    state[key] = cast(b.dataset.v);
    if (key === 'scale' || key === 'genre') { state.chars = null; state.music = null; syncNums(); }
    paint(); render();
  });
  paint();
}
function syncNums() {
  const e = estimate();
  $('#gcChars').value = e.chars; $('#gcMusic').value = e.music;
}
function num(id, key) {
  document.getElementById(id).addEventListener('input', ev => {
    const v = parseInt(ev.target.value, 10);
    state[key] = Number.isFinite(v) && v >= 0 ? Math.min(v, 500) : null; render();
  });
}

seg('gcGenre', 'genre'); seg('gcScale', 'scale'); seg('gcStyle', 'style'); seg('gcAnim', 'anim'); seg('gcSfx', 'sfx');
seg('gcDim', 'dim'); seg('gcEngine', 'engine'); seg('gcImg', 'imgTool'); seg('gcCodeTool', 'codeTool');
seg('gcTrailer', 'trailer', v => v === 'true');
num('gcChars', 'chars'); num('gcMusic', 'music'); num('gcVoice', 'voice');
document.getElementById('gcLangs').addEventListener('input', ev => { state.langs = Math.max(1, Math.min(41, parseInt(ev.target.value, 10) || 1)); render(); });
document.getElementById('gcFeats').addEventListener('change', ev => {
  const c = ev.target; if (!c.dataset.f) return;
  c.checked ? state.feats.add(c.dataset.f) : state.feats.delete(c.dataset.f); render();
});
document.getElementById('gcModel').addEventListener('change', ev => { state.model = ev.target.value; render(); });
for (const id of ['gcName', 'gcIdea']) document.getElementById(id).addEventListener('input', ev => { state[id === 'gcName' ? 'name' : 'idea'] = ev.target.value; render(); });

// Prompt tabs, copy, download
const tabs = document.getElementById('gcTabs');
tabs.addEventListener('click', ev => {
  const b = ev.target.closest('button'); if (!b) return;
  tabs.querySelectorAll('button').forEach(x => { const on = x === b; x.classList.toggle('tab-active', on); x.classList.toggle('text-zinc-400', !on); });
  document.querySelectorAll('[data-pane]').forEach(p => p.hidden = p.dataset.pane !== b.dataset.v);
});
document.querySelectorAll('[data-copy]').forEach(btn => btn.addEventListener('click', async () => {
  const txt = document.getElementById('gcP_' + btn.dataset.copy).textContent;
  try { await navigator.clipboard.writeText(txt); } catch (_) {
    const r = document.createRange(); r.selectNodeContents(document.getElementById('gcP_' + btn.dataset.copy));
    const s = getSelection(); s.removeAllRanges(); s.addRange(r);
  }
  const old = btn.textContent; btn.textContent = t('copied'); setTimeout(() => (btn.textContent = old), 1400);
}));
document.getElementById('gcDownload').addEventListener('click', () => {
  const P = window.__gcPrompts || {};
  const name = (state.name.trim() || 'my-game').replace(/[^\w가-힣ぁ-んァ-ン一-龥-]+/g, '-');
  const md = [`# ${state.name.trim() || t('defName')} — ${t('packTitle')}`, `\n## ${t('tDev')}\n\n${P.dev}`, `\n## ${t('tArt')}\n\n${P.art}`,
    `\n## ${t('tMusic')} (Suno)\n\n${P.music}`, `\n## ${t('tSfx')} (ElevenLabs)\n\n${P.sfx}`, ...(state.trailer ? [`\n## ${t('tTrailer')} (Higgsfield)\n\n${P.trailer}`] : []),
    `\n---\nhttps://tokensave.app`].join('\n');
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([md], { type: 'text/markdown' }));
  a.download = `${name}-prompts.md`; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 2000);
});

syncNums();
render();
