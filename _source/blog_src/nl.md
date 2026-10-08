![Nederlands in GPT: 29% meer tokens dan Engels (41 talen gemeten)](/tokens-nederlands-gpt-nl.jpg)

Ik vertaalde dezelfde klantenservice-prompt naar 41 talen en telde de tokens met o200k_base, de huidige tokenizer van OpenAI (GPT-4o en nieuwer). Engels heeft 34 tokens nodig, Nederlands **44 — 29% meer**, plaats 10 van 41 (1 = goedkoopst).

De Nederlandse versie:

> Vat de onderstaande e-mail van de klant samen in drie punten en stel een beleefd antwoord voor. De klant zegt dat de bestelling twee dagen te laat aankwam en dat er één artikel in de doos ontbrak.

## Resultaten

| Taal | Tokens | Meer dan in het Engels | Besparing bij versturen in het Engels |
|---|---:|---:|---:|
| English | 34 | – | – |
| 简体中文 | 35 | +3% | 3% |
| Español | 40 | +18% | 15% |
| Deutsch | 43 | +26% | 21% |
| **Nederlands** | **44** | **+29%** | **22%** |
| 한국어 | 49 | +44% | 31% |
| हिन्दी | 51 | +50% | 33% |
| 日本語 | 61 | +79% | 44% |
| Čeština | 68 | +100% | 50% |
| Ελληνικά | 70 | +106% | 51% |
| ਪੰਜਾਬੀ | 83 | +144% | 59% |

![Diagram: extra tokens per taal vergeleken met Engels in GPT (41 talen)](/blog-language-tax-chart-v5.png)

## Waarom

![Waarom: ontbrak → ont | br | ak · 3; beleefd → bele | efd · 2; aankwam → aank | wam · 2](/tokens-nederlands-gpt-waarom-nl.jpg)

De tokenizer leert vooral van Engelse tekst: woorden als " polite" of " customer" zijn één token, terwijl veel Nederlandse woorden in stukken worden gehakt:

- ontbrak → `ont | br | ak` · 3
- beleefd → `bele | efd` · 2
- aankwam → `aank | wam` · 2

## Met één knop naar het Engels

De grootste besparing haal je door je prompt in het Engels te sturen: ongeveer 22% minder tokens dan in het Nederlands. Huidige modellen begrijpen Engelse instructies uitstekend en antwoorden in het Nederlands als je daarom vraagt. Plak je prompt in de [TokenSave-tokenteller](/nl/) en druk op **💸 Tokens besparen**: spaties worden opgeschoond, de tekst wordt naar het Engels vertaald, overbodige tekst wordt weggehaald en "Reply in Dutch." wordt toegevoegd, zodat het antwoord in jouw taal blijft. Er wordt gebruikgemaakt van de ingebouwde vertaler van Chrome 138+ / Edge 148+ op desktop; de vertaling gebeurt op je eigen apparaat en je tekst wordt nooit geüpload. Druk op **↩ Origineel** om het origineel terug te krijgen.

## In geld

Bij een model van $2 per miljoen inputtokens kost het 68 dollar in het Engels en 88 dollar in het Nederlands om deze prompt een miljoen keer te versturen. Antwoordt het model ook in het Nederlands, dan geldt dezelfde 29% extra voor de outputtokens, die meestal 300–400% duurder zijn dan inputtokens.

## Zo bespaar je

![Zo bespaar je: Schrijf de systeemprompt en vaste instructies in het Engels; houd alleen de invoer van gebruikers in het Neder](/tokens-nederlands-gpt-zo-bespaar-je-nl.jpg)

- Schrijf de systeemprompt en vaste instructies in het Engels; houd alleen de invoer van gebruikers in het Nederlands.
- Laat tussenstappen (classificatie, extractie, tool-aanroepen) in het Engels of als JSON teruggeven, en alleen het eindantwoord in het Nederlands.
- Gebruik prompt caching voor het vaste deel van de prompt.

## Beperkingen

- Er is één prompt gemeten; bij andere teksten kan de verhouding ±0,1–0,2 afwijken.
- Claude en Gemini gebruiken andere tokenizers; deze cijfers gelden alleen voor OpenAI-modellen.
- De vertaling is gebaseerd op een gecontroleerde machinevertaling.

Alle resultaten voor 41 talen (in het Engels): [vergelijking van 41 talen](/blog/token-cost-by-language)

Alle 41 talen naast elkaar staan in de [talentabel](/languages).

## Bronnen

- [tiktoken: de tokenizer van OpenAI (o200k_base) op GitHub](https://github.com/openai/tiktoken)
- [Prijzen van de OpenAI API](https://developers.openai.com/api/docs/pricing)

<!-- autoimg -->
