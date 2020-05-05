# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


# Markers
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(3.5,1.5))
ax = fig.add_axes([0,0,1,1], frameon=False,
                  xlim=[0.5,10.5], ylim=[0.0,4.35], xticks=[], yticks=[])
X = np.linspace(1,10,12)
Y = np.arange(1,4)
X, Y = np.meshgrid(X,Y)
X ,Y = X.ravel(), Y.ravel()

plt.scatter(X, 1+Y, s=256, marker="s", fc="C1", ec="none", alpha=.25)
markers = [
    "$♠$", "$♣$", "$♥$","$♦$", "$→$","$←$","$↑$","$↓$", "$◐$","$◑$","$◒$","$◓$",
    "1", "2", "3", "4", "+", "x", "|", "_", 4, 5, 6, 7,
    ".", "o", "s", "P", "X", "*", "p", "D", "<", ">", "^", "v", ] 
for x,y,marker in zip(X,Y,markers):
    if   y == 3: fc = "white"
    elif y == 2: fc = "None"
    else:        fc = "C1"
    plt.scatter(x, 1+y, s=100, marker=marker, fc=fc, ec="C1", lw=0.5)

    if y == 1: marker = "\$%s\$" % marker
    if isinstance(marker,str): text = "'%s'" % marker
    else:                      text = '%s' % marker
    plt.text(x, 1+y-0.4, text,
              size="x-small", ha="center", va="top", family="Monospace")


# Spacing
n_segment = 4
width = 9
segment_width = 0.75*(width/n_segment)
segment_pad = (width - n_segment*segment_width)/(n_segment-1)
X0 =  1+np.arange(n_segment)*(segment_width+segment_pad)
marks = [ 10, [0,-1], (25, 5), [0,25,-1] ]
y = .6
for x0, mark in zip(X0,marks):
    X = np.linspace(x0, x0+segment_width, 50)
    Y = y*np.ones(len(X))    
    ax.plot(X, Y, linewidth=1, color="black",
            marker=".", mfc="white", mec="black", mew="1", markevery=mark)
    ax.text((X[0]+X[-1])/2, y-0.2, '%s' % str(mark),
            size="x-small", ha="center", va="top")

plt.text(.7, 1, "markevery",
         size="medium", ha="left", va="center", family="Source Code Pro")
plt.savefig("../figures/markers.pdf", dpi=600)

