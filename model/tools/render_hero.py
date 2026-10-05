"""High-quality still renders of the model (Cycles), for the site and for review.

  blender -b --factory-startup --python model/tools/render_hero.py -- \
      --model model/build/sr71a.glb --out model/build/renders/hero [--only hero] [--samples 256] [--res 2400x1350]

The aircraft floats against the site's near-black ground: it has no landing gear, so there is no
floor to sit on. Reflections come from the CC0 studio environment that ships with Blender (Greg
Zaal, Poly Haven, studio_small_01), lifted by a softbox overhead and two rim strips that draw the
chines and the fuselage. Materials are dressed by the names the builder gives them.

The "hero" view matches the web viewer's opening camera, so its render can stand in as the
viewer's poster while the model loads.
"""
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector

STUDIO = Path(bpy.utils.resource_path("LOCAL")) / "datafiles/studiolights/world/studio.exr"
GROUND = (0.0047, 0.0058, 0.0078)        # #05070a in linear light: the site's page colour

# name: (camera location, target, lens mm); Blender frame, nose at the origin, aircraft along -x
VIEWS = {
    "hero": ((13.0, -21.0, 6.5), (-16.0, 0.0, 0.5), 42),
    "nose_on": ((22.0, 0.0, 2.6), (-14.0, 0.0, 0.6), 85),
    "rear": ((-50.0, 15.0, 4.5), (-17.0, 0.0, 0.6), 50),
    "side": ((-15.6, -62.0, 0.9), (-15.6, 0.0, 0.9), 55),
    "top": ((-15.6, 0.0, 70.0), (-15.6, 0.0, 0.0), 45),
    "cockpit": ((1.5, -5.2, 2.9), (-6.0, 0.0, 0.9), 50),
    "inlet": ((-9.0, -9.5, 1.6), (-17.2, -4.1, 0.2), 45),
    "tail_check": ((-44.0, 0.0, 5.0), (-27.0, 0.0, 0.3), 40),
    "under_check": ((-36.0, -10.0, -6.0), (-26.0, 0.0, 0.0), 40),
}


def args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = {"model": "model/build/sr71a.glb", "out": "model/build/renders/hero", "samples": "256", "res": "2400x1350"}
    for i in range(0, len(argv) - 1, 2):
        out[argv[i].lstrip("-")] = argv[i + 1]
    return out


def look_at(ob, target):
    ob.rotation_euler = (Vector(target) - ob.location).to_track_quat("-Z", "Y").to_euler()


def node(nt, kind, **inputs):
    n = nt.nodes.new(kind)
    for k, v in inputs.items():
        n.inputs[k].default_value = v
    return n


def dress(m):
    """Replace a material's shader by its role, from the builder's material names."""
    nt = m.node_tree
    p = nt.nodes.get("Principled BSDF")
    if p is None:
        return
    name = m.name.split(".")[0]
    coord = node(nt, "ShaderNodeTexCoord")
    if name in ("Blackbird skin",):
        # satin blue-black, a clear coat, and a little roughness variation so it reads as paint
        p.inputs["Base Color"].default_value = (0.0105, 0.0118, 0.0155, 1)
        p.inputs["Metallic"].default_value = 0.0
        p.inputs["Coat Weight"].default_value = 0.25
        p.inputs["Coat Roughness"].default_value = 0.18
        noise = node(nt, "ShaderNodeTexNoise", Scale=0.35, Detail=4.0, Roughness=0.5)
        nt.links.new(coord.outputs["Object"], noise.inputs["Vector"])
        ramp = nt.nodes.new("ShaderNodeMapRange")
        ramp.inputs["From Min"].default_value, ramp.inputs["From Max"].default_value = 0.3, 0.7
        ramp.inputs["To Min"].default_value, ramp.inputs["To Max"].default_value = 0.31, 0.37
        nt.links.new(noise.outputs["Fac"], ramp.inputs["Value"])
        nt.links.new(ramp.outputs["Result"], p.inputs["Roughness"])
    elif name == "Canopy glass":
        p.inputs["Base Color"].default_value = (0.012, 0.016, 0.02, 1)
        p.inputs["Roughness"].default_value = 0.02
        p.inputs["Coat Weight"].default_value = 1.0
        p.inputs["Coat Roughness"].default_value = 0.0
        p.inputs["Alpha"].default_value = 0.45          # the cockpits show through, darkly
    elif name == "Ejector metal":
        # bare metal stained by heat: bronze to blue-grey in patches
        noise = node(nt, "ShaderNodeTexNoise", Scale=6.0, Detail=8.0, Roughness=0.6)
        nt.links.new(coord.outputs["Object"], noise.inputs["Vector"])
        cr = nt.nodes.new("ShaderNodeValToRGB")
        cr.color_ramp.elements[0].color = (0.30, 0.22, 0.15, 1)
        cr.color_ramp.elements[1].color = (0.20, 0.22, 0.27, 1)
        nt.links.new(noise.outputs["Fac"], cr.inputs["Fac"])
        nt.links.new(cr.outputs["Color"], p.inputs["Base Color"])
        p.inputs["Metallic"].default_value = 1.0
        p.inputs["Roughness"].default_value = 0.38
    elif name in ("Inlet duct", "Intake and nozzle"):
        p.inputs["Base Color"].default_value = (0.006, 0.006, 0.007, 1)
        p.inputs["Roughness"].default_value = 0.7


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
    sc.cycles.max_bounces = 8
    sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Medium High Contrast"
    sc.view_settings.exposure = 0.0
    w, h = (int(v) for v in a["res"].split("x"))
    sc.render.resolution_x, sc.render.resolution_y = w, h

    for m in bpy.data.materials:
        if m.use_nodes:
            dress(m)
    # stills show the aircraft as it stands: skin, engines and cockpits; the structure, tanks, bays
    # and stowed gear inside it are for the interactive viewer's x-ray and exploded views
    for o in bpy.data.objects:
        if o.get("a121_layer") in ("structure", "fuel", "bays", "gear"):
            o.hide_render = True
            for ch in o.children_recursive:
                ch.hide_render = True

    # world: the studio map lights and reflects; camera rays see the site's ground instead
    world = bpy.data.worlds.new("World"); sc.world = world; world.use_nodes = True
    nt = world.node_tree; nt.nodes.clear()
    env = nt.nodes.new("ShaderNodeTexEnvironment"); env.image = bpy.data.images.load(str(STUDIO))
    mapping = nt.nodes.new("ShaderNodeMapping"); mapping.inputs["Rotation"].default_value = (0, 0, math.radians(-35))
    tc = nt.nodes.new("ShaderNodeTexCoord"); nt.links.new(tc.outputs["Generated"], mapping.inputs["Vector"])
    nt.links.new(mapping.outputs["Vector"], env.inputs["Vector"])
    lit = node(nt, "ShaderNodeBackground", Strength=0.22); nt.links.new(env.outputs["Color"], lit.inputs["Color"])
    bg = node(nt, "ShaderNodeBackground", Color=(*GROUND, 1), Strength=1.0)
    lp = nt.nodes.new("ShaderNodeLightPath")
    mix = nt.nodes.new("ShaderNodeMixShader")
    nt.links.new(lp.outputs["Is Camera Ray"], mix.inputs["Fac"])
    nt.links.new(lit.outputs["Background"], mix.inputs[1]); nt.links.new(bg.outputs["Background"], mix.inputs[2])
    wo = nt.nodes.new("ShaderNodeOutputWorld"); nt.links.new(mix.outputs["Shader"], wo.inputs["Surface"])

    # softbox overhead, two long rim strips behind, and a low warm fill from the front
    for name, loc, energy, size, size_y, color in (
        ("softbox", (-14, 0, 22), 3500, 22, 9, (1.0, 1.0, 1.0)),
        ("rim left", (-34, 24, 7), 8000, 36, 2.5, (0.82, 0.9, 1.0)),
        ("rim right", (-34, -24, 7), 8000, 36, 2.5, (0.82, 0.9, 1.0)),
        ("fill", (26, -10, 2), 600, 10, 4, (1.0, 0.93, 0.85)),
    ):
        L = bpy.data.lights.new(name, "AREA"); L.shape = "RECTANGLE"; L.size, L.size_y = size, size_y
        L.energy = energy; L.color = color
        o = bpy.data.objects.new(name, L); o.location = loc; sc.collection.objects.link(o); look_at(o, (-15, 0, 0))

    only = a.get("only")
    for name, (loc, tgt, lens) in VIEWS.items():
        if only and name not in only.split(","):
            continue
        cd = bpy.data.cameras.new(name); cd.lens = lens; cd.sensor_width = 36; cd.sensor_fit = "HORIZONTAL"
        cam = bpy.data.objects.new(name, cd); sc.collection.objects.link(cam)
        cam.location = loc; look_at(cam, tgt); sc.camera = cam
        sc.render.filepath = str(out / f"{name}.png")
        bpy.ops.render.render(write_still=True)
        print("RENDERED", name, flush=True)
    print("HERO", out)


if __name__ == "__main__":
    main()
