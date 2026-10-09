// TokenSave — AI Image Cost Calculator page (tokensave.app/image)
// Prices: USD per generated image, checked 2026-10-05.
//   official = the model maker's own API pricing page
//   runway   = Runway API pricing page (1 credit = $0.01)
// Sources:
//   Nano Banana 2 / 2 Lite .... ai.google.dev/gemini-api/docs/pricing
//   Grok Imagine .............. docs.x.ai/developers/pricing (Imagine API)
//   FLUX.2 .................... bfl.ai/pricing (first MP + each additional MP; 1 MP = 1024x1024, max 4 MP)
//   Luma Uni-1.1 .............. lumalabs.ai/api/pricing (text-to-image at 2048px)
//   GPT Image, Nano Banana Pro, Nano Banana (2.5 Flash), Seedream 5, Runway Gen-4 Image ... docs.dev.runwayml.com/guides/pricing
// Resolutions: 0.5k = 512px, 1k = 1024px, 2k = 2048px (4 MP), 4k = 4096px (16 MP)

import { tr, fx } from './common.js';

// FLUX.2: output billed per megapixel, rounded up; 0.5K rounds up to 1 MP, 2K = 4 MP, 4K not offered (max 4 MP)
const flux = (first, extra) => ({ '0.5k': first, '1k': first, '2k': first + 3 * extra });

const MODELS = [
  { name: 'Nano Banana 2',               sub: 'Gemini 3.1 Flash Image', by: 'Google', src: 'official',
    p: { '0.5k': 0.045, '1k': 0.067, '2k': 0.101, '4k': 0.151 } },
  { name: 'Nano Banana 2 Lite',          sub: 'Gemini 3.1 Flash Lite Image', by: 'Google', src: 'official',
    p: { '1k': 0.0336 } },
  { name: 'Nano Banana Pro',             sub: 'Gemini 3 Pro Image', by: 'Google', src: 'runway',
    p: { '1k': 0.20, '2k': 0.20, '4k': 0.40 } },
  { name: 'Nano Banana',                 sub: 'Gemini 2.5 Flash Image', by: 'Google', src: 'runway',
    p: { '1k': 0.05 } },
  { name: 'GPT Image 2.5 · low',         by: 'OpenAI', src: 'runway', p: { '1k': 0.01, '2k': 0.01, '4k': 0.02 } },
  { name: 'GPT Image 2.5 · medium',      by: 'OpenAI', src: 'runway', p: { '1k': 0.05, '2k': 0.05, '4k': 0.11 } },
  { name: 'GPT Image 2.5 · high',        by: 'OpenAI', src: 'runway', p: { '1k': 0.16, '2k': 0.16, '4k': 0.19 } },
  { name: 'GPT Image 2.5 · xhigh',       by: 'OpenAI', src: 'runway', p: { '1k': 0.28, '2k': 0.28, '4k': 0.34 } },
  { name: 'GPT Image 2.5 · max',         by: 'OpenAI', src: 'runway', p: { '1k': 0.63, '2k': 0.63, '4k': 0.76 } },
  { name: 'GPT Image 2 · medium',        by: 'OpenAI', src: 'runway', p: { '1k': 0.05, '2k': 0.05, '4k': 0.11 } },
  { name: 'GPT Image 2 · high',          by: 'OpenAI', src: 'runway', p: { '1k': 0.20, '2k': 0.20, '4k': 0.41 } },
  { name: 'FLUX.2 [max]',                by: 'Black Forest Labs', src: 'official', p: flux(0.07, 0.03) },
  { name: 'FLUX.2 [pro]',                by: 'Black Forest Labs', src: 'official', p: flux(0.03, 0.015) },
  { name: 'FLUX.2 [flex]',               by: 'Black Forest Labs', src: 'official', p: flux(0.05, 0.05) },
  { name: 'FLUX.2 [klein] 9B',           by: 'Black Forest Labs', src: 'official', p: flux(0.015, 0.002) },
  { name: 'FLUX.2 [klein] 4B',           by: 'Black Forest Labs', src: 'official', p: flux(0.014, 0.001) },
  { name: 'Grok Imagine Image 2.0 · low',    by: 'xAI', src: 'official', p: { '1k': 0.04, '2k': 0.06 } },
  { name: 'Grok Imagine Image 2.0 · medium', by: 'xAI', src: 'official', p: { '1k': 0.06, '2k': 0.08 } },
  { name: 'Grok Imagine Image Quality',  by: 'xAI', src: 'official', p: { '1k': 0.05, '2k': 0.07 } },
  { name: 'Grok Imagine Image',          by: 'xAI', src: 'official', p: { '1k': 0.02, '2k': 0.02 } },
  { name: 'Seedream 5 Pro',              by: 'ByteDance', src: 'runway', p: { '1k': 0.05, '2k': 0.09 } },
  { name: 'Seedream 5 Lite',             by: 'ByteDance', src: 'runway', p: { '1k': 0.04, '2k': 0.04 } },
  { name: 'Luma Uni-1.1',                by: 'Luma AI', src: 'official', p: { '2k': 0.0404 } },
  { name: 'Luma Uni-1.1 Max',            by: 'Luma AI', src: 'official', p: { '2k': 0.10 } },
  { name: 'Runway Gen-4 Image',          by: 'Runway', src: 'official', p: { '0.5k': 0.05, '1k': 0.08 },
    label: { '0.5k': '720p', '1k': '1080p' } },
  { name: 'Runway Gen-4 Image Turbo',    by: 'Runway', src: 'official', p: { '0.5k': 0.02, '1k': 0.02 } },
];

const $ = id => document.getElementById(id);
const els = { count: $('iCount'), list: $('iResults') };
const state = { res: '1k' };

const money = n => fx(n, '$' + (n < 0.1 ? n.toFixed(n < 0.01 ? 4 : 3) : n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })));
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

function compute() {
  const count = Math.max(1, Math.min(1000000, Math.round(+els.count.value || 1)));
  const rows = MODELS.map(m => {
    const per = m.p[state.res];
    return per == null ? { m, na: true } : { m, per, total: per * count };
  });
  const ok = rows.filter(r => !r.na).sort((x, y) => x.total - y.total);
  const bad = rows.filter(r => r.na);
  const cheapest = ok.length ? ok[0].total : null;

  els.list.innerHTML = ok.map(r => {
    const tags = [
      r.m.src === 'official' ? tr('srcOfficial') : tr('srcRunway'),
      r.m.sub || '',
      r.m.label && r.m.label[state.res] ? r.m.label[state.res] : '',
    ].filter(Boolean).map(t => `<span class="px-1.5 py-0.5 rounded bg-zinc-800 text-zinc-400">${esc(t)}</span>`).join(' ');
    const best = r.total === cheapest
      ? ` <span class="ms-1 text-[10px] font-bold px-1.5 py-0.5 rounded-full bg-emerald-500/15 text-emerald-300">${esc(tr('cheapest'))}</span>` : '';
    return `<li class="grid grid-cols-12 gap-x-3 gap-y-1 px-5 py-3 items-center ${r.total === cheapest ? 'bg-emerald-500/5' : ''}">
      <div class="col-span-12 sm:col-span-6">
        <div class="font-semibold text-sm"><span class="ltr inline-block">${esc(r.m.name)}</span>${best}</div>
        <div class="text-[11px] text-zinc-500 mt-0.5 flex flex-wrap gap-1 items-center"><span>${esc(r.m.by)}</span> ${tags}</div>
      </div>
      <div class="col-span-6 sm:col-span-3 text-end tabular-nums text-sm text-zinc-300"><span class="ltr inline-block">${money(r.per)}</span></div>
      <div class="col-span-6 sm:col-span-3 text-end tabular-nums text-base font-bold"><span class="ltr inline-block">${money(r.total)}</span></div>
    </li>`;
  }).join('') + bad.map(r => `<li class="grid grid-cols-12 gap-3 px-5 py-2.5 items-center opacity-45">
      <div class="col-span-7 sm:col-span-6 text-sm"><span class="ltr inline-block">${esc(r.m.name)}</span> <span class="text-[11px] text-zinc-500">${esc(r.m.by)}</span></div>
      <div class="col-span-5 sm:col-span-6 text-end text-xs text-zinc-500">${esc(tr('na'))}</div>
    </li>`).join('');
}

const btns = document.querySelectorAll('#resTabs button');
btns.forEach(b => b.addEventListener('click', () => {
  state.res = b.dataset.res;
  btns.forEach(x => x.classList.toggle('tab-active', x === b));
  compute();
}));
btns.forEach(x => x.classList.toggle('tab-active', x.dataset.res === state.res));
document.querySelectorAll('#countPresets button').forEach(b =>
  b.addEventListener('click', () => { els.count.value = b.dataset.count; compute(); }));
els.count.addEventListener('input', compute);
compute();
