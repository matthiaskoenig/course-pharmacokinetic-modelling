from helpers import dxdt_absorption_first_order, f_pk
import numpy as np
import pandas as pd

t_points = np.linspace(0, 6, num=8)
dose = 100  # [mg]
V = 6.0  # [l] 
CL = 5.0  # [L/hr]
C_points = dose/V * t_points * np.exp(-CL/V*t_points)

# overview of the measurement data

t_unit = "hr"
c_unit = "mg/l"
df = pd.DataFrame({
    "t": t_points, 
    "c": C_points,
})
print(df)

f_pk(t=df.t.values, c=df.c.values, dose=dose, show=True);