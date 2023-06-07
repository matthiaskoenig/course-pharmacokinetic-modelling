import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

def dxdt_absorption_chain(x, t, ka, ke):
    """
    First order absorption model for transit chain.
    """
    # state variables
    A_tablet = x[0]  # [mg]
    A_central = x[1] # [mg/l]
    A_urine = x[2] # [mg]
    A1 = x[3]
    A2 = x[4]
    A3 = x[5]
    A4 = x[6]
    
    # rates
    va = ka * A_tablet  # [mg/hr]
    ve = ke * A_central # [mg/hr]
    v1 = ka * x[3]
    v2 = ka * x[4]
    v3 = ka * x[5]
    v4 = ka * x[6]

    # odes (stoichiometric equation)
    dxdt = np.zeros(7)
    
    dxdt[0] = -va            # dA_tablet/dt  [mg/hr]
    dxdt[1] =  v4 - ve     # dA_central/dt [mg/hr] (end of chain)
    dxdt[2] =  ve            # dA_urine/dt  [mg/hr]
    dxdt[3] = va - v1        # A1
    dxdt[4] = v1 - v2        # A2
    dxdt[5] = v2 - v3
    dxdt[6] = v3 - v4
        
    return dxdt

# initial condition and time span
t = np.arange(0, 10, 0.05) # [hr]
Dose_A = 10.0  # [mg]
x0 = [
    Dose_A,  # A_tablet  [mg]
    0.0,   # A_central [mg]
    0.0,   # A_urine [mg]
    0.0,   # A1 [mg]
    0.0,   # A2 [mg]
    0.0,   # A3 [mg]
    0.0,   # A4 [mg]
]

names = ["A_tablet", "A_central", "A_urine"]
colors = ["black", "tab:blue", "tab:orange"]

# parameters
ka = 2.0  # [1/hr]
ke = 5.0  # [1/hr]

n_samples = 5
kas = np.linspace(0.1, 2.0, num=n_samples)  # [1/hr]

# plot results
f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
f.suptitle("Absorption chain model")

for kp, ka in enumerate(kas):
    x = odeint(dxdt_absorption_chain, x0, t, args=(ka, ke))
    
    # all species
    for k, name in enumerate(names):
        ax1.plot(t, x[:, k], linewidth=2, color=colors[k], alpha=(kp+1)/n_samples, label=f"{ka=}")

    # only A_central
    ax2.plot(t, x[:, 1], linewidth=2, color=colors[1], alpha=(kp+1)/n_samples, label=f"{ka=}")

    for ax in (ax1, ax2):
        ax.set_xlabel("time [hr]")
        ax.set_ylabel("amount [mg]")
    ax2.legend()

plt.show()