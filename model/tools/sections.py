"""Draw cross-sections of a built model at given stations, for checking against section drawings.

  cd model/tools && uv run python sections.py ../build/sr71a.glb out.png [--ref other.glb] [--x 1,2,3]
  cd model/tools && uv run python sections.py ../build/sr71a.glb out.png --overlay --x 1,2,3

Each panel is one station (metres aft of the radome tip), drawn looking forward with the same scale
in every panel. With --ref, a second model is drawn in grey beneath for comparison. With --overlay,
all stations are drawn on one set of axes, the way section sheets group them.
"""
import sys

import cv2
import numpy as np
import trimesh

STATIONS = [0.8, 2.1, 3.1, 4.3, 5.0, 6.5, 7.9, 9.6, 12.5, 15.7, 17.7, 19.0, 20.2, 24.0, 28.0]


def load(path):
    s = trimesh.load(path, force="scene")
    m = s.to_geometry()
    # glTF from Blender is y up with the aircraft along -x; back to x aft, y span, z up
    v = m.vertices.copy()
    m.vertices = np.stack([-v[:, 0], v[:, 2], v[:, 1]], 1)
    return m


def section(m, x):
    p = m.section(plane_origin=[x, 0, 0], plane_normal=[1, 0, 0])
    if p is None:
        return []
    return [np.asarray(d)[:, 1:] for d in p.discrete]


def main():
    a = sys.argv[1:]
    src, out = a[0], a[1]
    ref = a[a.index("--ref") + 1] if "--ref" in a else None
    xs = [float(t) for t in a[a.index("--x") + 1].split(",")] if "--x" in a else STATIONS
    m = load(src); r = load(ref) if ref else None
    if "--overlay" in a:
        return overlay(m, xs, out)
    ppm, half_w, half_h = 110, 4.6, 2.4
    cols = 3
    pw, ph = int(2 * half_w * ppm), int(2 * half_h * ppm)
    rows = (len(xs) + cols - 1) // cols
    img = np.full((rows * ph, cols * pw, 3), 18, np.uint8)
    for k, x in enumerate(xs):
        ox, oy = (k % cols) * pw + pw // 2, (k // cols) * ph + ph // 2
        cv2.line(img, (ox - pw // 2 + 8, oy), (ox + pw // 2 - 8, oy), (50, 50, 50), 1)
        def draw(loops, col, th):
            for L in loops:
                # looking forward: the aircraft's right wing (+y) on the right
                px = np.stack([ox + L[:, 0] * ppm, oy - L[:, 1] * ppm], 1).astype(np.int32)
                cv2.polylines(img, [px.reshape(-1, 1, 2)], False, col, th, cv2.LINE_AA)
        if r is not None:
            draw(section(r, x), (110, 110, 110), 2)
        draw(section(m, x), (120, 230, 255), 1)
        cv2.putText(img, f"x {x:.1f} m", (ox - pw // 2 + 10, oy - ph // 2 + 24), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (220, 220, 220), 1, cv2.LINE_AA)
    cv2.imwrite(out, img)
    print("wrote", out)


def overlay(m, xs, out, ppm=150):
    half_w, top, bot = 5.4, 1.6, 0.9
    W, H = int(2 * half_w * ppm), int((top + bot) * ppm) + 60
    img = np.full((H, W, 3), 18, np.uint8)
    oy = int(top * ppm) + 30
    cv2.line(img, (0, oy), (W, oy), (60, 60, 60), 1)
    cv2.line(img, (W // 2, 0), (W // 2, H), (60, 60, 60), 1)
    for k, x in enumerate(xs):
        shade = 255 - int(150 * k / max(1, len(xs) - 1))
        col = (int(shade * 0.47), int(shade * 0.9), shade)
        for L in section(m, x):
            px = np.stack([W // 2 + L[:, 0] * ppm, oy - L[:, 1] * ppm], 1).astype(np.int32)
            cv2.polylines(img, [px.reshape(-1, 1, 2)], False, col, 1, cv2.LINE_AA)
    cv2.putText(img, "stations " + ", ".join(f"{x:g}" for x in xs) + " m aft of the radome tip; light to dark front to back",
                (16, H - 16), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (200, 200, 200), 1, cv2.LINE_AA)
    cv2.imwrite(out, img)
    print("wrote", out)


if __name__ == "__main__":
    main()
