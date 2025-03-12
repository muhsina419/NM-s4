def f(x):
    # Define the function to be integrated
    return x**2  # Example: f(x) = x^2

def trapezoidal_rule(a, b, n):
   
    # Calculate the step size
    h = (b - a) / n
    
    # Initialize the sum for the integral
    result = f(a) + f(b)
    
    for i in range(1, n):
        result += 2 * f(a + i * h)
    
    # Multiply by h/2 to get the final result
    result *= h / 2
    return result

# Example usage
a = 0  # Lower limit
b = 2  # Upper limit
n = 4  # Number of intervals (must be even)

integral_value = trapezoidal_rule(a, b, n)
print(f"The approximate value of the integral is: {integral_value}")
