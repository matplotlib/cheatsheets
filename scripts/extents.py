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


mpl.style.use([
    ROOT_DIR / 'styles/base.mplstyle',
])
mpl.rc('figure.constrained_layout', wspace=0.05)

Z = np.arange(5*5).reshape(5, 5)

(fig, axs) = plt.subplots(figsize=(8, 5), nrows=2, ncols=2)

ax = axs[0, 0]
ax.imshow(Z, extent=[0, 10, 0, 5], interpolation="nearest", origin="upper")
ax.set_xlim(-1, 11), ax.set_xticks([])
ax.set_ylim(-1, 6), ax.set_yticks([0, 5])
ax.text(1, 4.5, "(0,0)", ha="center", va="center", color="white", size="large")
ax.text(9, 0.5, "(4,4)", ha="center", va="center", color="black", size="large")
ax.text(5.0, 5.5, 'origin="upper"',
        ha="center", va="center", color="black", size="large")
ax.text(5.0, -0.5, "extent=[0,10,0,5]",
        ha="center", va="center", color="black", size="large")

ax = axs[1, 0]
ax.imshow(Z, extent=[0, 10, 0, 5], interpolation="nearest", origin="lower")
ax.set_xlim(-1, 11), ax.set_xticks([0, 10])
ax.set_ylim(-1, 6), ax.set_yticks([0, 5])
ax.text(1, 0.5, "(0,0)", ha="center", va="center", color="white", size="large")
ax.text(9, 4.5, "(4,4)", ha="center", va="center", color="black", size="large")

ax.text(5.0, 5.5, 'origin="lower"',
        ha="center", va="center", color="black", size="large")
ax.text(5.0, -0.5, "extent=[0,10,0,5]",
        ha="center", va="center", color="black", size="large")

ax = axs[1, 1]
ax.imshow(Z, extent=[10, 0, 0, 5], interpolation="nearest", origin="lower")
ax.set_xlim(-1, 11), ax.set_xticks([0, 10])
ax.set_ylim(-1, 6), ax.set_yticks([])
ax.text(9, 0.5, "(0,0)", ha="center", va="center", color="white", size="large")
ax.text(1, 4.5, "(4,4)", ha="center", va="center", color="black", size="large")
ax.text(5.0, 5.5, 'origin="lower"',
        ha="center", va="center", color="black", size="large")
ax.text(5.0, -0.5, "extent=[10,0,0,5]",
        ha="center", va="center", color="black", size="large")

ax = axs[0, 1]
ax.imshow(Z, extent=[10, 0, 0, 5], interpolation="nearest", origin="upper")
ax.set_xlim(-1, 11), ax.set_xticks([])
ax.set_ylim(-1, 6), ax.set_yticks([])
ax.text(9, 4.5, "(0,0)", ha="center", va="center", color="white", size="large")
ax.text(1, 0.5, "(4,4)", ha="center", va="center", color="black", size="large")
ax.text(5.0, 5.5, 'origin="upper"',
        ha="center", va="center", color="black", size="large")
ax.text(5.0, -0.5, "extent=[10,0,0,5]",
        ha="center", va="center", color="black", size="large")

fig.savefig(ROOT_DIR / "figures/extents.pdf", dpi=600)
