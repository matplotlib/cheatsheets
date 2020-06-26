import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

styles = mpatches.ArrowStyle.get_styles()
def demo_con_style(ax, connectionstyle):
    ax.text(.05, .95, connectionstyle.replace(",", ",\n"),
            family="Source Code Pro",
            transform=ax.transAxes, ha="left", va="top", size="x-small")

fig, ax = plt.subplots(figsize=(4, 2.5), frameon=False)
ax.axis("off")
for i,style in enumerate(mpatches.ArrowStyle.get_styles()):
    x0, y0 = 5 + 5*(i%3), -(i//3)
    x1, y1 = 1 + 5*(i%3), -(i//3)
    ax.plot([x0, x1], [y0, y1], ".", color="0.25")
    ax.annotate("",
                xy=(x0, y0), xycoords='data',
                xytext=(x1, y1), textcoords='data',
                arrowprops=dict(arrowstyle=style,
                                color="black",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=0"))
    ax.text( (x1+x0)/2, y0-0.2, style,
             family = "Source Code Pro", ha="center", va="top")

plt.savefig("../figures/annotation-arrow-styles.pdf")
# plt.show()
