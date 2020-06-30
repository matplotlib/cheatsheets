# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', linewidth=1.5)

fig = plt.figure(figsize=(2, 2), dpi=100)
margin = 0.01
ax = fig.add_axes([margin, margin, 1-2*margin, 1-2*margin])
n = 500
X = np.random.normal(0, 0.25, n)
Y = np.random.normal(0, 0.25, n)
ax.scatter(X, Y, s=50, c="k",  lw=2)
ax.scatter(X, Y, s=50, c="w",  lw=0)
ax.scatter(X, Y, s=40, c="C1", lw=0, alpha=0.1)

ax.set_xlim([-1, 1]), ax.set_xticks([]),
ax.set_ylim([-1, 1]), ax.set_yticks([])
plt.savefig("../figures/tip-transparency.pdf")
plt.show()
