# ----------------------------------------------------------------------------
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0.1, 10*np.pi, 10000)
Y = np.sin(X)

# fig = plt.figure(figsize=(8,2))
# plt.plot(X, Y, color="orange", linewidth=2)
# plt.xticks([]), plt.yticks([])
# plt.tight_layout()
# plt.savefig("../figures/sine.pdf", dpi=100)

# fig = plt.figure(figsize=(7,1.5))
# plt.plot(X, Y, "C1o:", markevery=500,  mec="1.0", lw=2, ms=8.5, mew=2)
# # plt.xticks([]), plt.yticks([])
# plt.ylim(-1.5, 1.5)
# plt.tight_layout()
# plt.savefig("../figures/sine-marker.pdf", dpi=100)

# fig, ax = plt.subplots(figsize=(7,1.5))
# ax.set_xscale("log")
# ax.plot(X, Y, "-")
# plt.plot(X, Y, "C1o-", markevery=500,  mec="1.0", lw=2, ms=8.5, mew=2)
# #plt.xticks([]), plt.yticks([])
# plt.ylim(-1.5, 1.5)
# plt.tight_layout()
# plt.savefig("../figures/sine-logscale.pdf", dpi=100)


fig = plt.figure(figsize=(7,1.5))
plt.plot(X, Y, "C1", lw=2)
plt.fill_betweenx([-1.5,1.5],[0],[2*np.pi], color=".9")
plt.text(0, -1, r" Period $\Phi$")
# plt.xticks([]), plt.yticks([])
plt.ylim(-1.5, 1.5)
plt.tight_layout()
plt.savefig("../figures/sine-period.pdf", dpi=100)
plt.show()

# X = np.linspace(0, 2*np.pi, 10000)
# Y = np.sin(10*X)

# fig = plt.figure(figsize=(3,3))
# ax = plt.subplot(projection="polar")
# ax.set_rorigin(-3)
# ax.set_xticks(np.linspace(0, 2*np.pi, 8+1 ))
# ax.set_xticklabels([])
# ax.set_yticklabels([])
# plt.ylim(-1.5, 1.5)
# plt.plot(X, Y, "C1")
# plt.savefig("../figures/sine-polar.pdf", dpi=100)
# plt.show()
