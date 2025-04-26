import sys
import numpy as np


try:
    from Interpolation import Interpolation, interp_example
except:
    cat = 12


class NewtonInterpolation(Interpolation):

    def interpolate_missing_values(self, x: np.array, y: np.array) -> np.array:
        mask = ~np.isnan(y)
        coefs = self.divided_differences(x[mask], y[mask])

        y_interp = y.copy()
        for i in range(len(x)):
            if np.isnan(y_interp[i]):
                y_interp[i] = self.newton_poly_eval(x[mask], coefs, x[i])

        return y_interp


    def divided_differences(self, x, y):
        n = len(x)
        coef = np.array(y, dtype=float)
        for j in range(1, n):
            coef[j:] = (coef[j:] - coef[j - 1:-1]) / (x[j:] - x[:n - j])
        return coef


    def newton_poly_eval(self, x_data, coef, x):
        result = 0
        basis_product = 1  # initially, this is 1 (for the a_0 term)

        for i in range(len(coef)):
            result += coef[i] * basis_product
            basis_product *= (x - x_data[i])  # build up (x - x0)(x - x1)... step-by-step

        return result


if __name__ == '__main__':
    
    interp_example(NewtonInterpolation())
