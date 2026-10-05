// TokenSave — AI Video Cost Calculator page (tokensave.app/video)
// Prices: USD list prices, checked 2026-10-05.
//   official = the model maker's own API pricing page
//   runway   = Runway API pricing page (1 credit = $0.01), used where the maker has no public per-second API price
// Sources:
//   Veo 3.1 ........ ai.google.dev/gemini-api/docs/pricing (audio included by default)
//   Kling .......... kling.ai/dev/pricing (1 unit = $0.14 list)
//   Runway, Seedance, Hailuo, Wan, HappyHorse, Gemini Omni Flash ... docs.dev.runwayml.com/guides/pricing
//   Luma Ray 3.2 ... lumalabs.ai/api/pricing (billed per 5 s / 10 s clip)
//   Grok Imagine ... docs.x.ai/developers/pricing (Imagine API)
//   FLUX 3 Video ... bfl.ai/pricing (text/image-to-video; HD=720p, FHD=1080p, UHD=4K; audio included)
// Sora 2 is excluded: OpenAI removed it from the API on 2026-09-24.

import { tr } from './common.js';

// p: { resolution: { a: price per second WITH audio, n: price per second WITHOUT audio, label?: exact resolution } }
// A price of null means that option is not offered.
const both = (x, label) => ({ a: x, n: x, label });
const silent = (x, label) => ({ a: null, n: x, label });

const MODELS = [
  { name: 'Veo 3.1',            by: 'Google',    src: 'official', audioIncl: true,
    p: { '720': both(0.40), '1080': both(0.40), '4k': both(0.60) } },
  { name: 'Veo 3.1 Fast',       by: 'Google',    src: 'official', audioIncl: true,
    p: { '720': both(0.10), '1080': both(0.12), '4k': both(0.30) } },
  { name: 'Veo 3.1 Lite',       by: 'Google',    src: 'official', audioIncl: true,
    p: { '720': both(0.05), '1080': both(0.08) } },
  { name: 'Kling 3.0',          by: 'Kuaishou',  src: 'official',
    p: { '720': { a: 0.126, n: 0.084 }, '1080': { a: 0.168, n: 0.112 }, '4k': both(0.42) } },
  { name: 'Kling 3.0 Turbo',    by: 'Kuaishou',  src: 'official',
    p: { '720': both(0.112), '1080': both(0.14) } },
  { name: 'Runway Gen-4.5',     by: 'Runway',    src: 'official',
    p: { '720': silent(0.12) } },
  { name: 'Runway Gen-4 Turbo', by: 'Runway',    src: 'official',
    p: { '720': silent(0.05) } },
  { name: 'Luma Ray 3.2',       by: 'Luma AI',   src: 'official', clipBilled: true,
    // price per 5 s clip / 10 s clip
    p: { '480': { a: null, n: [0.15, 0.45], label: '540p' }, '720': { a: null, n: [0.30, 0.90] }, '1080': { a: null, n: [1.20, 3.60] } } },
  { name: 'Grok Imagine Video 1.5', by: 'xAI',   src: 'official',
    p: { '480': both(0.08), '720': both(0.14), '1080': both(0.25) } },
  { name: 'Grok Imagine Video 1.5 Lite', by: 'xAI', src: 'official',
    p: { '480': both(0.02), '720': both(0.03), '1080': both(0.14) } },
  { name: 'Grok Imagine Video', by: 'xAI',       src: 'official',
    p: { '480': both(0.05), '720': both(0.07) } },
  { name: 'FLUX 3 Video',       by: 'Black Forest Labs', src: 'official', audioIncl: true,
    p: { '720': both(0.17), '1080': both(0.29), '4k': both(0.80) } },
  { name: 'FLUX 3 Video Draft', by: 'Black Forest Labs', src: 'official', audioIncl: true,
    p: { '720': both(0.06) } },
  { name: 'Seedance 2.0',       by: 'ByteDance', src: 'runway',
    p: { '480': both(0.36), '720': both(0.36), '1080': both(0.40), '4k': both(1.50) } },
  { name: 'Seedance 2.0 Fast',  by: 'ByteDance', src: 'runway',
    p: { '480': both(0.29), '720': both(0.29) } },
  { name: 'Seedance 2.5',       by: 'ByteDance', src: 'runway',
    p: { '480': both(0.20), '720': both(0.30), '1080': both(0.68) } },
  { name: 'Seedance 2 Mini',    by: 'ByteDance', src: 'runway',
    p: { '480': both(0.16), '720': both(0.16) } },
  { name: 'Hailuo 3',           by: 'MiniMax',   src: 'runway',
    p: { '720': both(0.10, '768p'), '1080': both(0.15, '2K') } },
  { name: 'Wan 3.0',            by: 'Alibaba',   src: 'runway',
    p: { '480': both(0.05), '720': both(0.10), '1080': both(0.20) } },
  { name: 'Wan 3.0 Prime',      by: 'Alibaba',   src: 'runway',
    p: { '480': both(0.068), '720': both(0.14), '1080': both(0.28) } },
  { name: 'HappyHorse 1.0',     by: 'Alibaba',   src: 'runway',
    p: { '720': both(0.15), '1080': both(0.30) } },
  { name: 'Gemini Omni Flash',  by: 'Google',    src: 'runway',
    p: { '720': both(0.10), '1080': both(0.15), '4k': both(0.30) } },
];

// Luma: billed per 5 s or 10 s clip; longer videos = several clips
function lumaClipCost([p5, p10], secs) {
  let cost = Math.floor(secs / 10) * p10;
  const rem = secs % 10;
  if (rem > 5) cost += p10; else if (rem > 0) cost += p5;
  return cost;
}

const $ = id => document.getElementById(id);
const els = { len: $('vLen'), clips: $('vClips'), list: $('vResults') };
const state = { res: '720', audio: '1' };

const money = n => '$' + (n < 0.1 ? n.toFixed(3) : n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

function compute() {
  const secs = Math.max(1, Math.min(600, Math.round(+els.len.value || 1)));
  const clips = Math.max(1, Math.min(10000, Math.round(+els.clips.value || 1)));
  const wantAudio = state.audio === '1';

  const rows = MODELS.map(m => {
    const cell = m.p[state.res];
    if (!cell) return { m, reason: tr('na') };
    const rate = wantAudio ? cell.a : cell.n;
    if (rate == null) return { m, reason: tr('noAudio') };
    const perClip = m.clipBilled ? lumaClipCost(rate, secs) : rate * secs;
    return { m, cell, perSec: perClip / secs, perClip, total: perClip * clips };
  });

  const ok = rows.filter(r => !r.reason).sort((x, y) => x.total - y.total);
  const bad = rows.filter(r => r.reason);
  const cheapest = ok.length ? ok[0].total : null;

  els.list.innerHTML = ok.map(r => {
    const tags = [
      r.m.src === 'official' ? tr('srcOfficial') : tr('srcRunway'),
      r.m.audioIncl ? tr('audioIncl') : '',
      r.cell.label ? r.cell.label : '',
      r.m.clipBilled ? tr('clipNote') : '',
    ].filter(Boolean).map(t => `<span class="px-1.5 py-0.5 rounded bg-zinc-800 text-zinc-400">${esc(t)}</span>`).join(' ');
    const best = r.total === cheapest
      ? ` <span class="ms-1 text-[10px] font-bold px-1.5 py-0.5 rounded-full bg-emerald-500/15 text-emerald-300">${esc(tr('cheapest'))}</span>` : '';
    return `<li class="grid grid-cols-12 gap-x-3 gap-y-1 px-5 py-3 items-center ${r.total === cheapest ? 'bg-emerald-500/5' : ''}">
      <div class="col-span-12 sm:col-span-5">
        <div class="font-semibold text-sm"><span class="ltr inline-block">${esc(r.m.name)}</span>${best}</div>
        <div class="text-[11px] text-zinc-500 mt-0.5 flex flex-wrap gap-1 items-center"><span>${esc(r.m.by)}</span> ${tags}</div>
      </div>
      <div class="col-span-4 sm:col-span-2 text-end tabular-nums text-sm text-zinc-300"><span class="ltr inline-block">${money(r.perSec)}<span class="text-zinc-500">/s</span></span></div>
      <div class="col-span-4 sm:col-span-2 text-end tabular-nums text-sm text-zinc-300"><span class="ltr inline-block">${money(r.perClip)}</span></div>
      <div class="col-span-4 sm:col-span-3 text-end tabular-nums text-base font-bold"><span class="ltr inline-block">${money(r.total)}</span></div>
    </li>`;
  }).join('') + bad.map(r => `<li class="grid grid-cols-12 gap-3 px-5 py-2.5 items-center opacity-45">
      <div class="col-span-7 sm:col-span-5 text-sm"><span class="ltr inline-block">${esc(r.m.name)}</span> <span class="text-[11px] text-zinc-500">${esc(r.m.by)}</span></div>
      <div class="col-span-5 sm:col-span-7 text-end text-xs text-zinc-500">${esc(r.reason)}</div>
    </li>`).join('');
}

function bindTabs(containerId, key, attr) {
  const btns = document.querySelectorAll(`#${containerId} button`);
  btns.forEach(b => b.addEventListener('click', () => {
    state[key] = b.dataset[attr];
    btns.forEach(x => x.classList.toggle('tab-active', x === b));
    compute();
  }));
  btns.forEach(x => x.classList.toggle('tab-active', x.dataset[attr] === state[key]));
}

bindTabs('resTabs', 'res', 'res');
bindTabs('audioTabs', 'audio', 'audio');
document.querySelectorAll('#lenPresets button').forEach(b =>
  b.addEventListener('click', () => { els.len.value = b.dataset.len; compute(); }));
els.len.addEventListener('input', compute);
els.clips.addEventListener('input', compute);
compute();
