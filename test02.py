import numpy as np


def euler_method(f, x0, y0, h, n):
    """
    Approximate the solution of the first-order ordinary differential equation
    y' = f(x, y) using Euler's method.

    :param f: The function defining the ODE y' = f(x, y)
    :param x0: The initial value of x
    :param y0: The initial value of y at x = x0
    :param h: The step size
    :param n: The number of steps to take
    :return: Approximate values of (x, y) using Euler's method
    """
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
    print("Investigating the Accuracy of Euler’s Method")
    print("\nUse Euler’s method to solve:")
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
    num_steps_a = int(1 / dx_a)

    for dx, num_steps, label in [(dx_a, num_steps_a, "(A)")]:
        # Perform Euler's method
        xs, ys = euler_method(f, x0, y0, dx, num_steps)

        # Calculate exact solution values
        exact_values = [exact_solution(x) for x in xs]

        print(f"Step size {label} dx = {dx}")
        print("x\tEuler's Method\tExact Solution\tError")
        for i in range(len(xs)):
            print(
                f"{xs[i]:.1f}\t{ys[i]:.4f}\t\t{exact_values[i]:.4f}\t\t{abs(ys[i] - exact_values[i]):.4f}"
            )
        print()


if __name__ == "__main__":
    main()
