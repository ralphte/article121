"""Build the SR-71A from geometry measured on NASA Dryden EG-0075-02 (see extract_dfrc.py).

  blender -b --factory-startup --python model/tools/build_sr71_v2.py -- \
      --components model/trace/dfrc/components.json --out model/build/sr71a.glb

Model axes, metres: x aft from the radome tip, y to the right wing, z up from the radome tip.
Blender gets X = -x, Y = y, Z = z (nose toward +X, as render_views.py expects).

Sources for the numbers that are not traced:
  pitot probe 0.914 m: 107.4 ft overall (SR-71A-1 p.1-4) minus 104.4 ft radome-to-tail (TM-4749 stations)
  fin cant 15 deg inboard: Gilyard and Smith, NASA CP-2054 fig 2
  wing section biconvex about 2.5 percent: Kock, NASA CP-2054 table 1
"""
import json
import math
import sys
from pathlib import Path

import bpy
import numpy as np
from mathutils import Vector

PROBE = 0.914
FIN_CANT = math.radians(15.0)


def args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = {"components": "model/trace/dfrc/components.json", "out": "model/build/sr71a.glb", "blend": None}
    for i in range(0, len(argv) - 1, 2):
        out[argv[i].lstrip("-")] = argv[i + 1]
    return out


def table(rows):
    a = np.asarray(rows, float)
    a = a[np.argsort(a[:, 0])]
    return lambda x, left=None, right=None: np.interp(x, a[:, 0], a[:, 1], left=left, right=right)


def smooth(v, k=7):
    if len(v) < k:
        return v
    pad = np.pad(v, (k // 2, k // 2), mode="edge")
    return np.convolve(pad, np.ones(k) / k, mode="valid")


def obj(name, verts, faces, mat, angle=None):
    me = bpy.data.meshes.new(name)
    me.from_pydata([Vector((-x, y, z)) for x, y, z in verts], [], faces)
    me.validate(); me.update()
    ob = bpy.data.objects.new(name, me)
    bpy.context.collection.objects.link(ob)
    ob.data.materials.append(mat)
    bpy.context.view_layer.objects.active = ob
    ob.select_set(True)
    if angle is None:
        bpy.ops.object.shade_flat()
    else:
        bpy.ops.object.shade_smooth_by_angle(angle=math.radians(angle))
    ob.select_set(False)
    return ob


def loft(rings, closed=True, cap_start=False, cap_end=False):
    """rings: list of (n, 3) arrays with equal n. Returns verts, quad faces."""
    n = len(rings[0])
    verts = [tuple(p) for r in rings for p in r]
    faces = []
    m = n if closed else n - 1
    for i in range(len(rings) - 1):
        for j in range(m):
            a, b = i * n + j, i * n + (j + 1) % n
            faces.append((a, b, b + n, a + n))
    if cap_start:
        faces.append(tuple(range(n - 1, -1, -1)))
    if cap_end:
        base = (len(rings) - 1) * n
        faces.append(tuple(base + j for j in range(n)))
    return verts, faces


# ------------------------------------------------------------ fuselage with chine shelf

def fuselage(c, mat):
    L = c["length_no_probe"]
    xs = np.unique(np.concatenate([np.linspace(0, 1.2, 25) ** 1.0, np.arange(1.2, L - 1.0, 0.1), np.linspace(L - 1.0, L, 21)]))
    bw = table(c["body_half_width"])
    top = table(c["fuselage_top_path"])
    bot = table(c["fuselage_bottom_path"])
    chz = table(c["chine_z"])
    plan = np.asarray(c["planform_half"], float)
    env = lambda x: np.interp(x, plan[:, 0], plan[:, 1])
    x_top_end = max(r[0] for r in c["fuselage_top_path"]) - 0.3
    x_bot_end = 17.4
    st, sb = np.asarray(c["side_top"], float), np.asarray(c["side_bottom"], float)
    X_AFT = 30.05                     # behind the fins and nacelles the side silhouette is the tail cone itself
    aft_top = lambda x: float(np.interp(x, st[:, 0], st[:, 1]))
    aft_bot = lambda x: float(np.interp(x, sb[:, 0], sb[:, 1]))
    def fair(x, xa, za, xb, zb, slope_a=0.0, slope_b=0.0):
        t = (x - xa) / (xb - xa)
        h00, h10, h01, h11 = 2*t**3 - 3*t**2 + 1, t**3 - 2*t**2 + t, -2*t**3 + 3*t**2, t**3 - t**2
        return h00 * za + h10 * (xb - xa) * slope_a + h01 * zb + h11 * (xb - xa) * slope_b

    rings, canopy_rings = [], []
    # Canopy: a separate body on the spine from the windscreen foot to where it fairs back in. The
    # traced top line includes it; the spine under it is faired between the stations either side.
    # Half-widths from the drawing's plan-view canopy outlines (paths 162 and 161): pilot's canopy
    # 4.4 to 5.8 m, up to 0.536 m; RSO's 5.9 to 6.8 m, 0.46 m.
    CAN_X0, CAN_X1 = 3.5, 8.5
    spine_slope0 = (float(top(CAN_X0)) - float(top(CAN_X0 - 0.5))) / 0.5
    HW_X = [3.5, 3.65, 3.9, 4.4, 5.2, 5.8, 6.4, 7.0, 7.6, 8.1, 8.5]
    HW_Y = [0.02, 0.2, 0.34, 0.5, 0.536, 0.5, 0.465, 0.44, 0.36, 0.2, 0.03]
    # how far out from the centreline the upper fillet reaches (m), by station
    FIL_X = [15.9, 17.7, 21.0, 22.6, 27.5, 29.5, 30.4]
    FIL_R = [float(env(15.9)), 3.0, 3.0, 1.6, 1.3, 1.1, 0.0]
    for x in xs:
        # body half-width: traced line, tapered into the radome tip and the tail cone tip
        b = float(bw(x, left=np.nan, right=np.nan))
        if np.isnan(b):
            b = float(bw(0.97)) * (x / 0.97) ** 0.8 if x < 1 else float(bw(30.9)) * max(0.0, (L - x) / (L - 30.9))
        b = max(b, 0.004)
        # top and bottom: traced where visible, then a fair curve to the tail cone tip
        if x <= x_top_end:
            zt = float(top(x))
            z_canopy = zt
            if CAN_X0 < x < CAN_X1:          # the forebody spine runs on under the canopy
                zt = fair(x, CAN_X0, float(top(CAN_X0)), CAN_X1, float(top(CAN_X1)), spine_slope0, 0.0)
        elif x < X_AFT:
            zt = fair(x, x_top_end, float(top(x_top_end)), X_AFT, aft_top(X_AFT), 0.0, (aft_top(X_AFT + 0.3) - aft_top(X_AFT)) / 0.3)
        else:
            zt = aft_top(x)
        if x <= x_bot_end:
            zb = float(bot(x))
        elif x < X_AFT:
            zb = fair(x, x_bot_end, float(bot(x_bot_end)), X_AFT, aft_bot(X_AFT), 0.0, (aft_bot(X_AFT + 0.3) - aft_bot(X_AFT)) / 0.3)
        else:
            zb = aft_bot(x)
        if x > L - 0.02:
            zt = zb = (aft_top(L - 0.05) + aft_bot(L - 0.05)) / 2
        if x < 0.05:
            zt = zb = 0.0
        zc = float(chz(x)) if x < 16.3 else float(chz(16.3))
        zc = min(max(zc, zb + 0.02), zt - 0.02) if zt - zb > 0.05 else (zt + zb) / 2
        # chine edge: the traced outline forward of the wing junction (sections 1 to 9)
        w = float(env(min(x, 15.9)))
        w = max(w, b)
        z0 = float(chz(x))
        # Forebody section (sections 1 to 9): a tent with concave flanks rising from the sharp chine edge
        # to a rounded spine, over a shallow V belly about half as deep. Measured off the section
        # drawing: height falls as (1 - u)^1.3 from the spine (u = 0) to the chine edge (u = 1).
        # Sections 1 to 3 carry a narrower hump on a flat chine shelf (uh is the hump's share of w).
        s_tent = 1.0 if x < 15.9 else max(0.0, 1.0 - (x - 15.9) / 1.6)
        uh = min(1.0, max(0.5, 0.5 + 0.5 * (x - 0.8) / 2.3))
        R_TOP, R_BOT = 0.14, 0.18
        d1t, d1b = math.hypot(1, R_TOP) - R_TOP, math.hypot(1, R_BOT) - R_BOT
        def tent_up(y):
            u = min(1.0, y / w / uh)
            return zc + (zt - zc) * max(0.0, 1 - (math.hypot(u, R_TOP) - R_TOP) / d1t) ** 1.3
        def tent_lo(y):
            u = min(1.0, y / w)
            return zc - (zc - zb) * max(0.0, 1 - (math.hypot(u, R_BOT) - R_BOT) / d1b) ** 1.05
        # Wing-body section behind the inlets (sections 10 to 16): a round body; between it and the
        # nacelle the underside runs straight from the body to the nacelle (a shallow V), and on top a
        # concave fillet descends from high on the body side to the wing, reaching all the way to the
        # nacelle at sections 10 to 13 and about 1.3 m out at 14 to 16. The section closes at W: the
        # inboard leading edge ahead of the cowl, inside the nacelle along it, the planform behind it.
        if x >= 15.9:
            if x < 29.4:
                W = min(float(env(15.92)) + 0.505 * (x - 15.92), 3.337 + 0.25) - 0.01
            else:
                W = float(env(x)) - 0.01
            W = max(W, b)
            Rf = min(W, max(b, float(np.interp(x, FIL_X, FIL_R))))
        else:
            W, Rf = w, w
        def round_up(y):
            u = min(1.0, y / max(b, 1e-6))
            return zc + (zt - zc) * max(0.0, 1 - u ** 2.3) ** (1 / 2.3)
        def round_lo(y):
            u = min(1.0, y / max(b, 1e-6))
            return zc - (zc - zb) * max(0.0, 1 - u ** 2.3) ** (1 / 2.3)
        def body_up(y):
            ys_ = 0.74 * b
            if y <= ys_ or Rf <= ys_ + 1e-3:
                return round_up(min(y, b)) if y <= b else z0
            if y >= Rf:
                return z0
            za, h = round_up(ys_), Rf - ys_
            dy = min(0.01, ys_ / 2)
            m0 = (round_up(ys_) - round_up(ys_ - dy)) / max(dy, 1e-6)
            lim = 3 * abs(za - z0) / h
            m0 = max(-lim, min(lim, m0)) if (z0 - za) * m0 >= 0 else 0.0
            t = (y - ys_) / h
            return (2*t**3 - 3*t**2 + 1) * za + (t**3 - 2*t**2 + t) * h * m0 + (-2*t**3 + 3*t**2) * z0
        # underside: the lower body curve and its tangent line out to (W, z0)
        q = np.linspace(0, b, 40)
        zq = np.array([round_lo(v) for v in q])
        sl = (z0 - zq) / np.maximum(W - q, 1e-6)
        k_t = int(np.argmax(sl)) if W > b + 1e-3 else len(q) - 1
        y_t, s_t = float(q[k_t]), float(sl[k_t])
        def body_lo(y):
            if y <= y_t:
                return round_lo(y)
            return z0 - s_t * (W - y) if W > b + 1e-3 else round_lo(min(y, b))
        if x < 0.05:
            zt = zb = zc = 0.0
        WW = max(w if s_tent > 0 else 0.0, W)
        N_U, N_L = 34, 26
        half = []
        for t in np.linspace(0, 1, N_U):                   # spine out to the chine or wing edge
            y = WW * (1 - math.cos(t * math.pi / 2)) ** 0.85 if t < 1 else WW
            half.append((y, s_tent * tent_up(min(y, w)) + (1 - s_tent) * body_up(min(y, W))))
        for t in np.linspace(0, 1, N_L + 1)[1:]:           # back to the keel
            y = WW * (1 - t)
            half.append((y, s_tent * tent_lo(min(y, w)) + (1 - s_tent) * body_lo(min(y, W))))
        if CAN_X0 <= x <= CAN_X1:
            hw = float(np.interp(x, HW_X, HW_Y))
            zs = tent_up(hw)
            h = max(z_canopy - zs, 0.005)
            ring = []
            for th in np.linspace(0, math.pi, 29):            # roof, right to left
                yy = hw * math.cos(th)
                ring.append((x, yy, zs + h * max(0.0, 1 - abs(yy / hw) ** 2.6) ** (1 / 2.6)))
            for yy in np.linspace(-hw, hw, 13)[1:-1]:           # floor, buried in the forebody
                ring.append((x, yy, tent_up(abs(yy)) - 0.08))
            canopy_rings.append(np.array(ring))
        right = np.array(half)
        left = right[1:-1][::-1] * [-1, 1]
        sec = np.vstack([right, left])
        rings.append(np.column_stack([np.full(len(sec), x), sec[:, 0], sec[:, 1]]))
    v, f = loft(rings)
    body = obj("Fuselage", v, f, mat, angle=50)
    v, f = loft(canopy_rings, cap_start=True, cap_end=True)
    return [body, obj("Canopy", v, f, mat, angle=35)]


# ------------------------------------------------------------ wing

def wing(c, mat):
    plan = np.asarray(c["planform_half"], float)
    env = lambda x: np.interp(x, plan[:, 0], plan[:, 1])
    chz = table(c["chine_z"])
    L = c["length_no_probe"]
    x0 = 15.3
    xs = np.arange(x0, L - 0.4, 0.05)

    def half_span(x):
        if x < 18.0:   # inboard leading edge runs from the chine to the nacelle; spike and cowl hide it in plan
            return float(min(env(x), env(15.92) + 0.505 * (x - 15.92))) if x >= 15.92 else float(env(x))
        return float(env(x))

    ys_out = np.array([half_span(x) for x in xs])
    # polygon of the wing outline for edge distances
    poly = np.vstack([np.column_stack([xs, ys_out]), [[xs[-1], 0.0], [x0, 0.0]]])
    a, bb = poly, np.roll(poly, -1, 0)
    ab = bb - a
    def edge_dist(px, py):
        ap = np.stack([px - a[:, 0], py - a[:, 1]], 1)
        t = np.clip((ap * ab).sum(1) / np.maximum((ab * ab).sum(1), 1e-12), 0, 1)
        d = ap - ab * t[:, None]
        dd = np.sqrt((d * d).sum(1))
        # ignore the closing edges along the centreline and the root
        dd[-2:] = 1e9
        return float(dd.min())

    T_MAX, REACH = 0.11, 1.9
    # leading edge station for a given span position on the outer wing (first x where the outline reaches y)
    _xs_le, _ys_le = xs[xs > 17.5], ys_out[xs > 17.5]
    def le_x(y):
        hit = np.where(_ys_le >= y)[0]
        return float(_xs_le[hit[0]]) if len(hit) else float(_xs_le[-1])
    span_n = 46
    upper, lower = [], []
    for x, Y in zip(xs, ys_out):
        ys = Y * (1 - np.cos(np.linspace(0, math.pi / 2, span_n))) ** 0.9
        ys[-1] = Y
        z0 = float(chz(x))
        u, l = [], []
        for y in ys:
            t = T_MAX * min(1.0, edge_dist(x, y) / REACH) ** 0.62
            # conical camber on the outer wing (Lockheed section drawing): the leading edge droops
            # toward the tip; up to about 0.16 m at the tip, fading 1.8 m aft of the edge
            droop = 0.0
            if y > 5.3:
                d_le = x - le_x(y)
                droop = 0.16 * ((y - 5.3) / (8.48 - 5.3)) * max(0.0, 1 - d_le / 1.8) ** 2
            u.append((x, y, z0 + t - droop)); l.append((x, y, z0 - t * 0.85 - droop))
        upper.append(u); lower.append(l)

    def mirror(rows):
        out = []
        for r in rows:
            left = [(x, -y, z) for (x, y, z) in reversed(r[1:])]
            out.append(np.array(left + r))
        return out
    U, Lw = mirror(upper), mirror(lower)
    vu, fu = loft(U, closed=False)
    vl, fl = loft(Lw, closed=False)
    off = len(vu)
    faces = fu + [tuple(off + i for i in reversed(q)) for q in fl]
    return obj("Wing", vu + vl, faces, mat, angle=40)


# ------------------------------------------------------------ nacelles, spikes, fins

def nacelle_rings(c):
    out_y, in_y = table(c["nacelle_plan_outer"]), table(c["nacelle_plan_inner"])
    top, bot = table(c["nacelle_side_top"]), table(c["nacelle_side_bottom"])
    cowl = np.asarray(c["cowl_plan"], float)
    x_lip = float(cowl[:, 0].min())
    lip_c, lip_r = (cowl[:, 1].max() + cowl[:, 1].min()) / 2, (cowl[:, 1].max() - cowl[:, 1].min()) / 2
    xs = np.arange(x_lip, 29.45, 0.05)
    ys, zs, aa, bbv = [], [], [], []
    for x in xs:
        o = float(out_y(x, left=np.nan, right=np.nan)); i = float(in_y(x, left=np.nan, right=np.nan))
        if np.isnan(i):
            i = 3.337 if x > 19 else np.nan
        if np.isnan(o):
            o = 5.11 if x > 19 else np.nan
        if np.isnan(o) or np.isnan(i):    # inlet region: blend from the cowl lip to the traced edges
            k = min(1.0, (x - x_lip) / (19.0 - x_lip))
            yc = lip_c * (1 - k) + 4.224 * k
            a = lip_r * (1 - k) + 0.887 * k
        else:
            yc, a = (o + i) / 2, (o - i) / 2
        t, b_ = float(top(x, left=np.nan, right=np.nan)), float(bot(x, left=np.nan, right=np.nan))
        if np.isnan(t) or np.isnan(b_) or x < 18.0:
            t, b_ = float(top(18.0)), float(bot(18.0))
            zc = (t + b_) / 2 - (18.0 - x) * 0.045
            b2 = a * 1.08
        else:
            zc, b2 = (t + b_) / 2, (t - b_) / 2
        if x > 26.2:                        # aft nacelle and ejector: gentle boat-tail to the nozzle
            k = (x - 26.2) / (29.45 - 26.2)
            a = a * (1 - 0.14 * k ** 1.5); b2 = b2 * (1 - 0.18 * k ** 1.5)
        ys.append(yc); zs.append(zc); aa.append(a); bbv.append(b2)
    return xs, smooth(np.array(ys)), smooth(np.array(zs)), smooth(np.array(aa)), smooth(np.array(bbv)), x_lip


def nacelles(c, mat, dark):
    xs, ys, zs, aa, bbv, x_lip = nacelle_rings(c)
    seg = 56
    ang = np.linspace(0, 2 * math.pi, seg, endpoint=False)
    objs = []
    sp = np.asarray(c["spike_plan"], float)
    tip = sp[sp[:, 0].argmin()]
    for side in (1, -1):
        rings = [np.column_stack([np.full(seg, x), side * y + a * np.cos(ang), z + b * np.sin(ang)]) for x, y, z, a, b in zip(xs, ys, zs, aa, bbv)]
        v, f = loft(rings)
        objs.append(obj(f"Nacelle {'R' if side > 0 else 'L'}", v, f, mat, angle=60))
        # spike: traced tip and lip-plane radius, then a cylinder back inside the inlet
        tip_x, tip_y = float(tip[0]), float(tip[1])
        base_x, base_y, base_r = 17.40, 4.205, 0.448
        tip_z = float(zs[0]) - 0.03
        prof = [(tip_x, 0.0), (tip_x + 0.15, 0.035), (base_x - 0.6, base_r * 0.62), (base_x, base_r), (18.3, 0.56), (19.2, 0.58)]
        rings = []
        for x, r in prof:
            k = min(1.0, (x - tip_x) / (base_x - tip_x))
            yc = tip_y + (base_y - tip_y) * k
            zc = tip_z + (float(zs[0]) - tip_z) * k
            rings.append(np.column_stack([np.full(seg, x), side * yc + max(r, 1e-3) * np.cos(ang), zc + max(r, 1e-3) * np.sin(ang)]))
        v, f = loft(rings)
        objs.append(obj(f"Spike {'R' if side > 0 else 'L'}", v, f, mat, angle=50))
        for label, x, y, z, r in (("Engine face", 19.0, ys[np.searchsorted(xs, 19.0)], zs[np.searchsorted(xs, 19.0)], 0.62),
                                  ("Nozzle", xs[-1] - 0.25, ys[-1], zs[-1], 0.92 * min(aa[-1], bbv[-1]))):
            verts = [(x, side * y + r * math.cos(t), z + r * math.sin(t)) for t in ang]
            objs.append(obj(f"{label} {'R' if side > 0 else 'L'}", verts, [tuple(range(seg))], dark))
    return objs


def fins(c, mat):
    """Fin outline from the side view, height set by published numbers.

    Kock (CP-2054 table 1) gives the vertical tail span as 3.302 m; with the 15 deg cant and the
    6.92 m tip separation in Gilyard (CP-2054 fig 2) that span is measured from the nacelle
    centreline, so the tip sits 3.302 cos 15 = 3.19 m above the nacelle axis. The drawing's side
    view puts it about 0.3 m higher and its front view about 0.5 m lower, so the outline's chord
    positions come from the side view and its height is scaled to the published value.
    """
    xs, ys, zs, aa, bbv, _ = nacelle_rings(c)
    loop = np.asarray(c["fin_side"], float)
    keep = [0]
    for i in range(1, len(loop)):
        if np.linalg.norm(loop[i] - loop[keep[-1]]) > 0.04:
            keep.append(i)
    loop = loop[keep]
    z_root_line = lambda x: float(np.interp(x, [24.774, 29.931], [1.59, 1.989]))
    zc = lambda x: float(np.interp(x, xs, zs))
    yc = lambda x: float(np.interp(x, xs, ys))
    z_tip_drawn = float(loop[:, 1].max())
    x_tip = float(loop[loop[:, 1].argmax(), 0])
    target_tip = zc(x_tip) + 3.302 * math.cos(FIN_CANT)
    k = (target_tip - z_root_line(x_tip)) / (z_tip_drawn - z_root_line(x_tip))
    objs = []
    th = 0.055
    for side in (1, -1):
        rings = []
        for off in (+th, -th):
            ring = []
            for x, z in loop:
                zr = z_root_line(x)
                z2 = zr + (z - zr) * k if z > zr else z - 0.25        # sink the root into the nacelle
                h = z2 - zc(x)                                         # height above the nacelle axis
                taper = 1.0 - 0.75 * min(1.0, max(h, 0) / 3.2)
                y = side * (yc(x) - h * math.tan(FIN_CANT)) + side * off * taper * math.cos(FIN_CANT)
                ring.append((x, y, z2))
            rings.append(np.array(ring))
        v, f = loft(rings, closed=True)
        n = len(rings[0])
        f.append(tuple(range(n)))
        f.append(tuple(range(2 * n - 1, n - 1, -1)))
        objs.append(obj(f"Fin {'R' if side > 0 else 'L'}", v, f, mat, angle=30))
    print(f"FIN tip z {target_tip:.3f} (drawn {z_tip_drawn:.3f}), height scale {k:.3f}")
    return objs


def probe(mat):
    seg = 16
    ang = np.linspace(0, 2 * math.pi, seg, endpoint=False)
    prof = [(-PROBE, 0.012), (-PROBE + 0.05, 0.025), (-0.25, 0.03), (0.02, 0.045)]
    rings = [np.column_stack([np.full(seg, x), r * np.cos(ang), r * np.sin(ang)]) for x, r in prof]
    v, f = loft(rings, cap_start=True)
    return obj("Pitot probe", v, f, mat, angle=60)


def main():
    a = args()
    c = json.loads(Path(a["components"]).read_text())
    bpy.ops.wm.read_factory_settings(use_empty=True)
    skin = bpy.data.materials.new("Blackbird skin"); skin.use_nodes = True
    p = skin.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = (0.018, 0.02, 0.026, 1); p.inputs["Metallic"].default_value = 0.35; p.inputs["Roughness"].default_value = 0.5
    dark = bpy.data.materials.new("Intake and nozzle"); dark.use_nodes = True
    dark.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.002, 0.002, 0.003, 1)
    parts = fuselage(c, skin) + [wing(c, skin), probe(skin)] + nacelles(c, skin, dark) + fins(c, skin)
    root = bpy.data.objects.new("SR-71A", None); bpy.context.collection.objects.link(root)
    for o in parts:
        o.parent = root
    out = Path(a["out"]); out.parent.mkdir(parents=True, exist_ok=True)
    if a.get("blend"):
        bpy.ops.wm.save_as_mainfile(filepath=str(Path(a["blend"]).resolve()))
    bpy.ops.export_scene.gltf(filepath=str(out.resolve()), export_format="GLB", export_apply=True, export_yup=True)
    print(f"BUILT {out} parts={len(parts)} faces={sum(len(o.data.polygons) for o in parts)}")


if __name__ == "__main__":
    main()
