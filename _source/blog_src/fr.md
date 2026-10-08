![Le français consomme 29 % de tokens de plus que l’anglais dans GPT](/tokens-francais-gpt-fr.jpg)

J’ai traduit le même prompt de service client dans 41 langues et compté les tokens avec o200k_base, le tokeniseur actuel d’OpenAI (GPT-4o et suivants). L’anglais demande 34 tokens ; le français **44, soit 29% de plus que l’anglais**, rang 9 sur 41 (1 = le moins cher).

La version française :

> Résumez l'e-mail du client ci-dessous en trois points et proposez une réponse polie. Le client indique que la commande est arrivée avec deux jours de retard et qu'un article manquait dans le colis.

## Résultats

| Langue | Tokens | Par rapport à l’anglais | Économie si envoyé en anglais |
|---|---:|---:|---:|
| English | 34 | ±0% | – |
| 简体中文 | 35 | +3% | 3% |
| Español | 40 | +18% | 15% |
| Deutsch | 43 | +26% | 21% |
| **Français** | **44** | **+29%** | **22%** |
| 한국어 | 49 | +44% | 31% |
| हिन्दी | 51 | +50% | 33% |
| 日本語 | 61 | +79% | 44% |
| Čeština | 68 | +100% | 50% |
| Ελληνικά | 70 | +106% | 51% |
| ਪੰਜਾਬੀ | 83 | +144% | 59% |

![Graphique : tokens supplémentaires par langue par rapport à l’anglais dans GPT](/blog-language-tax-chart-v5.png)

## Pourquoi

![Pourquoi: Résumez → Rés | ume | z · 3; ci-dessous → ci | -dessous · 2; proposez → propose | z · 2](/tokens-francais-gpt-pourquoi-fr.jpg)

Le tokeniseur apprend surtout sur du texte anglais : des mots comme « polite » ou « customer » tiennent en un seul token, alors que beaucoup de mots français sont découpés en morceaux :

- Résumez → `Rés | ume | z` · 3
- ci-dessous → `ci | -dessous` · 2
- proposez → `propose | z` · 2

## Passer à l'anglais en un clic

La plus grosse économie consiste à envoyer votre prompt en anglais : environ 22 % de tokens en moins qu'en français. Les modèles actuels comprennent parfaitement les instructions en anglais et répondent en français si vous le demandez. Dans le compteur de tokens TokenSave, collez votre prompt et appuyez sur **💸 Économiser des tokens** : il nettoie les espaces, traduit en anglais, supprime le superflu et ajoute « Reply in French. » pour que la réponse reste dans votre langue. Il utilise le traducteur intégré à Chrome 138+ / Edge 148+ sur ordinateur ; la traduction s'effectue sur votre propre appareil et votre texte n'est jamais envoyé en ligne. Appuyez sur **↩ Original** pour retrouver l'original.

## En argent

Avec un modèle à 2 $ le million de tokens d’entrée, envoyer ce prompt un million de fois coûte 68 $ en anglais et 88 $ en français. Si la réponse est aussi en français, le même écart s’applique aux tokens de sortie, généralement 300 à 400% plus chers.

## Comment économiser

![Comment économiser: Rédigez le prompt système et les consignes fixes en anglais ; gardez en français seulement ce que saisit l’uti](/tokens-francais-gpt-comment-economiser-fr.jpg)

- Rédigez le prompt système et les consignes fixes en anglais ; gardez en français seulement ce que saisit l’utilisateur.
- Demandez les étapes intermédiaires (classification, extraction, appels d’outils) en anglais ou en JSON, et seule la réponse finale en français.
- Utilisez le prompt caching pour la partie fixe du prompt.

## Limites

- Un seul prompt mesuré ; selon le texte, le ratio peut varier de ±0,1–0,2.
- Claude et Gemini utilisent d’autres tokeniseurs : ces chiffres ne valent que pour les modèles OpenAI.
- La traduction repose sur une traduction automatique relue.

Essayez avec votre propre texte dans le [compteur de tokens](/fr/) ; toutes les langues sont comparées dans le [tableau des langues](/languages).

Résultats complets des 41 langues (en anglais) : [comparaison de 41 langues](/blog/token-cost-by-language)

## Sources

- [tiktoken : le tokeniseur d’OpenAI (o200k_base) sur GitHub](https://github.com/openai/tiktoken)
- [Tarifs de l’API OpenAI](https://developers.openai.com/api/docs/pricing)

<!-- autoimg -->
