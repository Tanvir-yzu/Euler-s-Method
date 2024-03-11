#include <stdio.h>
//#include <math.h>

#define f(x, y) (y)

int main() {
    float x0, y0, x, y, h;
    int i, n;

    printf("Enter the initial value of x0: ");
    scanf("%f", &x0);

    printf("Enter the initial value of y0: ");
    scanf("%f", &y0);

    printf("Enter the value of step size h: ");
    scanf("%f", &h);

    printf("Enter the number of steps n: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Number of steps must be positive. Please enter a valid value.\n");
        return 1;
    }

    x = x0;
    y = y0;

    printf("\n");
    printf("x\t\ty\n");
    printf("%f\t%f\n", x, y);

    for (i = 1; i <= n; i++) {
        y = y + h * f(x, y);
        x = x + h;
        printf("%f\t%f\n", x, y);
    }

    return 0;
}
