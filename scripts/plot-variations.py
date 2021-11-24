# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import pathlib

# Scripts to generate all the basic plots
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


mpl.style.use([
    pathlib.Path(__file__).parent/'../styles/base.mplstyle',
    pathlib.Path(__file__).parent/'../styles/plotlet.mplstyle',
])
mpl.rc('axes', titlepad=1)


subplot_kw = dict(
    xlim=(0, 8), xticks=np.arange(1, 8),
    ylim=(0, 8), yticks=np.arange(1, 8),
)

# Basic line plot (color)
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
X = np.linspace(0, 10, 100)
Y = 4+2*np.sin(2*X)
ax.plot(X, Y, color="black", linewidth=0.75)
ax.grid()
fig.savefig("../figures/plot-color.pdf")

# Basic line plot (linestyle)
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
X = np.linspace(0, 10, 100)
Y = 4+2*np.sin(2*X)
ax.plot(X, Y, color="C1", linewidth=0.75, linestyle="--")
ax.grid()
fig.savefig("../figures/plot-linestyle.pdf")

# Basic line plot (linewidth)
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
X = np.linspace(0, 10, 100)
Y = 4+2*np.sin(2*X)
ax.plot(X, Y, color="C1", linewidth=1.5)
ax.grid()
fig.savefig("../figures/plot-linewidth.pdf")

# Basic line plot (marker)
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
X = np.linspace(0, 10, 100)
Y = 4+2*np.sin(2*X)
ax.plot(X, Y, color="C1", linewidth=0.75, marker="o", markevery=5, markersize=2)
ax.grid()
fig.savefig("../figures/plot-marker.pdf")

# Basic line plot (multi)
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
X = np.linspace(0, 10, 100)
Y1 = 4+2*np.sin(2*X)
Y2 = 4+2*np.cos(2*X)
ax.plot(X, Y1, color="C1", linewidth=0.75)
ax.plot(X, Y2, color="C0", linewidth=0.75)
ax.grid()
fig.savefig("../figures/plot-multi.pdf")

# Basic line plot (vsplit)
# -----------------------------------------------------------------------------
(fig, [ax2, ax1]) = plt.subplots(nrows=2, gridspec_kw=dict(hspace=0.2), subplot_kw=subplot_kw)

X = np.linspace(0, 10, 100)
Y1 = 2+1*np.sin(2*X)
ax1.plot(X, Y1, color="C1", linewidth=0.75)
ax1.set_ylim(0, 4), ax1.set_yticks(np.arange(1, 4))
ax1.grid()
ax1.tick_params(axis=u'both', which=u'both', length=0)

Y2 = 2+1*np.cos(2*X)
ax2.plot(X, Y2, color="C0", linewidth=0.75)
ax2.set_ylim(0, 4), ax2.set_yticks(np.arange(1, 4))
ax2.grid()
ax2.tick_params(axis=u'both', which=u'both', length=0)
fig.savefig("../figures/plot-vsplit.pdf")

# Basic line plot (hsplit)
# -----------------------------------------------------------------------------
(fig, [ax1, ax2]) = plt.subplots(ncols=2, gridspec_kw=dict(wspace=0.2), subplot_kw=subplot_kw)

X = np.linspace(0, 10, 100)
Y1 = 2+1*np.sin(2*X)
ax1.plot(Y1, X, color="C1", linewidth=0.75)
ax1.set_xlim(0, 4), ax1.set_xticks(np.arange(1, 4))
ax1.grid()
ax1.tick_params(axis=u'both', which=u'both', length=0)

Y2 = 2+1*np.cos(2*X)
ax2.plot(Y2, X, color="C0", linewidth=0.75)
ax2.set_xlim(0, 4), ax2.set_xticks(np.arange(1, 4))
ax2.grid()
ax2.tick_params(axis=u'both', which=u'both', length=0)
fig.savefig("../figures/plot-hsplit.pdf")

# Basic line plot (title)
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
X = np.linspace(0, 10, 100)
Y = 3+2*np.sin(2*X)
ax.plot(X, Y, color="C1", linewidth=0.75)
ax.set_ylim(0, 6), ax.set_yticks(np.arange(1, 6))
ax.grid()
ax.set_title("A Sine wave", size=4, weight="bold")
fig.savefig("../figures/plot-title.pdf")

# Basic line plot (xlabel)
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw=subplot_kw)
X = np.linspace(0, 10, 100)
Y = 3+2*np.sin(2*X)
ax.plot(X, Y, color="C1", linewidth=0.75), ax.set_xticklabels([])
ax.set_ylim(0, 6), ax.set_yticks(np.arange(1, 6)), ax.set_yticklabels([])
ax.grid()
ax.text(4, -1, "Time", transform=ax.transData, clip_on=False,
        size=3.5, ha="center", va="center")
fig.savefig("../figures/plot-xlabel.pdf")
