import numpy as np

def calculate_linear(a, b):
    # Linear equation: y = ax + b
    x_values = np.arange(0, 11)  # x from 0 to 10
    y_values = a * x_values + b
    return y_values

def calculate_quadratic(a, b, c):
    # Quadratic equation: y = ax^2 + bx + c
    x_values = np.arange(0, 11)  # x from 0 to 10
    y_values = a * x_values**2 + b * x_values + c
    return y_values

def main():
    print("Choose the type of equation:")
    print("1. Linear (y = ax + b)")
    print("2. Quadratic (y = ax^2 + bx + c)")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        a = float(input("Enter the coefficient a for the linear equation: "))
        b = float(input("Enter the coefficient b for the linear equation: "))
        
        y_values = calculate_linear(a, b)
        print("\nOutput values for Linear Equation (y = {}x + {}):".format(a, b))
        
    elif choice == '2':
        a = float(input("Enter the coefficient a for the quadratic equation: "))
        b = float(input("Enter the coefficient b for the quadratic equation: "))
        c = float(input("Enter the coefficient c for the quadratic equation: "))
        
        y_values = calculate_quadratic(a, b, c)
        print("\nOutput values for Quadratic Equation (y = {}x^2 + {}x + {}):".format(a, b, c))
        
    else:
        print("Invalid choice. Please select 1 or 2.")
        return
    
    # Display the results
    for x, y in zip(range(11), y_values):
        print("x = {}, y = {}".format(x, y))

    print(y_values,int)

if __name__ == "__main__":
    main()
