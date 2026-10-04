"""Trace NASA Dryden graphic EG-0075-02 (SR-71A three-view, public domain) into calibrated outlines.

  cd model/tools && uv run python trace_dfrc.py <rendered png> ../trace/dfrc

The drawing is rendered from its vector original (rsvg-convert -w 9000). Each view's silhouette is
filled, then calibrated against published stations rather than against the drawing's own scale:

  plan and side: radome tip = FS 102 and tail cone tip = FS 1355 (NASA TM-4749 figs 4 and 5)
  front:         wingtip to wingtip = 55.6 ft (SR-71A flight manual p.1-4)

Outputs, in metres with x = station from the radome tip (positive aft), y = right of centreline,
z = up from the drawing's wing reference line:
  plan.json   upper (right) half envelope y(x), wingtip span, check of span against 55.6 ft
  side.json   top and bottom envelopes z(x)
  front.json  silhouette contour (y, z)
plus *_mask.png and *_overlay.png for review.
"""
import json
import sys
from pathlib import Path

import cv2
import numpy as np

IN = 0.0254
FT = 0.3048
FS_NOSE, FS_TAIL = 102.0, 1355.0          # TM-4749
SPAN_FT = 55.6                             # flight manual p.1-4

VIEWS = {  # pixel boxes in the 9000 px render (padded)
    "plan": (1150, 0, 9000, 4080),
    "side": (1200, 5880, 9000, 7060),
    "front": (0, 3940, 4200, 4960),
}


def silhouette(gray, box):
    x0, y0, x1, y1 = box
    sub = gray[y0:y1, x0:x1]
    ink = (sub < 150).astype(np.uint8) * 255
    ink = cv2.morphologyEx(ink, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))
    h, w = ink.shape
    pad = np.zeros((h + 2, w + 2), np.uint8)
    flood = ink.copy()
    cv2.floodFill(flood, pad, (0, 0), 128)
    sil = (flood != 128).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(sil, 8)
    big = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    return (lab == big).astype(np.uint8), (x0, y0)


def columns(mask):
    """Per pixel column: top row, bottom row (or -1)."""
    has = mask.any(0)
    top = np.where(has, mask.argmax(0), -1)
    bot = np.where(has, mask.shape[0] - 1 - mask[::-1].argmax(0), -1)
    return top, bot, has


def nose_tip(top, bot, has, probe_width_px):
    """First column where the silhouette is clearly wider than the pitot probe."""
    width = np.where(has, bot - top, 0)
    xs = np.where(has)[0]
    first = xs[0]
    for c in range(first, first + 2000):
        if width[c] > 2.2 * probe_width_px and width[c + 3] > width[c]:
            return c, first
    raise RuntimeError("radome tip not found")


def main(png, outdir):
    out = Path(outdir); out.mkdir(parents=True, exist_ok=True)
    gray = cv2.imread(png, cv2.IMREAD_GRAYSCALE)
    stroke = 12.0
    report = {}

    # ---------------- plan
    m, (ox, oy) = silhouette(gray, VIEWS["plan"])
    top, bot, has = columns(m)
    xs = np.where(has)[0]
    probe_w = np.median((bot - top)[xs[0]:xs[0] + 200])
    nose_c, probe_c = nose_tip(top, bot, has, probe_w)
    tail_c = xs[-1]
    rows = np.where(m.any(1))[0]
    tip_top, tip_bot = rows[0], rows[-1]
    centre = (tip_top + tip_bot) / 2
    s_plan = (FS_TAIL - FS_NOSE) * IN / ((tail_c - nose_c))          # metres per px from stations
    span_drawn = (tip_bot - tip_top - stroke) * s_plan
    half = []
    for c in range(nose_c, tail_c + 1):
        if has[c]:
            half.append([round((c - nose_c) * s_plan, 4), round((centre - top[c] - stroke / 2) * s_plan, 4)])
    plan = {
        "source": "NASA Dryden EG-0075-02, plan view", "m_per_px": s_plan,
        "calibration": "radome tip FS 102 to tail cone tip FS 1355 (TM-4749)",
        "length_no_probe_m": round((tail_c - nose_c) * s_plan, 3),
        "probe_m": round((nose_c - probe_c) * s_plan, 3),
        "span_drawn_m": round(span_drawn, 3), "span_published_m": round(SPAN_FT * FT, 3),
        "span_error_pct": round((span_drawn / (SPAN_FT * FT) - 1) * 100, 2),
        "half_outline": half,
        "px": {"nose_x": float(nose_c + ox), "tail_x": float(tail_c + ox), "centre_y": float(centre + oy), "probe_x": float(probe_c + ox)},
    }
    report["plan"] = {k: v for k, v in plan.items() if k not in ("half_outline",)}
    (out / "plan.json").write_text(json.dumps(plan))
    cv2.imwrite(str(out / "plan_mask.png"), m * 255)

    # ---------------- side
    m, (ox, oy) = silhouette(gray, VIEWS["side"])
    # drop the ground line and wheels: keep rows above the lowest fuselage pixel
    top, bot, has = columns(m)
    xs = np.where(has)[0]
    probe_w = np.median((bot - top)[xs[0]:xs[0] + 200])
    nose_c, probe_c = nose_tip(top, bot, has, probe_w)
    tail_c = xs[-1]
    s_side = (FS_TAIL - FS_NOSE) * IN / (tail_c - nose_c)
    ref_row = (top[nose_c] + bot[nose_c]) / 2          # nose tip height as provisional z datum
    env = []
    for c in range(nose_c, tail_c + 1):
        if has[c]:
            env.append([round((c - nose_c) * s_side, 4), round((ref_row - top[c] - stroke / 2) * s_side, 4), round((ref_row - bot[c] + stroke / 2) * s_side, 4)])
    side = {"source": "NASA Dryden EG-0075-02, side view", "m_per_px": s_side,
            "calibration": "radome tip FS 102 to tail cone tip FS 1355 (TM-4749); z = 0 at the radome tip",
            "scale_vs_plan_pct": round((s_side / s_plan - 1) * 100, 2), "envelope": env,
            "px": {"nose_x": float(nose_c + ox), "tail_x": float(tail_c + ox), "ref_y": float(ref_row + oy)}}
    report["side"] = {k: v for k, v in side.items() if k not in ("envelope",)}
    report["side"]["fin_top_above_nose_m"] = round(max(e[1] for e in env), 3)
    report["side"]["lowest_below_nose_m"] = round(min(e[2] for e in env), 3)
    (out / "side.json").write_text(json.dumps(side))
    cv2.imwrite(str(out / "side_mask.png"), m * 255)

    # ---------------- front
    m, (ox, oy) = silhouette(gray, VIEWS["front"])
    top, bot, has = columns(m)
    xs = np.where(has)[0]
    l, r = xs[0], xs[-1]
    s_front = SPAN_FT * FT / (r - l - stroke)
    mid = (l + r) / 2
    cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cs, key=cv2.contourArea)[:, 0, :].astype(float)
    wing_row = np.median([ (top[i] + bot[i]) / 2 for i in range(l + 30, l + 300) if has[i]])
    contour = [[round((px - mid) * s_front, 4), round((wing_row - py) * s_front, 4)] for px, py in c[::2]]
    front = {"source": "NASA Dryden EG-0075-02, front view", "m_per_px": s_front,
             "calibration": "wingtip to wingtip 55.6 ft (flight manual); z = 0 at the outer wing mid-thickness",
             "scale_vs_plan_pct": round((s_front / s_plan - 1) * 100, 2), "contour": contour,
             "px": {"mid_x": float(mid + ox), "wing_y": float(wing_row + oy)}}
    report["front"] = {k: v for k, v in front.items() if k not in ("contour",)}
    (out / "front.json").write_text(json.dumps(front))
    cv2.imwrite(str(out / "front_mask.png"), m * 255)

    (out / "report.json").write_text(json.dumps(report, indent=1))
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
