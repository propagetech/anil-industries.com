# Anil Industries: redesign decisions

Single source of truth for the rebuild. Detailed research lives in `docs/research/`:
`competitors.md` (market + buyer), `keywords.md` (search intent + page map + FAQ drafts),
`design-benchmark.md` (nine international benchmarks + art-direction options).

Status: research complete 9 Oct 2026. Build follows the art direction chosen by the owner (section 6).

---

## 1. Business and buyer (facts from the old site only)

- **Business:** Anil Industries, steel strip supplier. Founded **1976** by **Mr. Kewal Krishan Babbar**.
  Raw material sourced from German brands (old About; owner to confirm whether a mill can be named).
- **Products:**
  - **Cold rolled steel strips:** 0.20 to 4.50 mm thick, 12.5 to 450 mm wide. Wide range of surface
    finish, closer thickness tolerances, high tensile and yield strength and hardness.
    Uses: hack saw, power saw and carbon saw blades; clutch, horn diaphragms, seat belts, brake
    assemblies, chain links, circlips, washers; surgical blades, stapler springs, general strip springs.
  - **Hardened and tempered steel strips:** 0.10 to 4.00 mm thick, 5 to 500 mm wide. Hardening and
    tempering in an inert atmosphere to avoid oxidation. Finish: scaleless grey, bright, blue;
    polished bright, blue, bronze, gold. Edges: slit, square, round. Hardness to suit the customer.
    Uses: wood cutting band, hand, cross cut and pit saws; flat springs for clutch plates, shims,
    washers, auto electric contact springs; compressor valve plates and flapper valves, forging
    hammer belts, mould liners, knitting and textile machine components, bearing casings; gang saw
    blades for marble and stone; leather and foam band knives; circular saw blanks, masonry tools,
    agricultural tools, industrial knives, industrial springs.
- **Grades (14):** C45, C50, C55, C65, C75, C80, SK85, SK95, C98, C120, 50CrV4, 75Cr1, 75Cr25, 75Ni8,
  with chemistry and a cross-reference to SAE/AISI, DIN 17222, EN 10132, BS 1449, BS 970, JIS,
  IS 2507, GOST. Transcribed verbatim from the archive; never retype from memory.
- **Process (from the archive diagram `imgs/image-description.webp`):** raw material hot rolled
  slitting, scale breaking and slitting, scale breaking and acid pickling, annealing, (cold rolling),
  skin passing, cold rolled slitting, packing and dispatch. Packing: seal, edge protector, steel hoop,
  metal protector, protective steel sheet, waterproof paper.
- **Buyer:** OEM purchase and engineering staff at saw blade, spring, auto component, compressor,
  textile machinery and tool makers in India; importers and blade/spring makers abroad (UK contact).
  Decision is technical first (grade, size, hardness, flatness, consistency), then commercial.
- **Objections (become FAQ + trust copy):** hardness consistency coil to coil; tolerances (thickness,
  width, flatness, camber); test certificate type and traceability; grade equivalence to the drawing;
  MOQ and trial lots; lead time; coil vs cut length; export packing, Incoterms, documents.
- **The ONE action:** send a quote request (prefilled email). Secondary: call.

## 2. Canonical domain and contact (real, from the archive)

- Domain: `https://www.anil-industries.com/` (from the sitemap).
- Address: L-125, Sector 2, DSIDC Bawana Industrial Area, Delhi 110039, India.
  Geo from the old map embed: 28.7979915, 77.0521289.
- Phone: +91 99999 07396 and +91 98116 37149 (mobile numbers; WhatsApp NOT confirmed, so no `wa.me`).
- Email: info@anil-industries.com (old site wrote "Info@"; lowercased, same mailbox).
- UK contact: Francisca Gomez, +44 7595 870124, 63 Woodford Crescent, Pinner, Middlesex HA5 3UA,
  United Kingdom. Her role (agent, stockist, enquiries) is unconfirmed: present as "UK contact".
- No social links existed (only icon images with no URLs): none published.

## 3. Competitor angle (summary of `research/competitors.md`)

Indian rivals (KND Steel Delhi, Silver Strips Sonipat, Steelcorp Mumbai) lead with superlatives over a
grade list and a WhatsApp button; specs hidden in toggles or PDFs. International mills (voestalpine,
Alleima, Waelzholz) publish real engineering data but are built for tonnage buyers. **Anil sits
between: a 50-year Delhi strip house that answers the engineer's questions on the page.**

Gaps we own honestly: the grade cross-reference as a searchable web table (none of nine benchmarks has
one); application-led navigation; size range stated up front; finish and edge guide; 1976 founding
(oldest in NCR scan) with the founder named; German raw material stated once, plainly; a spec-shaped
RFQ; the UK contact shown prominently; plain copy, no superlatives.

**Name clash:** searches for "Anil Industries" surface "Anil Special Steel Industries" (Jaipur, same
product, ICRA rating suspended). Every page says "Anil Industries, Bawana, Delhi" and the schema carries
the full address, founding date and founder, to disambiguate.

## 4. Keyword -> page map (summary of `research/keywords.md` section 4)

| Page | Path | Primary keyword | Supporting |
| --- | --- | --- | --- |
| Home | `./` | spring steel strip supplier Delhi | H&T strip, cold rolled strip, since 1976, export UK |
| Hardened and tempered | `hardened-tempered-steel-strips/` | hardened and tempered spring steel strip | blue polished, scaleless, quenched and tempered, C75, SK85, 75Ni8 |
| Cold rolled | `cold-rolled-steel-strips/` | cold rolled high carbon steel strip | hacksaw strip, CR spring steel, "not CRCA" |
| Grades | `grades/` | spring steel grades and equivalents | C75 / CK75 / C75S / 1075, SK5 / SK85, 50CrV4 / 6150, EN 10132, DIN 17222 |
| Applications | `applications/` | spring steel strip applications | band saw, gang saw, hacksaw, flapper valve, clutch spring, circlips, band knives |
| Quality and process | `quality/` | how H&T strip is processed | inert atmosphere, slitting, packing |
| About | `about/` | Anil Industries Delhi since 1976 | Bawana, founder, UK contact |
| FAQ | `faq/` | spring steel strip FAQ | the question cluster |
| Contact | `contact/` | request a quote steel strip | Bawana, UK contact |

Titles, H1/H2s, alt text and schema per page: `research/keywords.md` section 4. Headings use current
EN names; legacy names (CK75, CS80, EN42J) live in tables and body. Don't target "CRCA".

## 5. Lead-gen IA

Menu = buyer journey: **Products** (H&T, Cold rolled) / **Grades** / **Applications** / **Quality** /
**About** / **FAQ** / **Request a quote** (button). Every page: one job, one primary CTA
("Request a quote", prefilled with that page's product or grade), top and bottom, plus a call link.

Home spine: value prop (what, where, since when) + spec plate -> intent row (Find a grade / Check my
size / Request a quote) -> two products as spec sheets -> grade matrix teaser -> applications ->
process line -> why Anil (facts only) -> UK/export -> FAQ teaser -> closing RFQ band.

Redirects (Cloudflare `_redirects`, 301): `index.html` -> `/`, `about.html` -> `/about/`,
`coled-rolled-steel-strips.html` -> `/cold-rolled-steel-strips/`, `hardened-tempered-steel.html` ->
`/hardened-tempered-steel-strips/`, `qualities.html` -> `/quality/`, `contact.html` -> `/contact/`.

## 6. Art direction

Options researched (full detail `research/design-benchmark.md` section 3): A "Mill Certificate"
(industrial-precise, light), B "Temper Colours" (dark, technical), C "Since 1976" (editorial heritage).
**Chosen: see section 6a (filled after the owner's pick).**

### 6a. Brief (chosen 9 Oct 2026: Option A "Mill Certificate", full 9 pages)

- **Register:** industrial, precise. A mill test certificate set by a Swiss typographer: ruled,
  numbered, exact. Light paper palette that prints as a spec sheet.
- **Palette (from the logo):** ink `#17181B` / `#3D3F45` / muted `#5E616A`, paper `#F5F5F2`,
  surface `#FFFFFF`, brand magenta `#AA2F92` (logo, unaltered) with `#8A2276` hover and `#F8EAF4`
  tint; dark sections on ink with a lifted on-dark magenta. Focus is its own blue, never the brand.
- **Type:** Archivo variable set wide (`wdth` 112 to 118) for headings, IBM Plex Sans for body,
  IBM Plex Mono for every number, grade code and field label. Self-hosted woff2.
- **Motion:** low; instruments only (filter, size check). Nothing fades in on scroll.
- **Signature element:** the spec sheet as layout (numbered document header, ruled field cells,
  mono labels), a magenta inspection stamp drawn from the logo "A" in its ring, and a thickness
  gauge ruler showing both product ranges. Borrowed once each: the temper band (H&T page, finish
  swatches) and a year rail (About).
- **Owner wording decision:** Anil Industries is a **processor and supplier** ("processes and
  supplies"). Never "manufacturer" or "mill". The process line from the archive diagram is
  presented as our processing route.

### Anti-template rules (binding whatever the option)

No centred hero; no three-icon-card row; no Inter/Poppins/Montserrat/Fraunces/Playfair/Quicksand;
radius <= 2px; no gradient washes (the temper band is the only gradient, and it is a product fact);
no animated counters, carousels, parallax or scroll fade-ins; no stock handshake/hard-hat/globe
photos; every button names its result; specs are selectable text; no typed capitals; logo grey
`#9E9E9E` never carries text.

## 7. Signature components (all work with JS off)

1. Grade equivalence matrix: search + standard toggles, sticky first column, `#grade` anchors.
2. Capability envelope: thickness x width SVG + "check my size" inputs; JS off = table.
3. Thickness gauge ruler (decorative, numbers always printed).
4. Application finder: chips anchor to sections, `:target` highlight.
5. RFQ starter: spec-shaped form that builds a prefilled `mailto:`; JS off = `mailto` form +
   copyable checklist. Stores nothing.
6. Sticky spec summary rail on product pages (pure CSS).
7. Print stylesheet: any product page prints as an A4 spec sheet.
8. mm / inch toggle; JS off = mm with conversion note.

## 8. Content approach

Rewrite for clarity from the archive; keyword-informed; British English; ranges as "0.10 to 4.00 mm"
(no dashes). **Dropped** unverifiable old claims: "fastest growing steel supplier in the world",
"world class manufacturing base", "100% on-time conveyance". Old "Manufacturing Policies / Quality
Objectives" are rewritten plainly as objectives (what we aim for), not results. Typos fixed
("coled", "diaphram", "Temperings").

## 9. Imagery plan (montage pass, 9 Oct 2026)

- **Used (real product material):** `cold-rolled-steel-strips.webp`, `hardened-and-tempered-steel.webp`
  (product photos), `steel-coil-processing-flowchart.webp` (+ `-760` size; an illustrated
  flowchart of the 8-step route supplied on 9 Oct 2026, replacing the archive's line diagram
  `archive/imgs/image-description.webp`; the route is also rebuilt as an HTML process line).
  The original PNG is kept out of the repo.
- **Not used:** every stock photo from the old site (old filenames `shutterstock...`: coils, press
  brake, welding, plates, tube fabrication, businessman/email) plus social and vision/mission clip-art.
  None shows Anil's own works, and the design benchmark rules out generic stock. They remain in
  `archive/imgs/`.
- Gallery engine dormant: no verified photos of the Bawana works. **Needs owner input:** macro photos of
  coils, strip edges, each finish (grey, bright, blue, bronze, gold), the slitting line and packing.
  These would replace the product shots in the heroes and could feed a gallery page.
- OG card `imgs/og-card.jpg` (1200 x 630) is rendered from the real logo + product photo
  (source `drafts/og.html`, gitignored; regenerate with headless Chrome).
- **Home hero background (9 Oct 2026):** `imgs/hero-factory.webp` (+ `-tall` for phones), made by
  `tools/make_hero_bg.py` from `docs/art/hero-slitting-line-source.jpg`, an **AI-generated**
  illustration of a slitting line (ChatGPT). It is not Anil's works: used only as an unlabelled CSS
  background, never captioned or described as the Bawana plant. The product photo was removed from
  the home hero (it repeats in the Products section); the spec plate stays. Owner to confirm slitting
  is done in-house (section 12, item 1); if not, go back to the procedural coil (commit c66d5b6).
  Replace with a real photo of the slitting line when supplied.

## 10. Schema

`Organization` + `LocalBusiness` node `#organization` (name, legalName unconfirmed so omitted, address,
geo, telephone x2, email, foundingDate 1976, founder Person, areaServed IN + GB, contactPoint for the
UK), `WebSite`, `WebPage` on Home; `Product` on each product page (no price, no reviews);
`BreadcrumbList` on inner pages; `FAQPage` on FAQ (answers identical to visible text);
`ContactPage` on Contact.

## 11. URL convention and standards

Directory URLs (`slug/index.html`), depth-aware relative links, root-absolute only in `404.html`;
canonical/OG/sitemap/JSON-LD absolute on `https://www.anil-industries.com/`. WCAG 2.1 AA audited by
`tools/contrast-audit.mjs`. Self-hosted woff2. One `css/main.css`, one `js/main.js`. No cookies, no
trackers, no third-party requests (the map is a link to Google Maps, not an embed).

## 12. Needs owner input (blocks go-live, not the build)

1. ~~Manufacturer, processor or stockist?~~ Answered 9 Oct 2026: **processor and seller**.
   Still to confirm: which process steps are done in-house at Bawana (the archive diagram shows
   slitting, pickling, annealing, skin passing, hardening and tempering in inert atmosphere).
2. Certifications (ISO 9001, IATF 16949) with numbers and scope; shown as "to be confirmed" until then.
3. Test certificates: type (EN 10204 3.1?), contents, traceability.
4. Tolerances, hardness range per grade, which grades come in which product.
5. Delivery condition of cold rolled strip (annealed / skin passed / as rolled).
6. MOQ, lead time, trial lots, coil vs cut lengths, export packing, Incoterms, countries exported to.
7. UK contact's role and permission to name her on the site.
8. German raw material: can the mill(s) be named?
9. Whether either phone number is on WhatsApp.
10. Real photos of the Bawana works, slitting line, coils and finishes (replace stock).
11. Dates for a 50-year timeline; current leadership.
12. Google Business Profile access (to fix the Anil Special Steel name clash in Maps).

## 13. Data discrepancies found in the archive (owner to confirm)

- **Equivalence table column slips.** In the archive's international standards table, `S50C` sits
  in the BS 970 column of the 1050 row (S50C is a JIS G4051 name) and `75Cr1` sits in the BS 1449
  column of its row (75Cr1 is an EN 10132-4 name). The new grades table moves both to the column
  their own naming system belongs to. Everything else is transcribed cell for cell.
- **Same grade table on both product pages.** The archive printed one identical grade list on the
  cold rolled and the H&T pages, so the new site shows it once (Grades page) and does not claim
  which grades come in which product until the owner says.
- **Range formatting.** Chemistry ranges keep the archive's hyphen form (`0.42-0.50`); the en
  dashes in the 75Ni8 row were normalised to the same hyphen form. Values unchanged.
