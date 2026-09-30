# -*- coding: utf-8 -*-
SLUG = "da"
TAG = "da"
NATIVE = "Dansk"
OG = "da_DK"
DIR = "ltr"

S = dict(
    a1="Et token er et stykke tekst, som en AI-model læser. På engelsk svarer 1 token til cirka 4 tegn eller ¾ af et ord.",
    a2="Tokenizere trænes mest på engelsk, så dansk, koreansk, japansk og mange andre sprog deles op i flere tokens for det samme indhold.",
    a3="Ja. Alt kører lokalt i din browser. Din tekst sendes aldrig til nogen server.",
    asIn="Som input",
    asOut="Som output",
    badge="100 % i browseren · Intet uploades",
    based="o200k-baseret",
    chars="Tegn",
    clear="Ryd",
    copy="Kopiér",
    cost="Anslået pris",
    desc="Gratis AI-tokentæller til GPT, Claude og Gemini. Tæl tokens, tegn og anslået API-pris direkte i browseren, på alle sprog. Intet uploades.",
    eff="Sprogeffektivitet",
    efficient="{p} % effektiv",
    est="Anslået",
    exact="Præcis (o200k)",
    f1="OpenAI-modeller tælles med o200k-tokenizeren. Tallene for Claude og Gemini er skøn.",
    f2="Priserne er listepriser pr. 1M tokens, senest tjekket i september 2026. Tjek altid udbyderens prisside.",
    great="Fremragende",
    h1="AI-tokentæller",
    high="Højt tokenspild",
    lang="Sprog",
    moderate="Moderat spild",
    note="{name}: ${in} input / ${out} output pr. 1M tokens",
    optimize="Ryd mellemrum",
    optimizeTip="Fjern overflødige mellemrum og tomme linjer",
    ph1="Indsæt eller skriv din prompt her...",
    ph2="Tokens, tegn og anslået pris opdateres med det samme, mens du skriver. Virker på alle sprog.",
    prompt="Din prompt",
    q1="Hvad er et token?",
    q2="Hvorfor koster andre sprog mere?",
    q3="Er min tekst privat?",
    share="Ikke-engelsk andel: {p} %",
    sub="Tæl tokens, tegn og API-pris i realtid – på alle sprog.",
    tAlready="Allerede optimeret",
    tCleared="Ryddet",
    tCopied="Kopieret til udklipsholderen",
    tNothing="Intet at kopiere",
    tSaved="Optimeret – sparede {n} tokens",
    tip="Tip: Ikke-latinske skriftsystemer koster som regel flere tokens for det samme indhold. En systemprompt på engelsk kan sænke prisen.",
    title="AI-tokentæller til GPT, Claude og Gemini – TokenSave",
    tokens="Tokens",
    waste="{x}x tokenspild",
    words="Ord",
)

V = dict(
    a1="De fleste video-API'er tager betaling pr. sekund genereret video. Højere opløsning og indbygget lyd koster mere, så et klip i 1080p eller 4K kan koste flere gange så meget som et i 720p.",
    a2="Det afhænger af opløsningen. Lette modeller som Veo 3.1 Lite, Grok Imagine og Wan starter omkring $0.05 pr. sekund, mens premiummodeller i 4K kan koste $0.40 pr. sekund eller mere.",
    a3="Nej. OpenAI fjernede Sora 2-videomodellerne fra sit API den 24. september 2026, så Sora er ikke længere tilgængelig for udviklere.",
    audio="Lyd",
    audioIncl="Lyd inkluderet",
    audioOff="Uden lyd",
    audioOn="Med lyd",
    badge="Officielle API-priser · Opdateret september 2026",
    cheapest="Billigst",
    clipNote="Afregnes pr. klip på 5/10 s",
    clips="Antal klip",
    desc="Sammenlign API-prisen for AI-videomodeller: Veo 3.1, Kling 3.0, Runway Gen-4.5, Luma Ray, Grok Imagine, Seedance og flere. Vælg længde, opløsning og lyd, og se prisen pr. klip med det samme.",
    f1="Officielle listepriser fra hver udbyders API-prisside, tjekket den 30. september 2026. Modeller uden offentlig API-pris pr. sekund vises med Runways API-priser.",
    f2="Priserne ændrer sig ofte – tjek udbyderens side før store opgaver.",
    h1="Prisberegner til AI-video",
    len="Længde pr. klip (sekunder)",
    model="Model",
    na="Tilbydes ikke i denne opløsning",
    noAudio="Ingen indbygget lyd",
    notes="Priserne gælder pr. sekund genereret video. Skatter, mængderabatter og mislykkede genereringer er ikke medregnet.",
    perClip="Pr. klip",
    perSec="Pr. sekund",
    q1="Hvordan prissættes AI-video?",
    q2="Hvad er den billigste AI-videomodel?",
    q3="Er Sora med?",
    res="Opløsning",
    srcOfficial="Officiel pris",
    srcRunway="Via Runway API",
    sub="Se, hvad den samme video koster i alle de store AI-videomodeller.",
    title="Prisberegner til AI-video – priser for Veo 3.1, Kling, Runway, Luma | TokenSave",
    total="I alt",
)

I = dict(
    a1="De fleste billed-API'er tager en fast pris pr. billede, som stiger med opløsningen. OpenAI-modeller koster også mere ved højere kvalitet, og FLUX afregner pr. megapixel.",
    a2="Små modeller som FLUX.2 [klein], Grok Imagine og GPT Image i lav kvalitet koster omkring $0.01–0.02 pr. billede. Premiummodeller i 4K kan koste $0.15–0.40 pr. billede.",
    a3="Nano Banana er kælenavnet for Googles Gemini-billedmodeller. Nano Banana 2 er Gemini 3.1 Flash Image, og Nano Banana Pro er Gemini 3 Pro Image.",
    count="Antal billeder",
    desc="Sammenlign API-prisen pr. billede for Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream og Runway. Vælg opløsning og antal, og se totalen med det samme.",
    f1="Officielle listepriser fra hver udbyders API-prisside, tjekket den 30. september 2026. OpenAI og Nano Banana Pro vises med Runways API-priser.",
    h1="Prisberegner til AI-billeder",
    notes="Priserne gælder pr. genereret billede. Gebyrer for referencebilleder, skatter og mængderabatter er ikke medregnet.",
    perImg="Pr. billede",
    q1="Hvordan prissættes AI-billedgenerering?",
    q2="Hvad er den billigste AI-billedmodel?",
    q3="Hvad er Nano Banana?",
    sub="Se, hvad de samme billeder koster i alle de store AI-billedmodeller.",
    title="Prisberegner til AI-billeder – priser for Nano Banana, GPT Image, FLUX, Grok | TokenSave",
)

NAV = dict(navToken="Tokentæller", navVideo="Videopris", navImage="Billedpris")

SITE = dict(fAbout="Om os", fPrivacy="Privatliv", viewIn="Se siden på dansk")

META = {
    "token": ("AI-tokentæller – GPT, Claude, Gemini", "Tæl tokens, tegn og API-pris for GPT, Claude og Gemini. Gratis og privat."),
    "video": ("AI-videopris – Veo, Kling, Runway", "Sammenlign API-priser for Veo 3.1, Kling, Runway, Luma m.fl. pr. sekund og klip."),
    "image": ("AI-billedpris – Nano Banana, GPT Image", "Sammenlign API-priser pr. billede: Nano Banana, GPT Image, FLUX, Grok m.fl."),
}
