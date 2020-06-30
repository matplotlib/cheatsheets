# ----------------------------------------------------------------------------
# Title:   Scientific Visualisation - Python & Matplotlib
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Setup a plot such that only the bottom spine is shown
def setup(ax):
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines['top'].set_color('none')

    ax.spines['bottom'].set_position("center")
    
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00)
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', width=0.75)
    ax.tick_params(which='minor', length=2.5)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.patch.set_alpha(0.0)


fig = plt.figure(figsize=(5, .5))
fig.patch.set_alpha(0.0)
n = 1

fontsize = 18
ax = plt.subplot(n, 1, 1)
ax.tick_params(axis='both', which='minor', labelsize=6)
setup(ax)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
ax.xaxis.set_minor_formatter(ticker.ScalarFormatter())
ax.tick_params(axis='x', which='minor', rotation=0)

for tick in ax.get_xticklabels(which='both'):
    tick.set_fontname("Roboto Condensed")
    
plt.tight_layout()
plt.savefig("../figures/tip-font-family.pdf", transparent=True)
# plt.show()
