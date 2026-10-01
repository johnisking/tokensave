Écrire à une IA en français coûte plus cher qu'en anglais : le même texte est découpé en plus de *tokens*, et ce sont les tokens que l'on paie à l'API ou qui épuisent les limites d'un abonnement. Mais de combien, exactement ? Et Mistral, le modèle français, fait-il mieux que ChatGPT sur ce point ? J'ai mesuré.

![Le français coûte plus de tokens que l'anglais, chez OpenAI comme chez Mistral](/blog-mistral-francais.png)

## Le test

Deux textes, chacun en anglais et en français, avec exactement le même sens :

- **Un prompt court** (une demande de résumé d'e-mail client, 2 phrases).
- **Un prompt long** (des instructions pour vérifier une facture et rédiger un e-mail, environ 100 mots).

Je les ai passés dans deux tokeniseurs : **o200k_base**, celui de GPT-4o et des modèles OpenAI récents, et **Tekken**, le tokeniseur publié par Mistral (version de septembre 2024, utilisée par Mistral NeMo et les modèles suivants).

## Résultats

| Texte | Anglais | Français | Surcoût |
|---|---:|---:|---:|
| Prompt court, OpenAI (o200k) | 34 | 44 | **+29 %** |
| Prompt court, Mistral (Tekken) | 34 | 45 | **+32 %** |
| Prompt long, OpenAI (o200k) | 110 | 123 | **+12 %** |
| Prompt long, Mistral (Tekken) | 110 | 128 | **+16 %** |

Deux enseignements :

1. **Le français coûte entre 12 % et 30 % de tokens en plus** que l'anglais. Plus le texte est court et « technique », plus l'écart est grand.
2. **Mistral n'est pas plus économe en français que ChatGPT.** Sur ces deux textes, Tekken produit même un peu plus de tokens que o200k. Être une entreprise française ne change rien à la façon dont le tokeniseur découpe la langue.

Pour comparer : sur le même prompt court, l'allemand coûte 1,26× l'anglais chez OpenAI, l'italien 1,38×, le polonais 1,88×. Le français fait partie des langues les moins pénalisées, mais il reste pénalisé.

## Pourquoi le français coûte plus

Les tokeniseurs sont entraînés surtout sur de l'anglais. Les mots anglais courants deviennent un seul token, alors que beaucoup de mots français sont coupés en morceaux :

- « facturation » → `fact | uration` (2 tokens, chez OpenAI comme chez Mistral)
- « vérifie » → `vér | ifie` (2 tokens)
- « rédige » → `réd | ige` (2 tokens)
- « chaleureux » → 1 token chez OpenAI, mais `chale | ure | ux` (3 tokens) chez Mistral

En face, « invoice », « billing » ou « polite » font un seul token. Les élisions (« l'adresse », « n'utilise ») et les accents ajoutent encore quelques tokens.

## Ce que ça change concrètement

- **À l'API**, vous payez à peu près 12 à 30 % de plus pour le même contenu.
- **Dans un abonnement** (ChatGPT Plus, Claude Pro, Le Chat Pro), les limites d'utilisation sont calculées en tokens : elles s'épuisent plus vite quand on écrit en français.
- **Si la réponse est aussi en français**, le même surcoût s'applique aux tokens de sortie, qui coûtent en général 4 à 5 fois plus cher que ceux d'entrée.

## L'astuce : écrire en anglais, recevoir en français

Le plus simple est d'écrire le prompt en anglais et d'ajouter à la fin : **« Reply in French. »** Le modèle comprend aussi bien, la réponse arrive en français, et le prompt coûte moins cher.

Ça vaut surtout le coup pour :

- les **prompts système** et les instructions réutilisées des milliers de fois via l'API ;
- les **longs documents de contexte** collés dans la conversation ;
- les utilisateurs d'abonnement qui **atteignent souvent la limite**.

Pour une question courte posée une fois, le gain est négligeable : écrivez comme vous voulez.

## Et le prix des abonnements ?

Le Chat Pro de Mistral est affiché à 14,99 $ par mois, contre 20 $ pour ChatGPT Plus et Claude Pro et 19,99 $ pour Google AI Pro (prix américains, octobre 2026). Le tokeniseur ne rend pas Mistral plus avantageux en français, mais l'abonnement reste le moins cher des quatre.

Pour savoir si un abonnement ou l'API revient moins cher selon votre usage réel (nombre de messages, longueur, langue), utilisez le [comparateur Abonnement vs API](/fr/plans).

## Vérifiez avec vos propres textes

Chaque texte est différent. [TokenSave](/fr/) compte les tokens et le coût de votre prompt pour GPT, Claude et Gemini, puis le traduit en anglais en un clic, directement dans votre navigateur, en ajoutant « Reply in French ». Le code n'est pas touché, seuls les commentaires sont traduits. Gratuit, sans inscription, rien n'est envoyé.

Le classement complet des 41 langues est ici : [Combien de tokens coûte le français ?](/fr/blog/tokens-francais-gpt)

*Mesures effectuées en octobre 2026 avec o200k_base (OpenAI) et Tekken 2024-09 (Mistral). Les modèles Mistral les plus récents peuvent utiliser une version mise à jour de Tekken.*
