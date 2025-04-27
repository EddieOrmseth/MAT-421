import numpy as np
import matplotlib.pyplot as plt


class Interpolator:

    def interpolate_missing_values(self, x: np.array, y: np.array) -> np.array:
        raise "Interpolator::interpolate_missing_values must be implemented"
    
    def name(self):
        raise "Interpolator::name must be implemented"


def interp_example(interp: Interpolator):

    # x = np.linspace(0, 10, 1001)
    x = np.linspace(10, 20, 1001)
    y = np.zeros_like(x)
    for i in range(len(y)): y[i] = np.nan


    # 0010.jpg,1,593,278,0
    # 0011.jpg,1,592,271,0
    # 0012.jpg,1,591,265,0
    # 0013.jpg,1,590,259,0
    # 0014.jpg,1,590,257,0
    # 0015.jpg,1,589,253,0
    # 0016.jpg,1,587,252,0
    # 0017.jpg,1,586,252,0
    # 0018.jpg,1,585,252,0
    # 0019.jpg,1,585,255,0

    pts_x = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    pts_y = [593, 592, 591, 590, 590, 589, 587, 586, 585, 585]

    # pts_x = [0, 2, 3, 6, 8, 10]
    # pts_y = [1, 5, 3, 2, 8, 1]
    for i in range(len(pts_x)):
        idx = np.argmin(np.abs(x - pts_x[i]))
        y[idx] = pts_y[i]

    y_interp = interp.interpolate_missing_values(x, y)

    plt.plot(pts_x, pts_y, 'o', label='Original Points')
    plt.plot(x, y_interp, '--', label='Spline Curve')
    plt.legend()
    plt.show()
