from matplotlib import pyplot as plt
import numpy as np

#%%
# Warfarin
V = 10  # [l]
CL = 0.1  # [L/hr]
Dose = 100  # [mg]
Nt = 200
tend = 10*24
dt = tend/(Nt-1)
t = np.linspace(start=0, stop=tend, num=Nt)  # [hr]


#%%
# Dose dependency
f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5), dpi=300)


doses = np.linspace(0, 100, num=20)
aucs = np.zeros_like(doses)
for k, Dose in enumerate(doses):
    C = Dose / V * np.exp(-CL / V * t)  # [mg/l]
    auc = np.sum(dt * C)  # [hr] * [mg/l]
    aucs[k] = auc
    
    ax1.plot(t, C, label="__nolabel__")


ax2.plot(doses, aucs, '-o', color="black", label="AUC")

ax1.set_xlabel("time [hr]")
ax1.set_ylabel("concentration [mg/l]")
ax1.legend()
ax1.set_title("AUC Dose dependency")

ax2.set_xlabel("Dose [mg]")
ax2.set_ylabel("AUC [mg/l*hr]")
ax2.legend()
ax2.set_title("AUC Dose dependency")
plt.show()