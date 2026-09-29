# -*- coding: utf-8 -*-
SLUG = "cs"
TAG = "cs"
NATIVE = "Čeština"
OG = "cs_CZ"
DIR = "ltr"

S = dict(
    title="Počítadlo AI tokenů pro GPT, Claude a Gemini – TokenSave",
    desc="Bezplatné počítadlo AI tokenů pro GPT, Claude a Gemini. Okamžitě spočítá tokeny, znaky a odhadovanou cenu API přímo v prohlížeči, v jakémkoli jazyce. Nic se nenahrává.",
    badge="100% v prohlížeči · Nic se nenahrává",
    h1="Počítadlo AI tokenů",
    sub="Počítejte tokeny, znaky a cenu API v reálném čase — v jakémkoli jazyce.",
    prompt="Váš prompt",
    optimize="Optimalizovat",
    optimizeTip="Odstranit nadbytečné mezery a prázdné řádky",
    copy="Kopírovat",
    clear="Vymazat",
    ph1="Sem vložte nebo napište svůj prompt...",
    ph2="Tokeny, znaky a odhadovaná cena se aktualizují okamžitě při psaní. Funguje v jakémkoli jazyce.",
    tokens="Tokeny",
    chars="Znaky",
    words="Slova",
    cost="Odhadovaná cena",
    asIn="Jako vstup",
    asOut="Jako výstup",
    note="{name}: ${in} vstup / ${out} výstup za 1M tokenů",
    exact="Přesně (o200k)",
    based="Podle o200k",
    est="Odhad",
    eff="Jazyková efektivita",
    waste="{x}× plýtvání tokeny",
    efficient="Efektivita {p} %",
    great="Výborné",
    moderate="Mírné plýtvání",
    high="Vysoké plýtvání tokeny",
    share="Podíl neanglického textu: {p} %",
    tip="Tip: Nelatinková písma obvykle spotřebují víc tokenů pro stejný význam. Systémové prompty psané anglicky mohou snížit náklady.",
    q1="Co je token?",
    a1="Token je kousek textu, který AI model čte. V angličtině odpovídá 1 token zhruba 4 znakům nebo ¾ slova.",
    q2="Proč jsou jiné jazyky dražší?",
    a2="Tokenizéry se trénují hlavně na angličtině, takže čeština, korejština, japonština, čínština a mnoho dalších jazyků se pro stejný význam rozdělí na víc tokenů.",
    q3="Je můj text soukromý?",
    a3="Ano. Vše běží lokálně ve vašem prohlížeči. Váš text se nikdy neodesílá na žádný server.",
    f1="Modely OpenAI se počítají tokenizérem o200k. Počty pro Claude a Gemini jsou odhady.",
    f2="Ceny jsou ceníkové sazby za 1M tokenů, naposledy ověřeno v září 2026. Vždy si je ověřte na stránce s ceníkem poskytovatele.",
    tSaved="Optimalizováno — ušetřeno {n} tokenů",
    tAlready="Už je optimalizováno",
    tNothing="Není co kopírovat",
    tCopied="Zkopírováno do schránky",
    tCleared="Vymazáno",
    lang="Jazyk",
)

V = dict(
    title="Kalkulačka ceny AI videa – ceny Veo 3.1, Kling, Runway, Luma | TokenSave",
    desc="Porovnejte cenu API u AI video modelů: Veo 3.1, Kling 3.0, Runway Gen-4.5, Luma Ray, Grok Imagine, Seedance a dalších. Nastavte délku, rozlišení a zvuk a hned uvidíte cenu za klip.",
    badge="Oficiální ceny API · Aktualizováno v září 2026",
    h1="Kalkulačka ceny AI videa",
    sub="Zjistěte, kolik stojí stejné video u všech hlavních AI video modelů.",
    len="Délka klipu (sekundy)",
    clips="Počet klipů",
    res="Rozlišení",
    audio="Zvuk",
    audioOn="Se zvukem",
    audioOff="Bez zvuku",
    model="Model",
    perSec="Za sekundu",
    perClip="Za klip",
    total="Celkem",
    notes="Ceny jsou za sekundu vygenerovaného videa. Daně, množstevní slevy a neúspěšná generování nejsou zahrnuty.",
    na="V tomto rozlišení není k dispozici",
    noAudio="Bez nativního zvuku",
    cheapest="Nejlevnější",
    srcOfficial="Oficiální cena",
    srcRunway="Přes Runway API",
    audioIncl="Zvuk v ceně",
    clipNote="Účtováno po klipech 5/10 s",
    q1="Jak se účtuje AI video?",
    a1="Většina video API účtuje za sekundu vygenerovaného videa. Vyšší rozlišení a nativní zvuk stojí víc, takže klip v 1080p nebo 4K může stát několikanásobek klipu v 720p.",
    q2="Který AI video model je nejlevnější?",
    a2="Záleží na rozlišení. Lehké modely jako Veo 3.1 Lite, Grok Imagine a Wan začínají zhruba na $0.05 za sekundu, zatímco prémiové modely ve 4K mohou stát $0.40 za sekundu i víc.",
    q3="Je zahrnuta Sora?",
    a3="Ne. OpenAI 24. září 2026 odstranila video modely Sora 2 ze svého API, takže Sora už pro vývojáře není dostupná.",
    f1="Oficiální ceníkové ceny ze stránek s ceníky API jednotlivých poskytovatelů, ověřeno 30. září 2026. Modely bez veřejné ceny API za sekundu jsou uvedeny podle sazeb Runway API.",
    f2="Ceny se často mění — před velkými zakázkami si je ověřte na stránce poskytovatele.",
)

I = dict(
    title="Kalkulačka ceny AI obrázků – ceny Nano Banana, GPT Image, FLUX, Grok | TokenSave",
    desc="Porovnejte cenu API za obrázek u Nano Banana 2, Nano Banana Pro, GPT Image 2.5, FLUX.2, Grok Imagine, Seedream a Runway. Zvolte rozlišení a počet a hned uvidíte celkovou cenu.",
    h1="Kalkulačka ceny AI obrázků",
    sub="Zjistěte, kolik stojí stejné obrázky u všech hlavních AI modelů pro obrázky.",
    count="Počet obrázků",
    perImg="Za obrázek",
    notes="Ceny jsou za vygenerovaný obrázek. Poplatky za referenční obrázky, daně a množstevní slevy nejsou zahrnuty.",
    q1="Jak se účtuje generování AI obrázků?",
    a1="Většina API pro obrázky účtuje pevnou cenu za obrázek, která roste s rozlišením. Modely OpenAI si navíc účtují víc za vyšší kvalitu a FLUX účtuje podle megapixelů.",
    q2="Který AI model pro obrázky je nejlevnější?",
    a2="Malé modely jako FLUX.2 [klein], Grok Imagine a GPT Image v nízké kvalitě stojí kolem $0.01–0.02 za obrázek. Prémiové modely ve 4K mohou stát $0.15–0.40 za obrázek.",
    q3="Co je Nano Banana?",
    a3="Nano Banana je přezdívka obrázkových modelů Google Gemini. Nano Banana 2 je Gemini 3.1 Flash Image a Nano Banana Pro je Gemini 3 Pro Image.",
    f1="Oficiální ceníkové ceny ze stránek s ceníky API jednotlivých poskytovatelů, ověřeno 30. září 2026. OpenAI a Nano Banana Pro jsou uvedeny podle sazeb Runway API.",
)

NAV = dict(
    navToken="Počítadlo tokenů",
    navVideo="Cena videa",
    navImage="Cena obrázků",
)

SITE = dict(
    fAbout="O nás",
    fPrivacy="Soukromí",
    viewIn="Zobrazit tuto stránku v češtině",
)

META = {
    "token": ("Počítadlo AI tokenů – GPT, Claude", "Spočítejte tokeny a cenu API pro GPT, Claude a Gemini. Zdarma a soukromě."),
    "video": ("Cena AI videa – Veo, Kling, Runway", "Porovnejte ceny API Veo 3.1, Kling, Runway, Luma a dalších za sekundu i klip."),
    "image": ("Cena AI obrázků – Nano Banana, GPT", "Porovnejte cenu za obrázek u Nano Banana, GPT Image, FLUX, Grok a dalších."),
}
