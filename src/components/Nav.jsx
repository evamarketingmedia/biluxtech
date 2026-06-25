import React from "react";
import { Link } from "react-router-dom";

export default function Nav() {
  return (
    <header className="fixed top-0 left-0 right-0 z-50 backdrop-blur-md bg-ink/70 border-b border-cyan-400/15">
      <div className="max-w-6xl mx-auto flex items-center justify-between px-7 py-4">
        <Link to="/" className="flex items-center gap-2.5 font-semibold text-cream">
          <span className="w-1.5 h-1.5 rounded-full bg-cyan-300 shadow-[0_0_12px_3px_rgba(0,255,255,0.6)]" />
          BILUX TECH
        </Link>
        <Link
          to="/#contatti"
          className="border border-cyan-300 text-cream text-sm px-4.5 py-2 rounded-md hover:bg-cyan-300 hover:text-ink transition-all"
        >
          Contattaci
        </Link>
      </div>
    </header>
  );
}
