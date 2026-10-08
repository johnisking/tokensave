![Claude limiet: hoeveel tokens geven Claude Pro en Claude Max?](/claude-limiet-nl.jpg)

Anthropic zegt niet hoeveel tokens Claude Pro of Max bevatten. De plannen worden beschreven als veelvouden van Pro ("5x Pro", "20x Pro"), met een limiet per 5 uur en een weeklimiet. Nooit als een aantal tokens. Mensen hebben het wel gemeten. Hieronder zie je hoe groot de Claude limiet in tokens is, waarom die getallen zo hoog zijn en hoe je ze omrekent naar iets bruikbaars: wat je gebruik via de API zou kosten.

**Kort:** volgens metingen uit september 2026 in Claude Code op Opus 5 geeft Claude Max 5x zo'n 39 miljoen tokens per 5-uursvenster en Max 20x zo'n 1,9 miljard tokens per week; de Claude Pro limiet ligt naar schatting rond 8 miljoen tokens per venster.

## Hoeveel tokens geeft Claude Pro en Claude Max?

![Hoeveel tokens geeft Claude Pro en Claude Max?: Plan, Prijs, Per 5-uursvenster, Per week](/claude-limiet-hoeveel-tokens-geeft-claude-pro-en-claud-nl.jpg)

Gemeten in Claude Code in september 2026, op Claude Opus 5:

| Plan | Prijs | Per 5-uursvenster | Per week |
|---|---|---|---|
| Pro | $20 | ~8 miljoen tokens *(schatting)* | ~95 miljoen *(schatting)* |
| Max 5x | $100 | **~39 miljoen tokens** (mediaan) | minstens 1,3 miljard |
| Max 20x | $200 | ~155 miljoen *(schatting)* | **~1,9 miljard tokens** |

De **vetgedrukte** waarden zijn gemeten door [FinOps LLM](https://finopsllm.com/research/claude-pro-max-tokens-limit). Zij logden de Claude Code-sessies van één zware gebruiker tot de limieten hem stopten: de 5-uurslimiet op Max 5x twaalf keer, de weeklimiet op Max 20x twee keer. De andere waarden zijn onze schattingen. We hebben ze uit die metingen geschaald met de verhoudingen die Anthropic zelf noemt (Max 5x = vijf keer Pro, Max 20x = twintig keer Pro). Zie ze als orde van grootte, niet als garantie.

In Nederland en België kost Claude Pro €18 per maand zonder btw, Max 5x €90 en Max 20x €180. Met 21% btw is dat €21,78, €108,90 en €217,80. Alle prijzen op een rij vind je in [AI-abonnementen: prijzen](/nl/blog/ai-abonnement-prijzen).

## Waarom zijn de getallen zo groot?

Omdat bijna alles goedkope cache-reads zijn, geen nieuwe tekst. Negenendertig miljoen tokens in vijf uur klinkt als een berg tekst. Dat is het niet. In de gemeten sessies was **96% van de tokens cache-reads**: Claude Code leest bij elke stap van een taak zijn eigen context opnieuw in (je bestanden, het gesprek tot nu toe, de resultaten van tools). Maar zo'n 0,6% van de tokens was output, tekst die Claude echt schreef.

Cache-reads zijn goedkoop op de API: 10% van de normale inputprijs op Claude Opus 5, het gemeten model, en 5% op Opus 5.5 en Sonnet 5.5. De limieten van Anthropic tellen dus duidelijk niet elk token even zwaar. Ze werken eerder als een **kostenbudget**. Het mediane Max 5x-venster kwam overeen met ongeveer **$37 aan API-gebruik**. Op dezelfde schaal is een Pro-venster zo'n $7 en een Max 20x-venster zo'n $150.

Daarom zegt een aantal tokens minder dan je zou denken. Twee sessies met evenveel tokens kunnen een heel ander deel van je limiet opmaken. Dat hangt af van hoeveel verse input en output erin zit en welk model je gebruikt.

## Wat verbruikt je Claude limiet het snelst?

![Wat verbruikt je Claude limiet het snelst?: Opus in plaats van Sonnet. Opus 5.5 kost op de API per token twee keer zoveel als Sonnet 5.5, en gaat ook snel](/claude-limiet-wat-verbruikt-je-claude-limiet-het-snels-nl.jpg)

- **Opus in plaats van Sonnet.** Opus 5.5 kost op de API per token twee keer zoveel als Sonnet 5.5, en gaat ook sneller door je planlimiet heen.
- **Lange sessies.** Elke stap stuurt de hele context opnieuw mee. Een sessie die is gegroeid tot 150.000 tokens kost per stap veel meer dan een verse. Gebruik **/clear** tussen taken die niets met elkaar te maken hebben en **/compact** bij lange taken.
- **Een grote CLAUDE.md of veel tools.** Die gaan bij elke stap mee.
- **Schrijven in een andere taal.** Koreaans gebruikt voor dezelfde inhoud zo'n 44% meer tokens dan Engels, Japans zo'n 79% meer. Nederlands zit op ongeveer 29% meer dan Engels ([meting](/nl/blog/tokens-nederlands-gpt)).

## Hoeveel berichten is dat?

Ook voor Claude Code publiceert Anthropic geen aantallen berichten. Schattingen uit de community komen voor Pro uit op ongeveer **90 prompts per 5-uursvenster op Sonnet**, nadat Anthropic in mei 2026 de 5-uurslimieten verdubbelde. Voor Max 20x gaat het om **200 tot 900 prompts** per venster, sterk afhankelijk van hoe groot elke taak is ([bron](https://fast.io/resources/claude-code-usage-limits-guide/)). De Claude-app en Claude Code delen dezelfde limiet. Meer daarover lees je in [Claude Code limiet](/nl/blog/claude-code-limiet).

## Heeft Claude een daglimiet?

Nee, een daglimiet is er niet. Je hebt een schuivend venster van 5 uur dat begint bij je eerste bericht, met een weeklimiet daarbovenop. Loop je tegen de weeklimiet aan? Dan helpt alleen zwaar werk gelijkmatiger over de week verdelen, of een duurder plan.

## Is een Claude-abonnement goedkoper dan de API?

Vrijwel zeker wel als je Claude Code intensief gebruikt. Een Max 20x-week, gemeten op zo'n 1,9 miljard tokens, kost tegen API-prijzen ongeveer $1.800 voor dezelfde mix van modellen en cache-reads. Het plan kost $200 per maand. Bij lichter gebruik kan het antwoord omslaan. Vul je eigen taakgrootte en aantal taken per dag in bij de [kostencalculator voor coding agents](/nl/agents), of gebruik de [calculator abonnement vs API](/nl/plans) voor chat.

Gerelateerd: [Claude Max vs Pro](/blog/claude-max-vs-pro) (in het Engels) · [Claude Code limiet](/nl/blog/claude-code-limiet) · [Codex limiet](/nl/blog/codex-limiet) · [Tokens besparen in Claude Code](/blog/claude-code-save-tokens) (in het Engels) · [Claude token counter](/claude-token-counter) (in het Engels) · [Nederlandse token counter](/nl/)

*Anthropic past limieten vaak aan en publiceert geen tokenquota. Typ **/status** in Claude Code om te zien hoeveel je nog over hebt.*

## Bronnen

- [Claude Code gebruiken met je Pro- of Max-abonnement (Claude Helpcentrum)](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [Claude-abonnementen en prijzen (Anthropic)](https://claude.com/pricing)
- [Prijzen van de Claude API (Anthropic-documentatie)](https://platform.claude.com/docs/en/about-claude/pricing)
- [Prompt caching (Claude-documentatie)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
<!-- autoimg -->
