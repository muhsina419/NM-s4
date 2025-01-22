def fixed_point(g, x0, tolerance=1e-7, max_iterations=100):
    x = x0
    for i in range(max_iterations):
        x_new = g(x)
        
        if abs(x_new - x) < tolerance:
            print(f"Converged to root {x_new} in {i+1} iterations")
            return x_new
        
        x = x_new

    print("Maximum iterations reached. Method did not converge.")
    return None

if __name__ == "__main__":
    from sympy import sympify, symbols

    x = symbols('x')
    funct_expr = input("Enter the function g(x): ")
    g = sympify(funct_expr)

    # Create lambda functions for f(x) and f'(x)
    g_lambda = lambda x_value: float(g.subs(x, x_value))

    # Take initial guess as input from the user
    x0 = float(input("Enter the initial guess x0: "))

    # Call the Newton-Raphson method
    solution = fixed_point(g_lambda, x0)

    if solution is not None:
        print(f"\n Solution found: {solution}")
