# Bilux Tech: sito

Sito statico (HTML, CSS, JS) senza dipendenze. Il sito pubblicato è nella cartella `public/`.

## Avviarlo in locale

    cd public
    python3 -m http.server 8080

Poi apri http://localhost:8080 . In locale il form non può inviare: funziona solo su Netlify.

## Modificare i contenuti
Testi, servizi, progetti, FAQ, SEO e informativa privacy stanno in `build.py`. Dopo una modifica rigenera le pagine:

    python3 build.py

Stile in `public/css/style.css`, interazioni in `public/js/main.js`.

## Form di contatto (Netlify Forms)
Il form si chiama `contatto`. Netlify lo riconosce a ogni pubblicazione.
1. Su Netlify: Site configuration → Forms → **Enable form detection** (solo la prima volta).
2. Forms → Form notifications → **Add notification → Email notification** → biluxtech@gmail.com.
3. Pubblica di nuovo il sito, così Netlify rileva il form.

## Prima della pubblicazione
- Dopo aver cambiato immagini, CSS o JS aumenta `V` in `build.py` e rigenera, così i browser scaricano la versione nuova.
- Su Netlify: publish directory `public`, nessun comando di build (già impostato in `netlify.toml`).
