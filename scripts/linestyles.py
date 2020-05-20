# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(4.25,2*.55))
ax = fig.add_axes([0,0,1,1], xlim=[0.75,10.25], ylim=[0.5,2.5], frameon=False,
                      xticks=[], yticks=[]) 
y = 2

def split(n_segment):
    width = 9
    segment_width = 0.75*(width/n_segment)
    segment_pad = (width - n_segment*segment_width)/(n_segment-1)
    X0 = 1+np.arange(n_segment)*(segment_width+segment_pad)
    X1 = X0 + segment_width
    return X0, X1


# Line style
# ----------------------------------------------------------------------------
X0, X1 = split(5)
styles = "-", ":", "--", "-.", (0,(0.01,2))

for x0,x1,style in zip(X0,X1,styles):
    ax.plot([x0,x1],[y,y], color="C1", linestyle=style,
            solid_capstyle="round", dash_capstyle="round", linewidth=3)
    if isinstance(style,str): text = '"%s"' % style
    else:                      text = '%s' % str(style)
    text = text.replace(' ','')
    ax.text((x0+x1)/2, y-0.2, text,
            size=10, ha="center", va="top", family="Source code pro")
ax.text(X0[0]-0.25, y+0.2, "linestyle or ls", family = "Source code pro",
        size=14, ha="left", va="baseline")
y -= 1 

# Dash capstyle
# ----------------------------------------------------------------------------
X0, X1 = split(3)
styles = "butt", "round", "projecting"
for x0,x1,style in zip(X0,X1,styles):
    ax.plot([x0,x1],[y,y], color="C1", dash_capstyle="projecting",
            linewidth=7, linestyle="--", alpha=.25)
    ax.plot([x0,x1],[y,y], color="C1", linewidth=7,
            linestyle="--", dash_capstyle=style)
    ax.text((x0+x1)/2, y-0.2, '"%s"' % style, family = "Source code pro",
            size=10, ha="center", va="top")
ax.text(X0[0]-0.25, y+0.2, "capstyle or dash_capstyle", family = "Source code pro",
        size=14, ha="left", va="baseline")


plt.savefig("../figures/linestyles.pdf", dpi=200)
# plt.show()
