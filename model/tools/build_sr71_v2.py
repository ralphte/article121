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
# The chine meets the inboard leading edge at FS 712 (SR-71A-1 fig. 4-37; TM-4749 fig. 4 has
# FS 708). The traced planform kinks at the same place; the leading edge then runs straight out
# to the nacelle at the traced slope.
JX = 15.50
LE_SLOPE = 0.505
# Nacelle exit FS 1234 (SR-71A-1 fig. 4-37 plan); the bare-metal ejector flaps are its last 0.7 m.
NAC_EXIT = 28.75
EJECTOR_X = NAC_EXIT - 0.7
# Inlet: cowl lip radius Rc = 29.38 in (TM X-3144 fig. 8). The spike axis is canted 5.3 deg nose
# down and toed in 3.25 deg (TN D-6987 fig. 2).
RC = 0.7462
SPIKE_DOWN, SPIKE_IN = math.tan(math.radians(5.3)), math.tan(math.radians(3.25))
# Inlet sections from CR-163106 fig. 4 (spike forward), in cowl radii aft of the cowl lip:
# spike and centrebody radius, and the duct's outer wall. The spike is a 26 deg cone whose tip
# stands 3.35 Rc ahead of the lip when forward, as it is on the ground and below Mach 1.6.
SPIKE_R = [(-3.35, 0.0), (-3.20, 0.034), (-0.30, 0.686), (-0.10, 0.731), (0.0, 0.752), (0.15, 0.768),
           (0.35, 0.770), (0.60, 0.755), (1.0, 0.690), (1.25, 0.655), (1.5, 0.615), (2.0, 0.565), (2.25, 0.530),
           (2.5, 0.490), (2.68, 0.462), (2.70, 0.372), (3.0, 0.352), (4.9, 0.290), (5.25, 0.285), (5.40, 0.27)]
DUCT_R = [(0.0, 1.0), (0.4, 1.025), (0.8, 1.03), (1.2, 0.99), (1.45, 0.95), (1.6, 0.915), (2.2, 0.85),
          (3.0, 0.805), (4.0, 0.785), (5.4, 0.765)]


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


def smooth_table(rows, sigma=0.08, step=0.01, keep=()):
    """A traced profile resampled every `step` metres and smoothed with a Gaussian of `sigma`
    metres, so pixel-scale tracing noise does not show as banding in glossy reflections.
    `keep` lists (x0, x1) spans left unsmoothed (real corners such as the chine junction)."""
    a = np.asarray(rows, float)
    a = a[np.argsort(a[:, 0])]
    gx = np.arange(a[0, 0], a[-1, 0] + step / 2, step)
    gy = np.interp(gx, a[:, 0], a[:, 1])
    r = int(3 * sigma / step)
    k = np.exp(-0.5 * (np.arange(-r, r + 1) * step / sigma) ** 2); k /= k.sum()
    sm = np.convolve(np.pad(gy, r, mode="edge"), k, mode="valid")
    for x0, x1 in keep:
        m = (gx >= x0) & (gx <= x1)
        sm[m] = gy[m]
    return lambda x, left=None, right=None: np.interp(x, gx, sm, left=left, right=right)


def smooth(v, k=7):
    if len(v) < k:
        return v
    pad = np.pad(v, (k // 2, k // 2), mode="edge")
    return np.convolve(pad, np.ones(k) / k, mode="valid")


def obj(name, verts, faces, mat, angle=None, extra=None, face_mat=None, uv=None):
    """extra: further materials; face_mat: per-face material index (0 = mat, 1.. = extra);
    uv: a texture coordinate per vertex, for the textured panels and markings."""
    me = bpy.data.meshes.new(name)
    # model frame (x aft, y to the right wing, z up) to Blender (nose toward +X): a half turn about
    # z, not a mirror, so the right wing stays on the aircraft's right and lettering reads true
    me.from_pydata([Vector((-x, -y, z)) for x, y, z in verts], [], faces)
    if face_mat is not None:
        for poly, k in zip(me.polygons, face_mat):
            poly.material_index = k
    if uv is not None:
        lay = me.uv_layers.new(name="UVMap")
        for lp in me.loops:
            lay.data[lp.index].uv = uv[lp.vertex_index]
    me.validate(); me.update()
    ob = bpy.data.objects.new(name, me)
    bpy.context.collection.objects.link(ob)
    ob.data.materials.append(mat)
    for m in extra or []:
        ob.data.materials.append(m)
    bpy.context.view_layer.objects.active = ob
    ob.select_set(True)
    # consistent normals: outward for skins, inward for the duct liners (mirrored parts arrive flipped)
    bpy.ops.object.mode_set(mode="EDIT"); bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.normals_make_consistent(inside=("liner" in name.lower() or "duct" in name.lower()))
    bpy.ops.object.mode_set(mode="OBJECT")
    if angle is None:
        bpy.ops.object.shade_flat()
    else:
        bpy.ops.object.shade_smooth_by_angle(angle=math.radians(angle))
    ob.select_set(False)
    return ob


FSX = lambda fs: (fs - 102) * 0.0254      # fuselage station (in) to metres aft of the radome tip
LINE_W, LINE_LIFT = 0.012, 0.003           # panel lines: drawn width and height above the skin


def ribbon(pts, nrm, closed=False, w=LINE_W, lift=LINE_LIFT):
    """A thin strip lying `lift` above a surface along the polyline pts (k, 3), whose outward
    normals are nrm (k, 3): a panel line or a door edge, drawn in its own material."""
    pts, nrm = np.asarray(pts, float), np.asarray(nrm, float)
    nrm = nrm / (np.linalg.norm(nrm, axis=1)[:, None] + 1e-12)
    k = len(pts)
    tan = (np.roll(pts, -1, 0) - np.roll(pts, 1, 0)) if closed else np.gradient(pts, axis=0)
    sd = np.cross(tan, nrm)
    sd /= np.linalg.norm(sd, axis=1)[:, None] + 1e-12
    base = pts + nrm * lift
    a, b = base - sd * w / 2, base + sd * w / 2
    verts = [tuple(p) for pair in zip(a, b) for p in pair]
    m = k if closed else k - 1
    faces = [(2 * i, 2 * ((i + 1) % k), 2 * ((i + 1) % k) + 1, 2 * i + 1) for i in range(m)]
    return verts, faces


def with_extra(v, f, fm, pieces, start_uv=None):
    """Append pieces [(verts, faces, material index, uvs or None)] to a mesh; returns the merged
    verts, faces, per-face materials and per-vertex uvs (None when nothing is textured)."""
    v, f, fm = list(v), list(f), list(fm)
    uvs = list(start_uv) if start_uv is not None else [(0.0, 0.0)] * len(v)
    textured = start_uv is not None
    for pv, pf, mi, puv in pieces:
        o = len(v)
        v += list(pv); f += [tuple(o + k for k in q) for q in pf]; fm += [mi] * len(pf)
        uvs += list(puv) if puv is not None else [(0.0, 0.0)] * len(pv)
        textured |= puv is not None
    return v, f, fm, (uvs if textured else None)


def tag(ob, part, layer, explode=(0.0, 0.0, 0.0), accuracy="measured"):
    """Metadata the web viewer reads from the glTF extras: a stable part id, its layer, the
    exploded-view offset in metres (model frame: x aft, y to the right wing, z up; converted
    to glTF axes here) and whether the geometry is measured from drawings or representative."""
    dx, dy, dz = explode
    ob["a121_part"] = part
    ob["a121_layer"] = layer
    ob["a121_explode"] = [-dx, dz, dy]
    ob["a121_accuracy"] = accuracy
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
    base = np.arange(1.2, L - 1.0, 0.1)
    xs = np.unique(np.round(np.concatenate([np.linspace(0, 1.2, 25), base[(base < 3.3) | (base > 8.7)],
                                            np.arange(3.3, 8.7, 0.04), np.linspace(L - 1.0, L, 21)]), 4))
    bw = smooth_table(c["body_half_width"])
    top = smooth_table(c["fuselage_top_path"], sigma=0.06)
    bot = smooth_table(c["fuselage_bottom_path"])
    chz = smooth_table(c["chine_z"], sigma=0.15)
    plan = np.asarray(c["planform_half"], float)
    env = smooth_table(plan, sigma=0.06, keep=((JX - 0.2, 16.3), (29.0, 33.0)))
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

    rings, can_params = [], []
    # Canopy: a separate body on the spine from the windscreen foot to where it fairs back in. The
    # traced top line includes it; the spine under it is faired between the stations either side.
    # Half-widths from the drawing's plan-view canopy outlines (paths 162 and 161): pilot's canopy
    # 4.4 to 5.8 m, up to 0.536 m; RSO's 5.9 to 6.8 m, 0.46 m.
    CAN_X0, CAN_X1 = 3.5, 8.5
    spine_slope0 = (float(top(CAN_X0)) - float(top(CAN_X0 - 0.5))) / 0.5
    HW_X = [3.5, 3.65, 3.9, 4.4, 5.2, 5.8, 6.4, 7.0, 7.6, 8.1, 8.5]
    HW_Y = [0.02, 0.2, 0.34, 0.5, 0.536, 0.5, 0.465, 0.44, 0.36, 0.2, 0.03]
    # how far out from the centreline the upper fillet reaches (m), by station
    FIL_X = [JX, 17.7, 21.0, 22.6, 27.5, 29.4, 30.6]
    FIL_R = [float(env(JX)), 3.0, 3.0, 1.6, 1.3, 1.0, 0.0]
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
        w = float(env(min(x, JX)))
        w = max(w, b)
        z0 = float(chz(x))
        # Forebody section (sections 1 to 9): a tent with concave flanks rising from the sharp chine edge
        # to a rounded spine, over a shallow V belly about half as deep. Measured off the section
        # drawing: height falls as (1 - u)^1.3 from the spine (u = 0) to the chine edge (u = 1).
        # Sections 1 to 3 carry a narrower hump on a flat chine shelf (uh is the hump's share of w).
        s_tent = 1.0 if x < JX else max(0.0, 1.0 - (x - JX) / 1.6)
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
        if x >= JX:
            if x < 29.4:
                W = min(float(env(JX)) + LE_SLOPE * (x - JX), 3.337 + 0.25) - 0.01
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
        # behind the junction the wing-level parts of the section sit 1.5 cm under the wing's mid
        # plane, so the wing skin always covers them (coincident skins render as a crumpled patch)
        zw = z0 - 0.015 if x >= JX else z0
        def body_up(y):
            ys_ = 0.74 * b
            if y <= ys_ or Rf <= ys_ + 1e-3:
                return round_up(min(y, b)) if y <= b else zw
            if y >= Rf:
                return zw
            za, h = round_up(ys_), Rf - ys_
            dy = min(0.01, ys_ / 2)
            m0 = (round_up(ys_) - round_up(ys_ - dy)) / max(dy, 1e-6)
            lim = 3 * abs(za - zw) / h
            m0 = max(-lim, min(lim, m0)) if (zw - za) * m0 >= 0 else 0.0
            t = (y - ys_) / h
            return (2*t**3 - 3*t**2 + 1) * za + (t**3 - 2*t**2 + t) * h * m0 + (-2*t**3 + 3*t**2) * zw
        # underside: the lower body curve and its tangent line out to (W, z0)
        q = np.linspace(0, b, 40)
        zq = np.array([round_lo(v) for v in q])
        sl = (zw - zq) / np.maximum(W - q, 1e-6)
        k_t = int(np.argmax(sl)) if W > b + 1e-3 else len(q) - 1
        y_t, s_t = float(q[k_t]), float(sl[k_t])
        def body_lo(y):
            if y <= y_t:
                return round_lo(y)
            return zw - s_t * (W - y) if W > b + 1e-3 else round_lo(min(y, b))
        # Behind the inboard trailing edge only the tail cone remains: a rounded section centred on the
        # side-view outline. Blend to it over 29.4 to 30.6 m as the wing-body section closes.
        tail = min(1.0, max(0.0, (x - 29.4) / 1.2)) ** 1.5
        zm, hh = (zt + zb) / 2, (zt - zb) / 2
        def tail_up(y):
            u = min(1.0, y / max(b, 1e-6))
            return zm + hh * max(0.0, 1 - u ** 2.3) ** (1 / 2.3)
        def tail_lo(y):
            u = min(1.0, y / max(b, 1e-6))
            return zm - hh * max(0.0, 1 - u ** 2.3) ** (1 / 2.3)
        W = (1 - tail) * W + tail * b
        if x < 0.05:
            zt = zb = zc = 0.0
        WW = max(w if s_tent > 0 else 0.0, W)
        # Canopy: part of the forebody, not a box on it. A rounded crest at the traced top line, its
        # sides sloping down into the tent flanks and blended in with a smooth maximum that fades
        # to nothing at the fairing edge hb, so the canopy rises out of the spine as on the aircraft.
        in_can = CAN_X0 < x < CAN_X1 and s_tent > 0
        hw = float(np.interp(x, HW_X, HW_Y)) if in_can else 0.0
        hb = hw * 1.18
        zb_c = tent_up(min(hb, w)) if in_can else 0.0
        top_c = max(z_canopy, zb_c) if in_can else 0.0
        can_params.append((in_can, hw, zb_c, top_c))
        def canopy_up(y):
            u = min(1.0, y / max(hb, 1e-6))
            return zb_c + (top_c - zb_c) * (1 - u ** 2.2)
        def smax(a, b, k):
            return (a + b + math.sqrt((a - b) ** 2 + k * k)) / 2
        N_U, N_L = 44, 26
        half = []
        for t in np.linspace(0, 1, N_U):                   # spine out to the chine or wing edge
            y = WW * (1 - math.cos(t * math.pi / 2)) ** 0.85 if t < 1 else WW
            z_up = s_tent * tent_up(min(y, w)) + (1 - s_tent) * ((1 - tail) * body_up(min(y, W)) + tail * tail_up(y))
            if in_can and y < hb:
                z_up = smax(z_up, canopy_up(y), 0.035 * (1 - y / hb))
            half.append((y, z_up))
        for t in np.linspace(0, 1, N_L + 1)[1:]:           # back to the keel
            y = WW * (1 - t)
            half.append((y, s_tent * tent_lo(min(y, w)) + (1 - s_tent) * ((1 - tail) * body_lo(min(y, W)) + tail * tail_lo(y))))
        right = np.array(half)
        left = right[1:-1][::-1] * [-1, 1]
        sec = np.vstack([right, left])
        rings.append(np.column_stack([np.full(len(sec), x), sec[:, 0], sec[:, 1]]))
    # Sections, cut at stations (to be replaced by documented joints from research/structure):
    # the detachable nose ahead of the cockpits, the forward fuselage with both cockpits, the chine
    # forebody, the centre body with the wing carry-through, and the tail cone. Each is an open
    # shell, so the exploded view looks inside it.
    cuts = [("Nose section", 0.0, 3.30, (-4.0, 0, 0)), ("Forward fuselage", 3.30, 9.0, (-2.4, 0, 0.6)),
            ("Chine forebody", 9.0, JX, (-0.9, 0, 0.2)), ("Centre body", JX, 29.4, (0, 0, 0)),
            ("Tail cone", 29.4, 99.0, (3.2, 0, 0))]
    global FUSE
    cx_all = np.array([r[0, 0] for r in rings])
    FUSE = {"rings": rings, "xs": cx_all, "nu": N_U, "nl": N_L,
            "hw": np.array([p_[1] if p_[0] else 0.0 for p_ in can_params])}

    def ring_at(x):
        i = int(np.clip(np.searchsorted(cx_all, x) - 1, 0, len(rings) - 2))
        t = (x - cx_all[i]) / (cx_all[i + 1] - cx_all[i])
        return rings[i] * (1 - t) + rings[i + 1] * t

    def upper_z(x, y):
        up = ring_at(x)[:N_U]
        return float(np.interp(abs(y), up[:, 1], up[:, 2]))

    # Panel lines (cited stations): the nose section joint at FS 235 (SR-71A-1 fig. 4-24), the
    # forebody to mid-fuselage joint at FS 715 (TM X-2880 p.2), the air refuelling receptacle door
    # on the spine, FS 403 to 442 with a pointed aft end, and the drag chute door, FS 1004 to 1070
    # (SR-71A-1 fig. 4-37).
    def ring_line(x):
        r = ring_at(x)[:, 1:]
        area = 0.5 * np.sum(r[:, 0] * np.roll(r[:, 1], -1) - np.roll(r[:, 0], -1) * r[:, 1])
        t = np.roll(r, -1, 0) - np.roll(r, 1, 0)
        n = np.column_stack([t[:, 1], -t[:, 0]]) * (1 if area > 0 else -1)
        return ribbon(np.column_stack([np.full(len(r), x), r]), np.column_stack([np.zeros(len(r)), n]), closed=True)

    def top_outline(poly):
        dense = []
        for (xa, ya), (xb, yb) in zip(poly, poly[1:] + poly[:1]):
            n = max(2, int(math.hypot(xb - xa, yb - ya) / 0.03))
            dense += [(xa + (xb - xa) * k / n, ya + (yb - ya) * k / n) for k in range(n)]
        pts = [(x, y, upper_z(x, y)) for x, y in dense]
        slope = lambda x, y: (upper_z(x, abs(y) + 0.02) - upper_z(x, max(abs(y) - 0.02, 0.0))) / 0.04
        nr = [(0.0, -slope(x, y) * np.sign(y), 1.0) for x, y in dense]
        return ribbon(pts, nr, closed=True)

    lines = [ring_line(FSX(235)), ring_line(FSX(715)),
             top_outline([(FSX(403), -0.14), (FSX(442) - 0.25, -0.14), (FSX(442), 0.0), (FSX(442) - 0.25, 0.14), (FSX(403), 0.14)]),
             top_outline([(FSX(1004), -0.32), (FSX(1070), -0.32), (FSX(1070), 0.32), (FSX(1004), 0.32)])]

    # Crash rescue markings after the A-12 ground handling manual (fig. 2-6 sheet 1): a RESCUE arrow
    # beside the front cockpit pointing forward, and an ejection seat danger triangle beside each
    # cockpit, on both sides. The decals lie on the forebody flank just outboard of the canopy
    # fairing, following the skin; u runs to the viewer's right on each side.
    def decal(xc, width, height, side, y_top=0.70, nx=14, nv=10):
        verts, uvs, faces = [], [], []
        for i, x in enumerate(np.linspace(xc - width / 2, xc + width / 2, nx)):
            ys = np.linspace(y_top, y_top + 1.0, 400)
            zs_ = np.array([upper_z(x, y) for y in ys])
            arc = np.concatenate([[0], np.cumsum(np.hypot(np.diff(ys), np.diff(zs_)))])
            for j, sv in enumerate(np.linspace(0, height, nv)):
                y = float(np.interp(sv, arc, ys)); z = upper_z(x, y)
                dz = (upper_z(x, y + 0.01) - upper_z(x, y - 0.01)) / 0.02
                n = np.array([-dz, 1.0]); n /= np.linalg.norm(n)
                verts.append((x, side * (y + n[0] * 0.004), z + n[1] * 0.004))
                u = i / (nx - 1) if side < 0 else 1 - i / (nx - 1)
                uvs.append((u, 1 - j / (nv - 1)))
        for i in range(nx - 1):
            for j in range(nv - 1):
                faces.append((i * nv + j, (i + 1) * nv + j, (i + 1) * nv + j + 1, i * nv + j + 1))
        return verts, faces, uvs
    marks = []
    for side in (-1, 1):
        marks.append(decal(4.30, 0.62, 0.62 * 186 / 512, side) + (2 if side < 0 else 3,))
        for xc in (5.05, 6.70):
            marks.append(decal(xc, 0.42, 0.42 * 459 / 512, side, y_top=0.66) + (4,))

    # canopy window openings under the glass, a little inside the glass outline
    WINDOWS = ((3.66, 4.12, 0.0, 0.38), (3.70, 4.12, 0.47, 0.90), (4.32, 5.38, 0.45, 0.90), (5.98, 6.42, 0.52, 0.86))
    cp_hw = np.array([p_[1] if p_[0] else 0.0 for p_ in can_params])
    def in_window(x, y, z):
        hw = float(np.interp(x, cx_all, cp_hw))
        if hw < 0.05 or z < float(chz(x)) + 0.15:
            return False
        u = abs(y) / hw
        return any(x0 + 0.025 < x < x1 - 0.025 and (u0 == 0 or u > u0 + 0.03) and u < u1 - 0.035 for x0, x1, u0, u1 in WINDOWS)

    parts = []
    for name, x0, x1, ex in cuts:
        sel = [i for i, x in enumerate(cx_all) if x0 - 1e-6 <= x <= x1 + 1e-6]
        v, f = loft([rings[i] for i in sel])
        if name == "Forward fuselage":
            va = np.asarray(v)
            f = [q for q in f if not in_window(*va[list(q)].mean(0))]
        pieces = [(lv, lf, 1, None) for lv, lf in lines if x0 <= lv[0][0] < x1]
        if name == "Forward fuselage":
            pieces += [(mv, mf, mi, muv) for mv, mf, muv, mi in marks]
        v, f, fm, uvs = with_extra(v, f, [0] * len(f), pieces)
        extra = [LINE, MK_RESCUE, MK_RESCUE_R, MK_DANGER] if name == "Forward fuselage" else [LINE]
        parts.append(tag(obj(name, v, f, mat, angle=50, extra=extra, face_mat=fm, uv=uvs), name.lower().replace(" ", "-"), "skin", ex))
    # Canopy glass as thin panels lying 4 mm proud of the canopy crest, so the window outlines
    # are clean: windshield (front pane and two side panes), the pilot's side windows under a
    # metal top strip, and the RSO's small side windows. Each panel is laid out in (x, u), where
    # u is the lateral fraction of the canopy half-width at that station.
    cx = np.array([r[0, 0] for r in rings])
    cp = np.array([[p[1], p[2], p[3]] if p[0] else [np.nan] * 3 for p in can_params])
    ok = ~np.isnan(cp[:, 0])
    hw_at = lambda x: float(np.interp(x, cx[ok], cp[ok, 0]))
    zb_at = lambda x: float(np.interp(x, cx[ok], cp[ok, 1]))
    top_at = lambda x: float(np.interp(x, cx[ok], cp[ok, 2]))
    def crest(x, u):
        hw = hw_at(x); hb = hw * 1.18; y = u * hw
        z = zb_at(x) + (top_at(x) - zb_at(x)) * (1 - min(1.0, y / hb) ** 2.2)
        return y, z + 0.004
    def panel(x0, x1, u0, u1, side, nx=36, nu=14):
        pts, faces = [], []
        for i, x in enumerate(np.linspace(x0, x1, nx)):
            for j, u in enumerate(np.linspace(u0, u1, nu)):
                y, z = crest(x, u)
                pts.append((x, side * y, z))
        for i in range(nx - 1):
            for j in range(nu - 1):
                a_, b_ = i * nu + j, i * nu + j + 1
                q = (a_, b_, b_ + nu, a_ + nu)
                faces.append(q if side > 0 else q[::-1])
        return pts, faces
    glass = []
    for x0, x1, u0, u1 in ((3.66, 4.12, 0.0, 0.38), (3.70, 4.12, 0.47, 0.90), (4.32, 5.38, 0.45, 0.90), (5.98, 6.42, 0.52, 0.86)):
        for side in ((1,) if u0 == 0.0 else (1, -1)):
            pv, pf = panel(x0, x1, u0, u1, side)
            if u0 == 0.0:      # the front pane spans the centreline: mirror it into one panel
                pv2, pf2 = panel(x0, x1, u0, u1, -1)
                off = len(pv); pv = pv + pv2; pf = pf + [tuple(off + k for k in q) for q in pf2]
            off = sum(len(g[0]) for g in glass)
            glass.append((pv, pf))
    gv, gf, off = [], [], 0
    for pv, pf in glass:
        gv += pv; gf += [tuple(off + k for k in q) for q in pf]; off += len(pv)
    parts.append(tag(obj("Canopy glass", gv, gf, GLASS, angle=60), "canopy-glass", "skin", (-2.4, 0, 1.8)))
    return parts


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
            return float(min(env(x), env(JX) + LE_SLOPE * (x - JX))) if x >= JX else float(env(x))
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
    def surf(x, y):
        z0 = float(chz(x))
        t = T_MAX * min(1.0, edge_dist(x, y) / REACH) ** 0.62
        # conical camber on the outer wing (Lockheed section drawing): the leading edge droops
        # toward the tip; up to about 0.16 m at the tip, fading 1.8 m aft of the edge
        droop = 0.0
        if y > 5.3:
            d_le = x - le_x(y)
            droop = 0.16 * ((y - 5.3) / (8.48 - 5.3)) * max(0.0, 1 - d_le / 1.8) ** 2
        return z0 + t - droop, z0 - t * 0.85 - droop
    Y_SPLIT = 4.2            # nacelle centreline: the outer wing panels join outboard of it
    def panel(y_lo, y_hi_frac, n, outboard):
        upper, lower = [], []
        for x, Y in zip(xs, ys_out):
            if outboard and Y < Y_SPLIT + 0.05:
                continue
            hi = Y if outboard else min(Y, Y_SPLIT)
            ys = y_lo + (hi - y_lo) * (1 - np.cos(np.linspace(0, math.pi / 2, n))) ** 0.9
            ys[-1] = hi
            u, l = [], []
            for y in ys:
                zu, zl = surf(x, y)
                u.append((x, y, zu)); l.append((x, y, zl))
            upper.append(u); lower.append(l)
        return upper, lower
    # elevon hinge lines and side edges: inboard elevon WS 40 to 127, outboard WS 210 to 327, hinge
    # lines through the sensor rows just ahead of them (TM X-2880 table 3; SR-71A-1 fig. 4-37)
    def te_x(y):
        ok = xs[ys_out >= y]
        return float(ok[-1]) if len(ok) else float(xs[-1])
    ELEVONS = {"Inner wing": ((FSX(1244), 1.016), (FSX(1224), 3.226)), "Outer wing": ((FSX(1183), 5.334), (FSX(1177), 8.306))}
    def elevon_lines(name, side):
        (xa, ya), (xb, yb) = ELEVONS[name]
        poly = [(te_x(ya) - 0.03, ya), (xa, ya), (xb, yb), (te_x(yb) - 0.03, yb)]
        dense = []
        for (x0_, y0_), (x1_, y1_) in zip(poly[:-1], poly[1:]):
            n = max(2, int(math.hypot(x1_ - x0_, y1_ - y0_) / 0.04))
            dense += [(x0_ + (x1_ - x0_) * k / n, y0_ + (y1_ - y0_) * k / n) for k in range(n)]
        dense.append(poly[-1])
        out = []
        for k, sgn in ((0, 1.0), (1, -1.0)):           # upper and lower skins
            pts = [(x, side * y, surf(x, y)[k]) for x, y in dense]
            out.append(ribbon(pts, [(0.0, 0.0, sgn)] * len(pts)))
        return out
    objs = []
    for name, y_lo, n, outboard, ex in (("Inner wing", 0.0, 26, False, (0, 0.6, 0)), ("Outer wing", Y_SPLIT, 34, True, (0, 6.5, 0.3))):
        upper, lower = panel(y_lo, None, n, outboard)
        for side in (1, -1):
            U = [np.array([(x, side * y, z) for (x, y, z) in r]) for r in upper]
            Lw = [np.array([(x, side * y, z) for (x, y, z) in r]) for r in lower]
            vu, fu = loft(U, closed=False)
            vl, fl = loft(Lw, closed=False)
            off = len(vu)
            faces = fu + [tuple(off + i for i in reversed(q)) for q in fl]
            tagn = "R" if side > 0 else "L"
            v_, f_, fm_, _ = with_extra(vu + vl, faces, [0] * len(faces), [(lv, lf, 1, None) for lv, lf in elevon_lines(name, side)])
            ob = obj(f"{name} {tagn}", v_, f_, mat, angle=40, extra=[LINE], face_mat=fm_)
            objs.append(tag(ob, f"{name.lower().replace(' ', '-')}-{tagn.lower()}", "skin", (ex[0], side * ex[1], ex[2])))
    objs += wing_internals(xs, ys_out, surf)
    return objs


# ------------------------------------------------------------ nacelles, spikes, fins

def nacelle_rings(c):
    out_y, in_y = table(c["nacelle_plan_outer"]), table(c["nacelle_plan_inner"])
    top, bot = table(c["nacelle_side_top"]), table(c["nacelle_side_bottom"])
    cowl = np.asarray(c["cowl_plan"], float)
    x_lip = float(cowl[:, 0].min())
    lip_c, lip_r = (cowl[:, 1].max() + cowl[:, 1].min()) / 2, (cowl[:, 1].max() - cowl[:, 1].min()) / 2
    xs = np.append(np.arange(x_lip, NAC_EXIT - 0.02, 0.05), NAC_EXIT)
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
        if x < 18.0:
            t, b_ = float(top(18.0)), float(bot(18.0))
            zc = (t + b_) / 2 - (18.0 - x) * SPIKE_DOWN     # the inlet points down along the spike axis
            b2 = a * 1.08
        else:
            t, b_ = float(top(x)), float(bot(x))             # past the side-view trace: its last section
            zc, b2 = (t + b_) / 2, (t - b_) / 2
        if x > 26.2:                        # aft nacelle and ejector: gentle boat-tail to the nozzle
            k = (x - 26.2) / (NAC_EXIT - 26.2)
            a = a * (1 - 0.14 * k ** 1.5); b2 = b2 * (1 - 0.18 * k ** 1.5)
        ys.append(yc); zs.append(zc); aa.append(a); bbv.append(b2)
    return xs, smooth(np.array(ys)), smooth(np.array(zs)), smooth(np.array(aa)), smooth(np.array(bbv)), x_lip



class Acc:
    """Accumulates several pieces into one mesh, with a material index per face."""
    def __init__(self):
        self.v, self.f, self.m = [], [], []

    def add(self, verts, faces, mi=0):
        o = len(self.v)
        self.v += [tuple(p) for p in verts]
        self.f += [tuple(o + k for k in q) for q in faces]
        self.m += [mi] * len(faces)


def blade_row(acc, P, x, r0, r1, n, chord, thick, stagger, phase=0.0, mi=0, lean=0.0):
    """A ring of n thin blades between radii r0 and r1 at station x. Each blade is a twisted plate
    of `thick` metres, its chord turned `stagger` radians off the axis (more at the tip)."""
    for k in range(n):
        ph = phase + 2 * math.pi * k / n
        pts = []
        for r, st in ((r0, stagger * 0.6), (r1, stagger * 1.25)):
            c, t_ = 0.5 * chord * math.cos(st), 0.5 * chord * math.sin(st) / max(r, 0.05)
            for dx, dph in ((-c, -t_), (c, t_)):
                for side_off in (-thick / 2, thick / 2):
                    pts.append(P(x + dx + lean * (r - r0), r, ph + dph + side_off / max(r, 0.05)))
        # pts: root LE (2), root TE (2), tip LE (2), tip TE (2) -> a box
        v = [pts[0], pts[2], pts[3], pts[1], pts[4], pts[6], pts[7], pts[5]]
        acc.add(v, [(0, 1, 2, 3), (7, 6, 5, 4), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)], mi)


def revolve(acc, P, prof, n=48, phi0=0.0, phi1=2 * math.pi, mi=0, cap_start=False, cap_end=False):
    """A surface of revolution about the engine axis through (x, r) profile points, over the
    angle range phi0 to phi1 (a full turn closes the ring)."""
    full = abs(phi1 - phi0 - 2 * math.pi) < 1e-6
    phis = np.linspace(phi0, phi1, n, endpoint=not full)
    rings = [np.array([P(x, max(r, 1e-3), ph) for ph in phis]) for x, r in prof]
    v, f = loft(rings, closed=full, cap_start=cap_start and full, cap_end=cap_end and full)
    acc.add(v, f, mi)


def nacelles(c, mat, dark):
    xs, ys, zs, aa, bbv, x_lip = nacelle_rings(c)
    # engine face 5.4 cowl-lip radii aft of the lip (CR-163106 figs 4 and 5)
    x_face = x_lip + 5.4 * RC
    yc_at = lambda x: float(np.interp(x, xs, ys)); zc_at = lambda x: float(np.interp(x, xs, zs))
    seg = 56
    ang = np.linspace(0, 2 * math.pi, seg, endpoint=False)
    objs = []
    for side in (1, -1):
        sd = "R" if side > 0 else "L"
        sl = sd.lower()
        e_nac = (0.0, side * 4.6, -0.3)            # nacelles swing outward
        e_eng = (5.6, side * 4.6, -2.3)            # the J58 slides aft and down out of its nacelle
        e_spk = (-4.6, side * 4.6, -0.3)           # the spike comes forward out of the inlet
        rings = [np.column_stack([np.full(seg, x), side * y + a * np.cos(ang), z + b * np.sin(ang)]) for x, y, z, a, b in zip(xs, ys, zs, aa, bbv)]
        v, f = loft(rings)
        # the last 0.7 m is the bare-metal ejector, heat-stained in service
        fm = [1 if xs[i] > EJECTOR_X else 0 for i in range(len(rings) - 1) for _ in range(seg)]
        # panel lines: the suck-in door band FS 970 to 988 (SR-71A-1 fig. 1-21; A-12 covers 10 and 13)
        # and the tertiary door band FS 1150 to 1160 (fig. 1-21)
        bands = []
        for fs_ in (970, 988, 1150, 1160):
            x = FSX(fs_)
            yc_, zc_, a_, b_ = (float(np.interp(x, xs, arr)) for arr in (ys, zs, aa, bbv))
            bands.append(ribbon([(x, side * yc_ + a_ * math.cos(t), zc_ + b_ * math.sin(t)) for t in ang],
                                [(0.0, math.cos(t) / a_, math.sin(t) / b_) for t in ang], closed=True))
        v, f, fm, _ = with_extra(v, f, fm, [(lv, lf, 2, None) for lv, lf in bands])
        objs.append(tag(obj(f"Nacelle {sd}", v, f, mat, angle=60, extra=[EJECTOR, LINE], face_mat=fm), f"nacelle-{sl}", "skin", e_nac))

        # the inlet axis: ahead of the lip the spike's own axis, canted down and toed in; behind it
        # the nacelle centreline, which the duct, the centrebody and the engine share
        yl, zl = float(ys[0]), float(zs[0])
        def axis(x):
            if x < x_lip:
                return side * (yl - (x_lip - x) * SPIKE_IN), zl - (x_lip - x) * SPIKE_DOWN
            return side * yc_at(x), zc_at(x)
        def P(x, r, phi):
            cy, cz = axis(x)
            return (x, cy + r * math.cos(phi), cz + r * math.sin(phi))

        # inlet duct: the cowl's inner wall from CR-163106 fig. 4, never outside the nacelle skin;
        # its first ring is the outer lip, so the lip reads as a sharp edge with no gap
        dr = table(DUCT_R)
        lr = [rings[0][::-1]]
        for i, x in enumerate(xs):
            if x_lip + 0.02 <= x <= x_face:
                r = min(float(dr((x - x_lip) / RC)) * RC, 0.975 * min(aa[i], bbv[i]))
                cy, cz = axis(x)
                lr.append(np.column_stack([np.full(seg, x), cy + r * np.cos(ang), cz + r * np.sin(ang)])[::-1])
        v, f = loft(lr)
        objs.append(tag(obj(f"Inlet duct {sd}", v, f, DUCT, angle=60), f"inlet-duct-{sl}", "skin", e_nac))
        x_j58_exit = x_face + 4.31
        sel = [i for i, x in enumerate(xs) if x_j58_exit <= x <= xs[-1] - 0.01]
        lr = [np.column_stack([np.full(seg, xs[i]), side * ys[i] + 0.955 * aa[i] * np.cos(ang), zs[i] + 0.955 * bbv[i] * np.sin(ang)])[::-1] for i in sel]
        v, f = loft(lr)
        objs.append(tag(obj(f"Ejector liner {sd}", v, f, EJECTOR, angle=60), f"ejector-liner-{sl}", "skin", e_nac))

        # spike and centrebody, CR-163106 fig. 4 (spike forward, the parked position)
        acc = Acc()
        prof = [(x_lip + s_ * RC, r_ * RC) for s_, r_ in SPIKE_R]
        dense = []
        for (x0, r0), (x1, r1) in zip(prof[:-1], prof[1:]):
            n = max(1, int(abs(x1 - x0) / 0.08))
            dense += [(x0 + (x1 - x0) * k / n, r0 + (r1 - r0) * k / n) for k in range(n)]
        dense.append(prof[-1])
        revolve(acc, P, dense, n=seg)
        objs.append(tag(obj(f"Spike {sd}", acc.v, acc.f, mat, angle=50), f"spike-{sl}", "engines", e_spk))
        # four centrebody struts from the duct wall to the fixed centrebody, at 340, 70, 160 and 250 deg
        # clockwise from the top looking downstream (CR-163106 fig. 4 lower chart)
        acc = Acc()
        sr = table(SPIKE_R)
        for th in (340, 70, 160, 250):
            phi = math.radians(90 + th) if side > 0 else math.radians(90 - th)
            span = []
            for t in np.linspace(0, 1, 5):
                le = x_lip + RC * (2.75 + 0.25 * t)
                te = x_lip + RC * (4.90 + 0.27 * t)
                sec = []
                for u in np.linspace(0, 1, 9):
                    x = le + (te - le) * u
                    s_ = (x - x_lip) / RC
                    r = float(sr(s_)) * RC + (float(dr(s_)) * RC - float(sr(s_)) * RC) * (0.02 + 0.96 * t)
                    half = 0.035 * 4 * u * (1 - u) ** 1.3 + 0.002
                    sec.append((x, r, half))
                ring = [P(x, r, phi + h / r) for x, r, h in sec] + [P(x, r, phi - h / r) for x, r, h in sec[::-1]]
                span.append(np.array(ring))
            v, f = loft(span, cap_start=True, cap_end=True)
            acc.add(v, f)
        objs.append(tag(obj(f"Spike struts {sd}", acc.v, acc.f, DUCT, angle=40), f"spike-struts-{sl}", "engines", e_nac))

        # J58 (JT11D-20) after the flight manual cutaway (SR-71A-1 fig. 1-2): inlet case and variable
        # inlet guide vanes, a nine-stage compressor with the bypass bleed after the fourth stage,
        # eight burner cans, a two-stage turbine, the afterburner with four spray bar rings and four
        # flame holders, and the variable-area nozzle. 180 in long and about 50 in across (Smithsonian).
        # Its casing is drawn cut open on the side facing -y, as the manual draws it, so the stages
        # show without taking the engine apart.
        X = lambda dx: x_face + dx
        acc = Acc()
        case = [(0.0, 0.575), (0.08, 0.615), (0.30, 0.630), (1.45, 0.635), (1.62, 0.600), (1.80, 0.565),
                (2.55, 0.560), (2.72, 0.600), (4.25, 0.595), (4.32, 0.585)]
        thick = 0.018
        w0, w1 = math.radians(-25), math.radians(85)       # the window: from just below +y round to the top
        def shell(x0, x1, phi0, phi1, n):
            sel = [(X(d), r) for d, r in case if x0 - 1e-6 <= d <= x1 + 1e-6]
            sel = [(X(x0), float(np.interp(x0, *zip(*case))))] + [p_ for p_ in sel if X(x0) < p_[0] < X(x1)] + [(X(x1), float(np.interp(x1, *zip(*case))))]
            revolve(acc, P, sel, n=n, phi0=phi0, phi1=phi1)
            revolve(acc, P, [(x, r - thick) for x, r in sel], n=n, phi0=phi0, phi1=phi1)
        shell(0.0, 0.30, 0, 2 * math.pi, 64)
        shell(0.30, 4.20, w1, w0 + 2 * math.pi, 52)
        shell(4.20, 4.32, 0, 2 * math.pi, 64)
        # the cut edges of the window, so the casing shows its thickness
        for ph in (w1, w0 + 2 * math.pi):
            pts = [(X(d), r) for d, r in case if 0.30 <= d <= 4.20]
            v = [P(x, r, ph) for x, r in pts] + [P(x, r - thick, ph) for x, r in pts[::-1]]
            acc.add(v, [tuple(range(len(v)))])
        for d in (0.30, 4.20):
            r = float(np.interp(d, *zip(*case)))
            phs = np.linspace(w0, w1, 20)
            v = [P(X(d), r, p_) for p_ in phs] + [P(X(d), r - thick, p_) for p_ in phs[::-1]]
            acc.add(v, [tuple(range(len(v)))])
        objs.append(tag(obj(f"J58 {sd}", acc.v, acc.f, ENGINE, angle=40), f"j58-{sl}", "engines", e_eng, "representative"))

        # inlet case hub (the island cover), variable inlet guide vanes and the compressor
        acc = Acc()
        revolve(acc, P, [(X(0.0), 0.20), (X(0.10), 0.22), (X(0.30), 0.235), (X(0.9), 0.27), (X(1.45), 0.33), (X(1.62), 0.34),
                         (X(1.80), 0.30)], n=40)
        blade_row(acc, P, X(0.16), 0.22, 0.60, 22, 0.13, 0.012, math.radians(10))
        for k in range(9):
            d = 0.36 + k * 0.142
            hub = float(np.interp(d, [0.3, 0.9, 1.45], [0.235, 0.27, 0.33]))
            tip = float(np.interp(d, [0.3, 1.5], [0.598, 0.52]))
            blade_row(acc, P, X(d), hub, tip, 22 + 3 * k, 0.105 - 0.005 * k, 0.012, math.radians(38 + 2 * k), phase=0.13 * k)
            if k < 8:   # stator row between the rotors
                blade_row(acc, P, X(d + 0.071), hub, tip, 28 + 3 * k, 0.055, 0.009, math.radians(-18), phase=0.07 * k)
        # bypass bleed ring after the fourth stage
        revolve(acc, P, [(X(0.88), 0.60), (X(0.88), 0.625), (X(0.98), 0.625), (X(0.98), 0.60)], n=48)
        objs.append(tag(obj(f"J58 compressor {sd}", acc.v, acc.f, ENGINE, angle=35), f"j58-compressor-{sl}", "engines", e_eng, "representative"))

        # combustion: the diffuser, eight burner cans around the shaft housing
        acc = Acc()
        revolve(acc, P, [(X(1.80), 0.30), (X(1.90), 0.25), (X(2.55), 0.25), (X(2.60), 0.28)], n=40)
        for k in range(8):
            ph = math.pi / 8 + k * math.pi / 4
            cy0 = 0.405
            can = []
            for d, rr in ((1.86, 0.02), (1.90, 0.06), (1.98, 0.088), (2.40, 0.088), (2.52, 0.07), (2.58, 0.05)):
                cx_, cz_ = P(X(d), cy0, ph)[1:]
                can.append(np.array([(X(d), cx_ + rr * math.cos(t), cz_ + rr * math.sin(t)) for t in np.linspace(0, 2 * math.pi, 16, endpoint=False)]))
            v, f = loft(can, cap_start=True, cap_end=True)
            acc.add(v, f, 1)
        objs.append(tag(obj(f"J58 burner {sd}", acc.v, acc.f, ENGINE, angle=40, extra=[HOT], face_mat=acc.m), f"j58-burner-{sl}", "engines", e_eng, "representative"))

        # turbine: a nozzle guide vane row and two rotor stages, then the exhaust cone
        acc = Acc()
        blade_row(acc, P, X(2.64), 0.29, 0.55, 48, 0.07, 0.012, math.radians(-40))
        blade_row(acc, P, X(2.72), 0.30, 0.555, 70, 0.055, 0.010, math.radians(45), phase=0.02)
        blade_row(acc, P, X(2.80), 0.30, 0.56, 48, 0.06, 0.012, math.radians(-40), phase=0.05)
        blade_row(acc, P, X(2.88), 0.30, 0.565, 66, 0.055, 0.010, math.radians(45), phase=0.04)
        revolve(acc, P, [(X(2.60), 0.29), (X(2.95), 0.30), (X(3.15), 0.24), (X(3.35), 0.12), (X(3.42), 0.02)], n=40)
        objs.append(tag(obj(f"J58 turbine {sd}", acc.v, acc.f, HOT, angle=35), f"j58-turbine-{sl}", "engines", e_eng, "representative"))

        # afterburner: four spray bar rings, four flame holders (V gutters) and the liner
        acc = Acc()
        for r in (0.17, 0.29, 0.40, 0.50):
            for d in (3.22,):
                tor = []
                for ph in np.linspace(0, 2 * math.pi, 48, endpoint=False):
                    cx_, cy_, cz_ = P(X(d), r, ph)
                    ny, nz = math.cos(ph), math.sin(ph)
                    tor.append([(cx_ + 0.012 * math.cos(t), cy_ + 0.012 * math.sin(t) * ny, cz_ + 0.012 * math.sin(t) * nz) for t in np.linspace(0, 2 * math.pi, 8, endpoint=False)])
                n_ = len(tor)
                v = [p_ for ring in tor for p_ in ring]
                f = [(i * 8 + j, i * 8 + (j + 1) % 8, ((i + 1) % n_) * 8 + (j + 1) % 8, ((i + 1) % n_) * 8 + j) for i in range(n_) for j in range(8)]
                acc.add(v, f, 0)
        for r in (0.14, 0.26, 0.37, 0.48):
            # a V gutter opening aft: apex forward at radius r, the two legs flare 0.035 m
            revolve(acc, P, [(X(3.62), r + 0.035), (X(3.55), r), (X(3.62), r - 0.035)], n=56, mi=1)
        revolve(acc, P, [(X(3.00), 0.555), (X(4.25), 0.565)], n=56, mi=1)
        objs.append(tag(obj(f"J58 afterburner {sd}", acc.v, acc.f, ENGINE, angle=35, extra=[HOT], face_mat=acc.m), f"j58-afterburner-{sl}", "engines", e_eng, "representative"))

        # variable-area exhaust nozzle: 16 overlapping flaps on the casing lip, set part closed
        acc = Acc()
        for k in range(16):
            ph = 2 * math.pi * k / 16
            hw = math.pi / 16 * 1.08
            v = [P(X(4.30), 0.585, ph - hw), P(X(4.30), 0.585, ph + hw), P(X(4.57), 0.50, ph + hw * 0.92), P(X(4.57), 0.50, ph - hw * 0.92)]
            v2 = [(x, y, z) for x, y, z in v]
            inner = [P(X(4.30), 0.565, ph - hw), P(X(4.30), 0.565, ph + hw), P(X(4.57), 0.485, ph + hw * 0.92), P(X(4.57), 0.485, ph - hw * 0.92)]
            acc.add(v2 + inner, [(0, 1, 2, 3), (7, 6, 5, 4), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)])
        objs.append(tag(obj(f"J58 nozzle {sd}", acc.v, acc.f, HOT, angle=30), f"j58-nozzle-{sl}", "engines", e_eng, "representative"))

        # bypass tubes: six, from the fourth compressor stage to the afterburner
        acc = Acc()
        tang = np.linspace(0, 2 * math.pi, 12, endpoint=False)
        for kk in range(6):
            th = math.radians(30 + 60 * kk)
            pts = []
            for dx in np.linspace(0.93, 3.05, 12):
                rr = 0.69 if 1.05 < dx < 2.9 else 0.655
                cx_, cy_, cz_ = P(X(dx), rr, th)
                pts.append([(cx_, cy_ + 0.05 * math.cos(t), cz_ + 0.05 * math.sin(t)) for t in tang])
            v, f = loft([np.array(p_) for p_ in pts], cap_start=True, cap_end=True)
            acc.add(v, f)
        objs.append(tag(obj(f"Bypass tubes {sd}", acc.v, acc.f, ENGINE, angle=50), f"bypass-tubes-{sl}", "engines", e_eng, "representative"))

        # accessories under the compressor: main gearbox, fuel pump and fuel control (fig. 1-2,
        # items 20 to 22), and the chemical ignition (TEB) tank on the side (item 7)
        acc = Acc()
        def blk(d0, d1, w, r0, r1, ph):
            c0, c1 = P(X(d0), 0, 0), P(X(d1), 0, 0)
            ny, nz = math.cos(ph), math.sin(ph)
            ty, tz = -nz, ny
            v = []
            for d, cc in ((d0, c0), (d1, c1)):
                for rr in (r0, r1):
                    for ww in (-w, w):
                        v.append((X(d), cc[1] + rr * ny + ww * ty, cc[2] + rr * nz + ww * tz))
            acc.add(v, [(0, 1, 3, 2), (4, 6, 7, 5), (0, 4, 5, 1), (2, 3, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3)])
        down = -math.pi / 2
        blk(1.05, 1.85, 0.20, 0.60, 0.74, down)
        blk(1.15, 1.45, 0.11, 0.74, 0.80, down - 0.25)
        blk(1.50, 1.78, 0.09, 0.74, 0.79, down + 0.25)
        tv = []
        for d, rr in ((2.05, 0.02), (2.08, 0.07), (2.40, 0.07), (2.43, 0.02)):
            cx_, cy_, cz_ = P(X(d), 0.69, math.radians(200))
            tv.append(np.array([(cx_, cy_ + rr * math.cos(t), cz_ + rr * math.sin(t)) for t in np.linspace(0, 2 * math.pi, 14, endpoint=False)]))
        v, f = loft(tv, cap_start=True, cap_end=True)
        acc.add(v, f)
        objs.append(tag(obj(f"J58 accessories {sd}", acc.v, acc.f, ENGINE, angle=40), f"j58-gearbox-{sl}", "engines", e_eng, "representative"))

        # a dark annulus at the J58 exit plane closes the gap between the engine and the ejector, so
        # looking up the exhaust shows the nozzle flaps and the afterburner, not the far side of the skin
        x = x_j58_exit
        i = int(np.argmin(np.abs(xs - x)))
        outer = [(x, side * yc_at(x) + 0.955 * aa[i] * math.cos(t), zc_at(x) + 0.955 * bbv[i] * math.sin(t)) for t in ang]
        inner = [P(x, 0.59, t) for t in ang]
        f = [(k, (k + 1) % seg, seg + (k + 1) % seg, seg + k) for k in range(seg)]
        objs.append(tag(obj(f"Nozzle {sd}", outer + inner, f, dark), f"nozzle-{sl}", "skin", e_nac))
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
                if z > zr:
                    z2 = zr + (z - zr) * k
                else:
                    # the root sits on the nacelle's top, sunk into it; behind the nacelle exit the
                    # trailing edge overhangs the nozzle (TN D-6987 fig. 2), level with the exit's top
                    xe = min(x, NAC_EXIT)
                    sink = 0.25 * min(1.0, max(0.0, (NAC_EXIT - x) / 0.4))
                    z2 = zc(xe) + float(np.interp(xe, xs, bbv)) - 0.02 - sink
                h = z2 - zc(x)                                         # height above the nacelle axis
                taper = 1.0 - 0.75 * min(1.0, max(h, 0) / 3.2)
                y = side * (yc(x) - h * math.tan(FIN_CANT)) + side * off * taper * math.cos(FIN_CANT)
                ring.append((x, y, z2))
            rings.append(np.array(ring))
        v, f = loft(rings, closed=True)
        n = len(rings[0])
        f.append(tuple(range(n)))
        f.append(tuple(range(2 * n - 1, n - 1, -1)))
        # the split between the fixed stub fin and the all-moving fin above it, about 21 in above
        # the nacelle (systems.md 3.6, after Merlin)
        poly = rings[0][:, [0, 2]]
        def inside(px, pz):
            c_ = False
            for (ax, az), (bx, bz) in zip(poly, np.roll(poly, -1, 0)):
                if (az > pz) != (bz > pz) and px < ax + (pz - az) * (bx - ax) / (bz - az):
                    c_ = not c_
            return c_
        zsplit = lambda x: zc(x) + float(np.interp(x, xs, bbv)) + 0.53
        run = [x for x in np.linspace(poly[:, 0].min(), poly[:, 0].max(), 260) if inside(x, zsplit(x))]
        pieces = []
        if len(run) > 3:
            run = np.linspace(run[0] + 0.02, run[-1] - 0.02, 120)
            for off in (+1, -1):
                pts, nr = [], []
                for x in run:
                    z = zsplit(x); h = z - zc(x)
                    taper = 1.0 - 0.75 * min(1.0, max(h, 0) / 3.2)
                    y = side * (yc(x) - h * math.tan(FIN_CANT)) + side * off * th * taper * math.cos(FIN_CANT)
                    pts.append((x, y, z)); nr.append((0.0, side * off * math.cos(FIN_CANT), off * math.sin(FIN_CANT)))
                lv, lf = ribbon(pts, nr, lift=0.005)
                pieces.append((lv, lf, 1, None))
        v, f, fm, _ = with_extra(v, f, [0] * len(f), pieces)
        objs.append(tag(obj(f"Fin {'R' if side > 0 else 'L'}", v, f, mat, angle=30, extra=[LINE], face_mat=fm), f"fin-{'r' if side > 0 else 'l'}", "skin", (0.0, side * 5.6, 2.6)))
    print(f"FIN tip z {target_tip:.3f} (drawn {z_tip_drawn:.3f}), height scale {k:.3f}")
    return objs


def probe(mat):
    seg = 16
    ang = np.linspace(0, 2 * math.pi, seg, endpoint=False)
    prof = [(-PROBE, 0.012), (-PROBE + 0.05, 0.025), (-0.25, 0.03), (0.02, 0.045)]
    rings = [np.column_stack([np.full(seg, x), r * np.cos(ang), r * np.sin(ang)]) for x, r in prof]
    v, f = loft(rings, cap_start=True)
    return tag(obj("Pitot probe", v, f, mat, angle=60), "pitot-probe", "skin", (-4.0, 0, 0))


# ------------------------------------------------------------ internal structure and systems
# Stations from research/structure/structure.json (cited there): wing beams and ribs from the
# labelled YF-12A structure drawings (NASA TM X-2880 fig 2a, TM-104317 figs 26 and 31), which share
# the SR-71's stations from the wing aft; tanks, bays, cockpits and gear scaled from the SR-71A-1
# flight manual figures (about plus or minus 25 in). x is metres aft of the radome tip.

FS = lambda fs: (fs - 102) * 0.0254


def section_z(x, y):
    """Upper and lower skin heights of the fuselage section nearest station x, at lateral y."""
    xs, rings, nu, nl = FUSE["xs"], FUSE["rings"], FUSE["nu"], FUSE["nl"]
    i = int(np.argmin(np.abs(xs - x)))
    r = rings[i]
    up = r[:nu]
    lo = r[nu:nu + nl][::-1]
    lo = np.vstack([lo, up[-1:]])
    ay = abs(y)
    return float(np.interp(ay, up[:, 1], up[:, 2])), float(np.interp(ay, lo[:, 1], lo[:, 2])), float(up[-1, 1])


def volume(name, mat, xs_, ys_fn, inset, layer, part, accuracy="representative", explode=(0, 0, 0), side=1, n=16):
    """A closed volume inside the fuselage between stations xs_, spanning ys_fn(x) -> (y0, y1)
    on one side (side = 1 right, -1 left) or across the centreline (y0 < 0), inset from the skin."""
    rings = []
    for x in xs_:
        y0, y1 = ys_fn(x)
        top, bot = [], []
        for y in np.linspace(y0, y1, n):
            zu, zl, _ = section_z(x, y)
            zt, zb = zu - inset, zl + inset
            if zt - zb < 0.01:                   # thinner than the inset near the chine edge: keep inside
                zt = zb = (zu + zl) / 2
                zt += 0.004; zb -= 0.004
            top.append((x, side * y, zt)); bot.append((x, side * y, zb))
        ring = top + bot[::-1]
        rings.append(np.array(ring))
    v, f = loft(rings, cap_start=True, cap_end=True)
    return tag(obj(name, v, f, mat, angle=45), part, layer, explode, accuracy)


def frame(name, x, mat, depth=0.09, thick=0.035, ylim=None):
    """A fuselage frame at station x: the skin section offset inward by `depth`, `thick` wide."""
    xs, rings, nu, nl = FUSE["xs"], FUSE["rings"], FUSE["nu"], FUSE["nl"]
    i = int(np.argmin(np.abs(xs - x)))
    r = rings[i][:, 1:].copy()
    if ylim is not None:            # keep the frame to the body (behind the wing junction)
        r = r[np.abs(r[:, 0]) <= ylim + 1e-6]
    n = len(r)
    if n < 6:
        return None
    # inward offsets along rays from a centre on the centreline at the height of the section's
    # widest point (the chine plane): rays to the thin, sharp chine edge then run inside the chine,
    # so every offset point stays inside the skin
    wide = np.abs(r[:, 0]) >= np.abs(r[:, 0]).max() - 0.002
    c = np.array([0.0, float(r[wide, 1].mean())])
    d = r - c
    dist = np.linalg.norm(d, axis=1)[:, None] + 1e-9
    inner = c + d * np.maximum(0.55, 1 - depth / dist)
    r = c + d * (1 - 0.012 / dist)            # just under the skin, so the frame never shows through it
    loops = []
    for dx in (-thick / 2, thick / 2):
        loops.append(np.column_stack([np.full(n, x + dx), r]))
        loops.append(np.column_stack([np.full(n, x + dx), inner]))
    verts = [tuple(p) for L in loops for p in L]
    faces = []
    A, B, C, D = 0, n, 2 * n, 3 * n          # outer front, inner front, outer back, inner back
    for k in range(n):
        k2 = (k + 1) % n
        faces.append((A + k, A + k2, C + k2, C + k))      # outer band
        faces.append((B + k, D + k, D + k2, B + k2))      # inner band
        faces.append((A + k, B + k, B + k2, A + k2))      # front face
        faces.append((C + k, C + k2, D + k2, D + k))      # back face
    return obj(name, verts, faces, mat, angle=30)


def tube_along(points, r, mat, name, seg=10):
    ang = np.linspace(0, 2 * math.pi, seg, endpoint=False)
    rings = [np.array([(p[0], p[1] + r * math.cos(t), p[2] + r * math.sin(t)) for t in ang]) for p in points]
    v, f = loft(rings, cap_start=True, cap_end=True)
    return obj(name, v, f, mat, angle=60)


def box(name, x0, x1, y0, y1, z0, z1, mat):
    v = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    f = [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
    return obj(name, v, f, mat)


def wheel(name, x, y, z, r, w, mat, seg=28):
    """A tyre with its axis along y (main bogie wheels sit side by side across the aircraft)."""
    ang = np.linspace(0, 2 * math.pi, seg, endpoint=False)
    rings = []
    for yy, rr in ((y - w / 2, r * 0.82), (y - w / 2 + 0.02, r), (y + w / 2 - 0.02, r), (y + w / 2, r * 0.82)):
        rings.append(np.array([(x + rr * math.cos(t), yy, z + rr * math.sin(t)) for t in ang]))
    v, f = loft(rings, cap_start=True, cap_end=True)
    return obj(name, v, f, mat, angle=40)


def wing_internals(xs, ys_out, surf):
    """Spanwise beams and chordwise ribs of the inner wing box and the outer panel box, and the
    wing parts of fuel tanks 3, 6A and 6B, all held between the wing skins."""
    objs = []
    Y = lambda x: float(np.interp(x, xs, ys_out))
    def le_te(y):
        ok = xs[ys_out >= y]
        return (float(ok[0]), float(ok[-1])) if len(ok) else (None, None)
    def web(name, pts):
        # pts: list of (x, y); a sheet between the lower and upper skin, inset 6 mm
        top, bot = [], []
        for x, y in pts:
            zu, zl = surf(x, y)
            top.append((x, y, zu - 0.006)); bot.append((x, y, zl + 0.006))
        return [np.array(bot), np.array(top)]
    beams_in = [FS(f) for f in (769.4, 785.5, 802.0, 818.4, 834.8, 850.6, 866.7, 883.2, 900.3, 915.7, 954.9, 970.4, 987.1,
                                1002.9, 1019.0, 1035.8, 1051.6, 1067.3, 1083.8, 1099.9, 1116.3, 1131.7, 1148.5, 1163.9, 1180.0, 1196.1, 1213.2)]
    for side in (1, -1):
        sl = "r" if side > 0 else "l"
        verts, faces, off = [], [], 0
        def add(rows):
            nonlocal off
            v, f = loft(rows, closed=False)
            v = [(p[0], side * p[1], p[2]) for p in v]
            f = [q if side > 0 else q[::-1] for q in f]
            verts.extend(v); faces.extend(tuple(off + k for k in q) for q in f); off += len(v)
        for x in beams_in:                                   # inner box beams, WS 35 to 127
            y1 = min(Y(x), 3.226)
            if y1 > 0.95:
                add(web("beam", [(x, y) for y in np.linspace(0.889, y1, 14)]))
        for x in [FS(f) for f in range(1050, 1189, 16)]:      # outer panel box beams, WS 213 to 293.5
            if 24.0 <= x <= 27.7:
                y1 = min(Y(x), 7.455)
                if y1 > 5.5:
                    add(web("beam", [(x, y) for y in np.linspace(5.41, y1, 14)]))
        for y in (0.889, 1.829, 2.54, 3.226, 5.41, 6.121, 6.782, 7.455):   # ribs at WS 35, 72, 100, 127, 213, 241, 267, 293.5
            le, te = le_te(y)
            if le is None:
                continue
            if y < 4:
                lo, hi = max(le + 0.05, FS(738)), min(te - 0.05, FS(1226))
            else:
                lo, hi = max(le + 0.05, FS(1050)), min(te - 0.05, FS(1190))
            if hi - lo > 0.3:
                add(web("rib", [(x, y) for x in np.linspace(lo, hi, 30)]))
        objs.append(tag(obj(f"Wing structure {sl.upper()}", verts, faces, FRAME, angle=30), f"wing-structure-{sl}", "structure", (0, 0, 0), "measured"))
        # wing fuel: tank 3 (forward box) and tanks 6A, 6B (aft box), WS 35 to 127
        for tid, a, b in (("tank-3-wing", FS(738), FS(914)), ("tank-6a", FS(954), FS(1090)), ("tank-6b", FS(1090), FS(1226))):
            rows = []
            for x in np.linspace(a + 0.04, b - 0.04, 18):
                y1 = min(Y(x), 3.226) - 0.03
                if y1 < 1.0:
                    continue
                ys_ = np.linspace(0.92, y1, 10)
                top = [(x, side * y, surf(x, y)[0] - 0.015) for y in ys_]
                bot = [(x, side * y, surf(x, y)[1] + 0.015) for y in ys_]
                rows.append(np.array(top + bot[::-1]))
            if len(rows) > 2:
                v, f = loft(rows, cap_start=True, cap_end=True)
                if side < 0:
                    f = [q[::-1] for q in f]
                objs.append(tag(obj(f"{tid} {sl.upper()}", v, f, FUEL, angle=40), f"{tid}-{sl}", "fuel", (0, side * 0.5, 0)))
    return objs


def internals():
    objs = []
    # fuselage frames: tank-end bulkheads and cockpit bulkheads (flight manual figures), the
    # forebody-to-mid-fuselage joint (FS 715) and the wing beams carried through the fuselage
    stations = sorted(set([3.38, 3.61, 5.42, 7.12, FS(404), FS(474), FS(595), FS(715), FS(739)]
                          + [FS(f) for f in (769.4, 802.0, 834.8, 866.7, 900.3, 914, 954, 987.1, 1019.0, 1051.6,
                                             1083.8, 1116.3, 1148.5, 1180.0, 1213.2, 1300)]))
    fv, ff, off = [], [], 0
    for x in stations:
        body = None if x < JX else 1.05
        ob = frame("f", x, FRAME, ylim=body)
        if ob is None:
            continue
        me = ob.data
        vs = [tuple(ob.matrix_world @ v.co) for v in me.vertices]
        # obj() turned the model half round for Blender; undo so all frames merge into one model-frame mesh
        fv.extend([(-p[0], -p[1], p[2]) for p in vs]); ff.extend(tuple(off + k for k in pg.vertices) for pg in me.polygons); off += len(vs)
        bpy.data.objects.remove(ob, do_unlink=True)
    objs.append(tag(obj("Fuselage frames", fv, ff, FRAME, angle=30), "fuselage-frames", "structure", (0, 0, 0), "representative"))
    # longerons: top and bottom centreline, and the side longerons of the forebody core
    lv, lf, off = [], [], 0
    def lon(points):
        nonlocal off
        ob = tube_along(points, 0.03, FRAME, "l")
        vs = [(-v.co[0], -v.co[1], v.co[2]) for v in ob.data.vertices]
        lv.extend(vs); lf.extend(tuple(off + k for k in pg.vertices) for pg in ob.data.polygons); off += len(vs)
        bpy.data.objects.remove(ob, do_unlink=True)
    xs_l = np.arange(0.6, 30.4, 0.25)
    lon([(x, 0.0, section_z(x, 0.0)[0] - 0.06) for x in xs_l])
    lon([(x, 0.0, section_z(x, 0.0)[1] + 0.06) for x in xs_l])
    for sd in (1, -1):
        lon([(x, sd * 0.78, 0.5 * sum(section_z(x, 0.78)[:2])) for x in np.arange(FS(381), FS(791), 0.25)])
    objs.append(tag(obj("Longerons", lv, lf, FRAME, angle=60), "longerons", "structure", (0, 0, 0), "representative"))

    # fuel tanks in the fuselage (flight manual fig. 1-32, stations scaled from fig. 1-40)
    core = lambda x: (-min(0.74, 0.9 * section_z(x, 0)[2]), min(0.74, 0.9 * section_z(x, 0)[2]))
    for tid, a, b in (("tank-1a", 404, 474), ("tank-1", 474, 595), ("tank-2", 595, 739), ("tank-3", 739, 914),
                      ("tank-4", 954, 1106), ("tank-5", 1106, 1300)):
        x0, x1 = FS(a) + 0.04, FS(b) - 0.04
        objs.append(volume(tid.replace("-", " ").title(), FUEL, np.linspace(x0, x1, 16), core, 0.07, "fuel", tid, explode=(0, 0, 0)))

    # crew: SR-1 ejection seats and instrument panels (flight manual fig. 4-24 and 1-12, 1-17)
    for nm, xs_, zh in (("pilot", 4.48, 0.991), ("rso", 6.17, 1.143)):
        zu, zl, _ = section_z(xs_, 0.0)
        floor = zl + 0.42
        sv, sf, off = [], [], 0
        for part_ in (box("s", xs_ - 0.05, xs_ + 0.42, -0.25, 0.25, floor, floor + 0.14, SEAT),
                      box("s", xs_ + 0.32, xs_ + 0.46, -0.25, 0.25, floor + 0.1, floor + 0.85, SEAT),
                      box("s", xs_ + 0.30, xs_ + 0.46, -0.16, 0.16, floor + 0.85, floor + 1.02, SEAT)):
            vs = [(-v.co[0], -v.co[1], v.co[2]) for v in part_.data.vertices]
            sv.extend(vs); sf.extend(tuple(off + k for k in pg.vertices) for pg in part_.data.polygons); off += len(vs)
            bpy.data.objects.remove(part_, do_unlink=True)
        objs.append(tag(obj(f"Seat {nm}", sv, sf, SEAT, angle=30), f"seat-{nm}", "crew", (0, 0, 2.2), "representative"))
        # the instrument panel: the flight manual drawing (fig. 1-12 or 1-17) on a panel at the
        # cockpit's forward end (FS 258 and FS 318), tilted back 18 deg, under a glare shield
        px = FSX(258) if nm == "pilot" else FSX(318)
        pu, pl, _ = section_z(px, 0.0)
        face_mat, aspect, w = (PANEL_P, 865 / 1024, 0.70) if nm == "pilot" else (PANEL_R, 623 / 1024, 0.76)
        h, tilt = w * aspect, math.radians(18)
        zb = pl + 0.62
        room = (pu - 0.10) - zb
        if h * math.cos(tilt) > room:
            k = room / (h * math.cos(tilt)); w *= k; h *= k
        # and narrow enough that the glare shield's corners stay inside the skin
        ring = FUSE["rings"][int(np.argmin(np.abs(FUSE["xs"] - px)))][:FUSE["nu"]]
        for _ in range(3):
            z_top = zb + h * math.cos(tilt) + 0.05
            inside = ring[ring[:, 2] >= z_top]
            half = float(inside[:, 1].max()) if len(inside) else 0.3
            if w / 2 + 0.03 > half - 0.05:
                k = (half - 0.08) * 2 / w; w *= k; h *= k
        nx_, nz_ = math.cos(tilt), math.sin(tilt)                 # the face looks aft and a little up
        corners = [(px, -w / 2, zb), (px, w / 2, zb), (px - h * nz_, w / 2, zb + h * nx_), (px - h * nz_, -w / 2, zb + h * nx_)]
        shift = lambda c, d: [(x + d * nx_, y, z + d * nz_) for x, y, z in c]
        front, back = shift(corners, 0.002), shift(corners, -0.05)
        verts = front + corners + back
        faces = [(0, 1, 2, 3)]                                        # the drawing
        faces += [(8, 11, 10, 9), (4, 8, 9, 5), (5, 9, 10, 6), (6, 10, 11, 7), (7, 11, 8, 4)]
        fm = [1] + [0] * 5
        uv = [(0, 0), (1, 0), (1, 1), (0, 1)] + [(0, 0)] * 8
        # glare shield over the top edge
        xt, zt = px - h * nz_, zb + h * nx_
        g0 = len(verts)
        verts += [(xt - 0.03, -w / 2 - 0.03, zt + 0.01), (xt + 0.16, -w / 2 - 0.03, zt + 0.01), (xt + 0.16, w / 2 + 0.03, zt + 0.01), (xt - 0.03, w / 2 + 0.03, zt + 0.01),
                  (xt - 0.03, -w / 2 - 0.03, zt + 0.04), (xt + 0.16, -w / 2 - 0.03, zt + 0.04), (xt + 0.16, w / 2 + 0.03, zt + 0.04), (xt - 0.03, w / 2 + 0.03, zt + 0.04)]
        uv += [(0, 0)] * 8
        faces += [tuple(g0 + k for k in q) for q in ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7))]
        fm += [0] * 6
        print(f"PANEL {nm} x {px:.2f} floor {pl:.2f} top skin {pu:.2f} face z {zb:.2f} to {zt:.2f}, {w:.2f} x {h:.2f} m")
        objs.append(tag(obj(f"Panel {nm}", verts, faces, PANEL, extra=[face_mat], face_mat=fm, uv=uv), f"panel-{nm}", "crew", (0, 0, 2.2), "representative"))

    # cockpit tubs: floor, side walls up to the canopy fairing and end walls, from the instrument
    # panel to the aft bulkhead of each cockpit (FS 258 to 316 and 318 to 382, structure.json)
    for nm, a_, b_ in (("pilot", FSX(252), FSX(312)), ("rso", FSX(314), FSX(382))):
        rings_ = []
        for x in np.linspace(a_, b_, 14):
            zu, zl, _ = section_z(x, 0.0)
            floor = zl + 0.40
            hw = float(np.interp(x, FUSE["xs"], FUSE["hw"]))
            yw = max(0.30, 1.05 * hw)
            ztop = section_z(x, yw)[0] - 0.02
            prof = [(-yw, ztop), (-yw, floor + 0.05), (-yw + 0.05, floor), (yw - 0.05, floor), (yw, floor + 0.05), (yw, ztop)]
            rings_.append(np.array([(x, y, z) for y, z in prof]))
        v, f = loft(rings_, closed=False)
        n_ = len(rings_[0]); base = (len(rings_) - 1) * n_
        f.append(tuple(range(n_ - 1, -1, -1))); f.append(tuple(base + k for k in range(n_)))
        objs.append(tag(obj(f"Cockpit {nm}", v, f, COCKPIT, angle=30), f"cockpit-{nm}", "crew", (0, 0, 2.2), "representative"))

    # equipment bays: chine bays out to near the chine edge, centreline bays in the core
    def chine(y_in, frac):
        return lambda x: (y_in, max(y_in + 0.1, frac * section_z(x, 0)[2]))
    bays = [("Bay A nose", "bay-a", 1.12, 3.40, lambda x: (-0.35 * section_z(x, 0)[2], 0.35 * section_z(x, 0)[2]), 1),
            ("Bay B left chine", "bay-b", 3.40, 6.58, chine(0.55, 0.88), -1),
            ("Bay D right chine", "bay-d", 4.70, 6.76, chine(0.55, 0.88), 1),
            ("Mission bays K M left", "bay-km", 6.60, 10.67, chine(0.82, 0.9), -1),
            ("Mission bays L N right", "bay-ln", 6.60, 10.67, chine(0.82, 0.9), 1),
            ("Mission bays P S left", "bay-ps", 10.90, 14.78, chine(0.85, 0.9), -1),
            ("Mission bays Q T right", "bay-qt", 10.85, 14.83, chine(0.85, 0.9), 1),
            ("ANS bay", "bay-ans", 7.24, 7.98, lambda x: (-0.23, 0.23), 1)]
    for nm, pid, a, b, fn, sd in bays:
        objs.append(volume(nm, BAY, np.linspace(a, b, 12), fn, 0.04, "bays", pid, side=sd, n=10))

    # landing gear (stowed), drag chute door, refuelling receptacle, star tracker window
    for sd in (1, -1):
        sl = "r" if sd > 0 else "l"
        zu, zl, _ = section_z(21.16, 1.5)
        gv_, gf_, off = [], [], 0
        for k in range(3):
            ob = wheel("w", 21.16, sd * (1.15 + k * 0.36), zl + 0.42, 0.349, 0.19, TYRE)
            vs = [(-v.co[0], -v.co[1], v.co[2]) for v in ob.data.vertices]
            gv_.extend(vs); gf_.extend(tuple(off + kk for kk in pg.vertices) for pg in ob.data.polygons); off += len(vs)
            bpy.data.objects.remove(ob, do_unlink=True)
        objs.append(tag(obj(f"Main gear {sl.upper()}", gv_, gf_, TYRE, angle=40), f"main-gear-{sl}", "gear", (0, 0, -2.0), "representative"))
    zu, zl, _ = section_z(9.53, 0)
    nv, nf, off = [], [], 0
    for yy in (-0.13, 0.13):
        ob = wheel("w", 9.53, yy, zl + 0.3, 0.22, 0.14, TYRE)
        vs = [(-v.co[0], -v.co[1], v.co[2]) for v in ob.data.vertices]
        nv.extend(vs); nf.extend(tuple(off + kk for kk in pg.vertices) for pg in ob.data.polygons); off += len(vs)
        bpy.data.objects.remove(ob, do_unlink=True)
    objs.append(tag(obj("Nose gear", nv, nf, TYRE, angle=40), "nose-gear", "gear", (0, 0, -2.0), "representative"))
    for nm, pid, a, b, w in (("Drag chute door", "drag-chute", FS(1004), FS(1070), 0.32), ("Refuelling receptacle", "ar-receptacle", FS(403), FS(442), 0.14)):
        pts = []
        for x in np.linspace(a, b, 10):
            for y in np.linspace(-w, w, 6):
                pts.append((x, y, section_z(x, y)[0] - 0.012))      # under the skin: seen in x-ray
        faces = [(i * 6 + j, i * 6 + j + 1, (i + 1) * 6 + j + 1, (i + 1) * 6 + j) for i in range(9) for j in range(5)]
        objs.append(tag(obj(nm, pts, faces, MARKER, angle=60), pid, "gear" if pid == "drag-chute" else "bays", (0, 0, 0), "representative"))
    xw = FS(395)
    ang = np.linspace(0, 2 * math.pi, 24, endpoint=False)
    zt = section_z(xw, 0)[0] - 0.012
    objs.append(tag(obj("Star tracker window", [(xw + 0.115 * math.cos(t), 0.115 * math.sin(t), zt) for t in ang], [tuple(range(24))], MARKER), "star-tracker", "bays", (0, 0, 0), "representative"))
    return objs



def main():
    a = args()
    c = json.loads(Path(a["components"]).read_text())
    bpy.ops.wm.read_factory_settings(use_empty=True)
    skin = bpy.data.materials.new("Blackbird skin"); skin.use_nodes = True
    p = skin.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = (0.018, 0.02, 0.026, 1); p.inputs["Metallic"].default_value = 0.35; p.inputs["Roughness"].default_value = 0.5
    dark = bpy.data.materials.new("Intake and nozzle"); dark.use_nodes = True
    dark.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.002, 0.002, 0.003, 1)
    # named materials; render_beauty.py and the web viewer dress them by name
    global GLASS, EJECTOR, DUCT
    def named(name, rgba, metal, rough):
        m = bpy.data.materials.new(name); m.use_nodes = True
        b = m.node_tree.nodes["Principled BSDF"]
        b.inputs["Base Color"].default_value = rgba; b.inputs["Metallic"].default_value = metal; b.inputs["Roughness"].default_value = rough
        return m
    GLASS = named("Canopy glass", (0.02, 0.03, 0.035, 1), 0.0, 0.05)
    EJECTOR = named("Ejector metal", (0.33, 0.30, 0.27, 1), 1.0, 0.45)
    DUCT = named("Inlet duct", (0.01, 0.011, 0.013, 1), 0.2, 0.6)
    global ENGINE, HOT
    ENGINE = named("Engine metal", (0.40, 0.41, 0.43, 1), 1.0, 0.35)
    HOT = named("Engine hot section", (0.33, 0.25, 0.18, 1), 1.0, 0.42)
    # panel lines, the crash rescue markings and the instrument panel drawings (model/tools/textures.py)
    global LINE, MK_RESCUE, MK_RESCUE_R, MK_DANGER, PANEL_P, PANEL_R
    LINE = named("Panel line", (0.004, 0.0045, 0.006, 1), 0.0, 0.75)
    tex_dir = Path(__file__).resolve().parent.parent / "textures"
    def textured(name, file, alpha=False, emit=0.0):
        m = bpy.data.materials.new(name); m.use_nodes = True
        nt = m.node_tree; b = nt.nodes["Principled BSDF"]
        t = nt.nodes.new("ShaderNodeTexImage"); t.image = bpy.data.images.load(str(tex_dir / file))
        nt.links.new(t.outputs["Color"], b.inputs["Base Color"])
        b.inputs["Roughness"].default_value = 0.55
        if alpha:
            nt.links.new(t.outputs["Alpha"], b.inputs["Alpha"])
            m.surface_render_method = "BLENDED"
        if emit:
            nt.links.new(t.outputs["Color"], b.inputs["Emission Color"])
            b.inputs["Emission Strength"].default_value = emit
        return m
    MK_RESCUE = textured("Marking rescue", "mark-rescue.png", alpha=True)
    MK_RESCUE_R = textured("Marking rescue right", "mark-rescue-r.png", alpha=True)
    MK_DANGER = textured("Marking danger", "mark-danger.png", alpha=True)
    PANEL_P = textured("Panel face pilot", "panel-pilot.jpg", emit=0.35)
    PANEL_R = textured("Panel face RSO", "panel-rso.jpg", emit=0.35)
    global FRAME, FUEL, BAY, SEAT, PANEL, TYRE, MARKER, COCKPIT
    COCKPIT = named("Cockpit", (0.028, 0.03, 0.032, 1), 0.0, 0.7)
    FRAME = named("Frame", (0.55, 0.58, 0.62, 1), 1.0, 0.4)
    FUEL = named("Fuel tank", (0.85, 0.55, 0.12, 1), 0.0, 0.3)
    BAY = named("Bay", (0.15, 0.55, 0.75, 1), 0.0, 0.4)
    SEAT = named("Seat", (0.10, 0.11, 0.09, 1), 0.0, 0.7)
    PANEL = named("Panel", (0.02, 0.02, 0.025, 1), 0.2, 0.5)
    TYRE = named("Tyre", (0.03, 0.03, 0.03, 1), 0.0, 0.85)
    MARKER = named("Marker", (0.83, 0.26, 0.18, 1), 0.0, 0.5)
    parts = fuselage(c, skin) + wing(c, skin) + [probe(skin)] + nacelles(c, skin, dark) + fins(c, skin)
    parts += internals()
    root = bpy.data.objects.new("SR-71A", None); bpy.context.collection.objects.link(root)
    for o in parts:
        o.parent = root
    out = Path(a["out"]); out.parent.mkdir(parents=True, exist_ok=True)
    if a.get("blend"):
        bpy.ops.wm.save_as_mainfile(filepath=str(Path(a["blend"]).resolve()))
    bpy.ops.export_scene.gltf(filepath=str(out.resolve()), export_format="GLB", export_apply=True, export_yup=True, export_extras=True)
    print(f"BUILT {out} parts={len(parts)} faces={sum(len(o.data.polygons) for o in parts)}")


if __name__ == "__main__":
    main()
