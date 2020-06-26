# -----------------------------------------------------------------------------
# Matplotlib cheat sheet
# Released under the BSD License
# -----------------------------------------------------------------------------
import time
import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

n = 10_000_000
np.random.seed(1)
X = np.random.uniform(0,1,n)
Y = np.random.uniform(0,1,n)

start = time.perf_counter() 
ax.plot(X, Y, marker="o", ls="")
end = time.perf_counter()
print(f"Time: {end-start}s")

ax.clear()

start = time.perf_counter() 
ax.scatter(X, Y)
end = time.perf_counter()
print(f"Time: {end-start}s")

ax.clear()

n = 1_000
np.random.seed(1)
X = []
for i in range(n):
    X.append(np.random.uniform(0,1,10))
#np.random.uniform(0,1,n)
# Y = np.random.uniform(0,1,n)

start = time.perf_counter()
# for i in range(0,n,2): plt.plot(X[i:i+2], Y[i:i+2])
for i in range(n): plt.plot(X[i])
end = time.perf_counter()
print(f"Time: {end-start}s")

ax.clear()

start = time.perf_counter()
ax.plot(sum([list(x)+[None] for x in X],[]))
# X0,Y0 = X[0::2], Y[0::2]
# X1,Y1 = X[1::2], Y[1::2]
# S = [None]*len(X)
# X = [v for t in zip(X0,X1,S) for v in t]
# Y = [v for t in zip(Y0,Y1,S) for v in t]
# plt.plot(X,Y)
end = time.perf_counter()
print(f"Time: {end-start}s")

