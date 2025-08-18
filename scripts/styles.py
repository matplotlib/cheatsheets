# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import sys
import pathlib

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR / "fonts"))
import custom_fonts  # noqa


for style in ['default'] + plt.style.available:
    with plt.style.context(style):
        fig = plt.figure(figsize=(5, 3), dpi=100)
        ax = plt.subplot(1, 1, 1)
        X = np.linspace(0, 2*np.pi, 256)
        Y = np.cos(X)
        ax.plot(X, Y)
        plt.title(style, family="Source Serif Pro", size=32)
        plt.tight_layout()
        fig.savefig(ROOT_DIR / f"figures/style-{style}.pdf")
        plt.close(fig)
