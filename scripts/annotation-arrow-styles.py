import pathlib

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


mpl.style.use([
    pathlib.Path(__file__).parent/'../styles/base.mplstyle',
    pathlib.Path(__file__).parent/'../styles/plotlet-grid.mplstyle',
])


(fig, axes) = plt.subplots(4, 4, figsize=(5.7/2.54, 1.5), frameon=True)
for ax in axes.flatten():
    ax.axis("off")
for i, (ax, style) in enumerate(zip(axes.flatten(), mpatches.ArrowStyle.get_styles())):
    x0, y0 = 0.8, 0.5
    x1, y1 = 0.2, 0.5
    ax.plot([x0, x1], [y0, y1], ".", color="0.25")
    ax.annotate("",
                xy=(x0, y0), xycoords='data',
                xytext=(x1, y1), textcoords='data',
                arrowprops=dict(arrowstyle=style,
                                mutation_scale=10,
                                color="black",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=0"))
    ax.text( (x1+x0)/2, y0-0.2, style,
             transform=ax.transAxes,
             ha="center", va="top", fontsize=8)

plt.savefig("../figures/annotation-arrow-styles.pdf")
