# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import sys
import pathlib

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR / "fonts"))
import custom_fonts  # noqa


fig = plt.figure(figsize=(0.4, 0.4))
margin = 0.01
fig.subplots_adjust(left=margin, right=1-margin, top=1-margin, bottom=margin)
mpl.rc('axes', linewidth=.5)

# Subplots
# -----------------------------------------------------------------------------
nrows, ncols = 3, 3
for i in range(nrows*ncols):
    ax = plt.subplot(ncols, nrows, i+1)
    ax.set_xticks([]), ax.set_yticks([])
fig.savefig(ROOT_DIR / "figures/layout-subplot.pdf")
fig.clear()

# Subplots (colored)
# -----------------------------------------------------------------------------
nrows, ncols = 3, 3
for i in range(nrows*ncols):
    ax = plt.subplot(ncols, nrows, i+1)
    ax.set_xticks([]), ax.set_yticks([])
    if i == 0: ax.set_facecolor("#ddddff")
    if i == 8: ax.set_facecolor("#ffdddd")
fig.savefig(ROOT_DIR / "figures/layout-subplot-color.pdf")
fig.clear()

# Spines
# -----------------------------------------------------------------------------
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[])
ax.spines["top"].set_color("None")
ax.spines["right"].set_color("None")
fig.savefig(ROOT_DIR / "figures/layout-spines.pdf")
fig.clear()


# Gridspec
# -----------------------------------------------------------------------------
gs = fig.add_gridspec(3, 3)
ax1 = fig.add_subplot(gs[0, :], xticks=[], yticks=[])
ax2 = fig.add_subplot(gs[1, :-1], xticks=[], yticks=[])
ax3 = fig.add_subplot(gs[1:, -1], xticks=[], yticks=[])
ax4 = fig.add_subplot(gs[-1, 0], xticks=[], yticks=[])
ax5 = fig.add_subplot(gs[-1, -2], xticks=[], yticks=[])
fig.savefig(ROOT_DIR / "figures/layout-gridspec.pdf")
fig.clear()

# Gridspec (colored)
# -----------------------------------------------------------------------------
gs = fig.add_gridspec(3, 3)
ax1 = fig.add_subplot(gs[0, :], xticks=[], yticks=[])
ax1.set_facecolor("#ddddff")
ax2 = fig.add_subplot(gs[1, :-1], xticks=[], yticks=[])
ax3 = fig.add_subplot(gs[1:, -1], xticks=[], yticks=[])
ax4 = fig.add_subplot(gs[-1, 0], xticks=[], yticks=[])
ax5 = fig.add_subplot(gs[-1, -2], xticks=[], yticks=[])
fig.savefig(ROOT_DIR / "figures/layout-gridspec-color.pdf")
fig.clear()

# Inset axes
# -----------------------------------------------------------------------------
mpl.rc('axes', linewidth=.5)
margin = 0.0125
ax1 = fig.add_axes([margin, margin, 1-2*margin, 1-2*margin], xticks=[], yticks=[])
ax2 = ax1.inset_axes([0.5, 0.5, 0.4, 0.4], xticks=[], yticks=[])
fig.savefig(ROOT_DIR / "figures/layout-inset.pdf")
fig.clear()


# Axes divider
# -----------------------------------------------------------------------------
margin = 0.0125
ax = fig.add_axes([margin, margin, 1-2*margin, 1-2*margin], xticks=[], yticks=[])
divider = make_axes_locatable(ax)
cax = divider.new_horizontal(size="10%", pad=0.025)
fig.add_axes(cax)
cax.set_xticks([]), cax.set_yticks([])
fig.savefig(ROOT_DIR / "figures/layout-divider.pdf")
