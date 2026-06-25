import React from "react";
import { Mail } from "lucide-react";
import Nav from "../components/Nav.jsx";
import Footer from "../components/Footer.jsx";
import ServiceCard from "../components/ServiceCard.jsx";
import ContactForm from "../components/ContactForm.jsx";
import { SERVICES, CONTACT_EMAIL } from "../data/services.js";

function Hero() {
  return (
    <section
      className="relative pt-44 pb-20 px-7 text-center overflow-hidden"
      style={{
        backgroundImage:
          "radial-gradient(ellipse 60% 50% at 20% 0%, rgba(0,102,255,0.35), transparent 60%), radial-gradient(ellipse 50% 45% at 85% 15%, rgba(0,255,255,0.22), transparent 60%)",
      }}
    >
      <span className="block font-mono uppercase text-xs tracking-wider text-cyan-300 mb-5">
        Lombardia · Ticino
      </span>
      <h1 className="font-display text-4xl sm:text-6xl leading-[1.05] max-w-2xl mx-auto text-cream">
        Tecnologia e marketing,{" "}
        <span className="text-cyan-300 drop-shadow-[0_0_26px_rgba(0,255,255,0.5)]">in un unico posto</span>.
      </h1>
    </section>
  );
}

function Services() {
  return (
    <section id="servizi" className="py-16 px-7">
      <div className="max-w-6xl mx-auto grid sm:grid-cols-2 gap-px bg-cyan-400/15 border border-cyan-400/15">
        {SERVICES.map((s) => (
          <ServiceCard key={s.slug} {...s} />
        ))}
      </div>
    </section>
  );
}

function ContactCTA() {
  return (
    <section id="contatti" className="text-center py-28 px-7">
      <h2 className="font-display text-2xl sm:text-3xl text-cream mb-3">Parliamone.</h2>
      <p className="text-cream/55 text-sm mb-10">
        oppure scrivi direttamente a{" "}
        <a href={`mailto:${CONTACT_EMAIL}`} className="text-cyan-300 hover:underline inline-flex items-center gap-1">
          <Mail size={13} /> {CONTACT_EMAIL}
        </a>
      </p>
      <ContactForm />
    </section>
  );
}

export default function Home() {
  return (
    <div className="bg-ink text-cream font-sans overflow-x-hidden min-h-screen">
      <Nav />
      <Hero />
      <Services />
      <ContactCTA />
      <Footer />
    </div>
  );
}
