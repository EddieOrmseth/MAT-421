import numpy as np
import matplotlib.pyplot as plt


def evaluate(function, x_data):
    y = []
    for x in x_data:
        y.append(function(x))
    return y


def forwards_approx(function, x, h = 0.2):
    return (function(x + h) - function(x)) / h


def central_approx(function, x, h = 0.1):
    return (function(x + h) - function(x - h)) / (2*h)


def backwards_approx(function, x, h = 0.2):
    return (function(x) - function(x - h)) / h


if __name__ == "__main__":

    func = lambda x: 1*(x-1)*(x-7)*(x-7)
    deriv = lambda x: 1*3*(x-7)*(x-3)

    x_data = np.linspace(0, 10, 1000)

    value_y = evaluate(func, x_data)
    true_y = evaluate(deriv, x_data)
    forward_y = evaluate(lambda x: forwards_approx(func, x), x_data)
    central_y = evaluate(lambda x: central_approx(func, x), x_data)
    backwards_y = evaluate(lambda x: backwards_approx(func, x), x_data)

    plt.figure(figsize=(10, 6))
    plt.plot(x_data, value_y, label='True Function', color='black', linewidth=2)
    plt.plot(x_data, true_y, label='True Derivative', color='magenta', linewidth=2)
    plt.plot(x_data, forward_y, label='Forwards Approximation', color='red', linewidth=2)
    plt.plot(x_data, central_y, label='Central Approximation', color='green', linewidth=2)
    plt.plot(x_data, backwards_y, label='Backwards Approximation', color='blue', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('f\'(x)')
    plt.title('Finite Difference Approximations of f(x) = (x-1)(x-7)(x-7)')
    plt.legend()
    plt.grid(True)
    plt.ylim(-20, 50)

    plt.show()
