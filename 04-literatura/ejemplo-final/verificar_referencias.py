"""Verifica las referencias citadas en los artículos de ../articulos/ contra Crossref.

Para cada referencia:
  1. Busca su DOI en Crossref (https://api.crossref.org).
  2. Si existe, compara año, primer autor y título con lo que dice la cita.
  3. Si no existe, revisa si es uno de los artículos del corpus del taller.
Resultado: verificacion_referencias.csv

Uso:  python verificar_referencias.py
Requiere: pypdf, requests, pandas
"""
import re
import time
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

import pandas as pd
import requests
from pypdf import PdfReader

CARPETA = Path(__file__).parent / ".." / "articulos"
UA = {"User-Agent": "taller-claude-code-cide/1.0 (https://github.com/benjov/taller-claude-code-cide)"}
RE_DOI = re.compile(r"https://doi\.org/(10\.\d{4,9}/[^\s]+?)(?=\s|$)")
RE_CITA = re.compile(r"^(?P<autores>.+?) \((?P<anio>\d{4})\)\. (?P<titulo>.+?)\. (?P<resto>.+)$")


def normaliza(t):
    t = re.sub(r"<[^>]+>", "", t)                       # Crossref a veces trae etiquetas HTML
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9 ]", "", t.lower()).strip()


def texto_pdf(ruta):
    return re.sub(r"\s+", " ", " ".join(p.extract_text() or "" for p in PdfReader(ruta).pages))


# 1) Metadatos de los artículos del corpus y referencias que citan
corpus, citas = {}, []
for pdf in sorted(CARPETA.glob("*.pdf")):
    txt = texto_pdf(pdf)
    doi_propio = re.search(r"DOI: (10\.\S+)", txt).group(1)
    anio_propio = int(re.search(r"\((\d{4})\) · DOI", txt).group(1))
    corpus[doi_propio] = {"archivo": pdf.name, "anio": anio_propio}
    refs = txt.split("Referencias", 1)[1]
    refs = re.sub(r"ARTÍCULO FICTICIO.*?inventados|[\w ]+, \d+\(\d+\) p\. \d+", " ", refs)
    for m in RE_DOI.finditer(refs):
        inicio = refs.rfind("https://doi.org/", 0, m.start())
        inicio = 0 if inicio < 0 else refs.find(" ", inicio) + 1
        cita = refs[inicio:m.start()].strip()
        citas.append({"citado_en": pdf.name, "cita": cita, "doi": m.group(1).rstrip(".")})

# 2) Verificación
resultados, cache = [], {}
for c in citas:
    m = RE_CITA.match(c["cita"])
    anio_cit = int(m["anio"]) if m else None
    titulo_cit = m["titulo"] if m else ""
    autor_cit = normaliza(m["autores"].split(",")[0]) if m else ""

    if c["doi"] not in cache:
        r = requests.get(f"https://api.crossref.org/works/{c['doi']}", headers=UA, timeout=30)
        cache[c["doi"]] = (r.status_code, r.json()["message"] if r.status_code == 200 else None)
        time.sleep(0.3)
    estado, meta = cache[c["doi"]]

    fila = {**c, "anio_citado": anio_cit, "crossref_http": estado,
            "titulo_real": "", "anio_real": None, "similitud_titulo": None}
    if meta:
        titulo_real = re.sub(r"<[^>]+>", "", meta["title"][0]).strip()
        anio_real = meta["issued"]["date-parts"][0][0]
        autor_real = normaliza(meta.get("author", [{}])[0].get("family", ""))
        sim = SequenceMatcher(None, normaliza(titulo_cit), normaliza(titulo_real)).ratio()
        problemas = []
        if anio_cit != anio_real:
            problemas.append(f"año citado {anio_cit}, real {anio_real}")
        if sim < 0.85:
            problemas.append(f"título distinto (similitud {sim:.2f})")
        if autor_cit and autor_real and autor_cit != autor_real:
            problemas.append(f"primer autor distinto ({autor_real})")
        fila.update(titulo_real=titulo_real, anio_real=anio_real, similitud_titulo=round(sim, 2),
                    veredicto="⚠️ Existe, pero NO coincide: " + "; ".join(problemas) if problemas
                    else "✅ Existe y coincide")
    elif c["doi"] in corpus:
        real = corpus[c["doi"]]["anio"]
        fila.update(anio_real=real,
                    veredicto=("📄 Artículo del corpus del taller (ficticio): coincide" if anio_cit == real
                               else f"📄⚠️ Artículo del corpus, pero año citado {anio_cit} y real {real}"))
    else:
        fila["veredicto"] = "❌ El DOI no existe en Crossref: posible referencia inventada"
    resultados.append(fila)

df = pd.DataFrame(resultados)
df.to_csv(Path(__file__).parent / "verificacion_referencias.csv", index=False)
pd.set_option("display.width", 200, "display.max_colwidth", 70)
print(df[["citado_en", "doi", "veredicto"]].to_string(index=False))
