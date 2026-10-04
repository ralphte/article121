"""Photo-real check renders of the model (Cycles), for side-by-side comparison with photographs.

  blender -b --factory-startup --python model/tools/render_beauty.py -- --model model/build/sr71a.glb --out model/build/renders/beauty

Views: nose-on from slightly above (as in the Smithsonian NASM2016-00596 photograph of 61-7972),
three-quarter from above front left, and side.
"""
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


def args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = {"model": "model/build/sr71a.glb", "out": "model/build/renders/beauty", "samples": "96"}
    for i in range(0, len(argv) - 1, 2):
        out[argv[i].lstrip("-")] = argv[i + 1]
    return out


def look_at(cam, target):
    d = Vector(target) - cam.location
    cam.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()


def main():
    a = args()
    out = Path(a["out"]); out.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(Path(a["model"]).resolve()))
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    prefs = bpy.context.preferences.addons["cycles"].preferences
    try:
        prefs.compute_device_type = "METAL"; prefs.get_devices()
        for d in prefs.devices: d.use = True
        sc.cycles.device = "GPU"
    except Exception:
        sc.cycles.device = "CPU"
    sc.cycles.samples = int(a["samples"]); sc.cycles.use_denoising = True
    sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Medium High Contrast"

    # paint: the blue-black iron-ball finish, slightly glossy
    for m in bpy.data.materials:
        if not m.use_nodes: continue
        p = m.node_tree.nodes.get("Principled BSDF")
        if not p: continue
        if "skin" in m.name.lower():
            p.inputs["Base Color"].default_value = (0.012, 0.014, 0.02, 1)
            p.inputs["Roughness"].default_value = 0.42
            p.inputs["Metallic"].default_value = 0.0
            p.inputs["Coat Weight"].default_value = 0.25
            p.inputs["Coat Roughness"].default_value = 0.2

    # world: soft hangar-like light plus a key and two rims
    world = bpy.data.worlds.new("World"); sc.world = world; world.use_nodes = True
    bg = world.node_tree.nodes["Background"]; bg.inputs["Color"].default_value = (0.06, 0.07, 0.085, 1); bg.inputs["Strength"].default_value = 0.6
    floor = bpy.data.meshes.new("floor"); floor.from_pydata([(-80, -40, -2.2), (40, -40, -2.2), (40, 40, -2.2), (-80, 40, -2.2)], [], [(0, 1, 2, 3)])
    fo = bpy.data.objects.new("floor", floor); sc.collection.objects.link(fo)
    fm = bpy.data.materials.new("floor"); fm.use_nodes = True
    fp = fm.node_tree.nodes["Principled BSDF"]; fp.inputs["Base Color"].default_value = (0.08, 0.085, 0.09, 1); fp.inputs["Roughness"].default_value = 0.18
    fo.data.materials.append(fm)
    for name, loc, energy, size in (("key", (10, -14, 22), 9000, 14), ("rim L", (-24, 22, 9), 5000, 10), ("rim R", (-24, -22, 9), 5000, 10), ("top", (-12, 0, 30), 6000, 24)):
        L = bpy.data.lights.new(name, "AREA"); L.energy = energy; L.size = size
        o = bpy.data.objects.new(name, L); o.location = loc; sc.collection.objects.link(o); look_at(o, (-14, 0, 0))

    views = {
        "nose_on": ((30.0, 0.0, 1.45), (-14.0, 0.0, 0.75), 105),
        "three_quarter": ((14.0, -26.0, 17.0), (-15.0, 0.0, 0.3), 38),
        "side": ((-15.0, -48.0, 1.0), (-15.0, 0.0, 0.8), 45),
    }
    only = a.get("only")
    for name, (loc, tgt, lens) in views.items():
        if only and name != only: continue
        cd = bpy.data.cameras.new(name); cd.lens = lens; cd.sensor_width = 36
        cam = bpy.data.objects.new(name, cd); sc.collection.objects.link(cam)
        cam.location = loc; look_at(cam, tgt); sc.camera = cam
        sc.render.resolution_x, sc.render.resolution_y = (1600, 1066)
        sc.render.filepath = str(out / f"{name}.png")
        bpy.ops.render.render(write_still=True)
    print("BEAUTY", out)


if __name__ == "__main__":
    main()
