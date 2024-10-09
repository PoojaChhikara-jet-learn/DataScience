import numpy as np

def get_matrix_input(matrix_number):
    # Get the number of rows and columns for the matrix
    rows = int(input(f"Enter the number of rows for Matrix {matrix_number}: "))
    cols = int(input(f"Enter the number of columns for Matrix {matrix_number}: "))
    
    # Initialize an empty list to hold the matrix
    matrix = []
    
    print(f"Enter the elements of Matrix {matrix_number} row by row:")
    for i in range(rows):
        # Get the row input from the user
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        # Check if the number of elements matches the specified column count
        if len(row) != cols:
            print(f"Error: You must enter exactly {cols} elements for row {i + 1}.")
            return None  # Exit if input is invalid
        matrix.append(row)  # Add the row to the matrix
    
    return np.array(matrix)  # Convert the list to a NumPy array

def main():
    print("Matrix Operations Program")
    
    # Get the first matrix from the user
    matrix1 = get_matrix_input(1)
    if matrix1 is None:
        return  # Exit if there was an error
    
    # Get the second matrix from the user
    matrix2 = get_matrix_input(2)
    if matrix2 is None:
        return  # Exit if there was an error
    
    # Check if the matrices have the same shape
    if matrix1.shape != matrix2.shape:
        print("Error: Matrices must have the same size for addition or subtraction.")
        return
    
    # Ask the user for the desired operation
    operation = input("Choose operation (add or subtract): ").strip().lower()
    
    # Perform the chosen operation
    if operation == "add":
        result = matrix1 + matrix2
        print("Result of Addition:\n", result)
    elif operation == "subtract":
        result = matrix1 - matrix2
        print("Result of Subtraction:\n", result)
    else:
        print("Error: Invalid operation. Please choose 'add' or 'subtract'.")

# Start the program
if __name__ == "__main__":
    main()
