import numpy as np
from tabulate import tabulate  # Add this line

class TerminalColors:
    # ANSI escape codes for text color
    RESET = "\033[0m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"


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

def main():
    print(TerminalColors.BLUE+"\n\n" + "Investigating the Accuracy of Euler’s Method" + TerminalColors.RESET)
    print("\n" + TerminalColors.GREEN + "Use Euler’s method to solve:" + "\n"+TerminalColors.RESET)
    print("y' = 1 + y, y(0) = 1,")
    print("on the interval 0 <= x <= 1, starting at x = 0 and taking:")
    print("(A) dx = 0.1")
    print("(B) dx = 0.05")
    print("compare the approximations with the values of the exact solution y = 2e^x - 1\n")

    # Initial condition
    x0 = float(input("Enter the initial value for x: "))  # 0
    y0 = float(input("Enter the initial value for y: "))  # 1

    # Input step size and number of steps for (A)
    dx_a = float(input("Enter the step size for (A) dx = 0.1: "))  # 0.1 , 0.05
    interval_size_a = 1.0  # Interval size from 0 to 1
    num_steps_a = int(interval_size_a / dx_a)

    for dx, num_steps, label in [(dx_a, num_steps_a, "(A)")]:
        # Perform Euler's method
        xs, ys = euler_method(f, x0, y0, dx, num_steps)

        # Calculate exact solution values
        exact_values = [exact_solution(x) for x in xs]

        print(f"Step size {label} dx = {dx}")
        print("x\tEuler's Method\tExact Solution\tError")
        table = []
        for i in range(len(xs)):
            table.append([f"{xs[i]:.1f}", f"{ys[i]:.4f}", f"{exact_values[i]:.4f}", f"{abs(ys[i] - exact_values[i]):.4f}"])
        print(tabulate(table, headers=["x", "Euler's Method", "Exact Solution", "Error"]))
        print()


if __name__ == "__main__":
    main()
