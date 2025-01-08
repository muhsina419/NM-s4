# Function to add two matrices
def add_matrices(matrix1, matrix2):
    # Check if the matrices are of the same size
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must be of the same size")

    # Initialize a result matrix with zeros
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Add corresponding elements of the matrices
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

# Function to take matrix input from the user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of the {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        while len(row) != cols:
            print(f"Row should have {cols} elements. Please enter the row again.")
            row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix.append(row)
    return matrix

# Input number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Taking input for both matrices
print("Enter the first matrix:")
matrix1 = input_matrix(rows, cols)

print("Enter the second matrix:")
matrix2 = input_matrix(rows, cols)

# Adding the matrices
try:
    result_matrix = add_matrices(matrix1, matrix2)

    # Printing the result
    print("Resultant Matrix:")
    for row in result_matrix:
        print(row)
except ValueError as e:
    print(e)
