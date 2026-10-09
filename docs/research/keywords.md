# Anil Industries: keywords and search intent (Phase 0, A.3)

Researched 2026-10-09 with live web search (IndiaMART and TradeIndia category pages, mill and
stockist datasheets, standards references). Follows `_rebuild-kit/RESEARCH-STRATEGY.md` A.3:
one primary intent per page, keywords used naturally, nothing invented.

**No search-volume tool was used.** Priorities below (P1 to P3) are judgement from how often a
term appears across marketplace listings, mill pages and competitor titles, not measured volume.
If the owner wants numbers, run the P1 and P2 terms through Google Keyword Planner (India and UK)
before the build locks titles.

Source facts used (from the brief and the archived site in `archive/`):

- Anil Industries, L-125 Sector-2, DSIDC Bawana Industrial Area, Delhi 110039. Since 1976.
  Founder named on the old About page: Mr. Kewal Krishan Babbar. UK contact in Pinner, Middlesex.
- Cold rolled steel strips: 0.20 to 4.50 mm thick, 12.5 to 450 mm wide.
- Hardened and tempered (H&T) strips: 0.10 to 4.00 mm thick, 5 to 500 mm wide. Finishes scaleless
  grey, bright, blue; polished bright, blue, bronze, gold. Slit, square or round edges. "Can be
  supplied in different hardness ranges to suit the customer." Old copy says the process runs in
  an inert atmosphere.
- Grades C45, C50, C55, C65, C75, C80, SK85, SK95, C98, C120, 50CrV4, 75Cr1, 75Cr25, 75Ni8, with
  the chemistry table and an international cross-reference table already on the old site.

---

## 1. Findings that shape the strategy

1. **The SERP is marketplace-led.** For "hardened and tempered spring steel strip India" and
   "band saw steel strip India", page one is IndiaMART, TradeIndia, GlobalLinker, ExportersIndia
   and a few mills (Jainex, Bhushan). Most listings are thin: one grade, one thickness, no
   cross-reference. A manufacturer site with a real grade and equivalents table, sizes, finishes
   and applications on crawlable HTML has a genuine content gap to fill.
2. **No Bawana or Delhi maker ranks for H&T strip.** Delhi results are traders (for example TMA
   International, KND Steel listing Tata SUP10). "Delhi" and "Bawana" modifiers are therefore
   winnable, though low volume.
3. **Name collision.** "Anil Special Steel Industries" (Jaipur, Shalimar group) is a large H&T strip
   producer and shows up for the same queries. The site must make the brand unambiguous: always
   "Anil Industries, Bawana, Delhi" in the title of Home and Contact, in the Organization schema
   `name` + `address`, and in the footer. Never shorten to "Anil Steel".
4. **Grade-equivalent queries are a strong, under-served informational cluster.** Buyers search
   "C75 equivalent", "CK75 vs C75S", "SK5 equivalent", "50CrV4 equivalent SAE 6150". The answers
   live on aggregator sites (mfgrobots, totalmateria, machinemfg) that do not sell strip. A
   cross-reference page that also sells the strip can win these and convert them.
5. **Old UK and DIN designations are still what buyers type.** BS 5770 was withdrawn in 2000 and
   DIN 17222 was replaced by EN 10132, yet UK stockists still sell "CS80", "CS95", "EN42J" and
   quote "BS 5770". German and Indian buyers still write "CK75", "CK101". Use the current standard
   as the heading and the legacy names in the table and body so both are matched.
6. **"CRCA strip" is a different buyer.** In India CRCA means cold rolled close annealed, usually
   low carbon to IS 513 for automotive and white goods. Anil's cold rolled strip is high carbon
   (C45 to C120, alloy spring grades) for parts that are hardened later. Do **not** target "CRCA"
   as a primary keyword. Mention it once on the cold rolled page to disambiguate ("not CRCA mild
   steel: these are high carbon grades for hardening").
7. **Flapper valve steel is a premium niche** dominated by Alleima and voestalpine (20C, AISI 1095
   type, and martensitic stainless). Anil's old site lists "valve plate and flapper valve for
   compressor" as an application. Use it as an application section, not a page, and do not claim
   equivalence to those branded grades.
8. **Hardness is the most asked technical question** and no Indian supplier page answers it. The
   old site only says hardness is to customer requirement. A general, correctly hedged answer in
   the FAQ plus an owner-confirmed supply range (if they will give one) is a differentiator.

---

## 2. Keyword clusters with search intent

Intent: **T** transactional / commercial (wants a supplier), **I** informational, **L** local,
**X** export / international. Priority P1 (build the page around it) to P3 (use in body/FAQ).

### 2.1 Core product: hardened and tempered strip

| Keyword | Intent | Priority | Notes |
|---|---|---|---|
| hardened and tempered steel strip | T | P1 | Primary for H&T page |
| hardened and tempered spring steel strip | T | P1 | H1 wording |
| spring steel strip | T/I | P1 | Broadest head term; Home + H&T |
| spring steel strip manufacturer / supplier India | T, X | P1 | Use "supplier" until manufacturing is confirmed (see flags) |
| H&T strip / HT steel strip | T | P2 | Indian trade shorthand, use once in body and alt |
| high carbon spring steel strip | T | P2 | IndiaMART category name |
| blue tempered spring steel / blue polished spring steel strip | T, X | P2 | US and UK phrasing for the finish |
| polished spring steel strip, bright | T | P3 | Finish section H2 |
| scaleless blue / scaleless grey strip | I/T | P3 | Explain in finishes section |
| spring steel coil, slit coil | T, X | P3 | International buyers order "coil", Indian buyers say "strip" |
| quenched and tempered strip (Q+T) | X | P3 | European wording, synonym in body |
| pre-hardened spring steel strip | X | P3 | UK/US wording |

### 2.2 Core product: cold rolled strip

| Keyword | Intent | Priority | Notes |
|---|---|---|---|
| cold rolled steel strip | T | P1 | Primary for CR page (fix old URL typo "coled") |
| cold rolled high carbon steel strip | T | P1 | Qualifies against CRCA mild steel |
| cold rolled spring steel strip | T | P2 | IndiaMART listing title pattern |
| CR strip | T | P3 | Indian shorthand |
| annealed high carbon strip, soft annealed strip | T, X | P3 | Use only if the owner confirms delivery condition (annealed / skin passed) |
| CRCA strip | T | Avoid as target | Different product and buyer, mention once to disambiguate |

### 2.3 Grade-led

| Keyword | Intent | Priority | Page |
|---|---|---|---|
| C75 spring steel strip | T | P1 | Grades (anchor #c75) + H&T |
| CK75 equivalent / CK75 steel | I | P1 | Grades |
| C75S EN 10132 | I, X | P2 | Grades |
| SAE 1075 / AISI 1075 equivalent | I, X | P2 | Grades |
| C80 / CK85 / C85S / 1085 spring steel | T/I | P2 | Grades |
| SK5 / SK85 steel strip, SK5 equivalent | T/I, X | P1 | Grades (Japanese grade, popular in knife and blade trade) |
| SK4 / SK95 equivalent | I | P3 | Grades |
| C100S / CK101 / 1095 spring steel strip | T/I | P2 | Grades |
| 50CrV4 strip, 51CrV4 strip, SAE 6150 equivalent | T/I, X | P1 | Grades |
| 75Ni8 strip (band saw steel) | T | P2 | Grades + Applications (band saw) |
| 75Cr1 strip (circular saw, gang saw) | T | P2 | Grades + Applications |
| C45 / C55 / C65 steel strip, S45C, S55C | T/I | P3 | Grades |
| CS80 / CS95 spring steel (UK) | X | P2 | Grades, BS column |
| EN42J / EN44D spring steel | X, I | P3 | Grades, BS 970 column |
| EN 10132-4 spring steel strip | I, X | P2 | Grades intro |
| DIN 17222 | I, X | P3 | Grades, legacy column |
| IS 2507 spring steel | I, L | P3 | Grades, India column |
| spring steel grades chart / equivalent grades table | I | P1 | Grades H1 intent |

### 2.4 Application-led

| Keyword | Intent | Priority | Section on Applications page |
|---|---|---|---|
| band saw steel strip / bandsaw blade steel | T | P1 | Wood cutting saws |
| gang saw blade steel / marble gang saw strip | T | P2 | Stone cutting |
| hacksaw blade steel strip / power hacksaw strip | T | P2 | Metal cutting saws (cold rolled) |
| circular saw blank steel | T | P3 | Saw blanks |
| compressor flapper valve steel / valve plate steel | T | P2 | Compressor valves |
| clutch plate spring steel / cushion spring strip | T | P3 | Automotive |
| horn diaphragm steel | T | P3 | Automotive (note: old site spelt "diaphram") |
| circlip strip, washer and shim steel strip | T | P3 | Springs, circlips, washers, shims |
| surgical blade steel strip | T | P3 | Medical blades |
| textile / knitting machine component strip | T | P3 | Textile machinery |
| leather band knife steel / foam cutting band knife | T | P3 | Band knives |
| doctor blade / industrial knife strip | T | P3 | Only "industrial knives" is a confirmed application; do not add doctor blades unless confirmed |

### 2.5 Local (India)

| Keyword | Intent | Priority | Where |
|---|---|---|---|
| spring steel strip supplier Delhi | L, T | P1 | Home title/H1 support, Contact |
| steel strip manufacturer Delhi / NCR | L, T | P2 | Home, About (only if manufacturing confirmed) |
| hardened and tempered strip Bawana / DSIDC Bawana | L | P3 | Contact, footer, schema |
| spring steel strip India | T | P1 | Home, H&T |
| steel strip supplier Delhi since 1976 | L, nav | P3 | About |

### 2.6 Export / international

| Keyword | Intent | Priority | Where |
|---|---|---|---|
| spring steel strip exporter India | X | P2 | Home section "Export and UK buyers", Contact |
| hardened and tempered strip supplier UK | X | P2 | Contact (UK contact block), About |
| spring steel strip from India | X | P3 | Home body |
| C75S / CK75 strip supplier (Europe) | X | P3 | Grades |
| 1075 / 1095 spring steel strip supplier (US) | X | P3 | Grades, inch equivalents on product pages |

### 2.7 Natural-language questions (feed the FAQ)

- what is hardened and tempered steel / strip
- difference between cold rolled and hardened and tempered strip
- what is spring steel made of / what grade is spring steel
- C75 vs CK75, is C75 the same as CK75, what is C75S
- what is the equivalent of SK5 / SK85, SK5 vs 1080
- 50CrV4 vs 51CrV4, 50CrV4 equivalent
- what hardness is spring steel strip, HRC of hardened and tempered strip
- what is blue tempered / blue polished spring steel, scaleless meaning
- which steel is used for band saw blades / gang saw blades / flapper valves
- what is CRCA, is cold rolled strip the same as CRCA
- slit edge vs round edge strip
- minimum order quantity for spring steel strip, test certificate (mill test certificate / MTC / EN 10204 3.1)

---

## 3. Recommended page set (lean lead-gen B2B)

Seven pages plus a FAQ. No "Products" hub page: with two products, Home does the hub job and the
nav uses a two-item Products menu. No separate page per application or per grade (each would be
thin); they are anchored sections that can be split later if Search Console shows demand.

| # | Page | Path (directory URL, relative links) | Job in the funnel | Primary CTA |
|---|---|---|---|---|
| 1 | Home | `./` | Say what, where, for whom in 5 s; route to a product; trust (since 1976) | Request a quote |
| 2 | Hardened and tempered strips | `hardened-tempered-steel-strips/` | Spec sheet buyers act on: sizes, finishes, edges, grades, uses | Request a quote (prefills product) |
| 3 | Cold rolled strips | `cold-rolled-steel-strips/` | Same, for CR high carbon strip | Request a quote |
| 4 | Grades and equivalents | `grades/` | Cross-reference tool (filterable table + chemistry). Captures grade queries and converts them | "Quote this grade" per row |
| 5 | Applications | `applications/` | Buyer finds their part (band saw, flapper valve...) and the grades used for it | Request a quote |
| 6 | Quality and process | `quality/` | Objection handling: how strip is processed, inspected, packed, what certificates ship | Request a quote. **Build only if the owner supplies real facts**; otherwise fold into About as one section |
| 7 | About | `about/` | Since 1976, founder, Bawana works, UK contact, who we supply | Contact |
| 8 | FAQ | `faq/` | Answers the question cluster; feeds teasers on Home and product pages | Request a quote |
| 9 | Contact / RFQ | `contact/` | RFQ form (grade, thickness, width, finish, edge, hardness, qty, destination), Delhi + UK contacts, map, `tel:` and `wa.me` | Send enquiry |

Redirects (old URLs are `.html` on the live site): `coled-rolled-steel-strips.html` to
`cold-rolled-steel-strips/`, `hardened-tempered-steel.html` to `hardened-tempered-steel-strips/`,
`qualities.html` to `quality/` (or `about/#quality` if folded), `about.html`, `contact.html`,
`index.html` to their directory equivalents. Use Cloudflare `_redirects` (301).

---

## 4. Keyword to page to where-used

One primary intent per page. "Supporting" terms appear in H2s, body and alt, never stuffed.

| Page | Primary keyword | Supporting keywords | Title (under 60) | H1 | H2s | Image alt examples | Schema |
|---|---|---|---|---|---|---|---|
| Home | spring steel strip supplier Delhi | hardened and tempered steel strip, cold rolled steel strip, spring steel strip India, since 1976, export UK | Spring Steel Strips, Delhi, since 1976 \| Anil Industries | Hardened and tempered and cold rolled steel strips, Delhi, since 1976 | Two products, one supplier; Grades we stock and their equivalents; Where our strip goes (applications); Export and UK buyers; Common questions; Request a quote | "Coils of blue polished hardened and tempered spring steel strip at Anil Industries, Bawana, Delhi" | Organization + LocalBusiness (address, geo, foundingDate 1976, areaServed IN + GB, contactPoint x2), WebSite |
| Hardened and tempered | hardened and tempered spring steel strip | spring steel strip, H&T strip, blue polished spring steel, scaleless, quenched and tempered, C75, C80, SK85, 75Ni8, 50CrV4, band saw strip | Hardened and Tempered Spring Steel Strips \| Anil Industries | Hardened and tempered spring steel strips | Sizes: 0.10 to 4.00 mm by 5 to 500 mm; Finishes: scaleless and polished; Edges: slit, square, round; Hardness to your specification; Grades and equivalents; Applications; Questions | "Hardened and tempered spring steel strip, polished blue finish, round edge" | Product (name, description, material, brand; no price, no reviews), BreadcrumbList |
| Cold rolled | cold rolled high carbon steel strip | cold rolled steel strip, cold rolled spring steel strip, CR strip, hacksaw blade strip, not CRCA | Cold Rolled High Carbon Steel Strips \| Anil Industries | Cold rolled high carbon steel strips | Sizes: 0.20 to 4.50 mm by 12.5 to 450 mm; Grades; What it is used for (hacksaw, power saw, clutch, horn diaphragm, circlip, surgical blade, stapler spring); Cold rolled or hardened and tempered?; Questions | "Slit coils of cold rolled high carbon steel strip" | Product, BreadcrumbList |
| Grades | spring steel grades and equivalents | C75 equivalent, CK75, C75S, SAE 1075, SK5 / SK85, 50CrV4 / 51CrV4 / 6150, 75Ni8, 75Cr1, CS80, EN42J, EN 10132, DIN 17222, IS 2507, JIS, GOST | Spring Steel Grades and Equivalents: C75, CK75, SK5, 1075 | Spring steel strip grades and international equivalents | How to read the table; Carbon grades C45 to C120; Alloy grades 50CrV4, 75Cr1, 75Cr25, 75Ni8; Chemical composition; Legacy names (CK, CS, EN) and current EN 10132 names; Questions | Mostly a table; any image: "Grade-marked spring steel strip coils" | Dataset is overkill: use WebPage + BreadcrumbList; table as real HTML `<table>` |
| Applications | spring steel strip applications | band saw steel strip, gang saw blade steel, hacksaw strip, compressor flapper valve steel, clutch plate spring, circlips, washers, shims, surgical blades, band knives | Spring Steel Strip for Saw Blades, Valves and Springs | Where our steel strip is used | Saw blades (band, hand, gang, hack, power, circular blanks); Compressor valve plates and flappers; Automotive springs and parts; Washers, shims and circlips; Textile and knitting machine parts; Leather and foam band knives; Tools and industrial knives | "Band saw blades made from hardened and tempered strip" (only with a real photo) | WebPage + BreadcrumbList |
| Quality | spring steel strip quality / how H&T strip is made | inert atmosphere, flatness, hardness uniformity, slitting, edge dressing, test certificate | Quality and Process \| Anil Industries Steel Strips | How we process and check every coil | Hardening and tempering; Slitting and edge finishing; Inspection and documents; Packing for export | Real process photos only | WebPage + BreadcrumbList |
| About | Anil Industries Delhi since 1976 | steel strip supplier since 1976, Bawana, UK contact | About Anil Industries \| Steel Strip Supplier since 1976 | Steel strip supplier in Delhi since 1976 | Our story; The Bawana works; UK contact for export buyers; Who we supply | "Anil Industries works, L-125 DSIDC Bawana, Delhi" | Organization (founder, foundingDate), BreadcrumbList |
| FAQ | spring steel strip FAQ | all section 2.7 questions | Spring Steel Strip FAQ: Grades, Hardness and Finishes | Questions about spring steel strip | grouped: Products; Grades; Hardness and finish; Ordering | none needed | FAQPage (note: Google only shows FAQ rich results for a few authority sites since 2023, the markup is still valid and helps AI answers), BreadcrumbList |
| Contact | request a quote steel strip | spring steel strip supplier Delhi, UK contact, Bawana | Request a Quote for Steel Strips \| Anil Industries, Delhi | Request a quote | What to include in your enquiry; Delhi works; UK contact; Map | "Map of Anil Industries, DSIDC Bawana Industrial Area, Delhi" | LocalBusiness + ContactPage, BreadcrumbList |

### Draft meta descriptions (under 155 characters, no dashes, no invented claims)

| Page | Meta description |
|---|---|
| Home | Hardened and tempered spring steel strips and cold rolled high carbon strips from Bawana, Delhi, since 1976. C45 to C120, 50CrV4, 75Ni8. Request a quote. |
| Hardened and tempered | Hardened and tempered spring steel strip, 0.10 to 4.00 mm thick, 5 to 500 mm wide. Grey, bright, blue, bronze or gold finish. C75, C80, SK85, 75Ni8. |
| Cold rolled | Cold rolled high carbon steel strip, 0.20 to 4.50 mm thick, 12.5 to 450 mm wide, in C45 to C120, 50CrV4 and 75Ni8. For saw blades, clutches and circlips. |
| Grades | Cross-reference spring steel strip grades across SAE/AISI, DIN, EN 10132, BS, JIS, IS and GOST. Find the equivalent of C75, CK75, SK5, 50CrV4 and 75Ni8. |
| Applications | Steel strip for band saw, hack saw and gang saw blades, compressor flapper valves, clutch springs, circlips, shims, surgical blades and band knives. |
| Quality | How Anil Industries processes and checks spring steel strip in Delhi, and what to specify when you order: grade, size, hardness, finish and edge. |
| About | Anil Industries has supplied cold rolled and hardened and tempered steel strips from Delhi since 1976, with a UK contact in Pinner for export buyers. |
| FAQ | Answers on hardened and tempered strip: grades, equivalents, hardness, finishes, edges, sizes, cold rolled vs H&T, and how to order from Delhi or the UK. |
| Contact | Send your grade, thickness, width, finish and quantity for a quote. Anil Industries, L-125 Sector-2, DSIDC Bawana, Delhi 110039. UK contact in Pinner. |

The Quality description assumes Anil does the processing in Delhi. Confirm before use (flag F1).

---

## 5. FAQ (draft answers)

General metallurgy or the facts above only. **[CONFIRM]** marks anything the owner must verify
before it ships.

1. **What is hardened and tempered steel strip?**
   Carbon or alloy steel strip that has been heated above its critical temperature, quenched to
   make it fully hard, then reheated to a lower temperature (tempered) to trade a little hardness
   for toughness and spring properties. It arrives ready to blank or form into springs, blades and
   valve parts with no further heat treatment. Our hardened and tempered strip runs from 0.10 to
   4.00 mm thick and 5 to 500 mm wide.

2. **What is the difference between cold rolled and hardened and tempered strip?**
   Cold rolled strip is rolled to thickness at room temperature and is usually annealed, so it is
   relatively soft and easy to blank, punch and form. The buyer hardens the finished part. Hardened
   and tempered strip has already been through quench and temper, so the part keeps its spring
   hardness straight off the press. Choose cold rolled when you form heavily or heat treat in
   house; choose H&T when you want ready-to-use spring properties. [CONFIRM the delivery condition
   of the cold rolled strip: annealed, skin passed or as rolled]

3. **Is C75 the same as CK75 or C75S?**
   They describe practically the same 0.70 to 0.80% carbon steel. CK75 is the older German DIN
   17222 name, C75S is the current European name under EN 10132-4 (cold rolled narrow strip for
   springs), and SAE 1074/1075, JIS S75C and IS 75C6 are the closest equivalents in other systems.
   Equivalents are close, not identical, so always check the chemistry on the test certificate.

4. **What is the equivalent of SK5 (SK85)?**
   SK85 is the current Japanese JIS name for the grade long called SK5, a high carbon steel of
   about 0.80 to 0.90% carbon. It sits closest to C85S / CK85 under EN and DIN and to SAE 1080 to
   1085 in the US system. SK95 (formerly SK4) is the next step up, close to C100S / CK101 / SAE 1095.

5. **Which grades do you supply?**
   C45, C50, C55, C65, C75, C80, SK85, SK95, C98, C120, and the alloy grades 50CrV4, 75Cr1, 75Cr25
   and 75Ni8. Our grades page cross-references each to SAE/AISI, DIN 17222, EN 10132, BS, JIS, IS
   2507 and GOST. [CONFIRM which grades are available in which product: the old site printed the
   same table on both product pages]

6. **What hardness can you supply?**
   Hardened and tempered strip can be supplied in different hardness ranges to suit the part.
   As a general guide, softer tempers suit parts that are bent or set (band saw bodies, clutch
   springs) and harder tempers suit blanked flat springs, blades and valve plates. Tell us the
   hardness (HRC or HV) or tensile range your drawing calls for and we will match it. [CONFIRM the
   achievable range per grade and thickness before publishing any numbers]

7. **What finishes and edges are available?**
   Scaleless finishes in grey, bright or blue, and polished finishes in bright, blue, bronze or
   gold. Scaleless is the tempered surface without polishing; polished strip is ground or buffed
   bright, then left bright or coloured by a controlled oxide tint. Edges can be slit, square or
   round.

8. **Which steel is used for band saw, gang saw and hacksaw blades?**
   Wood band saw blades are commonly made from hardened and tempered high carbon or nickel alloyed
   strip such as C75 or 75Ni8. Marble and stone gang saw blades need very flat hardened and tempered
   strip, often a chromium alloyed grade such as 75Cr1. Hacksaw and power saw blades are commonly
   made from cold rolled high carbon strip that the blade maker hardens. Send us your blade size and
   we will suggest a grade. [CONFIRM the grades Anil actually recommends for each blade type]

9. **Is your cold rolled strip the same as CRCA?**
   No. In India CRCA usually means cold rolled close annealed low carbon (mild) steel for car
   bodies and appliances. Our cold rolled strip is high carbon and alloy spring steel, from C45 to
   C120 and 50CrV4 to 75Ni8, for parts that are hardened.

10. **Do you supply buyers outside India?**
    Yes, export buyers can reach us through our UK contact in Pinner, Middlesex, or the Delhi
    office directly. [CONFIRM countries served, shipping terms (FOB / CIF), and whether the UK
    contact holds stock or only handles enquiries]

11. **Do you provide test certificates?**
    [CONFIRM: mill test certificate or EN 10204 3.1 inspection certificate, what it reports
    (chemistry, hardness, tensile, dimensions), and whether it ships with every coil]

12. **What is the minimum order and the lead time?**
    [CONFIRM: MOQ by weight or coil, cut-to-length and slit-to-width options, typical lead time
    for stock grades and for special sizes or finishes]

---

## 6. Spelling and terminology for an international audience

| Topic | Use on the site | Also mention (body, alt, tables) | Why |
|---|---|---|---|
| Heat treatment name | "hardened and tempered" (H&T) | "quenched and tempered (Q+T)", "pre-hardened", "heat treated" | H&T is standard in India and UK; Q+T in EU; "pre-hardened" and "blue tempered" in UK/US |
| Product form | "strip" in headings | "coil", "slit coil", "flat", "strip in lengths", Hindi "patti" not needed | Indian buyers search strip; overseas buyers order coils and specify width "slit to" |
| Colour finish | "blue polished", "bright polished", "scaleless blue" | "blue tempered spring steel" | US stockists (McMaster style) sell "blue tempered 1075 / 1095" |
| Spelling | British English: colour, mould, aluminium, metre | | India and UK both use British spelling; fix old site typos "coled", "diaphram", "Temperings" |
| Units | mm first, inch in brackets on spec tables | 0.10 mm = 0.004 in; 4.00 mm = 0.157 in; 4.50 mm = 0.177 in; 500 mm = 19.7 in | US buyers think in thousandths of an inch |
| Thickness word | "thickness" | "gauge" | "gauge" is common in UK/US speech; do not use gauge numbers |
| Hardness | HRC and HV both | tensile strength in MPa (N/mm2) | EU specs use HV or tensile; US uses HRC |
| Standards | lead with current EN 10132-4 names (C75S) | DIN 17222 (CK75), BS 5770 / BS 1449 (CS80, CS95), BS 970 (EN42J), SAE/AISI, JIS, IS 2507, GOST | Legacy names are what people still search; BS 5770 is withdrawn, so do not claim conformance to it |
| CRCA | avoid as a product name | one disambiguation line | Means low carbon close annealed in India |
| Number format | 1,000 kg (international) | avoid lakh/crore | Export audience |
| Dashes | none: write "0.10 to 4.00 mm", never an en dash range | | House rule |

---

## 7. Owner confirmation flags (block publishing until answered)

- **F1 Manufacturer or supplier?** The old site says "supplier" on Home but has a "Manufacturing"
  page and describes hardening "in an inert atmosphere". If Anil runs its own H&T, slitting or
  rolling in Bawana, "manufacturer" keywords open up (high value). If not, keep "supplier".
- **F2** Delivery condition of cold rolled strip (annealed / skin passed / as rolled).
- **F3** Which grades in which product, and any grade the old table lists but is no longer stocked.
- **F4** Hardness range per grade and thickness, if they will publish one.
- **F5** Test certificates (type, contents), MOQ, lead time, cut-to-length, packing for export.
- **F6** Export: countries served, Incoterms, role of the UK contact (stock or enquiries).
- **F7** Raw material source. Old About says they "team up with the best of German brands for crude
  materials". If a named mill can be stated, it is a strong trust signal; if not, drop it.
- **F8** Drop unverifiable superlatives from the old copy ("fastest growing steel supplier in the
  world", "world class manufacturing base", "100% on-time delivery"). Not to be carried over.
- **F9** Founder name (Mr. Kewal Krishan Babbar) and current leadership for About and schema.

---

## Sources consulted

- IndiaMART spring steel strip category: https://m.indiamart.com/impcat/spring-steel-strip.html
- IndiaMART steel strips category: https://m.indiamart.com/impcat/steel-strips.html
- GlobalLinker steel strips: https://www.globallinker.com/steel-strips
- Anil Special Steel Industries profile (name collision): https://live-next.indiainfoline.com/company/anil-special-steel-industries-ltd/summary
- EN 10132-4 CK75 / C75S data: https://www.mfgrobots.com/Article/material/metal/35712.html
- thyssenkrupp C75/C75S and 75Cr1 precision strip sheets: https://www.thyssenkrupp-steel.com/
- 50CrV4 / 51CrV4 equivalents (Saarstahl): https://www.saarstahl.com/app/uploads/2024/03/20160318100831-51CrV4-50CrV4-.pdf
- SK85 / SK5 equivalents: https://www.marklines.com/en/product/1315
- Flapper valve steels: https://www.alleima.com/en/products/strip-steel/compressor-valve-steel and https://www.chillventa.de/en/exhibitors/voestalpine-precision-strip-ab-2256716/flapper-valve-steel-2363579
- Gang saw strip: https://www.voestalpine.com/precision-strip/products-brands/martin-miller/stone-saw-steel and https://www.waelzholz.com/en/news-stories/detail/precision-material-steel-strip-for-saw-blades
- Finishes (scaleless, bright and blue polished): https://www.voestalpine.com/precision-strip/products-brands/wisconstrip/special-strip-steel/specification
- UK CS80 / CS95 terminology: https://www.westyorkssteel.com/spring-steel/ ; BS 5770-3 withdrawn: https://knowledge.bsigroup.com/products/steel-strip-intended-for-the-manufacture-of-springs-specification-for-pre-hardened-and-tempered-carbon-steel
- CRCA meaning in India: https://www.ofbusiness.com/blog/metals/crc-uses-grades-150960
- Archived Anil Industries site: `../../archive/*.html`
