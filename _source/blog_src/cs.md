Přeložil jsem jeden běžný prompt do 41 jazyků a spočítal tokeny tokenizérem, který používají současné modely OpenAI (o200k_base, GPT-4o a novější). Čekal jsem, že nejhůř dopadne japonština nebo thajština. Obě ale vyšly levněji než **čeština** (2,00×): z Evropy je dražší jen řečtina (2,06×), stejně jako čeština vychází slovenština, a z celého srovnání už jen indická telugština (2,03×) a pandžábština (2,44×).

Prompt (anglicky 34 tokenů):

> Shrňte níže uvedený e-mail zákazníka do tří bodů a navrhněte zdvořilou odpověď. Zákazník píše, že objednávka dorazila se dvoudenním zpožděním a v krabici chyběla jedna položka.

| Jazyk | Tokeny | Oproti angličtině | Starý GPT-4 tokenizér |
|---|---:|---:|---:|
| Angličtina | 34 | 1,00× | 1,00× |
| Čínština (zjednodušená) | 35 | 1,03× | 1,53× |
| Němčina | 43 | 1,26× | 1,50× |
| Ruština | 45 | 1,32× | 2,15× |
| Korejština | 49 | 1,44× | 2,50× |
| Japonština | 61 | 1,79× | 2,21× |
| Polština | 64 | 1,88× | 2,12× |
| Ukrajinština | 64 | 1,88× | 3,15× |
| **Čeština** | **68** | **2,00×** | **2,59×** |
| Slovenština | 68 | 2,00× | 2,53× |
| Telugština | 69 | 2,03× | 9,38× |
| Řečtina | 70 | 2,06× | 4,94× |
| Pandžábština | 83 | 2,44× | 7,41× |

![Graf](/blog-language-tax-chart-v4.png)

**Proč?** Tokenizér zná celá anglická slova (" polite", " customer" = 1 token), ale česká slova skládá z kousků. Háčky a čárky často tvoří samostatný token:

- " zdvořilou" → ` zd | vo | ř | il | ou` (5 tokenů)
- " zpožděním" → ` z | po | žd | ě | ním` (5 tokenů)
- " navrhněte" → ` nav | r | hn | ě | te` (5 tokenů)

Zajímavost: stejný text **bez diakritiky** má 60 tokenů místo 68 (o 12 % méně). Nedoporučuju to jako trik, kvalita odpovědí může utrpět, ale ukazuje to, kolik stojí háčky a čárky.

**V penězích:** model za 2 $ / 1M vstupních tokenů, prompt poslaný milionkrát: angličtina 68 $, čeština 136 $. A to jen vstup. Pokud model odpovídá česky, stejný násobek platí i pro výstupní tokeny, které bývají 4–5× dražší.

**Co s tím:**

- Systémový prompt a pevné instrukce psát anglicky, česky jen vstup od uživatele.
- Mezikroky (klasifikace, extrakce, tool calls) nechat vracet anglicky nebo v JSON, česky jen finální odpověď.
- Využít prompt caching pro pevnou část promptu.

Omezení: je to jeden prompt, u jiných textů se poměr může lišit o ±0,1–0,2. Claude a Gemini mají jiné tokenizéry, čísla platí jen pro modely OpenAI. Překlad je strojový, pokud v něm najdete chybu, přeměřím to.

Celé výsledky všech 41 jazyků (anglicky): [srovnání 41 jazyků](/blog/token-cost-by-language)
