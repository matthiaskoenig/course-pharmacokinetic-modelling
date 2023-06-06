import numpy as np
import matplotlib.pyplot as plt

def simple_euler(C0, tend, N, CL, V):
    """ The function integrates the simple
    system dx/dt = -k x to a time tend using the  
    Euler method (N Steps) and initial condition x0.

    usage: C = simple_euler(C0, t, N)
    """
    k = 1 # set parameter k

    # some parameters
    dt = float(tend)/N
    timespan = np.linspace(0, tend, num=N)

    C = [float(C0)]

    # integration
    for i in range(1, N):
        # C(t) + dt * f
        C.append(C[i-1] + dt*(-CL/V*C[i-1]))
        
        
    # plot both solutions
    # f, ax = plt.subplots(nrows=1, ncols=1)
    # ax.plot(timespan, C,'ko', markersize=8, label='Euler method')
    # ax.plot(timespan, C0*np.exp(-CL/V*timespan), 'r-', label='analytical solution')
    # ax.set_xlabel('time t [hr]')
    # ax.set_ylabel('C(t) [mg]')
    # ax.legend(loc='upper right')
    # plt.show()

    abs_err = np.abs(C - C0*np.exp(-CL/V*timespan))
    print(abs_err)
    err = sum(abs_err)

    # return value of function
    return err

V = 10.14  # [l]
CL = 0.13  # [l/hr]
DOSE = 102  # [mg]
C0 = DOSE/V

steps = range(2,20)
errors = np.zeros_like(steps)
for k, N in enumerate(steps):
    err= simple_euler(C0=C0, tend=24*10, N=int(N), CL=CL, V=V)

    errors[k] = err

print(errors)

# simple_euler(C0=C0, tend=24*10, N=100, CL=CL, V=V)
# Dose dependency
# f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5), dpi=300)






