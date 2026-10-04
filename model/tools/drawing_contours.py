"""Write the NASA Dryden silhouettes as contours in metres, in the format compare.py reads."""
import json
from pathlib import Path

import cv2
import numpy as np

T = Path(__file__).resolve().parents[1] / "trace/dfrc"
BOX = {"plan": (1150, 0), "side": (1200, 5880), "front": (0, 3940)}

for view in ("plan", "side", "front"):
    meta = json.loads((T / f"{view}.json").read_text())
    m = cv2.imread(str(T / f"{view}_mask.png"), cv2.IMREAD_GRAYSCALE)
    cs, _ = cv2.findContours((m > 127).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    c = max(cs, key=cv2.contourArea)[:, 0, :].astype(float) + BOX[view]
    s, px = meta["m_per_px"], meta["px"]
    if view == "plan":
        pts = np.stack([(c[:, 0] - px["nose_x"]) * s, (px["centre_y"] - c[:, 1]) * s], 1)
    elif view == "side":
        pts = np.stack([(c[:, 0] - px["nose_x"]) * s, (px["ref_y"] - c[:, 1]) * s], 1)
    else:
        pts = np.stack([(c[:, 0] - px["mid_x"]) * s, (px["wing_y"] - c[:, 1]) * s], 1)
    out = {"spec": f"dfrc_{view}", "view": view, "contour_m": np.round(pts[::2], 4).tolist()}
    (T / f"cmp_{view}.json").write_text(json.dumps(out))
    print(view, len(pts), "points")
