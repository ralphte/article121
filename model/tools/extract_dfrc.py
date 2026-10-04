"""Extract component geometry from the vector paths of NASA Dryden EG-0075-02.

Uses the datums found by trace_dfrc.py (../trace/dfrc/*.json) to convert identified paths into
metres, and writes ../trace/dfrc/components.json. Path numbers were identified on labelled
overlays of each view (see README in ../trace/dfrc).
"""
import json
from pathlib import Path

import numpy as np

from svg_paths import load

HERE = Path(__file__).resolve().parent
T = HERE.parent / "trace/dfrc"
plan, side, front = (json.loads((T / f"{v}.json").read_text()) for v in ("plan", "side", "front"))
by = {}
for p in load():
    by.setdefault(p["i"], []).append(p["pts"])


def pts(i):
    return np.vstack(by[i])


def plan_m(q):
    return np.stack([(q[:, 0] - plan["px"]["nose_x"]) * plan["m_per_px"], (plan["px"]["centre_y"] - q[:, 1]) * plan["m_per_px"]], 1)


def side_m(q):
    return np.stack([(q[:, 0] - side["px"]["nose_x"]) * side["m_per_px"], (side["px"]["ref_y"] - q[:, 1]) * side["m_per_px"]], 1)


def front_m(q):
    return np.stack([(q[:, 0] - front["px"]["mid_x"]) * front["m_per_px"], (front["px"]["wing_y"] - q[:, 1]) * front["m_per_px"]], 1)


def profile(m, xs, which="max"):
    """Resample a set of (x, v) points as v(x) on xs, taking max or min where several points share an x."""
    order = np.argsort(m[:, 0])
    x, v = m[order, 0], m[order, 1]
    out = []
    for xi in xs:
        sel = np.abs(x - xi) < 0.06
        out.append(float((v[sel].max() if which == "max" else v[sel].min())) if sel.any() else np.nan)
    return np.array(out)


def summary(name, m):
    print(f"{name:28s} x {m[:,0].min():7.3f}..{m[:,0].max():7.3f}   v {m[:,1].min():7.3f}..{m[:,1].max():7.3f}")


if __name__ == "__main__":
    for i, lab in [(316, "plan fuselage body fwd"), (292, "plan fuselage body aft"), (264, "plan nacelle outer"), (263, "plan nacelle inner"),
                   (282, "plan cowl lip"), (262, "plan spike"), (284, "plan fin"), (305, "plan inboard wing line"), (317, "plan chine bay line")]:
        summary(lab, plan_m(pts(i)))
    for i, lab in [(349, "side fuselage"), (421, "side chine fwd"), (413, "side chine/wing aft"), (332, "side nacelle"), (414, "side spike"),
                   (333, "side fin"), (335, "side fin rudder line"), (422, "side canopy 1"), (426, "side canopy 2")]:
        summary(lab, side_m(pts(i)))
    for i, lab in [(431, "front cowl R"), (453, "front cowl L"), (439, "front spike tip R"), (461, "front spike tip L"), (467, "front fuselage blue"), (445, "front fuselage teal")]:
        summary(lab, front_m(pts(i)))


def build_components():
    """Profiles sampled every 10 cm, in model axes: x aft from the radome tip, y right, z up from the radome tip."""
    L = plan["length_no_probe_m"]
    xs = np.round(np.arange(0, L + 1e-6, 0.1), 3)
    env_plan = np.array(plan["half_outline"])
    env_side = np.array(side["envelope"])       # x, top, bottom (whole side silhouette)

    def resample(arr, col, x):
        return np.interp(x, arr[:, 0], arr[:, col])

    comp = {"source": "NASA Dryden EG-0075-02 (vector), calibrated to TM-4749 stations; see trace/dfrc/report.json",
            "length_no_probe": L}
    comp["planform_half"] = np.round(env_plan[::4], 4).tolist()

    # fuselage body half-width (plan paths 316 fwd, 292 aft), nose taper from the outline
    body = np.vstack([plan_m(pts(316)), plan_m(pts(292))])
    bw = profile(body, xs, "max")
    comp["body_half_width"] = [[float(x), round(float(v), 4)] for x, v in zip(xs, bw) if not np.isnan(v)]

    # side: fuselage top and bottom forward of the inlets come straight from the silhouette
    comp["side_top"] = [[float(x), round(float(resample(env_side, 1, x)), 4)] for x in xs]
    comp["side_bottom"] = [[float(x), round(float(resample(env_side, 2, x)), 4)] for x in xs]
    fus = side_m(pts(349))
    comp["fuselage_top_path"] = [[float(x), round(float(v), 4)] for x, v in zip(xs, profile(fus, xs, "max")) if not np.isnan(v)]
    comp["fuselage_bottom_path"] = [[float(x), round(float(v), 4)] for x, v in zip(xs, profile(fus, xs, "min")) if not np.isnan(v)]

    # chine line in side view (421 forward, 413 aft = wing edge)
    ch = np.vstack([side_m(pts(421)), side_m(pts(413))])
    comp["chine_z"] = [[float(x), round(float(v), 4)] for x, v in zip(xs, profile(ch, xs, "max")) if not np.isnan(v)]

    # nacelle: plan edges (264 outer, 263 inner), cowl (282), spike (262); side outline (332), spike (414)
    no, ni = plan_m(pts(264)), plan_m(pts(263))
    so = side_m(pts(332))
    nx = np.round(np.arange(17.6, 29.6, 0.1), 3)
    comp["nacelle_plan_outer"] = [[float(x), round(float(v), 4)] for x, v in zip(nx, profile(no, nx, "max")) if not np.isnan(v)]
    comp["nacelle_plan_inner"] = [[float(x), round(float(v), 4)] for x, v in zip(nx, profile(ni, nx, "min")) if not np.isnan(v)]
    comp["nacelle_side_top"] = [[float(x), round(float(v), 4)] for x, v in zip(nx, profile(so, nx, "max")) if not np.isnan(v)]
    comp["nacelle_side_bottom"] = [[float(x), round(float(v), 4)] for x, v in zip(nx, profile(so, nx, "min")) if not np.isnan(v)]
    comp["cowl_plan"] = np.round(plan_m(pts(282)), 4).tolist()
    comp["spike_plan"] = np.round(plan_m(pts(262)), 4).tolist()
    comp["spike_side"] = np.round(side_m(pts(414)), 4).tolist()
    comp["fin_side"] = np.round(side_m(pts(333)), 4).tolist()
    comp["fin_plan"] = np.round(plan_m(pts(284)), 4).tolist()
    comp["front_contour"] = front["contour"]
    comp["front_cowl"] = np.round(front_m(pts(431)), 4).tolist()
    comp["front_spike_tip"] = np.round(front_m(pts(439)), 4).tolist()
    (T / "components.json").write_text(json.dumps(comp))
    return comp


if __name__ == "__main__":
    c = build_components()
    print("components:", {k: (len(v) if isinstance(v, list) else v) for k, v in c.items()})
