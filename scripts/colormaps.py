import numpy as np
import matplotlib.pyplot as plt


figsize = 4.0, 0.25
fig = plt.figure(figsize=figsize)
ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)
ymin, ymax=  0, 1
xmin, xmax = 0, figsize[0]/figsize[1]

# Uniform colormaps
# -----------------------------------------------------------------------------
cmaps = ('viridis', 'plasma', 'inferno', 'magma', 'cividis',
         
         'PRGn', 'PiYG', 'RdYlGn', 'BrBG', 'RdGy', 'PuOr', 'RdBu',
         'RdYlBu',  'Spectral', 'coolwarm', 'bwr', 'seismic',

         'tab10', 'tab20', 'tab20b', 'tab20c',
         'Pastel1', 'Pastel2', 'Paired',
         'Set1', 'Set2', 'Set3', 'Accent', 'Dark2',

         'Greys', 'Reds','Oranges', 'YlOrBr', 'YlOrRd', 'OrRd',
         'PuRd', 'RdPu', 'BuPu', 'Purples', 'YlGnBu', 'Blues',
         'PuBu', 'GnBu', 'PuBuGn', 'BuGn','Greens', 'YlGn',

         'bone', 'gray', 'pink', 'afmhot', 'hot', 'gist_heat', 'copper', 
         'Wistia', 'autumn', 'summer', 'spring', 'cool', 'winter',

         'twilight', 'twilight_shifted', 'hsv',

         'terrain', 'ocean', 'gist_earth', 'cubehelix', 'rainbow'
)

for cmap in cmaps:
    n = 512

    if cmap in ['tab10']: n = 10
    if cmap in ['tab20', 'tab20b', 'tab20c']: n = 20
    if cmap in ['Pastel1', 'Set1']: n = 9
    if cmap in ['Pastel2', 'Accent', 'Dark2', 'Set2']: n = 8
    if cmap in ['Set3']: n = 12
    if cmap in ['Greys']: n = 11
    Z = np.linspace(0,1,n).reshape(1,n)
        
    ax.imshow(Z, extent=[xmin, xmax, ymin, ymax], cmap=plt.get_cmap(cmap))
    ax.set_xlim(xmin, xmax), ax.set_xticks([])
    ax.set_ylim(ymin, ymax), ax.set_yticks([])

    """
    if cmap == "tab10":
        x = np.linspace(xmin, xmax, 11, endpoint=True) + 0.5*(xmax-xmin)/11
        for i in range(10):
            ax.text(x[i], (ymin+ymax)/2, "C%d"%i, color="white", zorder=10,
                    family = "Source Pro Serif", size=10, ha="center", va="center")

    if cmap == "Greys":
        x = np.linspace(xmin, xmax, 12, endpoint=True) + 0.5*(xmax-xmin)/12
        for i in range(11):
            color = "%.1f"%(i/10)
            text = "%.1f"%(1-i/10)
            ax.text(x[i], (ymin+ymax)/2, text, color=color, zorder=10,
                    family = "Source Pro Serif", size=10, ha="center", va="center")
    """
    
    plt.savefig("../figures/colormap-%s.pdf" % cmap)
    ax.clear()
