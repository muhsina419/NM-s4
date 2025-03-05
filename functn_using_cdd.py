import numpy as np

#Define function f(x)=sin(x)
def f(x):
    return np.sin(x)

#Given values
x=np.pi/4
h=0.05

#calculate the central difference approximation
derivative_approx = (f(x+h)-f(x-h))/(2*h)
print(derivative_approx)