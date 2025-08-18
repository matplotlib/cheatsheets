# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import sys
import pathlib

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR / "fonts"))
import custom_fonts  # noqa


fig = plt.figure(figsize=(6, 1))
# ax = plt.subplot(111, frameon=False, aspect=.1)
# b = 0.0
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)


plt.scatter([5.5], [0.75], s=100, c="k")
plt.xlim(0, 6), plt.ylim(0, 1)
plt.xticks([]), plt.yticks([])

plt.annotate("text", (5.5, .75), (0.75, .75), size=16, va="center", ha="center",
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.text( 5.5, 0.6, "xy\nxycoords", size=10, va="top", ha="center", color=".5")
plt.text( .75, 0.6, "xytext\ntextcoords", size=10, va="top", ha="center", color=".5")

fig.savefig(ROOT_DIR / "figures/annotate.pdf")
# plt.show()
