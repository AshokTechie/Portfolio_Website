"use client";
import { PROFILE } from "@/lib/data";
import { scrollToTarget } from "@/lib/scroll";
import { asset } from "@/lib/asset";
import Button from "@/components/ui/Button";

export default function Hero() {
  const go = (id: string) => (e: React.MouseEvent) => {
    e.preventDefault();
    scrollToTarget(id);
    history.replaceState(null, "", `#${id}`);
  };

  return (
    <section id="hero" className="hero" aria-label="Introduction">
      <div className="hero-ghost" aria-hidden="true">{PROFILE.firstName.toUpperCase()}</div>

      <div className="hero-grid">
        <div className="hero-copy">
          <p className="mono hero-eyebrow rv">
            {PROFILE.role} <span aria-hidden="true">·</span> {PROFILE.company}
          </p>
          <h1 className="hero-h1">
            <span className="rv-mask" style={{ ["--i" as string]: 1 }}><span>Software</span></span>
            <span className="rv-mask" style={{ ["--i" as string]: 2 }}><span><span className="accent">Engineer.</span></span></span>
          </h1>
          <div className="hero-cta rv" style={{ ["--i" as string]: 3 }}>
            <Button href="#work" onClick={go("work")}>Explore work</Button>
            <Button href="#contact" onClick={go("contact")} variant="secondary">Let&apos;s talk</Button>
            <Button href={PROFILE.resume} variant="secondary" download="Ashok-H-Resume.pdf">Résumé ↓</Button>
          </div>
        </div>

        <div className="hero-stage">
          <img
            src={asset("/hero/hero-portrait.webp")}
            alt={`3D Character Portrait of ${PROFILE.name}`}
            className="hero-video"
            width={768}
            height={960}
            loading="eager"
            decoding="async"
          />
        </div>

        <div className="hero-meta rv" style={{ ["--i" as string]: 4 }}>
          <p className="mono">Since {PROFILE.since}</p>
          <p className="mono">{PROFILE.location}</p>
        </div>
      </div>

      <style>{`
        .hero { position: relative; overflow: clip; padding-top: calc(var(--nav-h) + 8px); min-height: 100svh; }
        .hero-ghost { position: absolute; left: 50%; top: calc(var(--nav-h) + 2svh); transform: translateX(-50%); z-index: 0;
          font-weight: 800; letter-spacing: -0.05em; line-height: .8; font-size: clamp(110px, 24vw, 380px); color: #e4e1da;
          user-select: none; pointer-events: none; white-space: nowrap; }
        .hero-grid { position: relative; width: 100%; max-width: calc(var(--max) + var(--gutter) * 2); margin-inline: auto;
          padding-inline: var(--gutter); display: grid; grid-template-columns: 1fr; justify-items: center; }
        .hero-stage { position: relative; order: 1; width: min(100%, calc(62svh * .8)); }
        .hero-video { width: 100%; height: auto; aspect-ratio: 768 / 960; object-fit: cover; mix-blend-mode: darken; background: transparent; -webkit-mask-image: linear-gradient(to right, transparent, #000 8%, #000 92%, transparent); mask-image: linear-gradient(to right, transparent, #000 8%, #000 92%, transparent); }
        .hero-copy { order: 2; position: relative; z-index: 2; width: 100%; margin-top: 8px; padding-bottom: 56px; text-align: left; }
        .hero-eyebrow { font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--mute); margin-bottom: 16px; }
        .hero-h1 { font-weight: 700; letter-spacing: -0.045em; line-height: 1; font-size: clamp(44px, 12vw, 64px); }
        .hero-h1 .accent { font-size: 1.05em; }
        .hero-cta { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 28px; }
        .hero-meta { display: none; }
        @media (min-width: 900px) {
          .hero { display: flex; align-items: flex-end; }
          .hero-grid { grid-template-columns: minmax(0,1fr) auto minmax(0,1fr); align-items: end; column-gap: clamp(8px, 2vw, 32px); }
          .hero-stage { order: 0; width: auto; height: min(96svh, 1040px); max-height: calc(100svh - var(--nav-h)); aspect-ratio: 768 / 960; }
          .hero-video { height: 100%; width: auto; }
          .hero-copy { order: 0; margin-top: 0; padding-bottom: clamp(40px, 9svh, 110px); }
          .hero-h1 { font-size: clamp(44px, 4.6vw, 84px); }
          .hero-stage { margin-inline: calc(-1 * clamp(0px, 8vw, 140px)); }
          .hero-meta { position: relative; z-index: 2; }
          .hero-meta { display: grid; gap: 6px; justify-self: end; text-align: right; padding-bottom: clamp(40px, 9svh, 110px);
            font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--mute); }
        }
      `}</style>
    </section>
  );
}
