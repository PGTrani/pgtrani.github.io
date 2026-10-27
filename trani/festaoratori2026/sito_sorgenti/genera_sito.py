#!/usr/bin/env python3
"""
Rigenera "index.html" (sito unico autonomo, pronto per GitHub Pages).

Come si usa:
    cd "sito_sorgenti"
    python3 genera_sito.py

Modifiche tipiche (tutte dentro template.html):
  - testi, orari, giochi, gruppi  -> oggetti STANDS / GROUPS nello <script>
  - posizione dei pin sulla mappa -> campi x,y (percentuali) in STANDS e INIZIO
  - colori / grafica             -> blocco <style>
Per cambiare un'immagine: sostituisci il file in assets/ (stesso nome) e rilancia.
"""
import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUT = os.path.join(os.path.dirname(HERE), "index.html")

def datauri(filename, mime):
    with open(os.path.join(ASSETS, filename), "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

tokens = {
    "__FONT__":  datauri("Qwerty.otf", "font/otf"),
    "__MAP__":   datauri("map.webp", "image/webp"),
    "__COVER__": datauri("cover.webp", "image/webp"),
}
for k in ["s1", "s2", "s3", "s4", "s5", "s6", "s6b", "s7", "s8"]:
    tokens["__" + k.upper() + "__"] = datauri(k + ".webp", "image/webp")

with open(os.path.join(HERE, "template.html"), encoding="utf-8") as f:
    html = f.read()
for tok, val in tokens.items():
    html = html.replace(tok, val)

import re
leftover = set(re.findall(r"__[A-Z0-9]+__", html))
assert not leftover, f"Token non sostituiti: {leftover}"

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("Generato:", OUT)
print("Dimensione:", round(os.path.getsize(OUT) / 1024), "KB")
