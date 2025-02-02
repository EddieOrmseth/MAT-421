import numpy as np
import matplotlib.pyplot as plot
from scipy.interpolate import KroghInterpolator

resolution = 100
x_points = np.array([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ])
y_points = np.array([ 1, 4, 7, 1, 2, 9, 1, 6, 4, 5 ])

interp = KroghInterpolator(x_points, y_points)

x_full = np.linspace(min(x_points), max(x_points), resolution)
y_full = interp(x_full)

plot.figure(figsize=(8, 5))
plot.plot(x_full, y_full, label='Newton Polynomial', color='blue')
plot.plot(x_points, y_points, marker='o', linestyle='None', color='r', label='Raw Points')
plot.title("Lagrange Interpolation")
plot.xlabel("X-axis")
plot.ylabel("Y-axis")
plot.legend()
plot.grid()
plot.show()
