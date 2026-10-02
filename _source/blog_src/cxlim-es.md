Codex, el agente de programación de OpenAI, viene incluido en los planes Plus, Pro y Business de ChatGPT, y es justo ahí donde la mayoría de la gente choca hoy con los límites de uso. Los límites de uso de Codex se comparten con ChatGPT Work, funcionan con una ventana de 5 horas y un tope semanal, y se agotan a velocidades muy distintas según el modelo. Aquí te explicamos cómo funcionan y cómo usar Codex de ChatGPT sacándole más partido.

## Qué planes incluyen Codex

El uso de Codex (y de ChatGPT Work) está incluido en **Plus** ($20), **Pro** ($100, $200 o $500) y en las licencias **Business** Standard y Premium. El uso no es ilimitado: cada plan tiene una cuota, que se mide en dos ventanas.

## Dos límites a la vez

**La ventana de 5 horas.** Una cuota móvil que empieza a contar con tu primera solicitud. Si la agotas, tienes que esperar a que la ventana se reinicie. OpenAI restableció la ventana de 5 horas para Plus a finales de agosto de 2026; en ese momento indicó que Pro 100 y Pro 200 no la tendrían durante los próximos meses.

**El límite semanal.** Un tope móvil de siete días que se suma al anterior. Si lo alcanzas, tienes que esperar al reinicio semanal, aunque tu ventana de 5 horas esté recién renovada.

Codex y ChatGPT Work consumen de la **misma cuota**.

## Cuánto uso tienes según el modelo

El centro de ayuda de OpenAI da una estimación de mensajes por ventana de 5 horas. El modelo que eliges cambia la cifra enormemente:

| Modelo | Plus | Pro (nivel 5×) |
|---|---|---|
| GPT-6 Astra | aprox. 5–45 | aprox. 25–225 |
| GPT-5.6 Sol | aprox. 10–100 | aprox. 50–500 |
| GPT-5.6 Terra | aprox. 25–200 | aprox. 125–1,000 |
| GPT-5.6 Luna | aprox. 250–2,000 | aprox. 1,250–10,000 |

El extremo bajo de cada rango corresponde a tareas largas, de varios pasos, sobre un código grande; el extremo alto, a solicitudes cortas y sencillas. Los niveles Pro superiores escalan: Pro 200 equivale a 10× Plus para nuevos suscriptores desde el 29 de septiembre de 2026, y Pro 500 a 25×.

**Ultrafast**, disponible solo en Pro 500, es un modo más rápido que consume tu uso incluido y tus créditos con mayor rapidez.

## Por qué Codex gasta la cuota tan rápido

Como cualquier agente de programación, Codex trabaja por pasos y en cada paso vuelve a enviar al modelo todo su contexto de trabajo: instrucciones, definiciones de herramientas, archivos que ha leído y pasos anteriores. Una tarea típica de 25 pasos para implementar una funcionalidad envía alrededor de 1,6 millones de tokens de entrada. En la API, esa tarea costaría unos $0,72 con un modelo de la clase Sol y alrededor de $3,60 con GPT-6 Astra, y por eso la cuota de Astra es mucho menor. Consulta [¿Cuánto cuesta por tarea un agente de programación con IA?](/blog/ai-coding-agent-cost) (en inglés)

## Cómo consultar tu uso

El centro de ayuda de OpenAI remite a **Settings → Usage** en ChatGPT, donde ves tu cuota restante y las horas de reinicio. Codex también te avisa cuando te acercas al límite.

## Cuando llegas al límite

1. **Espera al reinicio.** La ventana de 5 horas se recarga en cuestión de horas.
2. **Usa un reinicio acumulado o compra un reinicio instantáneo**, disponible en cuentas Plus y Pro que cumplan los requisitos.
3. **Usa créditos** para seguir trabajando en los planes que los admiten.
4. **Sube** a un nivel Pro superior.
5. **Usa una clave de API** con facturación por uso para el trabajo que exceda tu cuota.

## Cómo estirar tu cuota

- **Usa por defecto GPT-5.6 Sol o Terra.** Reserva GPT-6 Astra para los problemas difíciles en los que notes la diferencia: consume varias veces más cuota.
- **Usa Luna para ediciones simples**, renombrados y código repetitivo.
- **Mantén las tareas pequeñas y concretas.** Menos pasos significa menos contexto reenviado.
- **Empieza de cero entre tareas no relacionadas** para no arrastrar el historial antiguo.
- **Indica a Codex los archivos correctos** en lugar de dejar que busque en todo el repositorio.
- **Mantén breve tu archivo de instrucciones** y escríbelo en inglés si normalmente usas otro idioma: con el tokenizador de GPT, el coreano ocupa unas 1,44× y el japonés 1,79× los tokens del inglés.

Muchos de estos hábitos también sirven para Claude Code: consulta [Cómo ahorrar tokens en Claude Code](/blog/claude-code-save-tokens) (en inglés).

## Codex vs Claude Code: ¿cuál elegir?

Ambos están incluidos en planes de $20, $100 y $200 con sistemas de límites parecidos. La [comparativa ChatGPT Pro vs Claude Max](/blog/chatgpt-pro-vs-claude-max) (en inglés) explica las diferencias, y la [calculadora de agentes de programación](/es/agents) compara los costos mensuales de la API con cada plan.

*Los límites cambian a menudo. La [página de ayuda de OpenAI sobre el uso de Codex y Work](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex) tiene las cifras actualizadas.*
