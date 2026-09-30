Käänsin saman asiakaspalvelupromptin 41 kielelle ja laskin tokenit o200k_basella, OpenAI:n nykyisellä tokenisoijalla (GPT-4o ja uudemmat). Englanniksi tarvitaan 34 tokenia, suomeksi **49 eli 1,44×**, sija 19/41 (1 = halvin).

Suomenkielinen versio:

> Tiivistä alla oleva asiakkaan sähköposti kolmeen kohtaan ja ehdota kohteliasta vastausta. Asiakas kertoo, että tilaus saapui kaksi päivää myöhässä ja laatikosta puuttui yksi tuote.

## Tulokset

| Kieli | Tokenit | Englantiin verrattuna | Vanha GPT-4-tokenisoija |
|---|---:|---:|---:|
| English | 34 | 1,00× | 1,00× |
| 简体中文 | 35 | 1,03× | 1,53× |
| Español | 40 | 1,18× | 1,29× |
| Deutsch | 43 | 1,26× | 1,50× |
| 한국어 | 49 | 1,44× | 2,50× |
| **Suomi** | **49** | **1,44×** | **2,03×** |
| हिन्दी | 51 | 1,50× | 4,59× |
| 日本語 | 61 | 1,79× | 2,21× |
| Čeština | 68 | 2,00× | 2,59× |
| Ελληνικά | 70 | 2,06× | 4,94× |
| ਪੰਜਾਬੀ | 83 | 2,44× | 7,41× |

![Tulokset](/blog-language-tax-chart-v4.png)

## Miksi

Tokenisoija oppii enimmäkseen englanninkielisestä tekstistä: sanat kuten " polite" tai " customer" ovat yksi token, kun taas päätteiden pidentämät suomen sanat pilkkoutuvat:

- kohteliasta → `koht | eli | asta` · 3
- laatikosta → `laat | ik | osta` · 3
- Tiivistä → `Ti | iv | istä` · 3

## Vanhaan tokenisoijaan verrattuna

GPT-4-ajan tokenisoijalla (cl100k) sama prompti vei **2,03×**, nyt **1,44×**. Suomi hyötyi muutoksesta selvästi.

## Rahana

Mallilla, jonka hinta on 2 $ miljoonaa syötetokenia kohden, tämän promptin lähettäminen miljoona kertaa maksaa englanniksi 68 $ ja suomeksi 98 $. Jos vastauskin on suomeksi, sama kerroin koskee tulostetokeneita, jotka ovat yleensä 4–5 kertaa kalliimpia.

## Miten säästää

- Kirjoita järjestelmäprompti ja kiinteät ohjeet englanniksi; jätä suomeksi vain käyttäjän syöte.
- Pyydä välivaiheet (luokittelu, poiminta, työkalukutsut) englanniksi tai JSON-muodossa ja vain lopullinen vastaus suomeksi.
- Käytä prompt cachingia promptin kiinteälle osalle.

## Rajoitukset

- Mittasin vain yhden promptin; muilla teksteillä suhde voi vaihdella ±0,1–0,2.
- Claudella ja Geminillä on eri tokenisoijat – luvut pätevät vain OpenAI:n malleihin.
- Käännös perustuu tarkistettuun konekäännökseen.

Kaikkien 41 kielen tulokset (englanniksi): [41 kielen vertailu](/blog/token-cost-by-language)
