"""Bring the FlightGear SR-71 (GPL v2, Emmanuel Baranger) into the Article 121 frame for comparison.

  blender -b --factory-startup --python model/tools/import_reference.py -- --obj model/reference/fg-sr71.obj --out model/build/reference-fg.glb

FlightGear AC axes: x aft, y up, z lateral. Article 121 axes: x aft from the radome tip, z up from
the radome tip. Blender (as in build_sr71_v2): X = -x, Y = lateral, Z = up.
Landing gear, doors, drag chute and engine internals are removed so only the outer airframe remains.
"""
import sys
from pathlib import Path

import bpy

DROP = ("roue", "axe", "barre", "verrin", "accroche", "porte", "parachute", "bruleur", "turbine", "trous", "HDR")
RADOME_X, RADOME_Y = -15.03, -1.03


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    a = dict(zip(argv[::2], argv[1::2]))
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.wm.obj_import(filepath=str(Path(a["--obj"]).resolve()), forward_axis="Y", up_axis="Z")
    kept = 0
    for o in list(bpy.context.scene.objects):
        if o.type != "MESH":
            continue
        if any(o.name.startswith(d) for d in DROP):
            bpy.data.objects.remove(o, do_unlink=True); continue
        me = o.data
        for v in me.vertices:
            x, y, z = v.co.x, v.co.y, v.co.z          # obj import kept the file axes as x, y, z
            v.co = (-(x - RADOME_X), z, y - RADOME_Y)
        me.update(); kept += 1
    mat = bpy.data.materials.new("ref"); mat.use_nodes = True
    for o in bpy.context.scene.objects:
        if o.type == "MESH":
            o.data.materials.clear(); o.data.materials.append(mat)
    bpy.ops.export_scene.gltf(filepath=str(Path(a["--out"]).resolve()), export_format="GLB", export_yup=True)
    print("REFERENCE kept", kept)


main()
