# Générateur de Propositions Commerciales pour Services Marketing

## Objectif de la Compétence
Générer une proposition de services marketing professionnelle, prête pour le client. Cette compétence produit un document de proposition complet qui positionne l'agence/le consultant comme le choix évident, encadre la tarification avec des options d'ancrage et par paliers, et inclut des projections de ROI pour justifier l'investissement. Tout le contenu doit être rédigé en français, avec un ton professionnel et formel (vouvoiement).

## Quand l'Utiliser
- L'utilisateur souhaite créer une proposition pour un prospect marketing
- L'utilisateur a terminé un appel de découverte et doit formaliser la mission
- L'utilisateur veut un modèle pour les propositions de son agence marketing
- Déclenché par `/market proposal` ou `/market proposal <nom du client>`

## Comment Exécuter

### Étape 1 : Collecter les Informations de la Proposition
Collectez ces détails auprès de l'utilisateur (demandez s'ils ne sont pas fournis) :

**Sur le Client :**
1. Nom et entreprise du client
2. Secteur d'activité et modèle économique
3. Situation marketing actuelle (ce qu'il fait actuellement)
4. Points de douleur ou défis principaux
5. Objectifs (chiffre d'affaires, croissance, leads, notoriété de marque)
6. Fourchette budgétaire (si connue — en euros)
7. Calendrier de décision
8. Parties prenantes et décideurs clés

**Sur les Services :**
1. Quels services proposez-vous ? (SEO/référencement naturel, publicités payantes/SEA, contenu, réseaux sociaux, email, full-stack)
2. Modèle de mission (forfait mensuel, projet, basé sur la performance)
3. Calendrier proposé
4. Vos études de cas et résultats pertinents

**Si des données d'audit existent :** Vérifiez tout résultat `/market audit` précédent. Si trouvé, intégrez automatiquement les résultats dans la section Analyse de la Situation pour une proposition étayée par les données.

### Étape 2 : Cadre de Questions pour l'Appel de Découverte
Si l'utilisateur n'a pas encore eu l'appel de découverte, fournissez ces 10 questions essentielles :

**Compréhension de l'Activité :**
1. "Pouvez-vous me présenter votre modèle économique ? Comment générez-vous votre chiffre d'affaires ?"
2. "Qui est votre client idéal ? Décrivez-le en détail."
3. "À quoi ressemble votre processus de vente du premier contact jusqu'à la signature ?"

**Marketing Actuel :**
4. "Qu'est-ce que vous faites actuellement en marketing, et qu'est-ce qui fonctionne ou ne fonctionne pas ?"
5. "Quel est votre budget marketing mensuel actuel, et quel est le ROI ?"
6. "Quels outils et plateformes utilisez-vous ?"

**Objectifs et Attentes :**
7. "Si nous connaissons un succès remarquable, à quoi ressemble la situation dans 6 mois ? 12 mois ?"
8. "Quels chiffres spécifiques essayez-vous d'atteindre ? (Chiffre d'affaires, leads, trafic)"
9. "Quelle est la valeur vie client pour vous ?"

**Décision et Processus :**
10. "Qui d'autre est impliqué dans cette décision, et quel est votre calendrier pour choisir un prestataire ?"

**Questions Bonus :**
- "Quelle est votre plus grande frustration en matière de marketing en ce moment ?"
- "Avez-vous déjà travaillé avec des agences ou des consultants ? Qu'est-ce qui s'est bien ou mal passé ?"
- "Y a-t-il quelque chose qui vous ferait dire 'non' à travailler ensemble ?"

### Étape 3 : Construire le Document de Proposition

#### Section 1 : Page de Couverture
```
[Logo de votre Entreprise]

Proposition de Stratégie Marketing
Préparée pour : [Nom du Client]
Préparée par : [Votre Nom / Agence]
Date : [Date]
Valable jusqu'au : [Date + 30 jours]

CONFIDENTIEL
```

#### Section 2 : Résumé Exécutif (1 page maximum)
Rédigez un résumé concis qui :
- Reconnaît la situation et les objectifs du client
- Énonce le problème principal que vous allez résoudre
- Présente votre approche recommandée
- Évoque le résultat attendu
- Crée une urgence d'agir

**Modèle (en vouvoiement formel) :**
```
[Nom du Client] se trouve à un point d'inflexion. Avec [situation actuelle — ex : un produit-marché validé mais une génération de leads irrégulière], il existe une opportunité significative de [résultat souhaité — ex : accélérer l'acquisition clients pour soutenir vos objectifs de croissance].

Sur la base de notre analyse de [ce que vous avez examiné — leur site, publicités, concurrents, etc.], nous avons identifié [X] domaines clés où des améliorations stratégiques pourraient générer [résultat spécifique — ex : une augmentation de 40 à 60% des leads qualifiés dans les 6 mois].

Cette proposition décrit une mission de [durée] axée sur [domaines de services principaux], conçue pour [résultat principal]. Notre approche repose sur [votre différenciateur — ex : une méthodologie data-driven, une expertise sectorielle, des cadres éprouvés].

Nous recommandons de commencer par [première phase] pour établir les bases et obtenir des gains rapides, puis d'amplifier les efforts en fonction des données de performance.
```

#### Section 3 : Analyse de la Situation (2-3 pages)
Présentez votre analyse du marketing actuel du client. C'est là où les données d'audit de `/market audit` sont précieuses.

**Structure :**
1. **État Actuel** — Ce qu'ils font et comment cela fonctionne
2. **Opportunités Identifiées** — Domaines spécifiques où l'amélioration est possible
3. **Paysage Concurrentiel** — Comment ils se comparent aux concurrents (de `/market competitors` si disponible)
4. **Défis Clés** — Obstacles à traiter
5. **Contexte du Marché** — Tendances sectorielles et benchmarks (contexte européen si pertinent)

**Important :** Présentez tout comme des opportunités, pas des échecs. Le client doit se sentir compris, pas critiqué.

Bien : "Votre site web convertit à environ 1,8%, ce qui est en dessous du benchmark sectoriel de 3,2%. Nous voyons un chemin clair pour combler cet écart grâce à des initiatives CRO ciblées."

Mauvais : "Votre site web a un taux de conversion terrible et nécessite une refonte complète."

#### Section 4 : Stratégie et Approche (2-3 pages)
Présentez votre stratégie recommandée. Soyez suffisamment spécifique pour démontrer votre expertise, mais pas au point qu'ils pourraient l'exécuter sans vous.

**Structure :**
1. **Cadre Stratégique** — Votre approche globale et méthodologie
2. **Phase 1 : Fondations** (Mois 1-2) — Configuration, audits, bases de référence, gains rapides
3. **Phase 2 : Croissance** (Mois 3-4) — Exécution des campagnes principales, optimisation
4. **Phase 3 : Accélération** (Mois 5-6) — Amplifier ce qui fonctionne, éliminer ce qui ne fonctionne pas, augmenter l'investissement sur les gagnants
5. **En Continu : Optimiser** — Amélioration continue, reporting, raffinement de la stratégie

Pour chaque phase, incluez :
- Activités et livrables spécifiques
- Résultats attendus
- Comment le succès sera mesuré

#### Section 5 : Périmètre de la Mission (1-2 pages)
Détaillez exactement ce qui est inclus (et ce qui ne l'est pas).

**Inclus :**
- Livrables spécifiques avec quantités (ex : "8 articles de blog par mois, 1 500-2 000 mots chacun")
- Cadence des réunions (ex : "Appels stratégiques bimensuels, reporting mensuel")
- Engagements de temps de réponse (ex : "Réponse sous 24h les jours ouvrables")
- Outils et plateformes inclus
- Format et fréquence du reporting

**Explicitement Exclu :**
- Éléments hors périmètre pour prévenir le glissement de périmètre
- Coûts supplémentaires (budget publicitaire, logiciels, photos stock)
- Hypothèses sur les responsabilités du client

**Section Responsabilités du Client :**
Listez ce dont vous avez besoin de la part du client pour réussir :
- Retours et validations rapides (précisez le SLA)
- Accès aux comptes, outils et données
- Interlocuteur désigné
- Validations de contenu sous X jours ouvrables
- Budget publicitaire (séparé des honoraires de gestion)

#### Section 6 : Calendrier (1 page)
Calendrier visuel montrant les phases, jalons et livrables.

```
Mois 1      | Mois 2      | Mois 3      | Mois 4      | Mois 5      | Mois 6
------------|-------------|-------------|-------------|-------------|----------
FONDATIONS  | FONDATIONS  | CROISSANCE  | CROISSANCE  | ACCÉLÉRAT.  | ACCÉLÉRAT.
Audit &     | Gains       | Lancement   | Optimis.    | Amplifier   | Plein
Configuration| rapides &  | Campagnes   | & itérer    | gagnants    | régime
            | bases réf.  |             |             |             |

Jalons Clés :
- Semaine 2 : Audit et document stratégique finalisés
- Semaine 4 : Premières campagnes en ligne
- Mois 2 : Premier rapport de performance
- Mois 3 : Recommandations d'optimisation
- Mois 6 : Revue complète et actualisation de la stratégie
```

#### Section 7 : Investissement (1-2 pages)
Présentez la tarification en utilisant la structure à trois paliers Bon-Mieux-Meilleur. Tous les montants en euros (€), avec mention TVA.

**Modèle de Tarification à Trois Paliers :**

| Composant | Croissance | Accélération | Domination |
|---|---|---|---|
| Stratégie & Planification | Revue trimestrielle | Stratégie mensuelle | Stratégie hebdomadaire |
| Création de Contenu | 4 pièces/mois | 8 pièces/mois | 16 pièces/mois |
| Réseaux Sociaux | 3 plateformes | 5 plateformes | Toutes les plateformes |
| Gestion Publicités | Jusqu'à 5 000€ de budget | Jusqu'à 15 000€ de budget | Jusqu'à 50 000€ de budget |
| SEO/Référencement Naturel | On-page basique | Programme SEO complet | SEO complet + link building |
| Email Marketing | — | Newsletter mensuelle | Automation complète |
| Reporting | Rapport mensuel | Rapport bimensuel | Tableau de bord hebdomadaire |
| Réunions | Appel mensuel | Appel bimensuel | Appel hebdomadaire |
| **Investissement Mensuel HT** | **X XXX€ HT** | **X XXX€ HT** | **X XXX€ HT** |
| **TVA (20%)** | **XXX€** | **XXX€** | **XXX€** |
| **Total TTC** | **X XXX€ TTC** | **X XXX€ TTC** | **X XXX€ TTC** |

**Conseils de Psychologie Tarifaire :**
- Présentez trois options ; la plupart des clients choisissent le palier intermédiaire
- Nommez les paliers avec des labels aspirationnels (pas Bronze/Argent/Or)
- Ancrez d'abord le palier le plus élevé pour rendre le palier intermédiaire raisonnable
- Incluez un badge "Le Plus Populaire" ou "Recommandé" sur le palier intermédiaire
- Montrez le calcul : "À [votre valeur vie client], vous n'avez besoin que de [X] nouveaux clients par mois pour voir un ROI positif"
- Précisez toujours HT et TTC (TVA 20% en France)

**Référence des Modèles de Tarification :**

| Modèle | Quand l'Utiliser | Fourchette Typique |
|---|---|---|
| Forfait Mensuel | Services continus, relation à long terme | 2 000€-25 000€ HT/mois |
| Basé sur le Projet | Périmètre défini, livrable unique | 5 000€-100 000€ HT par projet |
| Basé sur la Performance | Le client veut partager le risque | Base + % du CA/leads |
| Hybride | Missions complexes | Forfait de base + prime de performance |
| Taux Horaire | Conseil, advisory, ad hoc | 150€-500€ HT/heure |

#### Section 8 : Projection du ROI
Montrez au client le retour attendu sur son investissement.

**Cadre de Calcul du ROI :**
```
État Actuel :
- Trafic mensuel du site web : [X]
- Taux de conversion actuel : [X%]
- Leads actuels/mois : [X]
- Taux de closing : [X%]
- Valeur moyenne de la commande : [X€]
- CA mensuel actuel issu du marketing : [X€]

État Projeté (6 mois) :
- Augmentation de trafic projetée : [X%] -> [nouveau trafic]
- Taux de conversion projeté : [X%] -> [nouveaux leads/mois]
- Augmentation projetée des leads : [X%]
- Augmentation projetée du CA : [X€]/mois
- ROI projeté sur 6 mois : [X]x

Investissement : [coût total sur 6 mois en €]
Retour Projeté : [augmentation CA projetée en €]
ROI : [X]x de retour
```

**Important :** Soyez conservateur dans les projections. Sous-promettez et sur-livrez. Utilisez des fourchettes plutôt que des chiffres précis. Ajoutez des avertissements stipulant que les résultats dépendent de multiples facteurs.

#### Section 9 : L'Équipe (0,5-1 page)
Présentez les membres de l'équipe qui travailleront sur ce compte.

Pour chaque membre de l'équipe :
- Nom et titre
- Expérience et expertise pertinentes
- Rôle dans cette mission
- Courte biographie (2-3 phrases maximum)

#### Section 10 : Études de Cas (1-2 pages)
Incluez 2-3 études de cas pertinentes démontrant des résultats similaires à ceux que vous promettez.

**Format de l'Étude de Cas :**
```
Client : [Secteur et type d'entreprise — anonymisez si nécessaire]
Défi : [1-2 phrases sur leur situation]
Solution : [1-2 phrases sur ce que vous avez fait]
Résultats :
- [Métrique spécifique 1 : ex : "Augmentation du trafic organique de 287% en 6 mois"]
- [Métrique spécifique 2 : ex : "Réduction du coût par lead de 45€ à 12€"]
- [Métrique spécifique 3 : ex : "180 000€ de nouveau CA généré"]
```

#### Section 11 : Prochaines Étapes (0,5 page)
Rendez absolument claire la suite des événements. Réduisez la friction.

```
Prêt à aller de l'avant ? Voici ce qui se passe ensuite :

1. Signer cette proposition (lien de signature électronique inclus)
2. Nous planifierons un appel de lancement sous 48 heures
3. Vous recevrez notre questionnaire d'onboarding et le formulaire de demande d'accès
4. Nous commençons la phase Fondations immédiatement

Des questions ? Contactez [Nom] à [email] ou [téléphone].

Cette proposition est valable jusqu'au [date — 30 jours à partir de maintenant].
```

#### Section 12 : Mentions Légales
Section obligatoire pour toute proposition commerciale en France/UE.

```
**Mentions Légales**

[Nom de l'Agence] — [Forme juridique] au capital de [X€]
SIRET : [numéro]
Siège social : [adresse complète]
TVA intracommunautaire : [numéro]

Cette proposition est soumise à nos Conditions Générales de Vente (CGV) disponibles sur demande.
La prestation sera formalisée par un Bon de Commande ou un contrat de prestation de services.
Toutes les données collectées dans le cadre de cette mission sont traitées conformément au RGPD.
```

### Étape 4 : Conception et Mise en Forme de la Proposition

**Meilleures Pratiques :**
- Gardez la proposition totale en dessous de 15 pages (hors annexes)
- Utilisez des en-têtes, polices et couleurs cohérents tout au long
- Incluez le logo du client aux côtés du vôtre sur la page de couverture
- Utilisez des graphiques et visuels plutôt que du texte dense où c'est possible
- Mettez en gras les chiffres et résultats clés
- Utilisez l'espace blanc généreusement — ne surchargez pas le contenu
- Incluez les numéros de page et une table des matières pour les propositions plus longues
- Enregistrez en PDF pour une présentation professionnelle

**Mise en Forme en Markdown :**
- Utilisez H1 pour le titre de la proposition
- Utilisez H2 pour les sections principales
- Utilisez H3 pour les sous-sections
- Utilisez des tableaux pour les tarifs, calendriers et comparaisons
- Utilisez le gras pour l'emphase sur les points clés
- Utilisez les citations en bloc pour les témoignages clients

### Étape 5 : Séquence de Suivi Après Envoi

**Jour 0 (Jour d'Envoi) :**
Envoyez la proposition par email avec une courte note d'accompagnement. Objet : "Votre Plan de Croissance Marketing — [Nom du Client]"

**Jour 2 :**
Email de suivi : "Je souhaitais m'assurer que vous avez bien reçu la proposition. N'hésitez pas à me proposer un bref appel pour la parcourir ensemble si cela vous serait utile."

**Jour 5 :**
Suivi avec valeur ajoutée : Partagez un article pertinent, une étude de cas ou un insight lié à leur secteur. Référencez la proposition subtilement.

**Jour 7 :**
Suivi direct : "Je serais ravi d'avoir votre avis sur la proposition. Avez-vous des questions auxquelles je pourrais répondre ? Je suis disponible [créneaux spécifiques] cette semaine pour un appel."

**Jour 14 :**
Dernier suivi : "Je souhaitais vous relancer une dernière fois au sujet de la proposition. Je comprends que le timing n'est peut-être pas optimal — si tel est le cas, je serais ravi de vous recontacter quand le moment sera plus opportun. Sinon, je serais très heureux d'échanger sur les prochaines étapes."

**Jour 21 :**
Email de rupture : "N'ayant pas eu de retour de votre part, j'imagine que le moment n'est pas opportun. Je clôturerai cette proposition le [date d'expiration]. Si les choses évoluent, ma porte reste ouverte. Je vous souhaite, ainsi qu'à [Entreprise], tout le succès que vous méritez."

### Étape 6 : Traitement des Objections

Préparez des réponses aux objections courantes des clients :

| Objection | Cadre de Réponse |
|---|---|
| "Trop cher" | Recadrez comme investissement, montrez le calcul du ROI, proposez un périmètre de démarrage plus petit, comparez au coût de l'inaction |
| "Nous pouvons le faire en interne" | Soulignez le coût d'opportunité, l'expertise spécialisée, la rapidité des résultats et le coût réel d'un recrutement interne |
| "Nous avons essayé ça avant et ça n'a pas fonctionné" | Demandez ce qui spécifiquement n'a pas fonctionné, différenciez votre approche, proposez un projet pilote avec des critères de succès clairs |
| "Nous devons réfléchir" | Fixez une date de suivi spécifique, proposez de traiter des préoccupations spécifiques, fournissez des références supplémentaires |
| "Pouvez-vous garantir les résultats ?" | Expliquez pourquoi les garanties sont irréalistes en marketing mais partagez les résultats historiques, proposez une composante de performance |
| "Nous parlons à d'autres agences" | Accueillez-le, différenciez-vous sur la méthodologie pas le prix, proposez une période d'essai, mettez l'accent sur la compatibilité culturelle |
| "Le délai est trop long" | Expliquez pourquoi les raccourcis échouent, proposez une phase gains rapides, montrez l'approche par phases avec une valeur précoce |
| "Nous n'avons pas le budget pour l'instant" | Proposez une mission de démarrage plus petite, différez une partie du paiement, montrez le coût de l'attente |

### Étape 7 : Conditions Générales de Vente (CGV) et Mentions Légales

Incluez ces éléments dans l'annexe de la proposition ou dans un document séparé (CGV obligatoires pour les relations B2B en France) :

1. **Conditions de Paiement :** Paiement à 30 jours (Net 30), modes de paiement acceptés (virement SEPA, chèque), pénalités de retard (taux légal + 10 points selon la loi française)
2. **Durée du Contrat :** Période d'engagement minimale, conditions de renouvellement automatique
3. **Politique d'Annulation :** Délai de préavis requis (typiquement 30 jours), processus de sortie
4. **Modifications du Périmètre :** Processus de traitement des changements de périmètre et coûts supplémentaires
5. **Propriété Intellectuelle :** Qui détient les livrables, conditions de licence
6. **Confidentialité :** Termes NDA, comment les données client sont traitées (RGPD)
7. **Limitations de Responsabilité :** Plafonds de responsabilité, force majeure
8. **Reporting et Communication :** Cadence et format convenus
9. **Coûts Tiers :** Responsabilité du client pour le budget publicitaire, logiciels, photos stock
10. **Avertissement sur les Résultats :** Les résultats marketing ne sont pas garantis, contexte des performances passées
11. **Bon de Commande :** La mission débute à réception du bon de commande signé ou du premier acompte
12. **Données Personnelles (RGPD) :** Désignation des rôles Responsable de Traitement / Sous-Traitant selon la nature des données traitées

## Format de Sortie

Générez un fichier appelé `PROPOSITION-CLIENT.md`. Tout le contenu doit être rédigé en français avec un ton professionnel et formel :

```markdown
# Proposition de Services Marketing

## Préparée pour : [Nom du Client]
## Préparée par : [Nom de l'Agence]
## Date : [Date]

---

## Table des Matières
1. Résumé Exécutif
2. Analyse de la Situation
3. Stratégie & Approche
4. Périmètre de la Mission
5. Calendrier
6. Investissement (avec TVA)
7. Projection du ROI
8. Notre Équipe
9. Études de Cas
10. Prochaines Étapes
11. Mentions Légales

---

[Contenu complet de la proposition avec toutes les sections renseignées selon les détails du client]

---

## Annexes
- Conditions Générales de Vente (CGV)
- Description Détaillée des Livrables
- Stack d'Outils Utilisés
- Bon de Commande
```

## Principes Clés
- La proposition est un document de vente, pas un cahier des charges. Elle doit VENDRE, pas simplement décrire.
- Commencez par les problèmes et objectifs du client, pas par vos services. Faites-le se sentir compris avant de présenter des solutions.
- Chaque tarif doit être ancré au ROI qu'il va générer. Ne présentez jamais le coût sans contexte.
- Utilisez le propre langage du client issu de l'appel de découverte. Renvoyez-lui ses propres mots.
- Si des données d'audit sont disponibles grâce aux compétences précédentes, utilisez-les abondamment — les propositions étayées par les données concluent 2-3 fois plus vite que les propositions génériques.
- Gardez-la concise. Les dirigeants parcourent. Utilisez le gras, les en-têtes et les tableaux pour rendre les informations clés lisibles rapidement.
- Incluez toujours une prochaine étape spécifique et limitée dans le temps. L'ambiguïté tue les deals.
- Rédigez en vouvoiement formel tout au long de la proposition.
- Mentionnez toujours les prix HT et TTC (TVA 20%) pour respecter la réglementation française.
- Incluez les Mentions Légales et référencez les CGV — obligatoire pour la conformité juridique française.
