"""Grade generated micrographs into the Optimal family.

fluorescence (fl_*): lift the black point to night-950 #0B1608 so they sit on Forest Night, soft-clip
  highlights so the leaf green never goes neon, and keep the stain colours saturated.
brightfield (bf_*): balance the slide to cream #FCF8F1 like the specimen photographs.
Outputs: film JPEGs (2560x1440) and design-system WebPs: full-bleed plus a square "field" plate
  (circular field of view with the ring accent) for social and editorial layouts.
"""
import sys, os, glob
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
SRC, FILM, DS = sys.argv[1:4]
for d in (FILM, os.path.join(DS, "fluorescence"), os.path.join(DS, "brightfield"), os.path.join(DS, "field")):
    os.makedirs(d, exist_ok=True)
NIGHT950 = np.array([11, 22, 8], np.float32)
NIGHT900 = (21, 37, 17)
CREAM_BF = np.array([252, 248, 241], np.float32)
CREAM = (255, 252, 247)

def fit(im, w, h):
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))

def grade_fl(a):
    a = a / 255.0
    a = 1 - np.exp(-a * 1.35)                 # soft shoulder: highlights roll off instead of clipping
    a = a / (1 - np.exp(-1.35))
    lum = a.mean(-1, keepdims=True)
    a = lum + (a - lum) * 1.06                 # keep it saturated
    a = np.clip(a, 0, 1)
    return NIGHT950 + a * (255 - NIGHT950)     # lift: black becomes night-950

def grade_bf(a):
    border = np.concatenate([a[:80].reshape(-1, 3), a[-80:].reshape(-1, 3), a[:, :80].reshape(-1, 3), a[:, -80:].reshape(-1, 3)])
    paper = np.percentile(border, 90, axis=0)
    return a * (CREAM_BF / paper)

def field(img, ground, ring):
    """Square plate: circular field of view (soft edge) on the ground colour, plus the ring accent."""
    S = 1600; R = int(S * 0.40)
    sq = fit(img, S, S)
    mask = Image.new("L", (S, S), 0); ImageDraw.Draw(mask).ellipse((S/2-R, S/2-R, S/2+R, S/2+R), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(10))
    out = Image.new("RGB", (S, S), ground); out.paste(sq, (0, 0), mask)
    d = ImageDraw.Draw(out, "RGBA")
    rr = R + 34
    d.ellipse((S/2-rr*1.03, S/2-rr*0.985, S/2+rr*1.03, S/2+rr*0.985), outline=ring, width=4)
    return out

for f in sorted(glob.glob(os.path.join(SRC, "*.png"))):
    name = os.path.basename(f)[:-4]
    im = fit(Image.open(f).convert("RGB"), 2560, 1440)
    a = np.asarray(im).astype(np.float32)
    fl = name.startswith("fl_")
    g = grade_fl(a) if fl else grade_bf(a)
    out = Image.fromarray(np.clip(g, 0, 255).astype(np.uint8))
    out.save(os.path.join(FILM, name + ".jpg"), quality=90)
    out.save(os.path.join(DS, "fluorescence" if fl else "brightfield", name[3:] + ".webp"), quality=86)
    field(out, NIGHT900 if fl else CREAM, (237, 231, 216, 150) if fl else (26, 80, 18, 128)).save(
        os.path.join(DS, "field", name[3:] + "-field.webp"), quality=86)
    print(name)
