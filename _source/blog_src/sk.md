Ten istý prompt zákazníckej podpory som preložil do 41 jazykov a tokeny spočítal pomocou o200k_base, aktuálneho tokenizéra OpenAI (GPT-4o a novšie). Angličtina potrebuje 34 tokenov, slovenčina **68 — teda 2,00×**, miesto 38 z 41 (1 = najlacnejší). Drahšie sú už len telugčina, gréčtina a pandžábčina.

Slovenská verzia:

> Zhrňte nižšie uvedený e-mail zákazníka do troch bodov a navrhnite zdvorilú odpoveď. Zákazník píše, že objednávka dorazila s dvojdňovým oneskorením a v krabici chýbala jedna položka.

## Výsledky

| Jazyk | Tokeny | Oproti angličtine | Starý tokenizér GPT-4 |
|---|---:|---:|---:|
| English | 34 | 1,00× | 1,00× |
| 简体中文 | 35 | 1,03× | 1,53× |
| Español | 40 | 1,18× | 1,29× |
| Deutsch | 43 | 1,26× | 1,50× |
| 한국어 | 49 | 1,44× | 2,50× |
| हिन्दी | 51 | 1,50× | 4,59× |
| 日本語 | 61 | 1,79× | 2,21× |
| **Slovenčina** | **68** | **2,00×** | **2,53×** |
| Čeština | 68 | 2,00× | 2,59× |
| Ελληνικά | 70 | 2,06× | 4,94× |
| ਪੰਜਾਬੀ | 83 | 2,44× | 7,41× |

![Výsledky](/blog-language-tax-chart-v4.png)

## Prečo

Tokenizér sa učí hlavne z anglického textu: slová ako " polite" či " customer" sú jeden token, kým slovenské slová s koncovkami a mäkčeňmi sa rozpadajú na kúsky:

- oneskorením → `ones | k | oren | ím` · 4
- dvojdňovým → `dvoj | d | ň | ovým` · 4
- navrhnite → `nav | r | hn | ite` · 4

## Oproti starému tokenizéru

Na tokenizéri z éry GPT-4 (cl100k) stál ten istý prompt **2,53×**, dnes **2,00×**.

## V peniazoch

S modelom za 2 $ na milión vstupných tokenov stojí odoslanie tohto promptu miliónkrát 68 $ v angličtine a 136 $ v slovenčine. Ak model odpovedá tiež po slovensky, rovnaký násobok platí aj pre výstupné tokeny, ktoré bývajú 4–5× drahšie.

## Ako ušetriť

- Systémový prompt a pevné inštrukcie píšte po anglicky; po slovensky nechajte len vstup od používateľa.
- Medzikroky (klasifikácia, extrakcia, volania nástrojov) si pýtajte po anglicky alebo v JSON, po slovensky len finálnu odpoveď.
- Pre pevnú časť promptu použite prompt caching.

## Obmedzenia

- Meraný bol jeden prompt; pri iných textoch sa pomer môže líšiť o ±0,1–0,2.
- Claude a Gemini používajú iné tokenizéry — čísla platia len pre modely OpenAI.
- Preklad vychádza z overeného strojového prekladu.

Všetky výsledky pre 41 jazykov (po anglicky): [porovnanie 41 jazykov](/blog/token-cost-by-language)
