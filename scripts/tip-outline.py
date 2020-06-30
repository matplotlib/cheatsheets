# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------

# Scripts to generate all the basic plots 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

fig = plt.figure(figsize=(2,2))
mpl.rcParams['axes.linewidth'] = 1.5
d = 0.01

ax = fig.add_axes([d,d,1-2*d,1-2*d], xticks=[], yticks=[])

np.random.seed(1)
Z = np.random.uniform(0,1,(8,8))
cmap = plt.get_cmap("Oranges")
ax.imshow(Z, interpolation="nearest", cmap=cmap, vmin=0, vmax=2)

text = ax.text(0.5, 0.1, "Label", transform=ax.transAxes,
             color=cmap(0.9), size=32, weight="bold", ha="center", va="bottom")
text.set_path_effects([path_effects.Stroke(linewidth=5, foreground='white'),
                       path_effects.Normal()])
plt.savefig("../figures/tip-outline.pdf")

