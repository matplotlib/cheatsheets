import matplotlib.pyplot as plt

def demo_con_style(ax, connectionstyle):
    x1, y1 = 0.3, 0.2
    x2, y2 = 0.8, 0.6
    ax.plot([x1, x2], [y1, y2], ".")
    ax.annotate("",
                xy=(x1, y1), xycoords='data',
                xytext=(x2, y2), textcoords='data',
                arrowprops=dict(arrowstyle="->", color="0.5",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle=connectionstyle),
                )
    ax.text(.05, .95, connectionstyle.replace(",", ",\n"),
            family="Source Code Pro",
            transform=ax.transAxes, ha="left", va="top", size="x-small")

fig, axs = plt.subplots(3, 3, figsize=(5, 5))
demo_con_style(axs[0, 0], "arc3,rad=0")
demo_con_style(axs[0, 1], "arc3,rad=0.3")
demo_con_style(axs[0, 2], "angle3,angleA=0,angleB=90")
demo_con_style(axs[1, 0], "angle,angleA=-90,angleB=180,rad=0")
demo_con_style(axs[1, 1], "angle,angleA=-90,angleB=180,rad=25")
demo_con_style(axs[1, 2], "arc,angleA=-90,angleB=0,armA=0,armB=40,rad=0")
demo_con_style(axs[2, 0], "bar,fraction=0.3")
demo_con_style(axs[2, 1], "bar,fraction=-0.3")
demo_con_style(axs[2, 2], "bar,angle=180,fraction=-0.2")

for ax in axs.flat:
    ax.set(xlim=(0, 1), ylim=(0, 1), xticks=[], yticks=[], aspect=1)
fig.tight_layout(pad=0.2)

plt.savefig("../figures/annotation-connection-styles.pdf")
# plt.show()
