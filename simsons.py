def f(x):
    # Define the function to be integrated
    return x**2  # Example: f(x) = x^2

def simpsons_rule(a, b, n):
    # Ensure n is even
    if n % 2 != 0:
        print("Error: n must be even")
        return None
    
    # Calculate the step size
    h = (b - a) / n
    
    # Initialize the sum for the integral
    result = f(a) + f(b)
    
    # Sum the odd terms (with coefficient 4)
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    
    # Sum the even terms (with coefficient 2)
    for i in range(2, n, 2):
        result += 2 * f(a + i * h)
    
    # Multiply by h/3 to get the final result
    result *= h / 3
    return result

# Example usage
a = 0  # Lower limit
b = 2  # Upper limit
n = 6  # Number of intervals (must be even)

integral_value = simpsons_rule(a, b, n)
print(f"The approximate value of the integral is: {integral_value}")
