import matplotlib.pyplot as plt

def runge_kutta(f, x0, y0, h, n):
    """
    Solves a differential equation using the fourth-order Runge-Kutta method.

    :param f: Function representing the right-hand side of the differential equation (dy/dx = f(x, y)).
    :param x0: Initial value of x.
    :param y0: Initial value of y (the value of the function at x0).
    :param h: Step size.
    :param n: Number of steps.
    :return: Arrays of x and y values (the solution of the differential equation).
    """
    x = [x0]
    y = [y0]

    for i in range(1, n + 1):
        k1 = h * f(x[-1], y[-1])
        k2 = h * f(x[-1] + h/2, y[-1] + k1/2)
        k3 = h * f(x[-1] + h/2, y[-1] + k2/2)
        k4 = h * f(x[-1] + h, y[-1] + k3)

        y_new = y[-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
        x_new = x[-1] + h

        x.append(x_new)
        y.append(y_new)

    return x, y

# Function representing the right-hand side of the differential equation
def f(x, y):
    return x**2 + y

# Initial conditions
x0 = 0
y0 = 1
# Step size and number of steps
h = 0.1
n = 100

# Solving the differential equation using the Runge-Kutta method
x, y = runge_kutta(f, x0, y0, h, n)

# Printing the results
print("Results of the Runge-Kutta method:")
for i in range(len(x)):
    print(f"Step {i+1}: x = {x[i]}, y = {y[i]}")

# Plotting the results
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of the Differential Equation using Runge-Kutta Method')
plt.grid(True)
plt.show()
