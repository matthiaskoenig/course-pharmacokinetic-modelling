from matplotlib import pyplot as plt
import numpy as np

# Warfarin
V = 10  # [l]
CL = 80  # [L/hr]
Dose = 100  # [mg]
t = np.linspace(start=0, stop=6, num=200)  # [hr]
C = Dose/V * np.exp(-CL/V * t)  # [mg/l]

# plot
f, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(t, C, label="aspirin", color="black", linewidth=2.0)
ax.set_xlabel("time [hour]")
ax.set_ylabel("aspirin [mg/l]")
ax.set_ylim(bottom=0)
ax.legend()
plt.show()
