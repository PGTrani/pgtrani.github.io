# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Progetto

Sito statico della Pastorale Giovanile (Arcidiocesi di Trani-Barletta-Bisceglie), pubblicato con GitHub Pages su <https://pgtrani.github.io/> direttamente dalla root di `main` (`.nojekyll` disattiva Jekyll: i file sono serviti così come sono). Nessun build, nessuna dipendenza, nessun test: HTML, un CSS condiviso e un po' di JS inline.

Testi, commit e commenti sono in italiano. Il pubblico sono ragazzi che aprono i link da telefono (spesso condivisi su WhatsApp o via QR): layout mobile-first, colonna unica da max 480px.

## Anteprima locale

```sh
python3 -m http.server 8000   # poi http://localhost:8000/
```

Serve un server (non `file://`) perché i link puntano a cartelle (`trani/`, `calendario/`) e si affidano alla risoluzione di `index.html`.

## Struttura e convenzioni

- Ogni pagina è una cartella con il suo `index.html` (URL puliti con slash finale). Gerarchia: home (`index.html`) → `diocesi/` o pagina città (`trani/`) → pagine di evento/servizio (`trani/calendario/`, `diocesi/meeting2026/`, ...). Gli eventi passati restano nella pagina del loro livello sotto un `<h2>` con l'anno pastorale (es. `2025/26`).
- Tutti i percorsi sono **relativi** e dipendono dalla profondità della pagina (`assets/style.css`, `../assets/style.css`, ...; vale anche per loghi, favicon e `assets/icons.svg#…`; link "indietro" `.back` verso `../`). Spostando una pagina vanno ricalcolati.
- Non c'è templating: `<head>` (meta, `theme-color` chiaro/scuro, favicon = logo PNG, Google Fonts *Bricolage Grotesque* + *Figtree*, stylesheet) e la testata sono duplicati in ogni pagina. Una modifica comune va replicata a mano su tutte: conviene partire da una pagina esistente dello stesso livello.
- Identità visiva presa dai loghi (vedi `PRODUCT.md`; palette, componenti e regole in `DESIGN.md`): blu del mare come colore portante, rosso delle scritte del logo per i titoli `h2`, fondo bianco freddo. Colori solo tramite le variabili su `:root` (override in `prefers-color-scheme: dark`).
- Struttura di ogni pagina: `header.sea` (fascia blu: `.back`, logo in disco bianco `.logo` o coppia in `.logos` con lo stemma come `.logo.tile`, `h1`, `p`, eventuale `p.meta`) chiusa da `svg.waves` con tre `<path>` periodici che scorrono in parallasse (fermi con `prefers-reduced-motion`; l'ultima onda ha il colore del fondo); poi `main` e `footer`.
- Componenti: `.actions` > `a.action` per le azioni principali (`.primary` = blu pieno); `nav.list` > `a.row` per gli elenchi raggruppati; ogni riga ha `.tile` (icona) + `.label` (sottotitolo in `<small>`) + icona `.go` (`chevron-right` per link interni, `arrow-up-right` per link esterni con `target="_blank"`). Città non attive: `div.row.soon` con `.badge` "In arrivo". Note: `ul.note` con un'icona per voce. Utility `.hidden`.
- Icone: solo dallo sprite `assets/icons.svg` (tratto 2px, stile Lucide) con `<svg class="i" aria-hidden="true"><use href="…/assets/icons.svg#nome"/></svg>`; niente emoji come icone. Per una nuova icona aggiungere un `<symbol>` 24×24 allo sprite.
- Loghi in `assets/img/` (ridimensionati a 360px): `logo-pg-trani.png` per le pagine di Trani, `logo-pg-diocesi.png` (+ `logo-diocesi.png`) per home e pagine diocesane.
- Per attivare una nuova città: creare `<città>/index.html` sul modello di `trani/index.html` e nella home trasformare il relativo `div.row.soon` in `a.row` con `href` e icona `.go`.

## Pagine con regole proprie

- **`trani/festaoratori2026/`** — unica eccezione allo stile del sito: mantiene la grafica a tema *Alice nel Paese delle Meraviglie*. `index.html` è **generato** (immagini e font incorporati in base64, ~800 KB): non modificarlo a mano, ma cambiare `sito_sorgenti/template.html` (oggetti `STANDS`, `GROUPS`, `HYMNS`) o `sito_sorgenti/assets/` e rilanciare `cd trani/festaoratori2026/sito_sorgenti && python3 genera_sito.py`. Gli mp3 in `inni/` sono caricati in streaming con percorso relativo.
- **`trani/notteprimaesami/`** — pagina autonoma (CSS/JS inline) con palette e font riallineati al sito (stesse variabili copiate nel suo `<style>`, da tenere allineate a mano), tema chiaro/scuro forzabile e dimensione testo salvati in `localStorage`. Il testo liturgico è trascritto parola per parola dal documento originale (`Momento_di_preghiera_maturandi_2026.docx`, nella repo archiviata `PGTrani/notteprimaesami`): non riscriverlo né parafrasarlo.
- **`trani/calendario/`** — pensata per essere condivisa: meta `og:title`/`og:description` per l'anteprima su WhatsApp. Si basa sul calendario Google pubblico indicato nel README, con tre link: iPhone (`webcal://` all'indirizzo iCal `.../public/basic.ics`), Android (`calendar.google.com/calendar/r?cid=...`), "Vedi il calendario" (embed web). Lo script inline rileva il sistema (iPadOS incluso, che si presenta come `MacIntel` con touch), sposta in cima e marca `.primary` il bottone giusto tramite gli id `ios`/`android`, e su iOS mostra la nota `#ios-google`. Se cambia calendario o anno, aggiornare insieme i tre link, titoli/meta della pagina e il bottone in `trani/index.html`.
- **`diocesi/meeting2026/`** — i bottoni puntano a file Google Drive: gli URL vanno copiati esattamente come forniti.

## Redirect dai vecchi indirizzi

`meeting2026/`, `festaoratori2026/` e `notteprimaesami/` in root (più `meeting2026/laboratori.html`) contengono solo pagine di redirect verso i nuovi percorsi: quegli indirizzi sono stati condivisi quando le pagine stavano in repo GitHub separate (ora archiviate, con Pages spento). Non rimuoverli. Se in futuro si sposta una pagina già condivisa, lasciare allo stesso modo un redirect nel vecchio percorso. Attenzione: una repo dell'organizzazione `PGTrani` con Pages attivo e nome uguale a una cartella del sito ha la precedenza su quel percorso.
