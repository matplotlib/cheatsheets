import numpy as np
import matplotlib.pyplot as plt

cmap = plt.get_cmap("Oranges")
color1, color2 = cmap(0.3), cmap(0.5)

plt.rcParams['hatch.color'] = color1
plt.rcParams['hatch.linewidth'] = 8

fig = plt.figure(figsize=(2,2))
ax = plt.subplot()
np.random.seed(123)

x1,y1 = 3*np.arange(2), np.random.randint(25,50,2)
x2,y2 = x1+1,           np.random.randint(25,75,2)

ax.bar(x1, y1, color=color2)
for i in range(len(x1)):
    plt.annotate("%d%%" % y1[i],  (x1[i], y1[i]), xytext=(0,1),
                 fontsize="x-small", color=color2,
                 textcoords="offset points", va="bottom", ha="center")

ax.bar(x2, y2, color=color2, hatch="/" )
for i in range(len(x2)):
    plt.annotate("%d%%" % y2[i],  (x2[i], y2[i]), xytext=(0,1),
                 fontsize="x-small", color=color2,
                 textcoords="offset points", va="bottom", ha="center")
    
ax.set_yticks([])
ax.set_xticks(0.5+np.arange(0,6,3))
ax.set_xticklabels(["2018", "2019"])
ax.tick_params('x', length=0, labelsize="small", which='major')

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.tight_layout()
plt.savefig("../figures/tip-hatched.pdf")
# plt.show()
