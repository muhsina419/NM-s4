import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return x+y

def euler_method(x0,y0,x_end,h):
    x_values = np.arange(x0,x_end+h,h)
    y_values = np.zeros(len(x_values))

    y_values[0]=y0

    for i in range (1, len(x_values)):
        y_values[i]=y_values[i-1]+h * f(x_values[i-1], y_values[i-1])

    return x_values,y_values

x0 = 0
y0 = 1
x_end = 2
h = 0.1

x_values , y_values = euler_method(x0,y0,x_end,h)

plt.plot (x_values,y_values,label="Euler Approximation", marker="o" , linestyle="-")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler method approximation")
plt.legend()
plt.grid(True)
plt.show()