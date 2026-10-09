"""Make the home hero background from the slitting line image.

Source: docs/art/hero-slitting-line-source.jpg, an AI-generated illustration (ChatGPT, 9 Oct 2026)
of a slitting line. It is NOT a photo of the Bawana works, so it is used only as an unlabelled
background; no caption or alt text may present it as Anil's plant. Replace it with a real photo
of the works when the owner supplies one (same script, new source).

The image is darkened to the site's night colour under the hero copy, so text contrast is
always measured against --night. The earlier procedural coil version is in commit c66d5b6.

    python3 tools/make_hero_bg.py
    # writes public/imgs/hero-factory.webp (right half of the stage, 960px and up)
    #    and public/imgs/hero-factory-tall.webp (portrait crop, band below the spec plate on phones)
"""
import os
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "docs", "art", "hero-slitting-line-source.jpg")
OUT = os.path.join(ROOT, "public", "imgs")
NIGHT = np.array([0x17, 0x18, 0x1B], dtype=np.float32) / 255.0


def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def fall_off(img, axis, start, end):
    """Blend to night before `start` and keep the image after `end` (fractions of the axis)."""
    rgb = np.asarray(img, dtype=np.float32) / 255.0
    h, w = rgb.shape[:2]
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    f = smoothstep(start * w, end * w, x) if axis == "x" else smoothstep(start * h, end * h, y)
    out = NIGHT + (rgb - NIGHT) * f[..., None]
    return Image.fromarray((np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8), "RGB")


def main():
    src = Image.open(SRC).convert("RGB")                     # 1536 x 1024
    w, h = src.size
    # machinery only; the layer starts mid-stage (css), so the copy column is on plain night
    wide = fall_off(src.crop((int(w * 0.33), 0, w, h)), "x", 0.0, 0.24)
    wide.save(os.path.join(OUT, "hero-factory.webp"), "WEBP", quality=78, method=6)
    tall = fall_off(src.crop((int(w * 0.365), 0, w, h)), "y", 0.18, 0.48)   # knives and recoils
    tall.save(os.path.join(OUT, "hero-factory-tall.webp"), "WEBP", quality=78, method=6)
    for name in ("hero-factory.webp", "hero-factory-tall.webp"):
        print(name, os.path.getsize(os.path.join(OUT, name)) // 1024, "KB")


if __name__ == "__main__":
    main()
