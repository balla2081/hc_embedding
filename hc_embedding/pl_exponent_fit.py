import numpy as np
import powerlaw


def get_pl_exponent(g):
    degree = np.array(list(g.degree().values()))
    results = powerlaw.Fit(degree)
    return results.power_law.alpha
