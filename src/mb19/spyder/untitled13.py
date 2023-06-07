import numpy as np
from matplotlib import pyplot as plt



kms = np.linspace(0.1, 10.0, num=10)
A = np.linspace(0, 10, num=100)  # [mM]

f, ax = plt.subplots(nrows=1, ncols=1)
f.suptitle("Michaelis Menten Kinetics")
Vmax = 1.0
for Km in kms:
    v = Vmax * A/(Km + A)
    ax.plot(A, v, label=f"{Km=:.2f}")
    
ax.set_xlabel("Km [mM]")
ax.set_ylabel("Rate v")
ax.legend()
plt.show()

# dependency of Vmax
Km = 1.0
Vmaxs = np.linspace(0.1, 10.0, num=10)
A = np.linspace(0, 10, num=100)  # [mM]

f, ax = plt.subplots(nrows=1, ncols=1)
f.suptitle("Michaelis Menten Kinetics")
Vmax = 1.0
for Vmax in Vmaxs:
    v = Vmax * A/(Km + A)
    ax.plot(A, v, label=f"{Vmax=:.2f}")
    
ax.set_xlabel("Vmax")
ax.set_ylabel("Rate v")
ax.legend()
plt.show()



# dependency of n
ns = np.linspace(1, 10, num=10)
Km = 5.0
Vmaxs = 1.0

A = np.linspace(0, 10, num=100)  # [mM]

f, ax = plt.subplots(nrows=1, ncols=1)
f.suptitle("Hill Kinetics")
for n in ns:
    v = Vmax * A**n/(Km**n + A**n)
    ax.plot(A, v, label=f"{n:.2f}")
    
ax.set_xlabel("n Hill coeffient")
ax.set_ylabel("Rate v")
ax.legend()
plt.show()