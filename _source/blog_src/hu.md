Ugyanazt az ügyfélszolgálati promptot lefordítottam 41 nyelvre, és a tokeneket az o200k_base-szel, az OpenAI jelenlegi tokenizálójával (GPT-4o és újabbak) számoltam meg. Angolul 34 token kell, magyarul **59 — ez 1,74× annyi**, 41 nyelv közül a 30. helyen a legolcsóbbtól számítva.

A magyar változat:

> Foglald össze az alábbi ügyfél-e-mailt három pontban, és javasolj egy udvarias választ. Az ügyfél azt írja, hogy a rendelés két nap késéssel érkezett, és egy termék hiányzott a dobozból.

## Eredmények

| Nyelv | Tokenek | Az angolhoz képest | Régi GPT-4 tokenizáló |
|---|---:|---:|---:|
| English | 34 | 1,00× | 1,00× |
| 简体中文 | 35 | 1,03× | 1,53× |
| Español | 40 | 1,18× | 1,29× |
| Deutsch | 43 | 1,26× | 1,50× |
| 한국어 | 49 | 1,44× | 2,50× |
| हिन्दी | 51 | 1,50× | 4,59× |
| **Magyar** | **59** | **1,74×** | **2,26×** |
| 日本語 | 61 | 1,79× | 2,21× |
| Čeština | 68 | 2,00× | 2,59× |
| Ελληνικά | 70 | 2,06× | 4,94× |
| ਪੰਜਾਬੀ | 83 | 2,44× | 7,41× |

![Eredmények](/blog-language-tax-chart-v4.png)

## Miért

A tokenizáló főleg angol szövegből tanul: az olyan szavak, mint a " polite" vagy a " customer", egyetlen tokenek, a toldalékokkal hosszú magyar szavak viszont darabokra esnek:

- ügyfél-e-mailt → `ügy | fél | -e | -mail | t` · 5
- dobozból → `do | bo | zb | ól` · 4
- hiányzott → `hi | ány | zott` · 3

## A régi tokenizálóhoz képest

A GPT-4-korszak tokenizálóján (cl100k) ugyanez a prompt **2,26×** volt, ma **1,74×**.

## Pénzben

Egy 1 millió bemeneti tokenenként 2 dolláros modellnél ezt a promptot egymilliószor elküldeni angolul 68 dollár, magyarul 118 dollár. Ha a válasz is magyarul jön, ugyanez a szorzó érvényes a kimeneti tokenekre, amelyek általában 4–5× drágábbak.

## Hogyan spórolj

- A rendszerpromptot és az állandó utasításokat írd angolul; csak a felhasználó bemenete maradjon magyarul.
- A köztes lépéseket (osztályozás, kinyerés, eszközhívások) kérd angolul vagy JSON-ban, és csak a végső választ magyarul.
- Használj prompt cachinget a prompt állandó részére.

## Korlátok

- Egyetlen promptot mértem; más szövegeknél az arány ±0,1–0,2-vel eltérhet.
- A Claude és a Gemini más tokenizálót használ — ezek a számok csak az OpenAI-modellekre érvényesek.
- A fordítás ellenőrzött gépi fordításon alapul.

Mind a 41 nyelv eredménye (angolul): [41 nyelv összehasonlítása](/blog/token-cost-by-language)
