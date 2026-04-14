<p align="center">
  <img src="banner.svg" alt="Suite Marketing IA pour Claude Code" width="100%">
</p>

# Suite Marketing IA pour Claude Code

Un système complet d'analyse marketing et d'automatisation par agents IA pour [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Auditez n'importe quel site web, générez des copies, construisez des séquences d'emails, créez des calendriers de contenu, analysez vos concurrents et produisez des rapports PDF prêts pour vos clients — le tout depuis votre terminal.

**Conçu pour les entrepreneurs, les agences et les solopreneurs qui souhaitent vendre des services marketing propulsés par l'IA.**

---

## Ce que ça fait

Tapez une commande dans Claude Code et obtenez instantanément une analyse marketing actionnable :

```
> /market audit https://example.fr

Lancement de 5 agents en parallèle...
✓ Analyse Contenu & Messaging        — Score : 72/100
✓ Optimisation des Conversions       — Score : 58/100
✓ SEO & Visibilité                   — Score : 81/100
✓ Positionnement Concurrentiel       — Score : 64/100
✓ Marque & Confiance                 — Score : 76/100
✓ Croissance & Stratégie             — Score : 61/100

Score Marketing Global : 69/100

Rapport complet sauvegardé dans MARKETING-AUDIT.md
```

---

## Installation

### Installation en une seule commande

```bash
curl -fsSL https://raw.githubusercontent.com/ASMAE-DEV-SE/claude-agents-marketing-eu/main/install.sh | bash
```

### Installation manuelle

```bash
git clone https://github.com/ASMAE-DEV-SE/claude-agents-marketing-eu.git
cd ai-marketing-agents-fr
./install.sh
```

### Optionnel : Support des rapports PDF

```bash
pip install reportlab
```

---

## Commandes disponibles

| Commande | Ce qu'elle fait |
|----------|----------------|
| `/market audit <url>` | Audit marketing complet avec 5 agents en parallèle |
| `/market quick <url>` | Snapshot marketing en 60 secondes |
| `/market copy <url>` | Génération de copies optimisées avec exemples avant/après |
| `/market emails <sujet>` | Génération de séquences d'emails complètes |
| `/market social <sujet>` | Calendrier de contenu social media sur 30 jours |
| `/market ads <url>` | Créatifs et copies publicitaires pour toutes les plateformes |
| `/market funnel <url>` | Analyse et optimisation du tunnel de vente |
| `/market competitors <url>` | Rapport d'intelligence concurrentielle |
| `/market landing <url>` | Analyse CRO de page d'atterrissage |
| `/market launch <produit>` | Plan de lancement produit |
| `/market proposal <client>` | Générateur de proposition client |
| `/market report <url>` | Rapport marketing complet (Markdown) |
| `/market report-pdf <url>` | Rapport marketing professionnel (PDF) |
| `/market seo <url>` | Audit de contenu SEO |
| `/market brand <url>` | Analyse de la voix de marque et charte éditoriale |

---

## Architecture

```
claude-agents-marketing-eu/
├── market/SKILL.md                     # Orchestrateur principal (route toutes les commandes /market)
│
├── skills/                             # 14 sous-compétences
│   ├── market-audit/SKILL.md           # Orchestration de l'audit complet
│   ├── market-copy/SKILL.md            # Analyse et génération de copies
│   ├── market-emails/SKILL.md          # Génération de séquences d'emails
│   ├── market-social/SKILL.md          # Calendrier de contenu social media
│   ├── market-ads/SKILL.md             # Créatifs et copies publicitaires
│   ├── market-funnel/SKILL.md          # Analyse et optimisation du tunnel
│   ├── market-competitors/SKILL.md     # Intelligence concurrentielle
│   ├── market-landing/SKILL.md         # CRO de page d'atterrissage
│   ├── market-launch/SKILL.md          # Génération de plan de lancement
│   ├── market-proposal/SKILL.md        # Générateur de proposition client
│   ├── market-report/SKILL.md          # Rapport marketing (Markdown)
│   ├── market-report-pdf/SKILL.md      # Rapport marketing (PDF)
│   ├── market-seo/SKILL.md             # Audit de contenu SEO
│   └── market-brand/SKILL.md           # Analyse de la voix de marque
│
├── agents/                             # 5 sous-agents en parallèle
│   ├── market-content.md               # Analyse du contenu et du messaging
│   ├── market-conversion.md            # CRO et optimisation du tunnel
│   ├── market-competitive.md           # Positionnement concurrentiel
│   ├── market-technical.md             # SEO technique et tracking
│   └── market-strategy.md              # Marque, pricing et stratégie de croissance
│
├── scripts/                            # Scripts utilitaires Python
│   ├── analyze_page.py                 # Analyse marketing d'une page web
│   ├── competitor_scanner.py           # Scanner de sites concurrents
│   ├── social_calendar.py              # Générateur de calendrier de contenu
│   └── generate_pdf_report.py          # Générateur de rapports PDF
│
├── templates/                          # Modèles marketing
│   ├── email-welcome.md                # Séquence d'accueil (5 emails)
│   ├── email-nurture.md                # Séquence de nurturing (6 emails)
│   ├── email-launch.md                 # Séquence de lancement produit (8 emails)
│   ├── proposal-template.md            # Modèle de proposition client
│   ├── content-calendar.md             # Calendrier de contenu 30 jours
│   └── launch-checklist.md             # Checklist de lancement
│
├── install.sh                          # Installateur en une commande
├── uninstall.sh                        # Désinstallateur propre
├── requirements.txt                    # Dépendances Python
└── LICENSE                             # Licence MIT
```

---

## Méthodologie de scoring

L'audit marketing complet évalue les sites web selon 6 dimensions :

| Catégorie | Poids | Ce qui est mesuré |
|-----------|-------|-------------------|
| Contenu & Messaging | 25% | Qualité des copies, propositions de valeur, titres, CTAs |
| Optimisation des Conversions | 20% | Tunnels, formulaires, preuves sociales, friction, urgence |
| SEO & Visibilité | 20% | SEO on-page, SEO technique, structure du contenu |
| Positionnement Concurrentiel | 15% | Différenciation, connaissance du marché, alternatives |
| Marque & Confiance | 10% | Qualité du design, signaux de confiance, autorité |
| Croissance & Stratégie | 10% | Pricing, canaux d'acquisition, rétention |

**Score Marketing Global** = Moyenne pondérée de toutes les catégories (0-100)

---

## Comment ça fonctionne

1. **Vous tapez une commande** — ex. `/market audit https://monsite.fr`
2. **Claude lit les fichiers de compétences** — ils indiquent à Claude exactement comment analyser le site
3. **5 sous-agents se lancent en parallèle** — chacun analyse une dimension différente
4. **Les scripts Python s'exécutent** — analyse automatisée des pages, scan des concurrents
5. **Les résultats sont compilés** — en un rapport scoré, priorisé et actionnable
6. **Le rapport est sauvegardé** — en fichier Markdown ou PDF professionnel

---

## Cas d'usage

### Pour les agences et freelances
- Lancez `/market audit` sur le site d'un prospect avant un appel commercial
- Générez `/market proposal` avec les résultats spécifiques et une tarification
- Livrez `/market report-pdf` comme livrable client professionnel

### Pour les solopreneurs
- Utilisez `/market copy` pour optimiser vos propres pages d'atterrissage
- Générez `/market emails` pour vos lancements de produits
- Construisez des `/market social` calendriers pour une présence régulière

### Pour les créateurs de contenu
- Analysez vos concurrents avec `/market competitors`
- Planifiez vos lancements avec `/market launch`
- Analysez votre tunnel avec `/market funnel`

---

## Désinstallation

```bash
./uninstall.sh
```

Ou manuellement :
```bash
rm -rf ~/.claude/skills/market*
rm -f ~/.claude/agents/market-*.md
```

---

## Licence

Licence MIT — voir [LICENSE](LICENSE) pour les détails.
