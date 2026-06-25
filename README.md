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

## Form di contatto

Il form in homepage invia i messaggi via [Formspree](https://formspree.io) (nessun backend da scrivere).

1. Crea un account gratuito su Formspree con l'email `biluxtech@gmail.com`.
2. Crea un nuovo form: otterrai un endpoint tipo `https://formspree.io/f/XXXXXXXX`.
3. Apri `src/components/ContactForm.jsx` e sostituisci `FORMSPREE_ENDPOINT` con il tuo endpoint reale.
4. Ogni invio dal form arriverà come email a `biluxtech@gmail.com`.

In alternativa, se deploi su Netlify puoi usare [Netlify Forms](https://docs.netlify.com/forms/setup/) aggiungendo l'attributo `data-netlify="true"` al tag `<form>` invece di Formspree.

## Deploy

Il progetto è pronto per essere deployato su **Vercel** o **Netlify**:

- **Vercel**: importa la repo, Vercel rileva automaticamente Vite. È incluso `vercel.json` con i rewrite per il client-side routing.
- **Netlify**: importa la repo, build command `npm run build`, publish directory `dist` (già configurato in `netlify.toml`, incluso il redirect per le route di react-router-dom).

Comando di build usato in entrambi i casi:

```bash
npm run build
```

L'output finale si trova in `dist/`.

