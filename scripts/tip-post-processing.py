import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvas
from scipy.ndimage import gaussian_filter

# First pass for drop-shadow
fig = Figure(figsize=(6,1.5))
canvas = FigureCanvas(fig)
ax = fig.add_axes([0,0,1,1], frameon=False,
                  xlim=[0,1], xticks=[], ylim=[0,1], yticks=[])
ax.text(0.5, 0.5, "Matplotlib", transform=ax.transAxes,
        ha="center", va="center", size=64, color="black")
canvas.draw()
Z = np.array(canvas.renderer.buffer_rgba())[:,:,0]
Z = gaussian_filter(Z, sigma=9)

# Second pass for text + drop-shadow
fig = plt.figure(figsize=(6,1.5))
ax = fig.add_axes([0,0,1,1], frameon=False,
                  xlim=[0,1], xticks=[], ylim=[0,1], yticks=[])
ax.imshow(Z, extent=[0,1,0,1], cmap=plt.cm.gray, alpha=0.65, aspect='auto')
ax.text(0.5, 0.5, "Matplotlib", transform=ax.transAxes,
        ha="center", va="center", size=64, color="black")

plt.savefig("../figures/tip-post-processing.pdf", dpi=600)
# plt.show()
