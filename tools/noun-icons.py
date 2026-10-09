#!/usr/bin/env python3
"""Fetch the Noun Project concept icons listed in site_data.NOUN_ICONS and prepare them.

    python3 tools/noun-icons.py

House workflow (site-rebuild reference-noun-icons.md): CC BY 3.0 or public domain only, download
the published PNG, vectorise with potrace, crop the viewBox to the artwork, recolour to --ink-2.
Writes public/imgs/noun-<slug>-<id>.svg and docs/icon-credits.md. Every icon is decorative
(alt="", no information depends on it). Find candidates with tools/noun-search.py.
"""
import os
import re
import subprocess
import sys
import tempfile
import urllib.request

from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
from site_data import NOUN_ICONS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public", "imgs")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
FILL = "#3D3F45"  # --ink-2: icons read as drawn lines, magenta stays for numbers and the stamp


def fetch(nid):
    for url in ("https://static.thenounproject.com/png/%d-512.png" % nid,
                "https://static.thenounproject.com/png/%d-200.png" % nid):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}),
                                          timeout=30).read()
        except Exception:
            continue
    raise RuntimeError("could not fetch icon %d" % nid)


def vectorise(png_bytes, tmp):
    """Alpha to a bitmap cropped to the artwork, then potrace. Cropping first is what tightens
    the viewBox: potrace sizes its output from the bitmap."""
    raw = os.path.join(tmp, "in.png")
    with open(raw, "wb") as f:
        f.write(png_bytes)
    im = Image.open(raw).convert("RGBA")
    mask = im.split()[3].point(lambda a: 255 if a > 40 else 0).convert("L")
    box = mask.getbbox()
    if box:
        mask = mask.crop(box)
    w, h = mask.size
    side = max(w, h)  # pad to a square so every icon sits centred in the same box
    sq = Image.new("L", (side, side), 0)
    sq.paste(mask, ((side - w) // 2, (side - h) // 2))
    sq = sq.point(lambda v: 0 if v else 255).convert("1")
    pbm = os.path.join(tmp, "in.pbm")
    sq.save(pbm)
    svg = os.path.join(tmp, "out.svg")
    subprocess.run(["potrace", "-s", "-o", svg, "-a", "1.0", "-O", "0.2", "--flat", pbm], check=True)
    with open(svg, encoding="utf-8") as f:
        return f.read()


def clean(svg):
    """Keep potrace's geometry and coordinate system, drop its metadata and fills."""
    vb = re.search(r'viewBox="([^"]+)"', svg)
    g = re.search(r"(<g[^>]*>)(.*?)</g>", svg, re.S)
    if not (vb and g):
        raise RuntimeError("unexpected potrace output")
    body = re.sub(r'\s(fill|stroke)="[^"]*"', "", g.group(2).strip())
    _, _, w, h = [float(v) for v in vb.group(1).split()]
    tr = re.search(r'transform="([^"]+)"', g.group(1))
    tr = ' transform="%s"' % tr.group(1) if tr else ""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %g %g" fill="%s" aria-hidden="true">\n'
            '<g%s>%s</g>\n</svg>\n' % (w, h, FILL, tr, body))


def main():
    rows = []
    with tempfile.TemporaryDirectory() as tmp:
        for slot, (nid, slug, creator) in NOUN_ICONS.items():
            name = "noun-%s-%d.svg" % (slug, nid)
            svg = clean(vectorise(fetch(nid), tmp))
            with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
                f.write(svg)
            rows.append("| %s | %s | %d | %s | CC BY 3.0 | `public/imgs/%s` |" % (
                slot, slug.replace("-", " "), nid, creator, name))
            print("%-24s %-36s %6d bytes" % (slot, name, len(svg)))
    with open(os.path.join(ROOT, "docs", "icon-credits.md"), "w", encoding="utf-8") as f:
        f.write("# Icon credits\n\nConcept icons from the Noun Project (thenounproject.com), used under "
                "CC BY 3.0. Traced from the published PNG, cropped and recoloured to --ink-2. Each "
                "`<img>` carries a `title` credit and each page an HTML comment listing its icons. "
                "Regenerate with `python3 tools/noun-icons.py`.\n\n"
                "| Slot | Icon | Noun id | Creator | Licence | File |\n| --- | --- | --- | --- | --- | --- |\n"
                + "\n".join(rows) + "\n")
    print("wrote docs/icon-credits.md")


if __name__ == "__main__":
    sys.exit(main())
