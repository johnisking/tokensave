![Suomi vie GPT:ssä 1,44× englannin tokenmäärän](/tokenit-suomi-gpt-fi.jpg)

Käänsin saman asiakaspalvelupromptin 41 kielelle ja laskin tokenit o200k_basella, OpenAI:n nykyisellä tokenisoijalla (GPT-4o ja uudemmat). Englanniksi tarvitaan 34 tokenia, suomeksi **49 eli 1,44×**, sija 19/41 (1 = halvin).

Suomenkielinen versio:

> Tiivistä alla oleva asiakkaan sähköposti kolmeen kohtaan ja ehdota kohteliasta vastausta. Asiakas kertoo, että tilaus saapui kaksi päivää myöhässä ja laatikosta puuttui yksi tuote.

## Tulokset

| Kieli | Tokenit | Englantiin verrattuna | Säästö englanniksi lähetettynä |
|---|---:|---:|---:|
| English | 34 | 1,00× | – |
| 简体中文 | 35 | 1,03× | 3% |
| Español | 40 | 1,18× | 15% |
| Deutsch | 43 | 1,26× | 21% |
| **Suomi** | **49** | **1,44×** | **31%** |
| 한국어 | 49 | 1,44× | 31% |
| हिन्दी | 51 | 1,50× | 33% |
| 日本語 | 61 | 1,79× | 44% |
| Čeština | 68 | 2,00× | 50% |
| Ελληνικά | 70 | 2,06× | 51% |
| ਪੰਜਾਬੀ | 83 | 2,44× | 59% |

![Tulokset](/blog-language-tax-chart-v4.png)

## Miksi

![Miksi: kohteliasta → koht | eli | asta · 3; laatikosta → laat | ik | osta · 3; Tiivistä → Ti | iv | istä · 3](/tokenit-suomi-gpt-fi-2.jpg)

Tokenisoija oppii enimmäkseen englanninkielisestä tekstistä: sanat kuten " polite" tai " customer" ovat yksi token, kun taas päätteiden pidentämät suomen sanat pilkkoutuvat:

- kohteliasta → `koht | eli | asta` · 3
- laatikosta → `laat | ik | osta` · 3
- Tiivistä → `Ti | iv | istä` · 3

## Vaihda englantiin yhdellä painikkeella

Suurin säästö syntyy, kun lähetät kehotteen englanniksi: suomeen verrattuna noin 31 % vähemmän tokeneita. Nykyiset mallit ymmärtävät englanninkieliset ohjeet erinomaisesti ja vastaavat suomeksi, jos pyydät. Liitä kehote TokenSaven token-laskuriin ja paina **💸 Säästä tokeneita**: se siistii välilyönnit, kääntää englanniksi, karsii täytesanat ja lisää rivin "Reply in Finnish.", jotta vastaus tulee omalla kielelläsi. Se käyttää työpöydän Chrome 138+:aan / Edge 148+:aan sisäänrakennettua kääntäjää; käännös tehdään omalla laitteellasi, eikä tekstiäsi koskaan ladata palvelimelle. Paina **↩ Alkuperäinen**, niin saat alkuperäisen takaisin.

## Rahana

Mallilla, jonka hinta on 2 $ miljoonaa syötetokenia kohden, tämän promptin lähettäminen miljoona kertaa maksaa englanniksi 68 $ ja suomeksi 98 $. Jos vastauskin on suomeksi, sama kerroin koskee tulostetokeneita, jotka ovat yleensä 4–5 kertaa kalliimpia.

## Miten säästää

![Miten säästää: Kirjoita järjestelmäprompti ja kiinteät ohjeet englanniksi; jätä suomeksi vain käyttäjän syöte.; Pyydä välivai](/tokenit-suomi-gpt-miten-saastaa-fi.jpg)

- Kirjoita järjestelmäprompti ja kiinteät ohjeet englanniksi; jätä suomeksi vain käyttäjän syöte.
- Pyydä välivaiheet (luokittelu, poiminta, työkalukutsut) englanniksi tai JSON-muodossa ja vain lopullinen vastaus suomeksi.
- Käytä prompt cachingia promptin kiinteälle osalle.

## Rajoitukset

- Mittasin vain yhden promptin; muilla teksteillä suhde voi vaihdella ±0,1–0,2.
- Claudella ja Geminillä on eri tokenisoijat – luvut pätevät vain OpenAI:n malleihin.
- Käännös perustuu tarkistettuun konekäännökseen.

Kaikkien 41 kielen tulokset (englanniksi): [41 kielen vertailu](/blog/token-cost-by-language)
<!-- autoimg -->
