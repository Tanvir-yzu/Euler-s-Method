#include <stdio.h>
#include <math.h>

#define f(x, y) (y)  // Define the function y' = f(x, y)

// Define the exact solution function for comparison
float exact_solution(float x) {
    return exp(x); // Example: For y' = y, the exact solution is y = e^x
}

int main() {
    // Declare variables
    float x0, y0, x, y, h; // Initial x, y, step size h
    int i, n; // Number of steps

    // Prompt the user to enter initial values and step parameters
    printf("Enter the initial value of x0: ");
    scanf("%f", &x0);

    printf("Enter the initial value of y0: ");
    scanf("%f", &y0);

    printf("Enter the value of step size h: ");
    scanf("%f", &h);

    printf("Enter the number of steps n: ");
    scanf("%d", &n);

    // Check if the number of steps is valid
    if (n <= 0) {
        printf("Number of steps must be positive. Please enter a valid value.\n");
        return 1;
    }

    // Initialize x and y with initial values
    x = x0;
    y = y0;

    // Print the header of the table
    printf("\n");
    printf("x\t\ty (Euler)\ty (Exact)\tError\n");
    printf("\n");

    // Print the initial values and error
    printf("%f\t%f\t%f\t%f\n", x, y, exact_solution(x), fabs(y - exact_solution(x)));

    // Perform Euler's method and print results
    for (i = 1; i <= n; i++) {
        y = y + h * f(x, y); // Update y using Euler's method
        x = x + h; // Update x
        printf("%f\t%f\t%f\t%f\n", x, y, exact_solution(x), fabs(y - exact_solution(x))); // Print results
    }

    return 0;
}
