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


# fig = plt.figure(figsize=(7,1.5))
# plt.plot(X, Y, "C1", lw=2)
# plt.fill_betweenx([-1.5,1.5],[0],[2*np.pi], color=".9")
# plt.text(0, -1, r" Period $\Phi$")
# # plt.xticks([]), plt.yticks([])
# plt.ylim(-1.5, 1.5)
# plt.tight_layout()
# plt.savefig("../figures/sine-period.pdf", dpi=100)
# plt.show()


# fig = plt.figure(figsize=(7,1.5))
# plt.plot(X, np.sin(X), "C0", lw=2, label="Sine")
# plt.plot(X, np.cos(X), "C1", lw=2, label="Cosine")
# plt.legend(bbox_to_anchor = (0.0, .9, 1.02, 0.1),
#            frameon=False, mode="expand", ncol=2, loc="lower left")
# plt.title("Sine and Cosine")
# plt.xticks([]), plt.yticks([])
# plt.ylim(-1.25, 1.25)
# plt.tight_layout()
# plt.savefig("../figures/sine-legend.pdf", dpi=100)
# plt.show()


fig = plt.figure(figsize=(7,1.5))
X = np.linspace(0, 10*np.pi, 1000)
Y = np.sin(X)
plt.plot(X, Y, "C1o-", markevery=50,  mec="1.0", lw=2, ms=8.5, mew=2)
# plt.xticks([]), plt.yticks([])
plt.ylim(-1.5, 1.5)
plt.annotate(" ", (X[200],Y[200]), (X[250], -1), ha="center", va="center",
             arrowprops = {"arrowstyle" : "->", "color": "C1"})
plt.annotate("A", (X[250],Y[250]), (X[250], -1), ha="center", va="center",
             arrowprops = {"arrowstyle" : "->", "color": "C1"})
plt.annotate(" ", (X[300],Y[300]), (X[250], -1), ha="center", va="center",
             arrowprops = {"arrowstyle" : "->", "color": "C1"})
plt.tight_layout()
plt.savefig("../figures/sine-annotate.pdf", dpi=100)
# plt.show()
