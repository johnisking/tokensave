Isinalin ko ang parehong customer-support prompt sa 41 wika at binilang ang token gamit ang o200k_base, ang kasalukuyang tokenizer ng OpenAI (GPT-4o at mas bago). Sa English, 34 token; sa Filipino, **52 token — 1.53× ng English**, ika-22 sa 41 (1 = pinakamura).

Ang bersyong Filipino:

> Ibuod ang email ng customer sa ibaba sa tatlong punto at magmungkahi ng magalang na sagot. Sinabi ng customer na dumating ang order nang dalawang araw na huli at may isang item na kulang sa kahon.

## Mga resulta

| Wika | Token | Kumpara sa English | Matitipid kung ipapadala sa English |
|---|---:|---:|---:|
| English | 34 | 1.00× | – |
| 简体中文 | 35 | 1.03× | 3% |
| Español | 40 | 1.18× | 15% |
| Deutsch | 43 | 1.26× | 21% |
| 한국어 | 49 | 1.44× | 31% |
| हिन्दी | 51 | 1.50× | 33% |
| **Filipino** | **52** | **1.53×** | **35%** |
| 日本語 | 61 | 1.79× | 44% |
| Čeština | 68 | 2.00× | 50% |
| Ελληνικά | 70 | 2.06× | 51% |
| ਪੰਜਾਬੀ | 83 | 2.44× | 59% |

![Mga resulta](/blog-language-tax-chart-v4.png)

## Bakit

Karamihang natututo ang tokenizer mula sa English na text: isang token lang ang mga salitang tulad ng " polite" o " customer", pero hinahati-hati ang maraming salitang Filipino na may panlapi:

- magmungkahi → `mag | m | ungk | ahi` · 4
- Ibuod → `I | bu | od` · 3
- magalang → `mag | alang` · 2

## Lumipat sa English sa isang pindot

Pinakamalaki ang matitipid kung sa English mo ipapadala ang prompt: mga 35% na mas kaunting token kumpara sa Filipino. Naiintindihan nang mabuti ng mga model ngayon ang instruction sa English at sasagot sila sa Filipino kung hihilingin mo. Hindi pa sinusuportahan ng built-in translator ng browser ang Filipino, kaya isalin nang isang beses sa English ang mga nakapirming instruction mo at gamitin ulit ang mga ito; ipinapakita ng TokenSave token counter kung eksaktong ilang token ang natitipid mo.

## Sa pera

Sa model na $2 bawat 1 milyong input token, ang pagpapadala ng prompt na ito nang 1 milyong beses ay $68 sa English at $104 sa Filipino. Kung Filipino rin ang sagot, parehong multiplier ang tatama sa output token, na kadalasang 4–5× na mas mahal.

## Paano makatipid

- Isulat sa English ang system prompt at mga nakapirming tagubilin; Filipino lang ang input ng user.
- Hilingin sa English o JSON ang mga pansamantalang hakbang (classification, extraction, tool call), at Filipino lang ang huling sagot.
- Gumamit ng prompt caching para sa nakapirming bahagi ng prompt.

## Mga limitasyon

- Isang prompt lang ang sinukat; sa ibang text, maaaring mag-iba ang ratio ng ±0.1–0.2.
- Iba ang tokenizer ng Claude at Gemini; para lang sa mga OpenAI model ang mga numerong ito.
- Batay ang salin sa sinuring machine translation.

Buong resulta ng 41 wika (sa English): [paghahambing ng 41 wika](/blog/token-cost-by-language)
