"""Render orthographic silhouettes and shaded views of a built model for checking against drawings.

  blender -b --factory-startup --python model/tools/render_views.py -- \
      --model model/build/sr71a.glb --out model/build/renders --ppm 60

Writes <view>_sil.png (white aircraft on black, exact scale: --ppm pixels per metre, aircraft
reference point at the image centre) and <view>_shaded.png for plan, side, front, plus
beauty.png. Also writes scale.json describing the pixel mapping for compare.py.
"""
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


def args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = {"model": "model/build/sr71a.glb", "out": "model/build/renders", "ppm": "60"}
    for i in range(0, len(argv) - 1, 2):
        out[argv[i].lstrip("-")] = argv[i + 1]
    return out


def main():
    a = args()
    out = Path(a["out"]); out.mkdir(parents=True, exist_ok=True)
    ppm = float(a["ppm"])
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(Path(a["model"]).resolve()))
    meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]

    # Bounds in Blender space (glTF import restores Z up). Nose sits toward -X after build.
    pts = [o.matrix_world @ Vector(c) for o in meshes for c in o.bound_box]
    lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    centre = (lo + hi) / 2
    size = hi - lo

    scene = bpy.context.scene
    world = bpy.data.worlds.new("World"); scene.world = world
    world.color = (0, 0, 0)
    scene.render.engine = "BLENDER_WORKBENCH"
    shading = scene.display.shading
    scene.render.film_transparent = False
    scene.view_settings.view_transform = "Standard"

    margin = 1.0
    views = {
        # name: (camera location offset direction, rotation euler, frame width m, frame height m)
        "plan": (Vector((0, 0, 1)), (0, 0, 0), size.x + 2 * margin, size.y + 2 * margin),
        "side": (Vector((0, -1, 0)), (math.radians(90), 0, 0), size.x + 2 * margin, size.z + 2 * margin),
        "front": (Vector((-1, 0, 0)), (math.radians(90), 0, math.radians(-90)), size.y + 2 * margin, size.z + 2 * margin),
    }
    scale_info = {"ppm": ppm, "centre_blender": list(centre), "bounds_lo": list(lo), "bounds_hi": list(hi), "views": {}}
    for name, (d, rot, fw, fh) in views.items():
        cam_data = bpy.data.cameras.new(name); cam_data.type = "ORTHO"
        cam = bpy.data.objects.new(name, cam_data); scene.collection.objects.link(cam)
        cam.location = centre + d * 100
        cam.rotation_euler = rot
        cam_data.clip_end = 1000
        w_px, h_px = int(round(fw * ppm)), int(round(fh * ppm))
        cam_data.ortho_scale = max(fw, fh)
        cam_data.sensor_fit = "AUTO"
        scene.render.resolution_x, scene.render.resolution_y = w_px, h_px
        scene.render.resolution_percentage = 100
        scene.camera = cam
        # silhouette
        shading.light = "FLAT"; shading.color_type = "SINGLE"; shading.single_color = (1, 1, 1)
        shading.background_type = "WORLD"
        scene.render.filepath = str(out / f"{name}_sil.png"); bpy.ops.render.render(write_still=True)
        # shaded
        shading.light = "STUDIO"; shading.color_type = "SINGLE"; shading.single_color = (0.55, 0.58, 0.62)
        shading.show_cavity = True
        scene.render.filepath = str(out / f"{name}_shaded.png"); bpy.ops.render.render(write_still=True)
        shading.show_cavity = False
        scale_info["views"][name] = {"width_px": w_px, "height_px": h_px, "frame_w_m": fw, "frame_h_m": fh}

    # beauty: three-quarter view from above the left wing, nose toward the viewer's right
    cam_data = bpy.data.cameras.new("beauty"); cam_data.lens = 70
    cam = bpy.data.objects.new("beauty", cam_data); scene.collection.objects.link(cam)
    cam.location = centre + Vector((22, -46, 26))
    direction = centre - cam.location
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    scene.camera = cam
    scene.render.resolution_x, scene.render.resolution_y = 1800, 1100
    shading.light = "STUDIO"; shading.show_cavity = True; shading.single_color = (0.5, 0.53, 0.58)
    scene.render.filepath = str(out / "beauty.png"); bpy.ops.render.render(write_still=True)

    (out / "scale.json").write_text(json.dumps(scale_info, indent=1))
    print("RENDERED", out)


if __name__ == "__main__":
    main()
