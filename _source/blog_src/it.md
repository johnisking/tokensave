![L’italiano usa 1,38× i token dell’inglese in GPT](/token-italiano-gpt-it.jpg)

Ho tradotto lo stesso prompt di assistenza clienti in 41 lingue e contato i token con o200k_base, il tokenizer attuale di OpenAI (GPT-4o e successivi). In inglese servono 34 token; in italiano **47, cioè 1,38× l’inglese**, posizione 17 su 41 (1 = il più economico).

La versione italiana:

> Riassumi l'email del cliente qui sotto in tre punti e suggerisci una risposta cortese. Il cliente dice che l'ordine è arrivato con due giorni di ritardo e che mancava un articolo nella scatola.

## Risultati

| Lingua | Token | Rispetto all’inglese | Risparmio inviando in inglese |
|---|---:|---:|---:|
| English | 34 | 1,00× | – |
| 简体中文 | 35 | 1,03× | 3% |
| Español | 40 | 1,18× | 15% |
| Deutsch | 43 | 1,26× | 21% |
| **Italiano** | **47** | **1,38×** | **28%** |
| 한국어 | 49 | 1,44× | 31% |
| हिन्दी | 51 | 1,50× | 33% |
| 日本語 | 61 | 1,79× | 44% |
| Čeština | 68 | 2,00× | 50% |
| Ελληνικά | 70 | 2,06× | 51% |
| ਪੰਜਾਬੀ | 83 | 2,44× | 59% |

![Risultati](/blog-language-tax-chart-v4.png)

## Perché

![Perché: Riassumi → Ri | ass | umi · 3; suggerisci → sugger | isci · 2; arrivato → arriv | ato · 2](/token-italiano-gpt-perche-it.jpg)

Il tokenizer impara soprattutto da testo inglese: parole come " polite" o " customer" sono un solo token, mentre molte parole italiane vengono spezzate:

- Riassumi → `Ri | ass | umi` · 3
- suggerisci → `sugger | isci` · 2
- arrivato → `arriv | ato` · 2

## Passa all'inglese con un pulsante

Il risparmio maggiore si ottiene inviando il prompt in inglese: circa il 28% di token in meno rispetto all'italiano. I modelli attuali capiscono perfettamente le istruzioni in inglese e rispondono in italiano se glielo chiedi. Nel contatore di token di TokenSave, incolla il tuo prompt e premi **💸 Risparmia token**: pulisce gli spazi, traduce in inglese, elimina il superfluo e aggiunge "Reply in Italian." così la risposta resta nella tua lingua. Usa il traduttore integrato in Chrome 138+ / Edge 148+ per desktop; la traduzione avviene sul tuo dispositivo e il tuo testo non viene mai caricato. Premi **↩ Originale** per recuperare l'originale.

## In denaro

Con un modello a 2 $ per milione di token in input, inviare questo prompt un milione di volte costa 68 $ in inglese e 94 $ in italiano. Se anche la risposta è in italiano, lo stesso moltiplicatore vale per i token in output, che di solito costano 4–5× di più.

## Come risparmiare

![Come risparmiare: Scrivi il prompt di sistema e le istruzioni fisse in inglese; lascia in italiano solo l’input dell’utente.; Ch](/token-italiano-gpt-come-risparmiare-it.jpg)

- Scrivi il prompt di sistema e le istruzioni fisse in inglese; lascia in italiano solo l’input dell’utente.
- Chiedi i passaggi intermedi (classificazione, estrazione, chiamate a strumenti) in inglese o JSON e solo la risposta finale in italiano.
- Usa il prompt caching per la parte fissa del prompt.

## Limiti

- È un solo prompt: con altri testi il rapporto può variare di ±0,1–0,2.
- Claude e Gemini usano altri tokenizer: questi numeri valgono solo per i modelli OpenAI.
- La traduzione parte da una traduzione automatica revisionata.

Risultati completi delle 41 lingue (in inglese): [confronto tra 41 lingue](/blog/token-cost-by-language)
<!-- autoimg -->
