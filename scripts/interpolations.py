import pathlib

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


mpl.style.use([
    pathlib.Path(__file__).parent/'../styles/base.mplstyle',
    pathlib.Path(__file__).parent/'../styles/plotlet-grid.mplstyle',
])


methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

np.random.seed(1)
Z = np.random.uniform(0, 1, (3, 3))


fig, axs = plt.subplots(nrows=6, ncols=3, figsize=(5.7/2.54, 5.7/2.54*2),
                        # fig, axs = plt.subplots(nrows=6, ncols=3, figsize=(4.5,9),
                        subplot_kw={'xticks': [], 'yticks': []})
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(Z, interpolation=interp_method, cmap='viridis',
              extent=[0, 1, 0, 1], rasterized=True)
    ax.text(0.5, 0.1, str(interp_method), weight="bold", color="white", size=6,
            ha="center", va="center")

plt.savefig("../figures/interpolations.pdf", dpi=600)
# plt.show()
