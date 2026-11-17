"""Trace the firm's oval phoenix seal (LeungBirdC.jpg from their site) into a one-colour SVG path."""
import sys, numpy as np, potrace
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
S = 8
im = im.resize((im.width * S, im.height * S), Image.LANCZOS)
a = np.asarray(im).astype(int)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
mask = (r - b > 90) & (r > 150)
bmp = potrace.Bitmap(~mask)
path = bmp.trace(turdsize=60, alphamax=1.0, opticurve=True, opttolerance=0.4)
d = []
for curve in path:
    s = curve.start_point
    d.append(f"M{s.x/S:.2f} {s.y/S:.2f}")
    for seg in curve.segments:
        if seg.is_corner:
            d.append(f"L{seg.c.x/S:.2f} {seg.c.y/S:.2f}L{seg.end_point.x/S:.2f} {seg.end_point.y/S:.2f}")
        else:
            d.append(f"C{seg.c1.x/S:.2f} {seg.c1.y/S:.2f} {seg.c2.x/S:.2f} {seg.c2.y/S:.2f} {seg.end_point.x/S:.2f} {seg.end_point.y/S:.2f}")
    d.append("Z")
w, h = im.width // S, im.height // S
open(out, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"><path fill="currentColor" fill-rule="evenodd" d="{"".join(d)}"/></svg>')
print("ok", w, h, len("".join(d)))
