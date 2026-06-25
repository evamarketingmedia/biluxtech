import React from "react";
import { Link, useParams, Navigate } from "react-router-dom";
import { ArrowLeft, Mail } from "lucide-react";
import Nav from "../components/Nav.jsx";
import Footer from "../components/Footer.jsx";
import { SERVICES, CONTACT_EMAIL } from "../data/services.js";

export default function ServicePage() {
  const { slug } = useParams();
  const service = SERVICES.find((s) => s.slug === slug);

  if (!service) return <Navigate to="/" replace />;

  return (
    <div className="bg-ink text-cream min-h-screen">
      <Nav />
      <div className="max-w-2xl mx-auto px-7 pt-32 pb-24">
        <Link
          to="/"
          className="inline-flex items-center gap-2 text-sm text-cream/60 hover:text-cyan-300 mb-10 transition-colors"
        >
          <ArrowLeft size={15} /> Torna alla home
        </Link>

        <span className="block font-mono uppercase text-xs text-cyan-300 mb-4">{service.eyebrow}</span>
        <h1 className="font-display text-4xl sm:text-5xl mb-6 leading-tight">{service.title}</h1>
        <p className="text-cream/70 text-lg leading-relaxed mb-10">{service.lead}</p>

        <ul className="grid sm:grid-cols-2 gap-3 mb-12">
          {service.points.map((p) => (
            <li key={p} className="border border-cyan-400/15 rounded-md px-4 py-3 text-sm text-cream/80">
              {p}
            </li>
          ))}
        </ul>

        <a
          href={`mailto:${CONTACT_EMAIL}`}
          className="inline-flex items-center gap-2 bg-gradient-to-br from-electric to-[#0044CC] text-white font-semibold text-sm px-7 py-4 rounded-md shadow-[0_0_0_1px_rgba(0,255,255,0.25),0_8px_24px_-8px_rgba(0,102,255,0.7)] hover:-translate-y-0.5 transition-all"
        >
          <Mail size={16} /> {service.cta}
        </a>
      </div>
      <Footer />
    </div>
  );
}
