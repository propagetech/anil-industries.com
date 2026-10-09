#!/usr/bin/env python3
"""One-shot static page generator for anil-industries.com.

Emits plain static HTML (committed; the deployed site has no build step). Keeps <head>, header
and footer byte-identical across pages and makes every asset/link path depth-aware:
home uses "" (css/...), inner pages "../", 404.html "/" (root-absolute, served at any depth).
Canonical / og:url / sitemap / JSON-LD stay absolute on the production domain.

Facts live in tools/site_data.py. Run from the repo root:  python3 tools/build.py
"""
import html
import json
import os
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(__file__))
from site_data import (APPLICATIONS, CHEM, CHEM_COLS, DOMAIN, EQ, EQ_COLS, FAQ, MAPS_URL, ORG,
                       PACKING, PROCESS, PRODUCTS)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OG = "imgs/og-card.jpg"
E = html.escape
YEAR = "2026"


def esc_attr(s):
    return html.escape(s, quote=True)


def mailto(subject, body):
    return "mailto:%s?subject=%s&amp;body=%s" % (ORG["email"], quote(subject), quote(body))


def home_href(p):
    return p if p else "./"


# --------------------------------------------------------------------------------------------
# Shared chrome
# --------------------------------------------------------------------------------------------

NAV = [
    ("grades", "Grades", "grades/"),
    ("applications", "Applications", "applications/"),
    ("quality", "Quality", "quality/"),
    ("about", "About", "about/"),
    ("faq", "FAQ", "faq/"),
]


def head(p, page):
    url = DOMAIN + "/" + page["slug"]
    ld = json.dumps(page["schema"], ensure_ascii=False, indent=1)
    return f'''<!doctype html>
<html lang="en-GB" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(page["title"])}</title>
<meta name="description" content="{esc_attr(page["desc"])}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#F5F5F2">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Anil Industries">
<meta property="og:title" content="{esc_attr(page["title"])}">
<meta property="og:description" content="{esc_attr(page["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/{OG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc_attr(page["title"])}">
<meta name="twitter:description" content="{esc_attr(page["desc"])}">
<meta name="twitter:image" content="{DOMAIN}/{OG}">
<link rel="icon" href="{p}imgs/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{p}imgs/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{p}imgs/apple-touch-icon.png">
<link rel="manifest" href="{p}site.webmanifest">
<link rel="preload" href="{p}fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}fonts/plex-sans-400.woff2" as="font" type="font/woff2" crossorigin>
{page.get("preload", "")}<link rel="stylesheet" href="{p}css/main.css">
<script>document.documentElement.className=document.documentElement.className.replace("no-js","js");</script>
<script src="{p}js/main.js" defer></script>
<script type="application/ld+json">
{ld}
</script>
</head>
'''


def header(p, active):
    ph, pc = PRODUCTS["ht"], PRODUCTS["cr"]
    prod_cur = " is-current" if active in ("ht", "cr") else ""

    def cur(k):
        return ' aria-current="page"' if k == active else ""

    items = "\n".join(
        f'        <li class="nav__item"><a class="nav__link" href="{p}{slug}"{cur(k)}>{label}</a></li>'
        for k, label, slug in NAV)
    return f'''<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topline">
  <div class="wrap topline__in">
    <p class="topline__id"><span>Anil Industries</span><span>Bawana, Delhi</span><span>Since 1976</span></p>
    <p class="topline__contact"><a href="tel:{ORG["phones"][0][1]}">{ORG["phones"][0][0]}</a><a href="mailto:{ORG["email"]}">{ORG["email"]}</a></p>
  </div>
</div>
<header class="site-header">
  <div class="wrap site-header__in">
    <a class="brand" href="{home_href(p)}" aria-label="Anil Industries, home"><img src="{p}imgs/logo-horizontal.webp" width="2150" height="272" alt=""></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav"><span class="nav-toggle__bars" aria-hidden="true"></span><span class="nav-toggle__label">Menu</span></button>
    <nav class="nav" id="site-nav" aria-label="Primary">
      <ul class="nav__list">
        <li class="nav__item nav__item--sub">
          <button class="nav__link nav__sub-toggle{prod_cur}" type="button" aria-expanded="false" aria-controls="nav-products">Products</button>
          <ul class="nav__sub" id="nav-products">
            <li><a href="{p}{ph["slug"]}"{cur("ht")}><span class="nav__sub-code">HT</span>Hardened and tempered strips</a></li>
            <li><a href="{p}{pc["slug"]}"{cur("cr")}><span class="nav__sub-code">CR</span>Cold rolled strips</a></li>
          </ul>
        </li>
{items}
        <li class="nav__item nav__item--cta"><a class="btn btn--primary btn--sm" href="{p}contact/"{cur("contact")}>Request a quote</a></li>
      </ul>
    </nav>
  </div>
</header>
'''


def footer(p):
    ph, pc = PRODUCTS["ht"], PRODUCTS["cr"]
    uk = ORG["uk"]
    phones = "<br>".join(f'<a href="tel:{t}">{d}</a>' for d, t in ORG["phones"])
    return f'''<footer class="site-footer">
  <div class="wrap site-footer__grid">
    <div class="site-footer__brand">
      <a class="brand brand--footer" href="{home_href(p)}" aria-label="Anil Industries, home"><img src="{p}imgs/logo.webp" width="500" height="224" alt=""></a>
      <p>Cold rolled and hardened and tempered steel strips, processed and supplied from Bawana, Delhi since 1976.</p>
    </div>
    <nav class="site-footer__col" aria-label="Products">
      <h2 class="site-footer__h">Products</h2>
      <ul>
        <li><a href="{p}{ph["slug"]}">Hardened and tempered strips</a></li>
        <li><a href="{p}{pc["slug"]}">Cold rolled strips</a></li>
        <li><a href="{p}grades/">Grades and equivalents</a></li>
        <li><a href="{p}applications/">Applications</a></li>
      </ul>
    </nav>
    <nav class="site-footer__col" aria-label="Company">
      <h2 class="site-footer__h">Company</h2>
      <ul>
        <li><a href="{p}quality/">Quality and process</a></li>
        <li><a href="{p}about/">About us</a></li>
        <li><a href="{p}faq/">Questions</a></li>
        <li><a href="{p}contact/">Request a quote</a></li>
      </ul>
    </nav>
    <div class="site-footer__col">
      <h2 class="site-footer__h">Delhi works</h2>
      <address>{E(ORG["street"])},<br>{ORG["locality"]} {ORG["postcode"]}, India<br>{phones}<br><a href="mailto:{ORG["email"]}">{ORG["email"]}</a></address>
    </div>
    <div class="site-footer__col">
      <h2 class="site-footer__h">UK contact</h2>
      <address>{uk["name"]}<br>{"<br>".join(uk["lines"])}<br><a href="tel:{uk["phone"][1]}">{uk["phone"][0]}</a></address>
    </div>
  </div>
  <div class="wrap site-footer__standards">
    <ul aria-label="Website standards">
      <li>WCAG 2.1 AA</li><li>No cookies or tracking</li><li>Self-hosted, no third-party requests</li><li>Served over HTTPS</li>
    </ul>
    <p>&copy; {YEAR} Anil Industries, Bawana, Delhi. Website by <a href="https://propage.in">ProPage</a>.</p>
  </div>
</footer>
</body>
</html>
'''


# --------------------------------------------------------------------------------------------
# Components
# --------------------------------------------------------------------------------------------

def sec_head(num, label, ref=""):
    r = f'<p class="folio__ref" aria-hidden="true">{ref}</p>' if ref else ""
    return (f'<div class="folio"><p class="folio__id"><span class="folio__num">{num}</span>'
            f'<span class="folio__label">{label}</span></p>{r}</div>')


def stamp(extra=""):
    """Decorative inspection stamp (ring text). Not the logo: no logo art is redrawn."""
    return f'''<svg class="stamp{extra}" viewBox="0 0 200 200" aria-hidden="true" focusable="false">
  <defs><path id="stamp-ring" d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0"/></defs>
  <circle cx="100" cy="100" r="96" fill="none" stroke="currentColor" stroke-width="3"/>
  <circle cx="100" cy="100" r="58" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text class="stamp__ring"><textPath href="#stamp-ring" startOffset="0">ANIL INDUSTRIES &#183; BAWANA DELHI &#183; EST. 1976 &#183;</textPath></text>
  <text class="stamp__mid" x="100" y="94" text-anchor="middle">SINCE</text>
  <text class="stamp__big" x="100" y="124" text-anchor="middle">1976</text>
</svg>'''


def ruler():
    """Thickness gauge: 0 to 4.50 mm, with both product ranges as bars (decorative; the
    numbers are always printed as text next to it)."""
    def pct(mm):
        return "%.3f%%" % (float(mm) / 4.5 * 100)

    labels = "".join(f'<span class="ruler__n" style="left:{pct(v)}">{v}{" mm" if v == "4.5" else ""}</span>'
                     for v in ["0", "0.5", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0", "4.5"])
    ht, cr = PRODUCTS["ht"], PRODUCTS["cr"]

    def bar(cls, prod, label):
        lo, hi = prod["thk"]
        w = "%.3f%%" % ((float(hi) - float(lo)) / 4.5 * 100)
        return (f'<div class="ruler__bar {cls}" style="left:{pct(lo)};width:{w}">'
                f'<span>{label} {lo} to {hi}</span></div>')

    return f'''<div class="ruler" aria-hidden="true">
  <div class="ruler__scale"></div>
  <div class="ruler__nums">{labels}</div>
  {bar("ruler__bar--ht", ht, "HT")}
  {bar("ruler__bar--cr", cr, "CR")}
  <div class="ruler__needle" hidden></div>
</div>'''


def dim(mm, prec):
    return f'<span class="dim" data-mm="{mm}" data-prec="{prec}">{mm}</span>'


def unit_toggle():
    return '''<div class="units js-only" role="group" aria-label="Units">
  <button type="button" class="units__btn" data-unit="mm" aria-pressed="true">mm</button>
  <button type="button" class="units__btn" data-unit="in" aria-pressed="false">inch</button>
</div>'''


def spec_fields(prod):
    lo, hi = prod["thk"]
    wlo, whi = prod["wid"]
    return f'''<dl class="fields">
  <div class="field field--wide"><dt>Thickness</dt><dd><span class="field__v">{dim(lo, 4)} to {dim(hi, 4)}</span> <span class="field__u" data-unit-label>mm</span></dd></div>
  <div class="field field--wide"><dt>Width</dt><dd><span class="field__v">{dim(wlo, 2)} to {dim(whi, 2)}</span> <span class="field__u" data-unit-label>mm</span></dd></div>
  <div class="field"><dt>Finish</dt><dd>{E(prod["finish"])}</dd></div>
  <div class="field"><dt>Edges</dt><dd>{E(prod["edges"])}</dd></div>
  <div class="field"><dt>Hardness</dt><dd>{E(prod["hardness"])}</dd></div>
  <div class="field"><dt>Grades</dt><dd>14 carbon and alloy grades, cross-referenced to 8 standards</dd></div>
</dl>'''


def size_check(p, idp="size"):
    ht, cr = PRODUCTS["ht"], PRODUCTS["cr"]
    return f'''<div class="sizecheck" id="{idp}">
  <form class="sizecheck__form js-only" data-sizecheck novalidate>
    <p class="sizecheck__title">Check your size</p>
    <div class="sizecheck__inputs">
      <label><span>Thickness (mm)</span><input type="number" name="t" step="0.01" min="0" inputmode="decimal" placeholder="e.g. 0.35"></label>
      <span class="sizecheck__x" aria-hidden="true">&#215;</span>
      <label><span>Width (mm)</span><input type="number" name="w" step="0.5" min="0" inputmode="decimal" placeholder="e.g. 32"></label>
      <button class="btn btn--ink" type="submit">Check</button>
    </div>
    <p class="sizecheck__out" aria-live="polite" data-sizecheck-out>Enter a thickness and width to see which strip covers it.</p>
  </form>
  <table class="ranges">
    <caption>Size ranges</caption>
    <thead><tr><th scope="col">Product</th><th scope="col">Thickness</th><th scope="col">Width</th></tr></thead>
    <tbody>
      <tr><th scope="row"><a href="{p}{ht["slug"]}">Hardened and tempered</a></th><td>{ht["thk"][0]} to {ht["thk"][1]} mm</td><td>{ht["wid"][0]} to {ht["wid"][1]} mm</td></tr>
      <tr><th scope="row"><a href="{p}{cr["slug"]}">Cold rolled</a></th><td>{cr["thk"][0]} to {cr["thk"][1]} mm</td><td>{cr["wid"][0]} to {cr["wid"][1]} mm</td></tr>
    </tbody>
  </table>
  <p class="note">1 mm = 0.03937 in. Sizes outside these ranges: ask us.</p>
</div>'''


def cta_band(p, title, text, product=None):
    q = f"?product={product}" if product else ""
    return f'''<section class="cta-band" aria-labelledby="cta-h">
  <div class="wrap cta-band__in">
    <div class="cta-band__copy">
      <p class="eyebrow eyebrow--on-dark">Request for quotation</p>
      <h2 id="cta-h">{title}</h2>
      <p>{text}</p>
    </div>
    <div class="cta-band__actions">
      <a class="btn btn--primary btn--lg" href="{p}contact/{q}">Request a quote</a>
      <p class="cta-band__alt">Or call <a href="tel:{ORG["phones"][0][1]}">{ORG["phones"][0][0]}</a></p>
    </div>
    {stamp(" stamp--band")}
  </div>
</section>'''


def crumbs(p, items):
    li = [f'<li><a href="{home_href(p)}">Home</a></li>']
    for label, href in items[:-1]:
        li.append(f'<li><a href="{p}{href}">{label}</a></li>')
    li.append(f'<li aria-current="page">{items[-1][0]}</li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(li)}</ol></nav>'


def page_hero(p, crumb_items, eyebrow, h1, lede, ref, actions="", extra="", cls=""):
    return f'''<section class="page-hero{cls}">
  <div class="wrap">
    <div class="page-hero__top">{crumbs(p, crumb_items)}<p class="page-hero__ref" aria-hidden="true">{ref}</p></div>
    <div class="page-hero__grid">
      <div class="page-hero__copy">
        <p class="eyebrow">{eyebrow}</p>
        <h1>{h1}</h1>
        <p class="lede">{lede}</p>
        {actions}
      </div>
      {extra}
    </div>
  </div>
</section>'''


def faq_items(items, open_first=False):
    out = []
    for i, (q, a) in enumerate(items):
        o = " open" if (open_first and i == 0) else ""
        out.append(f'''<details class="qa"{o}>
  <summary><span class="qa__n">Q{i + 1:02d}</span><span class="qa__q">{E(q)}</span></summary>
  <div class="qa__a"><p>{E(a)}</p></div>
</details>''')
    return "\n".join(out)


def eq_table(p, compact=False):
    cols = EQ_COLS
    head_cells = "".join(
        f'<th scope="col" data-col="{k}"><span class="th__std">{std}</span><span class="th__c">{country}</span></th>'
        for k, country, std in cols)
    rows = []
    rowset = EQ if not compact else [EQ[6], EQ[8], EQ[9], EQ[11], EQ[12]]
    for r in rowset:
        key = r[2] or r[1] or r[0]
        rid = "g-" + key.split(" / ")[0].replace(" ", "").lower()
        cells = [f'<th scope="row" class="eq__key">{E(key)}</th>']
        for i, (k, _, _) in enumerate(cols):
            v = r[i]
            cells.append(f'<td data-col="{k}">{E(v) if v else "<span class=\"nil\">not listed</span>"}</td>')
        q = quote(key.split(" / ")[0])
        if not compact:
            cells.append(f'<td class="eq__act"><a href="{p}contact/?grade={q}">Quote <span class="sr-only">{E(key)}</span></a></td>')
        rows.append(f'<tr id="{rid}">{"".join(cells)}</tr>')
    act_head = '<th scope="col" class="eq__act"><span class="sr-only">Action</span></th>' if not compact else ""
    return f'''<div class="tablewrap" tabindex="0" role="region" aria-label="Grade equivalents table, scrolls sideways">
<table class="matrix" id="eq-table" data-filterable>
  <caption class="sr-only">International equivalents of spring steel strip grades</caption>
  <thead><tr><th scope="col"><span class="th__key">Grade</span><span class="th__c">EN, DIN or SAE</span></th>{head_cells}{act_head}</tr></thead>
  <tbody>
  {"".join(rows)}
  </tbody>
</table>
</div>'''


def chem_table():
    head_cells = "".join(f'<th scope="col">{E(c)}</th>' for c in CHEM_COLS)
    rows = []
    for g, vals in CHEM:
        cells = "".join(f'<td>{E(v) if v else "<span class=\"nil\">&#183;</span>"}</td>' for v in vals)
        rows.append(f'<tr id="c-{g.replace(" ", "").lower()}"><th scope="row">{E(g)}</th>{cells}</tr>')
    return f'''<div class="tablewrap" tabindex="0" role="region" aria-label="Chemical composition table, scrolls sideways">
<table class="matrix matrix--chem" id="chem-table" data-filterable>
  <caption class="sr-only">Chemical composition by grade, percentage by weight</caption>
  <thead><tr><th scope="col">Grade</th>{head_cells}</tr></thead>
  <tbody>
  {"".join(rows)}
  </tbody>
</table>
</div>'''


def joinlist(items):
    return "; ".join([items[0]] + [x[0].lower() + x[1:] for x in items[1:]])


def process_line(full=True):
    items = []
    for i, (name, text) in enumerate(PROCESS):
        t = f'<p>{E(text)}</p>' if full else ""
        items.append(f'<li class="line__st"><span class="line__n">{i + 1:02d}</span><h3>{E(name)}</h3>{t}</li>')
    return f'<ol class="line{"" if full else " line--compact"}">{"".join(items)}</ol>'


# --------------------------------------------------------------------------------------------
# Schema helpers
# --------------------------------------------------------------------------------------------

ORG_ID = DOMAIN + "/#organization"


def org_node():
    uk = ORG["uk"]
    return {
        "@type": ["Organization", "LocalBusiness"],
        "@id": ORG_ID,
        "name": "Anil Industries",
        "alternateName": "Anil Industries, Bawana, Delhi",
        "url": DOMAIN + "/",
        "logo": DOMAIN + "/imgs/logo.webp",
        "image": DOMAIN + "/" + OG,
        "description": "Processor and supplier of cold rolled and hardened and tempered spring steel strips, "
                       "Bawana, Delhi, since 1976.",
        "foundingDate": ORG["founded"],
        "founder": {"@type": "Person", "name": ORG["founder_schema"]},
        "email": ORG["email"],
        "telephone": [t for _, t in ORG["phones"]],
        "address": {"@type": "PostalAddress", "streetAddress": ORG["street"], "addressLocality": ORG["locality"],
                    "postalCode": ORG["postcode"], "addressRegion": "Delhi", "addressCountry": "IN"},
        "geo": {"@type": "GeoCoordinates", "latitude": ORG["lat"], "longitude": ORG["lng"]},
        "areaServed": [{"@type": "Country", "name": "India"}, {"@type": "Country", "name": "United Kingdom"}],
        "contactPoint": [
            {"@type": "ContactPoint", "contactType": "sales", "telephone": ORG["phones"][0][1],
             "email": ORG["email"], "areaServed": "IN", "availableLanguage": ["en", "hi"]},
            {"@type": "ContactPoint", "contactType": "sales", "name": uk["name"],
             "telephone": uk["phone"][1], "areaServed": "GB", "availableLanguage": "en"},
        ],
        "knowsAbout": ["Hardened and tempered steel strip", "Cold rolled steel strip", "Spring steel strip",
                       "EN 10132", "C75S", "50CrV4", "75Ni8"],
    }


def page_node(slug, name, desc, typ="WebPage"):
    return {"@type": typ, "@id": DOMAIN + "/" + slug + "#webpage", "url": DOMAIN + "/" + slug,
            "name": name, "description": desc, "isPartOf": {"@id": DOMAIN + "/#website"},
            "about": {"@id": ORG_ID}, "inLanguage": "en-GB"}


def breadcrumb(items):
    els = [{"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"}]
    for i, (name, slug) in enumerate(items):
        els.append({"@type": "ListItem", "position": i + 2, "name": name, "item": DOMAIN + "/" + slug})
    return {"@type": "BreadcrumbList", "itemListElement": els}


def graph(*nodes):
    return {"@context": "https://schema.org", "@graph": list(nodes)}


def org_ref():
    return {"@type": "Organization", "@id": ORG_ID, "name": "Anil Industries"}


# --------------------------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------------------------

def rfq_starters():
    ht = ("Quote request: hardened and tempered strip",
          "Product: hardened and tempered steel strip\nGrade and standard:\nThickness and tolerance (mm):\n"
          "Width and tolerance (mm):\nFinish (scaleless grey / bright / blue, polished bright / blue / bronze / gold):\n"
          "Edge (slit / square / round):\nHardness (HRC, HV or tensile):\nCoil size or cut length:\n"
          "Quantity:\nDelivery location:\n\nName:\nCompany:\nPhone:\n")
    cr = ("Quote request: cold rolled strip",
          "Product: cold rolled steel strip\nGrade and standard:\nThickness and tolerance (mm):\n"
          "Width and tolerance (mm):\nSurface finish:\nCoil size or cut length:\nQuantity:\n"
          "Delivery location:\nWhat the part is:\n\nName:\nCompany:\nPhone:\n")
    gr = ("Grade question",
          "The grade on my drawing:\nThe standard it is specified to:\nWhat the part is:\n"
          "Thickness and width (mm):\n\nName:\nCompany:\n")
    ex = ("Export enquiry",
          "Country and port of delivery:\nProduct (hardened and tempered / cold rolled):\nGrade and standard:\n"
          "Thickness and width (mm):\nQuantity per order:\nDocuments you need with the shipment:\n\n"
          "Name:\nCompany:\nPhone:\n")
    return [
        ("Hardened and tempered strip", "Sizes, finish, edge and hardness checklist", mailto(*ht)),
        ("Cold rolled strip", "Sizes, finish and quantity checklist", mailto(*cr)),
        ("A grade question", "Send the grade on your drawing; we reply with the match", mailto(*gr)),
        ("Export enquiry", "Destination, documents and quantities", mailto(*ex)),
    ]


def page_home():
    p = ""
    ht, cr = PRODUCTS["ht"], PRODUCTS["cr"]
    title = "Spring Steel Strip Supplier, Delhi, since 1976 | Anil Industries"
    desc = ("Hardened and tempered spring steel strips and cold rolled high carbon strips from Bawana, "
            "Delhi, since 1976. C 45 to C 120, 50CrV4, 75Ni8. Request a quote.")
    why = [
        ("Fifty years in strip", f"Founded in 1976 by {ORG['founder']}. Steel strip is the whole business, not one line in a catalogue."),
        ("Processed, not just traded", "Our processing route runs from hot rolled coil to slit, packed strip. Hardened and tempered strip is treated in an inert atmosphere to avoid oxidation."),
        ("German raw material", "We source our raw material from German brands."),
        ("Hardness to your drawing", "Hardened and tempered strip is supplied in the hardness range your part needs, with the finish and edge you specify."),
        ("Grades in your language", "Every grade is cross-referenced to SAE / AISI, DIN, EN, BS, JIS, IS and GOST, so you can order against the standard on your drawing."),
        ("A contact in the UK", f"Buyers in the United Kingdom can reach {ORG['uk']['name']} in Pinner, Middlesex."),
    ]
    why_html = "".join(
        f'<li><span class="ledger__n">{i + 1:02d}</span><div><h3>{E(h)}</h3><p>{E(t)}</p></div></li>'
        for i, (h, t) in enumerate(why))

    def sheet(prod, key, uses):
        lo, hi = prod["thk"]
        wlo, whi = prod["wid"]
        return f'''<article class="sheet">
  <header class="sheet__head"><span class="sheet__doc">{prod["doc"]}</span><span class="sheet__kind">Product sheet</span></header>
  <div class="sheet__body">
    <div class="sheet__img"><img src="{p}{prod["img"]}" width="{prod["img_w"]}" height="{prod["img_h"]}" alt="{esc_attr(prod["img_alt"])}" loading="lazy" decoding="async"></div>
    <div class="sheet__main">
      <h3 class="sheet__title"><a href="{p}{prod["slug"]}">{prod["name"]}</a></h3>
      <dl class="fields fields--sheet">
        <div class="field"><dt>Thickness</dt><dd><span class="field__v">{lo} to {hi}</span> <span class="field__u">mm</span></dd></div>
        <div class="field"><dt>Width</dt><dd><span class="field__v">{wlo} to {whi}</span> <span class="field__u">mm</span></dd></div>
      </dl>
      <p class="sheet__uses"><span class="label">Used for</span> {E(uses)}</p>
      <p class="sheet__link"><a class="arrow-link" href="{p}{prod["slug"]}">Open the {prod["short"].lower()} spec sheet</a></p>
    </div>
  </div>
</article>'''

    body = f'''<main id="main">
<section class="hero">
  <div class="hero__stage">
  <div class="wrap hero__grid">
    <div class="hero__copy">
      <p class="eyebrow eyebrow--on-dark">Cold rolled and H&amp;T steel strip &#183; Bawana, Delhi &#183; Since 1976</p>
      <h1>Spring steel strip, processed to your specification.</h1>
      <p class="lede">Anil Industries processes and supplies cold rolled and hardened and tempered steel strip from 0.10 to 4.50 mm thick and 5 to 500 mm wide, in 14 carbon and alloy grades, for makers of saw blades, springs, compressor valves and automotive parts.</p>
      <div class="actions">
        <a class="btn btn--primary btn--lg" href="contact/">Request a quote</a>
        <a class="arrow-link arrow-link--on-dark" href="grades/">Find your grade</a>
      </div>
    </div>
    <figure class="hero__plate">
      <div class="hero__img"><img src="{ht["img"]}" width="{ht["img_w"]}" height="{ht["img_h"]}" alt="{esc_attr(ht["img_alt"])}" fetchpriority="high" decoding="async"></div>
      <figcaption class="plate">
        <span class="plate__head"><span>Spec plate</span><span>AI / 1976</span></span>
        <span class="plate__row"><span class="plate__k">Thickness</span><span class="plate__v">0.10 to 4.50 <small>mm</small></span></span>
        <span class="plate__row"><span class="plate__k">Width</span><span class="plate__v">5 to 500 <small>mm</small></span></span>
        <span class="plate__row plate__row--half"><span><span class="plate__k">Grades</span><span class="plate__v">14</span></span><span><span class="plate__k">Standards</span><span class="plate__v">8</span></span></span>
      </figcaption>
    </figure>
  </div>
  </div>
  <div class="wrap hero__ruler">
    <p class="hero__ruler-label"><span class="label">Thickness range</span> Hardened and tempered 0.10 to 4.00 mm. Cold rolled 0.20 to 4.50 mm.</p>
    {ruler()}
  </div>
  <div class="wrap">
    <ul class="intents">
      <li><a href="grades/"><span class="intents__n">01</span><span class="intents__t">Find a grade</span><span class="intents__d">C75S, CK 75, SAE 1075 or SK5: one table, eight standards.</span></a></li>
      <li><a href="#size"><span class="intents__n">02</span><span class="intents__t">Check your size</span><span class="intents__d">See which strip covers your thickness and width.</span></a></li>
      <li><a href="applications/"><span class="intents__n">03</span><span class="intents__t">Browse by part</span><span class="intents__d">Saw blades, valve plates, clutch springs, band knives.</span></a></li>
      <li><a href="contact/"><span class="intents__n">04</span><span class="intents__t">Request a quote</span><span class="intents__d">A spec-shaped form that opens your own email.</span></a></li>
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="h-products">
  <div class="wrap">
    {sec_head("01", "Products", "AI / HT + CR")}
    <div class="sec-intro">
      <h2 id="h-products">Two strips, one supplier</h2>
      <p>Choose hardened and tempered strip when the part must keep its spring hardness straight off the press. Choose cold rolled strip when you form heavily or harden the finished part yourself.</p>
    </div>
    <div class="sheets">
      {sheet(ht, "ht", "band, gang and circular saw blades, compressor valve plates, clutch springs, textile parts, band knives")}
      {sheet(cr, "cr", "hack saw and power saw blades, clutch parts, horn diaphragms, circlips, washers, surgical blades")}
    </div>
  </div>
</section>

<section class="section section--surface" aria-labelledby="h-size">
  <div class="wrap split">
    <div>
      {sec_head("02", "Size check")}
      <h2 id="h-size">Will your size run?</h2>
      <p>Thickness from 0.10 mm, width from 5 mm. Type your strip size and we will tell you which product covers it. For anything outside the range, ask: we will tell you plainly.</p>
    </div>
    {size_check(p)}
  </div>
</section>

<section class="section" aria-labelledby="h-grades">
  <div class="wrap">
    {sec_head("03", "Grades and equivalents", "AI / GR / 03")}
    <div class="sec-intro">
      <h2 id="h-grades">Order against the standard on your drawing</h2>
      <p>Your drawing may say CK 75, C75S, SAE 1075 or S75C. They are the same family of steel. Our cross-reference covers eight national standards; a few rows are below.</p>
    </div>
    {eq_table(p, compact=True)}
    <p class="more"><a class="arrow-link" href="grades/">See all grades, chemistry and equivalents</a></p>
  </div>
</section>

<section class="section section--surface" aria-labelledby="h-process">
  <div class="wrap">
    {sec_head("04", "Processing route", "AI / PR / 04")}
    <div class="sec-intro">
      <h2 id="h-process">From hot rolled coil to packed strip</h2>
      <p>Every coil follows the same route through our works, ending in packing built for transport: sealed, hooped, edge protected and wrapped in waterproof paper.</p>
    </div>
    {process_line(full=False)}
    <p class="more"><a class="arrow-link" href="quality/">How we process and check strip</a></p>
  </div>
</section>

<section class="section" aria-labelledby="h-why">
  <div class="wrap">
    {sec_head("05", "Why Anil Industries")}
    <div class="sec-intro">
      <h2 id="h-why">What you get from a strip specialist</h2>
      <p>Plain facts, no superlatives. If something here matters to your order, ask us to put it in writing on the quote.</p>
    </div>
    <ol class="ledger">{why_html}</ol>
  </div>
</section>

<section class="section section--ink" aria-labelledby="h-export">
  <div class="wrap split split--center">
    <div>
      <p class="eyebrow eyebrow--on-dark">Buying from outside India</p>
      <h2 id="h-export">A contact in the United Kingdom</h2>
      <p>UK buyers can speak to our contact in Pinner, Middlesex. Buyers anywhere else can write to the Delhi works directly.</p>
      <div class="actions"><a class="btn btn--light" href="contact/#uk">UK contact details</a><a class="arrow-link arrow-link--on-dark" href="mailto:{ORG["email"]}">Email Delhi</a></div>
    </div>
    <div class="card-uk">
      <p class="label label--on-dark">UK contact</p>
      <p class="card-uk__name">{ORG["uk"]["name"]}</p>
      <p>{", ".join(ORG["uk"]["lines"])}</p>
      <p><a href="tel:{ORG["uk"]["phone"][1]}">{ORG["uk"]["phone"][0]}</a></p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="h-faq">
  <div class="wrap split">
    <div>
      {sec_head("06", "Questions")}
      <h2 id="h-faq">What buyers ask first</h2>
      <p><a class="arrow-link" href="faq/">All questions</a></p>
    </div>
    <div class="qas">{faq_items([FAQ[1], FAQ[2], FAQ[5], FAQ[7]])}</div>
  </div>
</section>

{cta_band(p, "Send us your drawing or your spec", "Grade, size, finish, edge, hardness and quantity. We reply with a quote by email.")}
</main>
'''
    schema = graph(
        org_node(),
        {"@type": "WebSite", "@id": DOMAIN + "/#website", "url": DOMAIN + "/", "name": "Anil Industries",
         "publisher": {"@id": ORG_ID}, "inLanguage": "en-GB"},
        page_node("", title, desc),
    )
    return dict(slug="", title=title, desc=desc, schema=schema, active="home", body=body,
                preload=f'<link rel="preload" href="{ht["img"]}" as="image" type="image/webp">\n')


def product_page(key):
    prod = PRODUCTS[key]
    p = "../"
    other = PRODUCTS["cr" if key == "ht" else "ht"]
    if key == "ht":
        title = "Hardened and Tempered Spring Steel Strips | Anil Industries"
        desc = ("Hardened and tempered spring steel strip, 0.10 to 4.00 mm thick, 5 to 500 mm wide. "
                "Grey, bright, blue, bronze or gold finish. C 75, C 80, SK85, 75Ni8.")
        h1 = "Hardened and tempered spring steel strips"
        lede = ("Steel strip that is heated above the critical transformation temperature for its grade, "
                "quenched, then tempered in an inert atmosphere to avoid oxidation. It arrives with its "
                "spring properties set, ready to blank or form.")
        apps = [a for a in APPLICATIONS if a[2]]
        app_list = "".join(f'<li><h3><a href="{p}applications/#{a[0]}">{E(a[1])}</a></h3><p>{E(joinlist(a[2]))}.</p></li>' for a in apps)
        finishes = [("Scaleless grey", "fin-grey"), ("Scaleless bright", "fin-bright"), ("Scaleless blue", "fin-blue"),
                    ("Polished bright", "fin-pbright"), ("Polished blue", "fin-pblue"), ("Polished bronze", "fin-bronze"),
                    ("Polished gold", "fin-gold")]
        fin_html = "".join(f'<li><span class="swatch {c}" aria-hidden="true"></span>{n}</li>' for n, c in finishes)
        detail = f'''
<section class="block" aria-labelledby="h-process-ht">
  {sec_head("02", "Process")}
  <h2 id="h-process-ht">How the strip is hardened and tempered</h2>
  <ol class="steps">
    <li><span class="steps__n">01</span><div><h3>Harden</h3><p>The strip is heated above the critical transformation temperature for its grade.</p></div></li>
    <li><span class="steps__n">02</span><div><h3>Quench</h3><p>It is cooled rapidly, which makes it fully hard.</p></div></li>
    <li><span class="steps__n">03</span><div><h3>Temper</h3><p>It is reheated to a lower temperature and held there for a set time, trading a little hardness for toughness and spring.</p></div></li>
    <li><span class="steps__n">04</span><div><h3>Protect</h3><p>All of this happens in an inert atmosphere, so the surface does not oxidise.</p></div></li>
  </ol>
</section>

<section class="block" aria-labelledby="h-finish">
  {sec_head("03", "Finish and edge")}
  <h2 id="h-finish">Seven finishes, three edges</h2>
  <div class="temper" aria-hidden="true"></div>
  <p>Scaleless strip keeps the surface it comes out of tempering with. Polished strip is brought up bright, then left bright or coloured blue, bronze or gold.</p>
  <ul class="finishes">{fin_html}</ul>
  <dl class="fields fields--3">
    <div class="field"><dt>Slit edge</dt><dd>The cut edge as it comes off the slitter</dd></div>
    <div class="field"><dt>Square edge</dt><dd>The edge dressed square across the thickness</dd></div>
    <div class="field"><dt>Round edge</dt><dd>The edge dressed to a rounded profile</dd></div>
  </dl>
</section>

<section class="block" aria-labelledby="h-apps">
  {sec_head("04", "Applications")}
  <h2 id="h-apps">What our hardened and tempered strip becomes</h2>
  <ul class="applist">{app_list}</ul>
</section>'''
        faqs = [FAQ[0], FAQ[5], FAQ[6], FAQ[1]]
    else:
        title = "Cold Rolled High Carbon Steel Strips | Anil Industries"
        desc = ("Cold rolled high carbon steel strip, 0.20 to 4.50 mm thick, 12.5 to 450 mm wide, in C 45 "
                "to C 120, 50CrV4 and 75Ni8. For saw blades, clutches and circlips.")
        h1 = "Cold rolled high carbon steel strips"
        lede = ("Hot rolled steel processed further in cold reduction mills at room temperature, followed by "
                "annealing and/or temper rolling. The result is strip with a wide range of surface finish "
                "and closer thickness tolerances.")
        apps = [a for a in APPLICATIONS if a[3]]
        app_list = "".join(f'<li><h3><a href="{p}applications/#{a[0]}">{E(a[1])}</a></h3><p>{E(joinlist(a[3]))}.</p></li>' for a in apps)
        detail = f'''
<section class="block" aria-labelledby="h-props">
  {sec_head("02", "Properties")}
  <h2 id="h-props">What cold rolling gives you</h2>
  <ol class="steps">
    <li><span class="steps__n">01</span><div><h3>Surface</h3><p>A wide range of surface finishes, from the rolls rather than from polishing.</p></div></li>
    <li><span class="steps__n">02</span><div><h3>Tolerance</h3><p>Closer thickness tolerances than hot rolled strip.</p></div></li>
    <li><span class="steps__n">03</span><div><h3>Strength</h3><p>High tensile strength, yield strength and hardness, with a corresponding decrease in ductility.</p></div></li>
  </ol>
</section>

<section class="block" aria-labelledby="h-apps">
  {sec_head("03", "Applications")}
  <h2 id="h-apps">What our cold rolled strip becomes</h2>
  <ul class="applist">{app_list}</ul>
</section>

<section class="block" aria-labelledby="h-crca">
  {sec_head("04", "Not CRCA")}
  <h2 id="h-crca">Cold rolled spring steel, not CRCA</h2>
  <p>In India, CRCA usually means cold rolled close annealed low carbon steel for car bodies and appliances. Our cold rolled strip is high carbon and alloy steel, from C 45 to C 120 and 50CrV4 to 75Ni8, for parts that are hardened. If you need the part ready-hardened, see <a href="{p}{other["slug"]}">hardened and tempered strip</a>.</p>
</section>'''
        faqs = [FAQ[1], FAQ[7], FAQ[2], FAQ[10]]

    crumbs_items = [(prod["name"], prod["slug"])]
    hero = page_hero(
        p, crumbs_items, "Product sheet &#183; " + prod["doc"], h1, lede, prod["doc"] + " &#183; Rev. " + YEAR,
        actions=f'<div class="actions"><a class="btn btn--primary btn--lg" href="{p}contact/?product={key}">Request a quote</a><a class="arrow-link" href="{p}grades/">Grades and equivalents</a></div>',
        extra=f'<div class="page-hero__img"><img src="{p}{prod["img"]}" width="{prod["img_w"]}" height="{prod["img_h"]}" alt="{esc_attr(prod["img_alt"])}" fetchpriority="high" decoding="async"></div>',
        cls=" page-hero--ht" if key == "ht" else "")
    body = f'''<main id="main">
{hero}
<div class="wrap docgrid">
  <div class="docgrid__main">
    <section class="block" aria-labelledby="h-spec">
      <div class="block__bar">{sec_head("01", "Specification")}{unit_toggle()}</div>
      <h2 id="h-spec">Specification</h2>
      {spec_fields(prod)}
      {ruler()}
      <p class="note">Grades: see the full chemistry and international equivalents on the <a href="{p}grades/">grades page</a>. Tell us which grade and standard your drawing calls for.</p>
    </section>
    {detail}
    <section class="block" aria-labelledby="h-qa">
      {sec_head("05", "Questions")}
      <h2 id="h-qa">Questions about {prod["short"].lower()} strip</h2>
      <div class="qas">{faq_items(faqs)}</div>
    </section>
  </div>
  <aside class="rail" aria-label="Specification summary">
    <div class="rail__in">
      <p class="rail__doc">{prod["doc"]}</p>
      <p class="rail__name">{prod["name"]}</p>
      <dl class="rail__list">
        <div><dt>Thickness</dt><dd>{prod["thk"][0]} to {prod["thk"][1]} mm</dd></div>
        <div><dt>Width</dt><dd>{prod["wid"][0]} to {prod["wid"][1]} mm</dd></div>
        <div><dt>Edges</dt><dd>{E(prod["edges"])}</dd></div>
        <div><dt>Grades</dt><dd>14, 8 standards</dd></div>
      </dl>
      <a class="btn btn--primary btn--block" href="{p}contact/?product={key}">Request a quote for this</a>
      <button class="btn btn--ghost btn--block js-only" type="button" data-print>Print this spec sheet</button>
      {stamp(" stamp--rail")}
    </div>
  </aside>
</div>
{cta_band(p, "Quote for " + prod["short"].lower() + " strip", "Send the grade, thickness, width, finish, edge and quantity. We reply by email.", key)}
</main>
'''
    schema = graph(
        org_ref(),
        page_node(prod["slug"], title, desc),
        {"@type": "Product", "@id": DOMAIN + "/" + prod["slug"] + "#product", "name": prod["name"],
         "description": lede, "image": DOMAIN + "/" + prod["img"], "category": "Steel strip",
         "material": "Carbon and alloy spring steel", "brand": {"@id": ORG_ID},
         "manufacturer": {"@id": ORG_ID},
         "additionalProperty": [
             {"@type": "PropertyValue", "name": "Thickness", "minValue": float(prod["thk"][0]),
              "maxValue": float(prod["thk"][1]), "unitCode": "MMT"},
             {"@type": "PropertyValue", "name": "Width", "minValue": float(prod["wid"][0]),
              "maxValue": float(prod["wid"][1]), "unitCode": "MMT"}]},
        breadcrumb([(prod["name"], prod["slug"])]),
    )
    return dict(slug=prod["slug"], title=title, desc=desc, schema=schema, active=key, body=body)


def page_grades():
    p = "../"
    title = "Spring Steel Grades and Equivalents: C75, CK75, SK5, 1075"
    desc = ("Cross-reference spring steel strip grades across SAE / AISI, DIN, EN 10132, BS, JIS, IS and "
            "GOST. Find the equivalent of C75, CK75, SK5, 50CrV4 and 75Ni8.")
    toggles = "".join(
        f'<label class="chip"><input type="checkbox" data-col-toggle="{k}" checked><span>{std}</span></label>'
        for k, _, std in EQ_COLS)
    body = f'''<main id="main">
{page_hero(p, [("Grades and equivalents", "grades/")], "Reference &#183; AI / GR / 03",
           "Spring steel strip grades and international equivalents",
           "Fourteen carbon and alloy grades with their chemistry, and a cross-reference to eight national standards. Type any grade name to find its row.",
           "AI / GR / 03 &#183; Rev. " + YEAR)}
<section class="section section--tight" aria-labelledby="h-eq">
  <div class="wrap">
    {sec_head("01", "Equivalents")}
    <div class="sec-intro">
      <h2 id="h-eq">International standards reference</h2>
      <p>Each row is one family of steel as named in eight systems. Older names such as CK 75 (DIN 17222) and CS 80 (BS 1449) are still what many drawings say; the current European name is the EN 10132 column.</p>
    </div>
    <div class="finder js-only">
      <label class="finder__search"><span class="label">Find a grade</span><input type="search" id="grade-q" placeholder="SK5, C75S, CK 75, 1095, 50HGFA" autocomplete="off" spellcheck="false"></label>
      <fieldset class="finder__cols"><legend class="label">Show standards</legend>{toggles}</fieldset>
      <p class="finder__count" id="grade-count" aria-live="polite"></p>
    </div>
    {eq_table(p)}
    <p class="note">Equivalents are close, not identical: always compare chemistry. "Not listed" means the standard has no direct equivalent in our reference.</p>
  </div>
</section>

<section class="section section--surface section--tight" aria-labelledby="h-chem">
  <div class="wrap">
    {sec_head("02", "Chemistry")}
    <div class="sec-intro">
      <h2 id="h-chem">Chemical composition by grade</h2>
      <p>Percentage by weight. Silicon, sulphur and phosphorus are maximum values unless a range is shown.</p>
    </div>
    {chem_table()}
  </div>
</section>

<section class="section section--tight" aria-labelledby="h-read">
  <div class="wrap split">
    <div>
      {sec_head("03", "Reading the names")}
      <h2 id="h-read">Old names, new names</h2>
    </div>
    <dl class="fields fields--2">
      <div class="field"><dt>DIN 17222 &#8594; EN 10132</dt><dd>The German CK grades (CK 75) became the European C..S grades (C75S).</dd></div>
      <div class="field"><dt>JIS SK5 &#8594; SK85</dt><dd>Japan renamed its carbon tool steels by carbon content: SK5 is now SK85, SK4 is SK95.</dd></div>
      <div class="field"><dt>BS 1449 and BS 970</dt><dd>British names such as CS 80 and EN 42J still appear on drawings and are listed in our table.</dd></div>
      <div class="field"><dt>SAE / AISI</dt><dd>The four digit US numbers: 10xx for plain carbon, 6150 for chromium vanadium.</dd></div>
    </dl>
  </div>
</section>
{cta_band(p, "Quote against your grade", "Tell us the grade and the standard on your drawing, and the size you need.")}
</main>
'''
    schema = graph(org_ref(), page_node("grades/", title, desc), breadcrumb([("Grades and equivalents", "grades/")]))
    return dict(slug="grades/", title=title, desc=desc, schema=schema, active="grades", body=body)


def page_applications():
    p = "../"
    title = "Spring Steel Strip for Saw Blades, Valves and Springs"
    desc = ("Steel strip for band saw, hack saw and gang saw blades, compressor flapper valves, clutch "
            "springs, circlips, shims, surgical blades and band knives.")
    chips = "".join(f'<li><a href="#{a[0]}">{E(a[1])}</a></li>' for a in APPLICATIONS)
    arts = []
    for i, (aid, name, htl, crl) in enumerate(APPLICATIONS):
        cols = []
        if htl:
            cols.append(f'<div class="app__col"><p class="label">From hardened and tempered strip</p><ul>{"".join("<li>" + E(x) + "</li>" for x in htl)}</ul><a class="arrow-link" href="{p}{PRODUCTS["ht"]["slug"]}">Hardened and tempered spec</a></div>')
        if crl:
            cols.append(f'<div class="app__col"><p class="label">From cold rolled strip</p><ul>{"".join("<li>" + E(x) + "</li>" for x in crl)}</ul><a class="arrow-link" href="{p}{PRODUCTS["cr"]["slug"]}">Cold rolled spec</a></div>')
        arts.append(f'''<article class="app" id="{aid}" aria-labelledby="{aid}-h">
  <header class="app__head"><span class="app__n">{i + 1:02d}</span><h2 id="{aid}-h">{E(name)}</h2></header>
  <div class="app__cols">{"".join(cols)}</div>
</article>''')
    body = f'''<main id="main">
{page_hero(p, [("Applications", "applications/")], "Applications &#183; AI / AP / 04",
           "Where our steel strip is used",
           "Pick what you make. Each entry shows the parts our customers make from hardened and tempered strip and from cold rolled strip.",
           "AI / AP / 04 &#183; Rev. " + YEAR)}
<section class="section section--tight">
  <div class="wrap">
    <nav class="finder-chips" aria-label="What are you making?"><p class="label">What are you making?</p><ul>{chips}</ul></nav>
    <div class="apps">{"".join(arts)}</div>
  </div>
</section>
{cta_band(p, "Making something not listed here?", "Send us a drawing or a sample description and we will suggest the strip.")}
</main>
'''
    schema = graph(org_ref(), page_node("applications/", title, desc), breadcrumb([("Applications", "applications/")]))
    return dict(slug="applications/", title=title, desc=desc, schema=schema, active="applications", body=body)


def page_quality():
    p = "../"
    title = "Quality and Process | Anil Industries Steel Strips"
    desc = ("How Anil Industries processes spring steel strip in Delhi, how coils are packed, and what to "
            "specify when you order: grade, size, hardness, finish and edge.")
    work_to = ["Accurate dimensions and close tolerances", "Processing in line with each customer's requirements",
               "Cutting and edge preparation for reliable function", "Good forming properties",
               "Uniform hardening structure and the best possible spring properties",
               "A uniform, clean, defect-free surface"]
    objectives = ["Monitor and improve operational performance", "Reduce rework", "Reduce rejections",
                  "Improve productivity", "Raise customer satisfaction through our quality policy",
                  "Deliver defect-free products on time", "Increase training hours per employee every year"]
    pack = "".join(f'<li><span class="ledger__n">{i + 1:02d}</span><div><h3>{E(x)}</h3></div></li>' for i, x in enumerate(PACKING))
    body = f'''<main id="main">
{page_hero(p, [("Quality and process", "quality/")], "Quality &#183; AI / QA / 05",
           "How we process and check every coil",
           "The route our strip takes through the Bawana works, what we work to at each step, and how coils are packed for the journey to you.",
           "AI / QA / 05 &#183; Rev. " + YEAR)}
<section class="section section--tight" aria-labelledby="h-route">
  <div class="wrap">
    {sec_head("01", "Processing route", "AI / PR / 04")}
    <div class="sec-intro">
      <h2 id="h-route">The processing route</h2>
      <p>Annealing and cold rolling repeat until the strip reaches the thickness you ordered. Hardened and tempered strip then goes through hardening, quenching and tempering in an inert atmosphere before it is finished and edged.</p>
    </div>
    {process_line(full=True)}
    <figure class="diagram">
      <a href="{p}imgs/steel-coil-processing-flowchart.webp"><img src="{p}imgs/steel-coil-processing-flowchart-760.webp" srcset="{p}imgs/steel-coil-processing-flowchart-760.webp 760w, {p}imgs/steel-coil-processing-flowchart.webp 1448w" sizes="(min-width: 1060px) 980px, calc(100vw - 50px)" width="1448" height="1086" alt="Illustrated flowchart of the processing route: 1 raw material hot rolled slitting, 2 scale breaking and slitting, 3 acid pickling, 4 annealing, 5 cold rolling, 6 skin passing, 7 cold rolled slitting, 8 packing and dispatch, with the packed coil showing its seal, edge protector, steel hoop, metal protector, protective steel sheet and waterproof paper" loading="lazy" decoding="async"></a>
      <figcaption>Our processing route, from hot rolled coil to a coil packed for dispatch. Select the image to open it full size.</figcaption>
    </figure>
  </div>
</section>

<section class="section section--surface section--tight" aria-labelledby="h-workto">
  <div class="wrap split">
    <div>
      {sec_head("02", "What we work to")}
      <h2 id="h-workto">Processing policy</h2>
      <p>The standards we hold every coil to before it leaves the works.</p>
    </div>
    <ul class="checks">{"".join("<li>" + E(x) + "</li>" for x in work_to)}</ul>
  </div>
</section>

<section class="section section--tight" aria-labelledby="h-obj">
  <div class="wrap split">
    <div>
      {sec_head("03", "Quality objectives")}
      <h2 id="h-obj">What we keep improving</h2>
      <p>Objectives, not boasts: these are the measures we manage the works by.</p>
    </div>
    <ul class="checks">{"".join("<li>" + E(x) + "</li>" for x in objectives)}</ul>
  </div>
</section>

<section class="section section--surface section--tight" aria-labelledby="h-pack">
  <div class="wrap">
    {sec_head("04", "Packing")}
    <div class="sec-intro">
      <h2 id="h-pack">How coils are packed</h2>
      <p>Six layers of protection on every coil, so strip arrives flat, clean and dry.</p>
    </div>
    <ol class="ledger ledger--3">{pack}</ol>
  </div>
</section>

<section class="section section--tight" aria-labelledby="h-creds">
  <div class="wrap">
    {sec_head("05", "Credentials")}
    <div class="sec-intro">
      <h2 id="h-creds">Certificates and registrations</h2>
      <p>We only publish what we can show you. The items below are being confirmed and will be listed with their numbers before this site goes live.</p>
    </div>
    <ul class="tbc">
      <li><span class="label">To be confirmed</span>Quality management certification</li>
      <li><span class="label">To be confirmed</span>Test certificate type supplied with each coil</li>
      <li><span class="label">To be confirmed</span>Business registrations</li>
    </ul>
  </div>
</section>
{cta_band(p, "Need it in writing?", "Ask for tolerances, hardness and documents on your quote.")}
</main>
'''
    schema = graph(org_ref(), page_node("quality/", title, desc), breadcrumb([("Quality and process", "quality/")]))
    return dict(slug="quality/", title=title, desc=desc, schema=schema, active="quality", body=body)


def page_about():
    p = "../"
    title = "About Anil Industries | Steel Strip Supplier since 1976"
    desc = ("Anil Industries has processed and supplied cold rolled and hardened and tempered steel strips "
            "from Delhi since 1976, with a UK contact in Pinner for export buyers.")
    body = f'''<main id="main">
{page_hero(p, [("About", "about/")], "About &#183; Est. 1976",
           "Steel strip specialists in Delhi since 1976",
           f"Anil Industries was founded in 1976 by {ORG['founder']}. Fifty years on, we still do one thing: process and supply steel strip for the people who make blades, springs and precision parts.",
           "AI / AB / 06 &#183; Rev. " + YEAR)}
<section class="section section--tight" aria-labelledby="h-story">
  <div class="wrap yearrail">
    <ol class="yearrail__rail" aria-label="Milestones">
      <li><span class="yearrail__y">1976</span><span>Founded by {ORG["founder"]}</span></li>
      <li><span class="yearrail__y">2026</span><span>Fifty years in steel strip</span></li>
    </ol>
    <div class="yearrail__body">
      {sec_head("01", "Our story")}
      <h2 id="h-story">Fifty years of one product</h2>
      <p>Since 1976 we have supplied steel strip, and over the years our focus has settled on spring steel strip: cold rolled, and hardened and tempered. Our aim is simple: to be the dependable source our customers come back to for both.</p>
      <p>We keep improving how we work. We source our raw material from German brands and seek expert advice on process and direction. We are widening our markets and the range of customers we serve, in India and abroad.</p>
      <p>Our team takes responsibility at every level for finding the right solution, and works from what each customer actually needs.</p>
    </div>
  </div>
</section>

<section class="section section--surface section--tight" aria-labelledby="h-vm">
  <div class="wrap">
    {sec_head("02", "Vision and mission")}
    <h2 id="h-vm" class="sr-only">Vision and mission</h2>
    <dl class="fields fields--2 fields--big">
      <div class="field"><dt>Vision</dt><dd>To be a recognised name in the global steel industry for smart steel products, modern technology and high quality service.</dd></div>
      <div class="field"><dt>Mission</dt><dd>To keep evolving with the times: strengthening our products and services, and keeping every member of the team up to date with the latest developments in our industry.</dd></div>
    </dl>
  </div>
</section>

<section class="section section--tight" aria-labelledby="h-where">
  <div class="wrap split">
    <div>
      {sec_head("03", "Where we are")}
      <h2 id="h-where">Bawana, Delhi, and a contact in the UK</h2>
      <p>Our works are in the DSIDC Bawana Industrial Area in north west Delhi. Note the name: we are Anil Industries of Bawana, Delhi, and not connected with other companies of a similar name.</p>
    </div>
    <dl class="fields fields--2">
      <div class="field"><dt>Delhi works</dt><dd>{E(ORG["street"])}, {ORG["locality"]} {ORG["postcode"]}, India<br><a href="{MAPS_URL}">Open in Google Maps</a></dd></div>
      <div class="field"><dt>UK contact</dt><dd>{ORG["uk"]["name"]}, {", ".join(ORG["uk"]["lines"])}</dd></div>
    </dl>
  </div>
</section>

<section class="section section--surface section--tight" aria-labelledby="h-creds">
  <div class="wrap">
    {sec_head("04", "Credentials and compliance")}
    <div class="sec-intro">
      <h2 id="h-creds">Credentials and compliance</h2>
      <p>We publish only what can be verified. Business certifications are being confirmed and will be listed with their numbers before this site goes live.</p>
    </div>
    <ul class="tbc">
      <li><span class="label">To be confirmed</span>Quality management certification</li>
      <li><span class="label">To be confirmed</span>Business registrations</li>
      <li><span class="label label--ok">Verified</span>This website meets WCAG 2.1 AA, sets no cookies and makes no third-party requests</li>
    </ul>
  </div>
</section>
{cta_band(p, "Work with a strip specialist", "Tell us what you make and the strip you need.")}
</main>
'''
    schema = graph(org_node(), page_node("about/", title, desc, "AboutPage"), breadcrumb([("About", "about/")]))
    return dict(slug="about/", title=title, desc=desc, schema=schema, active="about", body=body)


def page_faq():
    p = "../"
    title = "Spring Steel Strip FAQ: Grades, Hardness and Finishes"
    desc = ("Answers on hardened and tempered strip: grades, equivalents, hardness, finishes, edges, cold "
            "rolled vs hardened and tempered, packing, and how to order.")
    body = f'''<main id="main">
{page_hero(p, [("Questions", "faq/")], "Questions &#183; AI / QA / 07",
           "Questions about spring steel strip",
           "Straight answers on grades, equivalents, hardness, finishes and ordering. If yours is not here, ask us.",
           "AI / FQ / 07 &#183; Rev. " + YEAR)}
<section class="section section--tight" aria-labelledby="h-all">
  <div class="wrap narrow">
    <h2 id="h-all" class="sr-only">All questions</h2>
    <div class="qas">{faq_items(FAQ, open_first=True)}</div>
  </div>
</section>
{cta_band(p, "Still have a question?", "Email us the grade or part you are working on.")}
</main>
'''
    schema = graph(
        org_ref(), page_node("faq/", title, desc, "FAQPage") | {
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in FAQ]},
        breadcrumb([("Questions", "faq/")]))
    return dict(slug="faq/", title=title, desc=desc, schema=schema, active="faq", body=body)


def page_contact():
    p = "../"
    title = "Request a Quote for Steel Strips | Anil Industries, Delhi"
    desc = ("Send your grade, thickness, width, finish and quantity for a quote. Anil Industries, L-125 "
            "Sector 2, DSIDC Bawana, Delhi 110039. UK contact in Pinner.")
    grades = "".join(f'<option value="{E(g)}"></option>' for g, _ in CHEM)
    starters = "".join(
        f'<li><a href="{href}"><span class="starter__t">{E(t)}</span><span class="starter__d">{E(d)}</span></a></li>'
        for t, d, href in rfq_starters())
    uk = ORG["uk"]
    phones = "".join(f'<li><a href="tel:{t}">{d}</a></li>' for d, t in ORG["phones"])
    checklist = ("Grade and standard\nThickness and tolerance (mm)\nWidth and tolerance (mm)\nFinish\nEdge\n"
                 "Hardness (HRC, HV or tensile)\nCoil size or cut length\nQuantity\nDelivery location")
    body = f'''<main id="main">
{page_hero(p, [("Request a quote", "contact/")], "Request for quotation &#183; AI / RFQ",
           "Request a quote",
           "Fill in what you know. The form opens your own email app with a complete request addressed to us; nothing is stored on this website.",
           "AI / RFQ &#183; Rev. " + YEAR)}
<section class="section section--tight" aria-labelledby="h-rfq">
  <div class="wrap docgrid">
    <div class="docgrid__main">
      <h2 id="h-rfq" class="sr-only">Quote request form</h2>
      <form class="rfq" action="mailto:{ORG["email"]}?subject=Quote%20request" method="post" enctype="text/plain" data-rfq>
        <fieldset>
          <legend><span class="folio__num">A</span> Material</legend>
          <div class="rfq__grid">
            <label class="rfq__f"><span>Product</span>
              <select name="Product" data-k="product">
                <option value="">Not sure yet</option>
                <option value="Hardened and tempered strip" data-key="ht">Hardened and tempered strip</option>
                <option value="Cold rolled strip" data-key="cr">Cold rolled strip</option>
              </select></label>
            <label class="rfq__f"><span>Grade</span><input name="Grade" data-k="grade" list="grade-list" placeholder="C 75, 75Ni8, SK85" autocomplete="off"></label>
            <datalist id="grade-list">{grades}</datalist>
            <label class="rfq__f"><span>Standard on your drawing</span><input name="Standard" data-k="standard" placeholder="EN 10132, DIN, SAE, JIS"></label>
            <label class="rfq__f"><span>Hardness</span><input name="Hardness" data-k="hardness" placeholder="HRC, HV or tensile range"></label>
          </div>
        </fieldset>
        <fieldset>
          <legend><span class="folio__num">B</span> Size and finish</legend>
          <div class="rfq__grid">
            <label class="rfq__f"><span>Thickness (mm)</span><input name="Thickness mm" data-k="thk" inputmode="decimal" placeholder="e.g. 0.35"></label>
            <label class="rfq__f"><span>Thickness tolerance</span><input name="Thickness tolerance" data-k="thktol" placeholder="plus or minus, mm"></label>
            <label class="rfq__f"><span>Width (mm)</span><input name="Width mm" data-k="wid" inputmode="decimal" placeholder="e.g. 32"></label>
            <label class="rfq__f"><span>Width tolerance</span><input name="Width tolerance" data-k="widtol" placeholder="plus or minus, mm"></label>
            <label class="rfq__f"><span>Finish</span>
              <select name="Finish" data-k="finish">
                <option value="">Not sure yet</option>
                <option>Scaleless grey</option><option>Scaleless bright</option><option>Scaleless blue</option>
                <option>Polished bright</option><option>Polished blue</option><option>Polished bronze</option><option>Polished gold</option>
                <option>Cold rolled surface</option>
              </select></label>
            <label class="rfq__f"><span>Edge</span>
              <select name="Edge" data-k="edge">
                <option value="">Not sure yet</option><option>Slit</option><option>Square</option><option>Round</option>
              </select></label>
          </div>
        </fieldset>
        <fieldset>
          <legend><span class="folio__num">C</span> Order</legend>
          <div class="rfq__grid">
            <label class="rfq__f"><span>Coil size or cut length</span><input name="Form" data-k="form" placeholder="Coil ID / OD, or length in mm"></label>
            <label class="rfq__f"><span>Quantity</span><input name="Quantity" data-k="qty" placeholder="kg or coils, per order or per month"></label>
            <label class="rfq__f rfq__f--wide"><span>Delivery location</span><input name="Delivery" data-k="dest" placeholder="City and country"></label>
            <label class="rfq__f rfq__f--wide"><span>What the part is (optional)</span><input name="Part" data-k="part" placeholder="Band saw blade, valve plate, clutch spring"></label>
          </div>
        </fieldset>
        <fieldset>
          <legend><span class="folio__num">D</span> You</legend>
          <div class="rfq__grid">
            <label class="rfq__f"><span>Name</span><input name="Name" data-k="name" autocomplete="name"></label>
            <label class="rfq__f"><span>Company</span><input name="Company" data-k="company" autocomplete="organization"></label>
            <label class="rfq__f"><span>Phone (optional)</span><input name="Phone" data-k="phone" type="tel" autocomplete="tel"></label>
          </div>
        </fieldset>
        <div class="rfq__submit">
          <button class="btn btn--primary btn--lg" type="submit">Open my email with this request</button>
          <p class="note">Your email app opens with the request filled in, addressed to {ORG["email"]}. Review it and press send. This site stores nothing.</p>
        </div>
      </form>
      <div class="checklist">
        <p class="label">Prefer to write your own email? Include:</p>
        <pre id="rfq-checklist">{E(checklist)}</pre>
        <button class="btn btn--ghost btn--sm js-only" type="button" data-copy="#rfq-checklist">Copy this checklist</button>
      </div>
    </div>
    <aside class="rail rail--contact" aria-label="Contact details">
      <div class="rail__in">
        <p class="rail__doc">Delhi works</p>
        <address>{E(ORG["street"])},<br>{ORG["locality"]} {ORG["postcode"]}, India</address>
        <ul class="rail__links">{phones}<li><a href="mailto:{ORG["email"]}">{ORG["email"]}</a></li><li><a href="{MAPS_URL}">Open in Google Maps</a></li></ul>
        <div class="rail__sep" id="uk">
          <p class="rail__doc">UK contact</p>
          <address>{uk["name"]}<br>{"<br>".join(uk["lines"])}</address>
          <ul class="rail__links"><li><a href="tel:{uk["phone"][1]}">{uk["phone"][0]}</a></li></ul>
        </div>
      </div>
    </aside>
  </div>
</section>
<section class="section section--surface section--tight" aria-labelledby="h-starters">
  <div class="wrap">
    {sec_head("E", "Email starters")}
    <div class="sec-intro">
      <h2 id="h-starters">Or start from a ready email</h2>
      <p>Each link opens your email app with a subject and a checklist of the details we need for that kind of request.</p>
    </div>
    <ul class="starters">{starters}</ul>
  </div>
</section>
</main>
'''
    schema = graph(org_node(), page_node("contact/", title, desc, "ContactPage"), breadcrumb([("Request a quote", "contact/")]))
    return dict(slug="contact/", title=title, desc=desc, schema=schema, active="contact", body=body)


def page_404():
    p = "/"
    title = "Page not found | Anil Industries"
    desc = "This page does not exist. Find spring steel strip, grades and quote requests from Anil Industries, Delhi."
    body = f'''<main id="main">
<section class="notfound">
  <div class="wrap">
    <p class="eyebrow eyebrow--on-dark">Error 404 &#183; Out of tolerance</p>
    <h1>This page is not in our range</h1>
    <p class="lede">The address may be from our old website. These pages will get you to the right strip.</p>
    <ul class="notfound__links">
      <li><a href="/hardened-tempered-steel-strips/">Hardened and tempered strips</a></li>
      <li><a href="/cold-rolled-steel-strips/">Cold rolled strips</a></li>
      <li><a href="/grades/">Grades and equivalents</a></li>
      <li><a href="/contact/">Request a quote</a></li>
    </ul>
    <a class="btn btn--light" href="/">Back to the home page</a>
  </div>
</section>
</main>
'''
    schema = graph(org_ref(), page_node("404.html", title, desc))
    return dict(slug="404.html", title=title, desc=desc, schema=schema, active="", body=body, robots=True)


# --------------------------------------------------------------------------------------------

def render(page, prefix):
    h = head(prefix, page)
    if page.get("robots"):
        h = h.replace('<meta name="theme-color"', '<meta name="robots" content="noindex">\n<meta name="theme-color"')
    return h + header(prefix, page["active"]) + page["body"] + footer(prefix)


def main():
    pages = [page_home(), product_page("ht"), product_page("cr"), page_grades(), page_applications(),
             page_quality(), page_about(), page_faq(), page_contact()]
    for pg in pages:
        prefix = "" if pg["slug"] == "" else "../"
        out = os.path.join(ROOT, pg["slug"], "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(render(pg, prefix))
        print("wrote", os.path.relpath(out, ROOT))
    nf = page_404()
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(render(nf, "/"))
    print("wrote 404.html")

    urls = "".join(
        f"  <url><loc>{DOMAIN}/{pg['slug']}</loc><lastmod>2026-10-09</lastmod></url>\n" for pg in pages)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    main()
