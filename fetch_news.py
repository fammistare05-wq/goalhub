#!/usr/bin/env python3
"""Scarica le notizie dalle fonti RSS e le salva in notizie.json.

Gira sui server di GitHub ogni 10 minuti. Usa solo librerie standard:
nessuna installazione, nessuna chiave, parte in pochi secondi.
"""
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from urllib.parse import quote

UA = {"User-Agent": "Mozilla/5.0 (compatible; GoalHubZone/1.0)"}


def gnews(q, hl="it", gl="IT", ceid="IT:it"):
    return (f"https://news.google.com/rss/search?q={quote(q)}"
            f"&hl={hl}&gl={gl}&ceid={ceid}")


CLUB = ["Inter", "Milan", "Juventus", "Napoli", "Roma", "Lazio", "Atalanta",
        "Fiorentina", "Bologna", "Torino", "Como", "Udinese", "Genoa",
        "Cagliari", "Parma", "Sassuolo", "Lecce", "Verona"]

FONTI = [
    ("TuttoMercatoWeb", "https://www.tuttomercatoweb.com/rss", "it", "🇮🇹"),
    ("Calciomercato.com", "https://www.calciomercato.com/rss", "it", "🇮🇹"),
    ("Sky Sport", "https://www.skysport.it/rss/calciomercato.xml", "it", "🇮🇹"),
    ("Gazzetta", "https://www.gazzetta.it/rss/calciomercato.xml", "it", "🇮🇹"),
    ("Corriere dello Sport", "https://www.corrieredellosport.it/rss/calciomercato", "it", "🇮🇹"),
    ("Di Marzio", "https://www.gianlucadimarzio.com/it/feed", "it", "🇮🇹"),
    ("Calcionews24", "https://www.calcionews24.com/feed/", "it", "🇮🇹"),
    ("Serie A ufficiali", gnews("calciomercato ufficiale firma when:1d"), "it", "🇮🇹"),
    ("Serie B", gnews("Serie B calciomercato when:1d"), "it", "🇮🇹"),
    ("BBC Sport", "https://feeds.bbci.co.uk/sport/football/rss.xml", "uk", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"),
    ("The Guardian", "https://www.theguardian.com/football/rss", "uk", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"),
    ("Sky Sports", "https://www.skysports.com/rss/12040", "uk", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"),
    ("Daily Mirror", "https://www.mirror.co.uk/sport/football/transfer-news/?service=rss", "uk", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"),
    ("Premier League", gnews("Premier League transfer when:1d", "en-GB", "GB", "GB:en"), "uk", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"),
    ("Marca", "https://e00-marca.uecdn.es/rss/futbol/mas-futbol.xml", "es", "🇪🇸"),
    ("AS", "https://as.com/rss/futbol/portada.xml", "es", "🇪🇸"),
    ("Mundo Deportivo", "https://www.mundodeportivo.com/feed/rss/futbol", "es", "🇪🇸"),
    ("LaLiga", gnews("fichajes LaLiga cuando:1d", "es", "ES", "ES:es"), "es", "🇪🇸"),
    ("L'Equipe", "https://www.lequipe.fr/rss/actu_actualites_football.xml", "fr", "🇫🇷"),
    ("RMC Sport", "https://rmcsport.bfmtv.com/rss/football/", "fr", "🇫🇷"),
    ("Ligue 1", gnews("Ligue 1 transfert mercato when:1d", "fr", "FR", "FR:fr"), "fr", "🇫🇷"),
    ("Kicker", "https://newsfeed.kicker.de/news/fussball", "de", "🇩🇪"),
    ("Bundesliga", gnews("Bundesliga Transfer wechsel when:1d", "de", "DE", "DE:de"), "de", "🇩🇪"),
    ("ESPN", "https://www.espn.com/espn/rss/soccer/news", "world", "🌍"),
    ("Fabrizio Romano", gnews('"Fabrizio Romano" when:1d', "en-US", "US", "US:en"), "world", "🌍"),
    ("Here we go", gnews('"here we go" transfer when:1d', "en-US", "US", "US:en"), "world", "🌍"),
    ("Mercato mondiale", gnews("official transfer signing football when:1d", "en-US", "US", "US:en"), "world", "🌍"),
] + [(f"{c} mercato", gnews(f"{c} calciomercato when:1d"), "it", "🇮🇹") for c in CLUB]

PAROLE = ["ufficiale", "here we go", "firma", "firmato", "accordo", "visite mediche",
          "prestito", "rinnovo", "offerta", "colpo", "cessione", "clausola",
          "trattativa", "mercato", "transfer", "signing", "signs", "deal",
          "medical", "agreement", "loan", "bid", "fichaje", "acuerdo", "traspaso",
          "transfert", "wechsel", "verpflichtet"]


def pulisci(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t or "")).strip()


def leggi(fonte):
    nome, url, cc, flag = fonte
    try:
        req = urllib.request.Request(url, headers=UA)
        raw = urllib.request.urlopen(req, timeout=25).read()
        root = ET.fromstring(raw)
    except Exception as exc:
        print(f"  KO  {nome}: {type(exc).__name__}")
        return []

    out = []
    for it in root.iter():
        if not it.tag.endswith("item") and not it.tag.endswith("entry"):
            continue
        titolo = desc = data = ""
        for ch in it:
            tag = ch.tag.split("}")[-1]
            if tag == "title":
                titolo = pulisci(ch.text)
            elif tag in ("description", "summary", "content"):
                desc = pulisci(ch.text)
            elif tag in ("pubDate", "published", "updated"):
                data = (ch.text or "").strip()
        if not titolo:
            continue
        blob = (titolo + " " + desc).lower()
        if not any(k in blob for k in PAROLE):
            continue
        quando = 0
        if data:
            try:
                quando = int(parsedate_to_datetime(data).timestamp() * 1000)
            except Exception:
                try:
                    quando = int(datetime.fromisoformat(
                        data.replace("Z", "+00:00")).timestamp() * 1000)
                except Exception:
                    quando = 0
        out.append({"title": titolo, "desc": desc[:190], "src": nome,
                    "cc": cc, "flag": flag, "when": quando})
    print(f"  OK  {nome}: {len(out)}")
    return out


def main():
    print(f"Leggo {len(FONTI)} fonti…")
    with ThreadPoolExecutor(max_workers=10) as ex:
        gruppi = list(ex.map(leggi, FONTI))

    items = [n for g in gruppi for n in g]

    visti, unici = set(), []
    for n in items:
        k = "".join(sorted(re.sub(r"[^a-z0-9 ]", "", n["title"].lower()).split()))
        if k in visti:
            continue
        visti.add(k)
        unici.append(n)

    unici.sort(key=lambda n: n["when"], reverse=True)
    unici = unici[:500]

    dati = {
        "aggiornato": int(datetime.now(timezone.utc).timestamp() * 1000),
        "fonti_ok": sum(1 for g in gruppi if g),
        "fonti_totali": len(FONTI),
        "notizie": unici,
    }
    with open("notizie.json", "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, separators=(",", ":"))
    print(f"\n✓ {len(unici)} notizie salvate da {dati['fonti_ok']}/{len(FONTI)} fonti")


if __name__ == "__main__":
    main()
