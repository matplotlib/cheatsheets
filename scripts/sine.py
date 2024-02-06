# ----------------------------------------------------------------------------
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import pathlib

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


ROOT_DIR = pathlib.Path(__file__).parent.parent

mpl.style.use([
    ROOT_DIR / 'styles/base.mplstyle',
    ROOT_DIR / 'styles/sine-plot.mplstyle',
])

X = np.linspace(0, 10*np.pi, 1000)
Y = np.sin(X)


fig, ax = plt.subplots(figsize=(5.7/2.54, 1.2/2.54))
ax.set_yticks(np.linspace(-1, 1, 5))
ax.plot(X, Y, color="C1")
fig.savefig(ROOT_DIR / "figures/sine.pdf")


X = np.linspace(0.1, 10*np.pi, 1000)
Y = np.sin(X)


fig, ax = plt.subplots(figsize=(5.7/2.54, 1.0/2.54))
ax.plot(X, Y, "C1o:", markevery=50, mec="1.0")
ax.set_ylim(-1.5, 1.5)
fig.savefig(ROOT_DIR / "figures/sine-marker.pdf")


fig, ax = plt.subplots(figsize=(5.7/2.54, 1.0/2.54))
ax.set_xscale("log")
ax.plot(X, Y, "C1o-", markevery=50, mec="1.0")
ax.set_ylim(-1.5, 1.5)
fig.savefig(ROOT_DIR / "figures/sine-logscale.pdf")


fig, ax = plt.subplots(figsize=(5.7/2.54, 1.0/2.54))
ax.plot(X, Y, "C1")
ax.fill_betweenx([-1.5, 1.5], [0], [2*np.pi], color=".9")
ax.text(0, -1, r" Period $\Phi$", va="top")
ax.set_ylim(-1.5, 1.5)
fig.savefig(ROOT_DIR / "figures/sine-period.pdf")


fig, ax = plt.subplots(figsize=(5.7/2.54, 1.0/2.54))
ax.plot(X, np.sin(X), "C0", label="Sine")
ax.plot(X, np.cos(X), "C1", label="Cosine")
ax.legend(bbox_to_anchor=(0.0, .9, 1.02, 0.1),
          frameon=False, mode="expand", ncol=2, loc="lower left")
ax.set_title("Sine and Cosine")
ax.set_xticks([]), ax.set_yticks([])
ax.set_ylim(-1.25, 1.25)
fig.savefig(ROOT_DIR / "figures/sine-legend.pdf")


fig, ax = plt.subplots(figsize=(5.7/2.54, 1.0/2.54))
X = np.linspace(0, 10*np.pi, 1000)
Y = np.sin(X)
ax.plot(X, Y, "C1o-", markevery=50, mec="1.0")
ax.set_ylim(-1.5, 1.5)
ax.annotate(" ", (X[200], Y[200]), (X[250], -1), ha="center", va="center",
            arrowprops=dict(arrowstyle="->", color="C1", linewidth=0.5, patchA=None, shrinkA=4, shrinkB=0.5))
ax.annotate("A", (X[250], Y[250]), (X[250], -1), ha="center", va="center",
            arrowprops=dict(arrowstyle="->", color="C1", linewidth=0.5, patchA=None, shrinkA=4, shrinkB=0.5))
ax.annotate(" ", (X[300], Y[300]), (X[250], -1), ha="center", va="center",
            arrowprops=dict(arrowstyle="->", color="C1", linewidth=0.5, patchA=None, shrinkA=4, shrinkB=0.5))
fig.savefig(ROOT_DIR / "figures/sine-annotate.pdf")
