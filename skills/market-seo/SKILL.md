# Audit SEO de Contenu

## Objectif de la Compétence
Réaliser un audit SEO complet d'une page web ou d'un site web, couvrant le SEO on-page, la qualité du contenu (E-E-A-T), l'analyse de mots-clés, le SEO technique et la stratégie de contenu. Cette compétence combine une analyse automatisée via `scripts/analyze_page.py` avec une revue manuelle de niveau expert pour produire un document d'audit SEO actionnable. Tout le contenu doit être rédigé en français et adapté aux marchés européens. Le référencement naturel (SEO) et le référencement payant (SEA) sont traités comme des leviers complémentaires.

## Quand l'Utiliser
- L'utilisateur fournit une URL et demande une analyse, un audit ou des recommandations SEO
- L'utilisateur veut améliorer ses classements en référencement naturel et son trafic organique
- L'utilisateur pose des questions sur le SEO on-page, les balises meta, la qualité du contenu ou le SEO technique
- L'utilisateur veut une analyse des lacunes de contenu ou des recommandations de stratégie de contenu
- Déclenché par `/market seo <url>` ou `/market seo`

## Comment Exécuter

### Étape 1 : Lancer l'Analyse Automatisée
Utilisez le script d'analyse Python pour collecter les données de base :

```bash
python3 scripts/analyze_page.py <url>
```

Ce script extrait :
- Balise title et méta-description
- Balises Open Graph
- Hiérarchie des titres (H1-H6)
- Liens (internes et externes)
- Images et statut du texte alt
- Formulaires et CTA
- Schema.org / données structurées
- Liens réseaux sociaux
- Scripts de tracking
- Balise meta viewport (indicateur de compatibilité mobile)
- Balise canonique
- Directives meta robots
- Balises hreflang (pour les sites multilingues UE)

Capturez la sortie JSON et utilisez-la comme base pour l'analyse manuelle.

### Étape 2 : Liste de Contrôle SEO On-Page
Évaluez chaque élément et notez-le : Réussi, À Améliorer ou Échoué.

#### Balise Title
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| Existe | Chaque page doit avoir une balise title unique | Réussi/Échoué |
| Longueur | 50-60 caractères (s'affiche complètement dans les SERPs) | Réussi/À Améliorer/Échoué |
| Mot-clé principal | Contient le mot-clé cible principal | Réussi/À Améliorer/Échoué |
| Position du mot-clé | Le mot-clé principal apparaît au début | Réussi/À Améliorer/Échoué |
| Nom de marque | Inclut le nom de la marque (généralement à la fin, séparé par un tiret ou une barre verticale) | Réussi/À Améliorer/Échoué |
| Unicité | Différent des autres pages du site | Réussi/Échoué |
| Attractivité | Un internaute voudrait-il cliquer dessus ? | Réussi/À Améliorer/Échoué |

**Erreurs courantes de balise title :**
- Trop longue (tronquée dans les résultats de recherche)
- Mot-clé principal absent
- Bourrage de mots-clés ("Meilleur Logiciel CRM | Top CRM | Logiciel CRM | Plateforme CRM")
- Même title sur plusieurs pages
- Titles génériques ("Accueil", "Bienvenue", "Page 1")
- Nom de marque absent

#### Méta-Description
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| Existe | Chaque page devrait avoir une méta-description | Réussi/Échoué |
| Longueur | 150-160 caractères | Réussi/À Améliorer/Échoué |
| Mot-clé principal | Inclut naturellement le mot-clé cible | Réussi/À Améliorer/Échoué |
| Appel à l'action | Inclut une raison de cliquer | Réussi/À Améliorer/Échoué |
| Unique | Différente des autres pages | Réussi/Échoué |
| Attractive | Fonctionne comme le texte publicitaire du résultat de recherche | Réussi/À Améliorer/Échoué |

#### Hiérarchie des Titres (H1-H6)
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| H1 présent | Exactement un H1 par page | Réussi/Échoué |
| H1 contient le mot-clé | Mot-clé principal dans le H1 | Réussi/À Améliorer/Échoué |
| H1 différent du title | H1 et balise title sont différents (mais liés) | Réussi/À Améliorer/Échoué |
| Hiérarchie logique | H2 sous H1, H3 sous H2 (pas de niveaux sautés) | Réussi/À Améliorer/Échoué |
| Sous-titres descriptifs | H2 et H3 décrivent clairement les sections de contenu | Réussi/À Améliorer/Échoué |
| Mots-clés dans les sous-titres | Mots-clés secondaires apparaissent naturellement dans les H2/H3 | Réussi/À Améliorer/Échoué |
| Non surutilisés | Titres utilisés pour la structure, pas le style | Réussi/À Améliorer/Échoué |

#### Optimisation des Images
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| Texte alt | Chaque image a un texte alt descriptif | Réussi/À Améliorer/Échoué |
| Qualité du texte alt | Le texte alt décrit l'image et inclut des mots-clés naturellement | Réussi/À Améliorer/Échoué |
| Noms de fichiers | Noms de fichiers descriptifs (pas IMG_001.jpg) | Réussi/À Améliorer/Échoué |
| Taille des fichiers | Images optimisées pour le web (WebP préféré, compressées) | Réussi/À Améliorer/Échoué |
| Chargement différé | Les images sous le pli utilisent le lazy loading | Réussi/À Améliorer/Échoué |
| Images responsives | Utilise srcset ou l'élément picture pour différentes tailles | Réussi/À Améliorer/Échoué |
| Images décoratives | Les images décoratives ont alt="" (pas alt manquant) | Réussi/À Améliorer/Échoué |

#### Maillage Interne
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| Liens internes présents | La page renvoie vers d'autres pages pertinentes du site | Réussi/À Améliorer/Échoué |
| Texte d'ancre | Le texte d'ancre des liens internes est descriptif (pas "cliquez ici") | Réussi/À Améliorer/Échoué |
| Liens profonds | Les liens vont vers des pages spécifiques, pas seulement la page d'accueil | Réussi/À Améliorer/Échoué |
| Contexte pertinent | Les liens sont contextuellement pertinents par rapport au contenu environnant | Réussi/À Améliorer/Échoué |
| Nombre raisonnable | 3-10 liens internes par 1 000 mots de contenu | Réussi/À Améliorer/Échoué |
| Liens cassés | Pas de liens internes cassés (404) | Réussi/Échoué |

#### Structure des URL
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| Lisible | L'URL est lisible par l'humain et descriptive | Réussi/À Améliorer/Échoué |
| Mots-clés | L'URL contient des mots-clés pertinents | Réussi/À Améliorer/Échoué |
| Longueur | Moins de 75 caractères (idéalement moins de 60) | Réussi/À Améliorer/Échoué |
| Tirets | Mots séparés par des tirets (pas des underscores) | Réussi/Échoué |
| Minuscules | Tous les caractères en minuscules | Réussi/Échoué |
| Pas de paramètres | URL propres sans paramètres de requête inutiles | Réussi/À Améliorer/Échoué |
| Slashes finaux | Utilisation cohérente (toujours ou jamais) | Réussi/À Améliorer/Échoué |

#### Balises hreflang (Obligatoires pour les Sites Multilingues UE)
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| Balises hreflang présentes | Obligatoires pour les sites ciblant plusieurs pays/langues UE | Réussi/Échoué |
| Couverture des langues | fr, de, it, es, be, nl, ch, en-gb selon les marchés ciblés | Réussi/À Améliorer/Échoué |
| Balise x-default | Présente pour les visiteurs dont la langue n'est pas couverte | Réussi/Échoué |
| Réciprocité | Chaque version de langue pointe vers toutes les autres | Réussi/Échoué |
| TLDs par pays | Utilisation correcte des TLDs : .fr, .de, .it, .es, .be, .nl, .ch | Réussi/À Améliorer/Échoué |

### Étape 3 : Évaluation de la Qualité du Contenu (E-E-A-T)

Évaluez le contenu par rapport au cadre E-E-A-T de Google :

#### Expérience (Experience)
Le contenu démontre-t-il une expérience de première main avec le sujet ?

**Vérifiez :**
- Anecdotes personnelles, études de cas ou exemples concrets
- Captures d'écran, photos ou preuves d'expérience pratique
- Détails spécifiques que seule une personne expérimentée connaîtrait
- Contenu de type "j'ai fait X et voici ce qui s'est passé"

**Score :** Fort / Présent / Faible / Absent

#### Expertise
L'auteur a-t-il des connaissances démontrées dans ce domaine ?

**Vérifiez :**
- Biographie d'auteur avec accréditations pertinentes
- Profondeur du contenu (pas superficiel)
- Informations et données précises
- Utilisation appropriée de la terminologie sectorielle
- Liens vers des sources faisant autorité

**Score :** Fort / Présent / Faible / Absent

#### Autorité (Authoritativeness)
Le site web et l'auteur sont-ils reconnus comme faisant autorité dans ce domaine ?

**Vérifiez :**
- Signatures d'auteur avec vrais noms et biographies
- Page À propos avec historique de l'entreprise
- Prix ou certifications sectoriels
- Backlinks de sites faisant autorité
- Mentions presse ou couverture médiatique
- Articles invités dans des publications du secteur

**Score :** Fort / Présent / Faible / Absent

#### Fiabilité (Trustworthiness)
Les utilisateurs peuvent-ils faire confiance à ce contenu et à ce site web ?

**Vérifiez :**
- HTTPS (certificat SSL)
- Politique de confidentialité conforme au RGPD et conditions d'utilisation
- Adresse physique et coordonnées
- Avis et témoignages clients
- Badges de sécurité et certifications (Trusted Shops, etc.)
- Pratiques commerciales transparentes
- Informations précises et à jour
- Affirmations et statistiques correctement sourcées
- Mentions légales (obligatoires en France)
- Numéro SIRET/RCS visible

**Score :** Fort / Présent / Faible / Absent

### Étape 4 : Analyse des Mots-Clés

#### Évaluation du Mot-Clé Principal
| Élément | Évaluation |
|---|---|
| Mot-clé principal identifié | Quel mot-clé cette page cible-t-elle ? |
| Alignement avec l'intention de recherche | Le contenu correspond-il à ce que les internautes attendent ? (informationnelle, commerciale, transactionnelle, navigationnelle) |
| Mot-clé dans le title | Présent, position, usage naturel |
| Mot-clé dans le H1 | Présent, usage naturel |
| Mot-clé dans les 100 premiers mots | Apparaît tôt dans le contenu |
| Mot-clé dans les sous-titres | Apparaît dans au moins un H2 ou H3 |
| Mot-clé dans la méta-description | Présent et naturel |
| Mot-clé dans l'URL | Présent |
| Densité du mot-clé | 1-2% est idéal. Plus de 3% est du bourrage de mots-clés. |

#### Mots-Clés Secondaires
Identifiez 5-10 mots-clés connexes devant être naturellement inclus dans le contenu :
- Synonymes et variations du mot-clé principal
- Variations longue traîne
- Questions connexes (Autres Questions Posées / PAA)
- Mots-clés LSI (Indexation Sémantique Latente)

#### Analyse de l'Intention de Recherche
Déterminez l'intention de recherche derrière le mot-clé cible et évaluez si le contenu correspond :

| Type d'Intention | Objectif de l'Utilisateur | Le Contenu Devrait Être |
|---|---|---|
| Informationnelle | Apprendre quelque chose | Article de blog, guide, tutoriel, FAQ |
| Commerciale | Comparer des options | Page de comparaison, avis, liste |
| Transactionnelle | Acheter quelque chose | Page produit, page tarifs, checkout |
| Navigationnelle | Trouver une page spécifique | Page d'accueil, page de connexion, outil spécifique |

**Un mauvais alignement est un facteur de pénalisation.** Si l'utilisateur cherche "comment faire X" (informationnelle) et atterrit sur une page de vente (transactionnelle), il repart — et Google le remarque.

### Étape 5 : Vérification Rapide du SEO Technique

#### Robots.txt
```
Vérification : /robots.txt existe-t-il et est-il correctement configuré ?
```
- [ ] robots.txt accessible
- [ ] Ne bloque pas les pages ou ressources importantes
- [ ] Pointe vers sitemap.xml
- [ ] Ne bloque pas CSS/JS (nécessaires pour le rendu)

#### Sitemap XML
```
Vérification : /sitemap.xml existe-t-il ?
```
- [ ] Le sitemap existe et est accessible
- [ ] Contient toutes les pages importantes
- [ ] Pas d'URL cassées dans le sitemap
- [ ] Soumis à Google Search Console
- [ ] Les dates de dernière modification sont précises

#### Balises Canoniques
- [ ] Balise canonique présente sur la page
- [ ] Pointe vers l'URL correcte (auto-référentielle ou vers la version canonique)
- [ ] Cohérente avec robots.txt et le sitemap

#### Vitesse de Page
Benchmarks de référence :

| Métrique | Bon | À Améliorer | Mauvais |
|---|---|---|---|
| Largest Contentful Paint (LCP) | Moins de 2,5s | 2,5-4,0s | Plus de 4,0s |
| First Input Delay (FID) | Moins de 100ms | 100-300ms | Plus de 300ms |
| Cumulative Layout Shift (CLS) | Moins de 0,1 | 0,1-0,25 | Plus de 0,25 |
| Time to First Byte (TTFB) | Moins de 200ms | 200-500ms | Plus de 500ms |
| First Contentful Paint (FCP) | Moins de 1,8s | 1,8-3,0s | Plus de 3,0s |

**Problèmes de vitesse courants à signaler :**
- Images non optimisées (recommander le format WebP, compression)
- JavaScript ou CSS bloquant le rendu
- Pas de mise en cache navigateur
- Pas de CDN détecté
- Scripts tiers excessifs (tracking, widgets, polices)
- CSS et JavaScript non minifiés
- Compression manquante (gzip ou brotli)

#### Compatibilité Mobile
- [ ] Balise meta viewport présente (`<meta name="viewport" content="width=device-width, initial-scale=1">`)
- [ ] Texte lisible sans zoom (minimum 16px pour le texte du corps)
- [ ] Cibles de toucher suffisamment grandes et espacées (minimum 48x48px)
- [ ] Pas de défilement horizontal requis
- [ ] Images responsives
- [ ] Formulaires utilisables sur mobile

#### Conformité RGPD (Vérification Technique)
- [ ] Bannière de consentement cookies conforme (refus aussi facile que l'acceptation)
- [ ] Politique de confidentialité complète et accessible
- [ ] Opt-in explicite pour le marketing par email
- [ ] Pas de cookies non essentiels sans consentement préalable
- [ ] Coordonnées du DPO (Délégué à la Protection des Données) si applicable

### Étape 6 : Analyse des Lacunes de Contenu

Méthodologie pour identifier les lacunes de contenu :

1. **Identifier le cluster thématique :** Quel est le sujet principal couvert par cette page/ce site ?
2. **Cartographier le contenu existant :** Quels sous-thèmes sont déjà couverts ?
3. **Identifier les sous-thèmes manquants :** Quels sujets connexes les concurrents couvrent-ils que ce site ne couvre pas ?
4. **Analyser les "Autres Questions Posées" :** Quelles questions les internautes posent-ils sur ce sujet ?
5. **Vérifier les recherches connexes :** Que suggère Google au bas de la page de résultats ?

**Modèle d'Analyse des Lacunes de Contenu :**
| Sujet Manquant | Potentiel de Volume | Concurrence | Type de Contenu Nécessaire | Priorité |
|---|---|---|---|---|
| [Sujet] | Élevé/Moyen/Faible | Élevé/Moyen/Faible | Blog/Guide/Outil/Page | 1-5 |

### Étape 7 : Optimisation des Extraits Enrichis (Featured Snippets)

Identifiez les opportunités de capturer des extraits enrichis :

**Types d'extraits enrichis :**
1. **Extrait paragraphe** — Réponse en 40-60 mots. Utilisez une question claire comme H2/H3 suivie d'une réponse concise.
2. **Extrait liste** — Utilisez des listes ordonnées ou non ordonnées avec un H2 contenant la requête cible.
3. **Extrait tableau** — Utilisez des tableaux HTML avec des en-têtes clairs.
4. **Extrait vidéo** — Incluez une vidéo avec un titre descriptif et des horodatages.

**Liste de contrôle d'optimisation :**
- [ ] Ciblez les requêtes sous forme de questions ("comment", "qu'est-ce que", "pourquoi")
- [ ] Placez la réponse immédiatement après l'en-tête de question
- [ ] Gardez les réponses en paragraphe entre 40 et 60 mots
- [ ] Utilisez des listes structurées et des tableaux là où c'est approprié
- [ ] Incluez la requête cible dans un H2 ou H3

### Étape 8 : Audit du Balisage Schema.org

Vérifiez l'implémentation des données structurées, avec attributs de langue française :

| Type de Schema | Applicable À | Statut |
|---|---|---|
| Organization | Page d'accueil, page À propos | Présent/Absent |
| LocalBusiness | Entreprises locales (avec `addressLocality` en français) | Présent/Absent/N.A. |
| Product | Pages produit (avec `priceCurrency: "EUR"`) | Présent/Absent/N.A. |
| Article | Articles de blog, actualités (avec `inLanguage: "fr"`) | Présent/Absent/N.A. |
| FAQ | Sections FAQ | Présent/Absent |
| HowTo | Contenu tutoriel | Présent/Absent/N.A. |
| Review/AggregateRating | Avis, témoignages | Présent/Absent/N.A. |
| BreadcrumbList | Toutes les pages avec fil d'Ariane | Présent/Absent |
| WebSite/SearchAction | Page d'accueil (boîte de recherche sitelinks) | Présent/Absent |
| Event | Pages d'événements (avec `location` en français) | Présent/Absent/N.A. |

**Guide d'implémentation :**
- Utilisez le format JSON-LD (format préféré de Google)
- Validez avec l'Outil de Test des Résultats Enrichis de Google
- Ne balisez pas le contenu qui n'est pas visible sur la page
- Gardez les données schema cohérentes avec le contenu on-page
- Spécifiez `"inLanguage": "fr"` pour le contenu en français
- Utilisez `"priceCurrency": "EUR"` pour toutes les données de prix

### Étape 9 : Opportunités de Maillage Interne

Identifiez les améliorations spécifiques du maillage interne :

1. **Pages orphelines** — Pages sans liens internes pointant vers elles
2. **Pages hub** — Pages à forte autorité devant lier vers du contenu connexe
3. **Clusters thématiques** — Groupez le contenu connexe et créez des structures de liens
4. **Liens CTA** — Le contenu de blog devrait lier vers les pages produit/service pertinentes
5. **Liens pied de page/barre latérale** — Liens sitewide vers les pages importantes

**Évaluation de l'Architecture de Liens :**
```
Page d'Accueil
  |-- Pages Catégorie/Service (Contenu Pilier)
       |-- Articles de Blog/Articles Individuels (Contenu Cluster)
            |-- Liens retour vers le Contenu Pilier
  |-- Pages de Conversion Clés (Tarifs, Inscription, Contact)
       |-- Liées depuis le contenu pertinent
```

### Étape 10 : Évaluation de l'Impact des Core Web Vitals

Évaluez l'impact sur le CA des performances des Core Web Vitals :

**Impacts documentés par la recherche :**
- Les sites réussissant tous les Core Web Vitals voient 24% moins d'abandons de pages
- Une diminution de 100ms du LCP correspond à une augmentation de 1,1% des taux de conversion
- Réduire le CLS de 0,1 correspond à une diminution de 15% du taux de rebond
- Les pages se chargeant en moins de 2 secondes ont un taux de rebond moyen de 9%, tandis que les pages se chargeant en 5 secondes ont 38%

**Recommandations par métrique :**
| Métrique | Si Échoué | Corrections Typiques |
|---|---|---|
| LCP | Plus de 2,5s | Optimisez l'image héros, préchargez les ressources critiques, utilisez un CDN, réduisez le temps de réponse serveur |
| FID/INP | Plus de 100ms | Réduisez l'exécution JavaScript, différez les scripts non critiques, utilisez des web workers |
| CLS | Plus de 0,1 | Définissez les dimensions des images, réservez de l'espace pour les publicités/intégrations, évitez d'insérer du contenu au-dessus du contenu existant |

### Étape 11 : Moteurs de Recherche Européens et SEO Local

Au-delà de Google.fr, prenez en compte :

**Moteurs de Recherche à Cibler :**
- **Google.fr** — Dominant en France (93%+ de part de marché)
- **Bing France** — Segment significatif, important pour les utilisateurs Windows
- **Qwant** — Moteur de recherche français axé sur la confidentialité, en croissance

**SEO Local pour la France :**
- [ ] Google Business Profile configuré et optimisé
- [ ] Pages Jaunes (pagesjaunes.fr) — annuaire de référence français
- [ ] Yelp France — pour les commerces locaux
- [ ] Tripadvisor (si applicable pour la restauration/hôtellerie)
- [ ] Cohérence NAP (Nom, Adresse, Téléphone) sur tous les annuaires

**TLDs Nationaux Européens :**
Recommandez les TLDs appropriés selon les marchés ciblés :
- France : .fr
- Allemagne : .de
- Italie : .it
- Espagne : .es
- Belgique : .be
- Pays-Bas : .nl
- Suisse : .ch (+ .fr pour la Suisse romande)

### Étape 12 : Recommandations de Stratégie de Blog et de Contenu

Sur la base des conclusions de l'audit, recommandez :

1. **Cadence de publication** — À quelle fréquence publier selon la concurrence et les ressources
2. **Types de contenu** — Articles de blog, guides, outils, vidéos, infographies
3. **Stratégie de ciblage des mots-clés** — Équilibre entre fort volume et longue traîne
4. **Longueur du contenu** — Benchmarquez par rapport au contenu bien classé pour les mots-clés cibles
5. **Stratégie de mise à jour du contenu** — À quelle fréquence rafraîchir le contenu existant
6. **Plan de distribution** — Comment promouvoir le contenu au-delà de la recherche organique

**Matrice de Priorisation du Contenu :**
| Idée de Contenu | Volume de Recherche | Concurrence | Valeur Business | Score de Priorité |
|---|---|---|---|---|
| [Sujet] | Élevé/Moyen/Faible | Élevé/Moyen/Faible | Élevé/Moyen/Faible | 1-10 |

Score : Fort volume + Faible concurrence + Forte valeur business = Priorité la plus élevée

## Format de Sortie

Générez un fichier appelé `SEO-AUDIT.md`. Tout le contenu doit être rédigé en français :

```markdown
# Audit SEO de Contenu
## [URL]
### Date : [Date]

---

## Score de Santé SEO : [X/100]

---

## Liste de Contrôle SEO On-Page

### Balise Title
- Statut : [Réussi/À Améliorer/Échoué]
- Actuelle : "[title actuel]"
- Recommandée : "[title amélioré]"
- Problèmes : [liste des problèmes]

### Méta-Description
- Statut : [Réussi/À Améliorer/Échoué]
- Actuelle : "[meta actuelle]"
- Recommandée : "[meta améliorée]"

### Hiérarchie des Titres
[Analyse de la structure H1-H6]

### Optimisation des Images
[Résultats de l'audit du texte alt]

### Maillage Interne
[Analyse des liens]

### Structure des URL
[Évaluation des URL]

### Balises hreflang
[Analyse de l'internationalisation pour les marchés UE ciblés]

---

## Qualité du Contenu (E-E-A-T)
| Dimension | Score | Preuves |
|---|---|---|
| Expérience | [Fort/Présent/Faible/Absent] | [détails] |
| Expertise | [Fort/Présent/Faible/Absent] | [détails] |
| Autorité | [Fort/Présent/Faible/Absent] | [détails] |
| Fiabilité | [Fort/Présent/Faible/Absent] | [détails] |

---

## Analyse des Mots-Clés
- Mot-clé Principal : [mot-clé]
- Intention de Recherche : [type]
- Placement du Mot-clé : [résultats de la liste de contrôle]
- Mots-clés Secondaires : [liste]

---

## SEO Technique
[Résultats de la vérification rapide]

### Conformité RGPD
[Évaluation des aspects techniques RGPD]

---

## Analyse des Lacunes de Contenu
[Tableau des sujets manquants]

---

## Opportunités d'Extraits Enrichis
[Opportunités spécifiques]

---

## Balisage Schema.org
[Actuel vs recommandé, avec attributs de langue française]

---

## Opportunités de Maillage Interne
[Recommandations spécifiques]

---

## Core Web Vitals
[Évaluation des performances avec impact sur le CA]

---

## SEO Local et Moteurs Européens
[Google Business Profile, Pages Jaunes, Bing France, Qwant, hreflang, TLDs nationaux]

---

## Recommandations de Stratégie de Contenu
[Plan de publication, priorités de contenu]

---

## Recommandations Priorisées

### Critique (À Corriger Immédiatement)
1. [recommandation avec impact attendu]

### Haute Priorité (Ce Mois)
1. [recommandation]

### Priorité Moyenne (Ce Trimestre)
1. [recommandation]

### Priorité Faible (Quand les Ressources le Permettent)
1. [recommandation]
```

## Principes Clés
- Les audits SEO doivent être pédagogiques, pas seulement diagnostiques. Expliquez POURQUOI chaque élément compte pour que le client comprenne la valeur.
- Fournissez toujours l'"avant" (état actuel) et l'"après" (changement recommandé) pour que le client voie exactement ce qui doit changer.
- Liez les améliorations SEO aux résultats business. "Optimisez votre balise title" ne signifie rien pour un chef d'entreprise. "Optimiser votre balise title pourrait augmenter votre taux de clic de 20-35%, apportant environ 500 visiteurs supplémentaires par mois sur cette page, soit environ X XXX€ de CA mensuel" est actionnable.
- Utilisez les données du script automatisé comme point de départ, mais ajoutez une analyse experte par-dessus. Le script trouve les données ; la compétence les interprète.
- Priorisez les recommandations par ratio effort/impact. Un changement de balise title prend 5 minutes mais impacte chaque impression de recherche. Une refonte complète du contenu prend des semaines.
- Si l'utilisateur a précédemment exécuté `/market audit` ou `/market landing`, croisez ces conclusions avec l'audit SEO pour une image plus complète.
- Mentionnez toujours la conformité RGPD comme facteur de fiabilité (Trustworthiness) dans l'évaluation E-E-A-T.
- Pour les sites ciblant plusieurs pays UE, les balises hreflang sont obligatoires — signalez leur absence comme une priorité haute.
