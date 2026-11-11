#!/usr/bin/env python3
"""Genera il sito statico Bilux Tech. Uso: python3 build.py [cartella-output, default: public]
Contenuti, SEO e layout condivisi vivono qui; l'output è HTML puro, senza build richiesta per servirlo."""
import json, os, sys, html

OUT = sys.argv[1] if len(sys.argv) > 1 else "public"
SITE = "https://biluxtech.com"
EMAIL = "biluxtech@gmail.com"
BRAND = "Bilux Tech"
V = "7"  # versione degli asset: aumentala dopo aver cambiato immagini, CSS o JS
# Incolla qui l'endpoint del servizio di invio (Web3Forms, Formspree, Netlify…). Vuoto = fallback via email.
FORM_ENDPOINT = "/"  # Netlify Forms: il form viene inviato al sito stesso
# Dati del titolare per l'informativa privacy (da completare prima della pubblicazione)
TITOLARE = "Bilux Tech"
PRIVACY_DATA = "11 novembre 2026"

e = html.escape

# ---------------------------------------------------------------- content
SERVICES = [
    dict(slug="siti-web", beam="web", name="Siti web e landing page", short="Siti web",
         row="Siti aziendali e landing page per campagne, progettati per farsi capire in pochi secondi e funzionare bene su ogni schermo.",
         glyph=[(0,0),(1,0),(2,0),(3,0),(0,1),(0,2),(0,3),(2,2)],
         title="Siti web e landing page in Lombardia e Ticino | Bilux Tech",
         desc="Progettiamo siti aziendali e landing page chiari, veloci e responsive, pensati per trasformare le visite in richieste di contatto.",
         lede="Siti che spiegano chiaramente chi sei e cosa offri, e landing page costruite per un solo obiettivo: farti contattare.",
         ex_title="Un sito è uno strumento di lavoro.",
         ex=["Il sito è spesso il primo contatto tra la tua azienda e un potenziale cliente. Se è lento, confuso o scomodo da telefono, quella persona se ne va prima di capire cosa fai.",
             "Progettiamo siti aziendali e landing page partendo da cosa deve fare chi arriva: chiedere un preventivo, prenotare, scoprire un prodotto. Struttura, testi e design seguono quell'obiettivo."],
         benefits=[("Si capisce subito cosa offri", "Gerarchia chiara, testi diretti e un invito all'azione evidente in ogni pagina."),
                   ("Funziona su ogni schermo", "Progettiamo partendo dallo smartphone, dove arriva gran parte delle visite."),
                   ("Parte con basi SEO corrette", "Titoli, descrizioni, struttura e velocità impostati per farsi trovare dai motori di ricerca."),
                   ("Sai da dove arrivano i contatti", "Analytics e tracciamento collegati, per misurare cosa funziona davvero.")],
         caps=[("Siti aziendali", "Presentazione di azienda, servizi e contatti, anche in più lingue."),
               ("Landing page", "Pagine dedicate a una campagna o a un'offerta, con un solo invito all'azione."),
               ("UX/UI design", "Struttura dei contenuti, percorsi e interfaccia definiti prima dello sviluppo."),
               ("Sviluppo responsive", "Pagine leggere e curate su smartphone, tablet e desktop."),
               ("SEO di base", "Titoli, meta description, struttura dei contenuti e sitemap."),
               ("Analytics e tracciamento", "Misurazione di visite, contatti e conversioni dalle campagne."),
               ("Form e integrazioni", "Moduli di contatto e collegamenti con gli strumenti che usi già."),
               ("Supporto ai testi", "Aiuto nel mettere in ordine i contenuti e scrivere testi chiari.")],
         projects=["immobilgreen", "ulakasha"],
         faq=[("Quanto tempo serve per realizzare un sito?", "Dipende da numero di pagine, lingue e contenuti già disponibili. Una landing page richiede in genere meno tempo di un sito completo. Dopo la prima chiamata ti diamo una stima precisa."),
              ("Qual è la differenza tra un sito e una landing page?", "Un sito presenta tutta l'attività su più pagine. Una landing page è una pagina singola con un solo obiettivo, di solito collegata a una campagna pubblicitaria."),
              ("Devo fornire io testi e immagini?", "Se li hai, partiamo da quelli. Se mancano, ti aiutiamo a strutturare i testi e a capire quali immagini servono."),
              ("Il sito sarà visibile su Google?", "Impostiamo correttamente le basi SEO: struttura, titoli, descrizioni, velocità e sitemap. Il posizionamento dipende anche da contenuti e concorrenza nel tempo, quindi non promettiamo posizioni precise.")]),
    dict(slug="marketing", beam="mkt", name="Marketing e advertising", short="Marketing",
         row="Strategia, posizionamento e campagne su Meta e Google, dal setup al monitoraggio dei risultati.",
         glyph=[(3,0),(2,1),(3,1),(1,2),(2,2),(3,2),(0,3),(1,3),(2,3),(3,3)],
         title="Marketing digitale e campagne Meta e Google Ads | Bilux Tech",
         desc="Strategia, posizionamento e gestione di campagne su Meta e Google per aziende e professionisti in Lombardia e Ticino.",
         lede="Una strategia chiara su dove investire, e campagne su Meta e Google gestite dal setup al report.",
         ex_title="Le persone giuste, nel posto giusto.",
         ex=["Un buon sito senza traffico resta vuoto. Una campagna che porta su una pagina debole spreca budget. Per questo seguiamo entrambe le parti.",
             "Partiamo da un'analisi di quello che fai oggi, definiamo posizionamento e canali, poi pianifichiamo e gestiamo le campagne guardando i dati."],
         benefits=[("Sai dove stai investendo", "Obiettivi, canali e budget definiti prima di partire, non strada facendo."),
                   ("Campagne e sito lavorano insieme", "Annunci e pagine di destinazione progettati per la stessa persona e lo stesso obiettivo."),
                   ("Decisioni basate sui dati", "Tracciamento impostato correttamente, per capire quali azioni portano contatti."),
                   ("Report che si capiscono", "Numeri essenziali spiegati in modo chiaro, con le prossime azioni da fare.")],
         caps=[("Audit", "Analisi della presenza digitale e delle campagne attive."),
               ("Strategia e posizionamento", "Chi vuoi raggiungere, con quale messaggio, su quali canali."),
               ("Funnel", "Il percorso dalla prima visita alla richiesta di contatto."),
               ("Meta Ads", "Campagne su Facebook e Instagram, dal setup all'ottimizzazione."),
               ("Google Ads", "Campagne sulla rete di ricerca per intercettare chi ti sta cercando."),
               ("Retargeting", "Annunci per chi ha già visitato il sito senza contattarti."),
               ("Tracciamento", "Pixel, eventi e conversioni impostati correttamente."),
               ("Reportistica", "Monitoraggio dei risultati e indicazioni per migliorare.")],
         projects=[],
         faq=[("Quanto budget serve per le campagne?", "Dipende da settore, zona e obiettivi. Prima di partire ti proponiamo un budget di test coerente con quello che vuoi ottenere."),
              ("In quanto tempo si vedono i risultati?", "Le prime indicazioni arrivano dopo alcune settimane di dati raccolti. Le campagne migliorano con l'ottimizzazione nel tempo, per questo le seguiamo con continuità."),
              ("Posso affidarvi solo le campagne, senza rifare il sito?", "Sì. Se la pagina di destinazione frena i risultati te lo segnaliamo e valutiamo insieme se e come intervenire."),
              ("Su quali piattaforme lavorate?", "Gestiamo campagne su Meta (Facebook e Instagram) e Google Ads.")]),
    dict(slug="consulenza", beam="con", name="Consulenza", short="Consulenza",
         row="Un affiancamento continuo per decidere priorità, canali e investimenti digitali con più chiarezza.",
         glyph=[(0,0),(1,0),(0,1),(3,3),(2,3),(3,2)],
         title="Consulenza marketing e digitale in Lombardia e Ticino | Bilux Tech",
         desc="Percorsi di consulenza per definire priorità, canali e investimenti digitali, con un affiancamento continuo nel tempo.",
         lede="Un affiancamento continuo per chi vuole decidere con più chiarezza priorità, canali e investimenti digitali.",
         ex_title="Un punto di vista esterno, quando serve.",
         ex=["Non sempre serve un nuovo sito o una nuova campagna. A volte serve capire cosa sta funzionando, cosa no e da dove ripartire.",
             "Nei percorsi di consulenza lavoriamo al tuo fianco: analizziamo la situazione, mettiamo in fila le priorità e ti accompagniamo nelle decisioni, che tu abbia un team interno o lavori da solo."],
         benefits=[("Priorità chiare", "Un elenco ordinato di cosa fare prima, cosa dopo e cosa lasciare stare."),
                   ("Meno investimenti a vuoto", "Ogni attività ha un obiettivo e un modo per verificare se funziona."),
                   ("Un interlocutore stabile", "La stessa persona segue il percorso e conosce la tua storia."),
                   ("Competenze che restano", "Le decisioni vengono spiegate, così il tuo team cresce insieme al progetto.")],
         caps=[("Analisi iniziale", "Sito, canali, campagne e comunicazione: com'è la situazione oggi."),
               ("Obiettivi", "Cosa vuoi ottenere e come misurarlo."),
               ("Piano delle attività", "Le azioni da fare, in ordine di priorità."),
               ("Scelta degli strumenti", "Quali piattaforme e servizi servono davvero."),
               ("Revisione periodica", "Momenti fissi per guardare i risultati e correggere la rotta."),
               ("Supporto al team", "Affiancamento a chi gestisce il digitale internamente.")],
         projects=[],
         faq=[("Come si svolge un percorso di consulenza?", "Si parte da un'analisi iniziale, poi si concordano incontri periodici con obiettivi e attività definiti. Ritmo e durata dipendono dalle tue esigenze."),
              ("È adatta anche a una piccola attività?", "Sì. Anzi, quando il tempo e il budget sono limitati, sapere dove concentrarsi fa ancora più differenza."),
              ("La consulenza include anche la realizzazione?", "La consulenza riguarda analisi e decisioni. Se emerge un intervento da fare, come un sito, una campagna o uno strumento, possiamo occuparcene noi.")]),
    dict(slug="software", beam="sw", name="Applicazioni su misura", short="Applicazioni",
         row="Applicazioni e software costruiti attorno a come lavori, quando i programmi standard non bastano.",
         glyph=[(0,0),(1,0),(0,1),(1,1),(3,1),(2,3),(3,3),(0,3)],
         title="Applicazioni e software su misura in Lombardia e Ticino | Bilux Tech",
         desc="Applicazioni web e strumenti su misura per semplificare processi, ridurre il lavoro manuale e tenere i dati in un unico posto.",
         lede="Applicazioni e software su misura, costruiti attorno a come lavori davvero.",
         ex_title="Quando i programmi standard non bastano.",
         ex=["Fogli di calcolo che si moltiplicano, dati copiati a mano da un sistema all'altro, programmi che fanno troppo o troppo poco: sono segnali che un processo potrebbe funzionare meglio.",
             "Progettiamo e sviluppiamo applicazioni su misura. Partiamo da come lavori oggi, individuiamo i passaggi da semplificare e costruiamo solo ciò che serve."],
         benefits=[("Lo strumento si adatta a te", "Non sei tu a cambiare processo per seguire il programma."),
                   ("Meno lavoro manuale", "Le attività ripetitive diventano automatiche."),
                   ("Dati in un unico posto", "Informazioni ordinate e accessibili a chi ne ha bisogno."),
                   ("Cresce con l'attività", "Si parte dall'essenziale e si aggiungono funzioni quando servono.")],
         caps=[("Applicazioni web", "Strumenti utilizzabili dal browser, su computer e dispositivi mobili."),
               ("Gestionali interni", "Clienti, ordini, prenotazioni o pratiche in un'unica interfaccia."),
               ("Aree riservate", "Spazi con accesso dedicato per clienti o collaboratori."),
               ("Integrazioni", "Collegamenti tra il tuo sito e gli strumenti che usi già."),
               ("Automazioni", "Passaggi ripetitivi eseguiti senza intervento manuale."),
               ("Evoluzione nel tempo", "Correzioni, aggiornamenti e nuove funzioni dopo il rilascio.")],
         projects=[],
         faq=[("Quanto costa un'applicazione su misura?", "Dipende dalle funzionalità. Di solito partiamo da una prima versione con l'essenziale, così puoi usarla presto e decidere insieme come farla crescere."),
              ("Da dove si parte?", "Da una chiamata in cui ci racconti come lavori oggi e dove perdi tempo. Da lì capiamo se uno strumento su misura è davvero la soluzione giusta."),
              ("Cosa succede dopo la consegna?", "Possiamo seguire correzioni, aggiornamenti ed evoluzioni nel tempo, in base a come lo strumento viene usato.")]),
]

PROJECTS = {
    "immobilgreen": dict(name="ImmobilGreen Garda", cat="Real estate, sito multilingua", url="https://immobilgreengarda.com",
        desc="Sito per la presentazione di quattro residenze di nuova costruzione a Manerba del Garda, vista lago, disponibile in italiano, inglese, francese e tedesco.",
        img="immobilgreen", alt="Homepage del sito ImmobilGreen Garda con vista sul Lago di Garda", dh=815, mh=711),
    "drivenode": dict(name="Drivenode", cat="Piattaforma eventi, web design e sviluppo", url="https://drivenode.it",
        desc="Piattaforma che raccoglie il calendario degli eventi dedicati al mondo auto e moto in Italia, con schede evento, località e contatti diretti.",
        img="drivenode", alt="Homepage di Drivenode con il calendario eventi del settore auto e moto", dh=900, mh=844),
    "momopolis": dict(name="Momòpolis", cat="Intrattenimento per famiglie, web design e sviluppo", url="https://momopolis.ch",
        desc="Sito per un family bar & park al coperto a Mendrisio, con la presentazione degli spazi, del bar e delle feste di compleanno.",
        img="momopolis", alt="Homepage del sito Momòpolis Family Bar & Park", dh=900, mh=844),
    "evamarketing": dict(name="Eva Marketing", cat="Consulenza e marketing, sito web", url="https://evamarketing.ch",
        desc="Sito per uno studio di consulenza, branding e marketing digitale rivolto ad aziende e professionisti, con la presentazione dei servizi e la prenotazione di una consulenza.",
        img="evamarketing", alt="Homepage del sito Eva Marketing", dw=800, dh=500, mh=844),
    "ulakasha": dict(name="Ūlakasha", cat="Moda artigianale, sito ed e-commerce", url="https://ulakasha.com",
        desc="Sito per un brand di abiti artigianali realizzati su ordinazione, con le creazioni, le collaborazioni, gli eventi e la prenotazione diretta dei capi, in italiano e inglese.",
        img="ulakasha", alt="Homepage del sito Ūlakasha con il logo della libellula", dw=800, dh=500, mh=844),
    "strasemplice": dict(name="STRASemplice", cat="Eventi e community, sito web", url="https://strasemplice.ch",
        desc="Sito per una community che organizza aperitivi, serate ed escursioni per conoscere gente nuova a Lugano e dintorni, con il calendario degli eventi e l'iscrizione online.",
        img="strasemplice", alt="Homepage del sito STRASemplice: la solita cerchia può aspettare", dw=800, dh=500, mh=844),
}

METHOD = [
    ("Ascoltiamo", "Una prima chiamata per capire obiettivi, tempi e budget. Facciamo domande prima di proporre soluzioni."),
    ("Progettiamo", "Definiamo struttura, contenuti e direzione visiva, così vedi come sarà il lavoro prima dello sviluppo."),
    ("Sviluppiamo", "Costruiamo il sito, la campagna o lo strumento, e lo verifichiamo su più dispositivi prima del lancio."),
    ("Miglioriamo", "Dopo la pubblicazione guardiamo i dati e correggiamo ciò che non funziona. Il lavoro non si ferma al lancio."),
]

WHY = [
    ("Un solo interlocutore", "Sito, marketing, consulenza e applicazioni nello stesso posto. Non devi coordinare fornitori diversi né rispiegare il progetto a ogni passaggio."),
    ("Assistenza su misura", "Ogni cliente ha esigenze diverse: ti seguiamo nei modi e nei tempi che servono a te, dal primo contatto a dopo il lancio."),
    ("Cura dell'esperienza utente", "Testi chiari, percorsi semplici, pulsanti dove le persone li cercano. Un sito facile da usare lavora meglio per te."),
    ("Attenzione alle prestazioni", "Pagine leggere e veloci anche da smartphone, perché nessuno aspetta un sito lento."),
    ("Supporto nel tempo", "Dopo il lancio restiamo raggiungibili per modifiche, aggiornamenti e nuove idee."),
]

# ---------------------------------------------------------------- helpers
ICON_EXT = '<svg class="icon-ext" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 9l6-6M4 3h5v5" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
MARK = '<svg class="brand-mark" viewBox="0 0 26 26" aria-hidden="true"><rect class="l1" x="0" y="11" width="15" height="15"/><rect class="l2" x="11" y="0" width="15" height="15"/></svg>'

def glyph(cells):
    rects = []
    for y in range(4):
        for x in range(4):
            cls = ' class="on"' if (x, y) in cells else ''
            rects.append(f'<rect{cls} x="{x*7}" y="{y*7}" width="5" height="5"/>')
    return f'<svg class="service-glyph" viewBox="0 0 26 26" aria-hidden="true">{"".join(rects)}</svg>'

NAV = [("Home", ""), ("Servizi", "servizi/"), ("Progetti", "progetti/"), ("Chi siamo", "chi-siamo/")]

def header(R, current):
    items = "".join(f'<li><a href="{R}{href}"{" aria-current=\"page\"" if current == href else ""}>{label}</a></li>' for label, href in NAV)
    mitems = "".join(f'<li><a class="m-link" href="{R}{href}"{" aria-current=\"page\"" if current == href else ""}>{label}</a></li>' for label, href in NAV + [("Contatti", "contatti/")])
    return f'''<a class="skip-link" href="#main">Vai al contenuto</a>
<header class="site-header on-dark">
  <div class="wrap header-inner">
    <a class="brand" href="{R}" aria-label="{BRAND}, vai alla home"><img class="brand-logo" src="{R}assets/logo-bilux-tech.webp?v={V}" alt="" width="450" height="88"></a>
    <nav class="main-nav" aria-label="Navigazione principale"><ul>{items}</ul></nav>
    <a class="btn btn--small header-cta" href="{R}contatti/"{" aria-current=\"page\"" if current == "contatti/" else ""}>Contatti</a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Apri il menu"><span></span><span></span></button>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu" aria-hidden="true">
  <nav aria-label="Navigazione mobile"><ul>{mitems}</ul></nav>
  <div class="mobile-menu-foot"><span>Scrivici</span><a href="mailto:{EMAIL}">{EMAIL}</a><span>Lombardia e Ticino</span></div>
</div>'''

def footer(R):
    svc = "".join(f'<a href="{R}servizi/{s["slug"]}/">{s["name"]}</a>' for s in SERVICES)
    return f'''<footer class="site-footer on-dark">
  <div class="wrap">
    <div class="grid footer-top">
      <div class="footer-claim"><img class="footer-logo" src="{R}assets/logo-bilux-tech.webp?v={V}" alt="{BRAND}" width="450" height="88" loading="lazy"><p>Tutti sono online. Pochi sono conosciuti.</p></div>
      <div class="footer-col"><h2>Servizi</h2>{svc}</div>
      <div class="footer-col"><h2>Studio</h2><a href="{R}progetti/">Progetti</a><a href="{R}chi-siamo/">Chi siamo</a><a href="{R}contatti/">Contatti</a></div>
      <div class="footer-col"><h2>Contatti</h2><a href="mailto:{EMAIL}">{EMAIL}</a><p>Lombardia e Ticino</p></div>
    </div>
    <div class="footer-bottom"><span>© 2026 {BRAND} · <a href="{R}privacy/">Privacy</a></span><button class="lights-switch" type="button" aria-pressed="false"><span class="sw" aria-hidden="true"></span><span class="sw-label">Spegni la luce</span></button><a href="#main">Torna su</a></div>
  </div>
</footer>'''

ORG = {
    "@context": "https://schema.org", "@type": "ProfessionalService", "@id": SITE + "/#org",
    "name": BRAND, "url": SITE + "/", "email": EMAIL, "image": SITE + "/assets/og-image.png",
    "description": "Studio digitale: siti web e landing page, marketing e advertising, consulenza, applicazioni e software su misura.",
    "areaServed": [{"@type": "AdministrativeArea", "name": "Lombardia"}, {"@type": "AdministrativeArea", "name": "Canton Ticino"}],
    "knowsLanguage": "it",
}

def page(path, title, desc, body, current="", schema=None, crumbs=None, robots="index, follow"):
    depth = path.count("/")
    R = "../" * depth
    canonical = SITE + "/" + path.replace("index.html", "")
    graph = [ORG]
    if crumbs:
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + u} for i, (n, u) in enumerate(crumbs)]})
    if schema: graph += schema
    ld = json.dumps({"@context": "https://schema.org", "@graph": [{k: v for k, v in g.items() if k != "@context"} for g in graph]}, ensure_ascii=False, indent=1)
    doc = f'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#101114">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:locale" content="it_IT">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{R}assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{R}assets/apple-touch-icon.png">
<link rel="preload" href="{R}assets/fonts/space-grotesk.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{R}assets/fonts/manrope.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{R}css/style.css?v={V}">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{header(R, current)}
<main id="main">
{body(R)}
</main>
{footer(R)}
<a class="m-cta" href="{R}contatti/">Raccontaci il tuo progetto</a>
<script src="{R}js/main.js?v={V}" defer></script>
</body>
</html>
'''
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f: f.write(doc)
    return canonical

# ---------------------------------------------------------------- blocks
def project_html(R, key, variant, on_light=False):
    p = PROJECTS[key]
    return f'''<article class="project project--{variant}">
  <a class="project-media reveal-media" href="{p["url"]}" target="_blank" rel="noopener" aria-label="Apri il sito {e(p["name"])} in una nuova scheda">
    <div class="project-frame"><img src="{R}assets/projects/{p["img"]}-desktop.webp?v={V}" alt="{e(p["alt"])}" width="{p.get("dw", 1440)}" height="{p["dh"]}" loading="lazy" decoding="async"></div>
    <div class="project-phone"><img src="{R}assets/projects/{p["img"]}-mobile.webp?v={V}" alt="" width="390" height="{p["mh"]}" loading="lazy" decoding="async"></div>
  </a>
  <div class="project-info">
    <h3>{e(p["name"])}</h3>
    <p class="project-cat">{e(p["cat"])}</p>
    <p class="project-desc">{e(p["desc"])}</p>
    <a class="text-link" href="{p["url"]}" target="_blank" rel="noopener">Visita il sito{ICON_EXT}<span class="visually-hidden"> (si apre in una nuova scheda)</span></a>
  </div>
</article>'''

def projects_all(R, keys=None):
    keys = keys or ["immobilgreen", "ulakasha", "strasemplice", "drivenode", "momopolis", "evamarketing"]
    variants = ["wide", "left", "right", "offset", "left", "right"]
    return '<div class="projects-list">' + "".join(project_html(R, k, v) for k, v in zip(keys, variants)) + '</div>'


def projects_carousel(R):
    cards = ""
    for k in ["immobilgreen", "ulakasha", "strasemplice", "drivenode", "momopolis", "evamarketing"]:
        p = PROJECTS[k]
        cards += f'''<li class="pj-card">
  <a class="pj-media reveal-media" href="{p["url"]}" target="_blank" rel="noopener" aria-label="Apri il sito {e(p["name"])} in una nuova scheda">
    <div class="project-frame"><img src="{R}assets/projects/{p["img"]}-desktop.webp?v={V}" alt="{e(p["alt"])}" width="{p.get("dw", 1440)}" height="{p["dh"]}" loading="lazy" decoding="async"></div>
    <div class="project-phone"><img src="{R}assets/projects/{p["img"]}-mobile.webp?v={V}" alt="" width="390" height="{p["mh"]}" loading="lazy" decoding="async"></div>
  </a>
  <div class="pj-info">
    <h3>{e(p["name"])}</h3>
    <p class="project-cat">{e(p["cat"])}</p>
    <p class="project-desc">{e(p["desc"])}</p>
    <a class="text-link" href="{p["url"]}" target="_blank" rel="noopener">Visita il sito{ICON_EXT}<span class="visually-hidden"> (si apre in una nuova scheda)</span></a>
  </div>
</li>'''
    arrow = lambda d: f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{d}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return f'''<div class="pj-carousel">
  <div class="wrap pj-bar"><p class="pj-label">Vedi alcuni progetti</p>
    <div class="pj-nav"><button class="pj-btn pj-prev" type="button" aria-label="Progetto precedente" disabled>{arrow("M15 5l-7 7 7 7")}</button><button class="pj-btn pj-next" type="button" aria-label="Progetto successivo">{arrow("M9 5l7 7-7 7")}</button></div>
  </div>
  <ul class="pj-track" tabindex="0" aria-label="Progetti, scorri orizzontalmente">{cards}</ul>
  <div class="wrap"><div class="pj-progress" aria-hidden="true"><span></span></div></div>
</div>'''

def method_html(title="Dall'idea al risultato. Senza complicazioni inutili.", intro="Quattro passaggi, sempre gli stessi, qualunque sia il progetto.", dark=False):
    steps = "".join(f'<li class="method-step"><span class="method-num">0{i+1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(METHOD))
    cls = "on-dark" if dark else "on-white"
    return f'''<section class="section {cls}" aria-labelledby="metodo-title">
  <div class="wrap">
    <div class="section-head"><h2 id="metodo-title" class="reveal">{title}</h2><p class="reveal">{intro}</p></div>
    <ol class="method">{steps}</ol>
  </div>
</section>'''

def contact_form(on_light=False):
    opts = "".join(f'<option>{s["name"]}</option>' for s in SERVICES)
    return f'''<form class="form" name="contatto" method="POST" action="/grazie/" data-netlify="true" netlify-honeypot="sito_web" data-contact data-endpoint="{FORM_ENDPOINT}" data-mailto="{EMAIL}" novalidate>
  <input type="hidden" name="form-name" value="contatto">
  <div class="form-row">
    <div class="field"><label for="f-nome">Nome e cognome</label><input id="f-nome" name="nome" type="text" autocomplete="name" required aria-describedby="e-nome"><span class="field-error" id="e-nome"></span></div>
    <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" inputmode="email" required aria-describedby="e-email"><span class="field-error" id="e-email"></span></div>
  </div>
  <div class="form-row">
    <div class="field"><label for="f-azienda">Azienda <span class="opt">(facoltativo)</span></label><input id="f-azienda" name="azienda" type="text" autocomplete="organization"></div>
    <div class="field"><label for="f-servizio">Di cosa hai bisogno?</label><select id="f-servizio" name="servizio">{opts}<option>Non lo so ancora</option></select></div>
  </div>
  <div class="field"><label for="f-msg">Raccontaci il progetto</label><textarea id="f-msg" name="messaggio" rows="5" required aria-describedby="e-msg" placeholder="Cosa ti serve, per quando, ed eventuali link utili."></textarea><span class="field-error" id="e-msg"></span></div>
  <div class="field"><label class="consent"><input type="checkbox" name="consenso" value="si" required aria-describedby="e-consenso"><span>Acconsento all'uso dei miei dati solo per ricevere una risposta a questa richiesta, come descritto nell'<a href="/privacy/" class="text-link">informativa privacy</a>.</span></label><span class="field-error" id="e-consenso"></span></div>
  <div class="hp" aria-hidden="true"><label>Lascia vuoto<input type="text" name="sito_web" tabindex="-1" autocomplete="off"></label></div>
  <div class="form-foot"><button class="btn {"" if on_light else "btn--dark"}" type="submit">Invia richiesta</button></div>
  <p class="form-status" role="status" aria-live="polite" tabindex="-1"></p>
</form>'''

def cta_band(R, title="Hai un progetto in mente? Parliamone."):
    return f'''<section class="cta-band on-accent">
  <div class="wrap"><h2 class="reveal">{title}</h2>
    <div class="cta-actions reveal"><a class="btn btn--white" href="{R}contatti/">Raccontaci il tuo progetto</a></div>
  </div>
</section>'''

def page_hero(R, crumbs, h1, lede, cta=True, beam="web"):
    bc = "".join(f'<li><a href="{R}{u}">{n}</a></li>' for n, u in crumbs[:-1]) + f'<li aria-current="page">{crumbs[-1][0]}</li>'
    actions = f'<div class="hero-actions"><a class="btn" href="{R}contatti/">Raccontaci il tuo progetto</a></div>' if cta else ""
    return f'''<section class="page-hero stage on-dark" data-torch data-beam="{beam}">
  <canvas class="dust" aria-hidden="true"></canvas>
  <div class="wrap">
    <nav class="breadcrumb" aria-label="Percorso"><ol>{bc}</ol></nav>
    <h1>{h1}</h1>
    <p class="lead">{lede}</p>
    {actions}
  </div>
</section>'''


BEAMS = ["web", "mkt", "con", "sw"]
def _prism_big():
    ys = [75, 225, 375, 525]
    EX, EY = 247, 297            # exit point on the right face
    cols = {"web": "#315CFF", "mkt": "#9A7BFF", "con": "#3CCBF4", "sw": "#F2C14E"}
    defs, rays = "", ""
    for i, (y, b) in enumerate(zip(ys, BEAMS)):
        c = cols[b]
        defs += (f'<linearGradient id="rg{i}" gradientUnits="userSpaceOnUse" x1="{EX}" y1="{EY}" x2="400" y2="{y}">'
                 f'<stop offset="0" stop-color="{c}" stop-opacity="1"/><stop offset=".55" stop-color="{c}" stop-opacity=".6"/>'
                 f'<stop offset="1" stop-color="{c}" stop-opacity=".06"/></linearGradient>')
        poly = f"{EX},{EY-2.5} 400,{y-20} 400,{y+20} {EX},{EY+2.5}"
        rays += (f'<polygon class="p-ray p-ray-glow" data-ray="{i}" style="--i:{i}" points="{poly}" fill="{c}" filter="url(#soft)"/>'
                 f'<polygon class="p-ray" data-ray="{i}" style="--i:{i}" points="{poly}" fill="url(#rg{i})"/>')
    return ('<svg class="prism-svg" viewBox="0 0 400 600" aria-hidden="true"><defs>'
            '<filter id="soft" x="-20%" y="-60%" width="140%" height="220%"><feGaussianBlur stdDeviation="9"/></filter>'
            '<filter id="softS" x="-20%" y="-200%" width="140%" height="500%"><feGaussianBlur stdDeviation="3"/></filter>'
            '<linearGradient id="beamG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#17181B" stop-opacity="0"/><stop offset=".35" stop-color="#9AA6D8" stop-opacity=".55"/><stop offset="1" stop-color="#FFFFFF"/></linearGradient>'
            '<linearGradient id="glassG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4A5FE0"/><stop offset=".55" stop-color="#22308F"/><stop offset="1" stop-color="#1A2470"/></linearGradient>'
            '<radialGradient id="coreG" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".4" stop-color="#9DB4FF" stop-opacity=".8"/><stop offset="1" stop-color="#315CFF" stop-opacity="0"/></radialGradient>'
            + defs + '</defs>'
            '<g class="p-glass"><polygon points="200,212 98,388 302,388" fill="url(#glassG)" opacity=".92"/>'
            '<polygon points="200,226 116,378 200,378" fill="#FFFFFF" opacity=".07"/>'
            '<polygon points="200,212 98,388 302,388" fill="none" stroke="#DDE3FF" stroke-width="1.6" stroke-linejoin="round" opacity=".9"/></g>'
            '<polygon class="p-beam" points="0,299 152,297 152,303 0,301" fill="url(#beamG)"/>'
            '<polygon class="p-beam" points="0,298 152,295 152,305 0,302" fill="#FFFFFF" opacity=".35" filter="url(#softS)"/>'
            + rays +
            '<line class="p-core" x1="152" y1="300" x2="247" y2="297" stroke="#FFFFFF" stroke-width="2" opacity=".85"/>'
            '<circle class="p-core" cx="247" cy="297" r="16" fill="url(#coreG)"/></svg>')
def _prism_mini():
    ys = [36, 82, 128, 174]
    cols = ["#315CFF", "#9A7BFF", "#3CCBF4", "#F2C14E"]
    rays = "".join(f'<polygon class="m-ray" style="--i:{i}" points="262,104 560,{y-12} 560,{y+12} 262,108" fill="{c}" opacity=".85"/>' for i, (y, c) in enumerate(zip(ys, cols)))
    return ('<svg class="prism-mini" viewBox="0 0 560 210" aria-hidden="true">'
            '<defs><linearGradient id="mg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4A5FE0"/><stop offset="1" stop-color="#1A2470"/></linearGradient>'
            '<linearGradient id="mb" x1="0" x2="1"><stop offset="0" stop-color="#17181B" stop-opacity="0"/><stop offset="1" stop-color="#17181B" stop-opacity=".7"/></linearGradient></defs>'
            '<polygon points="0,105 196,104 196,108 0,107" fill="url(#mb)"/>' + rays +
            '<polygon points="230,40 172,172 288,172" fill="url(#mg)" stroke="#DDE3FF" stroke-width="1.5" stroke-linejoin="round"/></svg>')
PRISM_SVG = _prism_big()
PRISM_MINI = _prism_mini()

# ---------------------------------------------------------------- pages
urls = []

def home(R):
    rows = "".join(f'''<li class="service-row" data-beam="{s["beam"]}" data-ray="{i}"><a href="{R}servizi/{s["slug"]}/"><span class="service-name">{s["name"]}</span><span class="service-desc">{s["row"]}</span></a></li>''' for i, s in enumerate(SERVICES))
    why = "".join(f'<div class="why-item"><h3>{t}</h3><p>{d}</p></div>' for t, d in WHY)
    return f'''<section class="hero stage on-dark" data-torch aria-labelledby="hero-title">
  <canvas class="dust" aria-hidden="true"></canvas>
  <div class="wrap hero-content">
    <p class="hero-place">Studio digitale in Lombardia e Ticino</p>
    <h1 class="hero-title" id="hero-title"><span class="line"><span data-text="Tutti sono online.">Tutti sono online.</span></span><span class="line"><span data-text="Pochi sono conosciuti.">Pochi sono conosciuti.</span></span></h1>
    <div class="hero-body">
      <p class="hero-lede">Siti web, applicazioni su misura e strategie digitali progettati per dare forma alle idee e rispondere a esigenze reali.</p>
      <div class="hero-actions"><a class="btn" href="{R}contatti/">Raccontaci il tuo progetto</a><a class="btn btn--ghost" href="#servizi">Scopri cosa facciamo</a></div>
    </div>
  </div>
  <p class="torch-hint" aria-hidden="true">Muovi il mouse: la luce la porti tu.</p>
</section>

<section class="manifesto" aria-labelledby="manifesto-title">
  <div class="wrap grid">
    <h2 class="manifesto-title reveal" id="manifesto-title">Non basta essere online. Serve avere qualcosa da dire.</h2>
    <div class="manifesto-body reveal">
      <p class="lead">Un sito, una campagna o un'applicazione valgono qualcosa solo se aiutano qualcuno a scegliere, a trovare un'informazione o a finire un lavoro.</p>
      <p class="muted">Per questo partiamo da cosa deve succedere dopo il clic, come una richiesta di preventivo, una prenotazione o un processo più rapido, e progettiamo lo strumento più semplice che lo rende possibile.</p>
    </div>
  </div>
</section>

<section class="section on-white on-light" id="servizi" aria-labelledby="servizi-title">
  <div class="wrap">
    <div class="section-head"><h2 id="servizi-title" class="reveal">Una luce, quattro colori.</h2><p class="reveal">Ogni progetto parte da un'idea sola. Poi si scompone in quello che serve: sito, marketing, consulenza o applicazioni. Da soli o insieme.</p></div>
    <div class="prism-wrap">
      {PRISM_SVG}
      <div>{PRISM_MINI}<ul class="prism-list">{rows}</ul></div>
    </div>
  </div>
</section>

<section class="section on-dark" id="progetti" aria-labelledby="progetti-title">
  <div class="wrap">
    <div class="section-head"><h2 id="progetti-title" class="reveal">Il nostro lavoro, senza troppe parole.</h2><p class="reveal">Siti realizzati per aziende, brand e community in Italia e in Svizzera.</p></div>
  </div>
  {projects_carousel(R)}
  <div class="wrap">
    <div class="projects-more"><a class="btn btn--ghost" href="{R}progetti/">Vedi tutti i progetti</a></div>
  </div>
</section>

{method_html()}

<section class="section on-dark" aria-labelledby="perche-title">
  <div class="wrap grid why">
    <div class="why-head"><h2 id="perche-title" class="reveal">Perché Bilux Tech</h2><p class="reveal">Nessuna promessa miracolosa: solo il modo in cui lavoriamo, ogni giorno.</p></div>
    <div class="why-list">{why}</div>
  </div>
</section>

<section class="section on-accent" id="contatti" aria-labelledby="contatti-title">
  <div class="wrap grid contact">
    <div class="contact-intro">
      <h2 id="contatti-title" class="reveal">Hai un progetto in mente? Parliamone.</h2>
      <p class="lead reveal">Raccontaci in poche righe cosa ti serve. Ti rispondiamo entro un giorno lavorativo.</p>
      <div class="contact-direct reveal"><span>Preferisci scriverci direttamente?</span><a class="contact-mail text-link" href="mailto:{EMAIL}">{EMAIL}</a></div>
    </div>
    <div class="contact-form-wrap">{contact_form()}</div>
  </div>
</section>'''

urls.append(page("index.html", "Bilux Tech | Siti web, marketing e applicazioni su misura in Lombardia e Ticino",
    "Bilux Tech progetta siti web e landing page, campagne di marketing, percorsi di consulenza e applicazioni su misura per aziende in Lombardia e Ticino.",
    home, current=""))

# services overview
def services_page(R):
    items = "".join(f'''<article class="overview-item"><h2>{s["name"]}</h2><div class="ov-body"><p>{s["lede"]}</p>
<ul class="ov-tags">{"".join(f"<li>{c[0]}</li>" for c in s["caps"][:6])}</ul>
<p><a class="text-link" href="{R}servizi/{s["slug"]}/">Scopri {"le applicazioni su misura" if s["slug"] == "software" else s["short"].lower()}</a></p></div></article>''' for s in SERVICES)
    return f'''{page_hero(R, [("Home",""),("Servizi","servizi/")], "Quattro servizi, un solo interlocutore.", "Siti web, marketing, consulenza e applicazioni su misura. Puoi affidarci un singolo progetto o farli lavorare insieme.")}
<section class="section on-light"><div class="wrap"><div class="overview">{items}</div></div></section>
<section class="section on-dark"><div class="wrap grid split"><h2 class="reveal">Sito e marketing, dalla stessa parte.</h2><div class="prose reveal"><p>Una campagna ha bisogno di un posto efficace dove portare le persone. Un sito ha bisogno del traffico giusto per generare opportunità.</p><p class="muted">Seguendo entrambe le parti, ogni scelta su annunci, pagine e contenuti va nella stessa direzione.</p></div></div></section>
{cta_band(R)}'''
urls.append(page("servizi/index.html", "Servizi: siti web, marketing, consulenza e applicazioni | Bilux Tech",
    "Siti web e landing page, marketing e advertising, consulenza e applicazioni su misura: scopri i servizi di Bilux Tech per aziende in Lombardia e Ticino.",
    services_page, current="servizi/", crumbs=[("Home",""),("Servizi","servizi/")]))

for s in SERVICES:
    def svc_page(R, s=s):
        benefits = "".join(f'<div class="benefit reveal"><h3>{t}</h3><p>{d}</p></div>' for t, d in s["benefits"])
        caps = "".join(f'<div class="capability"><h3>{t}</h3><p>{d}</p></div>' for t, d in s["caps"])
        faq = "".join(f'<details><summary>{q}<span class="pm" aria-hidden="true"></span></summary><div class="faq-a"><p>{a}</p></div></details>' for q, a in s["faq"])
        proj = ""
        if s["projects"]:
            pj = "".join(project_html(R, k, v) for k, v in zip(s["projects"], ["left", "right"]))
            proj = f'''<section class="section on-dark" aria-labelledby="pj-title"><div class="wrap">
<div class="section-head"><h2 id="pj-title" class="reveal">Progetti realizzati</h2><p class="reveal"><a class="text-link" href="{R}progetti/">Vedi tutti i progetti</a></p></div>
<div class="projects-list">{pj}</div></div></section>'''
        return f'''{page_hero(R, [("Home",""),("Servizi","servizi/"),(s["name"], f"servizi/{s['slug']}/")], s["name"], s["lede"], beam=s["beam"])}
<section class="section"><div class="wrap grid split"><h2 class="reveal">{s["ex_title"]}</h2><div class="prose reveal">{"".join(f"<p>{p}</p>" for p in s["ex"])}</div></div></section>
<section class="section on-white on-light" aria-labelledby="ben-title"><div class="wrap">
<div class="section-head"><h2 id="ben-title" class="reveal">Cosa ottieni</h2></div>
<div class="benefits">{benefits}</div></div></section>
<section class="section on-dark" aria-labelledby="cap-title"><div class="wrap">
<div class="section-head"><h2 id="cap-title" class="reveal">Cosa possiamo fare per te</h2><p class="reveal">Le attività che compongono il servizio. Scegliamo insieme quelle che servono al tuo progetto.</p></div>
<div class="capabilities">{caps}</div></div></section>
{proj}
{method_html(title="Come lavoriamo", intro="Lo stesso metodo per ogni progetto: chiaro all'inizio, verificabile alla fine.")}
<section class="section" aria-labelledby="faq-title"><div class="wrap">
<div class="section-head"><h2 id="faq-title" class="reveal">Domande frequenti</h2></div>
<div class="faq">{faq}</div></div></section>
{cta_band(R)}'''
    faq_schema = [{"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]},
                  {"@type": "Service", "name": s["name"], "description": s["desc"], "provider": {"@id": SITE + "/#org"},
                   "areaServed": ORG["areaServed"]}]
    urls.append(page(f"servizi/{s['slug']}/index.html", s["title"], s["desc"], svc_page, current="servizi/",
        schema=faq_schema, crumbs=[("Home",""),("Servizi","servizi/"),(s["name"], f"servizi/{s['slug']}/")]))

def projects_page(R):
    return f'''{page_hero(R, [("Home",""),("Progetti","progetti/")], "Progetti", "Una selezione di siti realizzati per aziende, brand e community in Italia e in Svizzera, dal real estate sul Lago di Garda agli eventi a Lugano.")}
<section class="section on-dark" aria-label="Elenco progetti"><div class="wrap">{projects_all(R)}</div></section>
{cta_band(R, "Il prossimo può essere il tuo.")}'''
urls.append(page("progetti/index.html", "Progetti e siti web realizzati | Bilux Tech",
    "ImmobilGreen Garda, Ūlakasha, STRASemplice, Drivenode, Momòpolis ed Eva Marketing: alcuni dei siti web progettati e sviluppati da Bilux Tech.",
    projects_page, current="progetti/", crumbs=[("Home",""),("Progetti","progetti/")]))

def about_page(R):
    return f'''{page_hero(R, [("Home",""),("Chi siamo","chi-siamo/")], "Uno studio piccolo, per scelta.", "Bilux Tech progetta siti web, marketing, consulenza e applicazioni su misura per aziende e professionisti in Lombardia e in Ticino.")}
<section class="section"><div class="wrap grid split"><h2 class="reveal">Chi segue il progetto è la persona con cui parli.</h2>
<div class="prose reveal"><p>Bilux Tech è uno studio indipendente. Seguiamo direttamente ogni progetto, dalla progettazione del sito o di un'applicazione alla gestione delle campagne.</p>
<p class="muted">Lavorare con una struttura piccola significa meno passaggi, comunicazione diretta e continuità dall'inizio alla fine. Ogni progetto parte da una chiamata conoscitiva, in cui capiamo obiettivi, tempi e budget prima di proporre una direzione.</p></div></div></section>
<section class="section on-white" aria-labelledby="val-title"><div class="wrap">
<div class="section-head"><h2 id="val-title" class="reveal">Come ci piace lavorare</h2></div>
<div class="about-values">
<div class="reveal"><h3>Comunicazione diretta</h3><p>Nessun intermediario tra te e chi lavora al progetto. Le domande ricevono risposte, non ticket.</p></div>
<div class="reveal"><h3>Tecnica e marketing insieme</h3><p>Chi sviluppa il sito conosce anche le campagne che ci porteranno traffico, e viceversa.</p></div>
<div class="reveal"><h3>Prima si capisce, poi si fa</h3><p>Ogni progetto parte da obiettivi chiari. Le soluzioni vengono dopo.</p></div>
</div></div></section>
{method_html(dark=True)}
{cta_band(R)}'''
urls.append(page("chi-siamo/index.html", "Chi siamo | Bilux Tech, studio digitale in Lombardia e Ticino",
    "Bilux Tech è uno studio digitale indipendente: chi segue il tuo progetto è la stessa persona con cui parli, dall'inizio alla fine.",
    about_page, current="chi-siamo/", crumbs=[("Home",""),("Chi siamo","chi-siamo/")]))

def contact_page(R):
    return f'''{page_hero(R, [("Home",""),("Contatti","contatti/")], "Parliamo del tuo progetto.", "Compila il modulo o scrivici un'email. Ti rispondiamo entro un giorno lavorativo.", cta=False)}
<section class="section on-light"><div class="wrap grid contact">
  <div class="contact-intro">
    <h2 class="h3">Come funziona</h2>
    <ol class="prose" style="margin-top:24px;display:grid;gap:14px">
      <li><strong>1. Ci scrivi</strong> <span class="muted">con due righe sul progetto, anche se non è ancora tutto definito.</span></li>
      <li><strong>2. Ti rispondiamo</strong> <span class="muted">entro un giorno lavorativo per fissare una prima chiamata.</span></li>
      <li><strong>3. Ne parliamo</strong> <span class="muted">e capiamo insieme obiettivi, tempi e budget prima di proporti una direzione.</span></li>
    </ol>
    <div class="contact-direct"><span class="muted">Email</span><a class="contact-mail text-link" href="mailto:{EMAIL}">{EMAIL}</a></div>
    <div class="contact-direct"><span class="muted">Dove lavoriamo</span><p class="h3" style="font-size:1.25rem">Lombardia e Canton Ticino</p></div>
  </div>
  <div class="contact-form-wrap">{contact_form(on_light=True)}</div>
</div></section>'''
urls.append(page("contatti/index.html", "Contatti | Bilux Tech",
    "Raccontaci il tuo progetto: siti web, marketing, consulenza o applicazioni su misura. Rispondiamo entro un giorno lavorativo.",
    contact_page, current="contatti/", crumbs=[("Home",""),("Contatti","contatti/")]))


def privacy_page(R):
    sec = lambda t, body: f'<h2 class="h3" style="margin-top:56px;margin-bottom:16px">{t}</h2>{body}'
    return f'''{page_hero(R, [("Home",""),("Privacy","privacy/")], "Informativa privacy", "Come trattiamo i dati che ci lasci tramite questo sito.", cta=False)}
<section class="section on-light"><div class="wrap"><div class="prose" style="max-width:72ch">
<p class="muted">Ultimo aggiornamento: {PRIVACY_DATA}</p>
{sec("Titolare del trattamento", f"<p>{TITOLARE}. Per qualsiasi domanda sui tuoi dati puoi scriverci a <a class='text-link' href='mailto:{EMAIL}'>{EMAIL}</a>.</p>")}
{sec("Quali dati raccogliamo", "<p>Quando compili il modulo di contatto raccogliamo nome e cognome, indirizzo email, azienda (facoltativa), il servizio che ti interessa e il testo del messaggio. Se ci scrivi via email trattiamo i dati contenuti nel messaggio.</p><p>Come ogni sito web, il server che lo ospita registra automaticamente alcuni dati tecnici (ad esempio indirizzo IP, data e ora della visita, tipo di browser) per garantirne il funzionamento e la sicurezza.</p>")}
{sec("Perché li usiamo", "<p>Usiamo i dati del modulo solo per rispondere alla tua richiesta ed eventualmente preparare un'offerta. Non li usiamo per newsletter o pubblicità e non li vendiamo a terzi.</p><p>La base del trattamento è il tuo consenso e la necessità di dare seguito a una tua richiesta prima di un eventuale contratto (art. 6 par. 1 lett. a e b GDPR; Legge federale sulla protezione dei dati, nLPD).</p>")}
{sec("Chi tratta i dati per nostro conto", "<p>Il sito e il modulo di contatto sono gestiti tramite Netlify, Inc. (Stati Uniti), che conserva i messaggi inviati e ce li inoltra via email. Il trasferimento avviene sulla base delle garanzie previste dalla normativa, come le clausole contrattuali standard.</p><p>Il sito non utilizza cookie di profilazione, strumenti di statistica o servizi di terze parti come font o video esterni.</p>")}
{sec("Per quanto tempo li conserviamo", "<p>Conserviamo i dati per il tempo necessario a gestire la tua richiesta e, se nasce una collaborazione, per la durata del rapporto e gli obblighi di legge che ne derivano.</p>")}
{sec("I tuoi diritti", f"<p>Puoi chiederci in qualsiasi momento di accedere ai tuoi dati, correggerli, cancellarli, limitarne l'uso o opporti al trattamento, e revocare il consenso dato. Scrivici a <a class='text-link' href='mailto:{EMAIL}'>{EMAIL}</a>.</p><p>Hai inoltre il diritto di presentare un reclamo all'autorità di controllo competente: in Svizzera l'Incaricato federale della protezione dei dati e della trasparenza (IFPDT), in Italia il Garante per la protezione dei dati personali.</p>")}
</div></div></section>'''
urls.append(page("privacy/index.html", "Informativa privacy | Bilux Tech", "Come Bilux Tech tratta i dati personali raccolti tramite il sito e il modulo di contatto.",
    privacy_page, crumbs=[("Home",""),("Privacy","privacy/")]))

def thanks_page(R):
    return f'''<section class="page-hero stage on-dark notfound" data-torch><canvas class="dust" aria-hidden="true"></canvas>
<div class="wrap"><h1>Messaggio inviato.</h1><p class="lead">Grazie per averci scritto. Ti rispondiamo entro un giorno lavorativo.</p>
<div class="hero-actions"><a class="btn" href="{R}">Torna alla home</a><a class="btn btn--ghost" href="{R}progetti/">Guarda i progetti</a></div></div></section>'''
page("grazie/index.html", "Messaggio inviato | Bilux Tech", "Grazie per averci scritto.", thanks_page, robots="noindex")

def notfound(R):
    return f'''<section class="page-hero stage on-dark notfound" data-torch><canvas class="dust" aria-hidden="true"></canvas>
<div class="wrap"><h1>Qui è buio pesto.</h1><p class="lead">Questa pagina non esiste, o forse è cambiata con il nuovo sito. Riparti dalla home o dai servizi.</p>
<div class="hero-actions"><a class="btn" href="/">Torna alla home</a><a class="btn btn--ghost" href="/servizi/">Vedi i servizi</a></div></div></section>'''
# 404 lives at root and uses absolute paths because it is served for any missing URL
page("404.html", "Pagina non trovata | Bilux Tech", "La pagina che cerchi non esiste.", lambda R: notfound("/"), robots="noindex")
with open(os.path.join(OUT, "404.html"), encoding="utf-8") as f: s404 = f.read()
s404 = s404.replace('href="css/', 'href="/css/').replace('href="assets/', 'href="/assets/').replace('src="js/', 'src="/js/').replace('href="servizi/', 'href="/servizi/').replace('href="progetti/', 'href="/progetti/').replace('href="chi-siamo/', 'href="/chi-siamo/').replace('href="contatti/', 'href="/contatti/').replace('href=""', 'href="/"')
with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f: f.write(s404)

# ---------------------------------------------------------------- sitemap, robots, redirects
sm = "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}</urlset>\n')
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

print("\n".join(urls))
