Google change les modèles disponibles dans l'application Gemini selon l'abonnement. **À partir du 9 octobre 2026, la version gratuite ne donne plus accès qu'à Flash-Lite**, le plus petit modèle, et l'abonnement Google AI Plus à 4,99 € par mois va bientôt perdre le modèle Pro. Jusqu'ici, on pouvait utiliser Pro et Deep Research assez largement sans payer : le changement se sentira. Voici ce qui change, le prix de chaque formule en euros, et comment continuer à utiliser un modèle de niveau Pro pour quelques euros, calculé avec le nombre de tokens réel du français.

## Quels modèles pour quelle formule

| Formule | Prix mensuel | Flash-Lite | Flash | Pro | Deep Think |
|---|---:|:---:|:---:|:---:|:---:|
| Gratuit | 0 € | ✓ | ✗ | ✗ | ✗ |
| AI Plus | 4,99 € | ✓ | ✓ | **✗ (retiré)** | ✗ |
| AI Pro | 21,99 € | ✓ | ✓ | ✓ | ✓ |
| AI Ultra | 99,99 € | ✓ | ✓ | ✓ | ✓ |
| AI Ultra (palier supérieur) | 219,99 € | ✓ | ✓ | ✓ | ✓ |

Prix en France relevés dans la presse française au 6 octobre 2026. Le changement concerne les comptes Google personnels ; les comptes Google Workspace (travail, école) ne sont pas touchés.

## À partir de quand ?

- **Gratuit :** Flash-Lite uniquement dès le 9 octobre.
- **AI Plus :** pas de date unique. Google prévient chaque abonné par e-mail de la date à laquelle Pro disparaît de son compte.
- **AI Pro et Ultra :** Flash-Lite, Flash et Pro restent disponibles, avec en plus le mode de raisonnement Deep Think.

Pour chaque modèle, on peut choisir un niveau de réflexion faible, moyen ou élevé. Plus il est élevé, plus vite on atteint la limite. Celle-ci ne se compte pas en nombre de messages mais en puissance de calcul consommée, et elle se recharge toutes les 5 heures. Le modèle Pro, Deep Research et la génération d'images ou de vidéos consomment davantage qu'une question simple.

## Pourquoi ce changement

Google a lancé le 30 septembre son modèle le plus avancé, Gemini 4 Argon. Les modèles puissants coûtent cher à faire tourner, et Google les réserve désormais aux formules payantes, avec l'objectif évident de pousser vers AI Pro et Ultra.

## Que faire selon votre usage

- **Recherches rapides, traductions, résumés :** la version gratuite (Flash-Lite) suffit souvent. Essayez-la quelques jours avant de décider de payer.
- **Vous aviez pris AI Plus pour le modèle Pro :** après la date indiquée dans votre e-mail, 4,99 € ne suffiront plus. Si Pro vous est indispensable, il faudra passer à AI Pro (21,99 €).
- **Étudiants :** Google offre AI Plus pendant 12 mois aux étudiants dans 140 pays hors États-Unis, pour toute inscription avant le 31 décembre 2026. Attention : l'offre mettait en avant l'accès à Gemini 3.1 Pro, qui disparaît justement d'AI Plus. Il reste Flash, 400 Go de stockage et la génération d'images.
- **21,99 € par mois vous semble cher ?** Comparez avec ChatGPT Plus (23 €) ou Vibe Pro de Mistral (17,99 €). Sur ChatGPT, même la version gratuite permet de discuter sans limite avec GPT-5.6 Luna, mais elle affiche des publicités. Tous les prix sont dans notre [comparatif des abonnements IA en euros](/fr/blog/abonnement-ia-prix-comparatif), et l'offre d'entrée de gamme d'OpenAI est détaillée dans [ChatGPT Go ou Plus](/fr/blog/chatgpt-go-vs-plus).

## Un modèle de niveau Pro pour quelques euros : l'API

Les modèles Gemini sont aussi accessibles via Google AI Studio et l'API, où l'on paie uniquement ce que l'on consomme. Le français demande environ 29 % de tokens en plus que l'anglais pour le même contenu ([le détail ici](/fr/blog/tokens-francais-gpt)), donc le calcul est fait sur des tokens français : environ 1 080 tokens en entrée et 500 en sortie par question, **20 questions par jour pendant 30 jours** (600 requêtes).

| Modèle | Coût API mensuel |
|---|---:|
| Gemini 3.5 Flash-Lite | environ 0,84 € |
| Gemini 3.8 Flash | environ 1,43 € |
| Gemini 3.1 Pro | environ 4,33 € |

Conversion à 1 $ = 0,885 €. Dans une longue conversation, tout l'historique est renvoyé à chaque message, donc le coût augmente avec la longueur de l'échange.

**Même avec le modèle Pro, 20 questions par jour coûtent bien moins cher que les 21,99 € d'AI Pro.** En revanche, vous perdez les fonctions de l'application : génération d'images, Deep Research, intégration à Gmail et Docs. Il faut aussi une application de chat compatible avec une clé API. Pour savoir ce qui revient le moins cher avec votre propre usage, entrez-le dans le [calculateur abonnement ou API](/fr/plans), ou comptez les tokens d'un de vos prompts avec le [compteur de tokens](/fr/).

*Sources : [Journal du Geek](https://www.journaldugeek.com/2026/10/05/mauvaise-nouvelle-si-vous-utilisez-la-version-gratuite-de-gemini/), [Décodeur IA](https://www.decodeur-ia.com/articles/gemini-gratuit-flash-lite-9-octobre-2026-ai-plus-sans-pro-pme), [BriefIA](https://www.briefia.fr/article/google-limite-gemini-gratuit-au-modele-flash-lite-le-9-octobre), [Clubic (offre étudiante)](https://www.clubic.com/actualite-626083-gemini-app-devoile-une-nouveaute-surprise-qui-intrigue-deja-les-utilisateurs.html). Vérifié le 6 octobre 2026. Les dates et les limites peuvent changer : consultez la page officielle de Google avant de souscrire.*
