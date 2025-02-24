import numpy as np
import matplotlib.pyplot as plt


def findExtrema(derivative, x0, learning_rate = .1, num_iterations: int = 100, seekMin: bool = True):
    if not seekMin: learning_rate *= -1
    point_list = [x0]
    for n in range(num_iterations):
        x_new = x0 - learning_rate * derivative(x0)
        x0 = x_new
        point_list.append(x_new)
    return point_list


if __name__ == "__main__":

    function = lambda x: (x-1) * (x-1) * (x-4)
    derivative = lambda x: (function(x + .001) - function(x - .001)) / .002

    x_values_min = findExtrema(derivative, 1.3)
    y_values_min = []
    for x in x_values_min:
        y_values_min.append(function(x))

    x_values_max = findExtrema(derivative, 0, seekMin=False)
    y_values_max = []
    for x in x_values_max:
        y_values_max.append(function(x))

    x_space = np.linspace(-2*np.pi, 2*np.pi, 400)
    y_func = []
    for x in x_space:
        y_func.append(function(x))

    plt.figure(figsize=(10, 6))
    plt.plot(x_space, y_func, label='line', color='blue', linewidth=2)
    plt.plot(x_values_min, y_values_min, label='points', color='red', linestyle="dotted", linewidth=2)
    plt.plot(x_values_max, y_values_max, label='points', color='green', linestyle="dotted", linewidth=2)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Taylor Series Approximations of sin(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.ylim(-5, 5)

    plt.show()
