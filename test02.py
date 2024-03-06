import numpy as np

def euler_method(f, x0, y0, h, n):
    xs = [x0]  # List to store x values
    ys = [y0]  # List to store y values

    for i in range(n):
        x = xs[-1]
        y = ys[-1]
        y_next = y + h * f(x, y)  # Euler's method formula
        x_next = x + h
        xs.append(x_next)
        ys.append(y_next)

    return xs, ys

def f(x, y):
    return 1 + y

def exact_solution(x):
    return 2 * np.exp(x) - 1

# Initial condition
x0 = 0
y0 = 1

# Step size and number of steps
dx = 0.1
num_steps = int(1 / dx)

# Perform Euler's method
xs, ys = euler_method(f, x0, y0, dx, num_steps)

# Calculate exact solution values
exact_values = [exact_solution(x) for x in xs]

print("Step size dx =", dx)
print("x\tEuler's Method\tExact Solution\tDifference")

for i in range(len(xs)):
    print(f"{xs[i]:.2f}\t{ys[i]:.6f}\t{exact_values[i]:.6f}\t{abs(ys[i] - exact_values[i]):.6f}")
