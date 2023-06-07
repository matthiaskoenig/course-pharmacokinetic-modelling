import numpy as np
from scipy.integrate import odeint
from matplotlib import pylab as plt

def dydt_compartment_model(x, t, ka, km, ke):
    """
    System of ODEs of the compartment model.
    """
    # state variables
    A_tablet = x[0]
    A_central = x[1]
    B_central = x[2]
    A_urine = x[3]
    B_urine = x[4]
    
    # rates
    va = ka * A_tablet
    vm = km * A_central
    vuA = ke * A_central
    vuB = ke * B_central

    # odes (stoichiometric equation)    
    return [
        -va,             # dA_tablet/dt
         va - vm - vuA,  # dA_central/dt
         vm - vuB,       # dB_central/dt
         vuA,            # dA_urine/dt
         vuB,            # dB_urine/dt
    ] 


# initial condition and time span
t = np.arange(0, 10, 0.1)
Dose_A = 10.0
x0 = [
    Dose_A,  # A_tablet
    0.0,   # A_central
    0.0,   # B_central
    0.0,   # A_urine
    0.0,   # B_urine
]

# parameters
ka = 1.0
km = 1.0
ke = 1.0