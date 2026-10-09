"""Render the home hero background: the end face of a wound steel strip coil.

Procedural, not a photo: every wrap of strip is a ring with its own reflectance, lit by a
turned-metal highlight, on the site's night colour. The left side falls off to night so the
hero copy always sits on a dark, even field (contrast is checked against --night).

    python3 tools/make_hero_bg.py      # writes imgs/hero-coil.webp and imgs/hero-coil-tall.webp

Replace with a real macro photo of a coil face from the Bawana works when the owner supplies one.
"""
import os
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NIGHT = np.array([0x17, 0x18, 0x1B], dtype=np.float32) / 255.0
STEEL = np.array([0.80, 0.83, 0.88], dtype=np.float32)   # cool bright steel
rng = np.random.default_rng(1976)


def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def render(w, h, centre, r_out, r_in, fade, ss=2):
    """centre as fractions of (w, h); radii as fractions of min(w, h); fade = (axis, start, end)."""
    W, H = w * ss, h * ss
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    cx, cy = centre[0] * W, centre[1] * H
    S = min(W, H)
    R_out, R_in = r_out * S, r_in * S
    dx, dy = x - cx, y - cy
    r = np.hypot(dx, dy)
    th = np.arctan2(dy, dx)

    # wraps: strip thickness in px, each wrap its own reflectance, a dark seam between wraps
    t = 6.0 * ss
    k = (r - R_in) / t
    idx = np.clip(np.floor(k).astype(np.int64), 0, None)
    n = int(idx.max()) + 2
    refl = 0.78 + 0.22 * rng.random(n).astype(np.float32)
    # occasional brighter, freshly slit wraps
    refl[rng.random(n) < 0.04] = 1.08
    f = k - np.floor(k)
    seam = 1.0 - 0.55 * (1.0 - smoothstep(0.0, 0.18, f)) - 0.35 * smoothstep(0.82, 1.0, f)
    face = refl[idx] * seam

    # turned-metal highlight: a soft bowtie along one axis plus a broad ambient term
    lobe = np.abs(np.cos(th - np.radians(-38.0))) ** 6
    lobe2 = np.abs(np.cos(th - np.radians(52.0))) ** 14
    light = 0.20 + 0.85 * lobe + 0.30 * lobe2
    # very slow variation round the coil so wraps do not read as perfect circles
    light *= 0.92 + 0.08 * np.sin(3.0 * th + r / (40.0 * ss))

    lum = face * light
    # bevel at the outer edge and shadow into the bore
    lum *= smoothstep(R_in, R_in + 14 * ss, r) * 0.85 + 0.15 * (r > R_in)
    lum *= 1.0 - 0.5 * smoothstep(R_out - 22 * ss, R_out, r)
    on_coil = (r >= R_in) & (r <= R_out)

    # steel packing hoops: flat bands across the face, through the bore
    for phi, bw in ((np.radians(-72.0), 0.050 * S), (np.radians(162.0), 0.050 * S)):
        along = dx * np.cos(phi) + dy * np.sin(phi)            # distance along the strap
        across = -dx * np.sin(phi) + dy * np.cos(phi)          # distance across it
        band = (along > R_in * 0.6) & (np.abs(across) < bw / 2)
        u = across / (bw / 2)
        strap = 0.30 + 0.38 * (1 - u ** 2) + 0.22 * (u < -0.80)   # domed band, lit edge
        strap *= 0.85 + 0.15 * np.cos(along / (90.0 * ss))
        shadow = (along > R_in * 0.6) & (across > bw / 2) & (across < bw / 2 + 10 * ss)
        lum = np.where(shadow, lum * 0.35, lum)
        lum = np.where(band & (r <= R_out + 2 * ss), strap, lum)

    # exposure kept low: this is a background, the copy and spec plate lead
    lum = np.where(on_coil, lum, 0.0) * 0.62
    rgb = NIGHT + (STEEL - NIGHT) * lum[..., None]

    # bore: deep shadow with a faint inner lip
    lip = np.exp(-((r - R_in) / (5.0 * ss)) ** 2) * (r < R_in)
    rgb = np.where((r < R_in)[..., None], NIGHT * 0.7 + STEEL * 0.10 * lip[..., None], rgb)

    # fall off to night under the copy (lighting, baked into the image)
    axis, a, b = fade
    fall = smoothstep(a * W, b * W, x) if axis == "x" else smoothstep(a * H, b * H, y)
    rgb = NIGHT + (rgb - NIGHT) * fall[..., None]

    # fine grain so large flat areas do not band
    rgb += (rng.standard_normal((H, W, 1)).astype(np.float32) * 0.008)
    img = Image.fromarray((np.clip(rgb, 0, 1) * 255 + 0.5).astype(np.uint8), "RGB")
    return img.resize((w, h), Image.LANCZOS)


def main():
    # landscape, from 960px: coil on the right, copy column on the left
    wide = render(2400, 1260, (0.79, 0.50), 0.92, 0.22, ("x", 0.38, 0.66))
    wide.save(os.path.join(ROOT, "imgs", "hero-coil.webp"), "WEBP", quality=72, method=6)
    # portrait, phones and tablets: coil behind the spec plate, copy above on plain night
    tall = render(900, 1400, (0.56, 0.70), 0.80, 0.20, ("y", 0.22, 0.50))
    tall.save(os.path.join(ROOT, "imgs", "hero-coil-tall.webp"), "WEBP", quality=72, method=6)
    for name in ("hero-coil.webp", "hero-coil-tall.webp"):
        p = os.path.join(ROOT, "imgs", name)
        print(name, os.path.getsize(p) // 1024, "KB")


if __name__ == "__main__":
    main()
