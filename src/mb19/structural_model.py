from matplotlib import pyplot as plt
import numpy as np

# Warfarin
V = 10  # [l]
CL = 0.1  # [L/hr]
Dose = 100  # [mg]
t = np.linspace(start=0, stop=10*24, num=200)  # [hr]
C = Dose/V * np.exp(-CL/V * t)  # [mg/l]

# plot
f, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5), dpi=300)
ax.plot(t/24.0, C, label="warfarin", color="black", linewidth=2.0)
ax.set_xlabel("time [day]")
ax.set_ylabel("warfarin [mg/l]")
ax.set_ylim(bottom=0)
ax.legend()
plt.show()

# --- Parameter scans ---

# Dose dependency
f, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5), dpi=300)
for Dose in np.linspace(0, 100, num=6):
    C = Dose / V * np.exp(-CL / V * t)  # [mg/l]
    ax.plot(t/24.0, C, label=f"{Dose} [mg]")
# reset dose
Dose = 100  # [mg]
ax.set_xlabel("time [day]")
ax.set_ylabel("warfarin [mg/l]")
ax.set_ylim(bottom=0)
ax.legend()
ax.set_title("Dose dependency")
plt.show()

# V dependency
f, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5), dpi=300)
for V in np.linspace(10, 100, num=5):
    C = Dose / V * np.exp(-CL / V * t)  # [mg/l]
    ax.plot(t/24.0, C, label=f"{V:.2f} [l]")
# reset volume
V = 10  # [mg]
ax.set_xlabel("time [day]")
ax.set_ylabel("warfarin [mg/l]")
ax.set_ylim(bottom=0)
ax.legend()
ax.set_title("Volume dependency")
plt.show()

# CL dependency
f, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5), dpi=300)
for CL in np.linspace(0.1, 3, num=5):
    C = Dose / V * np.exp(-CL / V * t)  # [mg/l]
    ax.plot(t/24.0, C, label=f"{CL:.2f} [l/hr]")

# reset clearance
CL = 0.1  # [L/hr]
ax.set_xlabel("time [day]")
ax.set_ylabel("warfarin [mg/l]")
ax.set_ylim(bottom=0)
ax.legend()
ax.set_title("Clearance dependency")
plt.show()