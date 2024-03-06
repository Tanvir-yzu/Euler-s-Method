# Investigating the Accuracy of Euler’s Method

This Python script investigates the accuracy of Euler's method in approximating the solution of a first-order ordinary differential equation.

## Problem Description

We are given the differential equation:

    y' = 1 + y, y(0) = 1,

and we need to solve it on the interval 0 <= x <= 1 using Euler’s method. Two step sizes are considered:
- (A) dx = 0.1
- (B) dx = 0.05

We will compare the approximations obtained using Euler’s method with the exact solution y = 2e^x - 1.

## Usage

1. Run the script.
2. Enter the initial values for x and y.
3. Enter the step size for (A) dx = 0.1.
4. The program will compute and display the approximations using Euler's method along with the exact solution and the error for each step.

## Instructions

- Make sure you have Python installed on your system.
- Run the script in a Python environment.
- Follow the prompts to enter the required values.
- Review the output to observe the accuracy of Euler's method for the given problem.

## Output 
```
Use Euler’s method to solve:
y' = 1 + y, y(0) = 1,
on the interval 0 <= x <= 1, starting at x = 0 and taking:
(A) dx = 0.1
(B) dx = 0.05
compare the approximations with the values of the exact solution y = 2e^x - 1

Enter the initial value for x: 0
Enter the initial value for y: 1
Enter the step size for (A) dx = 0.1: 0.1
Step size (A) dx = 0.1
x       Euler's Method  Exact Solution  Error
0.0     1.0000          1.0000          0.0000
0.1     1.2000          1.2103          0.0103
0.2     1.4200          1.4428          0.0228
0.3     1.6620          1.6997          0.0377
0.4     1.9282          1.9836          0.0554
0.5     2.2210          2.2974          0.0764
0.6     2.5431          2.6442          0.1011
0.7     2.8974          3.0275          0.1301
0.8     3.2872          3.4511          0.1639
0.9     3.7159          3.9192          0.2033
1.0     4.1875          4.4366          0.2491

```