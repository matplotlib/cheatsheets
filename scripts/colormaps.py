import pathlib

import numpy as np
import matplotlib.pyplot as plt


ROOT_DIR = pathlib.Path(__file__).parent.parent

figsize = 4.0, 0.25
fig = plt.figure(figsize=figsize)
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
ymin, ymax=  0, 1
xmin, xmax = 0, figsize[0]/figsize[1]

# Uniform colormaps
# -----------------------------------------------------------------------------
cmaps = ('viridis', 'plasma', 'inferno', 'magma', 'cividis',

         'PRGn', 'PiYG', 'RdYlGn', 'BrBG', 'RdGy', 'PuOr', 'RdBu',
         'RdYlBu', 'Spectral', 'coolwarm', 'bwr', 'seismic',

         'tab10', 'tab20', 'tab20b', 'tab20c',
         'Pastel1', 'Pastel2', 'Paired',
         'Set1', 'Set2', 'Set3', 'Accent', 'Dark2',

         'Greys', 'Reds', 'Oranges', 'YlOrBr', 'YlOrRd', 'OrRd',
         'PuRd', 'RdPu', 'BuPu', 'Purples', 'YlGnBu', 'Blues',
         'PuBu', 'GnBu', 'PuBuGn', 'BuGn', 'Greens', 'YlGn',

         'bone', 'gray', 'pink', 'afmhot', 'hot', 'gist_heat', 'copper',
         'Wistia', 'autumn', 'summer', 'spring', 'cool', 'winter',

         'twilight', 'twilight_shifted', 'hsv',

         'terrain', 'ocean', 'gist_earth', 'cubehelix', 'rainbow'
         )

for name in cmaps:
    # The maximum number of segments in a cmap is 256, and for anything smaller,
    # the cmap will map as a suitably discrete set of colours.
    Z = np.linspace(0, 1, 256).reshape(1, 256)

    ax.imshow(Z, extent=[xmin, xmax, ymin, ymax], cmap=name)
    ax.set_xlim(xmin, xmax), ax.set_xticks([])
    ax.set_ylim(ymin, ymax), ax.set_yticks([])

    fig.savefig(ROOT_DIR / f"figures/colormap-{name}.pdf")
    ax.clear()
