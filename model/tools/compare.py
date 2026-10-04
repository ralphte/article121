"""Score a built model against traced drawings.

  cd model/tools && uv run python compare.py ../build/renders/<run> ../trace/<view-spec>.json [...]

For each traced view, loads the model's matching <view>_sil.png (rendered by render_views.py
at a known pixels-per-metre), aligns the two silhouettes by their bounding-box centres, and
reports: size differences, intersection over union, and the mean and worst distance between
the two outlines in centimetres. Writes <view>_vs_<spec>.png overlays into the render folder.
"""
import json
import sys
from pathlib import Path

import cv2
import numpy as np


def model_contour_m(render_dir, view):
    scale = json.loads((render_dir / "scale.json").read_text())
    ppm = scale["ppm"]
    sil = cv2.imread(str(render_dir / f"{view}_sil.png"), cv2.IMREAD_GRAYSCALE)
    _, b = cv2.threshold(sil, 127, 255, cv2.THRESH_BINARY)
    cs, _ = cv2.findContours(b, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cs, key=cv2.contourArea)[:, 0, :].astype(float)
    h, w = b.shape
    # view coordinates in metres: u to the image right, v up, origin at the image centre
    return np.stack([(c[:, 0] - w / 2) / ppm, (h / 2 - c[:, 1]) / ppm], 1), ppm


def drawing_contour_view(traced, view):
    pts = np.asarray(traced["contour_m"], float)
    # renders put the nose on the right in plan and side views, so station x runs leftward
    if view in ("plan", "side"):
        pts = np.stack([-pts[:, 0], pts[:, 1]], 1)
    return pts


def raster(pts, origin, ppm, shape):
    px = ((pts - origin) * [ppm, -ppm] + [shape[1] / 2, shape[0] / 2]).astype(np.int32)
    m = np.zeros(shape, np.uint8)
    cv2.fillPoly(m, [px.reshape(-1, 1, 2)], 255)
    return m, px


def best_shift(mod, drw, ppm, thin=True):
    """Translation of the drawing that maximises overlap with the model, searched coarse to fine.
    Hairline features (the pitot probe) are removed first so they cannot drag the alignment."""
    lo = np.minimum(mod.min(0), drw.min(0)) - 1.5
    hi = np.maximum(mod.max(0), drw.max(0)) + 1.5
    res = 25.0                                    # px per metre for the search
    shape = (int((hi[1] - lo[1]) * res) + 1, int((hi[0] - lo[0]) * res) + 1)
    def mask(p):
        m = np.zeros(shape, np.uint8)
        q = ((p - lo) * res).astype(np.int32); q[:, 1] = shape[0] - 1 - q[:, 1]
        cv2.fillPoly(m, [q.reshape(-1, 1, 2)], 1)
        if thin:
            m = cv2.morphologyEx(m, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
        return m.astype(bool)
    M = mask(mod)
    best, bs = -1, np.zeros(2)
    for step, span in ((0.1, 1.2), (0.02, 0.12)):
        centre = bs.copy()
        for dx in np.arange(-span, span + 1e-9, step):
            for dy in np.arange(-span / 2, span / 2 + 1e-9, step):
                D = mask(drw + centre + [dx, dy])
                iou = (M & D).sum() / max((M | D).sum(), 1)
                if iou > best:
                    best, bs = iou, centre + [dx, dy]
    return bs


def main(render_dir, specs):
    render_dir = Path(render_dir)
    report = []
    for sp in specs:
        traced = json.loads(Path(sp).with_suffix(".json").read_text()) if not sp.endswith(".json") or "contour_m" not in Path(sp).read_text() else json.loads(Path(sp).read_text())
        view = traced["view"]
        mod, ppm = model_contour_m(render_dir, view)
        drw = drawing_contour_view(traced, view)
        cm, cd = (mod.min(0) + mod.max(0)) / 2, (drw.min(0) + drw.max(0)) / 2
        drw = drw - cd + cm
        drw = drw + best_shift(mod, drw, ppm, thin=(view != "front"))
        size_m, size_d = mod.max(0) - mod.min(0), drw.max(0) - drw.min(0)
        ext = np.vstack([mod, drw])
        span = ext.max(0) - ext.min(0)
        shape = (int(span[1] * ppm) + 80, int(span[0] * ppm) + 80)
        origin = (ext.min(0) + ext.max(0)) / 2
        mm, mpx = raster(mod, origin, ppm, shape)
        dm, dpx = raster(drw, origin, ppm, shape)
        inter = np.logical_and(mm > 0, dm > 0).sum()
        union = np.logical_or(mm > 0, dm > 0).sum()
        # outline distances via distance transforms of each outline
        def edge(px):
            e = np.full(shape, 255, np.uint8); cv2.polylines(e, [px.reshape(-1, 1, 2)], True, 0, 1); return e
        dt_m = cv2.distanceTransform(edge(mpx), cv2.DIST_L2, 5)
        dt_d = cv2.distanceTransform(edge(dpx), cv2.DIST_L2, 5)
        d1 = dt_m[np.clip(dpx[:, 1], 0, shape[0] - 1), np.clip(dpx[:, 0], 0, shape[1] - 1)]
        d2 = dt_d[np.clip(mpx[:, 1], 0, shape[0] - 1), np.clip(mpx[:, 0], 0, shape[1] - 1)]
        dists = np.concatenate([d1, d2]) / ppm * 100
        row = {
            "view": view, "spec": traced["spec"],
            "model_size_m": np.round(size_m, 3).tolist(), "drawing_size_m": np.round(size_d, 3).tolist(),
            "iou": round(inter / max(union, 1), 4),
            "mean_cm": round(float(dists.mean()), 1), "p95_cm": round(float(np.percentile(dists, 95)), 1), "max_cm": round(float(dists.max()), 1),
        }
        report.append(row)
        over = np.zeros(shape + (3,), np.uint8)
        over[mm > 0] = (70, 70, 70)
        cv2.polylines(over, [dpx.reshape(-1, 1, 2)], True, (60, 60, 255), 2)     # drawing in red
        cv2.polylines(over, [mpx.reshape(-1, 1, 2)], True, (255, 230, 120), 1)   # model in cyan
        cv2.imwrite(str(render_dir / f"{view}_vs_{traced['spec']}.png"), over)
        print(f"{view:6s} IoU {row['iou']:.3f}  mean {row['mean_cm']} cm  p95 {row['p95_cm']} cm  max {row['max_cm']} cm  "
              f"size model {row['model_size_m']} vs drawing {row['drawing_size_m']}")
    (render_dir / "compare.json").write_text(json.dumps(report, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
