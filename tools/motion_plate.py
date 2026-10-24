"""Grade a generated motion plate so it matches its still exactly (v1.4).

Run:  python3 tools/motion_plate.py <raw.mp4> <still image> <family> <out.mp4> [--graded-source]

families
  engraving  luminance mapped to the plate duotone, forest ink #183015 on cream #FFFCF7. Heavy fills that the
             video model adds fall back into ink line work. Pass --graded-source when the start image was already
             a graded plate (its tones are kept, only the hue is pinned); otherwise the black and white points
             are set from the first frame the way a still is graded (0.5th and 88th percentile, gamma 1.08).
  night      the same clip inverted into cream ink #EDE7D8 on Forest Night #152511
  match      photographs, specimens, red-chalk studies and micrographs: each channel's mean and spread is
             matched to the still, so the clip opens on the still's exact colour

Output: H.264, no audio, CRF 15, the source size and frame rate.
"""
import subprocess, sys
import numpy as np
from PIL import Image

INK, CREAM = np.array([24, 48, 21.]), np.array([255, 252, 247.])
NIGHT_BG, NIGHT_INK = np.array([21, 37, 17.]), np.array([237, 231, 216.])


def lum(a):
    return a[..., 0] * .2126 + a[..., 1] * .7152 + a[..., 2] * .0722


def first_frame(path, size):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-frames:v", "1", "-vf", f"scale={size[0]}:{size[1]}",
                          "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(size[1], size[0], 3).astype(float)


def grade(raw, still, family, out, graded_source=False):
    w, h = map(int, subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                    "stream=width,height", "-of", "csv=p=0", raw], capture_output=True, text=True).stdout.split(","))
    size = (360, 640) if h > w else (640, 360)
    f0 = first_frame(raw, size)
    if family in ("engraving", "night"):
        if graded_source:
            lo, hi, g = lum(INK) / 255, lum(CREAM) / 255, 1.0
        else:
            L = lum(f0)
            lo, hi, g = np.percentile(L, .5) / 255, np.percentile(L, 88) / 255, 1.08
        a, c = (INK, CREAM) if family == "engraving" else (NIGHT_INK, NIGHT_BG)
        t = f"pow(clip((val/255-{lo:.4f})/{hi - lo:.4f},0,1),{g})"
        vf = (f"format=gray,format=rgb24,lutrgb=r='{a[0]}+({c[0] - a[0]})*{t}':g='{a[1]}+({c[1] - a[1]})*{t}'"
              f":b='{a[2]}+({c[2] - a[2]})*{t}'")
    elif family == "match":
        s = np.asarray(Image.open(still).convert("RGB").resize(size)).astype(float)
        ms, ss = s.reshape(-1, 3).mean(0), s.reshape(-1, 3).std(0) + 1e-6
        mv, sv = f0.reshape(-1, 3).mean(0), f0.reshape(-1, 3).std(0) + 1e-6
        k = ss / sv
        vf = "lutrgb=" + ":".join(f"{ch}='clip({ms[i]:.3f}+(val-{mv[i]:.3f})*{k[i]:.4f},0,255)'" for i, ch in enumerate("rgb"))
    else:
        raise SystemExit(f"unknown family {family}")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", raw, "-vf", vf + ",format=yuv420p", "-an", "-c:v", "libx264",
                    "-preset", "slow", "-crf", "15", "-movflags", "+faststart", out], check=True)


def playback(shot_seconds, n_use=0, clip_seconds=3.0):
    """Media start and rate so a shot shows about 0.9 s of motion: up to 3x in short shots, 1x on holds of 0.9 s
    or more, and a different stretch of the clip each time a plate is reused."""
    rate = min(3.0, max(1.0, 0.9 / shot_seconds))
    start = (0.2, 1.2, 2.0, 0.6)[n_use % 4]
    start = max(0.0, min(start, clip_seconds - shot_seconds * rate - 0.05))
    if start + shot_seconds * rate > clip_seconds - 0.02:     # a hold longer than its clip slows down to fit
        rate = max(0.1, (clip_seconds - 0.05 - start) / shot_seconds)
    return round(start, 3), round(rate, 3)


if __name__ == "__main__":
    raw, still, family, out = sys.argv[1:5]
    grade(raw, still, family, out, "--graded-source" in sys.argv)
    print(family, "->", out)
