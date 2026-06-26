# Scraper — División de Honor Andaluza Grupo 1 Senior (lapreferente.com)

Recoge, desde **lapreferente.com**, los datos de la **División de Honor Andaluza
Grupo 1 Senior** (Andalucía) desde su primera edición **2016/2017** y construye:

- El **ranking histórico de partidos jugados (PJ)** por jugador → responde a
  *"¿quién es el jugador con más partidos en la historia?"*.
- **Todos los goleadores** temporada a temporada y su **agregado histórico**.

## ⚠️ Por qué no se ejecutó aquí

Este script se generó dentro de un entorno remoto cuya **política de red
bloqueaba el dominio `lapreferente.com`** (el proxy de egress respondía `403`
al `CONNECT`). Por eso no se pudo:

1. inspeccionar el HTML real para fijar selectores exactos, ni
2. ejecutar el scraping y entregar los datos ya extraídos.

El parser se diseñó para ser **robusto a no conocer el DOM**: localiza las
tablas por el **texto de sus cabeceras** (`Jugador`, `Goles`, `PJ`/`Partidos`,
`Equipo`), no por clases CSS. Ejecútalo en una máquina **con acceso libre a
internet**.

## Uso

```bash
pip install -r requirements.txt

# 1) Descubrir las URLs de cada temporada (2016/17 … actual)
python scraper.py --discover
#    Copia la salida dentro de la variable SEASONS en scraper.py

# 2) Scrapear y generar los CSV/JSON
python scraper.py --out salida/
```

## Salida (`salida/`)

| Fichero                          | Contenido                                            |
|----------------------------------|------------------------------------------------------|
| `goleadores_<temporada>.csv`     | Goleadores de cada temporada (jugador, equipo, goles)|
| `goleadores_historico.csv`       | Goles agregados por jugador (todas las temporadas)   |
| `partidos_<temporada>.csv`       | PJ por jugador en cada temporada                     |
| `partidos_historico.csv`         | **PJ agregados por jugador → ranking histórico**     |
| `resumen.json`                   | Líder de partidos y máximo goleador histórico + top 10|

## Notas y limitaciones

- **Partidos jugados**: lapreferente **no publica** un ranking histórico de PJ.
  El script lo reconstruye sumando los PJ de las plantillas de cada equipo en
  cada temporada. Si una temporada no expone PJ en la ficha de equipo, hay que
  reconstruirlos desde las **alineaciones** de cada partido (más costoso; el
  código deja indicado dónde añadir esa estrategia en `scrape_partidos`).
- **Nombres**: la agregación entre temporadas usa el nombre normalizado
  (minúsculas, sin acentos). Homónimos o cambios de grafía pueden requerir
  revisión manual.
- **Selectores**: si alguna cabecera de tabla tiene un nombre distinto al
  esperado, añade el alias en los conjuntos `COL_PLAYER / COL_TEAM / COL_GOALS /
  COL_GAMES` al inicio de `scraper.py`.
- Sé respetuoso con el sitio: `DELAY` controla el ritmo de peticiones; revisa
  `robots.txt` y las condiciones de uso de lapreferente.com.
