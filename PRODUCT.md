# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Ragazzi e giovanissimi delle parrocchie e i loro animatori. Aprono il sito dal telefono seguendo un link condiviso su WhatsApp, un QR o Instagram, spesso in movimento o durante un evento, e vogliono arrivare subito alla cosa che serve.

## Product Purpose

Punto unico della Pastorale Giovanile per arrivare in uno o due tocchi alle cose utili: calendario da aggiungere al telefono, materiali degli eventi, preghiere. È organizzato per livello: Diocesi e singole città (oggi attiva solo Trani; Barletta, Bisceglie, Corato e Forania sono "in arrivo"). Successo: chi apre il link trova e usa l'azione giusta senza cercarla.

## Operating Context

- I link vengono condivisi singolarmente (pagina calendario, pagina di un evento): ogni pagina deve funzionare anche come punto d'ingresso, con anteprima su WhatsApp.
- Gli eventi passati restano consultabili nella pagina del loro livello, raggruppati per anno pastorale (es. 2025/26).
- Gli indirizzi già condivisi non devono rompersi: quando una pagina si sposta resta un redirect.

## Capabilities and Constraints

- Sito statico su GitHub Pages, nessun build né dipendenze; HTML a mano con un CSS condiviso.
- Il calendario si aggiunge via `webcal://` su iPhone e via link Google Calendar su Android; la pagina rileva il sistema e mette in evidenza il pulsante giusto.
- La pagina della Festa degli Oratori 2026 ha una grafica propria (tema *Alice*) ed è generata da sorgenti: resta fuori dallo stile comune.
- Il testo delle preghiere (Notte prima degli esami) è trascritto parola per parola dal documento originale e non si modifica.

## Brand Commitments

- Loghi ufficiali: PG Trani ("Giovani di Trani"), PG diocesana, stemma dell'Arcidiocesi (in `assets/img/`).
- Tono: fatto per i giovani. Non formale/istituzionale "da chiesa", ma nemmeno infantile.
- Lingua italiana.

## Evidence on Hand

Loghi in `assets/img/`; link reali a Google Calendar, Google Drive (materiali del Meeting), Instagram `@pg_trani` e canale WhatsApp. Non esistono foto degli eventi nel repo: non vanno inventate.

## Product Principles

- L'azione principale di ogni pagina è evidentissima e raggiungibile con un tocco.
- Ogni pagina regge da sola, perché ci si arriva da un link condiviso.
- Leggero e immediato su rete mobile.
- I link condivisi non si rompono mai.

## Accessibility & Inclusion

Uso prevalente da telefono, anche all'aperto e di sera: contrasto alto, aree di tocco grandi, rispetto di tema chiaro/scuro e di "riduci movimento".
