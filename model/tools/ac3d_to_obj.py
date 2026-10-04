"""Convert an AC3D (.ac) model, as used by FlightGear, to Wavefront OBJ with object groups.

  python3 ac3d_to_obj.py in.ac out.obj

Applies each object's loc and rot down the hierarchy. Lines (SURF type 1 or 2) are skipped;
polygons are written as faces. Coordinates are written as found (FlightGear: x aft, y right, z up).
"""
import sys

import numpy as np


def parse(path):
    toks = open(path, encoding="latin-1").read().split("\n")
    i = 0
    objects = []

    def read_object(parent_m, parent_t, i):
        name, loc, rot, verts, faces = "", np.zeros(3), np.eye(3), None, []
        kids = 0
        while i < len(toks):
            line = toks[i].strip(); i += 1
            if not line:
                continue
            w = line.split()
            if w[0] == "name":
                name = line[5:].strip().strip('"')
            elif w[0] == "loc":
                loc = np.array(list(map(float, w[1:4])))
            elif w[0] == "rot":
                rot = np.array(list(map(float, w[1:10]))).reshape(3, 3)
            elif w[0] == "numvert":
                n = int(w[1])
                verts = np.array([list(map(float, toks[i + k].split()[:3])) for k in range(n)])
                i += n
            elif w[0] == "numsurf":
                ns = int(w[1])
                for _ in range(ns):
                    surf = int(toks[i].split()[1], 16); i += 1
                    while not toks[i].strip().startswith("refs"):
                        i += 1
                    nr = int(toks[i].split()[1]); i += 1
                    idx = [int(toks[i + k].split()[0]) for k in range(nr)]
                    i += nr
                    if (surf & 0xF) == 0 and nr >= 3:
                        faces.append(idx)
            elif w[0] == "kids":
                kids = int(w[1])
                m = parent_m @ rot.T
                t = parent_t + parent_m @ loc
                if verts is not None and faces:
                    objects.append((name, (verts @ m.T) + t, faces))
                for _ in range(kids):
                    while not toks[i].startswith("OBJECT"):
                        i += 1
                    i += 1
                    i = read_object(m, t, i)
                return i
        return i

    while i < len(toks) and not toks[i].startswith("OBJECT"):
        i += 1
    read_object(np.eye(3), np.zeros(3), i + 1)
    return objects


def main(src, dst):
    objs = parse(src)
    off = 1
    with open(dst, "w") as f:
        for name, v, faces in objs:
            f.write(f"o {name or 'part'}\n")
            for p in v:
                f.write(f"v {p[0]:.5f} {p[1]:.5f} {p[2]:.5f}\n")
            for fc in faces:
                f.write("f " + " ".join(str(off + k) for k in fc) + "\n")
            off += len(v)
    allv = np.vstack([o[1] for o in objs])
    print(f"{len(objs)} objects, {len(allv)} vertices, {sum(len(o[2]) for o in objs)} faces")
    print("bounds min", allv.min(0).round(3), "max", allv.max(0).round(3))
    for name, v, faces in objs:
        print(f"  {name[:32]:32s} {len(faces):6d} faces  x {v[:,0].min():7.2f}..{v[:,0].max():7.2f}  y {v[:,1].min():6.2f}..{v[:,1].max():6.2f}  z {v[:,2].min():6.2f}..{v[:,2].max():6.2f}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
