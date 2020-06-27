# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------

# Scripts to generate all the basic plots 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(0.4,0.4))
mpl.rcParams['axes.linewidth'] = 0.5
mpl.rcParams['xtick.major.size'] = 0.0
mpl.rcParams['ytick.major.size'] = 0.0
d = 0.01

# Basic line plot (color)
# -----------------------------------------------------------------------------
ax = fig.add_axes([d,d,1-2*d,1-2*d])
X = np.linspace(0, 10, 100)
Y = 4+2*np.sin(2*X)
ax.plot(X, Y, color="black", linewidth=0.75)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.grid(linewidth=0.125)
plt.savefig("../figures/plot-color.pdf")
fig.clear()

# Basic line plot (linestyle)
# -----------------------------------------------------------------------------
ax = fig.add_axes([d,d,1-2*d,1-2*d])
X = np.linspace(0, 10, 100)
Y = 4+2*np.sin(2*X)
ax.plot(X, Y, color="C1", linewidth=0.75, linestyle="--")
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.grid(linewidth=0.125)
plt.savefig("../figures/plot-linestyle.pdf")
fig.clear()

# Basic line plot (linewidth)
# -----------------------------------------------------------------------------
ax = fig.add_axes([d,d,1-2*d,1-2*d])
X = np.linspace(0, 10, 100)
Y = 4+2*np.sin(2*X)
ax.plot(X, Y, color="C1", linewidth=1.5)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.grid(linewidth=0.125)
plt.savefig("../figures/plot-linewidth.pdf")
fig.clear()

# Basic line plot (marker)
# -----------------------------------------------------------------------------
ax = fig.add_axes([d,d,1-2*d,1-2*d])
X = np.linspace(0, 10, 100)
Y = 4+2*np.sin(2*X)
ax.plot(X, Y, color="C1", linewidth=0.75, marker="o", markevery=5, markersize=2)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.grid(linewidth=0.125)
plt.savefig("../figures/plot-marker.pdf")
fig.clear()

# Basic line plot (multi)
# -----------------------------------------------------------------------------
ax = fig.add_axes([d,d,1-2*d,1-2*d])
X = np.linspace(0, 10, 100)
Y1 = 4+2*np.sin(2*X)
Y2 = 4+2*np.cos(2*X)
ax.plot(X, Y1, color="C1", linewidth=0.75)
ax.plot(X, Y2, color="C0", linewidth=0.75)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.grid(linewidth=0.125)
plt.savefig("../figures/plot-multi.pdf")
fig.clear()

# Basic line plot (vsplit)
# -----------------------------------------------------------------------------
ax1 = fig.add_axes([d, d, 1-2*d,.45-d])
ax2 = fig.add_axes([d, .55-d, 1-2*d,.45-d])

X = np.linspace(0, 10, 100)
Y1 = 2+1*np.sin(2*X)
ax1.plot(X, Y1, color="C1", linewidth=0.75)
ax1.set_xlim(0, 8), ax1.set_xticks(np.arange(1,8)), ax1.set_xticklabels([])
ax1.set_ylim(0, 4), ax1.set_yticks(np.arange(1,4)), ax1.set_yticklabels([])
ax1.grid(linewidth=0.125)
ax1.tick_params(axis=u'both', which=u'both',length=0)

Y2 = 2+1*np.cos(2*X)
ax2.plot(X, Y2, color="C0", linewidth=0.75)
ax2.set_xlim(0, 8), ax2.set_xticks(np.arange(1,8)), ax2.set_xticklabels([])
ax2.set_ylim(0, 4), ax2.set_yticks(np.arange(1,4)), ax2.set_yticklabels([])
ax2.grid(linewidth=0.125)
ax2.tick_params(axis=u'both', which=u'both',length=0)
plt.savefig("../figures/plot-vsplit.pdf")
fig.clear()

# Basic line plot (hsplit)
# -----------------------------------------------------------------------------
ax1 = fig.add_axes([d, d, .45-d, 1-2*d])
ax2 = fig.add_axes([.55-d, d, .45-d, 1-2*d])

X = np.linspace(0, 10, 100)
Y1 = 2+1*np.sin(2*X)
ax1.plot(Y1, X, color="C1", linewidth=0.75)
ax1.set_xlim(0, 4), ax1.set_xticks(np.arange(1,4)), ax1.set_xticklabels([])
ax1.set_ylim(0, 8), ax1.set_yticks(np.arange(1,8)), ax1.set_yticklabels([])
ax1.grid(linewidth=0.125)
ax1.tick_params(axis=u'both', which=u'both',length=0)

Y2 = 2+1*np.cos(2*X)
ax2.plot(Y2, X, color="C0", linewidth=0.75)
ax2.set_xlim(0, 4), ax2.set_xticks(np.arange(1,4)), ax2.set_xticklabels([])
ax2.set_ylim(0, 8), ax2.set_yticks(np.arange(1,8)), ax2.set_yticklabels([])
ax2.grid(linewidth=0.125)
ax2.tick_params(axis=u'both', which=u'both',length=0)
plt.savefig("../figures/plot-hsplit.pdf")
fig.clear()

# Basic line plot (title)
# -----------------------------------------------------------------------------
ax = fig.add_axes([d,d,1-2*d,.8-2*d])
X = np.linspace(0, 10, 100)
Y = 3+2*np.sin(2*X)
ax.plot(X, Y, color="C1", linewidth=0.75)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 6), ax.set_yticks(np.arange(1,6))
ax.grid(linewidth=0.125)
ax.text(4, 6.75, "A Sine wave", transform=ax.transData, clip_on=False,
        weight="bold", size=4, ha="center", va="center")
plt.savefig("../figures/plot-title.pdf")
fig.clear()


# Basic line plot (xlabel)
# -----------------------------------------------------------------------------
ax = fig.add_axes([d,.2-d,1-2*d,.8-2*d])
X = np.linspace(0, 10, 100)
Y = 3+2*np.sin(2*X)
ax.plot(X, Y, color="C1", linewidth=0.75)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8)), ax.set_xticklabels([])
ax.set_ylim(0, 6), ax.set_yticks(np.arange(1,6)), ax.set_yticklabels([])
ax.grid(linewidth=0.125)
ax.text(4, -1, "Time", transform=ax.transData, clip_on=False,
        size=3.5, ha="center", va="center")
# plt.show()
plt.savefig("../figures/plot-xlabel.pdf")
fig.clear()

