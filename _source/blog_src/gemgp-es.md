Google cambia qué modelos se pueden usar en la app de Gemini según el plan. **Desde el 9 de octubre, los usuarios gratuitos solo tendrán Flash-Lite**, el modelo más pequeño, y el plan Google AI Plus (4,99 € en España, 99 pesos en México) también se quedará sin el modelo Pro. Hasta ahora la versión gratuita daba bastante acceso a Pro y a Deep Research, así que el cambio se va a notar. Aquí tienes qué cambia, cuánto cuesta cada plan en euros y en pesos mexicanos, y cuánto costaría usar Gemini Pro por API, con los tokens calculados para el español.

## Qué modelos incluye cada plan

| Plan | España | México | Flash-Lite | Flash | Pro | Deep Think |
|---|---:|---:|:---:|:---:|:---:|:---:|
| Gratis | 0 € | 0 MXN | ✓ | ✗ | ✗ | ✗ |
| AI Plus | 4,99 € | 99 MXN | ✓ | ✓ | **✗ (se retira)** | ✗ |
| AI Pro | 21,99 € | 395 MXN | ✓ | ✓ | ✓ | ✓ |
| AI Ultra 5x | 99,99 € | 1.999 MXN | ✓ | ✓ | ✓ | ✓ |
| AI Ultra 20x | 219,99 € | 3.949 MXN | ✓ | ✓ | ✓ | ✓ |

Precios mensuales tomados de las páginas oficiales de Gemini para España y México, consultadas el 6 de octubre de 2026. Los cambios afectan a las cuentas personales de Google; las cuentas de trabajo y de centros educativos siguen otras reglas.

## Cuándo cambia

- **Gratis:** solo Flash-Lite a partir del 9 de octubre.
- **AI Plus:** no hay una fecha única. Google avisa a cada suscriptor por correo de cuándo se aplica en su cuenta.
- **AI Pro y Ultra:** siguen teniendo Flash-Lite, Flash y Pro, y además Deep Think.

En los modelos disponibles puedes elegir un nivel de razonamiento (bajo, medio o alto). Cuanto más alto, antes se agota el límite. Los límites ya no se cuentan en mensajes, sino en capacidad de cómputo, y se recuperan cada 5 horas. El modelo Pro, Deep Research y la generación de imágenes y vídeo gastan más límite que una pregunta sencilla.

## Por qué lo hace Google

El 30 de septiembre Google lanzó Gemini 4 Argon, su modelo más potente. Los modelos grandes cuestan mucho de ejecutar, y la lectura general es que Google quiere reservarlos para los planes de pago y empujar a más gente hacia AI Pro.
## Qué hacer según tu caso

- **Si usas Gemini para buscar, traducir o resumir:** Flash-Lite gratis suele bastar. Pruébalo unos días antes de decidir pagar.
- **Si pagabas AI Plus para tener Pro:** cuando el cambio llegue a tu cuenta, 4,99 € (o 99 pesos) ya no incluirán Pro. Si lo necesitas, tendrás que pasar a AI Pro (21,99 € o 395 pesos). AI Plus sigue teniendo sentido si lo que te interesa es el almacenamiento de 400 GB.
- **Estudiantes:** Google ofrece AI Plus gratis durante 12 meses para estudiantes que se apunten antes del 31 de diciembre de 2026. Ten en cuenta que ese plan también pierde Pro, y que al terminar el periodo gratuito se cobra automáticamente si no lo cancelas.
- **Si 21,99 € al mes te parece mucho:** compáralo con ChatGPT Plus y Claude Pro, que están en el mismo rango. En ChatGPT, incluso el plan gratuito tiene chat de texto ilimitado con GPT-5.6 Luna desde agosto. Tienes todos los planes en euros y pesos en nuestra [comparativa de precios de suscripciones de IA](/es/blog/precio-suscripciones-ia), y la diferencia entre los planes baratos de ChatGPT en [ChatGPT Go vs Plus](/es/blog/chatgpt-go-vs-plus).

## Usar Pro sin suscripción: la API

Los modelos de Gemini también se pueden usar desde Google AI Studio o por API, pagando solo lo que consumes. El español genera alrededor de un 18% más de tokens que el inglés para el mismo texto ([lo medimos aquí](/es/blog/tokens-espanol-gpt)), así que hemos calculado con tokens en español: unos 990 tokens de entrada y 460 de salida por pregunta, **20 preguntas al día durante 30 días** (600 peticiones al mes).

| Modelo | Precio por 1M tokens (entrada / salida) | Coste al mes (USD) | Coste al mes (EUR) |
|---|---|---:|---:|
| Gemini 3.5 Flash-Lite | 0,30 $ / 2,50 $ | 0,87 $ | 0,77 € |
| Gemini 3.8 Flash | 0,75 $ / 3,75 $ | 1,48 $ | 1,31 € |
| Gemini 3.1 Pro | 2 $ / 12 $ | 4,50 $ | 3,98 € |

Cambio usado: 1 USD = 0,885 EUR. En conversaciones largas el coste sube, porque en cada mensaje se vuelve a enviar todo lo anterior.

**Incluso con el modelo Pro, 20 preguntas al día por API salen mucho más baratas que AI Pro (21,99 €).** A cambio, pierdes las funciones de la app (generación de imágenes, Deep Research, integración con Gmail y Docs) y necesitas una app de chat que acepte claves de API. Para ver con tus propios números qué te sale más barato, usa la [calculadora suscripción vs API](/es/plans). Si quieres contar los tokens de un texto concreto, prueba el [contador de tokens](/es/). Y si buscas alternativas sin pagar, revisa nuestras [páginas de IA gratis](/es/blog/paginas-de-ia-gratis).

*Fuentes: [Infobae](https://www.infobae.com/tecno/2026/10/05/google-limita-la-version-gratuita-de-gemini-a-flash-lite-35-y-ai-plus-a-flash-36/), [Digital Trends Español](https://es.digitaltrends.com/android/el-nivel-gratuito-de-gemini-va-a-sufrir-una-gran-degradacion-a-partir-del-9-de-octubre/), [Movilzona](https://www.movilzona.es/noticias/actualizaciones/cambios-gemini-limita-funciones-usuarios-gratis/), [Notebookcheck](https://www.notebookcheck.net/Google-Gemini-drops-Flash-and-Pro-for-free-users-on-October-9.1415964.0.html); precios de [Gemini España](https://gemini.google/es/subscriptions/?hl=es) y [Gemini México](https://gemini.google/mx/subscriptions/?hl=es-419). Consultado el 6 de octubre de 2026. Las fechas y los límites pueden cambiar; revisa la página oficial de Google antes de contratar.*
