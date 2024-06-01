import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, diff, lambdify


def getGradLine(num):
    x = Symbol('x')
    f_x = 0.3 * x**2
    f_prime = diff(f_x, x)
    f_prime_func = lambdify(x, f_prime, 'numpy')
    result = f_prime_func(num)
    return result

# Define the function f(x) = x^2
def f(x):
    return 0.3 *  x**2

# Generate x-values and corresponding y-values
x = np.linspace(-10, 10, 1000)
y = f(x)

# Create the initial plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Initialize the red horizontal line (hidden initially)
line, = ax.plot([], [], color='red', linestyle='-', linewidth=2)
line.set_visible(False)

LINE_LENGTH = 10

# Event handler for left-click
def on_click(event):
    if event.button == 1:  # Left mouse button
        x_clicked = event.xdata
        y_clicked = f(x_clicked)

        m = getGradLine(x_clicked)
        θ = np.arctan(m)
        y = 0.5 * LINE_LENGTH * np.sin(θ)
        x = 0.5 * LINE_LENGTH * np.cos(θ)
        # distance formula : d^2 = (x1 - x2)^2 + (y1 - y2)^2
        # m = (y2 - y1) / (x2 - x1)
        line.set_data([x_clicked - x, x_clicked + x], [y_clicked - y, y_clicked + y])
        line.set_visible(True)
        fig.canvas.draw()

# Connect the event handler
fig.canvas.mpl_connect('button_press_event', on_click)

# Set labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Interactive Plot: Click to Add Red Horizontal Line")
plt.legend()

plt.grid(True)
plt.show()

θ = 60






