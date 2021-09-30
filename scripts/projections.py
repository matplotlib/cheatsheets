# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import numpy as np
import cartopy
import matplotlib as mpl
import matplotlib.pyplot as plt


CARTOPY_SOURCE_TEMPLATE = 'https://naturalearth.s3.amazonaws.com/{resolution}_{category}/ne_{resolution}_{name}.zip'


# Configures cartopy to download NaturalEarth shapefiles from S3 instead of naciscdn
# Taken from https://github.com/SciTools/cartopy/issues/1325#issuecomment-904343657
target_path_template = cartopy.io.shapereader.NEShpDownloader.default_downloader().target_path_template
downloader = cartopy.io.shapereader.NEShpDownloader(url_template=CARTOPY_SOURCE_TEMPLATE,
                                target_path_template=target_path_template)
cartopy.config['downloaders'][('shapefiles', 'natural_earth')] = downloader


# Polar plot
# -----------------------------------------------------------------------------
mpl.rc('axes', linewidth=4.0)
fig = plt.figure(figsize=(4,4))
b = 0.025
ax = fig.add_axes([b,b,1-2*b,1-2*b], projection="polar")
T = np.linspace(0, 3*2*np.pi, 500)
R = np.linspace(0, 2, len(T))
ax.plot(T, R, color="C1", linewidth=6)
ax.set_xticks(np.linspace(0, 2*np.pi, 2*8))
ax.set_xticklabels([])
ax.set_yticks(np.linspace(0, 2, 8))
ax.set_yticklabels([])
ax.set_ylim(0,2)
ax.grid(linewidth=1)
plt.savefig("../figures/projection-polar.pdf")
fig.clear()

# 3D plot
# -----------------------------------------------------------------------------
mpl.rc('axes', linewidth=2.0)
ax = fig.add_axes([0,.1,1,.9], projection="3d")
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
plt.savefig("../figures/projection-3d.pdf")
fig.clear()

# Cartopy plot
# -----------------------------------------------------------------------------
mpl.rc('axes', linewidth=3.0)
b = 0.025
ax = fig.add_axes([b,b,1-2*b,1-2*b], frameon=False,
                  projection=cartopy.crs.Orthographic())
ax.add_feature(cartopy.feature.LAND, zorder=0,
               facecolor="C1", edgecolor="0.0", linewidth=0)
plt.savefig("../figures/projection-cartopy.pdf")
