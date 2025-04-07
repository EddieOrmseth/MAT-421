import numpy as np
import matplotlib.pyplot as plt


def eulers_method(f, x0, y0, h, x_end): # method to evaluate funtion used euler's method
    x_values = np.arange(x0, x_end + h, h) # make all the x values
    y_values = np.zeros(len(x_values)) # start with zeros
    y_values[0] = y0 # initial value
    
    for i in range(1, len(x_values)): # iteratively compute the next y value
        y_values[i] = y_values[i - 1] + h * f(x_values[i - 1])
    
    return x_values, y_values


if __name__ == '__main__':
        # (x-1)(x-3)(x-5)
    f = lambda x: x**3 - 9*x**2 + 23*x - 15
    df_dx = lambda x: 3*x**2 - 18*x + 23

    x0 = 0
    y0 = f(x0)
    h = 0.1
    x_end = 6
    x_vals, y_est_vals = eulers_method(df_dx, x0, y0, h, x_end) # grab x and y values

    y_real_vals = [f(x) for x in x_vals]

    # plot the rest of the data
    plt.plot(x_vals, y_est_vals, label="Euler's Approximation") # Plot the solution
    plt.plot(x_vals, y_real_vals, label="True Function") # Plot the solution
    plt.title("Euler's Method Example")
    plt.legend()
    plt.grid()
    plt.show()
