import numpy as np
import matplotlib.pyplot as plt


def trig_diffentiate_sin(diff_num: int):
    diff_num %= 4
    if diff_num == 0: # derivatice of -cos is sin
        return lambda x: np.sin(x)
    elif diff_num == 1: # derivative of sin is cos
        return lambda x: np.cos(x)
    elif diff_num == 2: # derivative of cos is -sin
        return lambda x: -np.sin(x)
    else: # derivative of -sin is -cos
        return lambda x: -np.cos(x)


def compute_value(termList, x):
    total = 0
    for term in termList:
        total += term(x)
    return total


def taylor_sin(n_terms, a):
    termList = []
    for n in range(n_terms):
        derivative = trig_diffentiate_sin(n)
        f = lambda x, n=n, derivative=derivative: (derivative(a) * (x - a)**n) / (np.math.factorial(n))
        termList.append(f)
    
    return lambda x: compute_value(termList, x)


if __name__ == "__main__":
    x_values = np.linspace(-2*np.pi, 2*np.pi, 400)

    taylor_3 = taylor_sin(3, 0)  # 3 terms total
    taylor_5 = taylor_sin(5, 0)  # 5 terms total
    taylor_7 = taylor_sin(7, 0)  # 7 terms total

    true_values = np.sin(x_values)
    taylor_3_values = taylor_3(x_values)
    taylor_5_values = taylor_5(x_values)
    taylor_7_values = taylor_7(x_values)

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, true_values, label='sin(x)', color='black', linewidth=2)
    plt.plot(x_values, taylor_3_values, label='Taylor Series (3 terms)', linestyle='dashed', color='blue')
    plt.plot(x_values, taylor_5_values, label='Taylor Series (5 terms)', linestyle='dashed', color='green')
    plt.plot(x_values, taylor_7_values, label='Taylor Series (7 terms)', linestyle='dashed', color='red')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Taylor Series Approximations of sin(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.ylim(-2, 2)

    plt.show()
