# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------

# Scripts to generate all the basic plots
import pathlib

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


ROOT_DIR = pathlib.Path(__file__).parent.parent

fig = plt.figure(figsize=(5, .25))

ax = fig.add_axes([0, 0, 1, 1], frameon=False,
                  xticks=[], yticks=[], xlim=[0, 1], ylim=[-.5, 1.5])

epsilon=1e-12
plt.plot([0, 1], [0, 0], "black", clip_on=False, lw=8,
         ls=(.5, (epsilon, 1)), dash_capstyle="round")
plt.plot([0, 1], [1, 1], "black", clip_on=False, lw=8,
         ls=(-.5, (epsilon, 2)), dash_capstyle="round")
fig.savefig(ROOT_DIR / "figures/tip-dotted.pdf")
# plt.show()
