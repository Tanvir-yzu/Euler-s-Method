import numpy as np
import matplotlib.pyplot as plt

class TerminalColors:
    # ANSI escape codes for text color
    RESET = "\033[0m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"

def f(x, y):
    return 1 + y

def euler_method(x0, y0, h, x_interval):
    """
    Implements Euler's method to solve a differential equation.

    Parameters:
    x0 (float): Initial x value.
    y0 (float): Initial y value.
    h (float): Step size.
    x_interval (list): List containing the start and end x values.

    Returns:
    tuple: Tuple containing arrays of x and y values.
    """
    n = int((x_interval[1] - x_interval[0]) / h)
    x_values = np.linspace(x_interval[0], x_interval[1], n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0
    
    for i in range(n):
        y_values[i+1] = y_values[i] + h * f(x_values[i], y_values[i])
    
    return x_values, y_values

def exact_solution(x):
    return 2 * np.exp(x) - 1

def print_table(xs, ys, exact_values):
    print("x\tEuler's Method\tExact Solution\tError")
    for i in range(len(xs)):
        error = abs(ys[i] - exact_values[i])
        print(f"{xs[i]:.1f}\t{ys[i]:.4f}\t\t{exact_values[i]:.4f}\t\t{error:.4f}")

def main():
    print(TerminalColors.BLUE + "\n\n" + "Investigating the Accuracy of Euler’s Method" + TerminalColors.RESET)
    print("\n" + TerminalColors.GREEN + "Use Euler’s method to solve:" + "\n" + TerminalColors.RESET)
    print("y' = 1 + y, y(0) = 1,")
    print("on the interval 0 <= x <= 1, starting at x = 0")

    x0 = 0.0
    y0 = 1.0

    dx = float(input("Enter the step size (e.g., 0.1): "))
    interval_size = 1.0
    num_steps = int(interval_size / dx)

    x_values, y_values = euler_method(x0, y0, dx, [x0, 1])
    exact_values = [exact_solution(x) for x in x_values]

    print(f"Step size dx = {dx}")
    print_table(x_values, y_values, exact_values)
    
    plt.plot(x_values, y_values, label=f'Euler (Step size: {dx})')
    x_exact = np.linspace(x0, 1, 100)
    y_exact = exact_solution(x_exact)
    plt.plot(x_exact, y_exact, label='Exact solution', linestyle='--')
    plt.legend()
    plt.title('Approximated vs Exact Solutions for Euler\'s Method')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
