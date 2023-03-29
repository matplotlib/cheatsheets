# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import pathlib

import numpy as np
import cartopy
import matplotlib as mpl
import matplotlib.pyplot as plt


ROOT_DIR = pathlib.Path(__file__).parent.parent

mpl.style.use([
    ROOT_DIR / 'styles/base.mplstyle',
    ROOT_DIR / 'styles/plotlet.mplstyle',
])

CARTOPY_SOURCE_TEMPLATE = 'https://naturalearth.s3.amazonaws.com/{resolution}_{category}/ne_{resolution}_{name}.zip'


# Configures cartopy to download NaturalEarth shapefiles from S3 instead of naciscdn
# Taken from https://github.com/SciTools/cartopy/issues/1325#issuecomment-904343657
target_path_template = cartopy.io.shapereader.NEShpDownloader.default_downloader().target_path_template
downloader = cartopy.io.shapereader.NEShpDownloader(url_template=CARTOPY_SOURCE_TEMPLATE,
                                                    target_path_template=target_path_template)
cartopy.config['downloaders'][('shapefiles', 'natural_earth')] = downloader


# Polar plot
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw={'projection': 'polar'})
T = np.linspace(0, 3*2*np.pi, 500)
R = np.linspace(0, 2, len(T))
ax.plot(T, R, color="C1")
ax.set_xticks(np.linspace(0, 2*np.pi, 2*8))
ax.set_xticklabels([])
ax.set_yticks(np.linspace(0, 2, 8))
ax.set_yticklabels([])
ax.set_ylim(0, 2)
ax.grid(linewidth=0.2)
fig.savefig(ROOT_DIR / "figures/projection-polar.pdf")
fig.clear()

# 3D plot
# -----------------------------------------------------------------------------
(fig, ax) = plt.subplots(subplot_kw={'projection': '3d'})
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
Z = ((R**2 - 1)**2)
X, Y = R*np.cos(P), R*np.sin(P)

# Plot the surface.
ax.plot_surface(X, Y, Z, color="C1", antialiased=False)
ax.set_zlim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
fig.savefig(ROOT_DIR / "figures/projection-3d.pdf")
fig.clear()

# Cartopy plot
# -----------------------------------------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(frameon=False,
                     projection=cartopy.crs.Orthographic())
ax.add_feature(cartopy.feature.LAND, zorder=0,
               facecolor="C1", edgecolor="0.0", linewidth=0)
fig.savefig(ROOT_DIR / "figures/projection-cartopy.pdf")
