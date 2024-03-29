# Import necessary libraries
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For plotting
from tabulate import tabulate  # For creating tables in the terminal


# Define a class for terminal colors
class TerminalColors:
    # ANSI escape codes for text color
    RESET = "\033[0m"  # Reset color to default
    GREEN = "\033[92m"  # Green color
    BLUE = "\033[94m"  # Blue color


# Define the differential equation as a function
def f(x, y):
    return 1 + y  # The differential equation is y' = 1 + y


# Euler's method function
def euler_method(x0, y0, h, x_interval):
    # Initialize variables
    x = x0
    y = y0
    n = int((x_interval[1] - x_interval[0]) / h)  # Calculate the number of steps
    x_values = np.linspace(x_interval[0], x_interval[1], n + 1)  # Generate x values
    y_values = np.zeros(n + 1)  # Initialize y values array
    y_values[0] = y0  # Set initial y value

    # Perform Euler's method
    for i in range(n):
        y = y_values[i] + h * f(x, y)  # Update y using Euler's method
        x += h  # Increment x
        y_values[i + 1] = y  # Store updated y value

    return x_values, y_values


# Exact solution function
def exact_solution(x):
    return 2 * np.exp(x) - 1  # The exact solution is y = 2e^x - 1


# Main function
def main():
    # Prompt and explanation
    print(
        TerminalColors.BLUE
        + "\n\n"
        + "Investigating the Accuracy of Euler’s Method"
        + TerminalColors.RESET
    )
    print(
        "\n"
        + TerminalColors.GREEN
        + "Use Euler’s method to solve:"
        + "\n"
        + TerminalColors.RESET
    )
    print("y' = 1 + y, y(0) = 1,")
    print("on the interval 0 <= x <= 1, starting at x = 0 and taking:")
    print("(A) dx = 0.1")
    print("(B) dx = 0.05")
    print(
        "compare the approximations with the values of the exact solution y = 2e^x - 1\n"
    )

    # Input initial values and step size
    x0 = float(input("Enter the initial value for x: "))
    y0 = float(input("Enter the initial value for y: "))
    dx_a = float(input("Enter the step size for (A) dx = 0.1: "))
    interval_size_a = 1.0  # Interval size from 0 to 1
    num_steps_a = int(interval_size_a / dx_a)

    # Iterate over specified step sizes
    for dx, num_steps, label in [(dx_a, num_steps_a, "(A)")]:
        # Perform Euler's method
        xs, ys = euler_method(x0, y0, dx, [x0, 1])

        # Calculate exact solution values
        exact_values = [exact_solution(x) for x in xs]

        # Print results in a table
        print(f"Step size {label} dx = {dx}")
        table = []
        for i in range(len(xs)):
            table.append(
                [
                    f"{xs[i]:.1f}",
                    f"{ys[i]:.4f}",
                    f"{exact_values[i]:.4f}",
                    f"{abs(ys[i] - exact_values[i]):.4f}",
                ]
            )
        print(
            tabulate(table, headers=["x", "Euler's Method", "Exact Solution", "Error"])
        )
        print()

    # Plot the approximated solution
    plt.plot(xs, ys, label=f"Euler (Step size: {dx})")

    # Plot the exact solution
    x_exact = np.linspace(x0, 1, 100)
    y_exact = exact_solution(x_exact)
    plt.plot(x_exact, y_exact, label="Exact solution", linestyle="--")

    # Add grid lines
    plt.grid(True, linestyle="--", alpha=0.7)

    # Legend and title
    plt.legend()
    plt.title("Approximated vs Exact Solutions for Euler's Method")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
