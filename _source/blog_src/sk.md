![Slovenčina v GPT stojí o 100% viac tokenov ako angličtina](/tokeny-slovencina-gpt-sk.jpg)

Ten istý prompt zákazníckej podpory som preložil do 41 jazykov a tokeny spočítal pomocou o200k_base, aktuálneho tokenizéra OpenAI (GPT-4o a novšie). Angličtina potrebuje 34 tokenov, slovenčina **68 — teda o 100% viac**, miesto 38 z 41 (1 = najlacnejší). Drahšie sú už len telugčina, gréčtina a pandžábčina.

Slovenská verzia:

> Zhrňte nižšie uvedený e-mail zákazníka do troch bodov a navrhnite zdvorilú odpoveď. Zákazník píše, že objednávka dorazila s dvojdňovým oneskorením a v krabici chýbala jedna položka.

## Výsledky

| Jazyk | Tokeny | Oproti angličtine | Úspora pri odoslaní v angličtine |
|---|---:|---:|---:|
| English | 34 | ±0% | – |
| 简体中文 | 35 | +3% | 3% |
| Español | 40 | +18% | 15% |
| Deutsch | 43 | +26% | 21% |
| 한국어 | 49 | +44% | 31% |
| हिन्दी | 51 | +50% | 33% |
| 日本語 | 61 | +79% | 44% |
| Čeština | 68 | +100% | 50% |
| **Slovenčina** | **68** | **+100%** | **50%** |
| Ελληνικά | 70 | +106% | 51% |
| ਪੰਜਾਬੀ | 83 | +144% | 59% |

![Graf: tokeny navyše pre každý jazyk v porovnaní s angličtinou v GPT (41 jazykov)](/blog-language-tax-chart-v5.png)

## Prečo

![Prečo: oneskorením → ones | k | oren | ím · 4; dvojdňovým → dvoj | d | ň | ovým · 4; navrhnite → nav | r | hn | ite ·](/tokeny-slovencina-gpt-sk-2.jpg)

Tokenizér sa učí hlavne z anglického textu: slová ako " polite" či " customer" sú jeden token, kým slovenské slová s koncovkami a mäkčeňmi sa rozpadajú na kúsky:

- oneskorením → `ones | k | oren | ím` · 4
- dvojdňovým → `dvoj | d | ň | ovým` · 4
- navrhnite → `nav | r | hn | ite` · 4

## Prepnite do angličtiny jedným tlačidlom

Najväčšia úspora je poslať prompt v angličtine: pre slovenčinu asi o 50% menej tokenov. Súčasné modely anglickým inštrukciám výborne rozumejú a odpovedia po slovensky, keď ich o to požiadate. V [počítadle tokenov TokenSave](/sk/) vložte prompt a stlačte **💸 Ušetriť tokeny**: odstráni nadbytočné medzery, preloží text do angličtiny, vynechá výplňové slová a pridá „Reply in Slovak.“, aby odpoveď zostala vo vašom jazyku. Využíva prekladač vstavaný v Chrome 138+ / Edge 148+ na počítači; preklad prebieha vo vašom zariadení a text sa nikam neodosiela. Stlačením **↩ Originál** vrátite pôvodný text.

## V peniazoch

S modelom za 2 $ na milión vstupných tokenov stojí odoslanie tohto promptu miliónkrát 68 $ v angličtine a 136 $ v slovenčine. Ak model odpovedá tiež po slovensky, rovnaký násobok platí aj pre výstupné tokeny, ktoré bývajú o 300–400% drahšie.

## Ako ušetriť

![Ako ušetriť: Systémový prompt a pevné inštrukcie píšte po anglicky; po slovensky nechajte len vstup od používateľa.; Medzik](/tokeny-slovencina-gpt-ako-usetrit-sk.jpg)

- Systémový prompt a pevné inštrukcie píšte po anglicky; po slovensky nechajte len vstup od používateľa.
- Medzikroky (klasifikácia, extrakcia, volania nástrojov) si pýtajte po anglicky alebo v JSON, po slovensky len finálnu odpoveď.
- Pre pevnú časť promptu použite prompt caching.

## Obmedzenia

- Meraný bol jeden prompt; pri iných textoch sa pomer môže líšiť o ±0,1–0,2.
- Claude a Gemini používajú iné tokenizéry — čísla platia len pre modely OpenAI.
- Preklad vychádza z overeného strojového prekladu.

Všetky výsledky pre 41 jazykov (po anglicky): [porovnanie 41 jazykov](/blog/token-cost-by-language)

Všetkých 41 jazykov vedľa seba nájdete v [tabuľke jazykov](/languages).

## Zdroje

- [tiktoken: tokenizér OpenAI (o200k_base) na GitHube](https://github.com/openai/tiktoken)
- [Cenník OpenAI API](https://developers.openai.com/api/docs/pricing)

<!-- autoimg -->
