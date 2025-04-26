import sys
import numpy as np


try:
    from Interpolation import Interpolation, interp_example
except:
    cat = 12


class PiecewiseInterpolation(Interpolation):

    def interpolate_missing_values(self, x: np.array, y: np.array) -> np.array:
        present_indices = np.where(~np.isnan(y))[0]
        missing_indices = np.where(np.isnan(y))[0]

        x_present = x[present_indices]
        y_present = y[present_indices]
        y_interp = y.copy()

        for i in missing_indices:
            i_larger, i_smaller = self.find_surrounding_pts(x_present, x[i])
            if i_larger == -1 or i_smaller == -1: continue

            y_interp[i] = y_present[i_smaller] + ((y_present[i_larger] - y_present[i_smaller]) / (x_present[i_larger] - x_present[i_smaller])) * (x[i] - x_present[i_smaller])

        return y_interp

        
    def find_surrounding_pts(self, data, x):
        if x <= data[0]: return 0, 1
        elif data[-1] <= x: return len(data) - 2, len(data) - 1
        
        for i in range(len(data) - 1):
            if data[i] <= x <= data[i + 1]:
                return i, i + 1
    

if __name__ == '__main__':

    interp_example(PiecewiseInterpolation())
