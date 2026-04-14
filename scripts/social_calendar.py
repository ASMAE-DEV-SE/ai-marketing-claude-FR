#!/usr/bin/env python3
"""
Social Media Calendar Generator — Utility script for AI Marketing Claude Code Skills
Generates a structured 30-day social media content calendar with platform-specific posts.
European/French market edition — all output in French, CET timezone references.
"""

import sys
import json
from datetime import datetime, timedelta


# Content pillar templates (French descriptions, European market focus)
CONTENT_PILLARS = {
    "educational": {
        "name": "Éducatif",
        "description": "Apportez de la valeur à votre audience en lui enseignant quelque chose d'utile",
        "formats": ["Guide pratique", "Astuce rapide", "Démystification d'idée reçue", "Partage de méthode",
                     "Recommandation d'outil", "Tendance du secteur", "Analyse de données"],
        "platforms": {
            "linkedin": "Publication longue avec points clés, partage de méthodes et données chiffrées",
            "twitter": "Format fil de discussion (5 à 10 tweets), commencer par un constat surprenant ou une prise de position",
            "instagram": "Carrousel (5 à 10 slides), design soigné, une idée par slide",
            "tiktok": "Vidéo de 60 à 90 secondes face caméra ou capture d'écran, accrocher en 2 secondes",
            "youtube": "Vidéo approfondie de 8 à 15 min, titre optimisé pour la recherche, miniature percutante"
        }
    },
    "behind_the_scenes": {
        "name": "Dans les Coulisses",
        "description": "Montrez le processus réel, sans filtre",
        "formats": ["Une journée dans ma vie", "Révélation de mes outils", "Présentation de mon processus",
                     "Erreur et leçon retenue", "Partage de métriques/revenus", "Équipe/espace de travail"],
        "platforms": {
            "linkedin": "Format témoignage personnel, vulnérabilité + leçon apprise",
            "twitter": "Tweet unique avec photo ou fil court, authentique et direct",
            "instagram": "Stories ou Reels, ambiance décontractée et authentique, images de coulisses",
            "tiktok": "Images brutes, son tendance, atmosphère authentique",
            "youtube": "Style vlog, 5 à 10 min, quotidien ou révélation de processus"
        }
    },
    "social_proof": {
        "name": "Preuve Sociale",
        "description": "Montrez vos résultats, témoignages et crédibilité",
        "formats": ["Succès client / étude de cas", "Partage de témoignage", "Avant / Après",
                     "Jalon de chiffre d'affaires", "Contenu généré par les utilisateurs", "Récompense / Reconnaissance"],
        "platforms": {
            "linkedin": "Format étude de cas avec chiffres précis, mentionner le client",
            "twitter": "Capture d'écran du résultat + contexte bref, célébration publique",
            "instagram": "Graphique de témoignage designé ou extrait vidéo de témoignage",
            "tiktok": "Révélation avant/après, contenu de transformation",
            "youtube": "Analyse complète de l'étude de cas, 10 à 15 min"
        }
    },
    "engagement": {
        "name": "Engagement",
        "description": "Lancez des conversations et construisez une communauté",
        "formats": ["Prise de position / Opinion", "Question à la communauté", "Sondage", "L'un ou l'autre",
                     "Opinion impopulaire", "D'accord ou pas ?", "Complétez la phrase"],
        "platforms": {
            "linkedin": "Commencer par une affirmation forte, demander des avis en commentaires",
            "twitter": "Prise de position courte et percutante ou sondage, répondre à chaque commentaire",
            "instagram": "Sondages et questions en Stories, stickers interactifs",
            "tiktok": "Format point de vue ou duo, répondre aux commentaires",
            "youtube": "Post communautaire avec sondage, ou vidéo sollicitant des avis"
        }
    },
    "promotional": {
        "name": "Promotionnel",
        "description": "Promotion directe du produit/service (à utiliser avec modération)",
        "formats": ["Démo produit", "Mise en avant d'une fonctionnalité", "Offre spéciale",
                     "Promo webinaire/événement", "Ressource gratuite", "Invitation à rejoindre la communauté"],
        "platforms": {
            "linkedin": "Approche valeur d'abord, commencer par le problème résolu",
            "twitter": "Pitch court avec lien, ou fil montrant l'outil en action",
            "instagram": "Reel démo ou carrousel présentant les bénéfices, lien en bio",
            "tiktok": "Démo produit avec format tendance, vente douce",
            "youtube": "Tutoriel utilisant votre produit, pas un discours commercial"
        }
    }
}

# Posting frequency recommendations (European/CET timezone)
POSTING_FREQUENCY = {
    "linkedin": {
        "ideal": "3 à 5 fois/semaine",
        "minimum": "2 fois/semaine",
        "best_times": "Mardi-Jeudi 8h-10h, 12h (CET)"
    },
    "twitter": {
        "ideal": "3 à 5 fois/jour",
        "minimum": "1 fois/jour",
        "best_times": "Lundi-Vendredi 9h-12h (CET)"
    },
    "instagram": {
        "ideal": "4 à 7 fois/semaine (feed + reels)",
        "minimum": "3 fois/semaine",
        "best_times": "Mardi-Vendredi 10h-14h, 19h-21h (CET)"
    },
    "tiktok": {
        "ideal": "1 à 3 fois/jour",
        "minimum": "3 fois/semaine",
        "best_times": "7h-9h, 12h-15h, 19h-23h (CET)"
    },
    "youtube": {
        "ideal": "2 à 3 fois/semaine",
        "minimum": "1 fois/semaine",
        "best_times": "Jeudi-Samedi 14h-16h (CET)"
    },
    "facebook": {
        "ideal": "3 à 5 fois/semaine",
        "minimum": "2 fois/semaine",
        "best_times": "Mercredi-Vendredi 11h-13h (CET)"
    }
}

# Hook formulas by platform (French)
HOOK_FORMULAS = {
    "linkedin": [
        "J'ai {fait X} et {résultat inattendu}. Voici ce que j'en ai appris :",
        "La plupart des gens pensent {croyance commune}. Ils ont tort. Voici pourquoi :",
        "{Nombre} choses que j'aurais aimé savoir avant de {action} :",
        "J'ai passé {temps} à analyser {sujet}. Voici {nombre} enseignements :",
        "Arrêtez de {erreur commune}. Faites ceci à la place :",
        "Le secteur {industrie} est en train de changer. Voici ce dont personne ne parle :"
    ],
    "twitter": [
        "{Sujet} est cassé. Voici un fil sur comment le réparer 🧵",
        "J'ai étudié {nombre} {choses}. Voici ce qui distingue les meilleurs du lot :",
        "Opinion impopulaire : {affirmation audacieuse}",
        "Vous n'avez pas besoin de {chose}. Vous avez besoin de {meilleure chose}. Voici pourquoi :",
        "{Nombre} {choses} qui vont {bénéfice} (fil) :",
        "La plus grande erreur en {sujet} ? {Erreur}. Je vous explique :"
    ],
    "instagram": [
        "Enregistrez ça pour plus tard ↓",
        "PDV : Vous atteignez enfin {résultat désiré}",
        "{Nombre} choses sur {sujet} qui vont vous surprendre",
        "L'antisèche {sujet} dont vous ignoriez avoir besoin",
        "Si vous avez du mal avec {problème}, essayez ça →",
        "J'ai transformé {entrée} en {résultat impressionnant}. Voici comment :"
    ],
    "tiktok": [
        "Attendez la fin... (révélation de transformation)",
        "Les choses qui font vraiment sens dans {niche}",
        "PDV : Vous découvrez {chose utile}",
        "Je n'arrive pas à croire que {chose surprenante} fonctionne vraiment",
        "En réponse à @user — voici comment je {fais quelque chose}",
        "Jour {X} de {défi/série}"
    ]
}

# French and European seasonal occasions for the content calendar
FRENCH_OCCASIONS = {
    1: ["Soldes d'hiver", "Nouvel An"],
    2: ["Saint-Valentin", "Chandeleur"],
    3: ["Journée Internationale des Droits des Femmes (8 mars)"],
    4: ["Pâques", "Poisson d'Avril"],
    5: ["Fête du Travail (1er mai)", "Journée de l'Europe (9 mai)", "Ascension", "Pentecôte"],
    6: ["Fête de la Musique (21 juin)", "Fête des Pères", "Soldes d'été"],
    7: ["Fête Nationale (14 juillet)"],
    8: ["Assomption"],
    9: ["Journées du Patrimoine", "Rentrée des classes"],
    10: ["Fête de l'Halloween"],
    11: ["Toussaint", "Black Friday", "Beaujolais Nouveau"],
    12: ["Noël", "Saint-Nicolas (Alsace, Belgique, Pays-Bas)"]
}


def generate_calendar(topic, platforms=None, days=30, brand_name=None):
    """Generate a social media content calendar."""
    if platforms is None:
        platforms = ["linkedin", "twitter", "instagram"]

    start_date = datetime.now()
    calendar = {
        "sujet": topic,
        "marque": brand_name or topic,
        "plateformes": platforms,
        "duree_jours": days,
        "date_debut": start_date.strftime("%d/%m/%Y"),
        "date_fin": (start_date + timedelta(days=days)).strftime("%d/%m/%Y"),
        "fuseau_horaire": "CET/CEST (Europe centrale)",
        "planning_publication": {p: POSTING_FREQUENCY.get(p, {}) for p in platforms},
        "piliers_contenu": {
            k: {"nom": v["name"], "description": v["description"], "frequence": ""}
            for k, v in CONTENT_PILLARS.items()
        },
        "repartition_piliers": {
            "educational": "40%",
            "behind_the_scenes": "15%",
            "social_proof": "15%",
            "engagement": "20%",
            "promotional": "10%"
        },
        "formules_accroches": {p: HOOK_FORMULAS.get(p, []) for p in platforms},
        "occasions_saisonnieres_fr": FRENCH_OCCASIONS,
        "calendrier": []
    }

    # Generate 30 days of content ideas
    pillar_rotation = ["educational", "engagement", "educational", "behind_the_scenes",
                       "educational", "social_proof", "promotional",
                       "educational", "engagement", "educational"]

    # French day names
    days_fr = {
        "Monday": "Lundi",
        "Tuesday": "Mardi",
        "Wednesday": "Mercredi",
        "Thursday": "Jeudi",
        "Friday": "Vendredi",
        "Saturday": "Samedi",
        "Sunday": "Dimanche"
    }

    for day in range(days):
        date = start_date + timedelta(days=day)
        day_of_week_en = date.strftime("%A")
        day_of_week_fr = days_fr.get(day_of_week_en, day_of_week_en)

        # Skip weekends for LinkedIn-heavy calendars
        pillar_key = pillar_rotation[day % len(pillar_rotation)]
        pillar = CONTENT_PILLARS[pillar_key]

        format_idx = day % len(pillar["formats"])
        content_format = pillar["formats"][format_idx]

        # Check for French seasonal occasions for this date
        month_occasions = FRENCH_OCCASIONS.get(date.month, [])

        # Generate a French-language post example
        post_example = _generate_french_post_example(pillar_key, topic, content_format, brand_name)

        day_entry = {
            "jour": day + 1,
            "date": date.strftime("%d/%m/%Y"),
            "jour_semaine": day_of_week_fr,
            "pilier": pillar["name"],
            "format": content_format,
            "angle_sujet": f"{content_format} sur {topic}",
            "exemple_publication": post_example,
            "occasions_du_mois": month_occasions,
            "plateformes": {}
        }

        for platform in platforms:
            if platform in pillar["platforms"]:
                day_entry["plateformes"][platform] = {
                    "conseils": pillar["platforms"][platform],
                    "publier": True
                }

        calendar["calendrier"].append(day_entry)

    # Add repurposing strategy in French
    calendar["strategie_revalorisation"] = {
        "description": "Transformez 1 contenu en 10+ publications sur toutes les plateformes",
        "methode": [
            f"1. Créez un contenu long sur {topic} (article de blog ou vidéo YouTube)",
            "2. Extrayez 5 à 7 idées clés sous forme de publications individuelles",
            "3. Adaptez chaque idée au format spécifique de chaque plateforme",
            "4. Créez un carrousel/fil à partir de l'article complet",
            "5. Tournez un résumé de 60 secondes en Reel/TikTok",
            "6. Extrayez des citations pour des publications visuelles",
            "7. Créez un sondage ou une question à partir d'une idée",
            "8. Partagez les coulisses de la création du contenu",
            "9. Repartagez les publications les plus performantes 2 à 4 semaines plus tard",
            "10. Créez une compilation 'best of' chaque mois"
        ]
    }

    return calendar


def _generate_french_post_example(pillar_key, topic, content_format, brand_name=None):
    """Generate a short French-language post example based on content pillar and format."""
    brand = brand_name or "notre marque"

    examples = {
        "educational": {
            "Guide pratique": f"Vous vous demandez comment {topic} peut transformer votre activité ? Voici notre guide étape par étape 👇 Enregistrez ce post pour y revenir plus tard !",
            "Astuce rapide": f"Astuce rapide sur {topic} : beaucoup d'entreprises oublient cette étape clé. En l'appliquant, nos clients ont vu leurs résultats doubler en 30 jours. Passez à l'action dès aujourd'hui !",
            "Démystification d'idée reçue": f"Idée reçue sur {topic} : « C'est trop compliqué à mettre en place. » Faux. Voici pourquoi — et ce que vous devriez faire à la place 👇",
            "Partage de méthode": f"La méthode que nous utilisons chez {brand} pour {topic} — et qui a tout changé pour nos clients européens :",
            "Recommandation d'outil": f"Les 3 outils indispensables pour réussir en {topic} selon notre équipe. Le n°2 vous surprendra !",
            "Tendance du secteur": f"Le secteur {topic} évolue rapidement en Europe. Voici les tendances à surveiller pour rester compétitif en 2025.",
            "Analyse de données": f"Nous avons analysé les données de 100 entreprises européennes sur {topic}. Voici ce que les chiffres révèlent :"
        },
        "behind_the_scenes": {
            "Une journée dans ma vie": f"Dans les coulisses de {brand} — voici à quoi ressemble une vraie journée de travail sur {topic} 📸",
            "Révélation de mes outils": f"Notre stack d'outils pour gérer {topic} au quotidien. Rien de superflu, tout ce qui compte vraiment.",
            "Présentation de mon processus": f"Comment nous abordons {topic} chez {brand}, de A à Z. Moins glamour que prévu, mais terriblement efficace.",
            "Erreur et leçon retenue": f"On a fait une grosse erreur sur {topic} l'an dernier. Voici ce qu'on a appris — pour que vous ne la reproduisiez pas.",
            "Partage de métriques/revenus": f"Bilan honnête de notre progression sur {topic} ce trimestre. Les chiffres, sans filtre.",
            "Équipe/espace de travail": f"L'équipe derrière {brand} vous dit bonjour ! Voici les visages qui travaillent chaque jour sur {topic}."
        },
        "social_proof": {
            "Succès client / étude de cas": f"Comment [Client] a amélioré ses résultats sur {topic} de 47% en 60 jours grâce à {brand}. Étude de cas complète 👇",
            "Partage de témoignage": f"« Depuis que nous travaillons avec {brand} sur {topic}, notre retour sur investissement a été multiplié par 3. » — Directeur Marketing, PME française",
            "Avant / Après": f"Avant {brand} : {topic} leur prenait 8h par semaine. Après : 45 minutes. Voici comment.",
            "Jalon de chiffre d'affaires": f"Une étape importante franchie chez {brand} ! Merci à toute notre communauté qui nous fait confiance sur {topic} 🎉",
            "Contenu généré par les utilisateurs": f"Un de nos clients a partagé son expérience sur {topic}. Leurs mots valent mieux que les nôtres 💬",
            "Récompense / Reconnaissance": f"{brand} reconnu parmi les meilleures solutions européennes pour {topic} 🏆 Merci à tous nos clients fidèles !"
        },
        "engagement": {
            "Prise de position / Opinion": f"Prise de position : la majorité des entreprises abordent {topic} à l'envers. Êtes-vous d'accord ? Dites-le en commentaire 👇",
            "Question à la communauté": f"Question ouverte : quel est votre plus grand défi avec {topic} en ce moment ? Partagez en commentaire — vos réponses nous aident à mieux vous accompagner.",
            "Sondage": f"Sondage rapide : comment gérez-vous {topic} dans votre entreprise ? A) Manuellement B) Avec des outils C) Sous-traité D) Pas encore",
            "L'un ou l'autre": f"{topic} : vous préférez faire appel à un expert ou tout gérer en interne ? Votez et dites-nous pourquoi !",
            "Opinion impopulaire": f"Opinion impopulaire : trop d'entreprises françaises investissent dans {topic} avant d'avoir posé les bonnes bases. Vous en pensez quoi ?",
            "D'accord ou pas ?": f"D'accord ou pas ? « {topic} est désormais incontournable pour toute entreprise qui veut rester compétitive en Europe. » Commentez 👇",
            "Complétez la phrase": f"Complétez la phrase : « La chose la plus importante à savoir sur {topic}, c'est... » Partagez votre réponse !"
        },
        "promotional": {
            "Démo produit": f"Découvrez en 2 minutes comment {brand} simplifie {topic} pour les équipes européennes. Lien en bio 👆",
            "Mise en avant d'une fonctionnalité": f"Nouvelle fonctionnalité {brand} : gérez {topic} encore plus facilement, directement depuis votre tableau de bord.",
            "Offre spéciale": f"Offre limitée : accédez à {brand} avec 20% de réduction ce mois-ci. Idéal pour démarrer sur {topic} sans risque. Lien en bio.",
            "Promo webinaire/événement": f"Webinaire gratuit : « Maîtriser {topic} pour les entreprises européennes » — {brand} vous invite. Places limitées !",
            "Ressource gratuite": f"Téléchargez gratuitement notre guide complet sur {topic}. Conçu pour le marché français et européen. Lien en bio 📥",
            "Invitation à rejoindre la communauté": f"Rejoignez notre communauté de professionnels européens qui maîtrisent {topic} avec {brand}. Lien en bio pour commencer !"
        }
    }

    pillar_examples = examples.get(pillar_key, {})
    return pillar_examples.get(content_format, f"Publication sur {topic} — format : {content_format}")


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "utilisation": "python3 social_calendar.py <sujet> [plateforme1,plateforme2,...] [jours]",
            "exemple": "python3 social_calendar.py 'automatisation IA' linkedin,twitter,instagram 30",
            "description": "Génère un calendrier de contenu pour les réseaux sociaux — édition marché européen/français",
            "plateformes_disponibles": list(POSTING_FREQUENCY.keys()),
            "fuseaux_horaires": "CET (UTC+1) / CEST (UTC+2) en été",
            "occasions_saisonnieres": "Calendrier français et européen intégré (Soldes, Fêtes nationales, etc.)"
        }, indent=2, ensure_ascii=False))
        return

    topic = sys.argv[1]
    platforms = sys.argv[2].split(",") if len(sys.argv) > 2 else ["linkedin", "twitter", "instagram"]
    days = int(sys.argv[3]) if len(sys.argv) > 3 else 30

    calendar = generate_calendar(topic, platforms, days)
    print(json.dumps(calendar, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
