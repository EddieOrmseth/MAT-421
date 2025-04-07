import numpy as np
import matplotlib.pyplot as plt


def f(x, y): # this is the same ODE as before
    return -2 * y + 3 * x


def eulers_method(f, x0, y0, h, x_end): # method to evaluate funtion used euler's method
    x_values = np.arange(x0, x_end + h, h) # make all the x values
    y_values = np.zeros(len(x_values)) # start with zeros
    y_values[0] = y0 # initial value
    
    for i in range(1, len(x_values)): # iteratively compute the next y value
        y_values[i] = y_values[i - 1] + h * f(x_values[i - 1], y_values[i - 1])
    
    return x_values, y_values


# initial value stuff
x0 = 0
y0 = 5
h = 0.1
x_end = 5
x_vals, y_vals = eulers_method(f, x0, y0, h, x_end) # grab x and y values

# plot the rest of the data
plt.plot(x_vals, y_vals, label="Euler's Approximation") # Plot the solution
plt.title("Euler's Method Example")
plt.legend()
plt.grid()
plt.show()
