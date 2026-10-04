"""Sample the vector paths of NASA Dryden EG-0075-02 into polylines in render-pixel coordinates.

The SVG draws everything with transform matrix(0.1, 0, 0, -0.1, 0, 221) inside a 269 x 221 pt
viewBox; trace_dfrc.py works on a render 9000 px wide, so pixel = pt * 9000 / 269.
"""
import re
from pathlib import Path

import numpy as np

SVG = Path(__file__).resolve().parents[1] / "plans/pages/dfrc_EG-0075-02_SR-71A_3view.svg"
PX_PER_PT = 9000 / 269


def _bezier(p0, p1, p2, p3, n=16):
    t = np.linspace(0, 1, n)[:, None]
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


def densify(pts, step):
    """Insert points along each segment so consecutive points are at most `step` px apart."""
    out = [pts[0]]
    for a, b in zip(pts[:-1], pts[1:]):
        n = max(1, int(np.ceil(np.linalg.norm(b - a) / step)))
        out.extend(a + (b - a) * (np.arange(1, n + 1)[:, None] / n))
    return np.array(out)


def load():
    s = SVG.read_text()
    out = []
    for i, tag in enumerate(re.findall(r"<path[^>]*>", s)):
        d = re.search(r'd="([^"]*)"', tag)
        if not d:
            continue
        sw = re.search(r'stroke-width="([^"]+)"', tag)
        fill = re.search(r'fill="([^"]+)"', tag)
        toks = re.findall(r"[MCLZ]|-?\d+(?:\.\d+)?", d.group(1))
        pts, subpaths, cur, start = [], [], None, None
        k = 0
        cmd = None
        while k < len(toks):
            t = toks[k]
            if t in "MCLZ":
                cmd = t; k += 1
                if cmd == "Z" and start is not None:
                    pts.append(start); cur = start
                continue
            if cmd == "M":
                if pts:
                    subpaths.append(np.array(pts)); pts = []
                cur = np.array([float(toks[k]), float(toks[k + 1])]); start = cur; pts.append(cur); k += 2; cmd = "L"
            elif cmd == "L":
                cur = np.array([float(toks[k]), float(toks[k + 1])]); pts.append(cur); k += 2
            elif cmd == "C":
                c1 = np.array([float(toks[k]), float(toks[k + 1])]); c2 = np.array([float(toks[k + 2]), float(toks[k + 3])])
                p3 = np.array([float(toks[k + 4]), float(toks[k + 5])])
                pts.extend(list(_bezier(cur, c1, c2, p3)[1:])); cur = p3; k += 6
            else:
                k += 1
        if pts:
            subpaths.append(np.array(pts))
        for sp in subpaths:
            # user units -> pt (y flipped) -> render px
            px = np.stack([sp[:, 0] * 0.1, 221 - sp[:, 1] * 0.1], 1) * PX_PER_PT
            px = densify(px, 4.0)
            out.append({"i": i, "width": float(sw.group(1)) if sw else 0.0, "fill": fill.group(1) if fill else None, "pts": px})
    return out
