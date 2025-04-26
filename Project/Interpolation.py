import numpy as np
import matplotlib.pyplot as plt


class Interpolation:

    def interpolate_missing_values(self, x: np.array, y: np.array) -> np.array:
        raise "Must be implemented!"


def interp_example(interp: Interpolation):

    x = np.linspace(0, 1, 1001)
    y = np.zeros_like(x)
    for i in range(len(y)): y[i] = np.nan

    pts_x = [0, 2, 3, 6, 8, 10]
    pts_y = [1, 5, 3, 2, 8, 1]
    for i in range(len(pts_x)):
        idx = np.argmin(np.abs(x - pts_x[i]))  # Find index closest to desired x
        y[idx] = pts_y[i]

    y_newton = interp.interpolate_missing_values(x, y)

    plt.plot(pts_x, pts_y, 'o', label='Original Points')
    plt.plot(x, y_newton, '--', label='Spline Curve')
    plt.legend()
    plt.show()
