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

- Ogni pagina è una cartella con il suo `index.html` (URL puliti con slash finale). Gerarchia: home (`index.html`) → `diocesi/` o pagina città (`trani/`) → pagine di evento/servizio (`trani/calendario/`, `diocesi/meeting2026/`, ...). Gli eventi passati restano nella pagina del loro livello sotto un titolo di sezione con l'anno pastorale (`<h2 class="section-title">2025/26</h2>`).
- Tutti i percorsi sono **relativi** e dipendono dalla profondità della pagina (`assets/style.css`, `../assets/style.css`, `../../assets/style.css`; link "indietro" `.back` verso `../`). Spostando una pagina vanno ricalcolati.
- Non c'è templating: `<head>` (viewport, favicon emoji come data URI SVG, stylesheet) è duplicato in ogni pagina. Una modifica comune va replicata a mano su tutte.
- `assets/style.css` definisce i colori come variabili su `:root` con override in `prefers-color-scheme: dark`; usare le variabili, non colori fissi.
- Componenti riusati: `nav.buttons` con `a.btn` composto da `.icon` + `.label` (sottotitolo in `<small>`) + `.arrow`; varianti `.primary` (evidenziato) e `.disabled` (con `aria-disabled="true"`, senza `href` né freccia, per le città "In arrivo"); `.section-title` tra due `nav.buttons`; riquadri `.note`; utility `.hidden`. Nell'header: `.logo`/`.logos` (immagini), `.kicker` (sopratitolo), `.meta` (date/luogo).
- Loghi in `assets/img/` (ridimensionati a 360px): `logo-pg-trani.png` per le pagine di Trani, `logo-pg-diocesi.png` + `logo-diocesi.png` per home e pagine diocesane. Quelli con sfondo trasparente vanno messi con classe `round`/`tile` (fondo bianco) per restare leggibili in dark mode.
- Per attivare una nuova città: creare `<città>/index.html` sul modello di `trani/index.html` e nella home trasformare il relativo bottone `.disabled` in un link normale con `href` e `.arrow`.

## Pagine con regole proprie

- **`trani/festaoratori2026/`** — unica eccezione allo stile del sito: mantiene la grafica a tema *Alice nel Paese delle Meraviglie*. `index.html` è **generato** (immagini e font incorporati in base64, ~800 KB): non modificarlo a mano, ma cambiare `sito_sorgenti/template.html` (oggetti `STANDS`, `GROUPS`, `HYMNS`) o `sito_sorgenti/assets/` e rilanciare `cd trani/festaoratori2026/sito_sorgenti && python3 genera_sito.py`. Gli mp3 in `inni/` sono caricati in streaming con percorso relativo.
- **`trani/notteprimaesami/`** — pagina autonoma (CSS/JS inline) con palette riallineata a quella del sito, tema chiaro/scuro forzabile e dimensione testo salvati in `localStorage`. Il testo liturgico è trascritto parola per parola dal documento originale (`Momento_di_preghiera_maturandi_2026.docx`, nella repo archiviata `PGTrani/notteprimaesami`): non riscriverlo né parafrasarlo.
- **`trani/calendario/`** — pensata per essere condivisa: meta `og:title`/`og:description` per l'anteprima su WhatsApp. Si basa sul calendario Google pubblico indicato nel README, con tre link: iPhone (`webcal://` all'indirizzo iCal `.../public/basic.ics`), Android (`calendar.google.com/calendar/r?cid=...`), "Vedi il calendario" (embed web). Lo script inline rileva il sistema (iPadOS incluso, che si presenta come `MacIntel` con touch), sposta in cima e marca `.primary` il bottone giusto tramite gli id `ios`/`android`, e su iOS mostra la nota `#ios-google`. Se cambia calendario o anno, aggiornare insieme i tre link, titoli/meta della pagina e il bottone in `trani/index.html`.
- **`diocesi/meeting2026/`** — i bottoni puntano a file Google Drive: gli URL vanno copiati esattamente come forniti.

## Redirect dai vecchi indirizzi

`meeting2026/`, `festaoratori2026/` e `notteprimaesami/` in root (più `meeting2026/laboratori.html`) contengono solo pagine di redirect verso i nuovi percorsi: quegli indirizzi sono stati condivisi quando le pagine stavano in repo GitHub separate (ora archiviate, con Pages spento). Non rimuoverli. Se in futuro si sposta una pagina già condivisa, lasciare allo stesso modo un redirect nel vecchio percorso. Attenzione: una repo dell'organizzazione `PGTrani` con Pages attivo e nome uguale a una cartella del sito ha la precedenza su quel percorso.
