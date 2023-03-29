# ----------------------------------------------------------------------------
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import pathlib

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


ROOT_DIR = pathlib.Path(__file__).parent.parent

mpl.rcParams['axes.linewidth'] = 1.5

fig = plt.figure(figsize=(8, 1.5))
dx, dy = 0.0025, 0.01
ax = fig.add_axes([dx, dy, 1-2*dx, 1-2*dy], frameon=False)
X, Y = [], []
for x in np.linspace(0.01, 10*np.pi-0.01, 100):
    X.extend([x, x, None])
    Y.extend([0, np.sin(x), None])
print(X[:10], Y[:10])
plt.plot(X, Y, "black")
plt.xticks([]), plt.yticks([])
plt.xlim(-0.25, 10*np.pi+.25)
plt.ylim(-1.5, 1.5)
plt.tight_layout()
fig.savefig(ROOT_DIR / "figures/tip-multiline.pdf", dpi=100)
# plt.show()
