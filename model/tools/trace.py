"""Trace one view of a published drawing into a calibrated silhouette and profiles.

  cd model/tools && uv run python trace.py ../trace/<spec>.json

A spec file describes one view on one page:
{
  "page": "../plans/pages/<file>.png",       # source drawing (see plans/manifest.json for rights)
  "view": "plan" | "side" | "front",
  "crop": [x0, y0, x1, y1],                  # pixel box around the view
  "erase": [[x0, y0, x1, y1], ...],          # boxes to blank: dimension text, leaders, labels
  "threshold": 150,                          # darker than this is ink
  "close_px": 3,                             # seal small gaps in the outline before filling
  "datum_a": [x, y], "datum_b": [x, y],      # two pixel points with a known distance between them
  "datum_m": 32.74,                          # that distance in metres (for example nose to tail)
  "origin": "datum_a",                       # which datum is x = 0 (normally the nose tip)
  "x_axis": "datum_b"                        # direction of +x (toward the tail)
}

Writes next to the spec: <name>.mask.png (filled silhouette), <name>.overlay.png (outline
over the drawing) and <name>.json with the silhouette contour in metres and, for plan and
side views, the upper and lower envelope sampled every 5 cm along x.
"""
import json
import sys
from pathlib import Path

import cv2
import numpy as np


def load_spec(path):
    p = Path(path)
    spec = json.loads(p.read_text())
    spec["_dir"] = p.parent
    spec["_name"] = p.stem
    return spec


def filled_silhouette(gray, threshold, close_px):
    ink = (gray < threshold).astype(np.uint8) * 255
    if close_px > 0:
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * close_px + 1, 2 * close_px + 1))
        ink = cv2.morphologyEx(ink, cv2.MORPH_CLOSE, k)
    # flood the background from the border; whatever the flood cannot reach is the aircraft
    h, w = ink.shape
    flood = ink.copy()
    mask = np.zeros((h + 2, w + 2), np.uint8)
    for seed in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]:
        if flood[seed[1], seed[0]] == 0:
            cv2.floodFill(flood, mask, seed, 128)
    sil = (flood != 128).astype(np.uint8) * 255
    # keep the largest connected part (drops stray text that survived erasing)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(sil, 8)
    if n > 1:
        biggest = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
        sil = (lab == biggest).astype(np.uint8) * 255
    return sil


def frame(spec):
    a = np.array(spec[spec.get("origin", "datum_a")], float)
    b = np.array(spec[spec.get("x_axis", "datum_b")], float)
    da, db = np.array(spec["datum_a"], float), np.array(spec["datum_b"], float)
    m_per_px = spec["datum_m"] / np.linalg.norm(db - da)
    ex = (b - a) / np.linalg.norm(b - a)          # drawing direction of +x
    ey = np.array([-ex[1], ex[0]])                # 90 degrees from x in image coordinates
    return a, ex, ey, m_per_px


def to_metres(pts_px, spec):
    a, ex, ey, s = frame(spec)
    d = pts_px - a
    x = d @ ex * s
    y = -(d @ ey) * s                             # image y grows downward; flip so up is positive
    return np.stack([x, y], 1)


def main(path):
    spec = load_spec(path)
    page = cv2.imread(str((spec["_dir"] / spec["page"]).resolve()), cv2.IMREAD_GRAYSCALE)
    if page is None:
        sys.exit(f"cannot read {spec['page']}")
    x0, y0, x1, y1 = spec["crop"]
    work = page.copy()
    for ex0, ey0, ex1, ey1 in spec.get("erase", []):
        work[ey0:ey1, ex0:ex1] = 255
    view = work[y0:y1, x0:x1]
    sil = filled_silhouette(view, spec.get("threshold", 150), spec.get("close_px", 3))

    full = np.zeros_like(page); full[y0:y1, x0:x1] = sil
    contours, _ = cv2.findContours(full, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(contours, key=cv2.contourArea)[:, 0, :].astype(float)
    pts_m = to_metres(c, spec)

    out = {"spec": spec["_name"], "page": spec["page"], "view": spec["view"],
           "m_per_px": frame(spec)[3], "contour_m": np.round(pts_m, 4).tolist()}
    if spec["view"] in ("plan", "side"):
        xs = np.arange(np.floor(pts_m[:, 0].min() * 20) / 20, pts_m[:, 0].max(), 0.05)
        ys_full = np.indices(full.shape)
        on = np.argwhere(full > 0)[:, ::-1].astype(float)        # (x, y) pixels of the silhouette
        m = to_metres(on, spec)
        bins = np.digitize(m[:, 0], xs)
        upper, lower = [], []
        for i, x in enumerate(xs, start=1):
            sel = m[bins == i, 1]
            if sel.size:
                upper.append([round(float(x), 3), round(float(sel.max()), 4)])
                lower.append([round(float(x), 3), round(float(sel.min()), 4)])
        out["upper"], out["lower"] = upper, lower
    (spec["_dir"] / f"{spec['_name']}.json").write_text(json.dumps(out))
    cv2.imwrite(str(spec["_dir"] / f"{spec['_name']}.mask.png"), full[y0:y1, x0:x1])
    over = cv2.cvtColor(page[y0:y1, x0:x1], cv2.COLOR_GRAY2BGR)
    cv2.drawContours(over, [(c - [x0, y0]).astype(np.int32).reshape(-1, 1, 2)], -1, (0, 0, 255), 2)
    for k in ("datum_a", "datum_b"):
        px, py = spec[k]
        cv2.circle(over, (int(px - x0), int(py - y0)), 8, (255, 120, 0), 2)
    cv2.imwrite(str(spec["_dir"] / f"{spec['_name']}.overlay.png"), over)
    span = pts_m[:, 0].max() - pts_m[:, 0].min()
    print(f"{spec['_name']}: {len(c)} contour points, {out['m_per_px'] * 1000:.1f} mm per px, x extent {span:.2f} m")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p)
