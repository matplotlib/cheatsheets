# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import pathlib

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


mpl.style.use([
    pathlib.Path(__file__).parent/'../styles/base.mplstyle',
    pathlib.Path(__file__).parent/'../styles/ticks.mplstyle',
])


subplots_kw = dict(
    figsize=(5.7/2.54, 4/2.54),
    nrows=8,
    subplot_kw=dict(xlim=(0, 5), ylim=(0, 1)),
)

(fig, axs) = plt.subplots(**subplots_kw)

# Null Locator
ax = axs[0]
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.xaxis.set_minor_locator(ticker.NullLocator())
ax.text(0.0, 0.1, "ticker.NullLocator()",
        fontfamily='Source Code Pro', transform=ax.transAxes, in_layout=False)

# Multiple Locator
ax = axs[1]
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.text(0.0, 0.1, "ticker.MultipleLocator(0.5)",
        fontfamily='Source Code Pro', transform=ax.transAxes, in_layout=False)

# Fixed Locator
ax = axs[2]
majors = [0, 1, 5]
ax.xaxis.set_major_locator(ticker.FixedLocator(majors))
minors = np.linspace(0, 1, 11)[1:-1]
ax.xaxis.set_minor_locator(ticker.FixedLocator(minors))
ax.text(0.0, 0.1, "ticker.FixedLocator([0, 1, 5])",
        fontfamily='Source Code Pro', transform=ax.transAxes, in_layout=False)

# Linear Locator
ax = axs[3]
ax.xaxis.set_major_locator(ticker.LinearLocator(3))
ax.xaxis.set_minor_locator(ticker.LinearLocator(31))
ax.text(0.0, 0.1, "ticker.LinearLocator(numticks=3)",
        fontfamily='Source Code Pro', transform=ax.transAxes, in_layout=False)

# Index Locator
ax = axs[4]
ax.plot(range(0, 5), [0]*5, color='white')
ax.xaxis.set_major_locator(ticker.IndexLocator(base=.5, offset=.25))
ax.text(0.0, 0.1, "ticker.IndexLocator(base=0.5, offset=0.25)",
        fontfamily='Source Code Pro', transform=ax.transAxes, in_layout=False)

# Auto Locator
ax = axs[5]
ax.xaxis.set_major_locator(ticker.AutoLocator())
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.text(0.0, 0.1, "ticker.AutoLocator()",
        fontfamily='Source Code Pro', transform=ax.transAxes, in_layout=False)

# MaxN Locator
ax = axs[6]
ax.xaxis.set_major_locator(ticker.MaxNLocator(4))
ax.xaxis.set_minor_locator(ticker.MaxNLocator(40))
ax.text(0.0, 0.1, "ticker.MaxNLocator(n=4)",
        fontfamily='Source Code Pro', transform=ax.transAxes, in_layout=False)

# Log Locator
ax = axs[7]
ax.set_xlim(10**3, 10**10)
ax.set_xscale('log')
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=15))
ax.text(0.0, 0.1, "ticker.LogLocator(base=10, numticks=15)",
        fontfamily='Source Code Pro', transform=ax.transAxes, in_layout=False)

plt.savefig("../figures/tick-locators.pdf")
