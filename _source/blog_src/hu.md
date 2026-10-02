Ugyanazt az ügyfélszolgálati promptot lefordítottam 41 nyelvre, és a tokeneket az o200k_base-szel, az OpenAI jelenlegi tokenizálójával (GPT-4o és újabbak) számoltam meg. Angolul 34 token kell, magyarul **59 — ez 1,74× annyi**, 41 nyelv közül a 30. helyen a legolcsóbbtól számítva.

A magyar változat:

> Foglald össze az alábbi ügyfél-e-mailt három pontban, és javasolj egy udvarias választ. Az ügyfél azt írja, hogy a rendelés két nap késéssel érkezett, és egy termék hiányzott a dobozból.

## Eredmények

| Nyelv | Tokenek | Az angolhoz képest | Megtakarítás angol nyelvű küldéssel |
|---|---:|---:|---:|
| English | 34 | 1,00× | – |
| 简体中文 | 35 | 1,03× | 3% |
| Español | 40 | 1,18× | 15% |
| Deutsch | 43 | 1,26× | 21% |
| 한국어 | 49 | 1,44× | 31% |
| हिन्दी | 51 | 1,50× | 33% |
| **Magyar** | **59** | **1,74×** | **43%** |
| 日本語 | 61 | 1,79× | 44% |
| Čeština | 68 | 2,00× | 50% |
| Ελληνικά | 70 | 2,06× | 51% |
| ਪੰਜਾਬੀ | 83 | 2,44× | 59% |

![Eredmények](/blog-language-tax-chart-v4.png)

## Miért

A tokenizáló főleg angol szövegből tanul: az olyan szavak, mint a " polite" vagy a " customer", egyetlen tokenek, a toldalékokkal hosszú magyar szavak viszont darabokra esnek:

- ügyfél-e-mailt → `ügy | fél | -e | -mail | t` · 5
- dobozból → `do | bo | zb | ól` · 4
- hiányzott → `hi | ány | zott` · 3

## Válts angolra egy gombnyomással

A legnagyobb megtakarítás, ha angolul küldöd a promptot: magyar nyelv esetén kb. 43%-kal kevesebb token. A mai modellek tökéletesen értik az angol utasításokat, és magyarul válaszolnak, ha kéred. A TokenSave tokenszámlálójában illeszd be a promptot, és nyomd meg a **💸 Tokenspórolás** gombot: eltávolítja a felesleges szóközöket, angolra fordít, kigyomlálja a töltelékszavakat, és hozzáadja a „Reply in Hungarian.” sort, hogy a válasz a te nyelveden maradjon. Az asztali Chrome 138+ / Edge 148+ beépített fordítóját használja; a fordítás a saját eszközödön fut, a szöveged sosem kerül feltöltésre. Az eredetit a **↩ Eredeti** gombbal kapod vissza.

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
