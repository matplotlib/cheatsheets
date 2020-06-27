# ----------------------------------------------------------------------------
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 10*np.pi, 1000)
Y = np.sin(X)

plt.figure = plt.figure(figsize=(8,2))
plt.plot(X, Y, color="orange", linewidth=2)
# plt.xticks([]), plt.yticks([])
# plt.tight_layout()
plt.savefig("../figures/sine.pdf", dpi=100)
plt.show()
