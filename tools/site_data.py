"""Business facts and tables for the Anil Industries site.

Every value here is transcribed from the archived builder site (archive/*.html) or the owner's
answers recorded in docs/redesign-decisions.md. Do not add a fact that is not in one of those.
"""

DOMAIN = "https://www.anil-industries.com"

ORG = {
    "name": "Anil Industries",
    "founded": "1976",
    "founder": "Mr. Kewal Krishan Babbar",
    "founder_schema": "Kewal Krishan Babbar",
    "street": "L-125, Sector 2, DSIDC Bawana Industrial Area",
    "locality": "Delhi",
    "postcode": "110039",
    "lat": 28.7979915,
    "lng": 77.0521289,
    "email": "info@anil-industries.com",
    "phones": [("+91 99999 07396", "+919999907396"), ("+91 98116 37149", "+919811637149")],
    "uk": {
        "name": "Francisca Gomez",
        "phone": ("+44 7595 870124", "+447595870124"),
        "lines": ["63 Woodford Crescent", "Pinner, Middlesex", "HA5 3UA", "United Kingdom"],
    },
}

MAPS_URL = "https://www.google.com/maps/search/?api=1&query=28.7979915%2C77.0521289"

PRODUCTS = {
    "ht": {
        "name": "Hardened and tempered steel strips",
        "short": "Hardened and tempered",
        "slug": "hardened-tempered-steel-strips/",
        "doc": "AI / HT / 01",
        "img": "imgs/hardened-and-tempered-steel.webp",
        "img_w": 554, "img_h": 554,
        "img_alt": "Three coils of hardened and tempered spring steel strip in blue and bright finishes",
        "thk": ("0.10", "4.00"),
        "wid": ("5", "500"),
        "finish": "Scaleless: grey, bright, blue. Polished: bright, blue, bronze, gold.",
        "edges": "Slit, square or round",
        "hardness": "Supplied in hardness ranges to suit your part",
    },
    "cr": {
        "name": "Cold rolled steel strips",
        "short": "Cold rolled",
        "slug": "cold-rolled-steel-strips/",
        "doc": "AI / CR / 02",
        "img": "imgs/cold-rolled-steel-strips.webp",
        "img_w": 400, "img_h": 360,
        "img_alt": "Slit coils of cold rolled high carbon steel strip with a bright surface",
        "thk": ("0.20", "4.50"),
        "wid": ("12.5", "450"),
        "finish": "A wide range of surface finishes",
        "edges": "Slit to width",
        "hardness": "High tensile strength, yield strength and hardness",
    },
}

# Chemical composition, verbatim from the archive grade table (en dashes in 75Ni8 normalised to
# the hyphen form used by every other row). Columns: C, Mn, Si max, S max, P max, Cr, V, Ni, Mo.
CHEM_COLS = ["C %", "Mn %", "Si % (max)", "S % (max)", "P % (max)", "Cr %", "V %", "Ni %", "Mo %"]
CHEM = [
    ("C 45", ["0.42-0.50", "0.50-0.80", "0.4", "0.045", "0.045", "", "", "", ""]),
    ("C 50", ["0.47-0.55", "0.60-0.90", "0.4", "0.045", "0.045", "", "", "", ""]),
    ("C 55", ["0.50-0.60", "0.60-0.90", "0.35", "0.025", "0.035", "", "", "", ""]),
    ("C 65", ["0.60-0.70", "0.60-0.90", "0.35", "0.025", "0.035", "", "", "", ""]),
    ("C 75", ["0.70-0.80", "0.60-0.90", "0.35", "0.025", "0.035", "", "", "", ""]),
    ("C 80", ["0.75-0.85", "0.60-0.90", "0.35", "0.025", "0.035", "", "", "", ""]),
    ("SK85", ["0.80-0.90", "0.10-0.50", "0.10-0.35", "0.03", "0.03", "max 0.30", "", "max 0.25", ""]),
    ("SK95", ["0.90-1.00", "0.10-0.50", "0.10-0.35", "0.03", "0.03", "max 0.30", "", "max 0.25", ""]),
    ("C 98", ["0.95-1.05", "0.30-0.60", "0.10-0.35", "0.04", "0.04", "", "", "", ""]),
    ("C 120", ["1.10-1.30", "0.30-0.60", "0.25", "0.03", "0.03", "0.20-0.50", "", "", ""]),
    ("50CrV4", ["0.47-0.55", "0.70-1.10", "0.40", "0.035", "0.035", "0.90-1.20", "0.10-0.25", "", ""]),
    ("75Cr1", ["0.70-0.80", "0.60-0.80", "0.15-0.35", "0.03", "0.03", "0.30-0.40", "", "", ""]),
    ("75Cr25", ["0.70-0.78", "0.60-0.80", "max 0.35", "0.03", "0.04", "0.15-0.27", "", "", ""]),
    ("75Ni8", ["0.72-0.78", "0.30-0.50", "0.15-0.35", "0.025", "0.025", "max 0.15", "", "1.80-2.10", "max 0.1"]),
]

# International standards reference, cell for cell from the archive, except two column slips
# moved to the system they belong to (S50C -> JIS, 75Cr1 -> EN 10132); see
# docs/redesign-decisions.md section 13.
EQ_COLS = [
    ("sae", "USA", "SAE / AISI"),
    ("din", "Germany", "DIN 17222"),
    ("en", "Euronorm", "EN 10132"),
    ("bs1449", "Great Britain", "BS 1449"),
    ("bs970", "United Kingdom", "BS 970"),
    ("jis", "Japan", "JIS"),
    ("is", "India", "IS 2507"),
    ("gost", "Russia", "GOST"),
]
EQ = [
    ["1045", "CK 45", "", "", "EN 8D", "S45C", "45C 8", "45"],
    ["1050", "CK 50", "", "CS 50", "", "S50C", "", "50"],
    ["1055", "CK 55", "C55S", "", "EN 9", "S55C", "55C 6", "55"],
    ["1060", "CK 60", "C60S", "CS 60", "", "S60C / SUP11A", "", "60"],
    ["1065", "", "", "", "EN 42F", "S65C / SK7", "65C 6", "65"],
    ["1070", "CK 67", "C67S", "CS 70", "", "S70C", "70C 6", "70"],
    ["1074 / 1075", "CK 75", "C75S", "", "EN 42J", "S75C / SK6 / SUP3", "75C 6", ""],
    ["1080", "", "", "CS 80", "", "", "80C 6", ""],
    ["1085", "CK 85", "C85S", "", "", "SK85 / SK5", "85C 6", ""],
    ["1095", "CK 101", "C100S", "CS 95", "EN 44D", "SK95 / SK4 / SUP4", "98C 6", ""],
    ["", "", "C125S / 125Cr2", "", "", "SKS81 / SK2", "", ""],
    ["6150", "51CrV4", "51CrV4", "735A50", "EN 47", "SUP 10", "50Cr4V2", "50HGFA"],
    ["", "75Ni8", "75Ni8", "", "", "SKS51", "", ""],
    ["", "75Cr1", "75Cr1", "", "", "", "", ""],
]

# Processing route, from the archive diagram imgs/process-route.webp.
PROCESS = [
    ("Raw material", "Hot rolled coil is received and slit to a workable width."),
    ("Scale breaking and slitting", "Mill scale is cracked off mechanically and the coil is slit."),
    ("Acid pickling", "Remaining scale is removed in acid baths, leaving clean steel."),
    ("Annealing", "The strip is softened so it can be rolled further without cracking."),
    ("Cold rolling", "Rolled at room temperature down to the thickness you order."),
    ("Skin passing", "A light final pass sets the surface finish and flatness."),
    ("Cold rolled slitting", "Slit to your width, with the edge you specify."),
    ("Packing and dispatch", "Coils are sealed, hooped and wrapped for transport."),
]
PACKING = ["Seal", "Edge protector", "Steel hoop", "Metal protector", "Protective steel sheet",
           "Waterproof paper"]

# Applications, each tied to the product the archive lists it under.
APPLICATIONS = [
    ("saw-blades", "Saw blades",
     ["Band saw, hand saw, cross cut saw and pit saw blades, and all types of wood cutting saws",
      "Circular saw blanks for the engineering industry"],
     ["Hack saw and power saw blades, and all types of carbon saws"]),
    ("stone-cutting", "Stone cutting",
     ["Gang saw blades for marble and stone cutting"], []),
    ("automotive", "Automotive",
     ["Flat springs for clutch plates", "Shims and washers", "Auto electric contact springs",
      "Various components and springs"],
     ["Clutch parts and horn diaphragms", "Seat belt parts and brake assemblies",
      "Chain links, circlips and washers"]),
    ("compressors-engineering", "Compressors and engineering",
     ["Valve plates and flapper valves for compressors", "Forging hammer belts", "Mould liners",
      "Bearing casings"], ["General engineering strip springs"]),
    ("textile", "Textile and knitting machines",
     ["Knitting machine components", "Textile machine components"], []),
    ("leather-foam", "Leather and foam",
     ["Leather band knives", "Foam band knives"], []),
    ("medical-office", "Medical and office",
     [], ["Medical and surgical blades", "Stapler springs"]),
    ("tools-knives", "Tools, knives and springs",
     ["Masonry tools and agricultural tools", "Industrial knives",
      "Industrial springs and strip springs"], []),
]

# FAQ: visible text and FAQPage schema are generated from the same strings.
FAQ = [
    ("What is hardened and tempered steel strip?",
     "It is carbon or alloy steel strip that has been heated above the critical transformation "
     "temperature for its grade, quenched to make it hard, then reheated to a lower temperature and "
     "held there (tempering) to give it toughness and spring properties. We harden and temper in an "
     "inert atmosphere to avoid oxidation. The strip arrives ready to blank or form into springs, "
     "blades and valve parts. Our range is 0.10 to 4.00 mm thick and 5 to 500 mm wide."),
    ("What is the difference between cold rolled and hardened and tempered strip?",
     "Cold rolled strip is hot rolled steel processed further in cold reduction mills at room "
     "temperature, followed by annealing and/or temper rolling. It gives a wide range of surface "
     "finishes and closer thickness tolerances, and it is usually hardened after the part is made. "
     "Hardened and tempered strip has already been quenched and tempered, so the part keeps its "
     "spring hardness straight off the press."),
    ("Is C75 the same as CK75 or C75S?",
     "They describe practically the same steel of 0.70 to 0.80% carbon. CK 75 is the older German "
     "DIN 17222 name and C75S is the current European EN 10132 name. The closest equivalents are "
     "SAE 1074 / 1075, BS 970 EN 42J, JIS S75C / SK6 / SUP3 and IS 2507 75C 6. Equivalents are "
     "close, not identical, so always compare the chemistry."),
    ("What is the equivalent of SK5 (SK85)?",
     "SK85 is the current Japanese JIS name for the grade long called SK5. Its closest equivalents "
     "are SAE 1085, DIN 17222 CK 85, EN 10132 C85S and IS 2507 85C 6."),
    ("Which grades do you supply?",
     "C 45, C 50, C 55, C 65, C 75, C 80, SK85, SK95, C 98 and C 120, and the alloy grades 50CrV4, "
     "75Cr1, 75Cr25 and 75Ni8. Our grades page gives the chemistry of each and cross-references "
     "them to SAE / AISI, DIN 17222, EN 10132, BS 1449, BS 970, JIS, IS 2507 and GOST."),
    ("What hardness can you supply?",
     "Hardened and tempered strip can be supplied in different hardness ranges to suit your part. "
     "Tell us the hardness (HRC or HV) or the tensile range your drawing calls for and we will "
     "quote against it."),
    ("What finishes and edges are available?",
     "Hardened and tempered strip comes scaleless in grey, bright or blue, or polished in bright, "
     "blue, bronze or gold. Edges can be slit, square or round."),
    ("Is your cold rolled strip the same as CRCA?",
     "No. In India CRCA usually means cold rolled close annealed low carbon steel for car bodies "
     "and appliances. Our cold rolled strip is high carbon and alloy steel, from C 45 to C 120 and "
     "50CrV4 to 75Ni8, for parts such as saw blades, circlips and springs."),
    ("How is the strip packed?",
     "Coils leave us sealed and steel hooped, with edge protectors, a metal protector, a protective "
     "steel sheet and waterproof paper."),
    ("Do you work with buyers outside India?",
     "Yes. Buyers in the United Kingdom can reach our UK contact in Pinner, Middlesex, and any "
     "buyer can write to us in Delhi at info@anil-industries.com."),
    ("What should I include in a quote request?",
     "The grade and the standard it is specified to, thickness and width with tolerances, edge, "
     "finish, hardness, coil or cut length, the quantity and your delivery location. Our quote "
     "form lays these out for you."),
]
