import React from "react";
import { Link } from "react-router-dom";
import { ArrowUpRight } from "lucide-react";

export default function ServiceCard({ slug, icon: Icon, title, tag }) {
  return (
    <Link
      to={`/servizi/${slug}`}
      className="group bg-ink p-9 flex flex-col gap-4 transition-all hover:bg-ink-soft hover:shadow-[inset_0_0_0_1px_rgba(0,255,255,0.3),0_0_40px_-16px_rgba(0,102,255,0.5)]"
    >
      <div className="flex items-center justify-between">
        <Icon size={22} className="text-cyan-300" />
        <ArrowUpRight
          size={18}
          className="text-cream/40 group-hover:text-cyan-300 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-all"
        />
      </div>
      <h3 className="font-display text-xl text-cream">{title}</h3>
      <span className="font-mono text-xs text-cream/50">{tag}</span>
    </Link>
  );
}
