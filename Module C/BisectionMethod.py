import numpy as np
import matplotlib.pyplot as plot
from scipy.interpolate import KroghInterpolator


def Bisect(f, a, b, tolerance = .001) -> float:
    c = 0
    fc = tolerance + 1
    while abs(fc) > tolerance:
        c = (a + b) / 2
        fc = f(c)

        if (fc * f(a)) < 0: b = c # replace b
        else: a = c # replace a

    return c


f = lambda x: (x-1)*(x-4)*(x-7)*(x-9)

# initial point around intervals, get y values
x_start_pts = [0, 3, 5, 8, 10]
y_start_pts = []
for i in range(0, len(x_start_pts)):
    y_start_pts.append(f(x_start_pts[i]))

# find the zeros between the intervals
x_found_pts = []
y_found_pts = []
for i in range(0, len(x_start_pts) - 1):
    x = Bisect(f, x_start_pts[i], x_start_pts[i + 1])
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
plot.title("Bisection Method")
plot.xlabel("X-axis")
plot.ylabel("Y-axis")
plot.legend()
plot.grid()
plot.show()
