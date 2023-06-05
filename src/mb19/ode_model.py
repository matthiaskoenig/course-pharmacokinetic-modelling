from scipy.integrate import odeint
from matplotlib import pyplot as plt
import numpy as np

# Parameter
V = 10  # [l]
CL = 0.1  # [L/hr]
Dose = 100  # [mg]


def ydot(y, t):
    """ODE system: dx/dt"""
    C = y[0]
    return np.array([-CL/V * C])


# initial condition
y0 = np.array([Dose/V, ])  # [mg/l]

# Numerical integration
t = np.linspace(start=0, stop=10*24, num=200)  # [hr]
C = odeint(ydot, y0, t)

f, ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 5), dpi=300)
ax.plot(t/24.0, C[:, 0], label="warfarin", color="black", linewidth=2.0)
ax.set_xlabel("time [day]")
ax.set_ylabel("warfarin [mg/l]")
ax.set_ylim(bottom=0)
ax.legend()
plt.show()
