# Bilux Tech

Sito vetrina realizzato con Vite + React + Tailwind CSS.

## Avvio

```bash
npm install
npm run dev
```

Apri http://localhost:5173

## Build di produzione

```bash
npm run build
npm run preview
```

## Struttura

```
src/
  components/   Nav, Footer, ServiceCard
  data/         services.js — contenuti dei 4 servizi
  pages/        Home.jsx, ServicePage.jsx (route dinamica /servizi/:slug)
  App.jsx       definizione delle route (react-router-dom)
  main.jsx      entry point + BrowserRouter
  index.css     direttive Tailwind + animazione ticker
```

Per modificare i contenuti dei servizi, basta editare `src/data/services.js`.

## Form di contatto (Supabase)

Il form in homepage salva i messaggi in una tabella Supabase (niente backend da scrivere).

1. Crea un progetto gratuito su [supabase.com](https://supabase.com).
2. Apri **SQL Editor** nella dashboard e incolla il contenuto di `supabase/schema.sql`: crea la tabella `messages` con Row Level Security (il sito può solo inserire righe, non leggerle — i messaggi sono visibili solo a te nella dashboard).
3. Vai in **Project Settings → API** e copia:
   - **Project URL**
   - **anon public key**
4. Copia `.env.example` in `.env` nella root del progetto e inserisci i due valori:
   ```
   VITE_SUPABASE_URL=https://xxxxxxxxxxxx.supabase.co
   VITE_SUPABASE_ANON_KEY=la-tua-anon-key
   ```
5. Riavvia `npm run dev`. I messaggi inviati dal form li trovi in **Table Editor → messages**.

**Per ricevere anche una notifica email** (oltre a vedere i messaggi nella dashboard): in Supabase puoi creare un *Database Webhook* su `messages` (evento INSERT) collegato a un servizio come Resend, oppure una Edge Function che invia l'email a `biluxtech@gmail.com`. Questo passo è opzionale e non incluso di default.

⚠️ Il file `.env` non va mai committato su GitHub (è già escluso in `.gitignore`). Se deploi su Vercel o Netlify, imposta le stesse due variabili nelle impostazioni del progetto (Vercel: Settings → Environment Variables; Netlify: Site settings → Environment variables). Se usi il workflow GitHub Actions incluso per GitHub Pages, aggiungi le due variabili come **Repository secrets** (Settings → Secrets and variables → Actions) e passale come `env` nello step di build in `.github/workflows/deploy.yml`.

## Deploy

Il progetto è pronto per essere deployato su **Vercel** o **Netlify**:

- **Vercel**: importa la repo, Vercel rileva automaticamente Vite. È incluso `vercel.json` con i rewrite per il client-side routing.
- **Netlify**: importa la repo, build command `npm run build`, publish directory `dist` (già configurato in `netlify.toml`, incluso il redirect per le route di react-router-dom).

Comando di build usato in entrambi i casi:

```bash
npm run build
```

L'output finale si trova in `dist/`.

## Deploy su GitHub (GitHub Pages)

1. Crea un repository su GitHub e pusha questo progetto:
   ```bash
   git init
   git add .
   git commit -m "Bilux Tech"
   git branch -M main
   git remote add origin https://github.com/TUO-UTENTE/TUO-REPO.git
   git push -u origin main
   ```
2. Su GitHub vai in **Settings → Pages** e in "Build and deployment" seleziona **GitHub Actions** come source.
3. Il workflow incluso in `.github/workflows/deploy.yml` builda e pubblica automaticamente il sito a ogni push su `main`.
4. Il sito sarà disponibile su `https://TUO-UTENTE.github.io/TUO-REPO/` (il workflow imposta automaticamente il percorso corretto in base al nome del repo).

Se invece vuoi solo versionare il codice su GitHub e fare il deploy da Vercel/Netlify (collegando direttamente la repo), non serve nessuna configurazione aggiuntiva: bastano i passi 1 sopra, poi importi la repo su Vercel o Netlify.

