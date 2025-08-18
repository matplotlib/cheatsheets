"""
========================
Visualizing named colors
========================

Simple plot example with the named colors and its visual representation.
"""
import sys
import pathlib

import matplotlib as mpl
import matplotlib.pyplot as plt


ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR / "fonts"))
import custom_fonts  # noqa


mpl.style.use([
    ROOT_DIR / 'styles/base.mplstyle',
])
mpl.rc('figure.constrained_layout', h_pad=0, w_pad=0, hspace=0, wspace=0)

colors = dict(mpl.colors.BASE_COLORS, **mpl.colors.CSS4_COLORS)

# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mpl.colors.rgb_to_hsv(mpl.colors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]

n = len(sorted_names)
ncols = 3
nrows = n // ncols

fig, ax = plt.subplots(figsize=(4.5, 6))

# Get height and width
X, Y = fig.get_dpi() * fig.get_size_inches()
h = Y / (nrows + 1)
w = X / ncols

for i, name in enumerate(sorted_names):
    col = i // nrows
    row = i % nrows
    y = Y - (row * h) - h

    xi_line = w * (col + 0.05)
    xf_line = w * (col + 0.25)
    xi_text = w * (col + 0.3)

    ax.text(xi_text, y, name, fontsize=7,
            horizontalalignment='left',
            verticalalignment='center')

    ax.hlines(y + h * 0.1, xi_line, xf_line,
              color=colors[name], linewidth=(h * 0.6))

ax.set_xlim(0, X)
ax.set_ylim(0, Y)
ax.set_axis_off()

fig.savefig(ROOT_DIR / "figures/colornames.pdf")
