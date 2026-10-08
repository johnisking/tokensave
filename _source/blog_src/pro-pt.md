Em 29 de setembro de 2026, a OpenAI dividiu o ChatGPT Pro em três planos: **Pro 100**, **Pro 200** e o novo **Pro 500**. De quebra, reduziu sem alarde o quanto você pode usar no Pro 200. Se você está em dúvida entre eles, ou se perguntando se o Pro vale a pena para você, veja o que realmente mudou e como escolher.

![Planos do ChatGPT comparados por uso e preço](/blog-chatgpt-pro-tiers.png)

## Os planos lado a lado

![Os planos lado a lado: Plano, Preço / mês, Uso vs Plus, Preço por "um Plus" de uso, Ultrafast](/chatgpt-pro-100-200-500-precos-os-planos-lado-a-lado-pt.jpg)

| Plano | Preço / mês | Uso vs Plus | Preço por "um Plus" de uso | Ultrafast |
|---|---:|---:|---:|:---:|
| Go | $8 | menor | – | – |
| Plus | $20 | 1× | $20 | – |
| Pro 100 | $100 | 5× | $20 | – |
| Pro 200 | $200 | 10× | $20 | – |
| Pro 500 | $500 | 25× | $20 | ✓ |

Preços dos EUA, em dólares (US$). A página de ajuda da OpenAI diz apenas que o Pro 200 inclui mais uso que o Pro 100 e que o Pro 500 inclui o máximo; os multiplicadores 5×, 10× e 25× Plus não vêm da página de preços da OpenAI, e sim de uma publicação de Thibault Sottiaux (OpenAI) no X (5× e 10×, segundo o WinBuzzer) e de reportagens (25×, Windows Report).

Os três planos Pro têm os mesmos recursos: modelos Pro, Codex, deep research, criação de imagens, memória e envio de arquivos. A única diferença de recurso é o **Ultrafast**, um modo mais rápido do GPT-6 Astra, exclusivo do Pro 500. Comprar créditos extras no Pro 100 ou no Pro 200 não libera esse modo.

## O detalhe que quase todo mundo deixa passar: não existe mais desconto por volume

Divida o preço de cada plano pelo uso que ele oferece e todos chegam ao mesmo número: **$20 por "um Plus" de uso**. O Pro 500 não é mais vantajoso que o Pro 100; é só mais do mesmo, com velocidade extra.

Antes não era assim. Até essa mudança, o Pro 200 dava **20×** o uso do Plus, o que saía a $10 por unidade — metade do preço de qualquer outro plano. Quem assina o Pro 200 agora leva **10×**. Se você teve uma assinatura ativa do Pro 200 em algum momento entre 22 e 29 de setembro de 2026, mantém o limite antigo de 20× até **29 de outubro de 2026** e depois cai para 10×, pagando os mesmos $200.

A regra, então, é simples: **assine o menor plano cujo limite você não atinge.** Pagar por uma folga que você nunca usa é o único jeito de pagar caro demais.

## Qual plano escolher?

![Qual plano escolher?: Você quase nunca bate o limite do Plus; Você bate o limite do Plus algumas vezes por semana; Você vive esgotan](/chatgpt-pro-100-200-500-precos-qual-plano-escolher-pt.jpg)

- **Você quase nunca bate o limite do Plus:** fique no Plus ($20). Nenhum plano Pro dá respostas mais inteligentes no chat do dia a dia; eles só dão mais respostas.
- **Você bate o limite do Plus algumas vezes por semana:** Pro 100. Cinco vezes o uso por cinco vezes o preço, e ir de $20 para $100 é o menor salto possível.
- **Você vive esgotando o Pro 100:** Pro 200. Mesmo preço por unidade, o dobro de espaço.
- **Você usa o Codex ou agentes quase o dia todo, ou esperar pela resposta te custa dinheiro:** Pro 500. É o único plano com Ultrafast, mas lembre que gerar mais rápido também consome seu limite mais rápido.
- **Você está no Pro 200 antigo:** mantenha até 29 de outubro; é o melhor negócio que a OpenAI vende hoje. Depois disso, veja quanto você realmente usou. Se ficou abaixo de mais ou menos um quarto do limite antigo, o Pro 100 dá conta do recado por $100 a menos.

## E se eu usar a API direto?

![E se eu usar a API direto?: Seu uso, API do GPT-6 Sol, API do GPT-6 Astra](/chatgpt-pro-100-200-500-precos-e-se-eu-usar-a-api-direto-pt.jpg)

Se você manda principalmente mensagens curtas ou médias, pagar por token costuma sair bem mais barato que qualquer plano Pro. Veja quanto custa, aproximadamente, um mês de chat pela API, considerando conversas de 6 mensagens e texto em inglês:

| Seu uso | API do GPT-6 Sol | API do GPT-6 Astra |
|---|---:|---:|
| 30 mensagens normais por dia | ≈ $8 | ≈ $39 |
| 80 mensagens normais por dia | ≈ $21 | ≈ $103 |
| 80 mensagens longas por dia (colando documentos) | ≈ $59 | ≈ $294 |
| 200 mensagens longas por dia | ≈ $147 | ≈ $735 |

"Normal" = cerca de 150 tokens de entrada e 500 de saída por mensagem; "longa" = cerca de 2.000 de entrada e 700 de saída. Preços da API: Sol $2 / $10 e Astra $10 / $50 por milhão de tokens de entrada / saída.

Duas coisas fazem esses valores subirem rápido. Primeiro, cada nova mensagem reenvia a conversa inteira, então chats longos custam muito mais que os curtos. Segundo, idiomas diferentes do inglês precisam de mais tokens para o mesmo texto: o português, cerca de 20% a mais; o coreano, cerca de 40% a mais; e o japonês, cerca de 80% a mais — e a conta da API cresce na mesma proporção.

Resumindo: quem usa o modelo do dia a dia de forma leve ou moderada geralmente se dá melhor com o Plus ou com a API. O Pro começa a valer a pena quando você usa pesado os modelos mais avançados, trabalha com documentos longos ou vive dentro do Codex.

## Faça as suas contas

O uso de cada pessoa é diferente. A [calculadora Assinatura vs API](/pt/plans) permite informar quantas mensagens você envia, o tamanho delas e o idioma em que escreve, e mostra quanto o mesmo mês custaria pela API ao lado dos planos do ChatGPT, Claude e Gemini. Se algo mais barato que o Pro já resolve, veja [ChatGPT Go vs Plus](/pt/blog/chatgpt-go-vs-plus).

*Preços de 1 de outubro de 2026. A OpenAI pode mudar os limites de novo; confira chatgpt.com/pricing antes de assinar.*

## Fontes

- [Ajuda da OpenAI: níveis do ChatGPT Pro](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
- [Planos do ChatGPT e preços do Codex](https://learn.chatgpt.com/docs/pricing)
- [Ajuda da OpenAI: notas de versão do ChatGPT](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [Preços da API da OpenAI](https://developers.openai.com/api/docs/pricing)
<!-- autoimg -->
