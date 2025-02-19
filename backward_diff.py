import math
def f(x):
    return math.exp(x)

def backward_difference (x,h):
    return(f(x)-f(x-h))/h

x=1
h=0.01
result=backward_difference(x,h)
print(f"Approximate first derivative at x={x}: {result}")