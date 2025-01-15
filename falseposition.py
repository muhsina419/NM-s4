def find_interval(funct , start=-100,end=100,step=1):
    x=start
    while x<end:
        if funct(x)*funct(x+step)< 0:
            return x , x+step
        x+=step
    return None

def false_position(funct,a,b,tol=1e-6,max_iter=100):
    if funct(a)*funct(b) >= 0:
        raise ValueError("The function must have opposite signs at a and b")
    print(f"{'iteration':<10}{'a':<10}{'b':<10}{'c':<10}{'f(c)':<10}")
    for iteration in range (1, max_iter+1):
        c=(a*funct(b)-b*funct(a))/(funct(b)-funct(a))
        fc=funct(c)
        print(f"{'iteration':<10}{a:<10.6f}{b:<10.6f}{c:<10.6f}{fc:<10.6f}")
        if abs(fc)<tol:
            print("\nRoot found!")
            return c
        if funct(a)*fc < 0:
            b=c
        else:
            a=c
    print("\nMaximum iterations reached. Root may not be accurate.")
    return c
 
if __name__ == "__main__":
    import math
    def f(x):
        return x**3-x*2-10
    interval= find_interval(f)
    if interval:
        a , b = interval
    print("\nInterval found [",a,b,"]")
    root = false_position(f,a,b)
    print(f"\nAppropriate root :{root:.6f}")

