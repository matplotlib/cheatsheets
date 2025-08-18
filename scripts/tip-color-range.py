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


ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR / "fonts"))
import custom_fonts  # noqa


fig = plt.figure(figsize=(2, 2))
mpl.rcParams['axes.linewidth'] = 1.5
d = 0.01

ax = fig.add_axes([d, d, 1-2*d, 1-2*d], xticks=[], yticks=[])

X = np.random.seed(1)
X = np.random.randn(1000, 4)
cmap = plt.get_cmap("Oranges")
colors = [cmap(i) for i in [.1, .3, .5, .7]]
ax.hist(X, 2, density=True, histtype='bar', color=colors)

fig.savefig(ROOT_DIR / "figures/tip-color-range.pdf")
# plt.show()
