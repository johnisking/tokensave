Google presentó **Gemini 4 Argon** el 30 de septiembre de 2026, su nuevo modelo más potente. Está pensado para programación, ciberseguridad y tareas largas con agentes, y Google asegura que supera a GPT-6 Astra y a Claude Fable y Opus en varios benchmarks. Aquí tienes cuánto cuesta en la API, cuánto sale una petición real y cómo se compara con GPT y Claude.

## Precio de la API de Gemini 4 Argon

Precios por millón de tokens. Empieza con un precio de lanzamiento y después pasa al precio estándar.

| Tarifa | Entrada | Entrada en caché | Salida |
|---|---|---|---|
| Lanzamiento | $2 | ~$0,10 | $10 |
| Estándar | $4 | ~$0,20 | $20 |

La entrada en caché tiene un 95% de descuento, algo que se nota mucho si envías una y otra vez las mismas instrucciones o documentos. Google no ha dicho cuánto durará el precio de lanzamiento.

Argon también puede **generar hasta 1 millón de tokens** en una sola respuesta. Eso sí, una salida larga cuesta en proporción: 1 millón de tokens de salida son $20 por respuesta con el precio estándar.

## ¿Ya se puede usar?

Todavía no. Por ahora solo está disponible para los socios del programa de ciberdefensa Fairwind de Google, y después llegará a los suscriptores de Google AI Ultra y a los clientes de pago de la API. El identificador del modelo en la API sería `gemini-4-argon`, pero aún no aparece en la documentación oficial.

## Cómo se compara

Una petición típica: 2.000 tokens de entrada y 500 de salida.

| Modelo | Por 1M de tokens (entrada/salida) | 1 petición | 10.000 peticiones |
|---|---|---|---|
| Gemini 3.8 Flash | $0,75 / $3,75 | $0,0034 | $34 |
| **Gemini 4 Argon (lanzamiento)** | $2 / $10 | $0,009 | $90 |
| GPT-6 Sol | $2 / $10 | $0,009 | $90 |
| Claude Sonnet 5.5 | $2 / $10 | $0,009 | $90 |
| Gemini 3.1 Pro | $2 / $12 | $0,010 | $100 |
| **Gemini 4 Argon (estándar)** | $4 / $20 | $0,018 | $180 |
| Claude Opus 5.5 | $4 / $20 | $0,018 | $180 |
| GPT-6 Astra | $10 / $50 | $0,045 | $450 |
| Claude Fable 5.1 | $10 / $50 | $0,045 | $450 |

Los demás precios son tarifas oficiales de API revisadas en octubre de 2026.

Lo más destacado:

- **El precio estándar es exactamente el de Claude Opus 5.5:** $4 de entrada y $20 de salida.
- **El precio de lanzamiento es el mismo que GPT-6 Sol y Claude Sonnet 5.5.** Un modelo de gama alta a precio de gama media, de momento.
- **Incluso con el precio estándar es 2,5 veces más barato que GPT-6 Astra y Claude Fable 5.1.** Si se confirman los benchmarks de Google, es la mejor relación calidad-precio entre los modelos de gama alta.
- **Es más caro que Gemini 3.1 Pro**, unas 1,8 veces por petición con el precio estándar. Si 3.1 Pro ya te sirve, no hace falta cambiar.

## Cuándo usarlo

**Encaja bien en:** cambios grandes de código y migraciones, revisiones de seguridad, tareas largas con agentes de varios pasos y análisis de videos largos o gráficos. Cuanto más caro te salga un error, más vale la pena pagarlo.

**No hace falta para:** resúmenes, traducciones, clasificación y respuestas cortas. Gemini 3.8 Flash los resuelve por una quinta parte del costo por petición.

Lo habitual es mandar las peticiones del día a día a Flash o a 3.1 Pro y pasar a Argon solo las difíciles.

## Cómo gastar menos

1. **Pruébalo durante el lanzamiento.** Cuesta la mitad del precio estándar: es el mejor momento para ver si encaja con tu trabajo.
2. **Usa la caché.** La entrada en caché tiene un 95% de descuento, así que deja las instrucciones fijas y los documentos al principio del prompt.
3. **Limita la salida.** Puede escribir hasta 1 millón de tokens y la salida cuesta 5 veces más que la entrada. Pide solo lo que necesitas.
4. **Escribe los prompts en inglés.** En español el mismo texto suele ocupar más tokens. El botón 💸 Ahorrar tokens del [contador de tokens](/es/) traduce tu prompt al inglés dentro de tu propio dispositivo.

## Calcula tu propio costo

Ya puedes elegir Gemini 4 Argon en el [contador de tokens](/es/), con el precio estándar. Pega un prompt que uses de verdad y compara Argon, GPT-6 y Claude lado a lado.

*Los precios y las fechas de despliegue pueden cambiar. Revisa la [página de precios de la API de Gemini](https://ai.google.dev/gemini-api/docs/pricing) antes de trabajos grandes.*
