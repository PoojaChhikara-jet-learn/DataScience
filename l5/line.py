import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y)
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# with features like markers, colors, grid lines, and legends
plt.plot(x, y, marker='o', color='b', linestyle='-', linewidth=2, markersize=8, label='Data Line')
plt.title('Enhanced Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()
plt.show()


# Define the linear equation parameters
m = 2  # slope
b = 1  # intercept

# Generate x values
x = range(-10, 11)
y = [m * xi + b for xi in x]

# Create the plot
plt.plot(x, y, color='green')
plt.title('Plot of Linear Equation y = 2x + 1')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.show()


