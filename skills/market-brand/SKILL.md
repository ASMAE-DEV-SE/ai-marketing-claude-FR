# Analyse de la Voix de Marque et Génération de Charte Éditoriale

## Objectif de la Compétence
Analyser la voix, le ton et les messages d'une marque sur tous les canaux disponibles et générer un document complet de charte éditoriale. Cette compétence examine comment une marque communique, identifie les patterns et incohérences, et produit des recommandations actionnables que tout rédacteur ou marketeur peut suivre pour maintenir la cohérence de marque. Tout le contenu doit être rédigé en français et adapté au contexte culturel français et européen, en utilisant un ton professionnel de business français.

## Quand l'Utiliser
- L'utilisateur souhaite comprendre ou documenter la voix de sa marque
- L'utilisateur a besoin d'une charte éditoriale pour son équipe, des freelances ou une agence
- L'utilisateur veut assurer la cohérence sur tous les canaux marketing
- L'utilisateur est en cours de rebranding ou affine son identité de marque
- L'utilisateur veut comparer la voix de sa marque à ses concurrents
- Déclenché par `/market brand <url>` ou `/market brand`

## Comment Exécuter

### Étape 1 : Collecter le Matériel Source
Pour analyser la voix d'une marque, examinez le contenu de plusieurs sources. Priorisez dans cet ordre :

**Sources Primaires (à analyser obligatoirement) :**
1. **Page d'accueil** — La représentation la plus aboutie de la marque
2. **Page À propos** — Comment la marque se décrit elle-même
3. **Pages produit/service** — Comment elle présente ses offres

**Sources Secondaires (à analyser si disponibles) :**
4. **Articles de blog** (au moins 3-5 articles récents)
5. **Profils réseaux sociaux** (biographie, publications récentes, style d'engagement)
6. **Newsletters email** (email de bienvenue, envois récents)
7. **Textes orientés client** (messages d'erreur, flux d'onboarding, documentation d'aide)

**Sources Tertiaires :**
8. **Offres d'emploi** — Révèle la culture interne et les valeurs
9. **Communiqués de presse** — Style de communication formelle
10. **Textes publicitaires** — Approche des messages payants
11. **Scripts vidéo ou transcriptions podcast** — Voix de marque parlée

Utilisez les outils navigateur ou le script analyze_page.py pour accéder au contenu web. Pour les réseaux sociaux, vérifiez les liens sociaux sur le site et analysez les profils liés.

### Étape 2 : Analyse des Dimensions de la Voix
Cartographiez la voix de la marque selon quatre dimensions principales. Chaque dimension est un spectre, pas un binaire.

#### Dimension 1 : Formelle <-----> Décontractée
Où la marque se situe-t-elle sur le spectre de la formalité ? En France, le registre par défaut des communications B2B est plus formel qu'en Amérique du Nord.

| Signal | Formelle | Décontractée |
|---|---|---|
| Vouvoiement/Tutoiement | Vouvoie systématiquement | Tutoie parfois |
| Contractions | Les évite ("ne faites pas", "ne peut pas") | Les utilise librement ("ne faites pas" → "faites pas") |
| Structure des phrases | Complexe, phrases plus longues | Courte, phrases percutantes |
| Vocabulaire | Professionnel, standard du secteur | Conversationnel, mots du quotidien |
| Salutations | "Madame, Monsieur" | "Bonjour !" ou "Salut !" |
| Pronoms | Troisième personne ("l'entreprise", "on") | Première/deuxième personne ("nous", "vous") |
| Humour | Rare ou absent | Fréquent, naturel |
| Argot/expressions familières | Jamais | Occasionnellement ou fréquemment |

**Score : 1 (extrêmement formelle) à 10 (extrêmement décontractée)**

**Preuves requises :** Citez 3-5 exemples spécifiques du matériel source qui étayent votre évaluation.

#### Dimension 2 : Sérieuse <-----> Enjouée
Quelle légèreté la marque injecte-t-elle dans sa communication ?

| Signal | Sérieuse | Enjouée |
|---|---|---|
| Ton | Autoritaire, mesuré | Bonne humeur, amusant |
| Métaphores | Rares, conservatrices | Créatives, inattendues |
| Points d'exclamation | Rares | Fréquents |
| Utilisation d'émojis | Jamais | Parfois ou souvent |
| Jeux de mots | Jamais | Les apprécie |
| Messages d'erreur | "Une erreur est survenue" | "Oups ! Quelque chose s'est mal passé" |
| Auto-dérision | Jamais | Occasionnellement |

**Score : 1 (extrêmement sérieuse) à 10 (extrêmement enjouée)**

#### Dimension 3 : Technique <-----> Simple
Quel niveau d'expertise la marque suppose-t-elle chez son audience ?

| Signal | Technique | Simple |
|---|---|---|
| Jargon | Utilise librement les termes sectoriels | Évite ou explique tout jargon |
| Acronymes | Utilise sans définition | Épèle lors de la première utilisation |
| Niveau de détail | Explications approfondies | Vues d'ensemble de haut niveau |
| Hypothèse sur l'audience | Audience experte | Audience générale |
| Données/statistiques | Fréquentes, détaillées | Occasionnelles, simplifiées |
| Exemples | Complexes, spécifiques au domaine | Simples, analogies accessibles |

**Score : 1 (extrêmement technique) à 10 (extrêmement simple)**

#### Dimension 4 : Réservée <-----> Affirmée
Quelle personnalité et confiance la marque projette-t-elle ? Note : en France, une affirmation excessive peut être perçue comme arrogante — l'équilibre est clé.

| Signal | Réservée | Affirmée |
|---|---|---|
| Affirmations | Nuancées ("nous croyons", "peut aider") | Directes ("nous garantissons", "le meilleur") |
| Opinions | Neutres, équilibrées | Fortes, affirmées |
| Références concurrentielles | Évite de mentionner les concurrents | Compare directement |
| Personnalité | Professionnelle, discrète | Distinctive, mémorable |
| Promesses | Conservatrices | Ambitieuses |
| Controverse | Évite | Embrasse si aligné avec les valeurs |

**Score : 1 (extrêmement réservée) à 10 (extrêmement affirmée)**

### Étape 3 : Cartographie du Spectre de Ton

Au-delà des quatre dimensions, cartographiez comment le ton de la marque évolue selon les contextes :

| Contexte | Ton Typique | Exemple |
|---|---|---|
| Page d'accueil | [Confiant/Accueillant/Urgent/etc.] | "[citation de la page d'accueil]" |
| Description produit | [Informatif/Persuasif/Technique/etc.] | "[citation]" |
| Article de blog | [Éducatif/Conversationnel/Autoritaire/etc.] | "[citation]" |
| Réseaux sociaux | [Décontracté/Engageant/Promotionnel/etc.] | "[citation]" |
| Page d'erreur/404 | [Apologétique/Humoristique/Utile/etc.] | "[citation]" |
| Objets d'emails | [Direct/Curieux/Urgent/etc.] | "[citation]" |
| Boutons CTA | [Orienté action/Axé bénéfices/Urgent/etc.] | "[citation]" |
| Support client | [Empathique/Professionnel/Aimable/etc.] | "[citation]" |

### Étape 4 : Cadre de Personnalité de Marque

Associez la marque à l'un des cinq archétypes de personnalité principaux (les marques peuvent combiner 1-2) :

#### Les 5 Archétypes

**1. L'Autorité**
- Caractéristiques : Expert, fiable, fondé sur les données, établi
- Voix : Confiant mais pas arrogant, éducatif, précis
- Secteurs : Finance, santé, B2B entreprise, juridique, conseil
- Marques européennes types : McKinsey, Deutsche Bank, PwC France
- Phrases clés : "La recherche montre...", "Nos experts...", "Leader du secteur..."

**2. L'Innovateur**
- Caractéristiques : Avant-gardiste, disruptif, visionnaire, technophile
- Voix : Excitant, tourné vers l'avenir, parfois provocateur
- Secteurs : Tech, SaaS, startups, énergie renouvelable
- Marques européennes types : BlaBlaCar, Doctolib, OVHcloud
- Phrases clés : "Réinventez...", "L'avenir de...", "Nous construisons..."

**3. L'Ami**
- Caractéristiques : Chaleureux, accessible, utile, proche
- Voix : Conversationnel, empathique, inclusif, encourageant
- Secteurs : Produits grand public, éducation, plateformes communautaires
- Marques européennes types : Alan, Shine, Back Market
- Phrases clés : "On comprend...", "Vous pouvez y arriver...", "Là pour vous aider..."

**4. Le Rebelle**
- Caractéristiques : Audacieux, challengeant les conventions, irrévérencieux, passionné
- Voix : Direct, affirmé, parfois confrontationnel, mémorable
- Secteurs : Lifestyle, fitness, industries créatives, direct-to-consumer
- Marques européennes types : Gymshark, Oatly, ManoMano
- Phrases clés : "Arrêtez de vous contenter de...", "La vérité est...", "Nous en avons fini avec..."

**5. Le Guide**
- Caractéristiques : Sage, patient, méthodique, digne de confiance
- Voix : Clair, instructif, soutenant, compétent
- Secteurs : Éducation, développement professionnel, outils, plateformes
- Marques européennes types : Deezer, Sendinblue/Brevo, Qonto
- Phrases clés : "Voici comment...", "Étape par étape...", "Le guide complet de..."

**Évaluation :**
- Archétype principal : [lequel et pourquoi]
- Archétype secondaire : [si applicable]
- Adéquation à l'archétype : [Fort/Modéré/Faible — comment la marque incarne-t-elle cet archétype ?]

### Étape 5 : Analyse du Vocabulaire

Identifiez les patterns dans les choix de mots de la marque :

#### Mots Utilisés Fréquemment
Analysez tout le matériel source et identifiez les 15-20 mots ou phrases les plus caractéristiques. Organisez par catégorie :

**Mots d'action :** (verbes favoris)
- ex : "construire", "développer", "transformer", "optimiser", "accélérer"

**Mots descriptifs :** (adjectifs utilisés)
- ex : "performant", "simple", "robuste", "fluide", "innovant"

**Mots de valeur :** (mots reflétant leurs valeurs)
- ex : "transparent", "durable", "inclusif", "fiable", "confidentiel"

**Termes sectoriels :**
- ex : "tunnel de vente", "taux de conversion", "proposition de valeur", "référencement naturel", "réseaux sociaux"

#### Mots Évités
Identifiez les mots notamment absents ou qui sembleraient décalés par rapport à la marque :

- Mots trop familiers pour la marque (si formelle)
- Mots trop techniques pour la marque (si simple)
- Terminologie concurrentielle délibérément évitée
- Clichés sectoriels contournés

#### Phrases Signature
La marque a-t-elle des phrases récurrentes, des slogans ou des patterns linguistiques ?

- Slogan : [s'il en ont un]
- Phrases récurrentes : [patterns remarqués]
- Patterns linguistiques : [ex : commence toujours les phrases par des verbes, utilise fréquemment les tirets, favorise les paragraphes courts]

### Étape 6 : Contexte Culturel Français

La voix de marque doit tenir compte des spécificités culturelles françaises :

**Style de Communication Français :**
- Structure logique et argumentée (thèse - antithèse - synthèse)
- Respect de la distance professionnelle — le vouvoiement est la norme en B2B
- Appréciation de la nuance et de la subtilité plutôt que des affirmations directes
- Valorisation de l'expertise et de la légitimité intellectuelle
- La preuve et les données sont très respectées

**Ce qui Fonctionne en France :**
- Argumentation structurée et logique
- Références à l'expertise et aux certifications
- Humour subtil et discret plutôt qu'exubérant
- Mise en avant des valeurs collectives (service, qualité, durabilité)
- Transparence sur les prix et la politique de confidentialité (RGPD)

**Ce qui Peut Paraître Excessif en France :**
- Superlatifs trop fréquents ("le meilleur", "n°1", "révolutionnaire")
- Enthousiasme excessif dans le copywriting
- Familiarité non sollicitée (tutoiement avec des inconnus)
- Promesses trop fortes sans preuves

### Étape 7 : Comparaison de la Voix des Concurrents

Comparez la voix de la marque à 2-3 concurrents clés :

**Matrice de Comparaison des Voix :**
| Dimension | [Marque] | Concurrent 1 | Concurrent 2 | Concurrent 3 |
|---|---|---|---|---|
| Formelle <> Décontractée | X/10 | X/10 | X/10 | X/10 |
| Sérieuse <> Enjouée | X/10 | X/10 | X/10 | X/10 |
| Technique <> Simple | X/10 | X/10 | X/10 | X/10 |
| Réservée <> Affirmée | X/10 | X/10 | X/10 | X/10 |
| Archétype Principal | [type] | [type] | [type] | [type] |

**Évaluation de la Différenciation :**
- Quelle est la distinctivité de la voix de la marque par rapport aux concurrents ?
- Où les voix se recoupent-elles ? (opportunité de différenciation potentielle)
- Quel territoire de voix est inoccupé dans le paysage concurrentiel ?
- Recommandations spécifiques pour la différenciation vocale

### Étape 8 : Audit de Cohérence

Évaluez la cohérence de la voix sur tous les canaux analysés :

| Canal | Cohérence de la Voix | Notes |
|---|---|---|
| Page d'accueil | Cohérente/Principalement/Incohérente | [observations spécifiques] |
| Page À propos | Cohérente/Principalement/Incohérente | [notes] |
| Blog | Cohérente/Principalement/Incohérente | [notes] |
| Réseaux sociaux | Cohérente/Principalement/Incohérente | [notes] |
| Email | Cohérente/Principalement/Incohérente | [notes] |
| Pages produit | Cohérente/Principalement/Incohérente | [notes] |

**Problèmes de Cohérence Courants :**
- Différents rédacteurs créant des tons notablement différents
- Voix des réseaux sociaux radicalement différente du site web
- Texte du site formel mais newsletters email décontractées
- Contenu de blog rédigé dans une voix complètement différente des pages produit
- Messages d'erreur ou microcopy décalés par rapport à la marque
- Anciennes pages non mises à jour pour correspondre à la voix de marque actuelle
- Incohérence dans le registre (vouvoiement/tutoiement mélangés)

**Score de Cohérence Global :** X/10

### Étape 9 : Hiérarchie des Messages de Marque

Documentez les messages de la marque du plus condensé au plus développé :

#### Niveau 1 : Slogan (moins de 10 mots)
La forme la plus condensée du message de marque.
- Actuel : "[slogan existant ou suggestion]"
- Évaluation : Capture-t-il la proposition de valeur centrale ?

#### Niveau 2 : Propositions de Valeur (1 phrase chacune)
3-5 propositions de valeur centrales qui soutiennent la promesse de marque.
1. "[Proposition de valeur 1]"
2. "[Proposition de valeur 2]"
3. "[Proposition de valeur 3]"

#### Niveau 3 : Pitch Ascenseur (30 secondes / 75 mots)
Une explication conversationnelle de ce que fait la marque et pourquoi c'est important.
"[Pitch ascenseur rédigé à partir du contenu analysé]"

#### Niveau 4 : Boilerplate (100-150 mots)
Le paragraphe standard "à propos de nous" utilisé dans les communiqués de presse, signatures email et biographies de conférenciers.
"[Boilerplate rédigé à partir du contenu analysé]"

#### Niveau 5 : Histoire de Marque Complète (300-500 mots)
Le récit complet de qui est la marque, ce qu'elle défend et pourquoi elle existe.
- Statut actuel : [Existe/Partiel/Absent]
- Recommandations d'amélioration

### Étape 10 : Générer la Documentation de la Voix de Marque

Créez le guide complet des À faire et À éviter :

#### Tableau de la Voix

```
NOTRE VOIX EST :                    NOTRE VOIX N'EST PAS :
--------------------------------------------------------
[Caractéristique 1]                 [Anti-caractéristique 1]
ex : "Experte"                      ex : "Prétentieuse"

[Caractéristique 2]                 [Anti-caractéristique 2]
ex : "Utile"                        ex : "Condescendante"

[Caractéristique 3]                 [Anti-caractéristique 3]
ex : "Claire"                       ex : "Simpliste"

[Caractéristique 4]                 [Anti-caractéristique 4]
ex : "Affirmée"                     ex : "Agressive"
```

#### À Faire et À Éviter en Rédaction

**À FAIRE :**
- [Instruction de rédaction spécifique basée sur l'analyse]
- [Ex : "Vouvoyer systématiquement dans les communications client"]
- [Ex : "Mettre en avant le bénéfice avant la fonctionnalité"]
- [Ex : "Utiliser la voix active dans tous les titres et CTA"]
- [Ex : "S'adresser directement au lecteur avec 'vous' et 'votre'"]
- [Ex : "Structurer l'argumentation logiquement (problème → solution → bénéfice)"]

**À ÉVITER :**
- [Anti-patterns spécifiques basés sur l'analyse]
- [Ex : "Ne pas utiliser le jargon sans l'expliquer"]
- [Ex : "Ne pas utiliser la voix passive dans les appels à l'action"]
- [Ex : "Ne pas accumuler les superlatifs ('le meilleur', 'n°1', 'révolutionnaire')"]
- [Ex : "Ne pas commencer les phrases par 'Nous' — se concentrer sur le client"]
- [Ex : "Ne pas utiliser de termes anglais si un équivalent français existe"]

### Étape 11 : Exemples de Copywriting dans la Voix Identifiée

Fournissez 5-8 exemples de copies rédigées dans la voix de marque identifiée, adaptés au marché français :

**1. Titre de Page d'Accueil :**
"[Exemple de titre dans la voix de marque — en français]"

**2. Paragraphe de Description Produit :**
"[Exemple de description produit dans la voix de marque — en français]"

**3. Ouverture d'Article de Blog :**
"[Exemple d'intro d'article dans la voix de marque — en français]"

**4. Publication Réseaux Sociaux :**
"[Exemple de post social dans la voix de marque — en français]"

**5. Objet d'Email :**
"[Exemple d'objet d'email dans la voix de marque — en français]"

**6. Texte de Bouton CTA :**
"[Exemple de texte CTA dans la voix de marque — en français, ex : 'Commencer gratuitement', 'Demander une démo', 'Télécharger le guide']"

**7. Message d'Erreur :**
"[Exemple de message d'erreur dans la voix de marque — en français]"

**8. Message de Remerciement Client :**
"[Exemple de message de remerciement dans la voix de marque — en français]"

## Format de Sortie

Générez un fichier appelé `VOIX-MARQUE.md`. Tout le contenu doit être rédigé en français :

```markdown
# Charte de Voix de Marque
## [Nom de la Marque]
### Date d'Analyse : [Date]

---

## Résumé de la Voix
[Résumé en 2-3 phrases de la voix de marque, la personnalité et les caractéristiques clés]

---

## Dimensions de la Voix

### Formelle <-----> Décontractée : [X/10]
[Preuves et explications]

### Sérieuse <-----> Enjouée : [X/10]
[Preuves et explications]

### Technique <-----> Simple : [X/10]
[Preuves et explications]

### Réservée <-----> Affirmée : [X/10]
[Preuves et explications]

### Carte Visuelle de la Voix
```
Formelle                                   Décontractée
|----[X]----------------------------------|
Sérieuse                                   Enjouée
|--------[X]------------------------------|
Technique                                  Simple
|------------------[X]--------------------|
Réservée                                   Affirmée
|------------[X]--------------------------|
```

---

## Personnalité de Marque
- Archétype Principal : [Archétype]
- Archétype Secondaire : [Archétype]
- [Explication et preuves]

---

## Registre et Ton par Contexte
| Contexte | Ton | Exemple |
|---|---|---|
| [contexte] | [ton] | "[exemple en français]" |

---

## Vocabulaire

### Mots Que Nous Utilisons
[Listes de mots organisées]

### Mots Que Nous Évitons
[Mots ne correspondant pas à la marque]

### Phrases Signature
[Patterns et phrases récurrentes]

---

## Tableau de la Voix
| Notre Voix EST | Notre Voix N'EST PAS |
|---|---|
| [trait] | [anti-trait] |

---

## Directives de Rédaction

### À Faire
- [directives spécifiques]

### À Éviter
- [anti-patterns spécifiques]

---

## Contexte Culturel Français
[Spécificités culturelles à respecter, registre, formalité, style d'argumentation]

---

## Hiérarchie des Messages de Marque

### Slogan
[slogan]

### Propositions de Valeur
1. [proposition de valeur]

### Pitch Ascenseur
[pitch]

### Boilerplate
[boilerplate]

---

## Exemples de Copywriting
[8 exemples de copy dans la voix de marque — tous en français]

---

## Comparaison de la Voix des Concurrents
[Matrice de comparaison et analyse de différenciation]

---

## Audit de Cohérence
[Évaluation canal par canal]
- Score de Cohérence Global : [X/10]

---

## Recommandations
### Actions Immédiates
1. [recommandation]

### Opportunités d'Évolution de la Voix
1. [recommandation]

### Améliorations de Cohérence
1. [recommandation]
```

## Principes Clés
- L'analyse de la voix de marque nécessite de lire comme un détective. Chaque choix de mot, décision de ponctuation et structure de phrase révèle quelque chose sur la façon dont la marque veut être perçue.
- Fournissez toujours des PREUVES pour chaque évaluation. Ne dites pas seulement "la marque est décontractée" — citez des exemples spécifiques qui le prouvent.
- Le guide de voix de marque doit être utilisable par quelqu'un qui n'a jamais travaillé avec la marque auparavant. Un nouveau rédacteur devrait pouvoir lire ce document et écrire du contenu dans la charte de la marque.
- Les exemples de copywriting sont la partie la plus précieuse du livrable. Les gens apprennent la voix par l'exemple, pas par la description. Rendez les exemples divers (titres, corps de texte, réseaux sociaux, email, messages d'erreur) pour que les rédacteurs aient des références pour chaque contexte.
- La voix et le ton sont différents. La voix est la personnalité consistante. Le ton évolue selon le contexte (une réponse à une réclamation client est différente d'une annonce de lancement de produit, mais les deux devraient être dans la même voix).
- Si la voix de la marque est incohérente sur les canaux, cadrez-le comme une opportunité de renforcer leur marque, pas comme un échec. Les problèmes de cohérence sont courants et corrigeables.
- Si l'utilisateur a précédemment exécuté `/market competitors`, utilisez ces données pour la section de comparaison de voix des concurrents.
- Les dimensions de la voix doivent être représentées visuellement (spectre basé sur du texte) pour que les parties prenantes puissent rapidement comprendre le positionnement d'un coup d'œil.
- Tenez toujours compte du contexte culturel français : le vouvoiement comme norme B2B, la structure logique de l'argumentation, la valorisation de la nuance et de l'expertise sur les affirmations excessives.
- Tous les exemples de copywriting doivent être rédigés en français, adaptés au marché français et respectant les normes de communication professionnelle française.
