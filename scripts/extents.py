# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------

# Scripts to generate all the basic plots 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

Z = np.arange(5*5).reshape(5,5)

fig = plt.figure(figsize=(8,5))

ax = fig.add_subplot(2,2,1)
ax.imshow(Z, extent=[0,10,0,5], interpolation="nearest", origin="upper")
ax.set_xlim(-1, 11), ax.set_xticks([])
ax.set_ylim(-1, 6), ax.set_yticks([0,5])
ax.text(1, 4.5, "(0,0)", ha="center", va="center", color="white", size="large")
ax.text(9, 0.5, "(4,4)", ha="center", va="center", color="black", size="large")
ax.text(5.0, 5.5, 'origin="upper"',
        ha="center", va="center", color="black", size="large")
ax.text(5.0, -0.5, "extent=[0,10,0,5]",
        ha="center", va="center", color="black", size="large")

ax = fig.add_subplot(2,2,3)
ax.imshow(Z, extent=[0,10,0,5], interpolation="nearest", origin="lower")
ax.set_xlim(-1, 11), ax.set_xticks([0,10])
ax.set_ylim(-1, 6), ax.set_yticks([0,5])
ax.text(1, 0.5, "(0,0)", ha="center", va="center", color="white", size="large")
ax.text(9, 4.5, "(4,4)", ha="center", va="center", color="black", size="large")

ax.text(5.0, 5.5, 'origin="lower"',
        ha="center", va="center", color="black", size="large")
ax.text(5.0, -0.5, "extent=[0,10,0,5]",
        ha="center", va="center", color="black", size="large")


ax = fig.add_subplot(2,2,4)
ax.imshow(Z, extent=[10,0,0,5], interpolation="nearest", origin="lower")
ax.set_xlim(-1, 11), ax.set_xticks([0,10])
ax.set_ylim(-1, 6), ax.set_yticks([])
ax.text(9, 0.5, "(0,0)", ha="center", va="center", color="white", size="large")
ax.text(1, 4.5, "(4,4)", ha="center", va="center", color="black", size="large")
ax.text(5.0, 5.5, 'origin="lower"',
        ha="center", va="center", color="black", size="large")
ax.text(5.0, -0.5, "extent=[10,0,0,5]",
        ha="center", va="center", color="black", size="large")
plt.tight_layout()


ax = fig.add_subplot(2,2,2)
ax.imshow(Z, extent=[10,0,0,5], interpolation="nearest", origin="upper")
ax.set_xlim(-1, 11), ax.set_xticks([])
ax.set_ylim(-1, 6), ax.set_yticks([])
ax.text(9, 4.5, "(0,0)", ha="center", va="center", color="white", size="large")
ax.text(1, 0.5, "(4,4)", ha="center", va="center", color="black", size="large")
ax.text(5.0, 5.5, 'origin="upper"',
        ha="center", va="center", color="black", size="large")
ax.text(5.0, -0.5, "extent=[10,0,0,5]",
        ha="center", va="center", color="black", size="large")
plt.tight_layout()


plt.savefig("../figures/extents.pdf", dpi=600)
plt.show()



