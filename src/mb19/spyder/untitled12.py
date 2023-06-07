import numpy as np
from matplotlib import pyplot as plt

k = 1.0
A = np.linspace(0, 10, num=100)  # [mM]
v = k * A

f, ax = plt.subplots(nrows=1, ncols=1)
f.suptitle("Mass Action Kinetics")
ax.plot(A, v)
ax.set_xlabel("Concentration A [mM]")
ax.set_ylabel("Rate v")
plt.show()

s