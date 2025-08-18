import sys
import pathlib

import numpy as np
import matplotlib.pyplot as plt


ROOT_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR / "fonts"))
import custom_fonts  # noqa


cmap = plt.get_cmap("Oranges")
color1, color2 = cmap(0.3), cmap(0.5)

plt.rcParams['hatch.color'] = color1
plt.rcParams['hatch.linewidth'] = 8

fig = plt.figure(figsize=(2, 2))
ax = plt.subplot()
np.random.seed(123)

x1, y1 = 3*np.arange(2), np.random.randint(25, 50, 2)
x2, y2 = x1+1, np.random.randint(25, 75, 2)

ax.bar(x1, y1, color=color2)
for x, y in zip(x1, y1):
    plt.annotate(f"{y:d}%", (x, y), xytext=(0, 1),
                 fontsize="x-small", color=color2,
                 textcoords="offset points", va="bottom", ha="center")

ax.bar(x2, y2, color=color2, hatch="/" )
for x, y in zip(x2, y2):
    plt.annotate(f"{y:d}%", (x, y), xytext=(0, 1),
                 fontsize="x-small", color=color2,
                 textcoords="offset points", va="bottom", ha="center")

ax.set_yticks([])
ax.set_xticks(0.5+np.arange(0, 6, 3))
ax.set_xticklabels(["2018", "2019"])
ax.tick_params('x', length=0, labelsize="small", which='major')

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.tight_layout()
fig.savefig(ROOT_DIR / "figures/tip-hatched.pdf")
# plt.show()
