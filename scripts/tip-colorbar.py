# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------

# Scripts to generate all the basic plots
import sys
import pathlib

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects


ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR / "fonts"))
import custom_fonts  # noqa


fig = plt.figure(figsize=(2.15, 2))
mpl.rcParams['axes.linewidth'] = 1.5
d = 0.01
ax = fig.add_axes([d, d, 1-2*d, 1-2*d], xticks=[], yticks=[])

np.random.seed(1)
Z = np.random.uniform(0, 1, (8, 8))
cmap = plt.get_cmap("Oranges")
im = ax.imshow(Z, interpolation="nearest", cmap=cmap, vmin=0, vmax=2)
cb = fig.colorbar(im, fraction=0.046, pad=0.04)
cb.set_ticks([])

fig.savefig(ROOT_DIR / "figures/tip-colorbar.pdf")
# plt.show()
