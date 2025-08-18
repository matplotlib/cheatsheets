# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------

# Script to generate all the advanced plots
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
    ROOT_DIR / 'styles/plotlet.mplstyle',
])


subplot_kw = dict(
    xlim=(0, 8), xticks=np.arange(1, 8),
    ylim=(0, 8), yticks=np.arange(1, 8),
)

# Step plot
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
X = np.linspace(0, 10, 16)
Y = 4 + 2*np.sin(2*X)
ax.step(X, Y, color="C1")
ax.grid()
fig.savefig(ROOT_DIR / "figures/advanced-step.pdf")

# Violin plot
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
np.random.seed(10)
D = np.random.normal((3, 5, 4), (0.75, 1.00, 0.75), (200, 3))
VP = ax.violinplot(D, [2, 4, 6], widths=1.5,
                   showmeans=False, showmedians=False, showextrema=False)
for body in VP['bodies']:
    body.set_facecolor('C1')
    body.set_alpha(1)
ax.set_axisbelow(True)
ax.grid()
fig.savefig(ROOT_DIR / "figures/advanced-violin.pdf")

# Boxplot
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
np.random.seed(10)
D = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (100, 3))
VP = ax.boxplot(D, positions=[2, 4, 6], widths=1.5, patch_artist=True,
                showmeans=False, showfliers=False,
                medianprops={"color": "white",
                             "linewidth": 0.25},
                boxprops={"facecolor": "C1",
                          "edgecolor": "white",
                          "linewidth": 0.25},
                whiskerprops={"color": "C1",
                              "linewidth": 0.75},
                capprops={"color": "C1",
                          "linewidth": 0.75})
ax.set_axisbelow(True)
ax.grid()
fig.savefig(ROOT_DIR / "figures/advanced-boxplot.pdf")

# Barbs plot
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
np.random.seed(1)
X = [[2, 4, 6]]
Y = [[1.5, 3, 2]]
U = -np.ones((1, 3)) * 0
V = -np.ones((1, 3)) * np.linspace(50, 100, 3)
ax.barbs(X, Y, U, V, barbcolor="C1", flagcolor="C1", length=5, linewidth=0.5)
ax.set_axisbelow(True)
ax.grid()
fig.savefig(ROOT_DIR / "figures/advanced-barbs.pdf")

# Event plot
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
np.random.seed(1)
X = [2, 4, 6]
D = np.random.gamma(4, size=(3, 50))
ax.eventplot(D, colors="C1", orientation="vertical", lineoffsets=X,
             linewidth=0.25)
ax.set_axisbelow(True)
ax.grid()
fig.savefig(ROOT_DIR / "figures/advanced-event.pdf")

# Errorbar plot
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
np.random.seed(1)
X = [2, 4, 6]
Y = [4, 5, 4]
E = np.random.uniform(0.5, 1.5, 3)
ax.errorbar(X, Y, E, color="C1", linewidth=0.75, capsize=1)
ax.set_axisbelow(True)
ax.grid()
fig.savefig(ROOT_DIR / "figures/advanced-errorbar.pdf")

# Hexbin plot
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
np.random.seed(1)
X = np.random.uniform(1.5, 6.5, 100)
Y = np.random.uniform(1.5, 6.5, 100)
C = np.random.uniform(0, 1, 10000)
ax.hexbin(X, Y, C, gridsize=4, linewidth=0.25, edgecolor="white",
          cmap=plt.get_cmap("Wistia"), alpha=1.0)
ax.set_axisbelow(True)
ax.grid()
fig.savefig(ROOT_DIR / "figures/advanced-hexbin.pdf")

# Hist plot
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
np.random.seed(1)
X = 4 + np.random.normal(0, 1.5, 200)
ax.hist(X, bins=8, facecolor="C1", linewidth=0.25, edgecolor="white")
ax.set_ylim(0, 80), ax.set_yticks(np.arange(1, 80, 10))
ax.set_axisbelow(True)
ax.grid()
fig.savefig(ROOT_DIR / "figures/advanced-hist.pdf")

# Xcorr plot
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
np.random.seed(3)
Y = np.random.uniform(-4, 4, 250)
X = np.random.uniform(-4, 4, 250)
ax.xcorr(X, Y, usevlines=True, maxlags=6, normed=True, lw=1,
         color="C1")
ax.set_xlim(-8, 8), ax.set_xticks(np.arange(-8, 8, 2))
ax.set_ylim(-.25, .25), ax.set_yticks(np.linspace(-.25, .25, 9))
ax.set_axisbelow(True)
ax.grid()
fig.savefig(ROOT_DIR / "figures/advanced-xcorr.pdf")
