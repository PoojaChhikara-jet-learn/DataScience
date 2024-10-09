import numpy as np

def get_matrix_input(matrix_number):
    rows = int(input(f"Enter the number of rows for Matrix {matrix_number}: "))
    cols = int(input(f"Enter the number of columns for Matrix {matrix_number}: "))
    print(f"Enter the elements of Matrix {matrix_number} (row-wise):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Error: You must enter exactly {cols} elements for row {i + 1}.")
            return None
        matrix.append(row)
    return np.array(matrix)

def main():
    print("Matrix Operations Program")
    
    # Get input for the first matrix
    matrix1 = get_matrix_input(1)
    if matrix1 is None:
        return

    # Get input for the second matrix
    matrix2 = get_matrix_input(2)
    if matrix2 is None:
        return

    # Ensure matrices have the same shape for addition and subtraction
    if matrix1.shape != matrix2.shape:
        print("Error: Matrices must have the same shape for addition or subtraction.")
        return

    # Get operation choice from user
    operation = input("Choose operation (add or subtract): ").strip().lower()
    
    if operation == "add":
        result = matrix1 + matrix2
        print("Result of Addition:\n", result)
    elif operation == "subtract":
        result = matrix1 - matrix2
        print("Result of Subtraction:\n", result)
    else:
        print("Error: Invalid operation. Please choose 'add' or 'subtract'.")

if __name__ == "__main__":
    main()
