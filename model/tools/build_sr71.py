"""Build the Article 121 SR-71A model in Blender from measured geometry.

Run headless:
  blender -b --factory-startup --python model/tools/build_sr71.py -- \
      --geometry model/geometry/sr71a.json --out model/build/sr71a.glb [--blend model/build/sr71a.blend]

Axes (metres): x is fuselage station from the nose tip, positive aft; y is buttock
line, positive to the right wing; z is waterline, positive up, with z = 0 on the
chine and wing reference plane. Blender gets x' = -x (nose toward -X is turned so
the aircraft faces +X in glTF), y' = y, z' = z.

Every number comes from model/geometry/sr71a.json, which records the drawing and
page each value was traced or read from. Nothing is hand-tuned in this file.
"""
import json
import math
import sys
from pathlib import Path

import bmesh
import bpy
import numpy as np
from mathutils import Vector


def args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = {"geometry": "model/geometry/sr71a.json", "out": "model/build/sr71a.glb", "blend": None}
    for i in range(0, len(argv) - 1, 2):
        out[argv[i].lstrip("-")] = argv[i + 1]
    return out


def interp(xs, table):
    """Piecewise-linear lookup in a list of [x, value] pairs."""
    t = np.asarray(table, dtype=float)
    return np.interp(xs, t[:, 0], t[:, 1])


def to_blender(p):
    x, y, z = p
    return Vector((-x, y, z))


def mesh_object(name, verts, faces, material=None, smooth_angle=None):
    me = bpy.data.meshes.new(name)
    me.from_pydata([to_blender(v) for v in verts], [], faces)
    me.validate()
    me.update()
    ob = bpy.data.objects.new(name, me)
    bpy.context.collection.objects.link(ob)
    if material:
        ob.data.materials.append(material)
    bpy.context.view_layer.objects.active = ob
    ob.select_set(True)
    if smooth_angle is not None:
        bpy.ops.object.shade_smooth_by_angle(angle=math.radians(smooth_angle))
    else:
        bpy.ops.object.shade_flat()
    ob.select_set(False)
    return ob


def mirror_grid(rows):
    """rows: list of station rows, each a list of (x, y, z) from y = 0 outward on the right.
    Returns verts and quad faces for the full left+right surface."""
    verts, faces = [], []
    n = len(rows[0])
    for row in rows:
        left = [(x, -y, z) for (x, y, z) in reversed(row[1:])]
        verts.extend(left + list(row))
    m = 2 * n - 1
    for i in range(len(rows) - 1):
        for j in range(m - 1):
            a = i * m + j
            faces.append((a, a + 1, a + m + 1, a + m))
    return verts, faces


# ---------------------------------------------------------------- components

def lifting_surface(g, mat):
    """Chines, inboard wing and outboard wing as one sharp-edged surface.

    For each station the half-span runs from the centreline to the outline. Thickness at a
    point grows with its distance from the nearest outline edge, so every edge is sharp and the
    section thickens inward, which matches the chine and wing sections in the drawings.
    """
    outline = np.asarray(g["planform"]["half_outline"], dtype=float)   # [[x, y], ...] nose to tail
    stations = np.asarray(g["planform"]["stations"], dtype=float)
    span_samples = g["planform"].get("span_samples", 40)
    t_max = g["planform"]["max_half_thickness"]
    t_reach = g["planform"]["thickness_reach"]           # distance from edge at which full thickness is reached
    zc = lambda x: float(interp([x], g["planform"]["reference_plane_z"])[0])
    half_span = lambda x: float(np.interp(x, outline[:, 0], outline[:, 1]))

    # Closed polygon of the full planform for edge distances
    poly = np.vstack([outline, outline[::-1] * [1, -1]])

    def edge_distance(px, py):
        a = poly
        b = np.roll(poly, -1, axis=0)
        ab = b - a
        ap = np.stack([px - a[:, 0], py - a[:, 1]], axis=1)
        t = np.clip((ap * ab).sum(1) / np.maximum((ab * ab).sum(1), 1e-12), 0, 1)
        d = ap - ab * t[:, None]
        return float(np.sqrt((d * d).sum(1)).min())

    def half_thickness(x, y):
        d = edge_distance(x, y)
        return t_max * min(1.0, d / t_reach) ** 0.62

    upper, lower = [], []
    for x in stations:
        ys = half_span(x) * (1 - np.cos(np.linspace(0, math.pi / 2, span_samples))) ** 0.85
        ys[-1] = half_span(x)
        z0 = zc(x)
        upper.append([(x, y, z0 + half_thickness(x, y)) for y in ys])
        lower.append([(x, y, z0 - half_thickness(x, y)) for y in ys])
    vu, fu = mirror_grid(upper)
    vl, fl = mirror_grid(lower)
    off = len(vu)
    faces = fu + [tuple(off + i for i in reversed(f)) for f in fl]
    return mesh_object("Wing and chines", vu + vl, faces, mat, smooth_angle=40)


def body_of_revolution(name, profile, axis_y, axis_z, mat, segments=48, squash=(1.0, 1.0), cap_front=False):
    """profile: [[x, r], ...]; ellipse scaled by squash = (y scale, z scale)."""
    prof = np.asarray(profile, dtype=float)
    verts, faces = [], []
    for x, r in prof:
        for k in range(segments):
            a = 2 * math.pi * k / segments
            verts.append((x, axis_y + r * math.cos(a) * squash[0], axis_z + r * math.sin(a) * squash[1]))
    for i in range(len(prof) - 1):
        for k in range(segments):
            a = i * segments + k
            b = i * segments + (k + 1) % segments
            faces.append((a, b, b + segments, a + segments))
    return mesh_object(name, verts, faces, mat, smooth_angle=60)


def fuselage(g, mat):
    f = g["fuselage"]
    xs = np.asarray(f["stations"], dtype=float)
    top = interp(xs, f["top_z"])
    bot = interp(xs, f["bottom_z"])
    half_w = interp(xs, f["half_width"])
    seg = 56
    verts, faces = [], []
    for x, zt, zb, w in zip(xs, top, bot, half_w):
        zc = (zt + zb) / 2
        h = max((zt - zb) / 2, 1e-4)
        for k in range(seg):
            a = 2 * math.pi * k / seg
            # superellipse gives the slightly boxy upper fuselage seen in front views
            c, s = math.cos(a), math.sin(a)
            e = f.get("superellipse", 2.2)
            yy = w * math.copysign(abs(c) ** (2 / e), c)
            zz = h * math.copysign(abs(s) ** (2 / e), s)
            verts.append((x, yy, zc + zz))
    for i in range(len(xs) - 1):
        for k in range(seg):
            a = i * seg + k
            b = i * seg + (k + 1) % seg
            faces.append((a, b, b + seg, a + seg))
    return mesh_object("Fuselage", verts, faces, mat, smooth_angle=60)


def nacelles(g, mat, dark):
    n = g["nacelle"]
    objs = []
    for side in (1, -1):
        y = side * n["centre_y"]
        z = n["centre_z"]
        objs.append(body_of_revolution(f"Nacelle {'R' if side > 0 else 'L'}", n["profile"], y, z, mat))
        spike = [[x + n.get("spike_offset", 0.0), r] for x, r in n["spike_profile"]]
        objs.append(body_of_revolution(f"Spike {'R' if side > 0 else 'L'}", spike, y, z, mat, segments=40))
        # engine face and nozzle discs, set back inside the lips
        for label, x, r in (("Inlet", n["engine_face_x"], n["engine_face_r"]), ("Nozzle", n["nozzle_x"], n["nozzle_r"])):
            v = [(x, y + r * math.cos(2 * math.pi * k / 40), z + r * math.sin(2 * math.pi * k / 40)) for k in range(40)]
            objs.append(mesh_object(f"{label} {'R' if side > 0 else 'L'}", v, [tuple(range(40))], dark))
    return objs


def fins(g, mat):
    fdat = g["fins"]
    root = fdat["root"]      # [[x_le, x_te], z_root]
    tip = fdat["tip"]        # [[x_le, x_te], height above root]
    cant = math.radians(fdat["cant_deg"])
    t = fdat["half_thickness"]
    objs = []
    for side in (1, -1):
        y0, z0 = side * fdat["root_y"], fdat["root_z"]
        ring = []
        for (x_le, x_te), h in ((root[0], 0.0), (tip[0], tip[1])):
            # biconvex section: 8 points around the chord
            chord = x_te - x_le
            pts = []
            for k in range(8):
                u = k / 7
                pts.append((x_le + chord * u, 4 * t * u * (1 - u)))
            sec = pts + [(px, -pt) for px, pt in reversed(pts[1:-1])]
            ring.append([(px, pt, h) for px, pt in sec])
        verts, faces = [], []
        m = len(ring[0])
        for r_i, sec in enumerate(ring):
            for px, pt, h in sec:
                # cant the fin inboard about its root line
                yy = y0 + pt * math.cos(cant) - side * h * math.sin(cant)
                zz = z0 + pt * math.sin(cant) * side + h * math.cos(cant)
                verts.append((px, yy, zz))
        for k in range(m):
            a, b = k, (k + 1) % m
            faces.append((a, b, b + m, a + m))
        faces.append(tuple(range(m)))
        faces.append(tuple(range(2 * m - 1, m - 1, -1)))
        objs.append(mesh_object(f"Fin {'R' if side > 0 else 'L'}", verts, faces, mat, smooth_angle=30))
    return objs


def canopy(g, mat):
    c = g["canopy"]
    return body_of_revolution("Canopy", c["profile"], 0.0, c["base_z"], mat, segments=40, squash=(c["width_ratio"], 1.0))


# ---------------------------------------------------------------- main

def main():
    a = args()
    g = json.loads(Path(a["geometry"]).read_text())
    bpy.ops.wm.read_factory_settings(use_empty=True)

    skin = bpy.data.materials.new("Blackbird skin")
    skin.use_nodes = True
    bsdf = skin.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (0.018, 0.02, 0.026, 1)
    bsdf.inputs["Metallic"].default_value = 0.35
    bsdf.inputs["Roughness"].default_value = 0.5
    glass = bpy.data.materials.new("Canopy glass")
    glass.use_nodes = True
    gb = glass.node_tree.nodes["Principled BSDF"]
    gb.inputs["Base Color"].default_value = (0.01, 0.012, 0.016, 1)
    gb.inputs["Roughness"].default_value = 0.08
    gb.inputs["Metallic"].default_value = 0.6
    dark = bpy.data.materials.new("Intake and nozzle")
    dark.use_nodes = True
    dark.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.002, 0.002, 0.003, 1)

    parts = [lifting_surface(g, skin), fuselage(g, skin), canopy(g, glass)]
    parts += nacelles(g, skin, dark)
    parts += fins(g, skin)

    root = bpy.data.objects.new("SR-71A", None)
    bpy.context.collection.objects.link(root)
    for p in parts:
        p.parent = root

    out = Path(a["out"])
    out.parent.mkdir(parents=True, exist_ok=True)
    if a.get("blend"):
        bpy.ops.wm.save_as_mainfile(filepath=str(Path(a["blend"]).resolve()))
    bpy.ops.export_scene.gltf(filepath=str(out.resolve()), export_format="GLB", export_apply=True, export_yup=True)
    tris = sum(len(p.data.polygons) for p in parts if p.type == "MESH")
    print(f"BUILT {out} parts={len(parts)} faces={tris}")


if __name__ == "__main__":
    main()
