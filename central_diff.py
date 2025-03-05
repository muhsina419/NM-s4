import numpy as np

#Define the second derivative using the central difference method
def second_derivative(f,x,h=0.05):
    return (f(x+h)-2*f(x)+f(x-h)/(h**2))

#Example usage
def f(x):
    return np.sin(x)

#Given point 
x=np.pi/4
h=0.05

#second derivative functiom
second_derivative_result= second_derivative(f,x,h)

print("Second derivative of f(x) at x=pi/4 :", second_derivative_result)