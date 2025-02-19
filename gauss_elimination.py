import numpy as np

def gaussian_elimination(A, b):
    A= np.array(A, dtype=float)
    b= np.array(b, dtype=float)
    n= len(b)
    
    for i in range(n):
        max_row = i + np.argmax(abs(A[i:n, i]))
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[i], b[max_row] = b[max_row], b[i]
            
        for j in range(i+1, n):
            factor = A[j, i]/A[i, i]
            A[j, i:] -= factor*A[i,i:]
            b[j] -= factor*b[i]
            
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i]- np.dot(A[i, i+1:], x[i + 1 :])) / A[i,i]
        
    return x

n = int(input("Enter the number of variables: "))

print("Enter the coefficient matrix (A) row wise: ")
A = [list(map(float, input().split())) for _ in range(n)]

print("Enter the constant terms (b): ")  
b = [float(input()) for _ in range(n)]

solution = gaussian_elimination(A,b)    
print("Solution : ", solution)  
    