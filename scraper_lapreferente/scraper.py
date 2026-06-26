#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scraper de la División de Honor Andaluza Grupo 1 Senior en lapreferente.com

Objetivo:
  1) Reconstruir el ranking HISTÓRICO de PARTIDOS JUGADOS por jugador
     (lapreferente NO publica este ranking agregado: hay que sumarlo
     temporada a temporada).
  2) Recoger TODOS los goleadores temporada a temporada y su agregado
     histórico desde la temporada 2016/2017 (primera edición).

Por qué este diseño:
  El HTML concreto de lapreferente.com no pudo inspeccionarse durante el
  desarrollo (la red del entorno donde se generó este script bloqueaba el
  dominio). Para ser resistente a no conocer las clases CSS exactas, el
  parser NO depende de selectores frágiles: detecta las tablas relevantes
  por el TEXTO de sus cabeceras (Jugador, Goles, PJ/Partidos, Equipo).
  Esto funciona con la estructura estándar de tablas <table> que usa el
  sitio. Si alguna cabecera tiene un nombre distinto, basta con añadir el
  alias en los conjuntos COL_* de abajo.

Uso:
  pip install -r requirements.txt
  python scraper.py --discover            # descubre los IDs de cada temporada
  python scraper.py                        # scrapea con los IDs de SEASONS
  python scraper.py --out resultados/      # carpeta de salida

Salida (carpeta --out, por defecto ./salida):
  - goleadores_<temporada>.csv     (por temporada)
  - goleadores_historico.csv       (agregado de goles por jugador)
  - partidos_<temporada>.csv       (PJ por jugador y temporada)
  - partidos_historico.csv         (agregado de PJ por jugador)  <-- ranking pedido
  - resumen.json                   (líderes: + partidos y + goles histórico)

NOTA legal/ética: respeta robots.txt y el ritmo de peticiones (DELAY).
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import unicodedata
from collections import defaultdict
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE = "https://www.lapreferente.com"

# Página de la competición (temporada más reciente conocida).
# Desde aquí --discover intentará localizar el resto de temporadas.
COMPETITION_SLUG = "division-honor-andaluza-gr1"
SEED_URL = f"{BASE}/C8253-1/{COMPETITION_SLUG}/"

# Mapa temporada -> URL base de esa temporada en la competición.
# Rellénalo con la salida de `--discover`. Ejemplo de formato:
#   "2024/2025": f"{BASE}/C8253-1/{COMPETITION_SLUG}/",
#   "2023/2024": f"{BASE}/C7xxx-1/{COMPETITION_SLUG}/",
#   ...
#   "2016/2017": f"{BASE}/C2xxx-1/{COMPETITION_SLUG}/",   # primera edición
SEASONS = {
    # "2024/2025": f"{BASE}/C8253-1/{COMPETITION_SLUG}/",
}

# ---------------------------------------------------------------------------
# Configuración de red
# ---------------------------------------------------------------------------
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept-Language": "es-ES,es;q=0.9",
}
DELAY = 1.5          # segundos entre peticiones (sé educado)
TIMEOUT = 25
MAX_RETRIES = 4

# Alias de cabeceras de tabla (normalizados: minúsculas, sin acentos)
COL_PLAYER = {"jugador", "nombre", "futbolista"}
COL_TEAM = {"equipo", "club"}
COL_GOALS = {"goles", "gol", "g", "goleador"}
COL_GAMES = {"pj", "partidos", "partidosjugados", "pjug", "j", "jugados"}


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def norm(s: str) -> str:
    """minúsculas, sin acentos, sin espacios extra: para comparar cabeceras."""
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", "", s.strip().lower())


def name_key(name: str) -> str:
    """Clave para agregar el mismo jugador entre temporadas."""
    s = unicodedata.normalize("NFKD", name or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s.strip().lower())


def get(session: requests.Session, url: str) -> BeautifulSoup | None:
    """GET con reintentos y backoff exponencial."""
    delay = 2
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = session.get(url, headers=HEADERS, timeout=TIMEOUT)
            if r.status_code == 200:
                return BeautifulSoup(r.text, "html.parser")
            if r.status_code in (403, 404):
                print(f"  [{r.status_code}] {url}", file=sys.stderr)
                return None
            print(f"  [HTTP {r.status_code}] reintento {attempt} {url}", file=sys.stderr)
        except requests.RequestException as e:
            print(f"  [err] reintento {attempt}: {e}", file=sys.stderr)
        time.sleep(delay)
        delay *= 2
    return None


def parse_table_by_headers(soup: BeautifulSoup, want_cols: dict[str, set]):
    """
    Recorre todas las <table> y devuelve las filas (un dict por fila, con
    clave = etiqueta lógica de columna) de la PRIMERA tabla cuyas cabeceras
    incluyan TODAS las columnas pedidas.

    `want_cols` es {etiqueta_logica: conjunto_de_alias_de_cabecera}, p.ej.
    {"jugador": COL_PLAYER, "goles": COL_GOALS}.
    """
    for table in soup.find_all("table"):
        headers = []
        header_row = table.find("tr")
        if not header_row:
            continue
        for th in header_row.find_all(["th", "td"]):
            headers.append(norm(th.get_text()))

        # Construir índice etiqueta->posición usando los alias de cabecera
        def find_idx(aliases):
            for i, h in enumerate(headers):
                if h in aliases:
                    return i
            return None

        col_index = {}
        ok = True
        for label, aliases in want_cols.items():
            i = find_idx(aliases)
            if i is None:
                ok = False
                break
            col_index[label] = i
        if not ok:
            continue

        rows = []
        for tr in table.find_all("tr")[1:]:
            cells = tr.find_all(["td", "th"])
            if len(cells) <= max(col_index.values()):
                continue
            row = {}
            for label, i in col_index.items():
                row[label] = cells[i].get_text(strip=True)
            rows.append(row)
        if rows:
            return rows
    return []


def discover_seasons(session: requests.Session):
    """
    Intenta localizar los enlaces a temporadas anteriores desde la página
    semilla. lapreferente suele exponer un <select> de temporadas o enlaces
    que apuntan a otros IDs de competición con el mismo slug.
    """
    soup = get(session, SEED_URL)
    if not soup:
        print("No se pudo cargar la página semilla. ¿Bloqueo de red? "
              "Rellena SEASONS manualmente.", file=sys.stderr)
        return {}
    found = {}
    # 1) <option> dentro de selects de temporada
    for opt in soup.find_all("option"):
        txt = opt.get_text(strip=True)
        val = opt.get("value", "")
        m = re.search(r"(20\d{2})\s*[/\-]\s*(\d{2,4})", txt)
        if m and val:
            url = val if val.startswith("http") else urljoin(BASE, val)
            found[txt] = url
    # 2) enlaces que contienen el slug y un patrón de temporada en el texto
    for a in soup.find_all("a", href=True):
        txt = a.get_text(strip=True)
        m = re.search(r"(20\d{2})\s*[/\-]\s*(\d{2,4})", txt)
        if m and COMPETITION_SLUG in a["href"]:
            found[txt] = urljoin(BASE, a["href"])
    return found


def scrape_goleadores(session, season, base_url):
    """Goleadores de una temporada -> lista de {jugador, equipo, goles}."""
    url = urljoin(base_url, "goleadores.html")
    print(f"  goleadores: {url}")
    soup = get(session, url)
    if not soup:
        return []
    rows = parse_table_by_headers(soup, {
        "jugador": COL_PLAYER,
        "goles": COL_GOALS,
    })
    out = []
    for r in rows:
        try:
            goles = int(re.sub(r"\D", "", r.get("goles", "0")) or 0)
        except ValueError:
            goles = 0
        out.append({
            "temporada": season,
            "jugador": r.get("jugador", "").strip(),
            "equipo": r.get("equipo", "").strip(),
            "goles": goles,
        })
    return out


def scrape_partidos(session, season, base_url):
    """
    Partidos jugados (PJ) por jugador en una temporada.
    Estrategia: recorrer las plantillas de los equipos (suelen incluir una
    tabla con PJ y goles por jugador). Si no existen, este apartado quedará
    vacío y habrá que reconstruir PJ desde las alineaciones de cada partido
    (ver scrape_partidos_desde_alineaciones, más costoso).
    """
    # Localizar equipos desde la clasificación
    clasif_url = urljoin(base_url, "clasificacion.html")
    soup = get(session, clasif_url)
    if not soup:
        return []
    team_links = {}
    for a in soup.find_all("a", href=True):
        href = a["href"]
        # enlaces a fichas de equipo en lapreferente suelen llevar /E<id>
        if re.search(r"/E\d+", href):
            team_links[a.get_text(strip=True)] = urljoin(BASE, href)

    rows_out = []
    for team, turl in team_links.items():
        tsoup = get(session, turl)
        time.sleep(DELAY)
        if not tsoup:
            continue
        rows = parse_table_by_headers(tsoup, {
            "jugador": COL_PLAYER,
            "pj": COL_GAMES,
        })
        for r in rows:
            try:
                pj = int(re.sub(r"\D", "", r.get("pj", "0")) or 0)
            except ValueError:
                pj = 0
            rows_out.append({
                "temporada": season,
                "jugador": r.get("jugador", "").strip(),
                "equipo": team,
                "partidos": pj,
            })
    return rows_out


def write_csv(path, rows, fields):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})
    print(f"  -> {path} ({len(rows)} filas)")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--discover", action="store_true",
                    help="Solo descubrir IDs/temporadas y salir.")
    ap.add_argument("--out", default="salida", help="Carpeta de salida.")
    args = ap.parse_args()

    session = requests.Session()

    if args.discover:
        found = discover_seasons(session)
        if not found:
            print("No se encontraron temporadas automáticamente.")
        else:
            print("Temporadas encontradas (cópialas a SEASONS):\n")
            for k, v in sorted(found.items(), reverse=True):
                print(f'    "{k}": "{v}",')
        return

    if not SEASONS:
        print("SEASONS está vacío. Ejecuta primero `python scraper.py --discover` "
              "y pega el resultado en la variable SEASONS.", file=sys.stderr)
        sys.exit(1)

    all_gol, all_pj = [], []
    for season, base_url in SEASONS.items():
        print(f"\n== Temporada {season} ==")
        gol = scrape_goleadores(session, season, base_url)
        time.sleep(DELAY)
        pj = scrape_partidos(session, season, base_url)
        time.sleep(DELAY)
        all_gol.extend(gol)
        all_pj.extend(pj)
        if gol:
            write_csv(os.path.join(args.out, f"goleadores_{season.replace('/', '-')}.csv"),
                      gol, ["temporada", "jugador", "equipo", "goles"])
        if pj:
            write_csv(os.path.join(args.out, f"partidos_{season.replace('/', '-')}.csv"),
                      pj, ["temporada", "jugador", "equipo", "partidos"])

    # Agregados históricos
    gol_hist = defaultdict(lambda: {"jugador": "", "goles": 0, "equipos": set()})
    for r in all_gol:
        k = name_key(r["jugador"])
        gol_hist[k]["jugador"] = r["jugador"]
        gol_hist[k]["goles"] += r["goles"]
        if r["equipo"]:
            gol_hist[k]["equipos"].add(r["equipo"])

    pj_hist = defaultdict(lambda: {"jugador": "", "partidos": 0, "equipos": set()})
    for r in all_pj:
        k = name_key(r["jugador"])
        pj_hist[k]["jugador"] = r["jugador"]
        pj_hist[k]["partidos"] += r["partidos"]
        if r["equipo"]:
            pj_hist[k]["equipos"].add(r["equipo"])

    gol_rows = sorted(
        [{"jugador": v["jugador"], "goles": v["goles"],
          "equipos": ", ".join(sorted(v["equipos"]))} for v in gol_hist.values()],
        key=lambda x: x["goles"], reverse=True)
    pj_rows = sorted(
        [{"jugador": v["jugador"], "partidos": v["partidos"],
          "equipos": ", ".join(sorted(v["equipos"]))} for v in pj_hist.values()],
        key=lambda x: x["partidos"], reverse=True)

    if gol_rows:
        write_csv(os.path.join(args.out, "goleadores_historico.csv"),
                  gol_rows, ["jugador", "goles", "equipos"])
    if pj_rows:
        write_csv(os.path.join(args.out, "partidos_historico.csv"),
                  pj_rows, ["jugador", "partidos", "equipos"])

    resumen = {
        "competicion": "División de Honor Andaluza Grupo 1 Senior",
        "temporadas_scrapeadas": list(SEASONS.keys()),
        "lider_partidos_historico": pj_rows[0] if pj_rows else None,
        "max_goleador_historico": gol_rows[0] if gol_rows else None,
        "top10_partidos": pj_rows[:10],
        "top10_goleadores": gol_rows[:10],
    }
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "resumen.json"), "w", encoding="utf-8") as f:
        json.dump(resumen, f, ensure_ascii=False, indent=2)
    print(f"\n  -> {os.path.join(args.out, 'resumen.json')}")

    if pj_rows:
        print(f"\nLíder histórico de partidos: {pj_rows[0]['jugador']} "
              f"({pj_rows[0]['partidos']} PJ)")
    if gol_rows:
        print(f"Máximo goleador histórico: {gol_rows[0]['jugador']} "
              f"({gol_rows[0]['goles']} goles)")


if __name__ == "__main__":
    main()
