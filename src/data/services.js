import { Globe, LineChart, Users, Code2 } from "lucide-react";

export const CONTACT_EMAIL = "biluxtech@gmail.com";

export const SERVICES = [
  {
    slug: "siti-web",
    icon: Globe,
    title: "Siti web",
    tag: "Design + performance",
    eyebrow: "Servizio 01",
    lead: "Un sito costruito per generare contatti e vendite, non solo per esserci online.",
    points: ["Design su misura", "SEO tecnica", "Performance e velocità", "Mobile-first"],
    cta: "Parliamo del tuo sito",
  },
  {
    slug: "marketing",
    icon: LineChart,
    title: "Strategie di marketing",
    tag: "Acquisizione clienti",
    eyebrow: "Servizio 02",
    lead: "Un piano di acquisizione costruito sui tuoi numeri reali, non su template generici.",
    points: ["Posizionamento", "Funnel di acquisizione", "Advertising", "Analisi dei numeri"],
    cta: "Parliamo della tua strategia",
  },
  {
    slug: "consulenza",
    icon: Users,
    title: "Percorsi di consulenza",
    tag: "Affiancamento continuo",
    eyebrow: "Servizio 03",
    lead: "Affiancamento continuo per chi vuole imparare a guidare il marketing internamente.",
    points: ["Sessioni periodiche", "Formazione del team", "Reportistica", "Obiettivi misurabili"],
    cta: "Parliamo del tuo percorso",
  },
  {
    slug: "software",
    icon: Code2,
    title: "App e software su misura",
    tag: "Strumenti su misura",
    eyebrow: "Servizio 04",
    lead: "Strumenti costruiti intorno ai tuoi processi reali, per risparmiare ore ogni settimana.",
    points: ["Web app", "Integrazioni", "Automazioni", "Gestionali su misura"],
    cta: "Parliamo del tuo progetto",
  },
];
