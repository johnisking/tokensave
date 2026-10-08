![Deutsch braucht in GPT 26 % mehr Tokens als Englisch](/tokens-deutsch-gpt-de.jpg)

Ich habe denselben Kundenservice-Prompt in 41 Sprachen übersetzt und die Tokens mit o200k_base gezählt, dem aktuellen Tokenizer von OpenAI (GPT-4o und neuer). Englisch braucht 34 Tokens, Deutsch **43 – also 26% mehr**, Platz 7 von 41 (1 = am günstigsten).

Die deutsche Fassung:

> Fasse die folgende Kunden-E-Mail in drei Stichpunkten zusammen und schlage eine höfliche Antwort vor. Der Kunde sagt, dass die Bestellung zwei Tage zu spät ankam und ein Artikel im Paket fehlte.

## Ergebnisse

| Sprache | Tokens | Im Vergleich zu Englisch | Ersparnis auf Englisch |
|---|---:|---:|---:|
| English | 34 | ±0% | – |
| 简体中文 | 35 | +3% | 3% |
| Español | 40 | +18% | 15% |
| **Deutsch** | **43** | **+26%** | **21%** |
| 한국어 | 49 | +44% | 31% |
| हिन्दी | 51 | +50% | 33% |
| 日本語 | 61 | +79% | 44% |
| Čeština | 68 | +100% | 50% |
| Ελληνικά | 70 | +106% | 51% |
| ਪੰਜਾਬੀ | 83 | +144% | 59% |

![Diagramm: zusätzliche Tokens pro Sprache im Vergleich zu Englisch in GPT](/blog-language-tax-chart-v5.png)

## Warum

![Warum: Kunden-E-Mail → Kunden | -E | -Mail · 3; Stichpunkten → Stich | punk | ten · 3; höfliche → höf | liche · 2](/tokens-deutsch-gpt-de-2.jpg)

Der Tokenizer lernt vor allem aus englischem Text: Wörter wie „ polite“ oder „ customer“ sind ein einziger Token, deutsche Wörter – besonders Komposita – werden dagegen zerlegt:

- Kunden-E-Mail → `Kunden | -E | -Mail` · 3
- Stichpunkten → `Stich | punk | ten` · 3
- höfliche → `höf | liche` · 2

## Mit einem Klick auf Englisch umstellen

Am meisten sparst du, wenn du deinen Prompt auf Englisch sendest: rund 21 % weniger Tokens als auf Deutsch. Aktuelle Modelle verstehen englische Anweisungen bestens und antworten auf Deutsch, wenn du darum bittest. Füge deinen Prompt im TokenSave-Tokenzähler ein und drück **💸 Tokens sparen**: Er bereinigt Leerzeichen, übersetzt ins Englische, streicht Füllwörter und fügt "Reply in German." hinzu, damit die Antwort in deiner Sprache bleibt. Genutzt wird der integrierte Übersetzer von Desktop-Chrome 138+ / Edge 148+; die Übersetzung läuft auf deinem eigenen Gerät, und dein Text wird nie hochgeladen. Mit **↩ Original** bekommst du das Original zurück.

## In Geld

Bei einem Modell mit 2 $ pro 1 Mio. Input-Tokens kostet es 68 $ auf Englisch und 86 $ auf Deutsch, diesen Prompt eine Million Mal zu senden. Antwortet das Modell auch auf Deutsch, gilt derselbe Unterschied für die Output-Tokens, die meist 300–400% teurer sind.

## So sparst du

![So sparst du: System-Prompt und feste Anweisungen auf Englisch schreiben; nur die Eingaben der Nutzer bleiben auf Deutsch.; ](/tokens-deutsch-gpt-so-sparst-du-de.jpg)

- System-Prompt und feste Anweisungen auf Englisch schreiben; nur die Eingaben der Nutzer bleiben auf Deutsch.
- Zwischenschritte (Klassifizierung, Extraktion, Tool-Aufrufe) auf Englisch oder als JSON ausgeben lassen, nur die finale Antwort auf Deutsch.
- Prompt Caching für den festen Teil des Prompts nutzen.

## Einschränkungen

- Gemessen wurde ein einziger Prompt; bei anderen Texten kann der Faktor um ±0,1–0,2 abweichen.
- Claude und Gemini haben andere Tokenizer – die Zahlen gelten nur für OpenAI-Modelle.
- Die Übersetzung basiert auf einer geprüften maschinellen Übersetzung.

Probier es mit deinem eigenen Text im [Token-Rechner](/de/) aus; alle Sprachen im Vergleich stehen in der [Sprachtabelle](/languages).

Alle Ergebnisse für 41 Sprachen (auf Englisch): [Vergleich von 41 Sprachen](/blog/token-cost-by-language)

## Quellen

- [tiktoken: OpenAI-Tokenizer (o200k_base) auf GitHub](https://github.com/openai/tiktoken)
- [OpenAI-API-Preise](https://developers.openai.com/api/docs/pricing)

<!-- autoimg -->
