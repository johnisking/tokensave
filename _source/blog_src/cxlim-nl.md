Codex, de coding agent van OpenAI, zit in de ChatGPT-plannen Plus, Pro en Business. Het is ook de plek waar de meeste mensen nu tegen limieten aanlopen. Codex deelt zijn tegoed met ChatGPT Work, gebruikt een venster van 5 uur en een weeklimiet, en gaat daar per model heel verschillend doorheen. Hieronder lees je hoe de Codex limiet werkt, hoeveel de Codex limiet in Plus je geeft en hoe je er meer uit haalt.

**Kort:** Codex heeft twee limieten tegelijk, een schuivend venster van 5 uur en een weeklimiet, gedeeld met ChatGPT Work; in Plus krijg je naar schatting zo'n 5–45 berichten per 5 uur op GPT-6 Astra tot zo'n 250–2.000 op GPT-5.6 Luna, afhankelijk van het model.

## Welke plannen bevatten Codex?

Gebruik van Codex (en ChatGPT Work) zit in **Plus** ($20), **Pro** ($100, $200 of $500) en de seats **Business** Standard en Premium. Onbeperkt is het niet: elk plan krijgt een tegoed, gemeten over twee vensters. In Nederland kost Plus €23 per maand inclusief btw. Meer over de Pro-niveaus lees je in [ChatGPT Pro voor 100, 200 en 500 dollar](/nl/blog/chatgpt-pro-100-200-500), en alle prijzen staan in [AI-abonnementen: prijzen](/nl/blog/ai-abonnement-prijzen).

## Welke limieten heeft Codex?

Twee tegelijk: een venster van 5 uur en een weeklimiet.

**Het 5-uursvenster.** Een schuivend tegoed dat begint bij je eerste verzoek. Is het op, dan wacht je tot het venster wordt gereset. OpenAI bracht het 5-uursvenster eind augustus 2026 terug voor Plus. Toen zei het ook dat Pro 100 en Pro 200 het de komende maanden niet zouden krijgen.

**De weeklimiet.** Daarbovenop geldt een schuivend maximum over zeven dagen. Raak je dat, dan wacht je op de wekelijkse reset, ook als je 5-uursvenster nog vers is.

Codex en ChatGPT Work putten uit **hetzelfde tegoed**.

## Hoeveel geeft de Codex limiet in Plus en Pro?

Het helpcentrum van OpenAI noemt een geschat aantal berichten per 5-uursvenster. Het model dat je kiest, maakt een enorm verschil:

| Model | Plus | Pro (vijfvoudig niveau) |
|---|---|---|
| GPT-6 Astra | zo'n 5–45 | zo'n 25–225 |
| GPT-5.6 Sol | zo'n 10–100 | zo'n 50–500 |
| GPT-5.6 Terra | zo'n 25–200 | zo'n 125–1.000 |
| GPT-5.6 Luna | zo'n 250–2.000 | zo'n 1.250–10.000 |

De onderkant van elke bandbreedte zijn lange taken met veel stappen op een grote codebase. De bovenkant zijn korte, simpele verzoeken. Hogere Pro-niveaus schalen mee: Pro 200 geeft nieuwe abonnees sinds 29 september 2026 tien keer zoveel als Plus, Pro 500 vijfentwintig keer zoveel.

**Ultrafast**, alleen beschikbaar op Pro 500, is een snellere modus die je inbegrepen gebruik en tegoeden sneller opmaakt.

## Waarom gaat Codex zo snel door je limiet?

Zoals elke coding agent werkt Codex in stappen. Bij elke stap stuurt hij zijn hele werkcontext terug naar het model: instructies, tooldefinities, gelezen bestanden en eerdere stappen. Een gemiddelde featuretaak van 25 stappen stuurt zo'n 1,6 miljoen inputtokens. Via de API kost die taak ongeveer $0,72 op een model van de Sol-klasse en zo'n $3,60 op GPT-6 Astra. Daarom is het tegoed voor Astra zoveel kleiner. Zie [What does an AI coding agent cost per task?](/blog/ai-coding-agent-cost) (in het Engels) of reken het zelf uit met de [kostencalculator voor coding agents](/nl/agents).

## Hoe controleer je je gebruik?

Het helpcentrum van OpenAI verwijst naar **Instellingen → Gebruik** (Settings → Usage) in ChatGPT. Daar zie je je resterende tegoed en de resettijden. Codex waarschuwt je ook als je de limiet nadert.

## Wat doe je als je de limiet raakt?

1. **Wacht op de reset.** Het 5-uursvenster vult zich binnen een paar uur weer aan.
2. **Gebruik een bewaarde reset of koop een directe reset.** Dat kan op Plus- en Pro-accounts die daarvoor in aanmerking komen.
3. **Gebruik tegoeden** om door te werken op plannen die dat ondersteunen.
4. **Stap over** naar een hoger Pro-niveau.
5. **Gebruik een API-key** met pay-as-you-go-facturering voor werk boven je limiet.

## Hoe rek je je Codex limiet op?

- **Kies standaard GPT-5.6 Sol of Terra.** Gebruik GPT-6 Astra alleen voor lastige problemen waar je het verschil merkt: het kost een veelvoud van het tegoed.
- **Gebruik Luna voor simpele wijzigingen**, hernoemen en standaardcode.
- **Houd taken klein en concreet.** Minder stappen betekent minder context die opnieuw wordt verstuurd.
- **Begin opnieuw tussen taken die niets met elkaar te maken hebben**, zodat oude geschiedenis niet mee blijft gaan.
- **Wijs Codex de juiste bestanden aan** in plaats van hem de hele repo te laten doorzoeken.
- **Houd je instructiebestand kort**, en schrijf het in het Engels als je normaal een andere taal gebruikt. Op de tokenizer van GPT kost Koreaans zo'n 44% meer tokens dan Engels en Japans zo'n 79% meer. Nederlands kost ongeveer 29% meer ([meting](/nl/blog/tokens-nederlands-gpt)). Je eigen tekst check je in de [token counter](/nl/).

Veel van dezelfde gewoontes werken ook in Claude Code: zie [How to save tokens in Claude Code](/blog/claude-code-save-tokens) (in het Engels) en [Claude Code limiet](/nl/blog/claude-code-limiet).

## Codex of Claude Code?

Beide zitten in plannen van $20, $100 en $200, met vergelijkbare limietsystemen. De vergelijking [ChatGPT Pro vs Claude Max](/blog/chatgpt-pro-vs-claude-max) (in het Engels) bespreekt de verschillen. De [kostencalculator voor coding agents](/nl/agents) zet de maandelijkse API-kosten naast elk plan, en met de [plannencalculator](/nl/plans) vergelijk je de abonnementen zelf. Hoe ver je komt met Claude lees je in [Claude limiet](/nl/blog/claude-limiet).

*Limieten veranderen vaak. De [helppagina van OpenAI over gebruik van Codex en Work](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex) heeft de actuele cijfers.*
