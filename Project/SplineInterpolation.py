import sys
import numpy as np
from scipy.interpolate import UnivariateSpline


try:
    from Interpolation import Interpolator, interp_example
except:
    cat = 12


class SplineInterpolator(Interpolator):

    k: int = 3
    s: int = 0


    def __init__(self, k: int = 3, s: int = 0):
        self.k = k
        self.s = s


    def interpolate_missing_values(self, x: np.array, y: np.array) -> np.array:
        mask = ~np.isnan(y)
        spline = UnivariateSpline(x[mask], y[mask], k=self.k, s=self.s)
        y_interp = y.copy()
        missing_indices = np.where(np.isnan(y))[0]
        y_interp[missing_indices] = spline(x[missing_indices])
        return y_interp
    
    
    def name(self):
        if self.k == 3: return "Cubic Spline"
        if self.k == 5: return "Quintic Spline"
        else: return "Spline"


if __name__ == '__main__':

    interp_example(SplineInterpolator(k = 3, s =0))
    interp_example(SplineInterpolator(k = 5, s = 0))
