![Precio de Claude Code: ¿cuánto cuesta al mes? Pro vs Max vs API](/claude-code-precio-es.jpg)

¿Cuánto cuesta Claude Code? Claude Code viene incluido en las suscripciones Claude Pro y Max de Anthropic, y también puede funcionar con créditos de la API que pagas según el uso. Entonces, ¿cuál es el precio de Claude Code al mes? Depende de cuánto lo uses, y la diferencia entre la forma más barata y la más cara de pagar por el mismo trabajo puede ser de diez veces o más. Si buscabas Claude Code gratis, la respuesta corta es que siempre se paga, ya sea con un plan o por token; lo que sí puedes hacer es elegir la opción más barata para tu caso. Aquí tienes las cifras reales.

## Dos formas de pagar Claude Code

![Dos formas de pagar Claude Code: Plan, Precio al mes, Uso](/claude-code-precio-dos-formas-de-pagar-claude-code-es.jpg)

**1. Una suscripción.** Claude Code está incluido en estos planes (precios de EE. UU., revisados en octubre de 2026):

| Plan | Precio al mes | Uso |
|---|---|---|
| Pro | $20 ($17 con facturación anual) | Nivel base |
| Max 5× | $100 | 5× el uso de Pro |
| Max 20× | $200 | 20× el uso de Pro |

Pagas una tarifa fija y tienes límites de uso. Claude Code y la app de Claude comparten los mismos límites.

**2. La API.** Pagas por token según los precios de la API de Anthropic:

| Modelo | Entrada / 1M tokens | Salida / 1M tokens |
|---|---|---|
| Claude Haiku 4.5 | $1 | $5 |
| Claude Sonnet 5.5 | $2 | $10 |
| Claude Opus 5.5 | $4 | $20 |

La entrada que se lee desde la caché de prompts cuesta aproximadamente una décima parte del precio normal de entrada. No hay límites de plan, solo los límites de velocidad (rate limits) de tu cuenta, pero se cobra cada token.

## Por qué Claude Code consume tantos tokens

Claude Code trabaja por pasos: lee archivos, edita, ejecuta las pruebas, lee el resultado y vuelve a intentarlo. En cada paso envía al modelo **todo su contexto de trabajo**: instrucciones, definiciones de herramientas, los archivos que ha leído y todo lo que ocurrió antes. Una sola tarea del tamaño de una funcionalidad puede enviar fácilmente **1,6 millones de tokens de entrada**, aunque el código que escriba sea corto.

El **caché de prompts** (prompt caching) es lo que lo mantiene asequible: la parte repetida del contexto se cobra a cerca del 10 % del precio normal de entrada. Claude Code lo usa automáticamente.

## Cuánto cuesta una tarea con la API

![Cuánto cuesta una tarea con la API: Tarea, Pasos, Haiku 4.5, Sonnet 5.5, Opus 5.5](/claude-code-precio-cuanto-cuesta-una-tarea-con-la-api-es.jpg)

Con nuestro [modelo de costes para agentes de programación](/es/agents), con la caché activada:

| Tarea | Pasos | Haiku 4.5 | Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|---|
| Arreglo pequeño | ~8 | $0,08 | $0,15 | $0,31 |
| Nueva funcionalidad | ~25 | $0,36 | $0,72 | $1,43 |
| Refactorización grande | ~60 | $1,33 | $2,65 | $5,30 |

Sin caché, la misma tarea de nueva funcionalidad con Sonnet costaría unos $3,38 en lugar de $0,72.

## Cuánto cuesta Claude Code al mes

Suponiendo 22 días laborables:

| Cómo lo usas | Tareas al mes | API con Sonnet | API con Opus | Plan más barato que suele bastar |
|---|---|---|---|---|
| Ligero: 3 arreglos pequeños al día | 66 | ~$10 | ~$20 | API o Pro ($20) |
| Habitual: 5 funcionalidades al día | 110 | ~$79 | ~$158 | Pro o Max 5× |
| Intenso: 15 funcionalidades al día | 330 | ~$236 | ~$473 | Max 5× o Max 20× |
| Agentes todo el día: 8 tareas grandes al día | 176 | ~$466 | ~$932 | Max 20× |

El patrón es claro:

- **Uso ocasional:** la API puede salir más barata que cualquier plan. Pagas $10 en un mes en el que Pro costaría $20.
- **Uso diario:** una suscripción pronto sale mucho más barata. Un usuario habitual con Opus pagaría unos $158 en la API frente a $100 de Max 5×.
- **Uso intensivo:** Max es muchísimo más barato que la API, siempre que los límites de uso sean suficientes.

La trampa de los planes son los límites. Anthropic no publica cifras exactas de tokens para cada plan, y los usuarios intensivos llegan al tope semanal. Consulta [Límites de uso de Claude Code explicados](/es/blog/claude-code-limites-de-uso).

## Cómo convertir tokens a dólares

Una regla rápida para Claude Sonnet 5.5:

- 1 millón de tokens de entrada = $2 (o $0,20 si están en caché)
- 1 millón de tokens de salida = $10

Como la mayor parte de lo que envía Claude Code es contexto en caché, un precio combinado realista para trabajo con agentes en Sonnet suele quedar muy por debajo de $1 por millón de tokens procesados en total. Para Opus, multiplícalo por dos.

## Cómo decidir

![Cómo decidir: Empieza con Pro si programas con él unas cuantas veces por semana.; Fíjate en cuántas veces llegas al límite. ](/claude-code-precio-como-decidir-es.jpg)

1. **Empieza con Pro** si programas con él unas cuantas veces por semana.
2. **Fíjate en cuántas veces llegas al límite.** Si lo alcanzas casi todas las semanas, probablemente Max 5× te salga más barato que pagar la tarifa de la API por el trabajo extra.
3. **Usa la API** para automatización, pipelines de CI o un uso muy irregular, donde la facturación predecible por token es mejor que una cuota mensual.
4. **Elige el modelo según la tarea.** Sonnet se encarga de la mayoría del trabajo de programación; Opus cuesta el doble por token.

## Calcula tu propio mes

La [calculadora de costes de agentes de programación](/es/agents) te permite ajustar el tamaño de las tareas, las tareas por día y los días laborables, y compara los costes de API de los modelos de Claude, GPT y Gemini con todos los planes de Claude y ChatGPT. Para gastar menos tokens en cualquier caso, consulta [How to save tokens in Claude Code](/blog/claude-code-save-tokens) (en inglés).

*Los precios y los límites cambian a menudo. Revisa [claude.com/pricing](https://claude.com/pricing) antes de decidir.*
<!-- autoimg -->
