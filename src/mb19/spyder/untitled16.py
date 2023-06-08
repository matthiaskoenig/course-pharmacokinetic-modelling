import numpy as np
import matplotlib.pyplot as plt

dose = 100  # [mg]
V = 6.0  # [l]
CL = 5.0  # [L/hr]

# Generate time vector t spanning 20 hours
t = np.linspace(0, 20, num=100)

# Calculate concentration C using the equation
C = dose / V * t * np.exp(-CL / V * t)

# Generate the plot
plt.plot(t, C)
plt.xlabel('Time (hr)')
plt.ylabel('Concentration (mg/L)')
plt.title('Concentration vs. Time')
plt.grid(True)
plt.show()


import numpy as np
from scipy.integrate import trapz
from scipy.interpolate import interp1d

# Assuming you already have the time vector `t` and concentration vector `C`

# Calculate AUC using the trapezoidal rule
AUC = trapz(C, t)

# Calculate AUCinf (extrapolated AUC to infinity)
last_concentration = C[-1]
AUCinf = AUC + last_concentration / CL

# Calculate half-life (thalf)
half_concentration = C[0] / 2
interp_func = interp1d(C, t)
thalf = float(interp_func(half_concentration))

# Print the calculated pharmacokinetic parameters
print(f"AUC: {AUC:.2f} mg*hr/L")
print(f"AUCinf: {AUCinf:.2f} mg*hr/L")
print(f"Half-life (thalf): {thalf:.2f} hr")