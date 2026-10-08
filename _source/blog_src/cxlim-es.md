![Límites de uso de Codex en ChatGPT Plus, Pro y Business](/codex-limites-de-uso-es.jpg)

Codex, el agente de programación de OpenAI, viene incluido en los planes Plus, Pro y Business de ChatGPT, y es justo ahí donde la mayoría de la gente choca hoy con los límites de uso. Los límites de uso de Codex se comparten con ChatGPT Work, funcionan con una ventana de 5 horas en Plus y Business (también pueden aplicarse límites semanales), y se agotan a velocidades muy distintas según el modelo. Aquí te explicamos cómo funcionan y cómo usar Codex de ChatGPT sacándole más partido.

## Qué planes incluyen Codex

El uso de Codex (y de ChatGPT Work) está incluido en **Plus** ($20), **Pro** ($100, $200 o $500) y en las licencias **Business** Standard y Premium. El uso no es ilimitado: cada plan tiene una cuota incluida.

## Dos límites a la vez

**La ventana de 5 horas.** Una cuota móvil que empieza a contar con tu primera solicitud. Si la agotas, tienes que esperar a que la ventana se reinicie. Pro 100, Pro 200 y Pro 500 no tienen actualmente límite de cinco horas en Work y Codex; siguen teniendo una cuota incluida.

**El límite semanal.** OpenAI indica que también pueden aplicarse límites semanales. Si alcanzas uno, tienes que esperar a su reinicio, aunque tu ventana de 5 horas esté recién renovada.

Codex y ChatGPT Work consumen de la **misma cuota**.

## Cuánto uso tienes según el modelo

![Cuánto uso tienes según el modelo: Modelo, Plus, Business (Standard)](/codex-limites-de-uso-cuanto-uso-tienes-segun-el-modelo-es.jpg)

El centro de ayuda de OpenAI da una estimación de mensajes locales por ventana de 5 horas para Plus y Business Standard. El modelo que eliges cambia la cifra enormemente:

| Modelo | Plus | Business (Standard) |
|---|---|---|
| GPT-6 Astra | aprox. 5–45 | aprox. 5–45 |
| GPT-6.1 Sol | aprox. 15–160 | aprox. 15–160 |
| GPT-6 Sol | aprox. 15–150 | aprox. 15–150 |
| GPT-6 Luna | aprox. 350–3,000 | aprox. 350–3,000 |

El extremo bajo de cada rango corresponde a tareas largas, de varios pasos, sobre un código grande; el extremo alto, a solicitudes cortas y sencillas. Los planes Pro no tienen ahora ventana de 5 horas, pero sí una cuota incluida mayor: Pro 100 equivale a 5× Plus, Pro 200 a 10× Plus para nuevos suscriptores (quien tuvo una suscripción activa a Pro 200 entre el 22 y el 29 de septiembre de 2026 conserva el límite anterior hasta el 29 de octubre), y Pro 500 a 25× Plus. Estos multiplicadores no vienen de la página de precios de OpenAI, sino de una publicación en X de Thibault Sottiaux (OpenAI) y de informes de prensa (WinBuzzer, Windows Report).

**Ultrafast**, disponible solo en Pro 500, es un modo más rápido que consume tu uso incluido y tus créditos con mayor rapidez.

## Por qué Codex gasta la cuota tan rápido

Como cualquier agente de programación, Codex trabaja por pasos y en cada paso vuelve a enviar al modelo todo su contexto de trabajo: instrucciones, definiciones de herramientas, archivos que ha leído y pasos anteriores. Una tarea típica de 25 pasos para implementar una funcionalidad envía alrededor de 1,6 millones de tokens de entrada. En la API, esa tarea costaría unos $0,72 con un modelo de la clase Sol y alrededor de $3,60 con GPT-6 Astra, y por eso la cuota de Astra es mucho menor. Consulta [¿Cuánto cuesta por tarea un agente de programación con IA?](/blog/ai-coding-agent-cost) (en inglés)

## Cómo consultar tu uso

El centro de ayuda de OpenAI remite a **Settings → Usage** en ChatGPT, donde ves tu cuota restante y las horas de reinicio. Codex también te avisa cuando te acercas al límite.

## Cuando llegas al límite

![Cuando llegas al límite: Espera al reinicio. La ventana de 5 horas se recarga en cuestión de horas.; Usa un reinicio acumulado o compra](/codex-limites-de-uso-cuando-llegas-al-limite-es.jpg)

1. **Espera al reinicio.** La ventana de 5 horas se recarga en cuestión de horas.
2. **Usa un reinicio acumulado o compra un reinicio instantáneo**, disponible en cuentas Plus y Pro que cumplan los requisitos.
3. **Usa créditos** para seguir trabajando en los planes que los admiten.
4. **Sube** a un nivel Pro superior.
5. **Usa una clave de API** con facturación por uso para el trabajo que exceda tu cuota.

## Cómo estirar tu cuota

![Cómo estirar tu cuota: Usa por defecto GPT-6.1 Sol o GPT-6 Sol. Reserva GPT-6 Astra para los problemas difíciles en los que notes la dife](/codex-limites-de-uso-como-estirar-tu-cuota-es.jpg)

- **Usa por defecto GPT-6.1 Sol o GPT-6 Sol.** Reserva GPT-6 Astra para los problemas difíciles en los que notes la diferencia: consume mucha más cuota.
- **Usa Luna para ediciones simples**, renombrados y código repetitivo.
- **Mantén las tareas pequeñas y concretas.** Menos pasos significa menos contexto reenviado.
- **Empieza de cero entre tareas no relacionadas** para no arrastrar el historial antiguo.
- **Indica a Codex los archivos correctos** en lugar de dejar que busque en todo el repositorio.
- **Mantén breve tu archivo de instrucciones** y escríbelo en inglés si normalmente usas otro idioma: con el tokenizador de GPT, el coreano ocupa un 44 % más de tokens que el inglés y el japonés un 79 % más.

Muchos de estos hábitos también sirven para Claude Code: consulta [Cómo ahorrar tokens en Claude Code](/blog/claude-code-save-tokens) (en inglés).

## Codex vs Claude Code: ¿cuál elegir?

Ambos están incluidos en planes de $20, $100 y $200 con sistemas de límites parecidos. La [comparativa ChatGPT Pro vs Claude Max](/blog/chatgpt-pro-vs-claude-max) (en inglés) explica las diferencias, y la [calculadora de agentes de programación](/es/agents) compara los costos mensuales de la API con cada plan.

*Los límites cambian a menudo. La [página de ayuda de OpenAI sobre el uso de Codex y Work](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex) tiene las cifras actualizadas.*

## Fuentes

- [Ayuda de OpenAI: uso en Work y Codex](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)
- [Ayuda de OpenAI: reinicios guardados de Codex](https://help.openai.com/en/articles/20001498-how-banked-codex-resets-work)
- [Planes de ChatGPT y precios de Codex](https://learn.chatgpt.com/docs/pricing)
- [Ayuda de OpenAI: planes de ChatGPT Pro](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
<!-- autoimg -->
