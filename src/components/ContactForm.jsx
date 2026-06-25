import React, { useState } from "react";
import { Send, CheckCircle2, AlertCircle } from "lucide-react";
import { supabase } from "../lib/supabaseClient.js";

/**
 * Form di contatto collegato a Supabase: ogni invio viene salvato come riga
 * nella tabella "messages" del tuo progetto Supabase.
 *
 * SETUP RICHIESTO PRIMA DEL DEPLOY:
 * 1. Crea un progetto su https://supabase.com (gratuito).
 * 2. Nel SQL editor di Supabase esegui lo script che trovi in
 *    supabase/schema.sql per creare la tabella "messages".
 * 3. Copia Project URL e anon public key da
 *    Project Settings → API e crea un file ".env" nella root del progetto
 *    (parti da .env.example) con:
 *      VITE_SUPABASE_URL=...
 *      VITE_SUPABASE_ANON_KEY=...
 * 4. (Opzionale ma consigliato) Configura una Supabase Edge Function o un
 *    "Database Webhook" per inviarti un'email a biluxtech@gmail.com a ogni
 *    nuovo inserimento — i dati restano comunque sempre visibili nella
 *    dashboard Supabase, tabella "messages".
 */

export default function ContactForm() {
  const [status, setStatus] = useState("idle"); // idle | submitting | success | error
  const [values, setValues] = useState({ name: "", email: "", message: "" });

  function handleChange(e) {
    setValues((v) => ({ ...v, [e.target.name]: e.target.value }));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setStatus("submitting");

    const { error } = await supabase.from("messages").insert({
      name: values.name,
      email: values.email,
      message: values.message,
    });

    if (error) {
      console.error("Errore Supabase:", error.message);
      setStatus("error");
      return;
    }

    setStatus("success");
    setValues({ name: "", email: "", message: "" });
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
