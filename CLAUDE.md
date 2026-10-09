# anil-industries.com: agent brief

Hand-built static site for **Anil Industries, Bawana, Delhi** (cold rolled and hardened and tempered
steel strip, since 1976). Rebuilt 9 Oct 2026 with the house `site-rebuild` skill.
Business facts, IA, keyword map, art direction and open owner questions: `docs/redesign-decisions.md`.
Research: `docs/research/` (competitors, keywords, design benchmark).

## How the site is made

- **Pages are generated** by `python3 tools/build.py` from `tools/site_data.py` (facts + tables) and
  the layout in `build.py`. Output is plain static HTML that is committed; there is no deploy-time build.
  Edit the generator, re-run it, never hand-edit generated HTML only.
- Directory URLs (`slug/index.html`), depth-aware **relative** paths (home `css/...`, inner `../css/...`),
  `404.html` root-absolute. Canonical / OG / sitemap / JSON-LD absolute on `https://www.anil-industries.com/`.
- One `css/main.css`, one `js/main.js` (progressive enhancement only; every feature works with JS off).
  Self-hosted woff2 in `fonts/`. No CDN, no cookies, no third-party requests.
- `_redirects` (Cloudflare Pages) 301s the old `.html` URLs, including the misspelt `coled-rolled-steel-strips.html`.
- `archive/` holds the old builder site (disallowed in robots).

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
python3 -m http.server 8123          # in another shell
node tools/contrast-audit.mjs        # must print RESULT: PASS
python3 ../_rebuild-kit/tools/linkcheck.py .
grep -rn "—\|–" *.html */index.html css js && echo FAIL || echo OK
```

Do not commit or push without the owner's go-ahead.

## Design skills (house)

Visual polish follows the **`refactoring-ui`** skill (hierarchy, spacing scale, type scale,
HSL/OKLCH ramps, depth, imagery, finishing touches). Load it for any CSS/UI pass.

- Skill: `~/.claude/skills/refactoring-ui/` (also `~/.cursor/skills/refactoring-ui/`)
- Human PDF (do not paste book text here): `/Users/chetan/Downloads/Learning/refactoring-ui_compress 2.pdf`
- Full rebuilds: `site-rebuild` + `../_rebuild-kit/`. ProPage invariants (WCAG AA, real logo,
  photos-first, type-by-register, no em/en dashes) override generic taste.
