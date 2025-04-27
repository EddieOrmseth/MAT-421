import sys
import numpy as np
from scipy.interpolate import lagrange


try:
    from Interpolation import Interpolator, interp_example
except:
    cat = 12


class LagrangeInterpolator(Interpolator):


    def interpolate_missing_values(self, x: np.array, y: np.array) -> np.array:
        mask = ~np.isnan(y)
        interp_func = lagrange(x[mask], y[mask])
        missing_indices = np.where(np.isnan(y))
        y_interp = y.copy()
        y_interp[missing_indices] = interp_func(x[missing_indices])
        return y_interp
    

    def name(self):
        return "Lagrange"


if __name__ == '__main__':

    interp_example(LagrangeInterpolator())
