import numpy as np
from scipy.integrate import odeint
from matplotlib import pylab as plt

def dxdt_absorption_lag(x, t, ka, ke, lag=0.0):
    """
    First order absorption model with lag time
    """
    # state variables
    A_tablet = x[0]  # [mg]
    A_central = x[1] # [mg/l]
    A_urine = x[2] # [mg]
    
    # rates
    if t >= lag:
        va = ka * A_tablet  # [mg/hr]
    else:
        va = 0
    ve = ke * A_central # [mg/hr]

    # odes (stoichiometric equation)    
    return [
        -va,            # dA_tablet/dt  [mg/hr]
         va - ve,       # dA_central/dt [mg/hr]
         ve,            # dA_urine/dt  [mg/hr]
    ] 

# initial condition and time span
t = np.arange(0, 10, 0.05) # [hr]
Dose_A = 10.0  # [mg]
x0 = [
    Dose_A,  # A_tablet  [mg]
    0.0,   # A_central [mg]
    0.0,   # A_urine [mg]
]
names = ["A_tablet", "A_central", "A_urine"]
colors = ["black", "tab:blue", "tab:orange"]

ka = 2.0  # [1/hr]
ke = 5.0  # [1/hr]

n_samples = 5
lags = np.linspace(0.0, 2.0, num=n_samples)  # [hr]

# plot results
f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
f.suptitle("Lag absorption model")

for kp, lag in enumerate(lags):
    x = odeint(dxdt_absorption_lag, x0, t, args=(ka, ke, lag))
    
    # all species
    for k, name in enumerate(names):
        ax1.plot(t, x[:, k], linewidth=2, color=colors[k], alpha=(kp+1)/n_samples, label=f"{lag=}")

    # only A_central
    ax2.plot(t, x[:, 1], linewidth=2, color=colors[1], alpha=(kp+1)/n_samples, label=f"{lag=}")

    for ax in (ax1, ax2):

        ax.set_xlabel("time [hr]")
        ax.set_ylabel("amount [mg]")
    ax2.legend()

plt.show()