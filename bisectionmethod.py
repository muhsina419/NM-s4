# Function to implement the Bisection Method
def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Solves the equation func(x) = 0 using the Bisection method.

    Parameters:
        func (function): The function for which we want to find the root.
        a (float): The starting point of the interval.
        b (float): The ending point of the interval.
        tol (float): The tolerance level for the root's accuracy (default is 1e-6).
        max_iter (int): The maximum number of iterations allowed (default is 100).

    Returns:
        float: The approximate root of the equation func(x) = 0.
        int: The number of iterations used.
    """
    # Ensure that the function changes sign over the interval [a, b]
    if func(a) * func(b) > 0:
        raise ValueError("The function must change signs over the interval [a, b].")

    # Initializing variables
    iteration = 0
    c = a  # c will store the middle point

    # Loop until we reach the maximum number of iterations or desired tolerance
    while (b - a) / 2.0 > tol and iteration < max_iter:
        # Find the midpoint
        c = (a + b) / 2.0
        iteration += 1
        
        # Check if c is the root or if the tolerance has been met
        if func(c) == 0:
            break  # The exact root is found
        elif func(a) * func(c) < 0:
            # The root lies between a and c
            b = c
        else:
            # The root lies between c and b
            a = c

    return c, iteration


# Example usage

# Define a non-linear equation, for example: f(x) = x^3 - 5x + 3
def func(x):
    return x**5 + 6*x + 2

# Initial interval [a, b]
a = -9
b = 12

# Calling the bisection method
root, iterations = bisection_method(func, a, b)

# Output the result
print(f"Root: {root}")
print(f"Number of iterations: {iterations}")
