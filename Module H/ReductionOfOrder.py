import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


x = sp.symbols('x') # create main variable
v = sp.Function('v')(x)
C1, C2 = sp.symbols('C1 C2') # create constants for later

# y1 and y2 solutions
y1 = x**2
y2 = v * y1

# compute derivatives
y2_diff1 = sp.diff(y2, x)
y2_diff2 = sp.diff(y2_diff1, x)

# main ode to be solved
ode = x**2 * y2_diff2 - 4*x * y2_diff1 + 6*y2
ode_simplified = sp.simplify(ode)

# final solutions
v_eqn = sp.simplify(ode_simplified / y1)
v_general = sp.dsolve(sp.simplify(v_eqn), v).rhs
y2_final = sp.simplify(v_general * y1)
y2_final = y2_final.subs({C1: 1, C2: 0})

# create the final solution stuff
print(f"Second solution: y2(x) = {y2_final}")
y2_func = sp.lambdify(x, y2_final, 'numpy')

# values to be displayed in the plot
x_vals = np.linspace(0, 5, 100) # x values
y1_vals = x_vals**2
y2_vals = y2_func(x_vals)

# plot the rest of the data
plt.plot(x_vals, y1_vals, label="Y1 function", linestyle="dashed")
plt.plot(x_vals, y2_vals, label="Y2 function", linestyle="solid") # this line fails
plt.title("Both Solutions")
plt.legend()
plt.grid()
plt.show()
