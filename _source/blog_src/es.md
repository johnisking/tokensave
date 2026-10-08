![El español gasta un 18% más de tokens que el inglés en GPT](/tokens-espanol-gpt-es.jpg)

Traduje el mismo prompt de atención al cliente a 41 idiomas y conté los tokens con o200k_base, el tokenizador actual de OpenAI (GPT-4o y posteriores). En inglés son 34 tokens; en español, **40: un 18% más que el inglés**, puesto 4 de 41 (1 = el más barato).

La versión en español:

> Resume el siguiente correo del cliente en tres puntos y sugiere una respuesta amable. El cliente dice que el pedido llegó con dos días de retraso y que faltaba un artículo en la caja.

## Resultados

| Idioma | Tokens | Frente al inglés | Ahorro si se envía en inglés |
|---|---:|---:|---:|
| English | 34 | ±0% | – |
| 简体中文 | 35 | +3% | 3% |
| **Español** | **40** | **+18%** | **15%** |
| Deutsch | 43 | +26% | 21% |
| 한국어 | 49 | +44% | 31% |
| हिन्दी | 51 | +50% | 33% |
| 日本語 | 61 | +79% | 44% |
| Čeština | 68 | +100% | 50% |
| Ελληνικά | 70 | +106% | 51% |
| ਪੰਜਾਬੀ | 83 | +144% | 59% |

![Gráfico: tokens adicionales por idioma frente al inglés en GPT](/blog-language-tax-chart-v5.png)

## Por qué

![Por qué: sugiere → su | gi | ere · 3; retraso → retras | o · 2; faltaba → falt | aba · 2](/tokens-espanol-gpt-por-que-es.jpg)

El tokenizador aprende sobre todo de texto en inglés: palabras como " polite" o " customer" son un solo token, mientras que muchas palabras en español se parten en trozos:

- sugiere → `su | gi | ere` · 3
- retraso → `retras | o` · 2
- faltaba → `falt | aba` · 2

## Pasa a inglés con un solo botón

El mayor ahorro consiste en enviar tu prompt en inglés: alrededor de un 15% menos de tokens que en español. Los modelos actuales entienden perfectamente las instrucciones en inglés y responden en español si se lo pides. En el contador de tokens de TokenSave, pega tu prompt y pulsa **💸 Ahorrar tokens**: limpia los espacios, lo traduce al inglés, recorta el relleno y añade "Reply in Spanish." para que la respuesta siga en tu idioma. Usa el traductor integrado en Chrome 138+ / Edge 148+ de escritorio; la traducción se hace en tu propio dispositivo y tu texto nunca se sube. Pulsa **↩ Original** para recuperar el original.

## En dinero

Con un modelo a 2 $ por millón de tokens de entrada, enviar este prompt un millón de veces cuesta 68 $ en inglés y 80 $ en español. Si la respuesta también es en español, la misma diferencia se aplica a los tokens de salida, que suelen costar un 300–400% más.

## Cómo ahorrar

![Cómo ahorrar: Escribe el prompt de sistema y las instrucciones fijas en inglés; deja en español solo lo que escribe el usuar](/tokens-espanol-gpt-como-ahorrar-es.jpg)

- Escribe el prompt de sistema y las instrucciones fijas en inglés; deja en español solo lo que escribe el usuario.
- Pide los pasos intermedios (clasificación, extracción, llamadas a herramientas) en inglés o JSON y solo la respuesta final en español.
- Usa prompt caching para la parte fija del prompt.

## Limitaciones

- Es un solo prompt; con otros textos la proporción puede variar ±0,1–0,2.
- Claude y Gemini usan otros tokenizadores: estas cifras valen solo para modelos de OpenAI.
- La traducción parte de una traducción automática revisada.

Prueba con tu propio texto en el [contador de tokens](/es/); todos los idiomas comparados están en la [tabla de idiomas](/languages).

Resultados completos de los 41 idiomas (en inglés): [comparativa de 41 idiomas](/blog/token-cost-by-language)

## Fuentes

- [tiktoken: el tokenizador de OpenAI (o200k_base) en GitHub](https://github.com/openai/tiktoken)
- [Precios de la API de OpenAI](https://developers.openai.com/api/docs/pricing)

<!-- autoimg -->
