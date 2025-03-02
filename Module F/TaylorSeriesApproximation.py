import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import math

# signList = [0, 1, 0, -1]
# def taylor_numeric(f, x0, n, h=1e-5): # only works for sin at x0 = 0
    # return [signList[i % 4] / math.factorial(i) for i in range(n)]
def taylor_numeric(f, x0, n, h=1e-5):
    return [derivative(f, x0, dx=h, n=i, order=2*i+1) / np.math.factorial(i) for i in range(n)]


def evaluate_taylor(x, taylor_coefficients, x0, start = 0, end = -1):
    if (end == -1): end = len(taylor_coefficients)
    
    result = 0.0
    for i in range(start, end):
        result += taylor_coefficients[i] * (x - x0)**i

    return result


def evaluate(function, x_data):
    y = []
    for x in x_data:
        y.append(function(x))
    return y


if __name__ == "__main__":

    x0 = 0
    coeffs_1 = taylor_numeric(np.sin, x0, 1)
    coeffs_2 = taylor_numeric(np.sin, x0, 2)
    coeffs_3 = taylor_numeric(np.sin, x0, 3)
    coeffs_4 = taylor_numeric(np.sin, x0, 4)
    coeffs_5 = taylor_numeric(np.sin, x0, 5)
    coeffs_6 = taylor_numeric(np.sin, x0, 6)

    x_data = np.linspace(0, 4, 1000)

    y_true = np.sin(x_data)
    y_taylor_1 = evaluate(lambda x: evaluate_taylor(x, coeffs_1, x0), x_data)
    y_taylor_2 = evaluate(lambda x: evaluate_taylor(x, coeffs_2, x0), x_data)
    y_taylor_3 = evaluate(lambda x: evaluate_taylor(x, coeffs_3, x0), x_data)
    y_taylor_4 = evaluate(lambda x: evaluate_taylor(x, coeffs_4, x0), x_data)
    y_taylor_5 = evaluate(lambda x: evaluate_taylor(x, coeffs_5, x0), x_data)
    y_taylor_6 = evaluate(lambda x: evaluate_taylor(x, coeffs_6, x0), x_data)

    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_true, label='True Function', color='black', linewidth=2)
    plt.plot(x_data, y_taylor_1, label='Taylor Series Function 1-Term', color='magenta', linewidth=2)
    plt.plot(x_data, y_taylor_2, label='Taylor Series Function 2-Term', color='green', linewidth=2)
    plt.plot(x_data, y_taylor_3, label='Taylor Series Function 3-Term', color='blue', linewidth=2)
    plt.plot(x_data, y_taylor_4, label='Taylor Series Function 4-Term', color='red', linewidth=2)
    plt.plot(x_data, y_taylor_5, label='Taylor Series Function 5-Term', color='orange', linewidth=2)
    plt.plot(x_data, y_taylor_6, label='Taylor Series Function 6-Term', color='purple', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('f\'(x)')
    plt.title('Finite Difference Approximations of f(x) = (x-1)(x-7)(x-7)')
    plt.legend()
    plt.grid(True)
    plt.ylim(-4, 4)

    plt.show()
