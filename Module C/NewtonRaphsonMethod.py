import numpy as np
import matplotlib.pyplot as plot
from scipy.interpolate import KroghInterpolator


def NewtonRaphson(f, f_prime, x, tolerance = .01) -> float:
    while (abs(f(x)) > tolerance):
        x = x - (f(x) / f_prime(x))
    return x


f = lambda x: (x-1)*(x-4)*(x-7)*(x-9)
f_prime = lambda x: (f(x + .001) - f(x - .001)) / (.002)

# initial point around intervals, get y values
x_start_pts = [.5, 5, 6, 9.5]
y_start_pts = []
for i in range(0, len(x_start_pts)):
    y_start_pts.append(f(x_start_pts[i]))

# find the zeros between the intervals
x_found_pts = []
y_found_pts = []
for i in range(0, len(x_start_pts)):
    x = NewtonRaphson(f, f_prime, x_start_pts[i])
    x_found_pts.append(x)
    y_found_pts.append(f(x))

# compute so we can show equation
resolution = 100
x_full = np.linspace(0, 10, resolution)
y_full = []
for i in range(0, len(x_full)):
    y_full.append(f(x_full[i]))

# display everything
plot.figure(figsize=(8, 5))
plot.plot(x_start_pts, y_start_pts, marker='o', linestyle='None', color='r', label='Start Points')
plot.plot(x_found_pts, y_found_pts, marker='o', linestyle='None', color='b', label='Found Zeros')
plot.plot(x_full, y_full, marker='None', linestyle='-', color='g', label='Equation')
plot.title("Newton-Raphson Method")
plot.xlabel("X-axis")
plot.ylabel("Y-axis")
plot.legend()
plot.grid()
plot.show()
