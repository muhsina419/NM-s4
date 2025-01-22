def newton_raphson(f, f_dash, x0, tolerance=1e-7, max_iterations=100):
    x = x0
    for i in range(max_iterations):
        fx = f(x)
        fpx = f_dash(x)
        
        if fpx == 0:
            print(f"Derivative is zero, No solution found at iteration {i}")
            return None
        
        x_new = x - fx / fpx

        if abs(x_new - x) < tolerance:
            print(f"Converged to root {x_new} in {i+1} iterations")
            return x_new
        
        x = x_new

    print("Maximum iterations reached. Method did not converge.")
    return None

if __name__ == "__main__":
    from sympy import sympify, diff, symbols

    x = symbols('x')
    funct_expr = input("Enter the function f(x): ")
    f = sympify(funct_expr)
    f_dash = diff(f, x)

    # Create lambda functions for f(x) and f'(x)
    f_lambda = lambda x_value: float(f.subs(x, x_value))
    f_dash_lambda = lambda x_value: float(f_dash.subs(x, x_value))

    # Take initial guess as input from the user
    x0 = float(input("Enter the initial guess x0: "))

    # Call the Newton-Raphson method
    root = newton_raphson(f_lambda, f_dash_lambda, x0)

    if root is not None:
        print(f"\nAppropriate root: {root}")
