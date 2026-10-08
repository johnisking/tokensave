![Codex limiet: hoeveel geeft Codex in ChatGPT Plus en Pro?](/codex-limiet-nl.jpg)

Codex, de coding agent van OpenAI, zit in de ChatGPT-plannen Plus, Pro en Business. Het is ook de plek waar de meeste mensen nu tegen limieten aanlopen. Codex deelt zijn tegoed met ChatGPT Work, gebruikt in Plus en Business een venster van 5 uur (er kunnen ook weeklimieten gelden), en gaat daar per model heel verschillend doorheen. Hieronder lees je hoe de Codex limiet werkt, hoeveel de Codex limiet in Plus je geeft en hoe je er meer uit haalt.

**Kort:** Codex heeft in Plus en Business een schuivend venster van 5 uur, gedeeld met ChatGPT Work, en er kunnen ook weeklimieten gelden; Pro heeft nu geen 5-uurslimiet. In Plus krijg je naar schatting zo'n 5–45 berichten per 5 uur op GPT-6 Astra tot zo'n 350–3.000 op GPT-6 Luna, afhankelijk van het model.

## Welke plannen bevatten Codex?

Gebruik van Codex (en ChatGPT Work) zit in **Plus** ($20), **Pro** ($100, $200 of $500) en de seats **Business** Standard en Premium. Onbeperkt is het niet: elk plan krijgt een inbegrepen tegoed. In Nederland kost Plus €23 per maand inclusief btw. Meer over de Pro-niveaus lees je in [ChatGPT Pro voor 100, 200 en 500 dollar](/nl/blog/chatgpt-pro-100-200-500), en alle prijzen staan in [AI-abonnementen: prijzen](/nl/blog/ai-abonnement-prijzen).

## Welke limieten heeft Codex?

In Plus en Business een venster van 5 uur, en daarbovenop kunnen weeklimieten gelden.

**Het 5-uursvenster.** Een schuivend tegoed dat begint bij je eerste verzoek. Is het op, dan wacht je tot het venster wordt gereset. Pro 100, Pro 200 en Pro 500 hebben in Work en Codex op dit moment geen 5-uurslimiet; ze hebben wel een inbegrepen tegoed.

**De weeklimiet.** Volgens OpenAI kunnen daarbovenop ook weeklimieten gelden. Raak je die, dan wacht je op de reset, ook als je 5-uursvenster nog vers is.

Codex en ChatGPT Work putten uit **hetzelfde tegoed**.

## Hoeveel geeft de Codex limiet in Plus en Pro?

![Hoeveel geeft de Codex limiet in Plus en Pro?: Model, Plus, Business (Standard)](/codex-limiet-hoeveel-geeft-de-codex-limiet-in-plus-en-nl.jpg)

Het helpcentrum van OpenAI noemt een geschat aantal lokale berichten per 5-uursvenster voor Plus en Standard Business. Het model dat je kiest, maakt een enorm verschil:

| Model | Plus | Business (Standard) |
|---|---|---|
| GPT-6 Astra | zo'n 5–45 | zo'n 5–45 |
| GPT-6.1 Sol | zo'n 15–160 | zo'n 15–160 |
| GPT-6 Sol | zo'n 15–150 | zo'n 15–150 |
| GPT-6 Luna | zo'n 350–3.000 | zo'n 350–3.000 |

De onderkant van elke bandbreedte zijn lange taken met veel stappen op een grote codebase. De bovenkant zijn korte, simpele verzoeken. Pro heeft nu geen 5-uurslimiet, maar wel een groter inbegrepen tegoed: Pro 100 geeft vijf keer zoveel als Plus, Pro 200 geeft nieuwe abonnees tien keer zoveel als Plus, Pro 500 vijfentwintig keer zoveel (had je tussen 22 en 29 september 2026 een actief Pro 200-abonnement, dan houd je de oude limiet tot 29 oktober). Deze verhoudingen staan niet op de prijspagina van OpenAI; ze komen uit een bericht op X van Thibault Sottiaux (OpenAI) en uit persberichten (WinBuzzer, Windows Report).

**Ultrafast**, alleen beschikbaar op Pro 500, is een snellere modus die je inbegrepen gebruik en tegoeden sneller opmaakt.

## Waarom gaat Codex zo snel door je limiet?

Zoals elke coding agent werkt Codex in stappen. Bij elke stap stuurt hij zijn hele werkcontext terug naar het model: instructies, tooldefinities, gelezen bestanden en eerdere stappen. Een gemiddelde featuretaak van 25 stappen stuurt zo'n 1,6 miljoen inputtokens. Via de API kost die taak ongeveer $0,72 op een model van de Sol-klasse en zo'n $3,60 op GPT-6 Astra. Daarom is het tegoed voor Astra zoveel kleiner. Zie [What does an AI coding agent cost per task?](/blog/ai-coding-agent-cost) (in het Engels) of reken het zelf uit met de [kostencalculator voor coding agents](/nl/agents).

## Hoe controleer je je gebruik?

Het helpcentrum van OpenAI verwijst naar **Instellingen → Gebruik** (Settings → Usage) in ChatGPT. Daar zie je je resterende tegoed en de resettijden. Codex waarschuwt je ook als je de limiet nadert.

## Wat doe je als je de limiet raakt?

![Wat doe je als je de limiet raakt?: Wacht op de reset. Het 5-uursvenster vult zich binnen een paar uur weer aan.; Gebruik een bewaarde reset of ko](/codex-limiet-wat-doe-je-als-je-de-limiet-raakt-nl.jpg)

1. **Wacht op de reset.** Het 5-uursvenster vult zich binnen een paar uur weer aan.
2. **Gebruik een bewaarde reset of koop een directe reset.** Dat kan op Plus- en Pro-accounts die daarvoor in aanmerking komen.
3. **Gebruik tegoeden** om door te werken op plannen die dat ondersteunen.
4. **Stap over** naar een hoger Pro-niveau.
5. **Gebruik een API-key** met pay-as-you-go-facturering voor werk boven je limiet.

## Hoe rek je je Codex limiet op?

![Hoe rek je je Codex limiet op?: Kies standaard GPT-6.1 Sol of GPT-6 Sol. Gebruik GPT-6 Astra alleen voor lastige problemen waar je het verschil me](/codex-limiet-hoe-rek-je-je-codex-limiet-op-nl.jpg)

- **Kies standaard GPT-6.1 Sol of GPT-6 Sol.** Gebruik GPT-6 Astra alleen voor lastige problemen waar je het verschil merkt: het kost een veelvoud van het tegoed.
- **Gebruik Luna voor simpele wijzigingen**, hernoemen en standaardcode.
- **Houd taken klein en concreet.** Minder stappen betekent minder context die opnieuw wordt verstuurd.
- **Begin opnieuw tussen taken die niets met elkaar te maken hebben**, zodat oude geschiedenis niet mee blijft gaan.
- **Wijs Codex de juiste bestanden aan** in plaats van hem de hele repo te laten doorzoeken.
- **Houd je instructiebestand kort**, en schrijf het in het Engels als je normaal een andere taal gebruikt. Op de tokenizer van GPT kost Koreaans zo'n 44% meer tokens dan Engels en Japans zo'n 79% meer. Nederlands kost ongeveer 29% meer ([meting](/nl/blog/tokens-nederlands-gpt)). Je eigen tekst check je in de [token counter](/nl/).

Veel van dezelfde gewoontes werken ook in Claude Code: zie [How to save tokens in Claude Code](/blog/claude-code-save-tokens) (in het Engels) en [Claude Code limiet](/nl/blog/claude-code-limiet).

## Codex of Claude Code?

Beide zitten in plannen van $20, $100 en $200, met vergelijkbare limietsystemen. De vergelijking [ChatGPT Pro vs Claude Max](/blog/chatgpt-pro-vs-claude-max) (in het Engels) bespreekt de verschillen. De [kostencalculator voor coding agents](/nl/agents) zet de maandelijkse API-kosten naast elk plan, en met de [plannencalculator](/nl/plans) vergelijk je de abonnementen zelf. Hoe ver je komt met Claude lees je in [Claude limiet](/nl/blog/claude-limiet).

*Limieten veranderen vaak. De [helppagina van OpenAI over gebruik van Codex en Work](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex) heeft de actuele cijfers.*

## Bronnen

- [OpenAI Help: gebruik in Work en Codex](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)
- [OpenAI Help: opgespaarde Codex-resets](https://help.openai.com/en/articles/20001498-how-banked-codex-resets-work)
- [ChatGPT-abonnementen en Codex-prijzen](https://learn.chatgpt.com/docs/pricing)
- [OpenAI Help: ChatGPT Pro-niveaus](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
<!-- autoimg -->
