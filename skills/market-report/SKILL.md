# Générateur de Rapport Marketing (Format Markdown)

## Objectif de la Compétence
Générer un rapport marketing complet et professionnellement formaté en Markdown. Cette compétence compile les données de tous les audits et analyses précédents en un document unique prêt pour le client, avec des scores, des conclusions, des recommandations et un plan d'action priorisé avec des estimations d'impact sur le chiffre d'affaires. Tout le contenu doit être rédigé en français et adapté aux marchés européens.

## Quand l'Utiliser
- L'utilisateur souhaite un rapport marketing complet pour un client ou sa propre entreprise
- L'utilisateur a complété une ou plusieurs compétences d'audit et veut un rapport compilé
- L'utilisateur demande une évaluation marketing, un tableau de bord ou un document d'analyse
- Déclenché par `/market report` ou `/market report <domaine>`

## Comment Exécuter

### Étape 1 : Collecter Toutes les Données Disponibles
Avant de générer le rapport, vérifiez les données d'audit existantes des exécutions précédentes. Recherchez ces fichiers dans le répertoire du projet :

**Sources de données possibles :**
- `MARKETING-AUDIT.md` — issu de `/market audit`
- `LANDING-CRO.md` — issu de `/market landing`
- `SEO-AUDIT.md` — issu de `/market seo`
- `BRAND-VOICE.md` — issu de `/market brand`
- `COMPETITOR-ANALYSIS.md` — issu de `/market competitors`
- `FUNNEL-ANALYSIS.md` — issu de `/market funnel`
- `CONTENT-AUDIT.md` — issu de l'analyse de contenu
- `AD-AUDIT.md` — issu de `/market ads`
- `SOCIAL-AUDIT.md` — issu de `/market social`
- `EMAIL-AUDIT.md` — issu de `/market emails`

Si aucune donnée préalable n'existe, informez l'utilisateur et proposez de :
1. Lancer d'abord un audit rapide (recommandé)
2. Générer un rapport basé sur les informations disponibles (URL du site, données fournies par l'utilisateur)
3. Créer un modèle de rapport à compléter

### Étape 2 : Calculer le Tableau de Bord Marketing

Notez 6 catégories, chacune sur 100 points. Le score global est la moyenne pondérée.

#### Catégorie 1 : Site Web & Conversion (Poids : 25%)
Évaluez sur la base de l'analyse de la page d'atterrissage, des conclusions CRO et de l'évaluation UX.

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Vitesse de chargement | 15 | Moins de 2s = 15, Moins de 3s = 10, Moins de 5s = 5, Plus de 5s = 0 |
| Réactivité mobile | 15 | Entièrement responsive = 15, Principalement = 10, Partiellement = 5, Non = 0 |
| Clarté de la proposition de valeur | 20 | Immédiatement claire = 20, Nécessite un effort = 12, Vague = 5, Absente = 0 |
| Efficacité des CTA | 20 | Fort et clair = 20, Présent mais faible = 12, Peu clair = 5, Absent = 0 |
| Preuve sociale | 15 | Plusieurs types = 15, Quelques-uns = 10, Minimal = 5, Aucun = 0 |
| Optimisation des formulaires | 15 | Optimisé = 15, Adéquat = 10, À améliorer = 5, Défaillant = 0 |

#### Catégorie 2 : SEO & Référencement Naturel (Poids : 20%)
Évaluez sur la base des conclusions de l'audit SEO.

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Balises title et méta-descriptions | 15 | Optimisées = 15, Présentes = 10, Partielles = 5, Absentes = 0 |
| Hiérarchie des titres (H1-H6) | 10 | Correcte = 10, Principalement = 7, À améliorer = 3, Absente = 0 |
| Qualité du contenu (E-E-A-T) | 25 | Excellent = 25, Bon = 17, Moyen = 10, Faible = 3 |
| SEO technique | 20 | Aucun problème = 20, Problèmes mineurs = 13, Problèmes majeurs = 7, Critique = 0 |
| Maillage interne | 15 | Stratégique = 15, Présent = 10, Minimal = 5, Aucun = 0 |
| Balisage Schema.org | 15 | Complet = 15, Basique = 10, Minimal = 5, Absent = 0 |

#### Catégorie 3 : Contenu & Messages (Poids : 15%)
Évaluez sur la base de l'analyse de la voix de marque et de l'audit de contenu.

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Cohérence de la voix de marque | 20 | Cohérente = 20, Principalement = 13, Incohérente = 7, Pas de voix = 0 |
| Qualité du contenu | 25 | Niveau expert = 25, Bon = 17, Générique = 10, Faible = 3 |
| Variété du contenu | 15 | Plusieurs formats = 15, Quelques-uns = 10, Limité = 5, Unique = 0 |
| Fréquence de publication | 15 | Cadence régulière = 15, Irrégulière = 10, Rare = 5, Aucune = 0 |
| Ciblage de l'audience | 25 | Précisément ciblé = 25, En partie = 17, Large = 10, Hors-cible = 3 |

#### Catégorie 4 : Réseaux Sociaux & Communauté (Poids : 15%)
Évaluez sur la base de la présence et de l'engagement sur les réseaux sociaux.

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Présence sur les plateformes | 15 | Bonnes plateformes, actif = 15, Présent mais inactif = 8, Manque clé = 3 |
| Qualité du contenu | 25 | Engageant et dans la charte = 25, Adéquat = 15, Faible qualité = 7, Mauvais = 0 |
| Taux d'engagement | 25 | Au-dessus du benchmark = 25, Dans la norme = 17, En dessous = 10, Négligeable = 3 |
| Régularité des publications | 15 | Planning régulier = 15, Irrégulier = 10, Rare = 5, Abandonné = 0 |
| Construction de communauté | 20 | Communauté active = 20, Quelques engagements = 13, Diffusion uniquement = 7, Aucune = 0 |

#### Catégorie 5 : Email & Automatisation (Poids : 15%)
Évaluez sur la base de l'évaluation de l'email marketing.

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Mécanisme de collecte de contacts | 20 | Plusieurs opt-ins = 20, Un opt-in = 13, Aucun opt-in visible = 5 |
| Design et contenu email | 20 | Professionnel et engageant = 20, Adéquat = 13, À améliorer = 7 |
| Séquences d'automatisation | 25 | Complètes = 25, Basiques = 15, Minimales = 8, Aucune = 0 |
| Segmentation | 20 | Avancée = 20, Basique = 13, Aucune = 5 |
| Signaux de délivrabilité | 15 | Forts = 15, Adéquats = 10, Préoccupants = 5, Problèmes = 0 |

#### Catégorie 6 : Référencement Payant / SEA (Poids : 10%)
Évaluez sur la base de l'audit du compte publicitaire (si applicable).

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Structure des campagnes | 20 | Bien organisée = 20, Adéquate = 13, Désordonnée = 7, Aucune = 0 |
| Qualité du ciblage | 25 | Précis et multicouche = 25, Bon = 17, Large = 10, Gaspilleur = 3 |
| Qualité des créatives publicitaires | 25 | Convaincant et varié = 25, Adéquat = 17, Faible = 10, Mauvais = 3 |
| Cohérence page d'atterrissage | 15 | Parfaitement alignée = 15, Bonne = 10, Mal alignée = 5, Défaillante = 0 |
| Tracking et attribution | 15 | Complets = 15, Basiques = 10, Minimaux = 5, Absents = 0 |

#### Calcul du Score Global
```
Score Global = (Site Web * 0,25) + (SEO * 0,20) + (Contenu * 0,15) + (Réseaux Sociaux * 0,15) + (Email * 0,15) + (SEA * 0,10)
```

**Interprétation des Scores :**
| Plage de Score | Note | Signification |
|---|---|---|
| 85-100 | Excellent | Le marketing est un avantage concurrentiel. Optimisez et amplifiez. |
| 70-84 | Bien | Base solide avec des opportunités d'amélioration clairement identifiées. |
| 55-69 | Moyen | Fonctionnel mais laissant une croissance significative sur la table. |
| 40-54 | Insuffisant | Plusieurs domaines nécessitent de l'attention. Coût d'opportunité élevé. |
| 0-39 | Critique | Le marketing freine activement la croissance. Action immédiate requise. |

### Étape 3 : Rédiger les Analyses Approfondies par Catégorie

Pour chacune des 6 catégories, fournissez :

1. **Score et Note** — X/100 avec interprétation
2. **Conclusions Clés** — 3-5 observations spécifiques avec preuves
3. **Ce qui Fonctionne** — Éléments positifs à préserver et développer
4. **Lacunes et Problèmes** — Problèmes identifiés avec niveaux de gravité
5. **Recommandations** — Améliorations spécifiques et actionnables classées par impact
6. **Estimation de l'Impact sur le CA** — Impact financier estimé de la mise en œuvre des recommandations

**Cadre d'Estimation de l'Impact sur le Chiffre d'Affaires :**
```
Impact = (Changement de trafic estimé * Changement du taux de conversion * Valeur moyenne du contrat) * Facteur de confiance

Exemple :
- Trafic mensuel actuel : 10 000
- Les améliorations SEO recommandées pourraient augmenter le trafic de 30% : +3 000 visites
- Taux de conversion actuel : 2%, le CRO pourrait améliorer à 3% : +1% = +130 conversions
- Valeur moyenne du contrat : 500€
- Impact mensuel estimé sur le CA : 65 000€
- Facteur de confiance (conservateur) : 0,5
- Estimation conservatrice : 32 500€/mois de CA supplémentaire
```

### Étape 4 : Résumé de la Comparaison Concurrentielle
Si des données concurrentielles sont disponibles via `/market competitors`, incluez :

**Matrice de Positionnement Concurrentiel :**
| Facteur | Client | Concurrent 1 | Concurrent 2 | Concurrent 3 |
|---|---|---|---|---|
| Qualité du Site Web | X/10 | X/10 | X/10 | X/10 |
| Visibilité SEO | X/10 | X/10 | X/10 | X/10 |
| Qualité du Contenu | X/10 | X/10 | X/10 | X/10 |
| Présence Réseaux Sociaux | X/10 | X/10 | X/10 | X/10 |
| Position Globale | X/4 | X/4 | X/4 | X/4 |

**Avantages Concurrentiels :** Ce que le client fait mieux
**Lacunes Concurrentielles :** Où les concurrents surpassent le client
**Opportunités :** Les espaces que les concurrents n'adressent pas

### Étape 5 : Évaluation de la Qualité du Contenu
Résumez les conclusions de contenu sur tous les canaux :

- **Texte du site web** — Clarté, caractère persuasif, alignement avec la marque
- **Contenu de blog** — Profondeur, expertise, optimisation SEO, cadence de publication
- **Contenu réseaux sociaux** — Qualité d'engagement, cohérence de marque, optimisation par plateforme
- **Contenu email** — Efficacité des objets, qualité du corps du texte, force des CTA
- **Créatives publicitaires** — Clarté des messages, qualité visuelle, présentation de l'offre

### Étape 6 : Résumé de l'Optimisation de la Conversion
Compilez toutes les conclusions liées à la conversion :

- **Tunnels de vente principaux** — Comment les visiteurs deviennent clients
- **Fuites du tunnel** — Où les clients potentiels abandonnent
- **Gains CRO rapides** — Changements pouvant être mis en œuvre immédiatement
- **Opportunités de test** — Tests A/B recommandés avec hypothèses
- **Comparaison aux benchmarks** — Taux actuels vs standards du secteur

### Étape 7 : Aperçu SEO
Résumez la santé SEO dans un format lisible rapidement :

```
Aperçu Santé SEO :
- Balises Title : [Optimisées / À améliorer / Absentes]
- Méta-descriptions : [Optimisées / À améliorer / Absentes]
- Balises H1 : [Correctes / Problèmes / Absentes]
- Texte Alt des Images : [Complet / Partiel / Absent]
- Vitesse de Page : [Rapide / Modérée / Lente]
- Compatible Mobile : [Oui / Partiellement / Non]
- Balisage Schema.org : [Présent / Partiel / Absent]
- Robots.txt : [Configuré / Problèmes / Absent]
- Sitemap : [Présent / Problèmes / Absent]
- HTTPS : [Oui / Non]
- Core Web Vitals : [Réussi / À améliorer / Échoué]
- Balises hreflang : [Présentes / Partielles / Absentes] (obligatoires pour les sites multilingues UE)
- Conformité RGPD : [Conforme / Partiellement / Non conforme]
```

### Étape 8 : Construire le Plan d'Action Priorisé

Organisez toutes les recommandations en trois niveaux :

#### Gains Rapides (À Mettre en Œuvre Cette Semaine)
Changements à fort impact et faible effort. Implémentables en 1 à 5 jours ouvrables.

Formatez chaque élément comme suit :
```
- [ ] [Action] : [Description spécifique]
  - Impact : [ÉLEVÉ/MOYEN/FAIBLE]
  - Effort : [1-5 heures]
  - Résultat Attendu : [Résultat spécifique]
  - Impact sur le CA : [X XXX€/mois estimé]
```

#### Moyen Terme (À Mettre en Œuvre Ce Mois)
Impact modéré, effort modéré. Ces éléments nécessitent 1 à 4 semaines.

#### Stratégique (À Mettre en Œuvre Ce Trimestre)
Fort impact, effort élevé. Ce sont des changements fondamentaux nécessitant planification et effort soutenu.

### Étape 9 : Construire la Feuille de Route 30-60-90 Jours

**Jours 1-30 : Fondations & Gains Rapides**
- Semaine 1 : Mettre en œuvre tous les gains rapides du plan d'action
- Semaine 2 : Mettre en place le tracking et la baseline analytique
- Semaine 3 : Commencer les améliorations à moyen terme
- Semaine 4 : Premier bilan de performance et ajustements

**Jours 31-60 : Croissance & Optimisation**
- Semaines 5-6 : Lancer les améliorations des campagnes principales
- Semaine 7 : Démarrage du programme de tests A/B
- Semaine 8 : Mise en œuvre de la stratégie de contenu

**Jours 61-90 : Amplification & Expansion**
- Semaines 9-10 : Amplifier ce qui fonctionne, éliminer ce qui ne fonctionne pas
- Semaine 11 : Expansion vers de nouveaux canaux ou campagnes
- Semaine 12 : Revue complète, actualisation de la stratégie pour le trimestre suivant

### Étape 10 : Annexe

Incluez des notes méthodologiques pour que le client comprenne comment les scores ont été dérivés :

**Méthodologie de Notation :**
- Comment chaque catégorie a été évaluée
- Sources de données utilisées
- Benchmarks référencés
- Limites et hypothèses
- Date de l'analyse

**Outils Utilisés :**
- Listez les outils ou scripts utilisés dans l'analyse
- Référence à scripts/analyze_page.py si utilisé

**Glossaire :**
- Définissez les termes marketing qu'un client non-technicien pourrait ne pas connaître
- Terminologie clé : tunnel de vente, taux de conversion, proposition de valeur, référencement naturel (SEO), référencement payant (SEA), réseaux sociaux, analyse concurrentielle

## Format de Sortie

Générez un fichier appelé `RAPPORT-MARKETING.md`. Tout le contenu doit être rédigé en français :

```markdown
# Rapport Marketing
## [Nom de l'Entreprise / Domaine]
### Préparé par : [Nom de l'Agent / Agence]
### Date : [Date]

---

## Résumé Exécutif

### Score Marketing Global : [X/100] — [Note]

[Résumé en 2-3 paragraphes couvrant : état actuel, top 3 des conclusions, impact estimé sur le CA de la mise en œuvre des recommandations, et premières étapes recommandées]

### Détail des Scores
| Catégorie | Score | Note |
|---|---|---|
| Site Web & Conversion | X/100 | [Note] |
| SEO & Référencement Naturel | X/100 | [Note] |
| Contenu & Messages | X/100 | [Note] |
| Réseaux Sociaux | X/100 | [Note] |
| Email & Automatisation | X/100 | [Note] |
| Référencement Payant (SEA) | X/100 | [Note] |
| **Global** | **X/100** | **[Note]** |

### Top 3 des Actions Prioritaires
1. [Recommandation la plus impactante avec estimation CA]
2. [Deuxième recommandation la plus impactante]
3. [Troisième recommandation la plus impactante]

---

## Analyse Détaillée

### 1. Site Web & Conversion [X/100]
[Analyse approfondie avec conclusions, ce qui fonctionne, lacunes, recommandations]

### 2. SEO & Référencement Naturel [X/100]
[Analyse approfondie]

### 3. Contenu & Messages [X/100]
[Analyse approfondie]

### 4. Réseaux Sociaux [X/100]
[Analyse approfondie]

### 5. Email & Automatisation [X/100]
[Analyse approfondie]

### 6. Référencement Payant (SEA) [X/100]
[Analyse approfondie]

---

## Comparaison Concurrentielle
[Matrice et analyse]

---

## Aperçu SEO
[Liste de contrôle de santé]

---

## Résumé de l'Optimisation de la Conversion
[Analyse du tunnel de vente et recommandations CRO]

---

## Récapitulatif de l'Impact sur le Chiffre d'Affaires
| Recommandation | Impact Mensuel Estimé | Confiance | Priorité |
|---|---|---|---|
| [Recommandation 1] | X XXX€ | Élevée/Moyenne/Faible | 1 |
| [Recommandation 2] | X XXX€ | Élevée/Moyenne/Faible | 2 |
| ... | ... | ... | ... |
| **Impact Total Estimé** | **XX XXX€/mois** | | |

---

## Plan d'Action Priorisé

### Gains Rapides (Cette Semaine)
- [ ] [Actions avec impact et effort]

### Moyen Terme (Ce Mois)
- [ ] [Actions]

### Stratégique (Ce Trimestre)
- [ ] [Actions]

---

## Feuille de Route 30-60-90 Jours
[Plan semaine par semaine]

---

## Annexe
### Méthodologie
### Outils Utilisés
### Glossaire
### Sources de Données
```

## Principes Clés
- Ce rapport doit être suffisamment impressionnant pour servir d'outil commercial. Un rapport marketing bien conçu peut ouvrir la porte à une mission client.
- Toujours mettre en avant les opportunités et perspectives de croissance, pas les critiques. Cadrez tout à travers le prisme du potentiel de croissance.
- Quantifiez tout ce qui est possible. "32 000€/mois de chiffre d'affaires non réalisé" est plus convaincant que "vous laissez de l'argent sur la table."
- Rendez le plan d'action si spécifique qu'on pourrait le confier à un junior qui pourrait l'exécuter.
- Utilisez un formatage professionnel : en-têtes cohérents, tableaux pour les données, cases à cocher pour les actions, hiérarchie visuelle claire.
- Si des données des compétences précédentes sont disponibles, référencez des conclusions spécifiques. Sinon, soyez transparent sur ce qui est basé sur l'analyse vs l'estimation.
- Le rapport doit raconter une histoire : voici où vous en êtes, voici où vous pourriez être, voici comment y arriver, et voici ce que ça vaut.
- Utilisez toujours l'euro (€) et le formatage français des nombres : "32 500€" pas "$32,500".
- Mentionnez la conformité RGPD comme facteur dans les recommandations pertinentes.
