<div align="center">

<img src="banner.svg" alt="Suite Marketing IA" width="100%"/>

<br/>

# 🤖 Suite Marketing IA — Agents Claude Code

**Automatisez votre marketing avec des agents IA puissants, directement depuis votre terminal.**

<br/>

[![Licence MIT](https://img.shields.io/badge/Licence-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Code-orange.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](https://python.org)
[![Agents IA](https://img.shields.io/badge/Agents-5%20en%20parallèle-purple.svg)](#architecture)

<br/>

[🚀 Installation](#-installation) · [⚡ Commandes](#-commandes) · [🏗️ Architecture](#️-architecture) · [📊 Scoring](#-méthodologie-de-scoring) · [💡 Cas d'usage](#-cas-dusage)

</div>

---

## ✨ Présentation

La **Suite Marketing IA** est un système complet d'analyse marketing et d'automatisation par agents IA pour [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

> Auditez n'importe quel site, générez des copies percutantes, construisez des séquences d'emails, créez des calendriers de contenu, analysez vos concurrents et produisez des rapports PDF prêts pour vos clients — **le tout en une seule commande**.

**Conçu pour** les entrepreneurs, les agences et les solopreneurs qui souhaitent vendre des services marketing propulsés par l'IA.

---

## 🎯 Exemple en action

```
> /market audit https://monsite.fr

🚀 Lancement de 5 agents en parallèle...

  ✓ Contenu & Messaging            Score : 72 / 100
  ✓ Optimisation des Conversions   Score : 58 / 100
  ✓ SEO & Visibilité               Score : 81 / 100
  ✓ Positionnement Concurrentiel   Score : 64 / 100
  ✓ Marque & Confiance             Score : 76 / 100
  ✓ Croissance & Stratégie         Score : 61 / 100

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📊 Score Marketing Global : 69 / 100
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✅ Rapport complet sauvegardé → MARKETING-AUDIT.md
```

---

## 🚀 Installation

### ⚡ Installation en une seule commande

```bash
curl -fsSL https://raw.githubusercontent.com/ASMAE-DEV-SE/claude-agents-marketing-eu/main/install.sh | bash
```

### 🔧 Installation manuelle

```bash
git clone https://github.com/ASMAE-DEV-SE/claude-agents-marketing-eu.git
cd claude-agents-marketing-eu
./install.sh
```

### 📄 Support PDF *(optionnel)*

```bash
pip install reportlab
```

---

## ⚡ Commandes

| Commande | Description |
|:---------|:------------|
| `/market audit <url>` | Audit marketing complet — 5 agents en parallèle |
| `/market quick <url>` | Snapshot marketing express en 60 secondes |
| `/market copy <url>` | Copies optimisées avec exemples avant / après |
| `/market emails <sujet>` | Séquences d'emails complètes prêtes à l'envoi |
| `/market social <sujet>` | Calendrier social media 30 jours |
| `/market ads <url>` | Créatifs et copies pub pour toutes les plateformes |
| `/market funnel <url>` | Analyse et optimisation du tunnel de vente |
| `/market competitors <url>` | Rapport d'intelligence concurrentielle |
| `/market landing <url>` | Analyse CRO de page d'atterrissage |
| `/market launch <produit>` | Plan de lancement produit complet |
| `/market proposal <client>` | Proposition commerciale client personnalisée |
| `/market report <url>` | Rapport marketing complet en Markdown |
| `/market report-pdf <url>` | Rapport marketing professionnel en PDF |
| `/market seo <url>` | Audit de contenu SEO détaillé |
| `/market brand <url>` | Analyse de la voix de marque et charte éditoriale |

---

## 🏗️ Architecture

```
claude-agents-marketing-eu/
│
├── 📂 market/
│   └── SKILL.md                  ← Orchestrateur principal
│
├── 📂 skills/                    ← 14 sous-compétences spécialisées
│   ├── market-audit/
│   ├── market-copy/
│   ├── market-emails/
│   ├── market-social/
│   ├── market-ads/
│   ├── market-funnel/
│   ├── market-competitors/
│   ├── market-landing/
│   ├── market-launch/
│   ├── market-proposal/
│   ├── market-report/
│   ├── market-report-pdf/
│   ├── market-seo/
│   └── market-brand/
│
├── 📂 agents/                    ← 5 agents IA en parallèle
│   ├── market-content.md         ← Contenu & Messaging
│   ├── market-conversion.md      ← Optimisation des conversions
│   ├── market-competitive.md     ← Positionnement concurrentiel
│   ├── market-technical.md       ← SEO technique & tracking
│   └── market-strategy.md        ← Marque, pricing & croissance
│
├── 📂 scripts/                   ← Scripts Python utilitaires
│   ├── analyze_page.py
│   ├── competitor_scanner.py
│   ├── social_calendar.py
│   └── generate_pdf_report.py
│
├── 📂 templates/                 ← Modèles marketing prêts à l'emploi
│   ├── email-welcome.md          ← Séquence d'accueil (5 emails)
│   ├── email-nurture.md          ← Nurturing (6 emails)
│   ├── email-launch.md           ← Lancement produit (8 emails)
│   ├── proposal-template.md      ← Proposition client
│   ├── content-calendar.md       ← Calendrier 30 jours
│   └── launch-checklist.md       ← Checklist de lancement
│
├── install.sh
├── uninstall.sh
├── requirements.txt
└── LICENSE
```

---

## 📊 Méthodologie de Scoring

L'audit complet évalue chaque site sur **6 dimensions clés** :

| # | Catégorie | Poids | Ce qui est mesuré |
|:-:|:----------|:-----:|:------------------|
| 1 | Contenu & Messaging | **25%** | Qualité des copies, propositions de valeur, titres, CTAs |
| 2 | Optimisation des Conversions | **20%** | Tunnels, formulaires, preuves sociales, friction, urgence |
| 3 | SEO & Visibilité | **20%** | SEO on-page, SEO technique, structure du contenu |
| 4 | Positionnement Concurrentiel | **15%** | Différenciation, connaissance du marché, alternatives |
| 5 | Marque & Confiance | **10%** | Design, signaux de confiance, autorité |
| 6 | Croissance & Stratégie | **10%** | Pricing, canaux d'acquisition, rétention |

> **Score Global** = Moyenne pondérée de toutes les catégories **(0 → 100)**

---

## ⚙️ Comment ça fonctionne

```
Vous tapez une commande
        ↓
Claude lit les fichiers de compétences
        ↓
5 agents IA se lancent en parallèle
        ↓
Les scripts Python analysent la page
        ↓
Les résultats sont compilés et scorés
        ↓
Le rapport est sauvegardé (Markdown ou PDF)
```

---

## 💡 Cas d'usage

<details>
<summary><strong>🏢 Agences & Freelances</strong></summary>

<br/>

- Lancez `/market audit` sur le site d'un prospect avant un appel commercial
- Générez `/market proposal` avec des résultats chiffrés et une tarification
- Livrez `/market report-pdf` comme deliverable professionnel prêt à envoyer

</details>

<details>
<summary><strong>🚀 Solopreneurs</strong></summary>

<br/>

- Utilisez `/market copy` pour optimiser vos pages d'atterrissage
- Générez `/market emails` pour vos séquences de lancement
- Construisez un `/market social` calendrier pour une présence régulière

</details>

<details>
<summary><strong>✍️ Créateurs de contenu</strong></summary>

<br/>

- Analysez vos concurrents avec `/market competitors`
- Planifiez vos lancements avec `/market launch`
- Analysez votre tunnel avec `/market funnel`

</details>

---

## 🗑️ Désinstallation

```bash
./uninstall.sh
```

Ou manuellement :

```bash
rm -rf ~/.claude/skills/market*
rm -f ~/.claude/agents/market-*.md
```

---

## 📜 Licence

Distribué sous licence **MIT** — voir [LICENSE](LICENSE) pour les détails.

---

<div align="center">

Fait avec ❤️ pour les marketeurs et entrepreneurs francophones

⭐ **Si ce projet vous est utile, laissez une étoile !** ⭐

</div>
