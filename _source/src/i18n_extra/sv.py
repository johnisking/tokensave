# -*- coding: utf-8 -*-
SLUG = "sv"
TAG = "sv"
NATIVE = "Svenska"
OG = "sv_SE"
DIR = "ltr"

S = dict(
    a1="En token är en bit text som en AI-modell läser. På engelska motsvarar 1 token ungefär 4 tecken eller ¾ av ett ord.",
    a2="Tokenizers tränas mest på engelska, så svenska, koreanska, japanska, kinesiska och många andra språk delas upp i fler tokens för samma innehåll.",
    a3="Ja. Allt körs lokalt i din webbläsare. Din text skickas aldrig till någon server.",
    asIn="Som indata",
    asOut="Som utdata",
    badge="100 % i webbläsaren · Inget laddas upp",
    based="o200k-baserad",
    chars="Tecken",
    clear="Rensa",
    copy="Kopiera",
    cost="Uppskattad kostnad",
    desc="Gratis AI-tokenräknare för GPT, Claude och Gemini. Räkna tokens, tecken och uppskattad API-kostnad direkt i webbläsaren, på alla språk. Inget laddas upp.",
    eff="Språkeffektivitet",
    efficient="{p} % effektiv",
    est="Uppskattat",
    exact="Exakt (o200k)",
    f1="OpenAI-modeller räknas med o200k-tokenizern. Siffrorna för Claude och Gemini är uppskattningar.",
    f2="Priserna är listpriser per 1M tokens, senast kontrollerade i september 2026. Kontrollera alltid leverantörens prissida.",
    great="Utmärkt",
    h1="AI-tokenräknare",
    high="Högt tokenslöseri",
    lang="Språk",
  extRef="Officiella pris- och tokenizer-referenser:",
    moderate="Måttligt slöseri",
    note="{name}: ${in} indata / ${out} utdata per 1M tokens",
    optimize="Optimera",
    optimizeTip="Ta bort extra mellanslag och tomma rader",
    ph1="Klistra in eller skriv din prompt här...",
    ph2="Tokens, tecken och uppskattad kostnad uppdateras direkt medan du skriver. Fungerar på alla språk.",
    prompt="Din prompt",
    q1="Vad är en token?",
    q2="Varför kostar andra språk mer?",
    q3="Är min text privat?",
    share="Icke-engelsk andel: {p} %",
    sub="Räkna tokens, tecken och API-kostnad i realtid – på alla språk.",
    tAlready="Redan optimerad",
    tCleared="Rensat",
    tCopied="Kopierat till urklipp",
    tNothing="Inget att kopiera",
    tSaved="Optimerat – sparade {n} tokens",
    tip="Tips: Icke-latinska skriftsystem kostar oftast fler tokens för samma innehåll. Att skriva systemprompter på engelska kan sänka kostnaden.",
    title="AI-tokenräknare för GPT, Claude och Gemini – TokenSave",
    tokens="Tokens",
    waste="{x}x tokenslöseri",
    words="Ord",
)

V = dict(
    a1="De flesta video-API:er tar betalt per sekund genererad video. Högre upplösning och inbyggt ljud kostar mer, så ett klipp i 1080p eller 4K kan kosta flera gånger så mycket som ett i 720p.",
    a2="Det beror på upplösningen. Lätta modeller som Veo 3.1 Lite, Grok Imagine och Wan börjar kring $0.05 per sekund, medan premiummodeller i 4K kan kosta $0.40 per sekund eller mer.",
    a3="Nej. OpenAI tog bort Sora 2-videomodellerna från sitt API den 24 september 2026, så Sora är inte längre tillgänglig för utvecklare.",
    audio="Ljud",
    audioIncl="Ljud ingår",
    audioOff="Utan ljud",
    audioOn="Med ljud",
    badge="Officiella API-priser · Uppdaterat september 2026",
    cheapest="Billigast",
    clipNote="Debiteras per klipp om 5/10 s",
    clips="Antal klipp",
    desc="Jämför API-kostnaden för AI-videomodeller: Veo 3.1, Kling 3.0, Runway Gen-4.5, Luma Ray, Grok Imagine, Seedance med flera. Välj längd, upplösning och ljud och se priset per klipp direkt.",
    f1="Officiella listpriser från varje leverantörs API-prissida, kontrollerade den 30 september 2026. Modeller utan offentligt API-pris per sekund visas med Runways API-priser.",
    f2="Priserna ändras ofta – kontrollera på leverantörens sida före stora jobb.",
    h1="Kostnadskalkylator för AI-video",
    len="Längd per klipp (sekunder)",
    model="Modell",
    na="Erbjuds inte i denna upplösning",
    noAudio="Inget inbyggt ljud",
    notes="Priserna gäller per sekund genererad video. Skatter, volymrabatter och misslyckade genereringar ingår inte.",
    perClip="Per klipp",
    perSec="Per sekund",
    q1="Hur prissätts AI-video?",
    q2="Vilken är den billigaste AI-videomodellen?",
    q3="Ingår Sora?",
    res="Upplösning",
    srcOfficial="Officiellt pris",
    srcRunway="Via Runway API",
    sub="Se vad samma video kostar i alla stora AI-videomodeller.",
    title="Kostnadskalkylator för AI-video – priser för Veo 3.1, Kling, Runway, Luma | TokenSave",
    total="Totalt",
)

I = dict(
    a1="De flesta bild-API:er tar ett fast pris per bild som ökar med upplösningen. OpenAI-modeller kostar också mer vid högre kvalitetsinställningar, och FLUX debiterar per megapixel.",
    a2="Små modeller som FLUX.2 [klein], Grok Imagine och GPT Image i låg kvalitet kostar runt $0.01–0.02 per bild. Premiummodeller i 4K kan kosta $0.15–0.40 per bild.",
    a3="Nano Banana är smeknamnet på Googles Gemini-bildmodeller. Nano Banana 2 är Gemini 3.1 Flash Image och Nano Banana Pro är Gemini 3 Pro Image.",
    count="Antal bilder",
    desc="Jämför API-kostnaden per bild för Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream och Runway. Välj upplösning och antal och se totalen direkt.",
    f1="Officiella listpriser från varje leverantörs API-prissida, kontrollerade den 30 september 2026. OpenAI och Nano Banana Pro visas med Runways API-priser.",
    h1="Kostnadskalkylator för AI-bilder",
    notes="Priserna gäller per genererad bild. Avgifter för referensbilder, skatter och volymrabatter ingår inte.",
    perImg="Per bild",
    q1="Hur prissätts AI-bildgenerering?",
    q2="Vilken är den billigaste AI-bildmodellen?",
    q3="Vad är Nano Banana?",
    sub="Se vad samma bilder kostar i alla stora AI-bildmodeller.",
    title="Kostnadskalkylator för AI-bilder – priser för Nano Banana, GPT Image, FLUX, Grok | TokenSave",
)

NAV = dict(
    navToken="Tokenräknare",
    navVideo="Videokostnad",
    navImage="Bildkostnad",
)

SITE = dict(
    fAbout="Om oss",
    fPrivacy="Integritet",
    viewIn="Visa sidan på svenska",
)

META = {
    "token": ("AI-tokenräknare – GPT, Claude, Gemini", "Räkna tokens, tecken och API-kostnad för GPT, Claude och Gemini. Gratis, privat."),
    "video": ("AI-videokostnad – Veo, Kling, Runway", "Jämför API-priser för Veo 3.1, Kling, Runway, Luma m.fl. per sekund och klipp."),
    "image": ("AI-bildkostnad – Nano Banana, GPT Image", "Jämför API-priser per bild för Nano Banana, GPT Image, FLUX, Grok med flera."),
}
