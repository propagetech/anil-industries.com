# anil-industries.com: agent brief

Hand-built static site for **Anil Industries, Bawana, Delhi** (cold rolled and hardened and tempered
steel strip, since 1976). Rebuilt 9 Oct 2026 with the house `site-rebuild` skill.
Business facts, IA, keyword map, art direction and open owner questions: `docs/redesign-decisions.md`.
Research: `docs/research/` (competitors, keywords, design benchmark).

## How the site is made

- **Only `public/` is published.** It is the GitHub Pages artifact (`.github/workflows/deploy.yml`,
  `path: 'public'`) and the Cloudflare Pages **Build output directory: `public`** (no build command,
  framework preset None). `docs/`, `tools/`, `archive/`, `CLAUDE.md` and `README.md` live outside it
  so they are never served: the docs hold owner questions and third-party competitor notes.
- **Pages are generated** by `python3 tools/build.py` from `tools/site_data.py` (facts + tables) and
  the layout in `build.py`. It writes `public/**/index.html`, `public/404.html`, `public/sitemap.xml`
  and `public/_headers`. Output is committed; there is no deploy-time build. Edit the generator and
  re-run it; never hand-edit generated HTML only.
- `public/_headers` is generated: security headers, a CSP that pins the one inline script (the no-js
  class swap) by a hash computed from the same string, long caching for fonts/imgs, and noindex on
  `*.pages.dev`. CSS/JS are not fingerprinted, so they keep the Pages default caching. HSTS is a zone
  setting turned on after go-live verification, never in `_headers`.
- Directory URLs (`slug/index.html`), depth-aware **relative** paths (home `css/...`, inner `../css/...`),
  `404.html` root-absolute. Canonical / OG / sitemap / JSON-LD absolute on `https://www.anil-industries.com/`.
- One `css/main.css`, one `js/main.js` (progressive enhancement only; every feature works with JS off).
  Self-hosted woff2 in `public/fonts/`. No CDN, no cookies, no third-party requests.
- `public/_redirects` (Cloudflare Pages) 301s the old `.html` URLs, including the misspelt
  `coled-rolled-steel-strips.html`, plus `/404.html` and `/favicon.ico`.
- `archive/` holds the old builder site (untouched source). `build.py` copies its 6 pages and assets
  to `public/archive/` as a noindex reference (robots meta + `X-Robots-Tag`, its own looser CSP in
  `_headers`, `home.html` links pointed at `index.html`, CSS font paths fixed, Google Analytics loader
  stripped). Its old contact form and Google Map rely on the dead builder backend and stay broken.
  The copy is verbatim old content, so the dash rule and contrast audit exclude it.
- Images live in `public/imgs/`. The logo/favicon tools take cwd-relative paths, so run them from
  `public/` (`cd public && node ../tools/make-favicons.mjs imgs/logo.webp`).

## Design system: "Mill Certificate"

- Register: industrial, precise. Pages read like a mill test certificate: numbered folio headers
  (`01 PRODUCTS ... AI / HT / 01`), ruled field cells, mono labels, a thickness gauge ruler,
  a magenta inspection stamp (ring text only, never redrawn logo art). Temper band gradient appears on
  the H&T page only; year rail on About only.
- Tokens at the top of `css/main.css`: ink `#17181B`, paper `#F5F5F2`, brand magenta `#AA2F92`
  (the logo colour, unaltered), `--brand-on-night` for dark sections, focus blue `#1F5FD6`
  (focus is never the brand colour).
- Type: Archivo variable (`font-stretch` 106 to 118%) headings, IBM Plex Sans body, IBM Plex Mono for
  every number, grade code and label. Caps only via `text-transform`.
- Anti-template rules (binding): no centred hero, no three-icon-card rows, radius <= 2px, no gradient
  washes, no carousels / counters / scroll fade-ins, no stock photos, every button names its result.
- Concept icons: 12 Noun Project CC BY 3.0 line icons in `--ink-2`, only on dense text grids (the
  8 applications on `/applications/` and both product pages' application lists, and the 4 H&T
  process steps). Listed in `NOUN_ICONS` in `site_data.py`; `python3 tools/noun-icons.py` fetches,
  traces and recolours them, `tools/noun-search.py <term>` finds CC BY candidates. `build.py` adds
  the `title` credit and a per-page credits comment; `docs/icon-credits.md` is the full table.
- Container colour rules on dark sections use `:where()` so components (`.card-uk__name`, `.eyebrow`)
  keep their own colour. Do not raise their specificity.

## Content rules

- Wording decided by the owner: Anil Industries is a **processor and supplier**. Never "manufacturer"
  or "mill". British English. No em or en dashes anywhere (ranges are "0.10 to 4.00 mm").
- Never invent certifications, capacities, export countries, MOQ, lead times or clients. Credentials
  show as dashed "To be confirmed" cells until the owner supplies them.
- Grade and chemistry tables are transcribed from the archive; two column slips were corrected and are
  logged in the decisions doc section 13.
- FAQ visible text and FAQPage schema come from the same strings in `site_data.py`.
- Always say "Anil Industries, Bawana, Delhi" (name clash with Anil Special Steel Industries, Jaipur).

## Validate after any change

```bash
python3 tools/build.py
python3 -m http.server 8123 -d public     # in another shell
(cd public && node ../tools/contrast-audit.mjs)   # must print RESULT: PASS
python3 ../_rebuild-kit/tools/linkcheck.py public
grep -rn "—\|–" --exclude-dir=archive public && echo FAIL || echo OK
# responsive sweep (run from the repo root so it finds tools/node_modules; pass the paths):
node ~/.claude/skills/responsive-qa/scripts/qa-check.mjs / /grades/ /contact/ /hardened-tempered-steel-strips/ /cold-rolled-steel-strips/ /applications/ /quality/ /about/ /faq/ /404.html
```

Do not commit or push without the owner's go-ahead.

## Design skills (house)

Visual polish follows the **`refactoring-ui`** skill (hierarchy, spacing scale, type scale,
HSL/OKLCH ramps, depth, imagery, finishing touches). Load it for any CSS/UI pass.

- Skill: `~/.claude/skills/refactoring-ui/` (also `~/.cursor/skills/refactoring-ui/`)
- Human PDF (do not paste book text here): `/Users/chetan/Downloads/Learning/refactoring-ui_compress 2.pdf`
- Full rebuilds: `site-rebuild` + `../_rebuild-kit/`. ProPage invariants (WCAG AA, real logo,
  photos-first, type-by-register, no em/en dashes) override generic taste.
