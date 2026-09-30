# -*- coding: utf-8 -*-
SLUG = "no"
TAG = "no"
NATIVE = "Norsk"
OG = "nb_NO"
DIR = "ltr"

S = dict(
    a1="Et token er en tekstbit som en AI-modell leser. På engelsk tilsvarer 1 token omtrent 4 tegn eller ¾ av et ord.",
    a2="Tokenizere trenes mest på engelsk, så norsk, koreansk, japansk og mange andre språk deles opp i flere tokens for samme innhold.",
    a3="Ja. Alt kjører lokalt i nettleseren din. Teksten din sendes aldri til noen server.",
    asIn="Som input",
    asOut="Som output",
    badge="100 % i nettleseren · Ingenting lastes opp",
    based="o200k-basert",
    chars="Tegn",
    clear="Tøm",
    copy="Kopier",
    cost="Anslått kostnad",
    desc="Gratis AI-tokenteller for GPT, Claude og Gemini. Tell tokens, tegn og anslått API-kostnad direkte i nettleseren, på alle språk. Ingenting lastes opp.",
    eff="Språkeffektivitet",
    efficient="{p} % effektiv",
    est="Anslått",
    exact="Nøyaktig (o200k)",
    f1="OpenAI-modeller telles med o200k-tokenizeren. Tallene for Claude og Gemini er anslag.",
    f2="Prisene er listepriser per 1M tokens, sist sjekket i september 2026. Sjekk alltid leverandørens prisside.",
    great="Utmerket",
    h1="AI-tokenteller",
    high="Mye tokensløsing",
    lang="Språk",
    moderate="Moderat sløsing",
    note="{name}: ${in} input / ${out} output per 1M tokens",
    optimize="Rydd mellomrom",
    optimizeTip="Fjern overflødige mellomrom og tomme linjer",
    ph1="Lim inn eller skriv prompten din her...",
    ph2="Tokens, tegn og anslått kostnad oppdateres med én gang mens du skriver. Fungerer på alle språk.",
    prompt="Prompten din",
    q1="Hva er et token?",
    q2="Hvorfor koster andre språk mer?",
    q3="Er teksten min privat?",
    share="Ikke-engelsk andel: {p} %",
    sub="Tell tokens, tegn og API-kostnad i sanntid – på alle språk.",
    tAlready="Allerede optimalisert",
    tCleared="Tømt",
    tCopied="Kopiert til utklippstavlen",
    tNothing="Ingenting å kopiere",
    tSaved="Optimalisert – sparte {n} tokens",
    tip="Tips: Ikke-latinske skriftsystemer koster vanligvis flere tokens for samme innhold. En systemprompt på engelsk kan senke kostnaden.",
    title="AI-tokenteller for GPT, Claude og Gemini – TokenSave",
    tokens="Tokens",
    waste="{x}x tokensløsing",
    words="Ord",
)

V = dict(
    a1="De fleste video-API-er tar betalt per sekund generert video. Høyere oppløsning og innebygd lyd koster mer, så et klipp i 1080p eller 4K kan koste flere ganger så mye som et i 720p.",
    a2="Det avhenger av oppløsningen. Lette modeller som Veo 3.1 Lite, Grok Imagine og Wan starter rundt $0.05 per sekund, mens premiummodeller i 4K kan koste $0.40 per sekund eller mer.",
    a3="Nei. OpenAI fjernet Sora 2-videomodellene fra API-et sitt 24. september 2026, så Sora er ikke lenger tilgjengelig for utviklere.",
    audio="Lyd",
    audioIncl="Lyd inkludert",
    audioOff="Uten lyd",
    audioOn="Med lyd",
    badge="Offisielle API-priser · Oppdatert september 2026",
    cheapest="Billigst",
    clipNote="Belastes per klipp på 5/10 s",
    clips="Antall klipp",
    desc="Sammenlign API-kostnaden for AI-videomodeller: Veo 3.1, Kling 3.0, Runway Gen-4.5, Luma Ray, Grok Imagine, Seedance og flere. Velg lengde, oppløsning og lyd, og se prisen per klipp med én gang.",
    f1="Offisielle listepriser fra hver leverandørs API-prisside, sjekket 30. september 2026. Modeller uten offentlig API-pris per sekund vises med Runways API-priser.",
    f2="Prisene endres ofte – sjekk leverandørens side før store jobber.",
    h1="Kostnadskalkulator for AI-video",
    len="Lengde per klipp (sekunder)",
    model="Modell",
    na="Tilbys ikke i denne oppløsningen",
    noAudio="Ingen innebygd lyd",
    notes="Prisene gjelder per sekund generert video. Skatter, volumrabatter og mislykkede genereringer er ikke inkludert.",
    perClip="Per klipp",
    perSec="Per sekund",
    q1="Hvordan prises AI-video?",
    q2="Hva er den billigste AI-videomodellen?",
    q3="Er Sora med?",
    res="Oppløsning",
    srcOfficial="Offisiell pris",
    srcRunway="Via Runway API",
    sub="Se hva den samme videoen koster i alle de store AI-videomodellene.",
    title="Kostnadskalkulator for AI-video – priser for Veo 3.1, Kling, Runway, Luma | TokenSave",
    total="Totalt",
)

I = dict(
    a1="De fleste bilde-API-er tar en fast pris per bilde som øker med oppløsningen. OpenAI-modeller koster også mer ved høyere kvalitet, og FLUX tar betalt per megapiksel.",
    a2="Små modeller som FLUX.2 [klein], Grok Imagine og GPT Image i lav kvalitet koster rundt $0.01–0.02 per bilde. Premiummodeller i 4K kan koste $0.15–0.40 per bilde.",
    a3="Nano Banana er kallenavnet på Googles Gemini-bildemodeller. Nano Banana 2 er Gemini 3.1 Flash Image, og Nano Banana Pro er Gemini 3 Pro Image.",
    count="Antall bilder",
    desc="Sammenlign API-kostnaden per bilde for Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream og Runway. Velg oppløsning og antall, og se totalen med én gang.",
    f1="Offisielle listepriser fra hver leverandørs API-prisside, sjekket 30. september 2026. OpenAI og Nano Banana Pro vises med Runways API-priser.",
    h1="Kostnadskalkulator for AI-bilder",
    notes="Prisene gjelder per generert bilde. Gebyrer for referansebilder, skatter og volumrabatter er ikke inkludert.",
    perImg="Per bilde",
    q1="Hvordan prises generering av AI-bilder?",
    q2="Hva er den billigste AI-bildemodellen?",
    q3="Hva er Nano Banana?",
    sub="Se hva de samme bildene koster i alle de store AI-bildemodellene.",
    title="Kostnadskalkulator for AI-bilder – priser for Nano Banana, GPT Image, FLUX, Grok | TokenSave",
)

NAV = dict(navToken="Tokenteller", navVideo="Videokostnad", navImage="Bildekostnad")

SITE = dict(fAbout="Om oss", fPrivacy="Personvern", viewIn="Vis siden på norsk")

META = {
    "token": ("AI-tokenteller – GPT, Claude, Gemini", "Tell tokens, tegn og API-kostnad for GPT, Claude og Gemini. Gratis og privat."),
    "video": ("AI-videokostnad – Veo, Kling, Runway", "Sammenlign API-priser for Veo 3.1, Kling, Runway, Luma m.fl. per sekund."),
    "image": ("AI-bildekostnad – Nano Banana, GPT", "Sammenlign API-priser per bilde: Nano Banana, GPT Image, FLUX, Grok m.fl."),
}
