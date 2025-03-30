import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# this is the initial function I will use
def ode_function(t, y):
    return -2*y + 3*t


# the initail value is 0, only 1 element since there is only 1 dimension
y0 = [5]

t_span = (0, 5) # evaluate the function on this interval
t_eval = np.linspace(0, 5, 100) # this is the space, with a total of 100 values

# use scipy to solve the initial value problem
solution = solve_ivp(ode_function, t_span, y0, t_eval=t_eval, method='RK45')

plt.plot(solution.t, solution.y[0], label="ODE IVP Example") # plot the solution
plt.title("Solution to the IVP")
plt.legend()
plt.grid()
plt.show()
