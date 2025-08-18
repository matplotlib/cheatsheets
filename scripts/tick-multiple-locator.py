# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import sys
import pathlib

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR / "fonts"))
import custom_fonts  # noqa

mpl.style.use([
    ROOT_DIR / 'styles/base.mplstyle',
    ROOT_DIR / 'styles/ticks.mplstyle',
])


subplots_kw = dict(
    figsize=(5.7/2.54, 0.4/2.54),
    subplot_kw=dict(xlim=(0, 5), ylim=(0, 1)),
)

(fig, ax) = plt.subplots(**subplots_kw)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
ax.xaxis.set_minor_formatter(ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=5)
ax.tick_params(axis='x', which='minor', rotation=90)

fig.savefig(ROOT_DIR / "figures/tick-multiple-locator.pdf", transparent=True)
