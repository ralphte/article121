"""Textures the model builder puts on the cockpit panels and the rescue markings, cut from
government drawings (rights tier A):

  panel-pilot.jpg   SR-71A-1 flight manual, Figure 1-12, centre instrument panel, forward cockpit (p.1-23)
  panel-rso.jpg     SR-71A-1 flight manual, Figure 1-17, instrument panel, aft cockpit (p.1-28)
  mark-rescue.png   A-12 ground handling manual (CIA C06230171), Figure 2-6 sheet 1: RESCUE arrow
  mark-rescue-r.png the same arrow pointing the other way, its lettering kept readable (right side)
  mark-danger.png   the same figure: DANGER UPWARD EJECTION SEAT triangle

The panels are drawn white on black in Figure 1-12 and black on white in Figure 1-17. Both are
masked to the panel's own outline (callout numbers and leader lines on the white page fall away),
and the RSO's large white display faces become dark screens. The markings are the figure's line
art as an alpha mask in red; the manual gives no colours, so the red is a placeholder.

  uv run --with pillow --with numpy --with scipy python model/tools/textures.py
Needs poppler's pdftoppm for the A-12 manual page. Writes model/textures/.
"""
import subprocess
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

ROOT = Path(__file__).resolve().parents[2]
MEDIA = ROOT / "research/systems/media"
OUT = ROOT / "model/textures"
A12GH = ROOT / "model/plans/raw/cia_C06230171_A-12-support-manual-ground-handling.pdf"


def panel(src, box, blank=(), screens=False, width=1024):
    g = np.asarray(Image.open(src).convert("L").crop(box), float)
    for x0, y0, x1, y1 in blank:                       # insets drawn beside the panel
        g[max(0, y0 - box[1]):max(0, y1 - box[1]), max(0, x0 - box[0]):max(0, x1 - box[0])] = 255
    dark = g < 140
    # the page: white connected to the border. Everything else is the panel and its markings.
    lab, _ = ndi.label(~dark)
    edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    page = np.isin(lab, list(edge))
    body = ndi.binary_opening(~page, structure=np.ones((11, 11)))   # drops callout text and leader lines
    lab, n = ndi.label(body)
    if n:
        sizes = ndi.sum(body, lab, range(1, n + 1))
        body = np.isin(lab, [i + 1 for i, s in enumerate(sizes) if s > 0.002 * body.size])
    body = ndi.binary_fill_holes(ndi.binary_closing(body, structure=np.ones((9, 9))))
    rgb = np.stack([g, g * 0.97, g * 0.9], -1)
    rgb = np.where(dark[..., None], [14, 14, 16], rgb)
    if screens:                                          # big white faces are displays, not markings
        lab, n = ndi.label(~dark & body)
        sizes = ndi.sum(~dark & body, lab, range(1, n + 1))
        big = np.isin(lab, [i + 1 for i, s in enumerate(sizes) if s > 0.0015 * body.size])
        rgb = np.where(big[..., None], [22, 30, 28], rgb)
    rgb = np.where(body[..., None], rgb, [9, 9, 11])
    im = Image.fromarray(rgb.clip(0, 255).astype(np.uint8))
    return im.resize((width, round(width * im.height / im.width)), Image.LANCZOS)


def marking(page, box, keep=None, width=512):
    """Line art as alpha: ink is opaque, the page clear. Ink touching the crop's border (callout
    leaders) is dropped; `keep(x, y)` (crop pixels) can instead say which ink to keep."""
    g = np.asarray(page.convert("L").crop(box), float)
    a = (255 - g).clip(0, 255)
    a = np.where(a > 70, 255, a * 255 / 70)
    ink = a > 40
    if keep is None:
        lab, _ = ndi.label(ink, structure=np.ones((3, 3)))
        edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
        a = np.where(np.isin(lab, list(edge)), 0, a)
    else:
        yy, xx = np.mgrid[0:g.shape[0], 0:g.shape[1]]
        a = np.where(keep(xx, yy), a, 0)
    im = Image.fromarray(np.dstack([np.full_like(g, 196), np.full_like(g, 34), np.full_like(g, 28), a]).astype(np.uint8), "RGBA")
    return im.resize((width, round(width * im.height / im.width)), Image.LANCZOS)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    p = panel(MEDIA / "diagram_SR-71A-1_fig1-12_front-cockpit-center-instrument-panel_p1-23.jpg",
              (255, 472, 2025, 1968), blank=((300, 420, 528, 713), (1758, 502, 1938, 672)))
    p.save(OUT / "panel-pilot.jpg", quality=86)
    r = panel(MEDIA / "diagram_SR-71A-1_fig1-17_rear-cockpit-RSO-instrument-panel_p1-28.jpg",
              (270, 420, 1942, 1437), screens=True)
    r.save(OUT / "panel-rso.jpg", quality=86)
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-f", "28", "-l", "28", "-r", "300", "-png", str(A12GH), f"{td}/p"], check=True)
        page = Image.open(next(Path(td).glob("p*.png")))
        s = page.width / 600          # the boxes below are on the page at 600 px wide
        sc = lambda b: tuple(round(v * s) for v in b)
        rescue = marking(page, sc((80, 228, 262, 294)))
        rescue.save(OUT / "mark-rescue.png")
        # pointing right: mirror the arrow, then put the word back the right way round
        flip = rescue.transpose(Image.FLIP_LEFT_RIGHT)
        w, h = rescue.size
        word = (round(0.32 * w), round(0.28 * h), round(0.86 * w), round(0.70 * h))
        flip.paste((0, 0, 0, 0), (w - word[2], word[1], w - word[0], word[3]))
        flip.alpha_composite(rescue.crop(word), (w - word[2], word[1]))
        flip.save(OUT / "mark-rescue-r.png")
        # the triangle (apex down) and the word above it; a leader line meets its left edge
        bx = sc((378, 338, 572, 512))
        P = lambda x, y: (x * s - bx[0], y * s - bx[1])
        tri = [P(398.3, 373.3), P(553.3, 373.3), P(475.8, 503.5)]
        def in_tri(x, y, m=17 * s):
            (x0, y0), (x1, y1), (x2, y2) = tri
            d = lambda ax, ay, bx_, by: ((x - ax) * (by - ay) - (y - ay) * (bx_ - ax)) / np.hypot(bx_ - ax, by - ay)
            left_out = d(x2, y2, x0, y0) > 2 * s
            body = (d(x0, y0, x1, y1) <= 3 * s) & (d(x1, y1, x2, y2) <= m) & (d(x2, y2, x0, y0) <= m)
            body &= ~(left_out & (y < P(0, 408)[1]))           # the leader line meets the left edge here
            word = (y > P(0, 342)[1]) & (y < P(0, 374)[1]) & (x > P(436, 0)[0]) & (x < P(516, 0)[0])
            return body | word
        marking(page, bx, keep=in_tri).save(OUT / "mark-danger.png")
    for f in sorted(OUT.iterdir()):
        im = Image.open(f)
        print(f.name, im.size, f.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
