#!/usr/bin/env python3
"""
Competitor Scanner — Utility script for AI Marketing Claude Code Skills
Scans competitor websites to extract positioning, pricing, features, and trust signals
for competitive analysis.
"""

import sys
import json
import re
import urllib.request
import urllib.error
import ssl
from html.parser import HTMLParser
from urllib.parse import urlparse


class CompetitorPageParser(HTMLParser):
    """Parse competitor page for positioning data."""

    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta_description = ""
        self.og_title = ""
        self.og_description = ""
        self.h1_tags = []
        self.h2_tags = []
        self.pricing_indicators = []
        self.social_links = []
        self.trust_signals = []
        self.ctas = []
        self.testimonial_count = 0
        self.logo_count = 0

        self._in_title = False
        self._in_h1 = False
        self._in_h2 = False
        self._in_a = False
        self._in_button = False
        self._current_text = ""
        self._all_text = []
        self._current_href = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == "title":
            self._in_title = True
            self._current_text = ""
        elif tag == "meta":
            name = attrs_dict.get("name", "").lower()
            prop = attrs_dict.get("property", "").lower()
            content = attrs_dict.get("content", "")
            if name == "description":
                self.meta_description = content
            elif prop == "og:title":
                self.og_title = content
            elif prop == "og:description":
                self.og_description = content
        elif tag == "h1":
            self._in_h1 = True
            self._current_text = ""
        elif tag == "h2":
            self._in_h2 = True
            self._current_text = ""
        elif tag == "a":
            self._in_a = True
            self._current_text = ""
            self._current_href = attrs_dict.get("href", "")
            # Social links
            social_platforms = {"twitter.com": "Twitter/X", "x.com": "Twitter/X",
                                "facebook.com": "Facebook", "linkedin.com": "LinkedIn",
                                "instagram.com": "Instagram", "youtube.com": "YouTube",
                                "tiktok.com": "TikTok", "github.com": "GitHub"}
            href = attrs_dict.get("href", "")
            for domain, name in social_platforms.items():
                if domain in href:
                    self.social_links.append({"plateforme": name, "url": href})
        elif tag == "button":
            self._in_button = True
            self._current_text = ""
        elif tag == "img":
            alt = attrs_dict.get("alt", "").lower()
            src = attrs_dict.get("src", "").lower()
            # Count customer logos
            if any(word in alt for word in ["logo", "client", "partner", "customer", "trusted", "partenaire"]):
                self.logo_count += 1
            if any(word in src for word in ["logo", "client", "partner", "partenaire"]):
                self.logo_count += 1

    def handle_endtag(self, tag):
        if tag == "title" and self._in_title:
            self._in_title = False
            self.title = self._current_text.strip()
        elif tag == "h1" and self._in_h1:
            self._in_h1 = False
            text = self._current_text.strip()
            if text:
                self.h1_tags.append(text)
        elif tag == "h2" and self._in_h2:
            self._in_h2 = False
            text = self._current_text.strip()
            if text:
                self.h2_tags.append(text)
        elif tag == "a" and self._in_a:
            self._in_a = False
            text = self._current_text.strip()
            cta_words = ["sign up", "get started", "try free", "start", "buy", "subscribe",
                         "join", "register", "download", "book", "demo", "contact", "pricing",
                         "essayer", "commencer", "s'inscrire", "acheter", "réserver", "démo",
                         "contactez", "tarifs", "télécharger"]
            if any(w in text.lower() for w in cta_words):
                self.ctas.append(text)
        elif tag == "button" and self._in_button:
            self._in_button = False
            text = self._current_text.strip()
            if text:
                self.ctas.append(text)

    def handle_data(self, data):
        if self._in_title or self._in_h1 or self._in_h2 or self._in_a or self._in_button:
            self._current_text += data
        self._all_text.append(data.strip())

        # Detect pricing indicators
        text_lower = data.lower().strip()
        pricing_patterns = [r"\$\d+", r"€\d+", r"£\d+", r"/mois", r"/an", r"/month", r"/year", r"/mo",
                            r"par mois", r"par an", r"annuel", r"forfait gratuit",
                            r"essai gratuit", r"free plan", r"free tier", r"free trial", r"enterprise"]
        for pattern in pricing_patterns:
            if re.search(pattern, text_lower):
                self.pricing_indicators.append(data.strip())
                break

        # Detect testimonials
        testimonial_words = ["testimonial", "avis", "témoignage", "ce que disent nos clients",
                             "ils nous font confiance", "étude de cas", "success story",
                             "review", "said about", "what our customers", "customer stories"]
        if any(w in text_lower for w in testimonial_words):
            self.testimonial_count += 1

    def get_results(self):
        full_text = " ".join(self._all_text)
        word_count = len(full_text.split())

        # Extract positioning
        positioning = self.og_description or self.meta_description or ""
        if self.h1_tags:
            positioning = self.h1_tags[0]

        return {
            "positionnement": {
                "accroche": self.h1_tags[0] if self.h1_tags else self.title,
                "slogan": self.meta_description,
                "og_titre": self.og_title,
                "og_description": self.og_description,
                "sections_cles": self.h2_tags[:10]
            },
            "tarification": {
                "infos_tarifs_disponibles": len(self.pricing_indicators) > 0,
                "mentions_tarifs": list(set(self.pricing_indicators))[:10]
            },
            "confiance": {
                "plateformes_sociales": [s["plateforme"] for s in self.social_links],
                "nombre_liens_sociaux": len(self.social_links),
                "nombre_logos_estimes": self.logo_count,
                "temoignages_presents": self.testimonial_count > 0,
                "sites_avis": ["Trustpilot.fr", "Avis Vérifiés", "Google Avis France"]
            },
            "appels_action": list(set(self.ctas))[:10],
            "contenu": {
                "nombre_mots": word_count,
                "nombre_sections": len(self.h2_tags)
            }
        }


def fetch_page(url):
    """Fetch a webpage."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.5",
    }

    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req, timeout=15, context=ctx)
        return response.read().decode("utf-8", errors="replace")
    except:
        return None


def scan_competitor(url):
    """Scan a competitor website."""
    if not url.startswith("http"):
        url = "https://" + url

    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "")

    result = {
        "url": url,
        "domaine": domain,
        "statut": "succès"
    }

    html = fetch_page(url)
    if not html:
        result["statut"] = "erreur"
        result["message"] = "Impossible de récupérer la page"
        return result

    parser = CompetitorPageParser()
    try:
        parser.feed(html)
    except:
        result["statut"] = "erreur"
        result["message"] = "Impossible d'analyser la page"
        return result

    result["donnees"] = parser.get_results()

    # Try to fetch pricing page
    pricing_urls = [
        f"https://{parsed.netloc}/pricing",
        f"https://{parsed.netloc}/tarifs",
        f"https://{parsed.netloc}/plans",
        f"https://{parsed.netloc}/price",
    ]

    for pricing_url in pricing_urls:
        pricing_html = fetch_page(pricing_url)
        if pricing_html and len(pricing_html) > 1000:
            pricing_parser = CompetitorPageParser()
            try:
                pricing_parser.feed(pricing_html)
                pricing_data = pricing_parser.get_results()
                result["page_tarifs"] = {
                    "url": pricing_url,
                    "trouvee": True,
                    "mentions_tarifs": pricing_data["tarification"]["mentions_tarifs"],
                    "sections": pricing_data["positionnement"]["sections_cles"]
                }
            except:
                pass
            break
    else:
        result["page_tarifs"] = {"trouvee": False}

    return result


def scan_multiple(urls):
    """Scan multiple competitor URLs."""
    results = []
    for url in urls:
        result = scan_competitor(url)
        results.append(result)
    return results


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "utilisation": "python3 competitor_scanner.py <url1> [url2] [url3] ...",
            "exemple": "python3 competitor_scanner.py calendly.com acuityscheduling.com doodle.com",
            "description": "Analyse concurrentielle : positionnement, tarification et signaux de confiance des concurrents",
            "titre_rapport": "Analyse Concurrentielle",
            "presence_reseaux": "Présence sur les Réseaux Sociaux",
            "sites_avis_fr": ["Trustpilot.fr", "Avis Vérifiés", "Google Avis France"]
        }, indent=2, ensure_ascii=False))
        return

    urls = sys.argv[1:]
    if len(urls) == 1:
        result = scan_competitor(urls[0])
        print(json.dumps(result, indent=2, default=str, ensure_ascii=False))
    else:
        results = scan_multiple(urls)
        print(json.dumps({"analyse_concurrentielle": results}, indent=2, default=str, ensure_ascii=False))


if __name__ == "__main__":
    main()
