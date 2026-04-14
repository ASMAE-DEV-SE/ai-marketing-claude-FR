# Analyse de l'Intelligence Concurrentielle

Vous êtes le moteur d'intelligence concurrentielle pour `/market competitors <url>`. Vous identifiez les concurrents, analysez leurs stratégies marketing et produisez un rapport de comparaison complet qui révèle les lacunes de positionnement, les tactiques à adopter et les opportunités de différenciation. Tout le contenu généré doit être rédigé en français et adapté au contexte du marché européen. Les prix sont exprimés en euros (€) avec mention HT/TTC. La sortie est structurée pour la prise de décision stratégique et les présentations clients.

## Déclenchement de cette compétence

L'utilisateur exécute `/market competitors <url>`. Récupérez le site cible, identifiez les concurrents, analysez chacun d'eux et produisez un COMPETITOR-REPORT.md avec une intelligence actionnable. Tout le contenu doit être rédigé en français.

---

## Phase 1 : Identification des Concurrents

### 1.1 Catégories de Concurrents

Identifiez les concurrents selon trois niveaux :

| Catégorie | Définition | Comment les Trouver | Nombre |
|-----------|-----------|---------------------|--------|
| **Concurrents Directs** | Même produit, même audience, même marché | Cherchez les mots-clés de la catégorie de produit, vérifiez qui se classe | 3 à 5 |
| **Concurrents Indirects** | Produit différent, même problème résolu | Cherchez le problème résolu, vérifiez les approches alternatives | 2 à 3 |
| **Concurrents Aspirationnels** | Leaders du marché que la marque aspire à devenir | Leaders du secteur, créateurs de catégories, marques bien connues | 1 à 2 |

### 1.2 Méthodes de Découverte des Concurrents

Utilisez plusieurs méthodes pour identifier les concurrents :

**Méthode 1 : Découverte par Mots-Clés**
- Recherchez les mots-clés principaux du site cible (en français en priorité)
- Notez quelles entreprises se classent en page 1
- Recherchez "[catégorie de produit] logiciel/service/outil"
- Recherchez "[marque cible] alternatives"
- Recherchez "[marque cible] vs" et "meilleur [catégorie] France"

**Méthode 2 : Découverte par Site**
- Cherchez les pages de comparaison sur le site cible
- Vérifiez les liens de pied de page vers les associations du secteur
- Cherchez les pages "intégrations" qui mentionnent des outils similaires
- Vérifiez le blog du site cible pour les mentions de concurrents

**Méthode 3 : Découverte par Plateformes d'Avis (Priorité Marché Européen)**

Pour le marché français et européen, utilisez en priorité :
- **Trustpilot** — très populaire en France et Europe, forte crédibilité auprès des consommateurs
- **Avis Vérifiés** — certifié NF ISO 20488, référence française pour l'e-commerce, label reconnu
- **Google Reviews** — omniprésent, impact direct sur le référencement local
- **G2** — référence internationale pour le SaaS B2B, base d'avis importante
- **Capterra** — référence pour les logiciels d'entreprise, bon pour le B2B
- **Reddit** (subreddits francophones : r/France, r/Entrepreneur, r/french) — opinions authentiques

Notez les concurrents les mieux notés dans la même catégorie. Consultez les fonctionnalités "Comparer" sur les sites d'avis.

**Méthode 4 : Découverte Sociale et Communautaire**
- Recherchez sur Reddit (r/France, r/Entrepreneur) "[catégorie de produit] recommandations"
- Vérifiez Twitter/X pour les conversations sur la catégorie de produit
- Regardez LinkedIn pour les entreprises suivies par l'audience cible
- Consultez les forums francophones pertinents au secteur
- Vérifiez les groupes Facebook et LinkedIn en français du secteur

### 1.3 Collecte Automatisée de Données

Utilisez le script Python à `scripts/competitor_scanner.py` pour la collecte automatisée de données quand disponible :

```
python scripts/competitor_scanner.py --url [url-concurrent] --output json
```

Le script peut collecter :
- Contenu de la page d'accueil et métadonnées
- Données de la page de tarification (si publiques)
- Nombre d'articles de blog et sujets récents
- Liens de profils de réseaux sociaux et nombre d'abonnés
- Détection de la pile technologique
- Métriques de vitesse de page

Si le script n'est pas disponible, utilisez `WebFetch` pour collecter manuellement ces données pour chaque concurrent.

---

## Phase 2 : Cadre d'Analyse Concurrentielle

### 2.1 Analyse du Site Web et de la Messagerie

Pour chaque concurrent, analysez :

**Messagerie (en documentant en français) :**
| Élément | Ce qu'il Faut Capturer | Pourquoi C'est Important |
|---------|----------------------|--------------------------|
| **Titre** | Texte H1 exact | Révèle le positionnement et la proposition de valeur |
| **Sous-titre** | Texte de soutien | Montre l'angle de messagerie secondaire |
| **Proposition de valeur** | Promesse principale | Identifie le territoire de positionnement |
| **Public cible** | À qui ils s'adressent | Révèle la focalisation sur le segment de marché |
| **Différenciateur clé** | Ce qui les distingue | Montre les revendications de fossé concurrentiel |
| **Ton de voix** | Décontracté/formel/technique | Révèle les choix de personnalité de marque |
| **Preuve sociale** | Type et quantité | Montre la stratégie de crédibilité |
| **Conformité RGPD visible** | Bannière cookies, politique confidentialité | Indique le niveau de maturité légale de l'entreprise |

**Carte de Positionnement :**
Tracez chaque concurrent sur deux axes :
- Axe X : Simplicité perçue ←→ Puissance perçue
- Axe Y : Accessibilité perçue ←→ Premium perçu

```
CARTE DE POSITIONNEMENT
========================
                    PREMIUM
                       |
                       |
        [Concurrent C] |  [Aspirationnel]
                       |
SIMPLE ─────────────────┼────────────── PUISSANT
                       |
        [Cible]        |  [Concurrent A]
                       |
                       |
                    ACCESSIBLE
```

Adaptez les axes selon ce qui compte le plus dans le secteur spécifique.

### 2.2 Comparaison des Prix

Construisez une matrice de tarification détaillée. Tous les prix doivent être en euros (€) avec indication HT/TTC et mention de la TVA applicable :

```markdown
| Fonctionnalité/Offre | [Cible] | Concurrent A | Concurrent B | Concurrent C |
|---------------------|---------|-------------|-------------|-------------|
| Offre Gratuite | Oui/Non | Oui/Non | Oui/Non | Oui/Non |
| Prix Débutant (HT) | X €/mois HT | X €/mois HT | X €/mois HT | X €/mois HT |
| Prix Débutant (TTC) | X €/mois TTC | X €/mois TTC | X €/mois TTC | X €/mois TTC |
| Prix Pro (HT) | X €/mois HT | X €/mois HT | X €/mois HT | X €/mois HT |
| Entreprise | Sur devis | Sur devis | X €/mois HT | Sur devis |
| Essai Gratuit | X jours | X jours | X jours | X jours |
| Remise Annuelle | X% | X% | X% | X% |
| Prix Par Utilisateur | Oui/Non | Oui/Non | Oui/Non | Oui/Non |
| Limites d'Utilisation | [détail] | [détail] | [détail] | [détail] |
| TVA (20% France) | Précisé ? | Précisé ? | Précisé ? | Précisé ? |
```

**Évaluation de la Stratégie de Tarification :**
- La cible est-elle positionnée au-dessus, en dessous ou dans la moyenne du marché ?
- La tarification est-elle transparente ou cachée (nécessitant des appels commerciaux) ?
- Quel modèle de tarification est utilisé (par utilisateur, par usage, forfait, niveaux) ?
- Des tactiques d'ancrage de prix sont-elles utilisées ?
- La page de tarification communique-t-elle la valeur avant de montrer les chiffres ?
- Les prix sont-ils clairement indiqués HT et TTC (TVA 20% en France) — obligation légale ?

### 2.3 Matrice de Comparaison des Fonctionnalités

Construisez une comparaison complète des fonctionnalités. Documentez en français :

```markdown
| Catégorie | Fonctionnalité | [Cible] | Conc. A | Conc. B | Conc. C |
|-----------|---------------|---------|---------|---------|---------|
| Core | [Fonctionnalité 1] | Complète | Complète | Partielle | Non |
| Core | [Fonctionnalité 2] | Complète | Complète | Complète | Complète |
| Core | [Fonctionnalité 3] | Partielle | Complète | Non | Complète |
| Avancé | [Fonctionnalité 4] | Non | Complète | Non | Complète |
| Avancé | [Fonctionnalité 5] | Complète | Non | Complète | Non |
| Intégration | [Fonctionnalité 6] | Complète | Complète | Non | Partielle |
| Support | [Fonctionnalité 7] | Complète | Partielle | Complète | Complète |
| Conformité | RGPD / Hébergement UE | [statut] | [statut] | [statut] | [statut] |
```

Utilisez : Complète, Partielle, Non ou Bêta pour catégoriser.

Mettez en évidence :
- Les fonctionnalités où la cible a un avantage (fossés concurrentiels)
- Les fonctionnalités où la cible a un manque (vulnérabilité)
- Les fonctionnalités uniques à un concurrent (différenciateurs potentiels)
- La conformité RGPD et l'hébergement UE comme différenciateur potentiel sur le marché européen

### 2.4 Analyse de la Concurrence SEO

Pour chaque concurrent, analysez :

**Stratégie de Contenu :**
| Métrique | [Cible] | Conc. A | Conc. B | Conc. C |
|---------|---------|---------|---------|---------|
| Articles de blog (estimé) | X | X | X | X |
| Fréquence de publication | X/semaine | X/semaine | X/semaine | X/semaine |
| Profondeur du contenu | Superficiel/Moyen/Profond | | | |
| Types de contenu | Blog/Vidéo/Podcast | | | |
| Contenu en français ? | Oui/Non/Partiel | | | |
| Sujets clés | [liste] | [liste] | [liste] | [liste] |

**Stratégie de Mots-Clés :**
- Quels mots-clés (en français et en anglais) chaque concurrent cible-t-il clairement ?
- Où plusieurs concurrents se classent-ils mais pas la cible ? (lacunes de contenu)
- Les concurrents créent-ils du contenu de comparaison/alternatives ?
- Pour quels mots-clés à longue traîne en français les concurrents se classent-ils ?

**Analyse des Lacunes de Contenu :**
Listez les sujets que les concurrents couvrent mais pas la cible :
```
LACUNES DE CONTENU (Les Concurrents Couvrent, la Cible Ne Couvre Pas) :
  1. [Sujet] — couvert par Conc. A, B (forte intention de recherche en France)
  2. [Sujet] — couvert par Conc. A, C (intention moyenne)
  3. [Sujet] — couvert par Conc. B (forte intention de recherche)
  4. [Sujet] — couvert par tous les concurrents (lacune critique)
```

### 2.5 Comparaison de la Présence sur les Réseaux Sociaux

| Plateforme | [Cible] | Conc. A | Conc. B | Conc. C |
|-----------|---------|---------|---------|---------|
| Abonnés LinkedIn | X | X | X | X |
| Abonnés Twitter/X | X | X | X | X |
| Abonnés Instagram | X | X | X | X |
| Abonnés YouTube | X | X | X | X |
| Abonnés TikTok | X | X | X | X |
| Fréquence de publication | X/semaine | X/semaine | X/semaine | X/semaine |
| Taux d'engagement | X% | X% | X% | X% |
| Type de contenu principal | [type] | [type] | [type] | [type] |
| Langue du contenu | FR/EN/Mixte | | | |

### 2.6 Exploration des Avis Clients

Analysez les avis sur les plateformes tierces. Pour le marché européen, utilisez ces plateformes par ordre de priorité :

**Plateformes d'Avis Européennes (Priorité pour le Marché Français/Européen) :**

1. **Trustpilot** — très populaire en France et Europe, forte crédibilité auprès des consommateurs. Vérifiez la note globale, le nombre d'avis, la réactivité de l'entreprise.
2. **Avis Vérifiés** — certifié NF ISO 20488, référence française pour l'e-commerce. Avis vérifiés après achat, forte crédibilité pour les marchands en ligne.
3. **Google Reviews (Google Business Profile)** — omniprésent, impact direct sur le référencement local et la visibilité.
4. **G2** — référence internationale pour le SaaS B2B. Très consulté par les acheteurs logiciels professionnels.
5. **Capterra** — référence pour les logiciels d'entreprise. Fiches détaillées avec comparatifs.
6. **Reddit** (r/France, r/Entrepreneur, subreddits sectoriels francophones) — opinions authentiques et non filtrées.

**Pour chaque concurrent, extrayez :**
- Note globale (étoiles)
- Nombre d'avis (et tendance : en hausse ou en baisse ?)
- 3 principales fonctionnalités louées (ce que les clients adorent)
- 3 principales plaintes (ce que les clients détestent)
- Raisons courantes de changement (pourquoi les clients partent)
- Cas d'usage mentionnés le plus fréquemment
- Qualité du service client (délai de réponse aux avis négatifs)

**Matrice d'Intelligence des Avis :**
```markdown
| Concurrent | Trustpilot | Avis Vérifiés | G2 | Principales Louanges | Principale Plainte | Raison de Changement |
|-----------|-----------|--------------|-----|--------------------|--------------------|---------------------|
| Conc. A | 4,5/5 (500+) | 4,3/5 (200+) | 4,4/5 | Facile à utiliser | Intégrations limitées | Augmentation de prix |
| Conc. B | 4,2/5 (200+) | N/A | 4,1/5 | Fonctionnalités puissantes | Courbe d'apprentissage | Support médiocre |
| Conc. C | 3,8/5 (100+) | 3,9/5 (80+) | N/A | Bon rapport qualité-prix | Bogues | Meilleures alternatives |
```

---

## Phase 3 : Analyse SWOT

### 3.1 SWOT pour Chaque Concurrent

Pour chaque concurrent identifié, produisez une SWOT. Tout le contenu doit être rédigé en français :

```
CONCURRENT : [Nom]
URL : [url]

FORCES :
  - [Force spécifique avec preuve]
  - [Force spécifique avec preuve]
  - [Force spécifique avec preuve]

FAIBLESSES :
  - [Faiblesse spécifique avec preuve]
  - [Faiblesse spécifique avec preuve]
  - [Faiblesse spécifique avec preuve]

OPPORTUNITÉS (pour la cible à exploiter) :
  - [Opportunité basée sur la faiblesse du concurrent]
  - [Opportunité basée sur une lacune du marché européen]
  - [Opportunité basée sur un segment non servi]

MENACES (avantages concurrentiels à surveiller) :
  - [Menace avec impact potentiel]
  - [Menace avec impact potentiel]
  - [Menace avec impact potentiel]
```

### 3.2 SWOT Agrégée pour la Cible

Combinez toute l'intelligence concurrentielle en une seule SWOT pour la marque cible :

- **Forces :** Là où la cible surpasse tous ou la plupart des concurrents
- **Faiblesses :** Là où la cible est en retard sur tous ou la plupart des concurrents
- **Opportunités :** Lacunes du marché européen qu'aucun concurrent ne comble bien
- **Menaces :** Domaines où les concurrents sont significativement plus forts

---

## Phase 4 : Recommandations Stratégiques

### 4.1 Tactiques à Adopter

Identifiez des tactiques marketing spécifiques des concurrents valant la peine d'être adoptées. Tout le contenu doit être rédigé en français :

```
TACTIQUES À ADOPTER
====================

1. [Concurrent A] — [Tactique : ex. "Calculateur de ROI interactif en euros"]
   Pourquoi ça fonctionne : [explication]
   Comment l'implémenter : [étapes spécifiques pour la cible]
   Effort estimé : [Faible/Moyen/Élevé]
   Impact attendu : [Faible/Moyen/Élevé]

2. [Concurrent B] — [Tactique : ex. "Série de témoignages vidéo clients français"]
   Pourquoi ça fonctionne : [explication]
   Comment l'implémenter : [étapes spécifiques]
   Effort estimé : [Faible/Moyen/Élevé]
   Impact attendu : [Faible/Moyen/Élevé]

[Continuez pour 5 à 10 tactiques]
```

Concentrez-vous sur les tactiques qui sont :
- Prouvées (fonctionnant pour le concurrent sur le marché européen)
- Adaptables (peuvent être personnalisées pour la cible)
- Sous-utilisées (la cible ne le fait pas actuellement)

### 4.2 Stratégie de Différenciation Messagerie

En fonction de l'analyse concurrentielle, recommandez comment la cible devrait se différencier. Toutes les déclarations de positionnement en français :

**Cadre de Différenciation :**
1. **Catégorie :** La cible peut-elle créer ou posséder une sous-catégorie ? (ex. "le [attribut spécifique] [catégorie]")
2. **Audience :** La cible peut-elle posséder un segment d'audience spécifique ignoré par les concurrents ?
3. **Fonctionnalité :** Y a-t-il une fonctionnalité ou capacité unique qu'aucun concurrent n'offre ?
4. **Philosophie :** La cible peut-elle se différencier sur les valeurs, l'approche ou la méthodologie ?
5. **Expérience :** La cible peut-elle se différencier sur l'expérience client, le support ou la communauté ?
6. **Conformité RGPD :** Sur le marché européen, la conformité RGPD et l'hébergement des données en Europe peuvent être un différenciateur fort.

Pour chaque angle de différenciation viable, fournissez en français :
- Déclaration de positionnement
- Recommandation de titre
- Preuves ou points d'appui
- Comment cela se manifesterait sur le site web

### 4.3 Stratégie de Pages Alternatives

Recommandez la création de pages "[Concurrent] Alternative" pour capter le trafic à forte intention :

**Pour chaque concurrent majeur, définissez :**
```
PAGE : [Marque Cible] vs [Nom du Concurrent]
URL : /vs/[nom-concurrent] ou /alternatives/[nom-concurrent]

Titre : "Vous cherchez une alternative à [Concurrent] ? Voici pourquoi [X] équipes
ont choisi [Cible] à la place."

Sections (tout en français) :
  1. Tableau de comparaison rapide (fonctionnalités, tarification en €, notes)
  2. Où [Cible] gagne (3 à 4 avantages avec preuves)
  3. Où [Concurrent] gagne (honnête, renforce la confiance)
  4. Pour qui [Cible] est le mieux adapté (profil client idéal)
  5. Témoignages de migration (témoignages de clients ayant changé)
  6. Guide de migration ou offre de changement
  7. FAQ sur le changement
  8. CTA : "Essayez [Cible] gratuitement" ou "Voir comment [Cible] se compare"
```

**Valeur SEO :** Ces pages ciblent des requêtes de recherche à forte intention comme "[concurrent] alternatives" et "[cible] vs [concurrent]" — recherches en bas du tunnel de vente.

### 4.4 Développement du Récit de Transition

Créez un récit convaincant en français pour les clients envisageant de passer de chaque concurrent :

```
RÉCIT DE TRANSITION : [Concurrent] → [Cible]

Pourquoi les clients changent :
  1. [Raison principale basée sur l'exploration des avis Trustpilot/Avis Vérifiés]
  2. [Raison secondaire]
  3. [Raison tertiaire]

Modèle d'histoire de transition (en français) :
  "Comme beaucoup de [audience], [nom du client] a commencé avec [Concurrent] parce que
   [attrait initial]. Mais après [durée/événement], ils ont réalisé [point douloureux].
   Après être passé à [Cible], ils [résultat spécifique avec chiffres en euros]."

Offre de transition :
  - Assistance à la migration gratuite
  - Essai prolongé pour les utilisateurs de [Concurrent]
  - Correspondance ou réduction de prix (indiquer HT/TTC)
  - Onboarding dédié pour les nouveaux clients
```

---

## Phase 5 : Surveillance et Intelligence Continue

### 5.1 Liste de Vérification de Surveillance Concurrentielle

Recommandez des activités de surveillance continue :

- [ ] Configurer des Google Alertes pour chaque nom de concurrent (en français et en anglais)
- [ ] Suivre les concurrents sur les réseaux sociaux (LinkedIn, Twitter/X, Instagram)
- [ ] S'abonner aux newsletters des concurrents
- [ ] Vérifier les pages de tarification des concurrents mensuellement (noter les changements HT/TTC)
- [ ] Surveiller Trustpilot et Avis Vérifiés mensuellement — plateformes clés pour la France
- [ ] Surveiller G2 et Capterra trimestriellement pour le SaaS B2B
- [ ] Surveiller Google Reviews trimestriellement
- [ ] Suivre la publication de contenu des concurrents (sujets, fréquence, langue)
- [ ] Surveiller les lancements de produits et mises à jour des fonctionnalités des concurrents
- [ ] Surveiller les offres d'emploi des concurrents (révèle les priorités stratégiques)
- [ ] Suivre les dépenses publicitaires et créatifs des concurrents (Meta Ad Library, Google Ads Transparency)
- [ ] Examiner les profils de backlinks des concurrents trimestriellement
- [ ] Surveiller les forums francophones et Reddit (r/France, r/Entrepreneur) pour les mentions

### 5.2 Guide de Réponse Concurrentielle

Fournissez des conseils sur la façon de répondre aux mouvements des concurrents. Tout en français :

| Mouvement du Concurrent | Stratégie de Réponse | Délai |
|------------------------|---------------------|-------|
| Réduction de prix | Mettre en avant la valeur et la qualité, pas de guerre des prix | 1 semaine |
| Lancement d'une nouvelle fonctionnalité | Évaluer la pertinence, communiquer la feuille de route aux clients | 2 semaines |
| Campagne publicitaire agressive | Doubler les canaux propriétaires et la fidélisation | En cours |
| Contenu de comparaison négatif | Créer un contenu de comparaison factuel et équilibré | 1 semaine |
| Financement majeur / acquisition | Rassurer les clients, mettre en avant la stabilité et la concentration | 1 à 2 jours |
| Mauvais avis clients (Trustpilot, Avis Vérifiés) | Répondre publiquement et professionnellement, surveiller les opportunités | En cours |
| Changement de prix sans annonce | Documenter, analyser l'impact sur le positionnement | 3 à 5 jours |

---

## Format de Sortie : COMPETITOR-REPORT.md

Rédigez la sortie complète dans `COMPETITOR-REPORT.md`. Tout le contenu doit être rédigé en français :

```markdown
# Rapport d'Intelligence Concurrentielle : [Marque Cible]
**URL :** [url]
**Date :** [date actuelle]
**Concurrents Analysés :** [nombre]
**Marché :** France / Europe
**Position Concurrentielle : [Forte/Moyenne/Faible]**

---

## Synthèse Exécutive
[3 à 4 paragraphes couvrant le paysage concurrentiel sur le marché européen, la position de la cible,
le plus grand avantage concurrentiel, la plus grande menace concurrentielle et
les 3 recommandations stratégiques principales]

---

## Vue d'Ensemble des Concurrents

### Concurrents Directs
[Tableau récapitulatif avec nom, URL, positionnement, tarification en € HT/TTC, différenciateur clé]

### Concurrents Indirects
[Tableau récapitulatif]

### Concurrents Aspirationnels
[Tableau récapitulatif]

---

## Profils Détaillés des Concurrents

### [Nom du Concurrent A]
[Analyse complète : messagerie, tarification en € HT/TTC, fonctionnalités, SWOT,
présence sociale, avis (Trustpilot, Avis Vérifiés, Google Reviews, G2, Capterra)]

### [Nom du Concurrent B]
[Analyse complète]

[Répétez pour chaque concurrent]

---

## Tableaux de Comparaison

### Comparaison des Fonctionnalités
[Matrice complète des fonctionnalités, incluant conformité RGPD/hébergement UE]

### Comparaison des Prix
[Matrice complète des tarifications en euros, HT et TTC (TVA 20% France)]

### Notes des Avis Européens
[Matrice d'intelligence des avis — Trustpilot, Avis Vérifiés, Google Reviews, G2, Capterra]

### Présence sur les Réseaux Sociaux
[Tableau de comparaison des plateformes, avec langue du contenu]

---

## Carte de Positionnement
[Carte de positionnement visuelle avec explication]

---

## Analyse des Lacunes de Contenu et SEO
[Lacunes de contenu en français, opportunités de mots-clés, stratégie de pages de comparaison]

---

## Analyse SWOT — [Marque Cible]
[SWOT agrégée basée sur l'intelligence concurrentielle du marché européen]

---

## Recommandations Stratégiques

### Tactiques à Adopter
[5 à 10 tactiques avec guide d'implémentation, en français]

### Stratégie de Différenciation
[Angles de positionnement recommandés, déclarations en français]

### Pages Alternatives à Créer
[Pages de comparaison avec concurrents et plans, contenu en français]

### Récits de Transition
[Histoires de transition et offres pour chaque concurrent majeur, en français]

---

## Plan de Surveillance Concurrentielle
[Liste de vérification de surveillance continue et guide de réponse, incluant plateformes européennes]

---

## Prochaines Étapes
1. [Action concurrentielle la plus critique]
2. [Deuxième priorité]
3. [Troisième priorité]
```

---

## Sortie Terminal

Tout le contenu doit être rédigé en français :

```
=== RAPPORT D'INTELLIGENCE CONCURRENTIELLE ===

Cible : [nom]
Marché : France / Europe
Concurrents Analysés : [nombre]
Position Concurrentielle : [Forte/Moyenne/Faible]

Paysage Concurrentiel :
  Directs :        [Conc. A] (Trustpilot : X/5), [Conc. B] (Trustpilot : X/5)
  Indirects :      [Conc. C], [Conc. D]
  Aspirationnel : [Conc. E]

Principales Conclusions :
  Plus Grand Avantage : [avantage spécifique]
  Plus Grande Menace : [menace spécifique]
  Plus Grande Opportunité : [opportunité sur le marché européen]

Lacunes de Fonctionnalités : [X] fonctionnalités que les concurrents ont et pas la cible
Lacunes de Contenu : [X] sujets que les concurrents couvrent et pas la cible
Position Tarifaire : [Au-dessus/Dans/En dessous] de la moyenne du marché (en €)

Sources d'Avis Consultées : Trustpilot, Avis Vérifiés, Google Reviews, G2, Capterra

Top 3 Actions :
  1. [action]
  2. [action]
  3. [action]

Rapport complet enregistré dans : COMPETITOR-REPORT.md
```

---

## Intégration Inter-Compétences

- Si `MARKETING-AUDIT.md` existe, référencez les scores de positionnement concurrentiel
- Si `COPY-SUGGESTIONS.md` existe, utilisez l'analyse de messagerie pour la différenciation
- Si `FUNNEL-ANALYSIS.md` existe, comparez l'efficacité du tunnel avec les concurrents
- Si `AD-CAMPAIGNS.md` existe, utilisez l'intelligence concurrentielle pour les angles publicitaires
- Suggérez les étapes suivantes : `/market copy` pour une messagerie différenciée, `/market ads` pour des campagnes publicitaires concurrentielles, `/market funnel` pour la comparaison des tunnels de conversion
