"""
========================
Visualizing named colors
========================
Simple plot example with the named colors and its visual representation.
"""
from __future__ import division
from itertools import groupby

import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from matplotlib import rcParams

colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
colors.update(mcolors.TABLEAU_COLORS)

# Add default color cycler colors C0 ... C9
std_cycle = {f'(C{i}⁺)': c for i, c in
             enumerate(rcParams['axes.prop_cycle'].by_key()['color'])}

colors.update(std_cycle)

# Sort colors by hue, saturation, value
by_hsv = sorted(((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                 for name, color in colors.items()), key=lambda x: x[0])


# Group color synonyms
def joiner(colornames):
    """Join colornames by comma and replace gray/grey duplicates by gr[ae]y."""
    return ', '.join([cn.replace('gray', 'gr[ae]y') for cn in colornames
                      if 'grey' not in cn]).replace(', (', ' (')


by_hsv = [(k, joiner([item[1] for item in g])) for k, g in
          groupby(by_hsv, key=lambda x: x[0])]

n = len(by_hsv)
ncols = 3
nrows = n // ncols + 1

fig, ax = plt.subplots(figsize=(4.5, 6))

# Get height and width
X, Y = fig.get_dpi() * fig.get_size_inches()
h = Y / (nrows + 1)
w = X / ncols

for i, (hsv, name) in enumerate(by_hsv):
    col = i // (nrows - 1)
    row = i % (nrows - 1)
    y = Y - (row * h) - h

    xi_line = w * (col + 0.05)
    xf_line = w * (col + 0.25)
    xi_text = w * (col + 0.3)

    ax.text(xi_text, y, name, fontsize=7,
            horizontalalignment='left',
            verticalalignment='center')

    ax.hlines(y + h * 0.1, xi_line, xf_line,
              color=mcolors.hsv_to_rgb(hsv), linewidth=(h * 0.6))

ax.set_xlim(0, X)
ax.set_ylim(0, Y)
ax.set_axis_off()

fig.subplots_adjust(left=0, right=1,
                    top=1, bottom=0.01,
                    hspace=0, wspace=0)
fig.text(0.5, 0.02, '⁺) C… represent the default color cycler values that can\
         be re-assigned', fontsize=7, ha='center', va='bottom')

plt.savefig("../figures/colornames.pdf")
# plt.show()
