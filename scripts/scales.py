import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(0.4,2/3*0.4))
ax = fig.add_axes([0,0,1,1], frameon=False)
ax.tick_params(axis='both', which='both', length=0)
ax.set_xlim(-2,2)
X = np.linspace(-2,+2,1001)
Y = np.sin(X*2.5*2*np.pi)


# Linear scale
# -----------------------------------------------------------------------------
ax.set_xlim(X.min(), X.max())
ax.set_xscale("linear")
ax.plot(X, Y, color="C1", linewidth=0.75)
ax.set_ylim(-2.5,1.5)
ax.text(0, 0.12, "-∞", ha="left", va="bottom", size=3, transform=ax.transAxes)
ax.text(0, 0.15, "⇤",  ha="left", va="top", size=4, transform=ax.transAxes)
ax.text(1, 0.12, "+∞", ha="right", va="bottom", size=3, transform=ax.transAxes)
ax.text(1, 0.15, "⇥",  ha="right", va="top", size=4, transform=ax.transAxes)
plt.savefig("../figures/scale-linear.pdf")
ax.clear()

# Log scale
# -----------------------------------------------------------------------------
ax.set_xscale("log", basex=10)
ax.plot(X, Y, color="C1", linewidth=0.75)
ax.set_ylim(-2.5,1.5)
ax.text(0, 0.12, "0", ha="left", va="bottom", size=3, transform=ax.transAxes)
ax.text(0, 0.15, "⇤",  ha="left", va="top", size=4, transform=ax.transAxes)
ax.text(1, 0.12, "+∞", ha="right", va="bottom", size=3, transform=ax.transAxes)
ax.text(1, 0.15, "⇥",  ha="right", va="top", size=4, transform=ax.transAxes)
plt.savefig("../figures/scale-log.pdf")
ax.clear()

# Symlog scale
# -----------------------------------------------------------------------------
ax.set_xscale("symlog", basex=10, linthreshx=1)
ax.plot(X, Y, color="C1", linewidth=0.75)
ax.set_ylim(-2.5,1.5)
ax.text(0, 0.12, "-∞", ha="left", va="bottom", size=3, transform=ax.transAxes)
ax.text(0, 0.15, "⇤",  ha="left", va="top", size=4, transform=ax.transAxes)
ax.text(1, 0.12, "+∞", ha="right", va="bottom", size=3, transform=ax.transAxes)
ax.text(1, 0.15, "⇥",  ha="right", va="top", size=4, transform=ax.transAxes)
plt.savefig("../figures/scale-symlog.pdf")
ax.clear()

# Symlog scale
# -----------------------------------------------------------------------------
ax.set_xscale("logit")
ax.plot(X, Y, color="C1", linewidth=0.75)
ax.set_ylim(-2.5,1.5)
ax.text(0, 0.12, "0", ha="left", va="bottom", size=3, transform=ax.transAxes)
ax.text(0, 0.15, "⇤",  ha="left", va="top", size=4, transform=ax.transAxes)
ax.text(1, 0.12, "1", ha="right", va="bottom", size=3, transform=ax.transAxes)
ax.text(1, 0.15, "⇥",  ha="right", va="top", size=4, transform=ax.transAxes)
plt.savefig("../figures/scale-logit.pdf")
ax.clear()

