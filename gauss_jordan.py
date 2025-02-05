import numpy as np

def gauss_jordan(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)

    # Augmented matrix [A | b]
    aug_matrix = np.hstack((A, b))
    n = len(b)

    for i in range(n):
        # Make the diagonal element 1 (pivot)
        pivot = aug_matrix[i, i]
        if pivot == 0:
            raise ValueError("Zero pivot encountered, solution may not exist or be unique.")
        
        aug_matrix[i] = aug_matrix[i] / pivot

        # Make other elements in the column 0
        for j in range(n):
            if i != j:
                factor = aug_matrix[j, i]
                aug_matrix[j] -= factor * aug_matrix[i]

    return aug_matrix[:, -1]  # Extract solution vector

A=[[1,1,1],
   [2,-3,4],
   [3,4,5]]

b=[9,13,40]

solution = gauss_jordan(A,b)
print("Solution :",solution)