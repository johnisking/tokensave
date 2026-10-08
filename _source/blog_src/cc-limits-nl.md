![Claude Code limiet: de 5 uur limiet en de weeklimiet uitgelegd](/claude-code-limiet-nl.jpg)

"Claude usage limit reached" is een van de meest voorkomende meldingen in Claude Code. Ook een van de meest verwarrende. De Claude Code limiet bestaat namelijk uit twee limieten die tegelijk gelden: een 5 uur limiet en een weeklimiet. Hieronder lees je hoe ze werken, wat er in 2026 veranderde en wat je doet als je er een raakt.

**Kort:** Claude Code heeft twee limieten tegelijk, een 5 uur limiet vanaf je eerste bericht en een weeklimiet, en die deel je met de Claude-app; zit je aan een van beide, dan wacht je op de reset, zet je extra gebruik aan of stap je over op de API.

## Welke limieten heeft Claude Code?

Twee: een sessielimiet van 5 uur en een weeklimiet. Ze lopen naast elkaar, en elk van de twee kan je tegenhouden.

**1. De Claude Code 5 uur limiet.** Je gebruik wordt gemeten over een schuivend venster van vijf uur dat begint bij je eerste bericht. Is je tegoed voor dat venster op, dan wacht je tot het wordt gereset.

**2. De weeklimiet.** Bovenop de sessielimiet geldt een maximum voor je totale gebruik per week. Die kwam er in augustus 2025, om te voorkomen dat een klein deel van de accounts Claude Code dag en nacht liet draaien. Raak je hem, dan wacht je op de wekelijkse reset, ook als je 5-uursvenster nog vers is.

Beide limieten worden **gedeeld tussen Claude Code en de Claude-app** (web, desktop en mobiel). Een lang gesprek in de app gaat van hetzelfde tegoed af als je codeersessie.

## Hoeveel gebruik krijg je per plan?

![Hoeveel gebruik krijg je per plan?: Plan, Prijs, Gebruik](/claude-code-limiet-hoeveel-gebruik-krijg-je-per-plan-nl.jpg)

Anthropic beschrijft de limieten van de plannen ten opzichte van elkaar, niet in exacte aantallen tokens:

| Plan | Prijs | Gebruik |
|---|---|---|
| Pro | $20/maand | Basisniveau |
| Max 5x | $100/maand | Vijf keer Pro |
| Max 20x | $200/maand | Twintig keer Pro |

Hoe ver je daarmee komt, hangt sterk af van wat je doet. Grote bestanden, lange sessies en Opus gaan veel sneller door je tegoed dan korte taken op Sonnet. Elke stap stuurt namelijk de hele werkcontext opnieuw mee. In Nederland en België kosten de plannen €21,78, €108,90 en €217,80 per maand inclusief 21% btw. Meer prijzen in [AI-abonnementen: prijzen](/nl/blog/ai-abonnement-prijzen), en hoeveel tokens de plannen ongeveer geven lees je in [Claude limiet](/nl/blog/claude-limiet).

## Wat veranderde er in 2026?

![Wat veranderde er in 2026?: 6 mei 2026; Zomer 2026; 14 september 2026](/claude-code-limiet-wat-veranderde-er-in-2026-nl.jpg)

- **6 mei 2026:** Anthropic **verdubbelde de 5-uurslimieten van Claude Code** voor Pro, Max, Team en Enterprise met seats, en schrapte voor Pro en Max de extra verlaging van de limieten tijdens piekuren.
- **Zomer 2026:** er gold tijdelijk een **verhoging van 50%** op de weeklimieten.
- **14 september 2026:** Anthropic **verhoogde de standaard weeklimieten blijvend met 25%** voor Pro, Max, Team en Enterprise met seats. Dat verving de tijdelijke verhoging van 50%. Daardoor liggen de weeklimieten zo'n 17% lager dan in de zomer, maar nog steeds 25% boven het oorspronkelijke niveau.

Heb je het gevoel dat je sinds half september sneller tegen de weeklimiet aanloopt? Dat klopt.

## Hoe zie je hoeveel limiet je nog hebt?

In Claude Code toont het commando **/status** hoeveel tegoed je nog hebt. Claude Code waarschuwt je ook als je een limiet nadert. Kijk dit na voordat je aan een lange taak begint, niet halverwege.

## Wat doe je als je een limiet raakt?

![Wat doe je als je een limiet raakt?: Wacht op de reset. Bij de 5 uur limiet is dat meestal een kwestie van uren.; Zet extra gebruik aan (extra usag](/claude-code-limiet-wat-doe-je-als-je-een-limiet-raakt-nl.jpg)

1. **Wacht op de reset.** Bij de 5 uur limiet is dat meestal een kwestie van uren.
2. **Zet extra gebruik aan (extra usage).** Betaalde plannen kunnen doorwerken met los gefactureerde tegoeden in plaats van te stoppen.
3. **Stap over op API-tegoed.** Claude Code kan draaien op pay-as-you-go-facturering via de API. Het vraagt eerst je toestemming.
4. **Kies een hoger plan.** Van Pro naar Max 5x, of van Max 5x naar Max 20x.
5. **Gebruik minder tokens per taak.** Vaak de goedkoopste oplossing. Zie hieronder.

## Waarom raak je je limiet sneller dan verwacht?

Meestal door lange sessies en een grote context die bij elke stap terug naar het model gaat.

- **Lange sessies.** Elke stap stuurt alles wat eerder gebeurde opnieuw mee. Een sessie van twee uur sleept een enorme context mee in elke nieuwe stap.
- **Opus.** Gaat sneller door je tegoed dan Sonnet.
- **Grote bestanden en logs.** Een bestand van 3.000 regels of een volledig testlog inlezen kost tienduizenden tokens.
- **Vage taken.** "Ruim het project op" kan tientallen stappen kosten; "fix de falende test in auth.py" maar een paar.
- **Tegelijk de Claude-app gebruiken.** Beide putten uit dezelfde pot.

## Hoe rek je je Claude Code limiet op?

- Begin een nieuwe sessie (**/clear**) tussen taken die niets met elkaar te maken hebben, en vat een lange sessie samen met **/compact**.
- Wijs Claude de juiste bestanden aan in plaats van hem te laten zoeken.
- Houd je instructies in CLAUDE.md kort: ze gaan bij elke stap mee.
- Gebruik Sonnet voor routinewerk en bewaar Opus voor lastige problemen.

Meer details en cijfers vind je in [How to save tokens in Claude Code](/blog/claude-code-save-tokens) (in het Engels). Hoeveel tokens je tekst of code kost, zie je in de [token counter](/nl/). Let op: Nederlands kost zo'n 29% meer tokens dan Engels ([meting](/nl/blog/tokens-nederlands-gpt)).

## Abonnement of API?

Loop je regelmatig tegen de weeklimiet aan? Vergelijk dan wat dat extra gebruik via de API zou kosten met de prijs van het volgende plan. Onze gids [Claude Code cost per month](/blog/claude-code-cost-per-month) (in het Engels) en de [kostencalculator voor coding agents](/nl/agents) rekenen het voor je uit. Plannen van verschillende aanbieders vergelijk je met de [plannencalculator](/nl/plans). De limieten van de concurrent van OpenAI staan in [Codex limiet](/nl/blog/codex-limiet).

*Limieten veranderen. De [helppagina van Anthropic over Claude Code met Pro of Max](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan) en de [prijspagina](https://claude.com/pricing) geven de actuele regels.*
<!-- autoimg -->
