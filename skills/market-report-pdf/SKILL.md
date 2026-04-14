# Générateur de Rapport Marketing PDF

## Objectif de la Compétence
Générer un rapport marketing PDF professionnel et visuellement soigné en utilisant le script Python `scripts/generate_pdf_report.py`. Cette compétence collecte toutes les données d'audit et d'analyse disponibles, les structure dans le format JSON attendu, invoque le script et produit un PDF branded avec des jauges de score, des graphiques à barres, des tableaux comparatifs, des conclusions et un plan d'action priorisé. Tout le contenu doit être rédigé en français et adapté aux marchés européens.

## Quand l'Utiliser
- L'utilisateur veut une version PDF du rapport marketing (pas seulement Markdown)
- L'utilisateur prépare un livrable pour une présentation client
- L'utilisateur demande un "rapport soigné", un "rapport prêt pour le client" ou un "rapport PDF"
- L'utilisateur veut un rapport visuel avec graphiques et scores
- Déclenché par `/market report-pdf` ou `/market report-pdf <domaine>`

## Choisir PDF vs Markdown

| Format | Idéal Pour | Avantages | Inconvénients |
|---|---|---|---|
| **PDF** | Présentations clients, pièces jointes email, supports commerciaux | Apparence professionnelle, formatage cohérent, graphiques visuels, imprimable | Plus difficile à modifier, nécessite le script Python |
| **Markdown** | Usage interne, référence rapide, édition itérative, contrôle de version | Facile à modifier, lisible dans tout éditeur, compatible git | Moins soigné visuellement, pas de graphiques |

**Règle pratique :** Si le rapport va à un client ou prospect, utilisez le PDF. Pour un usage interne ou édition ultérieure, utilisez Markdown.

## Comment Exécuter

### Étape 1 : Collecter Toutes les Données Disponibles
Rassemblez les données de toutes les exécutions de compétences précédentes. Recherchez ces fichiers dans le répertoire du projet :

**Sources de données principales :**
- `MARKETING-AUDIT.md` — Résultats de l'audit global
- `LANDING-CRO.md` — Analyse de conversion de la page d'atterrissage
- `SEO-AUDIT.md` — Conclusions SEO
- `BRAND-VOICE.md` — Analyse de la voix de marque
- `COMPETITOR-ANALYSIS.md` — Données de comparaison concurrentielle
- `FUNNEL-ANALYSIS.md` — Analyse du tunnel de vente
- `SOCIAL-AUDIT.md` — Audit réseaux sociaux
- `EMAIL-AUDIT.md` — Audit email marketing
- `AD-AUDIT.md` — Audit publicitaire

**Si aucune donnée préalable n'existe :**
1. Recommandez à l'utilisateur de lancer d'abord `/market audit <url>` pour les meilleurs résultats
2. Si l'utilisateur insiste pour générer un rapport sans audits préalables, analysez directement l'URL fournie et construisez la structure de données depuis zéro
3. Utilisez le script analyze_page.py pour collecter les données automatisées : `python scripts/analyze_page.py <url>`

### Étape 2 : Construire la Structure de Données JSON
Le script `scripts/generate_pdf_report.py` attend un fichier JSON en entrée avec cette structure exacte :

```json
{
  "url": "https://exemple.fr",
  "date": "12 avril 2026",
  "brand_name": "Exemple SAS",
  "overall_score": 62,
  "executive_summary": "Résumé en 2-4 phrases de la santé marketing globale, des principales opportunités et de l'impact estimé sur le CA de la mise en œuvre des recommandations.",
  "categories": {
    "Contenu & Messages": {
      "score": 68,
      "weight": "25%"
    },
    "Optimisation de la Conversion": {
      "score": 52,
      "weight": "20%"
    },
    "SEO & Découvrabilité": {
      "score": 74,
      "weight": "20%"
    },
    "Positionnement Concurrentiel": {
      "score": 48,
      "weight": "15%"
    },
    "Marque & Confiance": {
      "score": 70,
      "weight": "10%"
    },
    "Croissance & Stratégie": {
      "score": 55,
      "weight": "10%"
    }
  },
  "findings": [
    {
      "severity": "Critique",
      "finding": "Description de la conclusion la plus importante"
    },
    {
      "severity": "Élevé",
      "finding": "Description d'une conclusion haute priorité"
    },
    {
      "severity": "Moyen",
      "finding": "Description d'une conclusion priorité moyenne"
    },
    {
      "severity": "Faible",
      "finding": "Description d'une conclusion de priorité moindre"
    }
  ],
  "quick_wins": [
    "Premier gain rapide actionnable",
    "Deuxième gain rapide actionnable",
    "Troisième gain rapide actionnable"
  ],
  "medium_term": [
    "Première action à moyen terme",
    "Deuxième action à moyen terme",
    "Troisième action à moyen terme"
  ],
  "strategic": [
    "Première action stratégique",
    "Deuxième action stratégique",
    "Troisième action stratégique"
  ],
  "competitors": [
    {
      "name": "Concurrent A",
      "positioning": "Leur positionnement sur le marché",
      "pricing": "Leur modèle tarifaire (en €)",
      "social_proof": "Leurs signaux de confiance",
      "content": "Leur approche de contenu"
    },
    {
      "name": "Concurrent B",
      "positioning": "Leur positionnement sur le marché",
      "pricing": "Leur modèle tarifaire (en €)",
      "social_proof": "Leurs signaux de confiance",
      "content": "Leur approche de contenu"
    }
  ]
}
```

### Étape 3 : Guide d'Assemblage des Données Champ par Champ

#### `url` (chaîne, obligatoire)
L'URL cible du site web. Utilisez l'URL complète avec le protocole.

#### `date` (chaîne, obligatoire)
La date de génération du rapport. Format : "JJ mois AAAA" (ex : "12 avril 2026").

#### `brand_name` (chaîne, obligatoire)
Le nom de l'entreprise ou de la marque. Utilisé dans les en-têtes du tableau de comparaison concurrentielle.

#### `overall_score` (entier, 0-100, obligatoire)
La moyenne pondérée de tous les scores de catégories. Calculez comme suit :
```
overall_score = (contenu * 0,25) + (conversion * 0,20) + (seo * 0,20) + (concurrent * 0,15) + (marque * 0,10) + (croissance * 0,10)
```

#### `executive_summary` (chaîne, obligatoire)
Un résumé en 2-4 phrases couvrant :
- Évaluation de la santé marketing actuelle
- 1 à 2 conclusions les plus impactantes
- Impact estimé sur le CA de la mise en œuvre des recommandations
- Première étape recommandée

Gardez-le concis et percutant. Il apparaît sur la page de couverture juste sous la jauge de score.

#### `categories` (objet, obligatoire)
Exactement 6 catégories avec leurs scores. Les catégories correspondent à ces domaines d'évaluation :

| Catégorie | Ce qu'elle Mesure | Guide de Notation |
|---|---|---|
| Contenu & Messages | Qualité du copywriting, proposition de valeur, clarté des titres, texte des CTA, cohérence de la voix de marque | 80+ : Clair, axé sur les bénéfices, spécifique. 60-79 : Adéquat mais générique. <60 : Vague, centré sur les fonctionnalités, peu clair |
| Optimisation de la Conversion | Preuve sociale, design des formulaires, placement des CTA, traitement des objections, urgence, conformité RGPD | 80+ : Plusieurs types de preuve, formulaires optimisés, CTA clairs. 60-79 : Certains éléments présents. <60 : Éléments critiques manquants |
| SEO & Découvrabilité | Balises title, méta-descriptions, titres, schema, maillage interne, vitesse de page, hreflang, conformité RGPD | 80+ : Entièrement optimisé. 60-79 : Principalement présent avec lacunes. <60 : Problèmes majeurs ou éléments manquants |
| Positionnement Concurrentiel | Différenciation, clarté tarifaire, contenu de comparaison, conscience du marché | 80+ : Positionnement clair, pages de comparaison existantes. 60-79 : Quelque différenciation. <60 : Pas de positionnement clair |
| Marque & Confiance | Qualité du design, badges de confiance, signaux de sécurité, apparence professionnelle, signaux RGPD | 80+ : Design moderne, signaux de confiance partout. 60-79 : Design adéquat. <60 : Dépassé ou non professionnel |
| Croissance & Stratégie | Capture de leads, email marketing, stratégie de contenu, canaux d'acquisition, conformité RGPD comme avantage | 80+ : Stratégie multicanal en place. 60-79 : Certains canaux actifs. <60 : Pas de stratégie de croissance claire |

#### `findings` (tableau, obligatoire)
Un tableau d'objets de conclusions, chacun avec les champs `severity` (gravité) et `finding` (conclusion).

**Niveaux de gravité :**
- `Critique` — Perd directement du CA ou des clients. À corriger immédiatement.
- `Élevé` — Impact significatif sur la croissance. À corriger en 1-2 semaines.
- `Moyen` — Opportunité d'amélioration significative. À corriger en 1 mois.
- `Faible` — Amélioration souhaitable. À corriger quand les ressources le permettent.

**Rédiger des conclusions efficaces :**
- Soyez spécifique : "Le titre de la page d'accueil dit 'Bienvenue sur notre plateforme'" pas "Le titre nécessite une amélioration"
- Quantifiez l'impact : "Méta-descriptions absentes sur 8 des 12 pages d'atterrissage"
- Référencez les benchmarks : "Le temps de chargement est de 4,2s (benchmark : moins de 2s)"
- Incluez des preuves : "Aucun témoignage trouvé sur la page d'accueil, la page tarifs ou la page d'inscription"
- Mentionnez les problèmes RGPD : "Bannière cookies non conforme au RGPD — le refus n'est pas aussi accessible que l'acceptation"

Visez 5 à 10 conclusions. Ordonnez de la plus grave à la moins grave.

#### `quick_wins` (tableau, obligatoire)
3 à 5 actions pouvant être mises en œuvre en une semaine avec un effort minimal. Chacune doit être une instruction spécifique et actionnable.

**Bon gain rapide :** "Réécrire le titre de la page d'accueil de 'Bienvenue sur notre plateforme' en 'Réduisez votre temps de reporting de 75% — Analyses automatisées pour les équipes de croissance'"

**Mauvais gain rapide :** "Améliorer le titre" (trop vague)

#### `medium_term` (tableau, obligatoire)
3 à 5 actions nécessitant 1 à 3 mois de mise en œuvre. Plus élaborées mais à fort impact.

#### `strategic` (tableau, obligatoire)
3 à 5 actions nécessitant 3 à 6 mois. Ce sont des changements fondamentaux nécessitant planification et effort soutenu.

#### `competitors` (tableau, optionnel)
Jusqu'à 3 objets concurrents pour le tableau de comparaison. Si aucune donnée concurrentielle n'est disponible, omettez ce champ — le script sautera la section concurrentielle.

### Étape 4 : Écrire le Fichier JSON
Sauvegardez les données assemblées dans un fichier JSON temporaire :

```bash
# Écrire les données JSON dans un fichier temporaire
cat > /tmp/report_data.json << 'JSONEOF'
{
  ... données JSON assemblées ...
}
JSONEOF
```

### Étape 5 : Invoquer le Script Générateur PDF

**Vérification des prérequis :**
Vérifiez d'abord que `reportlab` est installé :
```bash
python3 -c "import reportlab" 2>/dev/null || pip3 install reportlab
```

**Générer le rapport :**
```bash
python3 scripts/generate_pdf_report.py /tmp/report_data.json "RAPPORT-MARKETING-<domaine>.pdf"
```

Remplacez `<domaine>` par le nom de domaine du site cible (sans protocole ni www), en utilisant des tirets à la place des points. Par exemple :
- `exemple.fr` devient `RAPPORT-MARKETING-exemple-fr.pdf`
- `monapplication.io` devient `RAPPORT-MARKETING-monapplication-io.pdf`

**Mode démo (sans arguments) :**
Exécuter le script sans arguments génère un rapport exemple avec des données fictives :
```bash
python3 scripts/generate_pdf_report.py
# Crée : RAPPORT-MARKETING-sample.pdf
```

### Étape 6 : Vérifier la Sortie
Après génération, vérifiez que le PDF a été créé :
```bash
ls -la "RAPPORT-MARKETING-<domaine>.pdf"
```

Communiquez le chemin du fichier et sa taille à l'utilisateur.

### Étape 7 : Nettoyage
Supprimez le fichier JSON temporaire :
```bash
rm /tmp/report_data.json
```

## Contenu du Rapport PDF

Le PDF généré comprend les pages suivantes :

### Page 1 : Page de Couverture
- Titre du rapport : "Rapport d'Audit Marketing"
- URL cible
- Date de génération
- Jauge de score global (visualisation circulaire avec code couleur)
- Lettre de note (A+ à F)
- Résumé exécutif

### Page 2 : Détail des Scores
- Graphique à barres horizontales montrant les 6 scores de catégories avec code couleur
- Tableau des scores avec noms de catégories, scores, poids et labels de statut
- Code couleur : Vert (80+), Bleu (60-79), Jaune (40-59), Rouge (<40)

### Page 3 : Conclusions Clés
- Tableau des conclusions avec labels de gravité et descriptions
- Indicateurs de gravité codés par couleur (Critique = rouge, Élevé = orange, Moyen = jaune, Faible = bleu)
- Conclusions ordonnées de la plus grave à la moins grave

### Page 4 : Plan d'Action Priorisé
- Section Gains Rapides (Cette Semaine)
- Section Moyen Terme (1-3 Mois)
- Section Stratégique (3-6 Mois)
- Actions numérotées dans chaque niveau

### Page 5 : Paysage Concurrentiel (si données concurrentielles fournies)
- Tableau de comparaison client vs jusqu'à 3 concurrents
- Lignes : Positionnement, Tarification (€), Preuve Sociale, Contenu

### Dernière Page : Méthodologie
- Explication de la méthodologie de notation
- Poids des catégories et critères de mesure
- Pied de page : "Généré par la Suite Marketing IA pour Claude Code"

## Palette de Couleurs

Le PDF utilise une palette de couleurs professionnelle :

| Élément | Couleur | Code Hex |
|---|---|---|
| Principal (en-têtes, titres) | Bleu Marine Foncé | #1B2A4A |
| Accent (liens, surlignages) | Bleu | #2D5BFF |
| Mise en valeur (attention) | Orange | #FF6B35 |
| Succès (scores élevés) | Vert | #00C853 |
| Avertissement (scores moyens) | Ambre | #FFB300 |
| Danger (scores faibles, critique) | Rouge | #FF1744 |
| Fond clair | Gris Clair | #F5F7FA |
| Texte principal | Gris Foncé | #2C3E50 |
| Texte secondaire | Gris Moyen | #7F8C9B |
| Bordures | Bordure Claire | #E0E6ED |

## Correspondance Score-Couleur
- 80-100 : Vert (#00C853) — Performance forte
- 60-79 : Bleu (#2D5BFF) — Solide avec marge de progression
- 40-59 : Ambre (#FFB300) — Nécessite de l'attention
- 0-39 : Rouge (#FF1744) — Problèmes critiques

## Dépannage

| Problème | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'reportlab'` | Exécutez `pip3 install reportlab` |
| Le script produit un PDF vide | Vérifiez que les données JSON ont tous les champs obligatoires |
| La jauge de score ne s'affiche pas | Assurez-vous que `overall_score` est un nombre entre 0 et 100 |
| Tableau des concurrents absent | Assurez-vous que le tableau `competitors` a des objets avec les champs `name`, `positioning`, `pricing`, `social_proof`, `content` |
| Le PDF ne fait qu'une page | Vérifiez les erreurs de parsing JSON — exécutez `python3 -c "import json; json.load(open('/tmp/report_data.json'))"` |
| Les polices semblent incorrectes | Le script utilise Helvetica (intégré à reportlab). Pas de polices personnalisées nécessaires. |

## Intégration avec les Autres Compétences

Cette compétence fonctionne mieux combinée avec d'autres compétences d'audit. Le flux de travail recommandé :

1. Exécutez `/market audit <url>` — Génère des données d'audit complètes
2. Exécutez `/market competitors <url>` — Ajoute des données de comparaison concurrentielle
3. Exécutez `/market seo <url>` — Ajoute des conclusions SEO détaillées
4. Exécutez `/market landing <url>` — Ajoute l'analyse CRO
5. Exécutez `/market report-pdf <url>` — Compile tout dans un PDF

La compétence de rapport PDF cherchera automatiquement les fichiers de sortie de ces compétences et incorporera leurs données dans le JSON du rapport.

## Sortie
- **Fichier :** `RAPPORT-MARKETING-<domaine>.pdf`
- **Emplacement :** Répertoire racine du projet
- **Taille :** Typiquement 200Ko-500Ko selon le volume de contenu
- **Pages :** 5-7 pages selon que les données concurrentielles et sections supplémentaires sont incluses

## Principes Clés
- Le rapport PDF est le livrable le plus orienté client de la boîte à outils. La qualité est primordiale.
- Vérifiez toujours que les données JSON sont complètes et exactes avant de générer. Des données de mauvaise qualité donnent des résultats de mauvaise qualité.
- Utilisez le PDF pour les premières impressions clients et les conversations commerciales. Faites le suivi avec le rapport Markdown plus détaillé si le client s'engage.
- Chaque score doit être justifiable. Si un client demande "pourquoi j'ai obtenu 52 en Optimisation de la Conversion ?", les conclusions doivent fournir des preuves claires.
- Arrondissez les scores à des nombres entiers. Les décimales impliquent une fausse précision.
- Gardez le résumé exécutif concis — 2-4 phrases maximum. Les clients parcourent les pages de couverture.
- Si vous générez pour un prospect (pas encore client), le rapport sert d'outil commercial. Rendez les opportunités convaincantes et le plan d'action réalisable.
- Utilisez toujours l'euro (€) avec le formatage français des nombres : "32 500€/mois" pas "$32,500/month".
- Intégrez les mentions de conformité RGPD dans les conclusions pertinentes.
