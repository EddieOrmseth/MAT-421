import numpy as np
import matplotlib.pyplot as plt


def f(x):
    a, b, c = 1, -3, 2
    return a*x**2 + b*x + c


def df(x):
    a, b, c = 1, -3, 2
    return 2*a*x + b


def line(slope, intercept, x):
    return slope * x + intercept
    

if __name__ == "__main__":
    x0 = 1
    slope = df(x0)

    y0 = f(x0)
    intercept = y0 - slope * x0

    x_values = np.linspace(-2, 4, 400)
    y_values = f(x_values)
    tangent_values = line(slope, intercept, x_values)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label="function", color='blue')
    plt.plot(x_values, tangent_values, label="Tangent", linestyle='dashed', color='red')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Quadratic Function and Tangent Line')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.show()
