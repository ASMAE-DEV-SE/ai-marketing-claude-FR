#!/usr/bin/env python3
"""
Marketing Report PDF Generator — AI Marketing Claude Code Skills
Generates professional, client-ready PDF marketing reports with charts,
score visualizations, and prioritized action plans.

Requires: reportlab (pip install reportlab)
"""

import sys
import json
import os
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                     TableStyle, PageBreak, Image)
    from reportlab.graphics.shapes import Drawing, Rect, Circle, String, Line, Wedge
    from reportlab.graphics.charts.barcharts import VerticalBarChart
    from reportlab.graphics import renderPDF
except ImportError:
    print("Erreur : reportlab est requis. Installez-le avec : pip install reportlab")
    sys.exit(1)


# Color palette
COLORS = {
    "primary": HexColor("#1B2A4A"),
    "accent": HexColor("#2D5BFF"),
    "highlight": HexColor("#FF6B35"),
    "success": HexColor("#00C853"),
    "warning": HexColor("#FFB300"),
    "danger": HexColor("#FF1744"),
    "light_bg": HexColor("#F5F7FA"),
    "text": HexColor("#2C3E50"),
    "text_light": HexColor("#7F8C9B"),
    "border": HexColor("#E0E6ED"),
    "white": white,
    "black": black,
}


def score_color(score):
    """Return color based on score value."""
    if score >= 80:
        return COLORS["success"]
    elif score >= 60:
        return COLORS["accent"]
    elif score >= 40:
        return COLORS["warning"]
    else:
        return COLORS["danger"]


def format_french_date(dt=None):
    """Format a datetime object as a French-style date string (e.g. '12 avril 2026')."""
    if dt is None:
        dt = datetime.now()
    months_fr = [
        "", "janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre"
    ]
    return f"{dt.day} {months_fr[dt.month]} {dt.year}"


def draw_score_gauge(score, x, y, size=80):
    """Create a circular score gauge drawing."""
    d = Drawing(size + 20, size + 30)

    # Background circle
    d.add(Circle(size / 2 + 10, size / 2 + 15, size / 2,
                 fillColor=COLORS["light_bg"], strokeColor=COLORS["border"], strokeWidth=2))

    # Score arc (simplified as colored inner circle)
    color = score_color(score)
    inner_r = size / 2 - 8
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r,
                 fillColor=color, strokeColor=None))

    # White center
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r - 10,
                 fillColor=COLORS["white"], strokeColor=None))

    # Score text
    d.add(String(size / 2 + 10, size / 2 + 10, str(int(score)),
                 fontSize=20, fillColor=COLORS["primary"],
                 textAnchor="middle", fontName="Helvetica-Bold"))

    return d


def create_bar_chart(categories, scores, width=450, height=180):
    """Create a horizontal bar chart for category scores."""
    d = Drawing(width, height)

    bar_height = 20
    gap = 8
    max_bar_width = width - 180
    start_y = height - 30
    label_x = 5
    bar_x = 160

    for i, (cat, score) in enumerate(zip(categories, scores)):
        y = start_y - i * (bar_height + gap)

        # Category label
        d.add(String(label_x, y + 5, cat[:22],
                     fontSize=9, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica"))

        # Background bar
        d.add(Rect(bar_x, y, max_bar_width, bar_height,
                   fillColor=COLORS["light_bg"], strokeColor=None))

        # Score bar
        bar_width = (score / 100) * max_bar_width
        color = score_color(score)
        d.add(Rect(bar_x, y, bar_width, bar_height,
                   fillColor=color, strokeColor=None))

        # Score label
        d.add(String(bar_x + max_bar_width + 10, y + 5, f"{int(score)}",
                     fontSize=10, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica-Bold"))

    return d


def generate_report(data, output_path):
    """Generate a professional marketing PDF report."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=28,
        textColor=COLORS["primary"],
        spaceAfter=6,
        fontName="Helvetica-Bold"
    )

    subtitle_style = ParagraphStyle(
        "CustomSubtitle",
        parent=styles["Normal"],
        fontSize=14,
        textColor=COLORS["text_light"],
        spaceAfter=20,
        fontName="Helvetica"
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading1"],
        fontSize=18,
        textColor=COLORS["primary"],
        spaceBefore=20,
        spaceAfter=10,
        fontName="Helvetica-Bold"
    )

    subheading_style = ParagraphStyle(
        "CustomSubheading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=COLORS["accent"],
        spaceBefore=14,
        spaceAfter=8,
        fontName="Helvetica-Bold"
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["Normal"],
        fontSize=10,
        textColor=COLORS["text"],
        spaceAfter=6,
        fontName="Helvetica",
        leading=14
    )

    # Build document elements
    elements = []

    # === PAGE DE COUVERTURE ===
    elements.append(Spacer(1, 1.5 * inch))
    elements.append(Paragraph("Rapport d'Audit Marketing", title_style))

    url = data.get("url", "example.com")
    # Support both pre-formatted date string and auto-generated French date
    raw_date = data.get("date")
    if raw_date:
        date_str = raw_date
    else:
        date_str = format_french_date()
    elements.append(Paragraph(f"{url}", subtitle_style))
    elements.append(Paragraph(f"Généré le : {date_str}", subtitle_style))
    elements.append(Spacer(1, 0.5 * inch))

    # Overall score gauge
    overall_score = data.get("overall_score", 0)
    gauge = draw_score_gauge(overall_score, 0, 0, size=100)
    elements.append(gauge)
    elements.append(Spacer(1, 0.3 * inch))

    grade = "A+" if overall_score >= 90 else "A" if overall_score >= 80 else "B" if overall_score >= 70 else "C" if overall_score >= 60 else "D" if overall_score >= 50 else "F"
    elements.append(Paragraph(f"Score Marketing Global : {int(overall_score)}/100 (Note : {grade})", heading_style))

    exec_summary = data.get("executive_summary", "Ce rapport fournit une analyse complète de l'efficacité marketing du site web, couvrant le contenu, la conversion, le référencement, le positionnement concurrentiel, la notoriété de la marque et la stratégie de croissance.")
    elements.append(Paragraph(exec_summary, body_style))

    elements.append(PageBreak())

    # === RÉPARTITION DES SCORES ===
    elements.append(Paragraph("Répartition des Scores", heading_style))

    categories = data.get("categories", {})
    cat_names = list(categories.keys()) if categories else [
        "Contenu & Message", "Optimisation de la Conversion", "SEO & Visibilité",
        "Positionnement Concurrentiel", "Marque & Confiance", "Croissance & Stratégie"
    ]
    cat_scores = [categories.get(c, {}).get("score", 50) for c in cat_names] if categories else [65, 58, 72, 55, 68, 60]

    # Bar chart
    chart = create_bar_chart(cat_names, cat_scores)
    elements.append(chart)
    elements.append(Spacer(1, 0.3 * inch))

    # Score table
    score_data = [["Catégorie", "Score", "Poids", "Statut"]]
    weights = ["25%", "20%", "20%", "15%", "10%", "10%"]
    for i, (name, score) in enumerate(zip(cat_names, cat_scores)):
        status = "Solide" if score >= 75 else "À améliorer" if score >= 50 else "Critique"
        weight = weights[i] if i < len(weights) else "—"
        score_data.append([name, f"{int(score)}/100", weight, status])

    score_table = Table(score_data, colWidths=[180, 70, 60, 90])
    score_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.append(score_table)

    elements.append(PageBreak())

    # === CONSTATS CLÉS ===
    elements.append(Paragraph("Constats Clés", heading_style))

    findings = data.get("findings", [])
    if not findings:
        findings = [
            {"severity": "Critique", "finding": "L'accroche de la page d'accueil manque de clarté — les visiteurs ne comprennent pas la proposition de valeur en moins de 5 secondes"},
            {"severity": "Élevé", "finding": "Aucune preuve sociale sur la page d'accueil — absence de témoignages, logos clients et badges de confiance"},
            {"severity": "Élevé", "finding": "Le CTA principal utilise un texte générique ('Commencer') au lieu d'un message axé sur la valeur"},
            {"severity": "Moyen", "finding": "Meta descriptions manquantes sur les pages d'atterrissage clés"},
            {"severity": "Moyen", "finding": "Aucun mécanisme de capture d'e-mails ou d'offre d'entrée visible"},
            {"severity": "Faible", "finding": "Le contenu du blog ne contient pas de liens internes vers les pages produit"},
        ]

    # Map English severity keys to French display labels
    severity_fr_map = {
        "Critical": "Critique",
        "High": "Élevé",
        "Medium": "Moyen",
        "Low": "Faible",
        "Critique": "Critique",
        "Élevé": "Élevé",
        "Moyen": "Moyen",
        "Faible": "Faible",
    }

    findings_data = [["Priorité", "Constat"]]
    for f in findings:
        severity_raw = f.get("severity", "Medium")
        severity = severity_fr_map.get(severity_raw, severity_raw)
        finding = f.get("finding", "")
        findings_data.append([severity, Paragraph(finding, body_style)])

    findings_table = Table(findings_data, colWidths=[70, 400])
    severity_colors = {
        "Critique": COLORS["danger"],
        "Élevé": COLORS["highlight"],
        "Moyen": COLORS["warning"],
        "Faible": COLORS["accent"],
        # Also support English keys passed directly
        "Critical": COLORS["danger"],
        "High": COLORS["highlight"],
        "Medium": COLORS["warning"],
        "Low": COLORS["accent"],
    }
    table_style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
    ]
    for i, f in enumerate(findings, 1):
        severity_raw = f.get("severity", "Medium")
        color = severity_colors.get(severity_raw, COLORS["warning"])
        table_style_cmds.append(("TEXTCOLOR", (0, i), (0, i), color))
        table_style_cmds.append(("FONTNAME", (0, i), (0, i), "Helvetica-Bold"))

    findings_table.setStyle(TableStyle(table_style_cmds))
    elements.append(findings_table)

    elements.append(PageBreak())

    # === PLAN D'ACTION ===
    elements.append(Paragraph("Plan d'Action Priorisé", heading_style))

    # Quick Wins
    elements.append(Paragraph("Actions Rapides (Cette Semaine)", subheading_style))
    quick_wins = data.get("quick_wins", [
        "Réécrire l'accroche de la page d'accueil pour qu'elle soit spécifique et axée sur les bénéfices",
        "Ajouter 3 à 5 logos clients ou badges de confiance au-dessus de la ligne de flottaison",
        "Modifier le CTA principal avec un texte à valeur ajoutée (ex. : 'Démarrez votre essai gratuit — sans CB')",
        "Ajouter des meta descriptions aux 5 pages d'atterrissage principales",
    ])
    for i, win in enumerate(quick_wins, 1):
        elements.append(Paragraph(f"{i}. {win}", body_style))

    elements.append(Spacer(1, 0.2 * inch))

    # Medium-Term
    elements.append(Paragraph("Moyen Terme (1 à 3 Mois)", subheading_style))
    medium_term = data.get("medium_term", [
        "Construire un tunnel de capture d'e-mails avec un lead magnet",
        "Créer des pages de comparaison pour les 3 principaux concurrents",
        "Développer 3 études de cas avec des résultats mesurables",
        "Mettre en place une stratégie de contenu blog ciblant les mots-clés à forte intention",
    ])
    for i, action in enumerate(medium_term, 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(Spacer(1, 0.2 * inch))

    # Strategic
    elements.append(Paragraph("Stratégique (3 à 6 Mois)", subheading_style))
    strategic = data.get("strategic", [
        "Lancer un programme de parrainage avec une structure d'incitation",
        "Construire un hub de contenu d'autorité avec des articles piliers",
        "Mettre en place une campagne de reciblage sur tout le tunnel de conversion",
        "Développer l'optimisation tarifaire basée sur des métriques de valeur",
    ])
    for i, action in enumerate(strategic, 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(PageBreak())

    # === PANORAMA CONCURRENTIEL ===
    if data.get("competitors"):
        elements.append(Paragraph("Paysage Concurrentiel", heading_style))

        comp_data = [["", data.get("brand_name", "Cible")] + [c.get("name", f"Concurrent {i+1}") for i, c in enumerate(data["competitors"][:3])]]
        comp_rows_en = ["Positioning", "Pricing", "Social Proof", "Content"]
        comp_rows_fr = ["Positionnement", "Tarification", "Preuve Sociale", "Contenu"]

        for row_name_fr, row_name_en in zip(comp_rows_fr, comp_rows_en):
            row = [row_name_fr, data.get("brand_name", "Cible")]
            for comp in data["competitors"][:3]:
                row.append(comp.get(row_name_en.lower().replace(" ", "_"), "—"))
            # Ensure consistent columns
            while len(row) < len(comp_data[0]):
                row.append("—")
            comp_data.append(row)

        col_count = len(comp_data[0])
        col_width = 470 / col_count
        comp_table = Table(comp_data, colWidths=[col_width] * col_count)
        comp_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
            ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ]))
        elements.append(comp_table)
        elements.append(PageBreak())

    # === MÉTHODOLOGIE ===
    elements.append(Paragraph("Méthodologie", heading_style))
    elements.append(Paragraph(
        "Cet audit évalue six dimensions clés de l'efficacité marketing. "
        "Chaque catégorie est notée de 0 à 100 sur la base des meilleures pratiques du secteur et des benchmarks concurrentiels.",
        body_style
    ))

    method_data = [
        ["Catégorie", "Poids", "Ce que nous mesurons"],
        ["Contenu & Message", "25%", "Qualité du texte, clarté de la proposition de valeur, efficacité des CTA"],
        ["Optimisation de la Conversion", "20%", "Conception du tunnel, formulaires, preuve sociale, réduction des frictions"],
        ["SEO & Visibilité", "20%", "SEO on-page, SEO technique, structure du contenu"],
        ["Positionnement Concurrentiel", "15%", "Différenciation, tarification, stratégie face aux alternatives"],
        ["Marque & Confiance", "10%", "Qualité du design, signaux de confiance, indicateurs d'autorité"],
        ["Croissance & Stratégie", "10%", "Stratégie tarifaire, canaux d'acquisition, fidélisation"],
    ]

    method_table = Table(method_data, colWidths=[165, 50, 255])
    method_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    elements.append(method_table)

    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph(
        "Généré par AI Marketing Suite pour Claude Code",
        ParagraphStyle("Footer", parent=body_style, fontSize=8, textColor=COLORS["text_light"])
    ))

    # Build PDF
    doc.build(elements)
    return output_path


def main():
    if len(sys.argv) < 2:
        # Demo mode — generate sample report
        sample_data = {
            "url": "https://example.com",
            "date": format_french_date(),
            "overall_score": 62,
            "executive_summary": "Cet audit marketing révèle plusieurs opportunités à fort impact pour améliorer les taux de conversion et renforcer le positionnement concurrentiel. Le site dispose de solides bases de contenu mais sous-performe en matière d'optimisation de la conversion et de veille concurrentielle.",
            "categories": {
                "Contenu & Message": {"score": 68, "weight": "25%"},
                "Optimisation de la Conversion": {"score": 52, "weight": "20%"},
                "SEO & Visibilité": {"score": 74, "weight": "20%"},
                "Positionnement Concurrentiel": {"score": 48, "weight": "15%"},
                "Marque & Confiance": {"score": 70, "weight": "10%"},
                "Croissance & Stratégie": {"score": 55, "weight": "10%"},
            },
            "findings": [
                {"severity": "Critique", "finding": "L'accroche de la page d'accueil est générique — elle ne communique pas de valeur spécifique à la cible"},
                {"severity": "Critique", "finding": "Aucune preuve sociale visible au-dessus de la ligne de flottaison"},
                {"severity": "Élevé", "finding": "Le bouton CTA principal affiche 'Envoyer' — il devrait utiliser un texte à valeur ajoutée"},
                {"severity": "Élevé", "finding": "La page tarifaire ne présente pas les fonctionnalités en comparaison et ne répond pas aux objections"},
                {"severity": "Moyen", "finding": "Pages de comparaison avec les concurrents manquantes — perte de trafic à forte intention"},
                {"severity": "Moyen", "finding": "Les articles de blog ne contiennent pas de liens internes vers les pages produit"},
                {"severity": "Faible", "finding": "Liens vers les réseaux sociaux dans le pied de page mais aucune intégration de preuve sociale"},
            ],
            "quick_wins": [
                "Réécrire l'accroche : 'Nous aidons les entreprises à croître' → 'Obtenez 3x plus de leads qualifiés en 30 jours — sans démarchage téléphonique'",
                "Ajouter 5 logos clients au-dessus de la ligne de flottaison avec 'Ils nous font confiance : plus de 500 entreprises'",
                "Changer le bouton 'Envoyer' en 'Obtenir mon Audit Marketing Gratuit'",
                "Ajouter une section témoignages avec nom, photo, entreprise et résultats chiffrés",
            ],
            "medium_term": [
                "Créer des pages '[Concurrent] Alternative' pour les 3 principaux concurrents",
                "Produire 3 études de cas vidéo montrant des résultats clients mesurables",
                "Mettre en place un pop-up de sortie avec une offre de lead magnet",
                "Lancer une séquence d'e-mails de nurturing pour les prospects non convertis",
            ],
            "strategic": [
                "Développer un hub de contenu d'autorité avec 10 pages piliers ciblant des mots-clés à fort volume",
                "Construire un programme de parrainage avec des incentives double face",
                "Lancer des campagnes de reciblage sur Meta et Google avec des messages adaptés au tunnel",
                "Créer un outil gratuit ou un diagnostic pour capter des leads en haut de tunnel",
            ],
            "competitors": [
                {"name": "Concurrent A", "positioning": "Plateforme tout-en-un", "pricing": "49€-199€/mois", "social_proof": "10 000+ utilisateurs", "content": "Blog actif"},
                {"name": "Concurrent B", "positioning": "Orientation entreprise", "pricing": "Sur devis", "social_proof": "Logos Fortune 500", "content": "Livres blancs"},
                {"name": "Concurrent C", "positioning": "Économique", "pricing": "Gratuit-29€/mois", "social_proof": "4,8★ Trustpilot", "content": "Chaîne YouTube"},
            ],
            "brand_name": "Exemple SARL"
        }

        output = "RAPPORT-MARKETING-exemple.pdf"
        generate_report(sample_data, output)
        print(f"Rapport exemple généré : {output}")
        return

    # JSON input mode
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "RAPPORT-MARKETING.pdf"

    with open(input_file, "r") as f:
        data = json.load(f)

    generate_report(data, output_file)
    print(f"Rapport généré : {output_file}")


if __name__ == "__main__":
    main()
