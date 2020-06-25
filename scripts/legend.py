# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(4,4))
ax = fig.add_axes([0.15,0.15,.7,.7], frameon=True, aspect=1,
                  xticks=[], yticks=[])

def text(x, y, _text):
    color= "C1"
    if not 0 < x < 1 or not 0 < y < 1:  color = "C0"
    size = 0.15
    ax.text(x, y, _text, color="white", #bbox={"color": "C1"},
            size="xx-large", weight="bold", ha="center", va="center")
    rect = plt.Rectangle((x-size/2, y-size/2), size, size, facecolor=color,
                         zorder=-10, clip_on=False)
    ax.add_patch(rect)

def point(x, y):
    ax.scatter([x], [y], facecolor="C0", edgecolor="white",
               zorder=10, clip_on=False)

d = .1
e = .15/2

text(  d,   d, "1"), text( 0.5,   d, "2"), text(1-d,   d, "3")
text(  d, 0.5, "4"), text( 0.5, 0.5, "5"), text(1-d, 0.5, "6")
text(  d, 1-d, "7"), text( 0.5, 1-d, "8"), text(1-d, 1-d, "9")

text( -d, 1-d, "A"), text( -d, 0.5, "B"), text(  -d,   d, "C")
point(-d+e, 1-d+e), point(-d+e, 0.5), point(-d+e, d-e),

text(  d,  -d, "D"), text(0.5,  -d, "E"), text( 1-d,  -d, "F")
point(d-e, -d+e), point(0.5, -d+e), point(1-d+e, -d+e),

text(1+d,   d, "G"), text(1+d, 0.5, "H"), text( 1+d, 1-d, "I")
point(1+d-e, d-e), point(1+d-e, .5), point(1+d-e, 1-d+e),

text(1-d, 1+d, "J"), text(0.5, 1+d, "K"), text(   d, 1+d, "L")
point(1-d+e, 1+d-e), point(0.5, 1+d-e), point(d-e, 1+d-e),

plt.xlim(0,1), plt.ylim(0,1)

plt.savefig("../figures/legend-placement.pdf")
# plt.show()
