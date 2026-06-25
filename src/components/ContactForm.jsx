import React, { useState } from "react";
import { Send, CheckCircle2, AlertCircle } from "lucide-react";

/**
 * Form di contatto funzionante senza backend proprio, tramite Formspree
 * (https://formspree.io — piano free sufficiente per un sito vetrina).
 *
 * SETUP RICHIESTO PRIMA DEL DEPLOY:
 * 1. Crea un account gratuito su https://formspree.io con l'email biluxtech@gmail.com
 * 2. Crea un nuovo form: Formspree genera un endpoint tipo
 *    https://formspree.io/f/XXXXXXXX
 * 3. Sostituisci FORMSPREE_ENDPOINT qui sotto con il tuo endpoint reale.
 * 4. Ogni invio dal form arriverà come email a biluxtech@gmail.com.
 *
 * In alternativa a Formspree puoi usare un altro servizio "form-to-email"
 * (es. Web3Forms, Netlify Forms se deployi su Netlify) cambiando solo l'URL
 * e il formato del body in handleSubmit.
 */

const FORMSPREE_ENDPOINT = "https://formspree.io/f/YOUR_FORM_ID";

export default function ContactForm() {
  const [status, setStatus] = useState("idle"); // idle | submitting | success | error
  const [values, setValues] = useState({ name: "", email: "", message: "" });

  function handleChange(e) {
    setValues((v) => ({ ...v, [e.target.name]: e.target.value }));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setStatus("submitting");

    try {
      const res = await fetch(FORMSPREE_ENDPOINT, {
        method: "POST",
        headers: { Accept: "application/json" },
        body: new FormData(e.target),
      });

      if (res.ok) {
        setStatus("success");
        setValues({ name: "", email: "", message: "" });
      } else {
        setStatus("error");
      }
    } catch {
      setStatus("error");
    }
  }

  if (status === "success") {
    return (
      <div className="flex flex-col items-center gap-3 text-cream/80 py-6">
        <CheckCircle2 size={28} className="text-cyan-300" />
        <p>Messaggio inviato. Ti risponderemo a breve.</p>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto text-left flex flex-col gap-4">
      <div>
        <label htmlFor="name" className="block text-xs font-mono uppercase text-cream/50 mb-1.5">
          Nome
        </label>
        <input
          id="name"
          name="name"
          type="text"
          required
          value={values.name}
          onChange={handleChange}
          className="w-full bg-ink-soft border border-cyan-400/15 rounded-md px-4 py-3 text-sm text-cream placeholder:text-cream/30 focus:outline-none focus:border-cyan-300 focus:shadow-[0_0_0_3px_rgba(0,255,255,0.15)] transition-all"
          placeholder="Il tuo nome"
        />
      </div>

      <div>
        <label htmlFor="email" className="block text-xs font-mono uppercase text-cream/50 mb-1.5">
          Email
        </label>
        <input
          id="email"
          name="email"
          type="email"
          required
          value={values.email}
          onChange={handleChange}
          className="w-full bg-ink-soft border border-cyan-400/15 rounded-md px-4 py-3 text-sm text-cream placeholder:text-cream/30 focus:outline-none focus:border-cyan-300 focus:shadow-[0_0_0_3px_rgba(0,255,255,0.15)] transition-all"
          placeholder="nome@email.com"
        />
      </div>

      <div>
        <label htmlFor="message" className="block text-xs font-mono uppercase text-cream/50 mb-1.5">
          Messaggio
        </label>
        <textarea
          id="message"
          name="message"
          required
          rows={4}
          value={values.message}
          onChange={handleChange}
          className="w-full bg-ink-soft border border-cyan-400/15 rounded-md px-4 py-3 text-sm text-cream placeholder:text-cream/30 focus:outline-none focus:border-cyan-300 focus:shadow-[0_0_0_3px_rgba(0,255,255,0.15)] transition-all resize-none"
          placeholder="Raccontaci cosa stai costruendo..."
        />
      </div>

      {status === "error" && (
        <div className="flex items-center gap-2 text-sm text-red-300">
          <AlertCircle size={16} /> Invio non riuscito. Riprova o scrivi direttamente via email.
        </div>
      )}

      <button
        type="submit"
        disabled={status === "submitting"}
        className="inline-flex items-center justify-center gap-2 bg-gradient-to-br from-electric to-[#0044CC] text-white font-semibold text-sm px-7 py-4 rounded-md shadow-[0_0_0_1px_rgba(0,255,255,0.25),0_8px_24px_-8px_rgba(0,102,255,0.7)] hover:-translate-y-0.5 transition-all disabled:opacity-60 disabled:translate-y-0"
      >
        <Send size={16} />
        {status === "submitting" ? "Invio in corso..." : "Invia messaggio"}
      </button>
    </form>
  );
}
