Quand on utilise ChatGPT, Claude, Gemini ou Mistral, on ne paie ni au mot ni au message, mais au **token**. C'est l'unité qui sert à facturer l'API, à remplir la fenêtre de contexte et à épuiser les limites des abonnements. Le problème, c'est qu'on ne voit jamais ces tokens. Un compteur de tokens sert à les rendre visibles avant d'envoyer quoi que ce soit.

J'ai mesuré un vrai texte en français pour montrer à quel point les estimations « à vue de nez » peuvent tromper.

![Le même e-mail coûte 21 % de tokens en plus en français](/blog-compteur-tokens-fr.png)

## Un token, c'est quoi ?

![Un token, c'est quoi ?: « Résumez » → Rés | ume | z · 3 tokens; « ci-dessous » → ci | -dessous · 2 tokens; « summarize » → 1 token](/compteur-de-tokens-pourquoi-un-token-c-est-quoi-fr.jpg)

Un token est un morceau de texte : parfois un mot entier, parfois une partie de mot, une ponctuation ou un espace. Le découpage dépend du tokeniseur de chaque modèle. Par exemple, chez OpenAI :

- « Résumez » → `Rés | ume | z` · 3 tokens
- « ci-dessous » → `ci | -dessous` · 2 tokens
- « summarize » → 1 token

Les mots anglais courants tiennent souvent en un seul token. Beaucoup de mots français sont coupés en plusieurs morceaux.

## Le test : un e-mail de compte rendu

![Le test : un e-mail de compte rendu: Version, Mots, Caractères, GPT (o200k), Mistral (Tekken)](/compteur-de-tokens-pourquoi-le-test-un-e-mail-de-compte-rendu-fr.jpg)

J'ai écrit un e-mail de compte rendu de réunion (161 mots), puis sa traduction anglaise (146 mots), et je les ai passés dans deux tokeniseurs : **o200k_base** (GPT-4o et modèles OpenAI récents) et **Tekken** (Mistral).

| Version | Mots | Caractères | GPT (o200k) | Mistral (Tekken) |
|---|---:|---:|---:|---:|
| Anglais | 146 | 821 | 165 | 170 |
| Français | 161 | 997 | **199** | **206** |
| Écart | | | +21 % | +21 % |

## 5 raisons d'utiliser un compteur de tokens

![5 raisons d'utiliser un compteur de tokens: Poste, Tokens par mois, Coût par mois](/compteur-de-tokens-pourquoi-5-raisons-d-utiliser-un-compteur-de-toke-fr.jpg)

### 1. Les règles approximatives ne tiennent pas

On lit partout que « 1 token ≈ 4 caractères » ou que « 100 tokens ≈ 75 mots ». Sur cet e-mail français, on obtient plutôt **5 caractères par token** et **81 mots pour 100 tokens**. Et l'écart devient énorme dès qu'on colle autre chose que de la prose :

- un identifiant UUID coûte **18 tokens** à lui seul ;
- un tableau en JSON indenté coûte **190 % de tokens en plus** que le même tableau en CSV ([mesure complète ici](/blog/json-vs-yaml-vs-csv-tokens)).

Une règle unique ne peut pas couvrir tous ces cas. Compter, si.

### 2. Le français coûte plus cher que l'anglais

Sur cet e-mail, le français demande **21 % de tokens en plus**, chez OpenAI comme chez Mistral. Sur un prompt de service client court, l'écart monte à **29 %**. Concrètement, à contenu égal, un prompt en français coûte plus cher à l'API et épuise plus vite la limite d'un abonnement. Le compteur montre l'écart sur vos propres textes.

### 3. La réponse coûte souvent plus que la question

Les tokens de sortie (ce que le modèle écrit) sont en général **300 à 400 % plus chers** que les tokens d'entrée. Prenons un outil qui résume 1 000 e-mails comme celui-ci par jour, soit 30 000 par mois, avec un modèle à 2 $ le million de tokens d'entrée et 8 $ le million de tokens de sortie, et une réponse d'environ 250 tokens :

| Poste | Tokens par mois | Coût par mois |
|---|---:|---:|
| Entrée en français (199 tokens) | 5,97 M | 11,94 $ |
| Entrée en anglais (165 tokens) | 4,95 M | 9,90 $ |
| Sortie (250 tokens) | 7,5 M | **60,00 $** |

Passer le prompt en anglais fait gagner environ 2 $. Demander une réponse 50 % plus courte en fait gagner 30. Sans compteur, on optimise souvent le mauvais côté.

### 4. Les limites d'abonnement et la fenêtre de contexte

ChatGPT Plus, Claude Pro ou Mistral Vibe Pro (ex-Le Chat) ne facturent pas au token, mais leurs limites d'utilisation et la taille maximale d'une conversation sont, elles, calculées en tokens. Un long document collé dans la conversation peut à lui seul consommer une bonne partie de votre quota. Savoir combien de tokens il représente aide à choisir : le coller en entier, n'en garder qu'un extrait, ou le résumer d'abord.

### 5. Chaque modèle compte différemment

Le même texte ne fait pas le même nombre de tokens selon le modèle : 199 chez OpenAI, 206 chez Mistral pour notre e-mail. Les prix au million de tokens varient aussi énormément d'un modèle à l'autre. Pour comparer deux offres, il faut multiplier le bon nombre de tokens par le bon prix, ce que fait un compteur.

## Comment s'en servir en pratique

1. Collez votre prompt (ou votre document) dans [TokenSave](/fr/).
2. Regardez le nombre de tokens et le coût estimé pour GPT, Claude et Gemini.
3. Essayez une variante : plus courte, en CSV plutôt qu'en JSON, ou en anglais.
4. Appuyez sur **💸 Économiser des tokens** : l'outil nettoie les espaces, traduit en anglais et ajoute « Reply in French. » pour que la réponse reste en français.

Tout se passe dans votre navigateur : le texte n'est envoyé à aucun serveur. Gratuit et sans inscription.

## Les limites

- Deux textes, deux tokeniseurs. Claude et Gemini utilisent d'autres tokeniseurs ; les chiffres exacts changent, mais pas l'ordre de grandeur.
- Les images, les PDF et les fichiers audio sont comptés autrement que le texte.
- Le coût réel dépend aussi du cache, des remises par lot et de la longueur des réponses.

Pour aller plus loin : [Combien de tokens coûte le français ?](/fr/blog/tokens-francais-gpt) et [Mistral ou ChatGPT : combien coûte vraiment un prompt en français ?](/fr/blog/mistral-chatgpt-cout-prompt-francais)

*Mesures effectuées en octobre 2026 avec o200k_base (OpenAI) et Tekken 2024-09 (Mistral). Les prix utilisés dans l'exemple sont hypothétiques.*

## Sources

- [tiktoken (OpenAI) : le tokeniseur o200k_base](https://github.com/openai/tiktoken)
- [Mistral NeMo et le tokeniseur Tekken (Mistral AI)](https://mistral.ai/news/mistral-nemo/)
- [Tarifs de l'API OpenAI (prix au million de tokens)](https://developers.openai.com/api/docs/pricing)
- [Comprendre et compter les tokens (aide OpenAI)](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)
- [Comptage des tokens (documentation Anthropic)](https://platform.claude.com/docs/en/build-with-claude/token-counting)
- [Le Chat devient Vibe (Mistral AI)](https://mistral.ai/news/vibe-agent/)
<!-- autoimg -->
