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
    return x * y

def main():
    # Input parameters
    x0 = float(input("Enter the initial value of x: "))
    y0 = float(input("Enter the initial value of y at x = x0: "))
    h = float(input("Enter the step size (h): "))
    n = int(input("Enter the number of steps to take: "))

    # Perform Euler's method
    xs, ys = euler_method(f, x0, y0, h, n)

    # Print the results
    for x, y in zip(xs, ys):
        print(f"x = {x}, y = {y}")

if __name__ == "__main__":
    main()
    
    """
    Enter the initial value of x: 0
Enter the initial value of y at x = x0: 1
Enter the step size (h): 0.1
Enter the number of steps to take: 5
x = 0.0, y = 1.0
x = 0.1, y = 1.0
x = 0.2, y = 1.01
x = 0.30000000000000004, y = 1.0301
x = 0.4, y = 1.060401
x = 0.5, y = 1.10100501

    
    """
