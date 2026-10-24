"""Export the Specimen film's generated plates into the design system (v1.4).

Run:  python3 tools/specimen_export.py <film assets/gen dir> assets/illustration/specimen

engraved/   transparent ink, trimmed to the drawing: <name>.webp in forest ink #183015 for cream grounds and
            <name>-cream.webp in cream ink #FFFCF7 for Forest Night (the v1.2 plate convention). The ink density
            comes from the graded duotone (ink #183015 on cream #FFFCF7), so nothing is redrawn.
chalk/      red-chalk studies on their own cream paper, 2560 x 1440
specimens/  single objects on cream seamless #FCF8F1, 2560 x 1440
ontario/    Ontario land and water, photo-graded, 2560 x 1440 (never captioned as a named real place)
"""
import os, sys
import numpy as np
from PIL import Image

INK, CREAM = np.array([24, 48, 21.]), np.array([255, 252, 247.])
PLATES = {
    "engraved": {"ecorche": "00a_vitruvian_ecorche", "bronchial-tree": "01_bronchial", "iris": "02_iris",
                 "cochlea": "03_cochlea", "spine": "04_spine", "neuron": "05_neuron", "hand": "06b_hand_living",
                 "alveoli": "09_alveoli", "femur": "10_femur", "heart": "41_heart_engr"},
    "chalk": {"chalk-heart": "07_redheart", "chalk-head": "08_redhead", "chalk-knee": "11_redknee"},
    "specimens": {"dandelion": "13_dandelion", "birch-rings": "14_birchrings", "fiddlehead": "15_fiddlehead",
                  "maple-leaf": "16_mapleleaf", "pomegranate": "17_pomegranate", "robin-egg": "19_robinegg",
                  "honeycomb": "22_honeycomb", "lichen-stone": "23_lichen_stone"},
    "ontario": {"oak-snow": "27_oak_snow", "delta": "28_delta", "kettle-lake": "29_kettlelake",
                "lightning": "30_lightning", "frost": "31_frost", "murmuration": "32_murmuration",
                "lake-ice": "33_ice_cracks", "pine-granite": "34_pine_granite", "gneiss": "35_gneiss",
                "maple-canopy": "36_maple_canopy", "surf": "37_surf", "moonrise": "38_moonrise",
                "birch-forest": "39_birch_trunks"},
}


def lum(a):
    return a[..., 0] * .2126 + a[..., 1] * .7152 + a[..., 2] * .0722


def engraved(src, out_dir, name):
    a = np.asarray(Image.open(src).convert("RGB").resize((2560, 1440), Image.LANCZOS)).astype(float)
    t = np.clip((lum(a) - lum(INK)) / (lum(CREAM) - lum(INK)), 0, 1)
    alpha = np.clip((1 - t - 0.10) / 0.90, 0, 1)             # paper grain (up to ~10% density) is not ink
    ys, xs = np.nonzero(alpha > 0.3)
    pad = 24
    y0, y1 = max(ys.min() - pad, 0), min(ys.max() + pad, a.shape[0])
    x0, x1 = max(xs.min() - pad, 0), min(xs.max() + pad, a.shape[1])
    al = (alpha[y0:y1, x0:x1] * 255).round().astype(np.uint8)
    for suffix, ink in (("", INK), ("-cream", CREAM)):
        rgb = np.broadcast_to(ink.astype(np.uint8), al.shape + (3,))
        Image.fromarray(np.dstack([rgb, al]), "RGBA").save(os.path.join(out_dir, f"{name}{suffix}.webp"), quality=90, method=6)


def opaque(src, out_dir, name):
    Image.open(src).convert("RGB").resize((2560, 1440), Image.LANCZOS).save(os.path.join(out_dir, f"{name}.webp"), quality=86, method=6)


if __name__ == "__main__":
    gen, out = sys.argv[1:3]
    for family, plates in PLATES.items():
        d = os.path.join(out, family)
        os.makedirs(d, exist_ok=True)
        for name, stem in plates.items():
            src = os.path.join(gen, stem + ".jpg")
            (engraved if family == "engraved" else opaque)(src, d, name)
            print(family, name)
