---
name: Pastorale Giovanile · PG Trani
description: Il mare dei loghi PG come porta d'ingresso; un tocco sull'azione giusta.
colors:
  sea: "#1356b4"
  wave-1: "#2f86ea"
  wave-2: "#8cc8ff"
  on-sea: "#ffffff"
  on-sea-soft: "#d4e8ff"
  bg: "#f3f7fc"
  card: "#ffffff"
  text: "#0c2340"
  muted: "#4a5f7a"
  line: "#e1e9f3"
  azure: "#1d6ee0"
  azure-strong: "#1259c4"
  tint: "#e5f0fd"
  red: "#c4102b"
  sea-dark: "#0d3a7a"
  wave-1-dark: "#1a5bb0"
  wave-2-dark: "#2c74cf"
  on-sea-soft-dark: "#b9d6f7"
  bg-dark: "#061529"
  card-dark: "#0d2341"
  text-dark: "#eaf2fc"
  muted-dark: "#9fb3cc"
  line-dark: "#1b3558"
  azure-dark: "#2366d4"
  azure-strong-dark: "#1d5cc4"
  tint-dark: "#143561"
  red-dark: "#ff7a8a"
  tile-ink-dark: "#8cc8ff"
typography:
  display:
    fontFamily: "Bricolage Grotesque, Figtree, system-ui, sans-serif"
    fontSize: "clamp(1.9rem, 7vw, 2.4rem)"
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Bricolage Grotesque, Figtree, system-ui, sans-serif"
    fontSize: "1.3rem"
    fontWeight: 800
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 650
    lineHeight: 1.3
  body:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 500
  badge:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.78rem"
    fontWeight: 600
rounded:
  focus: "6px"
  tile: "12px"
  card: "16px"
  emblem: "22px"
  pill: "999px"
  disc: "50%"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  row-gap: "14px"
  gutter: "16px"
  section: "32px"
  page-end: "40px"
components:
  sea-band:
    backgroundColor: "{colors.sea}"
    textColor: "{colors.on-sea}"
    padding: "16px 16px 76px"
  logo-disc:
    backgroundColor: "{colors.on-sea}"
    rounded: "{rounded.disc}"
    size: "104px"
    padding: "4px"
  back-link:
    textColor: "{colors.on-sea-soft}"
    rounded: "{rounded.pill}"
    padding: "8px 12px 8px 4px"
  button-primary:
    backgroundColor: "{colors.azure}"
    textColor: "{colors.on-sea}"
    typography: "{typography.title}"
    rounded: "{rounded.card}"
    padding: "14px 16px"
    height: "64px"
  button-primary-hover:
    backgroundColor: "{colors.azure-strong}"
    textColor: "{colors.on-sea}"
  button-secondary:
    backgroundColor: "{colors.card}"
    textColor: "{colors.text}"
    typography: "{typography.title}"
    rounded: "{rounded.card}"
    padding: "14px 16px"
    height: "64px"
  list-group:
    backgroundColor: "{colors.card}"
    rounded: "{rounded.card}"
  list-row:
    textColor: "{colors.text}"
    typography: "{typography.title}"
    padding: "12px 16px"
    height: "64px"
  list-row-soon:
    textColor: "{colors.muted}"
  icon-tile:
    backgroundColor: "{colors.tint}"
    textColor: "{colors.azure}"
    rounded: "{rounded.tile}"
    size: "40px"
  badge:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
  note:
    backgroundColor: "{colors.tint}"
    textColor: "{colors.text}"
    rounded: "{rounded.card}"
    padding: "4px 16px"
---

# Design System: Pastorale Giovanile · PG Trani

## Overview

**Creative North Star: "Il mare sotto la croce"**

Il sistema nasce dai loghi ufficiali della Pastorale Giovanile: il blu del mare di Trani e delle onde sotto la croce, il rosso delle scritte. Ogni pagina si apre su una fascia di mare a tutta larghezza con il logo in un disco bianco, il titolo e un sottotitolo; il bordo inferiore della fascia sono tre onde sovrapposte che scorrono lente in parallasse e chiudono sul colore del fondo. Sotto le onde il mare finisce e comincia un fondo bianco freddo dove c'è solo ciò che si tocca: l'azione principale per prima, poi gruppi di righe titolati.

La densità è quella di un'app da telefono, non di un sito istituzionale: una colonna sola di 520px al massimo, aree di tocco alte 64px, contenitori morbidi con un'ombra leggera, icone disegnate a tratto dentro tessere azzurre. Il tono è giovane ma non infantile: il carattere display è un grotesk deciso a peso 800, il testo è un sans caldo e leggibile. Niente aria formale "da chiesa", niente decorazioni: l'unico gesto espressivo è il mare.

Il sistema rifiuta in modo esplicito il default del sito precedente: fondo crema, accenti terracotta ed emoji usate come icone. Le uniche immagini sono i loghi ufficiali; non esistono foto degli eventi e non se ne inventano.

Eccezioni sancite: la pagina della Festa degli Oratori 2026 (`trani/festaoratori2026/`) mantiene di proposito la sua grafica a tema *Alice* ed è fuori da questo sistema. La pagina di preghiera "Notte prima degli esami" è una pagina di lettura con CSS proprio: eredita solo palette e caratteri, non la fascia di mare né i componenti, e non va presa come modello.

**Key Characteristics:**
- Fascia d'apertura blu pieno con logo in disco bianco e bordo a tre onde in parallasse.
- Una colonna sola (max 520px), pensata per il telefono e per l'arrivo da link condiviso.
- Azione principale piena azzurra, primo elemento sotto le onde.
- Elenchi raggruppati in un unico contenitore con righe divise da filetti.
- Icone a tratto 2px in tessere azzurre; mai emoji.
- Tema scuro completo via `prefers-color-scheme`, movimento fermo con "riduci movimento".

## Colors

Una palette fredda di blu presi dal logo, con un solo rosso riservato ai titoli di sezione; il tema scuro è una sostituzione completa degli stessi ruoli (chiavi `-dark` nel frontmatter).

### Primary
- **Mare di Trani** (`sea`): il blu pieno della fascia d'apertura. Vive solo lì, a tutta larghezza, ed è anche il `theme-color` della barra del browser. In scuro scende a un blu notte (`sea-dark`).
- **Azzurro Azione** (`azure`): il riempimento del pulsante principale e l'inchiostro delle icone nelle tessere; è anche il colore dell'anello di focus. Al passaggio diventa **Azzurro Profondo** (`azure-strong`).

### Secondary
- **Onda Larga** (`wave-1`) e **Onda Chiara** (`wave-2`): le due onde dietro e in mezzo del bordo della fascia. Non si usano altrove, tranne Onda Chiara come colore di selezione del testo e (in scuro) come inchiostro di icone e focus (`tile-ink-dark`).
- **Spuma** (`on-sea-soft`): sottotitoli e link indietro sopra il mare. Il bianco pieno (`on-sea`) è per il titolo sul mare e per testo e icone dentro il pulsante principale.

### Tertiary
- **Rosso delle Scritte** (`red`): solo per i titoli di sezione (h2), come le scritte del logo. In scuro diventa un rosa corallo (`red-dark`) per restare leggibile sul blu notte.

### Neutral
- **Fondo Freddo** (`bg`): il fondo di pagina e il colore della terza onda, che così "chiude" la fascia nel contenuto. Anche il fondo dei badge.
- **Carta** (`card`): pulsanti e contenitori degli elenchi.
- **Inchiostro Notte** (`text`): testo principale.
- **Grigio Fondale** (`muted`): sottorighe, chevron, piè di pagina, città "in arrivo".
- **Filetto** (`line`): divisori tra le righe di un elenco e contorno delle tessere disattivate.
- **Velo Azzurro** (`tint`): fondo delle tessere icona, delle note informative e dello stato premuto delle righe.

### Named Rules
**The Sea Opens Rule.** Il blu pieno del mare sta solo nella fascia d'apertura. Il contenuto vive su fondo freddo e carta bianca; il blu torna sotto le onde soltanto come riempimento dell'azione principale e inchiostro delle icone.

**The Red Is Ink Rule.** Il rosso è inchiostro per i titoli di sezione e nient'altro: mai pulsanti, fondi, bordi o icone rossi.

**The Full Override Rule.** Ogni colore passa da un token e ogni token ha il suo valore scuro. In tema scuro si sostituiscono tutti i ruoli, comprese onde e ombra; non si aggiungono colori letterali fuori dai token.

## Typography

**Display Font:** Bricolage Grotesque (con Figtree, system-ui, sans-serif)
**Body Font:** Figtree (con system-ui, -apple-system, Segoe UI, sans-serif)

**Character:** Un grotesk espressivo a peso 800, stretto e con spaziatura negativa, per i pochi titoli; un sans geometrico e caldo per tutto ciò che si legge e si tocca. Insieme suonano giovani e diretti, senza essere né istituzionali né giocosi. Entrambi da Google Fonts (Bricolage 700–800 con asse opsz, Figtree 400–700).

### Hierarchy
- **Display** (800, clamp(1.9rem, 7vw, 2.4rem), 1.08, −0.025em, `text-wrap: balance`): il titolo bianco nella fascia di mare. Uno per pagina.
- **Headline** (800, 1.3rem, −0.02em, rosso): titoli di sezione sopra un gruppo di righe, spesso l'anno pastorale ("2025/26") o "Seguici".
- **Title** (Figtree 650, 1.0625rem nelle righe e 1.08rem nei pulsanti, 1.3): l'etichetta di ogni riga e pulsante toccabile.
- **Body** (400, 1.0625rem, 1.5): testo corrente e note; la colonna da 520px tiene la riga corta.
- **Label** (500, 0.9rem, grigio): la sottoriga sotto l'etichetta, con data, luogo o istruzione breve. Sul mare il sottotitolo usa Figtree 500 in Spuma.
- **Badge** (600, 0.78rem): lo stato "In arrivo" in una pillola.

### Named Rules
**The Two Voices Rule.** Bricolage Grotesque parla solo nei titoli (h1 sul mare, h2 di sezione). Tutto ciò che si tocca o si legge è Figtree.

**The Tappable Weight Rule.** Le etichette toccabili sono a peso 650, sempre più pesanti delle sottorighe a 500: l'occhio trova il bersaglio prima della spiegazione.

## Layout

Una sola colonna centrata, larga al massimo 520px, con margini laterali di 16px; il corpo pagina è una colonna flex che spinge il piè di pagina in fondo. La fascia di mare è a tutta larghezza e il suo contenuto interno rispetta la stessa colonna da 520px.

Ritmo verticale: 12px tra pulsanti d'azione impilati, 32px sopra ogni titolo di sezione e 10px sotto, 20px sopra una nota, 40px in fondo al contenuto. Dentro righe e pulsanti lo spazio tra tessera ed etichetta è 14px. La fascia ha 16px sopra e 76px sotto per far posto alle onde (64px).

Sopra i 720px cambia poco, di proposito: la fascia cresce (28px sopra, 104px sotto, onde alte 88px, logo 120px) e il contenuto scende di 8px. La colonna resta stretta anche su desktop.

Ordine fisso di ogni pagina: link indietro (tranne la home), logo, titolo, sottotitolo, eventuali righe "meta"; poi sotto le onde l'azione principale o il primo gruppo di righe, poi i gruppi titolati; piè di pagina con il nome della Pastorale.

## Elevation & Depth

Sistema quasi piatto con un'unica ombra morbida: pulsanti e contenitori degli elenchi si staccano dal fondo freddo con un'ombra ambientale a due strati, in chiaro una velatura blu-notte, in scuro un'ombra nera più profonda. Il disco del logo ha un'ombra sua, più corta, per staccarsi dal mare. La profondità vera del sistema è quella delle onde: tre piani di colore sovrapposti che scorrono a velocità diverse.

### Shadow Vocabulary
- **Ombra Carta** (`--shadow`): pulsanti e contenitori degli elenchi. Valori chiaro/scuro nel sidecar.
- **Ombra Disco**: solo il logo (e lo stemma) sopra il mare.

### Named Rules
**The Soft Lift Rule.** Una sola ombra per tutti i contenitori; nessun bordo attorno alle carte. I filetti esistono solo dentro un elenco, tra una riga e l'altra.

## Shapes

Angoli morbidi e costanti: 16px per pulsanti, elenchi e note; 12px per le tessere delle icone; pillola piena per il link indietro e i badge; disco per il logo. Lo stemma dell'Arcidiocesi, che non è tondo, sta in una tessera bianca da 22px. Il focus disegna un anello di 3px con 3px di distacco e angoli da 6px; dentro un elenco l'anello rientra e segue i 16px del contenitore.

L'unica sagoma non squadrata del sistema è l'onda: curve geometriche regolari ripetute su una larghezza doppia del riquadro, così lo scorrimento è continuo. I filetti tra le righe partono a 70px dal bordo sinistro, allineati dopo la tessera, così le icone formano una colonna pulita.

## Components

### Fascia di mare (componente firma)
Il mare come porta d'ingresso: ogni pagina comincia qui e da qui si capisce subito di chi è.
- **Struttura:** fondo Mare, testo centrato; link indietro in alto a sinistra, logo in disco bianco 104px (120px su desktop), titolo Display bianco, sottotitolo in Spuma, righe "meta" opzionali a 0.95rem. Più loghi affiancati con 14px di spazio.
- **Bordo a onde:** un SVG a tutta larghezza alto 64px (88px su desktop), ancorato in fondo, con tre tracciati: Onda Larga (scorre in 21s), Onda Chiara (15s, in senso inverso), e una terza nel colore del fondo (27s) che chiude la fascia. L'animazione `drift` sposta ogni onda di 720px in modo lineare e infinito; con "riduci movimento" si ferma del tutto. È decorativo: `aria-hidden`.

### Pulsanti d'azione
Grandi, separati, pensati per il pollice.
- **Shape:** angoli morbidi (16px), altezza minima 64px, imbottitura 14px 16px; tessera icona a sinistra, etichetta con sottoriga, chevron a destra.
- **Primary:** fondo Azzurro Azione, testo e chevron bianchi, tessera in bianco al 18% con icona bianca.
- **Secondary:** fondo Carta, testo Inchiostro, Ombra Carta.
- **Hover / Active:** il primario passa ad Azzurro Profondo; il secondario prende una velatura di Velo Azzurro (45%). Alla pressione il pulsante si stringe appena (scala 0.985, 120ms). Transizioni di colore 150ms ease.
- **Promozione dinamica:** nella pagina calendario lo script riconosce iPhone o Android, rende primario il pulsante giusto e lo porta in cima; senza riconoscimento restano tutti secondari.

### Elenchi raggruppati
Un solo contenitore per gruppo, righe divise da filetti.
- **Contenitore:** fondo Carta, angoli 16px, Ombra Carta, contenuto ritagliato.
- **Riga:** altezza minima 64px, imbottitura 12px 16px, tessera 40px + etichetta (peso 650) con sottoriga opzionale + indicatore a destra. Chevron a destra per le pagine interne, freccia in diagonale per i link esterni (Drive, Instagram, WhatsApp).
- **Stati:** al passaggio velatura di Velo Azzurro al 45%, premuto Velo Azzurro pieno.
- **Riga "in arrivo":** testo grigio, tessera trasparente con contorno sottile nel colore del filetto, nessuno stato al passaggio, badge "In arrivo" al posto dell'indicatore.

### Tessere icona
- **Style:** quadrato da 40px, angoli 12px, fondo Velo Azzurro, icona Azzurro Azione (Onda Chiara in scuro).
- **Icone:** sprite condiviso di simboli a tratto 24×24, tratto 2px con terminali tondi, disegnati a 22px (20px per chevron e note). Si richiamano per riferimento dallo sprite, non si incollano.

### Badge
- **Style:** pillola, fondo Fondo Freddo dentro la carta, testo grigio, 0.78rem a peso 600, imbottitura 3px 10px. Oggi segna solo "In arrivo".

### Note informative
- **Style:** blocco Velo Azzurro con angoli 16px, elenco di voci con icona a tratto 20px a sinistra e testo a 0.97rem; voci divise da un filetto azzurro al 15%. Il grassetto evidenzia la parola chiave dell'istruzione.

### Navigazione
- **Link indietro:** in cima alla fascia, chevron sinistro + nome del livello superiore ("Tutte le città", "PG Trani", "Diocesi"), in Spuma a 0.95rem peso 600, pillola che al passaggio prende un velo bianco al 12% e il testo diventa bianco pieno; focus bianco.
- **Gerarchia:** home → Diocesi o città → evento. Gli eventi passati stanno nella pagina del loro livello, sotto il titolo dell'anno pastorale.

## Do's and Don'ts

### Do:
- **Do** apri ogni pagina del sistema con la fascia di mare: logo in disco bianco, titolo Display, sottotitolo in Spuma e bordo a tre onde con l'ultima nel colore del fondo.
- **Do** metti l'azione principale come primo elemento sotto le onde, piena Azzurro Azione, alta almeno 64px; al massimo una piena per schermata.
- **Do** raggruppa i link correlati in un unico contenitore con righe divise da filetti che partono dopo la tessera (70px).
- **Do** usa icone a tratto 2px dallo sprite condiviso, dentro tessere azzurre da 40px; chevron per le pagine interne, freccia in diagonale per i link esterni.
- **Do** passa ogni colore da un token e dagli il valore scuro corrispondente.
- **Do** ferma lo scorrimento delle onde con "riduci movimento"; nessun altro elemento si anima in modo continuo.
- **Do** tieni la colonna a 520px anche su schermi larghi.

### Don't:
- **Don't** usare emoji come icone.
- **Don't** tornare al default del sito precedente: fondo crema, accenti terracotta, emoji.
- **Don't** usare il rosso per pulsanti, fondi, bordi o icone: è solo per i titoli di sezione.
- **Don't** spezzare un elenco in tante carte separate, né mettere bordi attorno alle carte.
- **Don't** usare foto d'evento inventate o di repertorio: le uniche immagini sono i loghi ufficiali.
- **Don't** applicare questo sistema alla Festa degli Oratori 2026, che ha una grafica propria, né prendere la pagina "Notte prima degli esami" come modello di componenti.
