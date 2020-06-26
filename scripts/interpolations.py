import matplotlib.pyplot as plt
import numpy as np

methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

np.random.seed(1)
Z = np.random.uniform(0,1,(3,3))


fig, axs = plt.subplots(nrows=6, ncols=3, figsize=(4.5,9),
                        subplot_kw={'xticks': [], 'yticks': []})
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(Z, interpolation=interp_method, cmap='viridis',
              extent=[0,9,0,9])
    ax.text(4.5, 1, str(interp_method), weight="bold", color="white", size=12,
            transform=ax.transData, ha="center", va="center")

plt.tight_layout()
plt.savefig("../figures/interpolations.pdf", dpi=600)
plt.show()
