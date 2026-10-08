![O português gasta 1,21× mais tokens que o inglês no GPT](/tokens-portugues-gpt-pt.jpg)

Traduzi o mesmo prompt de atendimento ao cliente para 41 idiomas e contei os tokens com o o200k_base, o tokenizador atual da OpenAI (GPT-4o e posteriores). Em inglês são 34 tokens; em português, **41: 1,21× o inglês**, posição 5 de 41 (1 = o mais barato).

A versão em português:

> Resuma o e-mail do cliente abaixo em três tópicos e sugira uma resposta educada. O cliente diz que o pedido chegou com dois dias de atraso e que faltava um item na caixa.

## Resultados

| Idioma | Tokens | Em relação ao inglês | Economia se enviado em inglês |
|---|---:|---:|---:|
| English | 34 | 1,00× | – |
| 简体中文 | 35 | 1,03× | 3% |
| Español | 40 | 1,18× | 15% |
| **Português** | **41** | **1,21×** | **17%** |
| Deutsch | 43 | 1,26× | 21% |
| 한국어 | 49 | 1,44× | 31% |
| हिन्दी | 51 | 1,50× | 33% |
| 日本語 | 61 | 1,79× | 44% |
| Čeština | 68 | 2,00× | 50% |
| Ελληνικά | 70 | 2,06× | 51% |
| ਪੰਜਾਬੀ | 83 | 2,44× | 59% |

![Resultados](/blog-language-tax-chart-v4.png)

## Por quê

![Por quê: tópicos → tóp | icos · 2; educada → educ | ada · 2; faltava → falt | ava · 2](/tokens-portugues-gpt-por-que-pt.jpg)

O tokenizador aprende principalmente com texto em inglês: palavras como " polite" ou " customer" são um único token, enquanto muitas palavras em português são quebradas em pedaços:

- tópicos → `tóp | icos` · 2
- educada → `educ | ada` · 2
- faltava → `falt | ava` · 2

## Mude para o inglês com um botão

A maior economia é enviar seu prompt em inglês: cerca de 17% menos tokens do que em português. Os modelos atuais entendem perfeitamente instruções em inglês e respondem em português se você pedir. No contador de tokens do TokenSave, cole seu prompt e pressione **💸 Economizar tokens**: ele limpa os espaços, traduz para o inglês, corta o excesso e adiciona "Reply in Portuguese." para que a resposta continue no seu idioma. Ele usa o tradutor integrado ao Chrome 138+ / Edge 148+ para desktop; a tradução acontece no seu próprio dispositivo e seu texto nunca é enviado. Pressione **↩ Original** para recuperar o original.

## Em dinheiro

Com um modelo a US$ 2 por milhão de tokens de entrada, enviar este prompt um milhão de vezes custa US$ 68 em inglês e US$ 82 em português. Se a resposta também vier em português, o mesmo multiplicador vale para os tokens de saída, que costumam custar 4–5× mais.

## Como economizar

![Como economizar: Escreva o prompt de sistema e as instruções fixas em inglês; deixe em português só o que o usuário digita.; Pe](/tokens-portugues-gpt-como-economizar-pt.jpg)

- Escreva o prompt de sistema e as instruções fixas em inglês; deixe em português só o que o usuário digita.
- Peça as etapas intermediárias (classificação, extração, chamadas de ferramentas) em inglês ou JSON e só a resposta final em português.
- Use prompt caching para a parte fixa do prompt.

## Limitações

- É um único prompt; com outros textos a proporção pode variar ±0,1–0,2.
- Claude e Gemini usam outros tokenizadores: estes números valem só para modelos da OpenAI.
- A tradução parte de uma tradução automática revisada.

Resultados completos dos 41 idiomas (em inglês): [comparação de 41 idiomas](/blog/token-cost-by-language)
<!-- autoimg -->
