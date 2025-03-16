import numpy as np
import matplotlib.pyplot as plt

def plot_linear(m, c):
    x = np.linspace(0, 50, 100)
    y = m * x + c
    plt.plot(x, y, label=f'y = {m}x + {c}', color='blue')
    
def plot_quadratic(a, b, c):
    x = np.linspace(0, 50, 100)
    y = a * x**2 + b * x + c
    plt.plot(x, y, label=f'y = {a}x^2 + {b}x + {c}', color='green')
    
def plot_cubic(a, b, c, d):
    x = np.linspace(0, 50, 100)
    y = a * x**3 + b * x**2 + c * x + d
    plt.plot(x, y, label=f'y = {a}x^3 + {b}x^2 + {c}x + {d}', color='red')

def main():
    print("Select the type of equation to plot:")
    print("1. Linear (y = mx + c)")
    print("2. Quadratic (y = ax^2 + bx + c)")
    print("3. Cubic (y = ax^3 + bx^2 + cx + d) (optional)")
    
    choice = input("Enter the number corresponding to your choice (1/2/3): ")
    
    if choice == '1':
        m = float(input("Enter the slope (m): "))
        c = float(input("Enter the y-intercept (c): "))
        plot_linear(m, c)
        
    elif choice == '2':
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the constant c: "))
        plot_quadratic(a, b, c)
        
    elif choice == '3':
        a = float(input("Enter the coefficient a: "))
        b = float(input("Enter the coefficient b: "))
        c = float(input("Enter the coefficient c: "))
        d = float(input("Enter the constant d: "))
        plot_cubic(a, b, c, d)
        
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
        return
    
    # Configure the plot
    plt.title("Equation Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
