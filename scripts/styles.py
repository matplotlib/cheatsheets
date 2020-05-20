# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

styles = ['default'] + plt.style.available

for style in styles:
    fig = plt.figure(figsize=(5,3), dpi=100)
    plt.style.use(style)
    ax = plt.subplot(1,1,1)
    X = np.linspace(0,2*np.pi, 256)
    Y = np.cos(X)
    ax.plot(X,Y)
    plt.title(style, family="Source Serif Pro", size=32)
    plt.tight_layout()
    # plt.show()
    plt.savefig("../figures/style-%s.pdf" % style)
    plt.close(fig)


