import matplotlib.pyplot as plot
import numpy as np
from scipy.interpolate import interp1d as interp

x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
y = [ 1, 4, 7, 1, 2, 9, 1, 6, 4, 5 ]

x_full = np.linspace(min(x), max(x), 1000)
linearInterp = interp(x, y, kind="linear")
y_linear_full = linearInterp(x_full)

plot.plot(x, y, marker='o', linestyle='None', color='r', label='Original Data')
plot.plot(x_full, y_linear_full, marker='None', linestyle='-', color='b', label='Linear Interpolation')
plot.title("Linear Interpolation")
plot.xlabel("X-axis")
plot.ylabel("Y-axis")
plot.legend()
plot.grid()
plot.show()
