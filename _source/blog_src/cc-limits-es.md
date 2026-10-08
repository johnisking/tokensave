![Límites de uso de Claude Code: el límite de 5 horas y el semanal](/claude-code-limites-de-uso-es.jpg)

"Claude usage limit reached" es uno de los mensajes que más ven los usuarios de Claude Code, y también uno de los más confusos, porque los límites de uso de Claude Code son dos y funcionan al mismo tiempo: el límite de 5 horas y el límite semanal. Aquí te explicamos cómo funcionan, qué cambió en 2026 y qué puedes hacer cuando llegas a uno de ellos.

## Los dos límites de uso de Claude Code

**1. El límite de 5 horas (por sesión).** Tu uso se mide en una ventana móvil de cinco horas que empieza con tu primer mensaje. Cuando agotas lo disponible para esa ventana, tienes que esperar a que se reinicie.

**2. El límite semanal.** Además del límite por sesión, hay un tope para el uso total a lo largo de una semana. Se introdujo en agosto de 2025 para evitar que una pequeña parte de las cuentas tuviera Claude Code funcionando día y noche. Si llegas a él, tienes que esperar al reinicio semanal aunque tu ventana de 5 horas esté recién empezada.

Ambos límites se **comparten entre Claude Code y la app de Claude** (web, escritorio y móvil). Una conversación larga en la app consume la misma cuota que tu sesión de programación.

## Cuánto incluye cada plan

![Cuánto incluye cada plan: Plan, Precio, Uso](/claude-code-limites-de-uso-cuanto-incluye-cada-plan-es.jpg)

Anthropic describe los límites de cada plan en relación con los demás, no en tokens exactos:

| Plan | Precio | Uso |
|---|---|---|
| Pro | $20 al mes | Nivel base |
| Max 5× | $100 al mes | 5× Pro |
| Max 20× | $200 al mes | 20× Pro |

Cuánto te rinde depende mucho de lo que hagas. Los archivos grandes, las sesiones largas y Opus agotan la cuota mucho más rápido que las tareas cortas con Sonnet, porque en cada paso se vuelve a enviar todo el contexto de trabajo.

## Qué cambió en 2026

![Qué cambió en 2026: 6 de mayo de 2026; Verano de 2026; 14 de septiembre de 2026](/claude-code-limites-de-uso-que-cambio-en-2026-es.jpg)

- **6 de mayo de 2026:** Anthropic **duplicó los límites de 5 horas de Claude Code** para los planes Pro, Max, Team y Enterprise por puestos, y eliminó la reducción adicional de límites en horas pico para Pro y Max.
- **Verano de 2026:** estuvo vigente un **aumento temporal del 50 %** en los límites semanales.
- **14 de septiembre de 2026:** Anthropic **subió de forma permanente un 25 % los límites semanales estándar** para Pro, Max, Team y Enterprise por puestos. Como esto sustituyó al aumento temporal del 50 %, los límites semanales quedaron alrededor de un 17 % por debajo de los del verano, aunque todavía un 25 % por encima del nivel original.

Así que, si sientes que desde mediados de septiembre llegas antes al límite semanal, es lo esperable.

## Cómo ver cuánto te queda

Dentro de Claude Code, el comando **/status** muestra la cuota que te queda. Claude Code también te avisa cuando te acercas a un límite. Revísalo antes de empezar una tarea larga, no a mitad de ella.

## Qué hacer cuando llegas a un límite

![Qué hacer cuando llegas a un límite: Espera al reinicio. En el límite de 5 horas, normalmente es cuestión de horas.; Activa el uso adicional. Los p](/claude-code-limites-de-uso-que-hacer-cuando-llegas-a-un-limite-es.jpg)

1. **Espera al reinicio.** En el límite de 5 horas, normalmente es cuestión de horas.
2. **Activa el uso adicional.** Los planes de pago pueden seguir con créditos de uso que se facturan aparte, en lugar de detenerse.
3. **Cambia a créditos de la API.** Claude Code puede funcionar con facturación de la API de pago por uso; te pide tu consentimiento antes de hacerlo.
4. **Mejora tu plan.** De Pro a Max 5×, o de Max 5× a Max 20×.
5. **Usa menos tokens por tarea.** A menudo es la solución más barata. Lo vemos más abajo.

## Por qué llegas a los límites antes de lo esperado

- **Sesiones largas.** En cada paso se vuelve a enviar todo lo que pasó antes. Una sesión de dos horas arrastra un contexto enorme a cada nuevo paso.
- **Opus.** Consume la cuota más rápido que Sonnet.
- **Archivos y logs grandes.** Leer un archivo de 3.000 líneas o un log de pruebas completo añade decenas de miles de tokens.
- **Tareas vagas.** "Limpia el proyecto" puede llevar decenas de pasos; "arregla el test que falla en auth.py" lleva unos pocos.
- **Usar la app de Claude al mismo tiempo.** Ambas tiran de la misma cuota.

## Cómo estirar tus límites

- Empieza una sesión nueva (**/clear**) entre tareas que no tienen relación, y usa **/compact** para resumir una sesión larga.
- Indícale a Claude los archivos correctos en lugar de dejar que los busque.
- Mantén breves las instrucciones de tu CLAUDE.md: se envían en cada paso.
- Usa Sonnet para el trabajo rutinario y reserva Opus para los problemas difíciles.

Más detalles y cifras en [How to save tokens in Claude Code](/blog/claude-code-save-tokens) (en inglés).

## ¿Plan o API?

Si llegas con frecuencia al límite semanal, compara lo que te costaría ese uso adicional en la API con el siguiente plan. Nuestra guía [Precio de Claude Code al mes](/es/blog/claude-code-precio) y nuestra [calculadora de agentes de programación](/es/agents) hacen las cuentas por ti.

*Los límites cambian. La [página de ayuda sobre los planes de Claude Code](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan) y la [página de precios](https://claude.com/pricing) de Anthropic tienen las reglas actuales.*

## Fuentes

- [Usar Claude Code con tu plan Pro o Max (Centro de ayuda de Claude)](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [Planes y precios de Claude (Anthropic)](https://claude.com/pricing)
- [Uso adicional en los planes de pago de Claude (Centro de ayuda de Claude)](https://support.claude.com/en/articles/12429409-extra-usage-for-max-20x-plans)
- [Gestionar los costes de forma eficaz (documentación de Claude Code)](https://code.claude.com/docs/en/costs)
<!-- autoimg -->
