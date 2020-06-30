import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['axes.linewidth'] = 1.5


fig = plt.figure(figsize=(2,2))
d = 0.01
ax1 = fig.add_axes([d,d,1-2*d,1-2*d], label="cartesian")
ax2 = fig.add_axes([d,d,1-2*d,1-2*d], projection="polar", label="polar")

ax1.set_xticks([]) #np.linspace(0.0, 0.4, 5))
ax1.set_yticks([]) #np.linspace(0.0, 1.0, 11))

ax2.set_rorigin(0)
ax2.set_thetamax(90)
ax2.set_ylim(0.5,1.0)
ax2.set_xticks(np.linspace(0, np.pi/2, 10))
ax2.set_yticks(np.linspace(0.5, 1.0, 5))

ax2.set_xticklabels([])
ax2.set_yticklabels([])

plt.savefig("../figures/tip-dual-axis.pdf")
plt.show()
