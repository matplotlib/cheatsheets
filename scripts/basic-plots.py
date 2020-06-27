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
ax = fig.add_axes([d,d,1-2*d,1-2*d])

# Basic line plot
# -----------------------------------------------------------------------------
X = np.linspace(0, 10, 100)
Y = 4+2*np.sin(2*X)
ax.plot(X, Y, color="C1", linewidth=0.75)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.grid(linewidth=0.125)
plt.savefig("../figures/basic-plot.pdf")
ax.clear()


# Basic line plot (color)
# -----------------------------------------------------------------------------
X = np.linspace(0, 10, 100)
Y = 4+2*np.sin(2*X)
ax.plot(X, Y, color="black", linewidth=0.75)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.grid(linewidth=0.125)
plt.savefig("../figures/basic-plot-color.pdf")
ax.clear()

# Basic scatter plot
# -----------------------------------------------------------------------------
np.random.seed(3)
X = 4+np.random.normal(0, 1.25, 24)
Y = 4+np.random.normal(0, 1.25, len(X))
ax.scatter(X, Y, 5, zorder=10,
           edgecolor="white", facecolor="C1", linewidth=0.25)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.grid(linewidth=0.125)
plt.savefig("../figures/basic-scatter.pdf")
ax.clear()

# Basic bar plot
# -----------------------------------------------------------------------------
np.random.seed(3)
X = 0.5 + np.arange(8)
Y = np.random.uniform(2, 7, len(X))
ax.bar(X, Y, bottom=0, width=1, 
       edgecolor="white", facecolor="C1", linewidth=0.25)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.set_axisbelow(True)
ax.grid(linewidth=0.125)
plt.savefig("../figures/basic-bar.pdf")
ax.clear()


# Basic imshow plot
# -----------------------------------------------------------------------------
np.random.seed(3)
I = np.zeros((8,8,4))
I[:,:] = mpl.colors.to_rgba("C1")
I[...,3] = np.random.uniform(0.25,1.0,(8,8))
ax.imshow(I, extent=[0,8,0,8], interpolation="nearest")
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.grid(linewidth=0.25, color="white")
plt.savefig("../figures/basic-imshow.pdf")
ax.clear()


# Basic contour plot
# -----------------------------------------------------------------------------
np.random.seed(1)
X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-3, 3, 256))
Z = (1 - X/2. + X**5 + Y**3)*np.exp(-X**2-Y**2)
Z = Z - Z.min()
colors = np.zeros((5,4))
colors[:] = mpl.colors.to_rgba("C1")
colors[:,3] = np.linspace(0.15, 0.85, len(colors))
plt.contourf(Z, len(colors), extent=[0,8,0,8], colors=colors)
plt.contour(Z, len(colors), extent=[0,8,0,8], colors="white", linewidths=0.125,
            nchunk=10)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
# ax.set_axisbelow(True)
# ax.grid(linewidth=0.125, color="0.75")
plt.savefig("../figures/basic-contour.pdf")
ax.clear()


# Basic pie plot
# -----------------------------------------------------------------------------
X = 1,2,3,4
colors = np.zeros((len(X),4))
colors[:] = mpl.colors.to_rgba("C1")
colors[:,3] = np.linspace(0.25, 0.75, len(X))
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.set_axisbelow(True)
ax.grid(linewidth=0.25, color="0.75")
ax.pie(X, colors=["white",]*len(X), radius=3, center=(4,4), 
        wedgeprops = {"linewidth": 0.25, "edgecolor": "white"}, frame=True)
ax.pie(X, colors=colors, radius=3, center=(4,4), 
        wedgeprops = {"linewidth": 0.25, "edgecolor": "white"}, frame=True)
plt.savefig("../figures/basic-pie.pdf")
ax.clear()


# Basic text plot
# -----------------------------------------------------------------------------
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.set_axisbelow(True)
ax.grid(linewidth=0.25, color="0.75")
ax.text(4, 4, "TEXT", color="C1", size=8, weight="bold",
        ha="center", va="center", rotation=25)
plt.savefig("../figures/basic-text.pdf")
ax.clear()

# Basic fill plot
# -----------------------------------------------------------------------------
np.random.seed(1)
X = np.linspace(0, 8, 16)
Y1 = 3 + 4*X/8 + np.random.uniform(0.0, 0.5, len(X))
Y2 = 1 + 2*X/8 + np.random.uniform(0.0, 0.5, len(X))
plt.fill_between(X, Y1, Y2, color="C1", alpha=.5, linewidth=0)
plt.plot(X, (Y1+Y2)/2, color="C1", linewidth=0.5)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.set_axisbelow(True)
ax.grid(linewidth=0.125, color="0.75")
plt.savefig("../figures/basic-fill.pdf")
ax.clear()

# Basic quiver plot
# -----------------------------------------------------------------------------
np.random.seed(1)
T = np.linspace(0, 2*np.pi, 8)
X, Y = 4 + 1*np.cos(T), 4 + 1*np.sin(T)
U, V = 1.5*np.cos(T), 1.5*np.sin(T)
plt.quiver(X, Y, U, V, color="C1",
           angles='xy', scale_units='xy', scale=0.5, width=.05)
ax.set_xlim(0, 8), ax.set_xticks(np.arange(1,8))
ax.set_ylim(0, 8), ax.set_yticks(np.arange(1,8))
ax.set_axisbelow(True)
ax.grid(linewidth=0.125, color="0.75")
plt.savefig("../figures/basic-quiver.pdf")
ax.clear()

