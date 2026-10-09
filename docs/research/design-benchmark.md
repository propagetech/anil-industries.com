# Anil Industries: design benchmark and art direction

Research date: 9 Oct 2026. Purpose: give the rebuild an international-grade face that a UK
or German strip buyer would find as credible as a European mill, without looking like a
template. Feeds `docs/redesign-decisions.md` (art-direction brief) and the build.

Method: live visits with a headless browser at 1440 x 900 (computed styles read from the
DOM, viewport screenshots), plus page-text fetches for IA and product pages. Fonts and
colours below are measured, not guessed. Cookie banners were left untouched.

---

## 0. What we are designing for

**The buyer.** A purchase or quality engineer at an Indian OEM (auto clutch, saw, compressor
valve, textile machinery) or an export buyer working through the UK contact. They arrive
with a grade, a thickness, a width and a hardness in mind. Their job on the site: "Can this
mill make my spec, and how fast can I get a quote?" Everything else is supporting evidence.

**The product content we already own (from the archived site).**

- Cold rolled strip: 0.20 to 4.50 mm thick, 12.5 to 450 mm wide.
- Hardened and tempered strip: 0.10 to 4.00 mm thick, 5 to 500 mm wide; finishes
  scaleless grey, bright, blue, polished bright, blue, bronze and gold; slit, square or
  round edges; hardness to customer range.
- A 15-grade chemistry table (C45 to C120, SK85, SK95, 50CrV4, 75Cr1, 75Cr25, 75Ni8) with
  C, Mn, Si, S, P, Cr, V, Ni, Mo.
- An **international standards cross-reference** across SAE/AISI, DIN 17222, EN 10132,
  BS 1449, BS 970, JIS, IS 2507 and GOST. This is the single most valuable asset on the
  old site and none of the nine benchmark sites below publishes anything like it in HTML.
- Applications by industry (wood saw, stone gang saw, auto clutch and shims, compressor
  flapper valves, textile and knitting parts, leather and foam band knives, surgical
  blades, hack saws).
- Contacts: Bawana Industrial Area, Delhi 110039, two phones, info@ mailbox; UK contact
  in Pinner, Middlesex.

**The brand (measured from `imgs/logo.webp`).**

| Role | Hex | HSL | Notes |
| --- | --- | --- | --- |
| Logo magenta | `#AA2F92` | 312, 57%, 43% | Passes AA as text on white (5.95:1) and white on it (5.95:1). |
| Logo ring grey | `#9E9E9E` | 0, 0%, 62% | 2.45:1 on paper. Decorative only, never text or a control border. |

A lucky, ownable fact: **magenta/purple is a real temper colour.** Bright carbon steel
heated in air passes through straw, gold, bronze, purple and blue oxide tints as the
temperature rises (roughly 200 to 320 C). Anil sells blue, bronze and gold finishes. So the
logo colour is not an arbitrary brand hue; it sits inside the physics of the product.
Option B builds on this, and the recommendation borrows it.

The old site set Playfair Display + Quicksand (a site-builder default). Both go.

---

## 1. Benchmark: nine international sites

### 1.1 voestalpine Precision Strip (Austria) `voestalpine.com/precision-strip`

- **Hero:** a short typographic claim ("You have the requirements...") beside a coil photo,
  immediately followed by an even tile grid grouped by family (Steel Rules, Saw Steel...).
- **IA:** four top items (Value & Innovation, Products & Brands, Communication, Company),
  mega-menu two levels deep, organised by **sub-brand** (Bohlerstrip, Uddeholmstrip,
  Martin Miller, Wisconstrip) and then by application.
- **Specs:** none on the hub. Datasheets live as PDFs under "Brochures & Downloads".
- **RFQ:** a named Chief Sales Officer card with phone and email; no form. Side tabs
  "competence nearby" and "Steel App".
- **Type / colour / motion:** proprietary corporate sans in Light (300) at 22 to 36 px,
  near-black body, cyan-blue `#0082B4` accent, grey tiles. Almost no motion.
- **Borrow:** the **named human sales contact** with direct line. For a 50-year family firm
  this is a strength: a named person beats a generic form.

### 1.2 Alleima, formerly Sandvik Materials (Sweden) `alleima.com/en/products/strip-steel`

- **Hero:** dark, full-width coil-texture photo with a very large left-aligned H1
  ("Strip steel", 76 px, tracking -2 px, regular weight). Breadcrumbs directly under it.
- **IA:** Products / Industries / Technical center / Careers / Contact in a full-screen
  menu; products split by application (compressor valve, knife, medical, razor blade,
  spring, doctor blade, shock absorber).
- **Specs:** a separate "List of alloys" plus small cards for alloy surcharges,
  tolerances, shape, edges, surfaces. Datasheets in a Technical center.
- **RFQ:** no quote form; contact and sales-office pages.
- **Type / colour / motion:** proprietary grotesk ("Alleima Neurial"), one weight doing
  all the work, hierarchy by size alone. Deep navy `#0F232E` + oxblood `#872823` + light
  greys `#F1F1F1`. Restrained.
- **Borrow:** **application-first product families** (compressor valve, saw, spring) and the
  confidence of one large regular-weight headline instead of bold everything.

### 1.3 Waelzholz / C.D. Walzholz (Germany) `waelzholz.com`

- **Hero:** a video playing through giant knockout letters ("CHANGE") on white.
- **IA:** Steel Materials / Industries & Applications / Sustainability / Company /
  Career / News; utility row Downloads / Contact / five languages.
- **Specs:** category tiles with prose. No grade table on the hub. A **coil calculator**
  (weight, outer diameter or strip length) and an **ISO / US unit toggle**.
- **RFQ:** contact partners by country, e-mail form, **sample request** for some lines.
- **Type / colour / motion:** Exo 2 in weights 200 to 300 with +0.4 px tracking, navy
  `#003A69`, white, `#F5F5F5`. Hero motion is the only motion.
- **Borrow:** the **coil calculator** (a genuine engineering utility that brings buyers
  back) and the **mm / inch toggle** for export buyers.

### 1.4 SSAB (Sweden) `ssab.com/en`

- **Hero:** furnace photo, two-line light-weight headline, then the line "What are you
  looking for?" and **four intent cards overlapping the photo edge** (Browse all our steel,
  Contact us, MySSAB, Downloads), each with a one-line explanation.
- **IA:** Products and Services / Fossil-free steel / Technical support / Contact, with a
  utility row (Company, Investors, Careers, Newsroom, International, Search).
- **Specs:** product groups ("Strenx 700 product group") each with "Product offer and
  datasheets"; a search-and-filter product browser.
- **RFQ:** Contact plus the MySSAB portal for existing customers.
- **Type / colour / motion:** SSAB Sans Pro (display 72 px regular) + Roboto body; navy
  `#0F2445`, pale steel `#DBE0E8`, warm paper `#F5F4F2`.
- **Borrow:** the **intent router directly under the H1**. It replaces the generic "three
  feature cards" with "tell us your task". For Anil: Find a grade / Check my size /
  Request a quote / Download spec sheet.

### 1.5 Outokumpu (Finland) `outokumpu.com/en/products/steel-finder`

- **Hero:** none on the tool page: breadcrumb, H1 "Steel Finder", then straight into a
  search field ("Search by grade names, standards, product categories, grade families").
- **IA:** Products / Expertise / Industries / Surcharges, plus a blue utility bar
  (Certificates, Steel Finder, Outokumpu Connect).
- **Specs:** a **plain HTML results table** (Product name, EN number, Thickness, Width,
  Microstructure), 90 rows, filters for thickness, width and standard. A second tab holds
  corrosion tables.
- **RFQ:** a **vertical "CONTACT" tab pinned to the right edge** on every page, opening a
  form with "Reason for contact".
- **Type / colour / motion:** Tee Franklin (300 body, 500 display), navy `#003057` text,
  sky blue `#009EE8` bars and table headers, `#F2F2F0` panels.
- **Borrow:** **the table is the tool.** The finder is a real `<table>` with filters on
  top, so it works as a document even without the filters. This is exactly the JS-off
  pattern we need.

### 1.6 Aperam (Luxembourg) `aperam.com`

- **Hero:** four-slide carousel on a purple-to-orange gradient with a cut-out coil render,
  a circular badge and stacked italic callouts.
- **IA:** Stainless / Alloys / Electrical / Steel / About / Sustainability / Investors /
  Megatrends; utility row with **Get quote** and a **live nickel surcharge ticker**.
- **Specs:** "Select Your Product" dropdown, then product cards.
- **Type / colour / motion:** Nunito 700 headings (rounded, friendly), purple `#5F2869`,
  orange `#EB5E0B`, violet `#543286`; about twenty icon/font files loaded.
- **Borrow:** **Get quote as a permanent utility-bar item**. **Avoid** everything else: it
  is the cautionary example, and it is purple, so it is the closest look-alike risk for
  Anil's magenta. Carousel, gradient wash, badge stickers and a rounded display face read
  as marketing, not metallurgy.

### 1.7 Hadrian (USA, precision aerospace machining) `hadrian.co`

- **Hero:** navy field, two-line 72 px headline (Sohne, tracking -2.16 px) left, a short
  claim right, then a **wide toolpath line drawing in a frame with chamfered lower corners**
  (a machined-part silhouette) carrying two full-width outline buttons in mono caps.
- **IA:** single MENU button; a header **strip of live factory clocks in mono** (CA, AZ,
  AL, DC) set in a ruled cell row.
- **Type / colour / motion:** Sohne + Sohne Breit + Sohne Mono; navy `#002548`, sky
  `#70B8FD`, one gold line accent. Line-drawing motion, nothing bouncy.
- **Borrow:** two devices. (1) **Mono data in ruled cells** as decoration that is also
  information. (2) **The chamfer**: a 45 degree cut corner on frames and buttons reads as
  machined metal, not as a "rounded card".

### 1.8 Machina Labs (USA, robotic sheet forming) `machinalabs.ai`

- **Hero:** full-bleed factory video, dark scrim, single line in **Roboto Mono 500 uppercase
  at 72 px**: "INTELLIGENT. AGILE. REAL METAL."
- **IA:** slash-prefixed nav (/CAPABILITIES /APPLICATIONS /RESOURCES /CAREERS) and an
  outlined "CONTACT US" in amber.
- **Type / colour / motion:** Roboto body, Roboto Mono display; `#191919`, `#FCFCFC`,
  warm grey `#F3F0EE`, amber accent from the logo.
- **Borrow:** the courage of **one typographic decision carried everywhere** (mono as the
  voice). Caution: all-mono display is now a recognisable "deep-tech" trope; we use mono
  for data only.

### 1.9 IEM (USA, power equipment; 2025 w3 Award, manufacturing websites category) `iemfg.com`

- **Hero:** a **diptych**: a wide site photo (bridge and cranes at dusk) left, a macro of
  copper bus bars right, one headline spanning both.
- **IA:** Company / Products & Services / Industry Solutions / Resources, with Careers and
  Contact quiet on the right; the header is built from **hairline-ruled cells** in the
  brand red, logo cell and search cell boxed.
- **Type / colour / motion:** Basis Grotesque 700 for display, Basis Off-White for body;
  white with one red `#D42E12`. Photography carries all the colour.
- **Borrow:** the **scale-plus-macro diptych** (the plant, and the material up close) and the
  **ruled-cell header** that makes the grid itself the decoration.

Also checked: **Uddeholm** (`uddeholm.com`): five-slide carousel, products by use (hot
work, cold work...), grade pages reached from category lists, "Pocket book" and apps as
reference tools. Useful only as confirmation that even the best tool-steel brand hides
grade comparison in PDFs and apps.

### 1.10 What the benchmark tells us

1. **Nobody publishes the cross-reference.** Every mill keeps grade equivalence in PDFs,
   apps or portals. An HTML, searchable, printable SAE/DIN/EN/BS/JIS/IS/GOST matrix is a
   real differentiator for Anil and it already has the data.
2. **The good ones route by task, not by section.** SSAB's intent cards and Outokumpu's
   search-first finder put the buyer's question before the company story.
3. **Restraint reads premium.** Alleima, SSAB, Hadrian and IEM all use one family, a single
   accent and large regular-weight headlines. Aperam (busiest) looks least credible.
4. **Engineering utilities create return visits**: Waelzholz's coil calculator, the
   voestalpine Steel App, Outokumpu's finder.
5. **Human contact still wins** in strip steel: named sales contacts, country contacts,
   sample requests. None of them makes the buyer start from a blank form.
6. **Typical gaps**: heavy JS menus, carousels, JS-obfuscated emails, consent walls, and
   specs locked in PDFs. A fast static site with real HTML tables beats them on speed,
   accessibility and SEO for long-tail grade queries ("SK85 equivalent", "C75S strip").

---

## 2. What makes a site read as a generic template (and our "do not do" list)

**The tells.** Centred hero over a stock photo or mesh gradient, H1 + subline + two pill
buttons. Three icon cards ("Quality / Experience / Delivery") with line icons in tinted
circles. Inter or Poppins everywhere, everything bold. Rounded 16 to 24 px pastel cards with
large soft shadows. Counters that animate ("50+ years, 1000+ clients"). A testimonial
carousel. A logo wall in greyscale. Fade-up on every section. Purple-to-blue gradients.
Accordion FAQ at the bottom. Stock handshake and hard-hat photos. A "Get Started" CTA that
means nothing in B2B.

**Do not do (rules for this build):**

1. No centred hero. Headline left-aligned on the grid, data or photo on the right.
2. No three-icon-card row anywhere. If we have three things, they are a table, a list with
   numbers, or a ruled spec block.
3. No Inter, Poppins, Montserrat, Fraunces, Playfair or Quicksand.
4. No border-radius above 2 px on structural elements. Corners are square or chamfered.
5. No gradient washes or mesh backgrounds. The only gradient allowed is the thin temper
   band (Section 3), which is a literal colour record of the product, not decoration.
6. No animated counters, no carousels, no auto-playing sliders, no parallax.
7. No fade-in-on-scroll for content. Motion is reserved for instruments (gauge, filters).
8. No stock photos of handshakes, hard hats, globes or generic factories. Use Anil's own
   coils, slitting line, strip edges, finishes and parts; macro shots first.
9. No vague CTA. Every button names its result: "Request a quote", "Download C75S sheet",
   "Check my size".
10. No icon used where a number would do. "0.10 to 4.00 mm" beats a ruler icon.
11. No spec data as images or PDFs only. Every spec is selectable HTML text.
12. No floating chat bubbles, no cookie wall (we set no non-essential cookies).
13. No typed capitals. Caps only via `text-transform` + `letter-spacing`.
14. No em or en dashes in copy. Ranges are "0.10 to 4.00 mm", never with a dash.
15. Logo grey `#9E9E9E` never carries text or a control border.

---

## 3. Three art-direction options

All three: WCAG 2.1 AA, square or chamfered geometry, real photography of Anil's material,
one CSS + one small vanilla JS, every interaction works with JS off, all motion behind
`@media (prefers-reduced-motion: no-preference)`.

Contrast ratios below were computed with the WCAG relative-luminance formula.

### Option A: "Mill Certificate"

- **Register:** Industrial, precise (the "industrial / bold" register, kept restrained).
- **Mood:** a mill test certificate set by a Swiss typographer: ruled, numbered, exact.
- **Palette:**

  | Token | Hex | Use | Contrast |
  | --- | --- | --- | --- |
  | `--ink` | `#17181B` | text, rules on headers | 16.3:1 on paper |
  | `--ink-2` | `#3D3F45` | secondary text | 9.6:1 |
  | `--muted` | `#5E616A` | captions, field labels | 5.7:1 |
  | `--line-strong` | `#8A8D95` | input borders, table header rule | 3.0:1 (non-text) |
  | `--line` | `#C9CBD0` | hairlines (decorative) | n/a |
  | `--paper` | `#F5F5F2` | page | n/a |
  | `--surface` | `#FFFFFF` | sheets, tables | n/a |
  | `--brand` | `#AA2F92` | links, primary button, stamp | 5.4:1 on paper, white on it 5.95:1 |
  | `--brand-700` | `#8A2276` | hover, link visited, small text on tint | 7.5:1 |
  | `--brand-50` | `#F8EAF4` | selected row, highlight | ink on it 15.3:1 |
  | `--ring` | `#9E9E9E` | logo ring motif only | decorative |

- **Type:** **Archivo** (variable, `wdth` 62 to 125) for headings at width 112 to 118 and
  weight 650 to 800, so headings feel broad and rolled; **IBM Plex Sans** for body (an
  engineering-born humanist grotesk, excellent at 16 px); **IBM Plex Mono** for every
  number, grade code, tolerance and field label. All three verified on Fontsource
  (`archivo`, `ibm-plex-sans`, `ibm-plex-mono`; Archivo's width axis is served as
  `archivo:vf/latin-wdth-normal.woff2`).
- **Layout system:** 12-column grid, 72 rem max, 24 px gutter, visible as **hairline column
  rules** in the header and spec blocks (the IEM idea). Rhythm on an 8 px base: 4, 8, 12,
  16, 24, 32, 48, 64, 96. Type scale 14 / 16 / 18 / 22 / 28 / 36 / 48 / 64 (clamp from
  phone to desktop). Body measure 62ch.
- **Signature element:** **the spec sheet as layout.** Product pages are composed like a
  mill certificate: a numbered document header (`AI / CR / 01`), ruled field cells
  ("Thickness", "Width", "Edge", "Finish", "Hardness") with labels in mono caps and values
  large, a chemistry table, and a magenta **inspection stamp** (the logo "A" in a ring,
  drawn as an inline SVG) marking the IS/EN conformity block. Plus a **thickness gauge
  ruler** (a vernier-style scale from 0.10 to 4.50 mm) that is the visual of the capability
  range.
- **Motion:** low. The gauge needle eases to the typed thickness; filter rows cross-fade in
  120 ms. Nothing else moves.
- **Home hero:** paper background, left 7 columns: eyebrow in mono caps "Cold rolled and
  hardened and tempered steel strip, Delhi, since 1976"; H1 "Spring steel strip, rolled
  to your tolerance." Right 5 columns: a tall macro photo of a slit strip edge with a
  ruled **spec plate** overlapping its bottom edge (Thickness 0.10 to 4.50 mm / Width 5 to
  500 mm / 15 grades / 8 standards) in mono. Beneath, spanning 12 columns, a **four-cell
  intent row** in ruled cells (Find a grade / Check my size / Request a quote / Download
  spec sheets), the SSAB pattern rendered as a certificate row, not cards.

### Option B: "Temper Colours"

- **Register:** Modern, technical (dark).
- **Mood:** quenched steel under shop lights; colour arrives only as heat tint.
- **Palette:**

  | Token | Hex | Use | Contrast |
  | --- | --- | --- | --- |
  | `--bg` | `#0E1013` | page (quench black) | n/a |
  | `--surface` | `#171A1F` | panels | n/a |
  | `--text` | `#ECEDEF` | body | 16.3:1 on bg |
  | `--muted` | `#A3A7B0` | secondary | 7.9:1 on bg, 7.2:1 on surface |
  | `--straw` | `#D8B66A` | temper 1 (about 220 C) | 9.8:1 |
  | `--bronze` | `#B9773A` | temper 2 (about 250 C) | 5.2:1 |
  | `--magenta` | `#D45BBA` | temper 3, the brand lifted for dark | 5.5:1 |
  | `--blue` | `#7D9BE6` | temper 4 (about 300 C) | 7.0:1 |
  | `--brand` | `#AA2F92` | filled buttons with white text | 5.95:1 (fails 3.2:1 as text on bg, so never text) |

- **Type:** **Chivo** (variable 100 to 900; headings at 800, tight tracking) + **Public
  Sans** body + **Chivo Mono** for data. All verified on Fontsource.
- **Layout system:** asymmetric 12-column; big dark photographic bands alternate with
  dense data bands; 8 px rhythm; type scale tops out at 80 px.
- **Signature element:** **the temper band**: a 6 px strip whose gradient is the actual
  oxide sequence straw, gold, bronze, magenta, purple, blue. It sits under the header, as
  the progress rule on the hardness scale, and as the swatch row for the finish options
  (bright, blue, bronze, gold), so the brand colour is explained by the product.
- **Motion:** medium. The temper band sweeps once on load (600 ms); hero photo has a slow
  sheen pass. Both gated by reduced motion.
- **Home hero:** full-bleed dark macro of a blued coil, H1 bottom-left in Chivo 800 "Steel
  strip, heat-treated to the colour.", the temper band running across the bottom of the
  hero with finish names under each segment in mono.
- **Risk:** dark B2B sites read as tech start-ups, print badly, and render spec tables
  harder to scan on phones in daylight; magenta must be lifted to `#D45BBA` for text,
  which drifts from the logo.

### Option C: "Since 1976"

- **Register:** Editorial, heritage authority.
- **Mood:** a trade almanac or the Financial Times' metals page: printed, sober, dated.
- **Palette:**

  | Token | Hex | Use | Contrast |
  | --- | --- | --- | --- |
  | `--paper` | `#F3EFE6` | newsprint page | n/a |
  | `--ink` | `#1C1A17` | text | 15.1:1 |
  | `--oxide` | `#6B6259` | secondary | 5.2:1 |
  | `--brand-deep` | `#8E2479` | links, headings accents | 6.8:1; white on it 7.8:1 |
  | `--brand` | `#AA2F92` | stamp, large display only | 5.2:1 |
  | `--brand-tint` | `#EFD9E8` | pull-quote panel | brand-deep on it 5.9:1 |
  | `--rule` | `#D8D1C4` | column rules | decorative |
  | `--night` | `#1C1A17` / `#E7A9D6` | footer, magenta on dark 9.1:1 | |

- **Type:** **Newsreader** (variable, optical size; display at 600) + **Schibsted Grotesk**
  body (a newspaper-born grotesk) + **Spline Sans Mono** for data. All on Fontsource.
- **Layout system:** newspaper columns: 6-column text grid with marginalia (dates, grade
  codes) in the left margin; drop folios ("No. 01 Cold rolled") on section heads.
- **Signature element:** **the 50-year timeline as a ledger**: a left-margin year rail
  (1976, then milestones) that follows the reader, and dated marginal notes beside specs.
- **Motion:** minimal.
- **Home hero:** masthead-style: "Anil Industries, Delhi. Steel strip since 1976." set
  large in Newsreader, dateline in mono, a wide plant photograph below the fold line like a
  front-page picture.
- **Risk:** reads "heritage" more than "precision", and serif-led layouts are less natural
  for dense chemistry tables. Good for the About page, weak for the buyer's core task.

---

## 4. Recommendation: Option A "Mill Certificate", with B's temper band as one accent

**Why A.**

1. **It serves the buyer's actual job.** The site's primary content is spec data. A
   certificate layout makes the data the hero instead of decorating around it, which is
   what international buyers recognise from their own mill certs and drawings.
2. **It is ownable.** None of the nine benchmarks uses the document itself as the visual
   language; most use photo tiles. Hairline grids, mono field labels and a magenta
   inspection stamp are distinctive without gimmicks.
3. **It keeps the logo honest.** Magenta `#AA2F92` passes AA on white and paper as-is, so
   the brand colour is used at full strength, not lightened (B) or darkened (C).
4. **Light, printable and fast.** Buyers print spec pages and forward them; a paper
   palette prints cleanly and the print stylesheet is almost free.
5. **Distinct from Aperam**, the purple competitor look: no gradients, no rounded faces.

**Borrow from B, once:** use the **temper band** only on the Hardened and Tempered page as
the finish swatch row (bright, blue, bronze, gold) and as a 4 px rule under the H&T page
header, with the short explanation that magenta sits in the temper sequence. One literal,
product-true use; never as a site-wide gradient.

**Borrow from C, once:** the year rail on the About page only.

**Art-direction brief line (for `docs/redesign-decisions.md`):**
register Industrial-precise / palette from logo `#AA2F92` + graphite neutrals on mill paper
/ Archivo (wdth 115) + IBM Plex Sans + IBM Plex Mono / motion low, instruments only /
signature: the mill-certificate spec sheet, gauge ruler and inspection stamp.

**Starter tokens (Option A):**

```css
:root {
  --ink: #17181B; --ink-2: #3D3F45; --muted: #5E616A;
  --line-strong: #8A8D95; --line: #C9CBD0;
  --paper: #F5F5F2; --surface: #FFFFFF;
  --brand: #AA2F92; --brand-700: #8A2276; --brand-50: #F8EAF4;
  --ring: #9E9E9E; /* decorative only */
  --focus: #1F5FD6; /* focus is its own colour, never the brand */
  --temper: linear-gradient(90deg, #E8D9A8, #D8B66A, #B9773A, #AA2F92, #6B3FA0, #2C4FA3);

  --font-head: "Archivo", "Arial Narrow", Arial, sans-serif;
  --font-body: "IBM Plex Sans", "Segoe UI", Arial, sans-serif;
  --font-data: "IBM Plex Mono", ui-monospace, Menlo, monospace;

  --s-1: 4px; --s-2: 8px; --s-3: 12px; --s-4: 16px; --s-5: 24px;
  --s-6: 32px; --s-7: 48px; --s-8: 64px; --s-9: 96px;
  --radius: 0; --chamfer: 10px;
}
h1, h2, h3 { font-family: var(--font-head); font-variation-settings: "wdth" 115; }
.data, td, .spec-value { font-family: var(--font-data); font-variant-numeric: tabular-nums; }
```

Check `--focus` and every pair again with `tools/contrast-audit.mjs` once the CSS exists.
Preload only Archivo (wdth) and IBM Plex Sans 400; load Plex Mono 400/500 normally.

---

## 5. Signature UX components

Each one is real HTML first; the JS is an enhancement that never hides content.

### 5.1 Grade equivalence matrix (the centrepiece)

- **What:** one table, rows = grades (1045 / C45 ... 75Ni8), columns = SAE/AISI, DIN 17222,
  EN 10132, BS 1449, BS 970, JIS, IS 2507, GOST, plus "Available as CR / H&T". A search box
  ("Type any grade: SK5, C75S, 50HGFA") filters rows and highlights the matching cell;
  column toggles let a buyer show just "their" two standards. Each row links to
  `/grades/c75s/` (a static page per grade: chemistry, equivalents, typical applications,
  available sizes), which is also the long-tail SEO play.
- **Sticky first column and header** so the matrix scrolls sideways on phones.
- **JS off:** the full table renders, every grade has an `id` so `#sk85` links work, and a
  plain A to Z grade index above it. Ctrl+F does the searching.
- **A11y:** real `<table>` with `<caption>`, `scope="col"`/`scope="row"`, the filter
  result count announced via `aria-live="polite"`.

### 5.2 Capability envelope (thickness x width)

- **What:** an SVG chart with thickness on one axis (0.10 to 4.50 mm, log scale so thin
  gauges are readable) and width on the other (5 to 500 mm), two shaded regions for CR and
  H&T. Two number inputs ("My strip: 0.35 mm x 32 mm") drop a crosshair point and answer
  in words: "Inside our hardened and tempered range" or "Outside: talk to us".
- **JS off:** the SVG is static with labelled corners, and directly under it a two-row
  table (Product / Thickness range / Width range / Edges / Finishes). The inputs sit in a
  `<form>` that submits to the RFQ section with the values in the mailto body.
- **A11y:** the SVG has `role="img"` and an `aria-label` that states both ranges; the
  answer is text, never colour alone.

### 5.3 Thickness gauge ruler

- **What:** a vernier-style ruler from 0.10 to 4.50 mm, with ticks every 0.05 mm, used as
  the hero device on product pages and as the page divider. On hover/focus of a size in a
  table, a needle slides to that value.
- **JS off / reduced motion:** a static ruler with the min and max values marked in mono;
  it is decorative (`aria-hidden="true"`) because the numbers are always printed as text.

### 5.4 Application finder

- **What:** "What are you making?" with nine industry chips (Wood saw, Stone gang saw,
  Hack saw, Clutch and shims, Compressor valve, Textile and knitting, Band knife, Surgical
  blade, General springs). Each answers with recommended grades, product (CR or H&T),
  typical thickness, finish and hardness, linking to grade pages.
- **JS off:** each chip is an anchor to an `<article id="...">` section on the same page;
  `:target` styling highlights the chosen one. The chips are a real `<nav>` list.

### 5.5 RFQ starter (prefilled mailto with spec checklist)

- **What:** a short form (grade, standard, product, thickness, thickness tolerance, width,
  width tolerance, edge, finish, hardness HV/HRC, coil ID/OD or cut length, quantity per
  month, destination, name, company). Submit builds a `mailto:info@anil-industries.com`
  with a structured, labelled body ("Grade: C75S (EN 10132)...") and subject
  "RFQ: C75S, 0.35 x 32 mm, H&T". Any page with a grade or size in context pre-fills it
  (`?grade=c75s` read by JS, never containing personal data). Secondary routes:
  WhatsApp/phone for India, the named UK contact for export.
- **JS off:** the form uses `method="get" action="mailto:..." enctype="text/plain"`, which
  still opens a mail client; under it a copyable plain-text checklist ("Paste this into
  your email") and the direct email, phone and UK contact. No backend, no data stored.
- **A11y:** visible labels, `autocomplete` on name and organisation, error text in words.

### 5.6 Sticky spec summary on product and grade pages

- **What:** on wide screens a right-hand rail (`position: sticky`) showing the
  certificate fields (thickness, width, edges, finishes, hardness, grades count) and two
  actions: "Request a quote for this" and "Print spec sheet". On phones it collapses to a
  bottom bar with only the RFQ action.
- **JS off:** pure CSS sticky; it is just an `<aside>` that stays in normal flow where
  sticky is unsupported. No JS required at all.

### 5.7 Print-ready spec sheet (instead of PDFs)

- **What:** a `@media print` stylesheet that turns any product or grade page into a one-page
  A4 mill-style sheet: logo, document number, date printed, fields, chemistry, equivalents,
  contact block, URL. "Print / Save as PDF" is a button calling `window.print()`.
- **JS off:** the browser's own print works identically; the button is hidden by a
  `.js` class gate so no dead control shows.

### 5.8 mm / inch toggle (export buyers)

- **What:** every dimension is marked up as `<data value="0.35">0.35 mm</data>`; the toggle
  (Waelzholz pattern) rewrites the visible text to inches with 4 decimals and remembers the
  choice in `localStorage` (wrapped in try/catch).
- **JS off:** millimetres only, with a one-line note "1 mm = 0.03937 in". Metric is the
  contract unit anyway.

---

## 6. Sources (visited 9 Oct 2026)

- voestalpine Precision Strip: https://www.voestalpine.com/precision-strip/en/
- Alleima strip steel: https://www.alleima.com/en/products/strip-steel/
- Waelzholz: https://www.waelzholz.com/en/ and https://www.waelzholz.com/en/steel-materials/
- SSAB: https://www.ssab.com/en
- Outokumpu Steel Finder: https://www.outokumpu.com/en/products/steel-finder
- Aperam: https://www.aperam.com/
- Uddeholm: https://www.uddeholm.com/en/
- Hadrian: https://www.hadrian.co/
- Machina Labs: https://machinalabs.ai/
- IEM (2025 w3 Awards, manufacturing website): https://www.iemfg.com/ and
  https://www.wearefine.com/news/iem-wins-w3-2025-gold-award-for-best-manufacturing-website/
- Fontsource availability checked via `https://cdn.jsdelivr.net/fontsource/fonts/<id>@latest/latin-400-normal.woff2`
  (HTTP 200 for archivo, ibm-plex-sans, ibm-plex-mono, chivo, chivo-mono, public-sans,
  newsreader, schibsted-grotesk, spline-sans-mono, martian-mono) and the Fontsource API
  (Archivo variable axes: wdth 62 to 125, wght 100 to 900).
- Ulbrich (US precision strip) was attempted and returned HTTP 403 to automated fetches.
