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
    figsize=(5.7/2.54, 3.5/2.54),
    nrows=7,
    subplot_kw=dict(xlim=(0, 5), ylim=(0, 1))
)

(fig, axs) = plt.subplots(**subplots_kw)

# Null formatter
ax = axs[0]
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(ticker.NullFormatter())
ax.text(0.0, 0.1, "ticker.NullFormatter()",
        fontfamily="Source Code Pro", transform=ax.transAxes, in_layout=False)

# Fixed formatter
ax = axs[1]
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax.xaxis.set_major_locator(ticker.FixedLocator(range(6)))
majors = ["zero", "one", "two", "three", "four", "five"]
ax.xaxis.set_major_formatter(ticker.FixedFormatter(majors))
ax.text(0.0, 0.1, "ticker.FixedFormatter(['zero', 'one', 'two', …])",
        fontfamily="Source Code Pro", transform=ax.transAxes, in_layout=False)

# FuncFormatter formatter
ax = axs[2]
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: "[%.2f]" % x))
ax.text(0.0, 0.1, 'ticker.FuncFormatter(lambda x, pos: "[%.2f]" % x)',
        fontfamily="Source Code Pro", transform=ax.transAxes, in_layout=False)

# FormatStr formatter
ax = axs[3]
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter(">%d<"))
ax.text(0.0, 0.1, "ticker.FormatStrFormatter('>%d<')",
        fontfamily="Source Code Pro", transform=ax.transAxes, in_layout=False)

# Scalar formatter
ax = axs[4]
ax.xaxis.set_major_locator(ticker.AutoLocator())
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
ax.text(0.0, 0.1, "ticker.ScalarFormatter()",
        fontfamily="Source Code Pro", transform=ax.transAxes, in_layout=False)

# StrMethod formatter
ax = axs[5]
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x}"))
ax.text(0.0, 0.1, "ticker.StrMethodFormatter('{x}')",
        fontfamily="Source Code Pro", transform=ax.transAxes, in_layout=False)

# Percent formatter
ax = axs[6]
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=5))
ax.text(0.0, 0.1, "ticker.PercentFormatter(xmax=5)",
        fontfamily="Source Code Pro", transform=ax.transAxes, in_layout=False)

plt.savefig("../figures/tick-formatters.pdf")
