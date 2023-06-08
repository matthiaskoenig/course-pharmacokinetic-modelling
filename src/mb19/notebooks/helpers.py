from scipy import stats
import numpy as np


def print_pk(pk):
    """Print pk information"""
    lines = []
    keys = [key for key in pk if not "unit" in key]
    for key in keys:
        unit = pk[f"{key}_unit"]
        lines.append(
            f"{key:<10}: {pk[key]:.2f} [{unit}]"
        )
    info = "\n".join(lines)
    print(info)


def f_pk(t, c, dose, show: bool = False):
    """Calculate PK information."""
    dose_unit = "mg"
    t_unit = "hr"
    c_unit = "mg/l"
    auc_unit = f"{c_unit}*{t_unit}"
    cl_unit = "l/hr"
    vd_unit = "l"

    auc = np.sum((t[1:] - t[0:-1]) * (c[1:] + c[0:-1]) / 2.0)
    idx = np.nanargmax(c)
    tmax, cmax = t[idx], c[idx]

    max_index = np.nanargmax(c)
    x = t[max_index + 1:]
    y = np.log(c[max_index + 1:])

    # using mask to remove nan values
    mask = ~np.isnan(x) & ~np.isnan(y)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask], y[mask])

    kel = -slope
    thalf = np.log(2) / kel

    auc_delta = -c[-1] / slope
    aucinf = auc + auc_delta

    vd = dose / (aucinf * kel)
    cl = kel * vd

    pk = {
        'dose': dose,
        'dose_unit': dose_unit,
        'auc': auc,
        'auc_unit': auc_unit,
        'aucinf': aucinf,
        'aucinf_unit': auc_unit,
        'tmax': tmax,
        'tmax_unit': t_unit,
        'cmax': cmax,
        'cmax_unit': c_unit,
        'thalf': thalf,
        'thalf_unit': t_unit,
        'kel': kel,
        'kel_unit': f"1/{t_unit}",
        'vd': vd,
        'vd_unit': vd_unit,
        'cl': cl,
        'cl_unit': cl_unit,
    }
    if show:
        print_pk(pk)

    return pk


def dxdt_absorption_first_order(x, t, ka, ke):
    """
    First order absorption model
    """
    # state variables
    A_tablet = x[0]  # [mg]
    A_central = x[1]  # [mg/l]
    A_urine = x[2]  # [mg]

    # rates
    va = ka * A_tablet  # [mg/hr]
    ve = ke * A_central  # [mg/hr]

    # odes (stoichiometric equation)
    return [
        -va,  # dA_tablet/dt  [mg/hr]
        va - ve,  # dA_central/dt [mg/hr]
        ve,  # dA_urine/dt  [mg/hr]
    ]
