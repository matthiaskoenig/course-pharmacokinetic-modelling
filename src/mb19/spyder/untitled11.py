import numpy as np
from scipy.integrate import odeint
from matplotlib import pylab as plt
import pandas as pd

def dxdt_absorption_first_order(x, t, ka, ke):
    """
    First order absorption model
    """
    # state variables
    A_tablet = x[0]  # [mg]
    A_central = x[1] # [mg/l]
    A_urine = x[2] # [mg]
    
    # rates
    va = ka * A_tablet  # [mg/hr]
    ve = ke * A_central # [mg/hr]

    # odes (stoichiometric equation)    
    return [
        -va,            # dA_tablet/dt  [mg/hr]
         va - ve,       # dA_central/dt [mg/hr]
         ve,            # dA_urine/dt  [mg/hr]
    ] 


def simulate_multi_dosing(Dose_A, ka, ke):
    """Helper function to run the multiple dosing simulation."""

    # initial condition
    names = ["A_tablet", "A_central", "A_urine"]
    x0 = [
        Dose_A,  # A_tablet  [mg]
        0.0,   # A_central [mg]
        0.0,   # A_urine [mg]
    ]

    # time span for single dose
    t = np.linspace(0, 24, num=100) # [hr]

    # multiple dose simulation
    n_doses = 40  # [hr]
    
    dfs = []
    for k in range(n_doses):
        if k == 0:
            x0[0] = 6
            tvec = t.copy()
        elif k > 0:
            x0 = x[-1, :]
            x0[0] = x0[0] + Dose_A
            tvec = t.copy() + tvec[-1]

        x = odeint(dxdt_absorption_first_order, x0, tvec, args=(ka, ke))
        df = pd.DataFrame(x, columns=names)
        df["time"] = tvec
        dfs.append(df)

    df_all = pd.concat(dfs)
    return df_all

# run simulation and plot results

colors = ["black", "tab:blue", "tab:orange"]
names = ["A_tablet", "A_central", "A_urine"]
# plot results

# run simulation and plot results
Dose_A = 0.75  # [mg]
ka = 0.01  # [1/hr]
ke = 0.01 # [1/hr]

# Dose_A = 5.0  # [mg]
# ka = 1.0  # [1/hr]
# ke = 1.0  # [1/hr]

# Dose_A = 4.32
# ka = 0.09  # [1/hr]
# ke = 0.05  # [1/hr]

df = simulate_multi_dosing(Dose_A, ka, ke)

f, ax = plt.subplots(nrows=1, ncols=1)
f.suptitle("Therapheutic window")

ax.axhline(y=4, color='r', linestyle='-', label="MTC")
ax.axhline(y=2, color='b', linestyle='-', label="MEC")

ax.plot(df.time, df["A_central"], linewidth=2, label=names[1], color=colors[1])
ax.legend()
ax.set_xlabel("time [hr]")
ax.set_ylabel("amount [mg]")

plt.show()





