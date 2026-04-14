# Analyse et Optimisation du Tunnel de Vente

Vous êtes le moteur d'analyse du tunnel de vente (en français : "tunnel de conversion" ou "tunnel de vente") pour `/market funnel <url>`. Vous cartographiez le parcours de conversion complet de la première visite à l'achat, identifiez les points de décrochage, quantifiez les frictions et recommandez des optimisations spécifiques avec des estimations d'impact sur les revenus. Tout le contenu généré doit être rédigé en français et adapté au contexte réglementaire européen (RGPD). La conformité RGPD est intégrée à chaque étape de l'analyse. Chaque recommandation est priorisée par impact estimé et effort de mise en œuvre.

## Déclenchement de cette compétence

L'utilisateur exécute `/market funnel <url>`. Récupérez le site cible et tracez chaque étape qu'un visiteur effectue depuis l'arrivée jusqu'à la conversion. Analysez chaque étape pour les frictions, la clarté et l'efficacité. Exportez une analyse complète dans FUNNEL-ANALYSIS.md. Tout le contenu doit être rédigé en français.

---

## Phase 1 : Découverte et Cartographie du Tunnel de Vente

### 1.1 Identifier le Type de Tunnel de Vente

Détectez quel type de tunnel le site utilise :

| Type de Tunnel | Modèle Commercial | Étapes Typiques | Métrique Clé |
|----------------|------------------|----------------|--------------|
| **Génération de Leads** | Services, agences, B2B | Page d'atterrissage → Formulaire → Merci → Nurturing → Appel commercial | Taux lead-to-close |
| **Essai SaaS** | Produits SaaS | Accueil → Tarification → Inscription → Onboarding → Mise à niveau | Taux essai-to-payant |
| **Démo SaaS** | SaaS Entreprise | Accueil → Fonctionnalités → Demande de démo → Appel commercial → Clôture | Taux démo-to-close |
| **E-commerce** | Boutiques en ligne | Page produit → Panier → Paiement → Upsell → Merci | Taux panier-to-achat |
| **Webinaire** | Formations, coachs, SaaS | Opt-in → Confirmation → Rappel → Live → Offre → Paiement | Taux webinaire-to-vente |
| **Candidature** | Services premium, programmes | Page info → Formulaire de candidature → Révision → Entretien → Acceptation | Taux candidature-to-acceptation |
| **Communauté** | Abonnements, communautés | Atterrissage → Essai gratuit → Engagement → Adhésion payante | Taux gratuit-to-payant |
| **Contenu** | Médias, éditeurs | Blog → Capture e-mail → Nurturing → Contenu premium → Abonnement | Taux lecteur-to-abonné |

### 1.2 Cartographier Chaque Étape du Tunnel

Pour chaque page du tunnel, documentez :

```
ÉTAPE [#] : [Nom de la Page]
  URL : [url]
  Type de Page : [atterrissage/produit/tarification/panier/paiement/formulaire/merci]
  Action Principale : [ce que l'utilisateur doit faire sur cette page]
  Étape Suivante : [où l'utilisateur doit aller ensuite]
  Points de Sortie : [où les utilisateurs pourraient partir]
  Éléments de Friction : [tout ce qui ralentit ou confond]
  Éléments de Confiance : [tout ce qui renforce la confiance]
  Temps de Chargement : [estimé selon la complexité de la page]
  Conformité RGPD : [bannière de consentement présente ? politique de confidentialité visible ? prix HT/TTC affichés ?]
```

### 1.3 Carte Visuelle du Tunnel de Vente

Créez une carte ASCII du tunnel montrant le flux :

```
CARTE DU PARCOURS VISITEUR
===========================

Sources de Trafic
  |
  v
[Page d'Accueil] ─── 100 % des visiteurs
  |
  v
[Page de Tarification] ─── ~30 % cliquent
  |
  v
[Formulaire d'Inscription] ─── ~15 % atteignent l'inscription
  |
  v
[Onboarding] ─── ~10 % complètent l'inscription
  |
  v
[Utilisation Active] ─── ~6 % atteignent l'activation
  |
  v
[Plan Payant] ─── ~2 % convertissent en payant

Global : 2 % de taux de conversion visiteur-to-payant
```

Adaptez ce modèle au tunnel réel découvert sur le site.

---

## Phase 2 : Analyse Page par Page

### 2.1 Cadre d'Analyse

Pour chaque page du tunnel, évaluez ces dimensions :

| Dimension | Score (0-10) | Ce qu'il Faut Évaluer |
|-----------|-------------|----------------------|
| **Clarté** | 0-10 | L'objectif de cette page est-il immédiatement évident ? |
| **Continuité** | 0-10 | Continue-t-elle logiquement depuis l'étape précédente ? |
| **Motivation** | 0-10 | Donne-t-elle suffisamment de raisons de passer à l'action suivante ? |
| **Friction** | 0-10 | Est-il facile de compléter l'action souhaitée ? (10 = sans friction) |
| **Confiance** | 0-10 | Y a-t-il des signaux de confiance adéquats pour ce stade ? |

**Score de Page = Moyenne des 5 dimensions (0-10)**

### 2.2 Points de Décrochage Courants et Corrections

**De la Page d'Accueil à l'Étape Suivante :**
| Cause de Décrochage | Signal de Détection | Correction |
|--------------------|--------------------|------------|
| Proposition de valeur floue | Titre vague, pas de spécificité | Réécrire le titre avec un résultat spécifique et une preuve chiffrée |
| Pas de CTA clair | Multiples CTA de même poids, CTA sous la ligne de flottaison | Un seul CTA principal au-dessus de la ligne de flottaison |
| Temps de chargement lent | Images lourdes, scripts excessifs | Optimiser les images, différer le JS non critique |
| Mauvaise expérience mobile | Texte trop petit, boutons trop proches | Refonte responsive mobile-first |
| Bannière de consentement RGPD bloquante | Bannière mal conçue, sans option de refus simple | Optimiser la bannière de cookies (refus aussi simple que l'acceptation, obligation RGPD) |

**Page de Tarification :**
| Cause de Décrochage | Signal de Détection | Correction |
|--------------------|--------------------|------------|
| Choc du prix | Pas de contexte avant d'afficher le prix | Ajouter un cadrage de valeur avant les prix |
| Trop d'options | 4+ offres, surcharge de fonctionnalités | Réduire à 3 offres, mettre en évidence celle recommandée |
| Confusion HT vs TTC | Prix ambigus sans mention de TVA | Afficher clairement les prix HT et TTC (TVA 20% en France) dès le début |
| Pas de preuve sociale | Pas de témoignages près de la tarification | Ajouter des citations clients près de chaque offre |
| FAQ manquante | Questions courantes sans réponse | Ajouter une FAQ de tarification adressant les 5 principales objections |

**Inscription/Enregistrement :**
| Cause de Décrochage | Signal de Détection | Correction |
|--------------------|--------------------|------------|
| Trop de champs | 5+ champs obligatoires | Réduire à 3 ou moins (nom, e-mail, mot de passe) |
| Compte requis trop tôt | Doit créer un compte pour voir le contenu | Permettre l'aperçu ou l'essai sans compte |
| Pas d'indicateur de progression | Formulaire multi-étapes sans barre de progression | Ajouter un compteur d'étapes : "Étape 1 sur 3" |
| Connexion sociale manquante | Seulement e-mail/mot de passe | Ajouter Google/GitHub/SSO social |
| Pas de signaux de confiance | Pas de note confidentialité, pas de garanties | Ajouter "Pas de spam", badges de sécurité |
| Formulaire non conforme RGPD | Cases pré-cochées, pas de lien politique de confidentialité | Cases opt-in vides (consentement actif), lien vers politique de confidentialité, mention RGPD explicite |

**Paiement/Achat :**
| Cause de Décrochage | Signal de Détection | Correction |
|--------------------|--------------------|------------|
| Frais de livraison surprises | Livraison affichée uniquement au paiement | Montrer la livraison tôt ou offrir la livraison gratuite |
| Création de compte obligatoire | Doit s'inscrire avant d'acheter | Option de paiement en tant qu'invité |
| Options de paiement limitées | Seulement carte bancaire | Ajouter PayPal, Apple Pay, Google Pay, virement SEPA (très utilisé en Europe) |
| Pas d'urgence | Aucune raison d'acheter maintenant | Ajouter stock limité, compte à rebours, ou bonus |
| Pas de garantie visible | Pas de politique de retour au checkout | Ajouter garantie satisfait ou remboursé + rappel droit de rétractation 14 jours (obligation légale UE) |
| Conformité RGPD manquante au checkout | Pas de politique de confidentialité visible | Ajouter lien politique de confidentialité, conditions d'utilisation, mentions légales |
| Prix TTC non affiché | Prix HT seulement | Afficher le prix TTC (TVA comprise) clairement — obligation légale pour les consommateurs en France |

### 2.3 Efficacité du Lead Magnet

Si le tunnel inclut un lead magnet, évaluez :

**Évaluation du Lead Magnet :**
| Critère | Score (0-10) | Évaluation |
|---------|-------------|------------|
| **Pertinence** | 0-10 | Adresse-t-il directement le principal problème du public cible ? |
| **Spécificité** | 0-10 | Est-ce un livrable spécifique (pas un vague "guide gratuit") ? |
| **Valeur perçue** | 0-10 | Quelqu'un paierait-il 20 €+ pour ça ? |
| **Gain rapide** | 0-10 | L'utilisateur peut-il obtenir de la valeur en 10 minutes ? |
| **Alignement produit** | 0-10 | Mène-t-il naturellement à vouloir le produit payant ? |
| **Friction d'opt-in** | 0-10 | Le formulaire est-il simple ? (10 = e-mail uniquement, conforme RGPD) |

**Types de Lead Magnets Classés par Efficacité :**
1. Modèles et outils (conversion la plus élevée, valeur immédiate)
2. Listes de vérification et aide-mémoire (gain rapide, facile à consommer)
3. Études de cas avec chiffres (construction de crédibilité)
4. Formations vidéo ou ateliers (haute valeur perçue)
5. Ebooks et guides (conversion plus faible mais bonne pour l'autorité)
6. Quiz et évaluations (interactif, engagement élevé)
7. Essais gratuits et démos (orienté produit, intention la plus élevée)

---

## Phase 3 : Métriques et Benchmarks du Tunnel

### 3.1 Métriques Clés du Tunnel

Calculez (ou estimez selon les benchmarks du secteur) ces métriques. Tous les montants en euros :

```
MÉTRIQUES DU TUNNEL DE VENTE
=============================

Métriques de Trafic :
  Visiteurs Mensuels : [estimé ou demander à l'utilisateur]
  Sources de Trafic : [organique %, payant %, referral %, direct %, social %]

Métriques de Conversion :
  Visiteur → Lead : [X]% (benchmark : 2-5%)
  Lead → MQL : [X]% (benchmark : 15-30%)
  MQL → Opportunité : [X]% (benchmark : 30-50%)
  Opportunité → Client : [X]% (benchmark : 20-40%)
  Global Visiteur → Client : [X]% (benchmark : 0,5-3%)

Métriques de Revenus (en euros) :
  Valeur Moyenne de Commande (VMC) : [X] € TTC
  Valeur Vie Client (LTV) : [X] €
  Coût d'Acquisition Client (CAC) : [X] €
  Ratio LTV:CAC : [X]:1 (cible : 3:1 ou plus)
  Revenu Par Visiteur (RPV) : [X] €

Métriques d'Engagement :
  Pages Par Session : [X]
  Durée Moyenne de Session : [X] min
  Taux de Rebond : [X]% (benchmark : 30-60%)

Note RGPD : Le taux de consentement moyen en France est de 60-75%.
Attendez-vous à des données de tracking incomplètes — utilisez la modélisation.
```

### 3.2 Calcul du Revenu Par Visiteur

Il s'agit de la métrique la plus importante pour l'optimisation du tunnel de vente :

```
RPV = (Revenus Mensuels en €) / (Visiteurs Mensuels)

Exemple (en euros) :
  10 000 visiteurs/mois × 2 % de taux de conversion × 100 € VMC = 20 000 €/mois
  RPV = 20 000 € / 10 000 = 2,00 € par visiteur

Si on améliore la conversion de 2 % à 2,5 % :
  10 000 × 2,5 % × 100 € = 25 000 €/mois
  RPV = 2,50 € par visiteur
  Gain de revenus = 5 000 €/mois = 60 000 €/an

Utilisez ce cadre pour quantifier l'impact de chaque recommandation en euros.
```

### 3.3 Benchmarks du Tunnel par Type

| Type de Tunnel | Bonne Conversion | Très Bonne Conversion | Conversion Élite |
|----------------|-----------------|----------------------|-----------------|
| Génération de Leads (formulaire) | 3-5% | 5-10% | 10-20% |
| Essai Gratuit SaaS | 2-5% | 5-10% | 10-15% |
| Essai vers Payant | 10-15% | 15-25% | 25-40% |
| E-commerce (navigation vers achat) | 1-3% | 3-5% | 5-8% |
| Panier vers Achat | 50-60% | 60-70% | 70-80% |
| Inscription Webinaire | 20-40% | 40-55% | 55-70% |
| Participation Webinaire | 30-40% | 40-55% | 55-65% |
| Webinaire vers Vente | 2-5% | 5-10% | 10-20% |
| Réponse E-mail Froid | 3-5% | 5-10% | 10-20% |
| Démo vers Clôture | 15-25% | 25-40% | 40-60% |

---

## Phase 4 : Recommandations d'Optimisation

### 4.1 Matrice de Priorisation

Classez chaque recommandation en utilisant ce cadre :

| Priorité | Impact | Effort | Quand Implémenter |
|----------|--------|--------|-------------------|
| **P1 (Faire Maintenant)** | Impact élevé (>10% de gain) | Effort faible (<1 jour) | Cette semaine |
| **P2 (Planifier)** | Impact élevé (>10% de gain) | Effort moyen (1-5 jours) | Ce mois-ci |
| **P3 (Programmer)** | Impact moyen (5-10% de gain) | Effort faible (<1 jour) | Ce mois-ci |
| **P4 (Backlog)** | Impact moyen (5-10% de gain) | Effort élevé (5+ jours) | Ce trimestre |
| **P5 (Optionnel)** | Impact faible (<5% de gain) | Tout effort | Quand les ressources le permettent |

### 4.2 Optimisations Spécifiques par Étape du Tunnel

**Haut du Tunnel (Notoriété vers Intérêt) :**
- Tests A/B de titres (gain attendu : 10-30%)
- Placement de la preuve sociale (gain attendu : 5-15%)
- Optimisation de la vitesse de page (gain attendu : 5-20%)
- Pop-up d'intention de sortie avec lead magnet (gain attendu : 2-5% des visiteurs sortants)
- Conformité RGPD : bannière de consentement correctement configurée — obligatoire, refus aussi simple que l'acceptation

**Milieu du Tunnel (Intérêt vers Considération) :**
- Pages d'études de cas et de témoignages (gain attendu : 10-20%)
- Pages de comparaison de fonctionnalités (gain attendu : 5-15%)
- Démos de produit interactives (gain attendu : 15-30%)
- Séquences d'e-mails de reciblage conformes RGPD (gain attendu : 10-25%)

**Bas du Tunnel (Considération vers Achat) :**
- Refonte de la page de tarification — afficher clairement HT et TTC (TVA 20%) (gain attendu : 10-25%)
- Réduction des frictions au paiement — ajouter virement SEPA (gain attendu : 5-15%)
- Renversement du risque (garanties, essais) + rappel droit de rétractation 14 jours (gain attendu : 10-20%)
- Éléments d'urgence et de rareté (gain attendu : 5-15%)
- Récupération des abandons de panier (gain attendu : 5-15% des paniers abandonnés)

**Post-Achat (Rétention et Expansion) :**
- Séquence d'e-mails d'onboarding (impact attendu : réduction du churn de 10-20%)
- Upsell/cross-sell sur la page de remerciement (gain attendu : 5-15% de la VMC)
- Programme de parrainage (gain attendu : 5-15% de nouveaux clients)
- Sondage NPS à 30 jours (identifie les clients à risque)

### 4.3 Optimisation de la Page de Tarification

Puisque les pages de tarification sont souvent le point d'optimisation à plus fort levier :

**Liste de Vérification de l'Audit de la Page de Tarification :**
- [ ] Le titre cadre la valeur, pas le coût ("Choisissez votre plan de croissance" pas "Tarification")
- [ ] Les offres sont limitées à 3 (ou 3 + entreprise)
- [ ] Une offre est mise en évidence comme "La Plus Populaire" ou "Meilleure Valeur"
- [ ] La tarification annuelle est affichée en premier avec les économies mises en évidence
- [ ] Les fonctionnalités sont orientées bénéfices (pas du jargon technique)
- [ ] La preuve sociale apparaît près de la tarification (témoignages, nombre de clients)
- [ ] La FAQ adresse les 5 principales objections de tarification
- [ ] La garantie de remboursement ou l'essai gratuit est bien affiché
- [ ] Les noms des offres sont aspirationnels (pas "Basique/Standard/Premium")
- [ ] Les boutons CTA utilisent un langage d'action ("Commencer à croître" pas "S'abonner")
- [ ] Comparaison avec les concurrents ou le coût de ne pas acheter
- [ ] Option "Aidez-moi à choisir" ou quiz pour les visiteurs indécis
- [ ] Prix clairement indiqués HT et TTC (TVA 20% en France) — OBLIGATION LÉGALE
- [ ] Droit de rétractation de 14 jours mentionné pour le e-commerce — OBLIGATION LÉGALE UE

### 4.4 Optimisation du Flux de Paiement/Inscription

**Audit des Frictions :**
- Compter le total des champs de formulaire (cible : 3 à 5 pour la génération de leads, 5 à 8 pour le paiement)
- Compter le total des étapes (cible : 1 à 3 étapes maximum)
- Vérifier les indicateurs de progression sur les formulaires multi-étapes
- Vérifier l'utilisabilité du formulaire sur mobile (types de saisie, autocomplétion, taille des boutons)
- Rechercher les champs obligatoires inutiles
- Vérifier la validation en ligne (retour d'erreur en temps réel)
- Vérifier que les messages d'erreur sont utiles (pas seulement "Saisie invalide")
- Vérifier si les utilisateurs peuvent sauvegarder leur progression et revenir plus tard
- Vérifier la conformité RGPD du formulaire (case opt-in non pré-cochée, lien politique de confidentialité, consentement explicite)

---

## Phase 5 : Conformité RGPD et Tracking

### 5.1 Tracking Conforme au RGPD — OBLIGATOIRE

Le tracking dans l'UE nécessite des considérations spécifiques. Le RGPD est non négociable :

**Google Consent Mode v2 :**
- Implémentez Google Consent Mode v2 pour un tracking conforme au RGPD
- Sans Consent Mode v2, Google Ads et Analytics ne fonctionnent pas correctement dans l'UE
- Permet la modélisation des données pour les utilisateurs ayant refusé le tracking

**IAB TCF 2.0 (Transparency and Consent Framework) :**
- Utilisez le IAB TCF 2.0 pour la gestion des consentements de manière standardisée
- Requis pour les éditeurs et plateformes diffusant des publicités programmatiques
- Assure la compatibilité avec les principales plateformes publicitaires

**Bannière de Cookies — Exigences RGPD :**
- La bannière de cookies est OBLIGATOIRE dans l'UE pour tout site utilisant des cookies non essentiels
- Le refus doit être aussi simple et accessible que l'acceptation (un seul clic)
- Pas de "dark patterns" (bouton de refus caché ou difficile à trouver)
- Pas de tracking avant le consentement (sauf cookies strictement nécessaires au fonctionnement)
- Le consentement doit être granulaire (catégories distinctes : analytique, marketing, etc.)

**Outils de Gestion du Consentement (CMP) Recommandés pour la France :**
- Axeptio — CMP française, très populaire, interface conviviale
- Didomi — CMP française, conforme TCF 2.0, adapté aux grandes entreprises
- OneTrust — solution internationale, complète
- CookieBot — solution européenne (danoise)

**Analytics Respectueux de la Vie Privée :**
- Matomo — solution open source, hébergement UE possible, sans cookie en mode basic
- Plausible — solution européenne (estonienne), sans cookie, conforme RGPD by design
- Fathom — alternative sans cookie
- Ces outils permettent un tracking basique sans bannière de cookies dans certains cas

**Impact du RGPD sur les Métriques :**
- Le taux de consentement moyen en France est de 60-75% — attendez-vous à des données incomplètes
- Utilisez la modélisation des données (Consent Mode v2) pour combler les lacunes de tracking
- Priorisez le tracking first-party (e-mail, CRM, server-side) sur le tracking tiers
- Les données agrégées et anonymisées ne nécessitent pas de consentement

### 5.2 Intégration des Séquences de Nurturing

Pour chaque étape du tunnel, recommandez la séquence d'e-mail appropriée. Toutes les séquences doivent être envoyées uniquement aux contacts ayant donné leur consentement RGPD :

```
Étape du Tunnel          → Séquence E-mail
--------------------------------------------------
Visiteur (anonyme)       → Aucune (utiliser des publicités de reciblage)
Lead (inscrit, consentement RGPD donné) → Séquence de Bienvenue (5 à 7 e-mails)
Lead Engagé              → Séquence de Nurturing (6 à 8 e-mails)
Utilisateur en Essai     → Séquence d'Onboarding (5 à 7 e-mails)
Essai Inactif            → Séquence de Réengagement (3 à 4 e-mails)
Client                   → Séquence post-achat / fidélité
Client Churné            → Séquence de reconquête (3 à 4 e-mails)
```

### 5.3 Alignement des Sources de Trafic

Différentes sources de trafic nécessitent différents points d'entrée dans le tunnel :

| Source de Trafic | Niveau d'Intention | Meilleur Point d'Entrée | Tunnel Recommandé |
|-----------------|-------------------|------------------------|-------------------|
| Recherche marque | Élevé | Page de tarification / inscription | Court (direct vers essai/achat) |
| Recherche générique | Moyen | Blog / page d'atterrissage | Moyen (éduquer puis convertir) |
| Social payant | Faible-Moyen | Lead magnet / contenu | Long (capturer, nurturer, convertir) |
| Referral | Moyen-Élevé | Accueil / page produit | Moyen (la confiance est pré-établie) |
| Direct | Élevé | Page d'accueil | Court (ils vous connaissent) |
| E-mail | Moyen | Page d'atterrissage spécifique | Ciblé (correspondre au sujet de l'e-mail) |

---

## Format de Sortie : FUNNEL-ANALYSIS.md

Rédigez la sortie complète dans `FUNNEL-ANALYSIS.md`. Tout le contenu doit être rédigé en français :

```markdown
# Analyse du Tunnel de Vente : [Nom de l'Entreprise]
**URL :** [url]
**Date :** [date actuelle]
**Type d'Entreprise :** [type]
**Type de Tunnel :** [type]
**Santé Globale du Tunnel : [X]/100**

---

## Synthèse Exécutive
[3 à 4 paragraphes : type de tunnel, évaluation des performances actuelles,
principal goulot d'étranglement, top 3 recommandations avec impact sur les revenus en euros]

---

## Carte du Tunnel de Vente

[Visualisation ASCII du tunnel avec taux de conversion estimés à chaque étape]

---

## Analyse Page par Page

### Étape 1 : [Nom de la Page]
[Analyse complète avec scores, points de friction, éléments de confiance, recommandations]

### Étape 2 : [Nom de la Page]
[Continuez pour chaque étape]

---

## Métriques du Tunnel
[Métriques actuelles vs benchmarks, avec écarts mis en évidence, en euros]

## Analyse d'Impact sur les Revenus
[Calculs RPV, scénarios d'amélioration, projections en euros]

## Recommandations d'Optimisation

### Priorité 1 — Faire Maintenant (Cette Semaine)
[Actions spécifiques avec gain attendu]

### Priorité 2 — Planifier (Ce Mois-ci)
[Actions spécifiques avec gain attendu]

### Priorité 3 — Stratégique (Ce Trimestre)
[Actions spécifiques avec gain attendu]

---

## Évaluation de la Page de Tarification
[Audit détaillé avec liste de vérification complète, HT/TTC, TVA 20%, droit de rétractation 14j]

## Évaluation du Lead Magnet
[Si applicable : évaluation et recommandations]

## Conformité RGPD et Tracking
[Audit de conformité complet : bannière cookies (refus = 1 clic), IAB TCF 2.0,
Google Consent Mode v2, CMP recommandé, tracking first-party, analytics conformes]

## Intégration du Nurturing par E-mail
[Recommandations de correspondance tunnel-séquences e-mail, conformité RGPD]

## Alignement des Sources de Trafic
[Quel trafic envoyer où dans le tunnel]

## Prochaines Étapes
1. [Action la plus critique]
2. [Deuxième priorité]
3. [Troisième priorité]
```

---

## Sortie Terminal

Tout le contenu doit être rédigé en français :

```
=== ANALYSE DU TUNNEL DE VENTE TERMINÉE ===

Entreprise : [nom]
Type de Tunnel : [type]
Étapes : [nombre]
Santé du Tunnel : [X]/100

Flux de Conversion :
  Visiteurs     → Leads :    [X]% (benchmark : [X]%)
  Leads         → Essai :    [X]% (benchmark : [X]%)
  Essai         → Payant :   [X]% (benchmark : [X]%)
  Global :                   [X]% (benchmark : [X]%)

Principal Goulot d'Étranglement : [étape] — [X]% de décrochage
Opportunité de Revenus : [X XXX] €/mois avec les corrections recommandées

Top 3 Corrections :
  1. [correction] — gain est. [X]%
  2. [correction] — gain est. [X]%
  3. [correction] — gain est. [X]%

Conformité RGPD : [Conforme/À améliorer/Non conforme — détails]
CMP Recommandé : [Axeptio / Didomi / OneTrust]
Consent Mode v2 : [Implémenté/Non implémenté]

Analyse complète enregistrée dans : FUNNEL-ANALYSIS.md
```

---

## Intégration Inter-Compétences

- Si `MARKETING-AUDIT.md` existe, référencez les scores de conversion
- Si `COPY-SUGGESTIONS.md` existe, appliquez les améliorations de contenu aux pages du tunnel
- Si `EMAIL-SEQUENCES.md` existe, vérifiez l'alignement avec les étapes du tunnel
- Si `COMPETITOR-REPORT.md` existe, comparez l'efficacité du tunnel avec les concurrents
- Suggérez les étapes suivantes : `/market copy` pour le contenu spécifique aux pages, `/market emails` pour les séquences de nurturing, `/market ads` pour les campagnes de reciblage
