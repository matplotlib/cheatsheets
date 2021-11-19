# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------

# Script to generate the tips
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects


mpl.rcParams['axes.linewidth'] = 1.5

margin = 0.01
rect = [margin, margin, 1-2*margin, 1-2*margin]


# color range
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(2, 2))
ax = fig.add_axes(rect, xticks=[], yticks=[])

np.random.seed(1)
X = np.random.randn(1000, 4)
cmap = plt.get_cmap("Oranges")
colors = [cmap(i) for i in [0.1, 0.3, 0.5, 0.7]]
ax.hist(X, 2, density=True, histtype='bar', color=colors)

fig.savefig("../figures/tip-color-range.pdf")


# colorbar
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(2.15, 2))
ax = fig.add_axes(rect, xticks=[], yticks=[])

np.random.seed(1)
Z = np.random.uniform(0, 1, (8, 8))
cmap = plt.get_cmap("Oranges")
im = ax.imshow(Z, interpolation="nearest", cmap=cmap, vmin=0, vmax=2)
cb = fig.colorbar(im, fraction=0.046, pad=0.04)
cb.set_ticks([])

fig.savefig("../figures/tip-colorbar.pdf")


# dotted
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(5, 0.25))

ax = fig.add_axes(
    [0, 0, 1, 1], frameon=False, xticks=[], yticks=[], xlim=[0, 1], ylim=[-0.5, 1.5]
)

epsilon=1e-12
ax.plot([0,1], [0,0], "black", clip_on=False, lw=8,
         ls=(.5,(epsilon, 1)), dash_capstyle="round")
ax.plot([0,1], [1,1], "black", clip_on=False, lw=8,
         ls=(-.5,(epsilon, 2)), dash_capstyle="round")
fig.savefig("../figures/tip-dotted.pdf")


# dual axis
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(2, 2))
ax1 = fig.add_axes(rect, label="cartesian")
ax2 = fig.add_axes(rect, projection="polar", label="polar")

ax1.set_xticks([])  # np.linspace(0.0, 0.4, 5))
ax1.set_yticks([])  # np.linspace(0.0, 1.0, 11))

ax2.set_rorigin(0)
ax2.set_thetamax(90)
ax2.set_ylim(0.5, 1.0)
ax2.set_xticks(np.linspace(0, np.pi/2, 10))
ax2.set_yticks(np.linspace(0.5, 1.0, 5))

ax2.set_xticklabels([])
ax2.set_yticklabels([])

fig.savefig("../figures/tip-dual-axis.pdf")


# font family
# -----------------------------------------------------------------------------
# Setup a plot such that only the bottom spine is shown
def setup(ax):
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.yaxis.set_major_locator(mpl.ticker.NullLocator())
    ax.spines['top'].set_color('none')

    ax.spines['bottom'].set_linewidth(1)
    ax.spines['bottom'].set_position("center")

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00)
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', width=0.75)
    ax.tick_params(which='minor', length=2.5)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.patch.set_alpha(0.0)


fig = plt.figure(figsize=(5, 0.5))
fig.patch.set_alpha(0.0)
n = 1

fontsize = 18
ax = plt.subplot(n, 1, 1)
ax.tick_params(axis='both', which='minor', labelsize=6)
setup(ax)
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.2))
ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
ax.xaxis.set_minor_formatter(mpl.ticker.ScalarFormatter())
ax.tick_params(axis='x', which='minor', rotation=0)

for tick in ax.get_xticklabels(which='both'):
    tick.set_fontname("Roboto Condensed")

fig.tight_layout()
fig.savefig("../figures/tip-font-family.pdf", transparent=True)


# hatched
# -----------------------------------------------------------------------------
cmap = plt.get_cmap("Oranges")
color1, color2 = cmap(0.3), cmap(0.5)

mpl.rcParams['hatch.color'] = color1
mpl.rcParams['hatch.linewidth'] = 8

fig = plt.figure(figsize=(2, 2))
ax = plt.subplot()
np.random.seed(123)

x1, y1 = 3 * np.arange(2), np.random.randint(25, 50, 2)
x2, y2 = x1 + 1, np.random.randint(25, 75, 2)

ax.bar(x1, y1, color=color2)
for i in range(len(x1)):
    ax.annotate("%d%%" % y1[i],  (x1[i], y1[i]), xytext=(0,1),
                 fontsize="x-small", color=color2,
                 textcoords="offset points", va="bottom", ha="center")

ax.bar(x2, y2, color=color2, hatch="/")
for i in range(len(x2)):
    ax.annotate("%d%%" % y2[i],  (x2[i], y2[i]), xytext=(0,1),
                 fontsize="x-small", color=color2,
                 textcoords="offset points", va="bottom", ha="center")

ax.set_yticks([])
ax.set_xticks(0.5 + np.arange(0, 6, 3))
ax.set_xticklabels(["2018", "2019"])
ax.tick_params('x', length=0, labelsize="small", which='major')

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)

fig.tight_layout()
fig.savefig("../figures/tip-hatched.pdf")


# multiline
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(8, 1.5))
dx, dy = 0.0025, 0.01
ax = fig.add_axes([dx, dy, 1-2*dx, 1-2*dy], frameon=False)
X, Y = [], []
for x in np.linspace(0.01, 10*np.pi-0.01, 100):
    X.extend([x, x, None])
    Y.extend([0, np.sin(x), None])
print(X[:10], Y[:10])
ax.plot(X, Y, "black")
ax.set_xticks([]), ax.set_yticks([])
ax.set_xlim(-0.25, 10*np.pi+0.25)
ax.set_ylim(-1.5, 1.5)
fig.tight_layout()
fig.savefig("../figures/tip-multiline.pdf", dpi=100)


# outline
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(2, 2))
ax = fig.add_axes(rect, xticks=[], yticks=[])

np.random.seed(1)
Z = np.random.uniform(0, 1, (8, 8))
cmap = plt.get_cmap("Oranges")
ax.imshow(Z, interpolation="nearest", cmap=cmap, vmin=0, vmax=2)

text = ax.text(0.5, 0.1, "Label", transform=ax.transAxes,
             color=cmap(0.9), size=32, weight="bold", ha="center", va="bottom")
text.set_path_effects([path_effects.Stroke(linewidth=5, foreground='white'),
                       path_effects.Normal()])
fig.savefig("../figures/tip-outline.pdf")


# transparency
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(2, 2), dpi=100)
ax = fig.add_axes(rect)
n = 500
np.random.seed(5)
X = np.random.normal(0, 0.25, n)
Y = np.random.normal(0, 0.25, n)
ax.scatter(X, Y, s=50, c="k", lw=2)
ax.scatter(X, Y, s=50, c="w", lw=0)
ax.scatter(X, Y, s=40, c="C1", lw=0, alpha=0.1)

ax.set_xlim([-1, 1]), ax.set_xticks([]),
ax.set_ylim([-1, 1]), ax.set_yticks([])
fig.savefig("../figures/tip-transparency.pdf")
