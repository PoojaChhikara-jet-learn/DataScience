import numpy as np
import matplotlib.pyplot as plt

# Generate data for plots
# Sine and Cosine Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)  # Sine wave data
y2 = np.cos(x)  # Cosine wave data

# Histogram Data
data = np.random.randn(1000)  # Random data for histogram

# Pie Chart Data
labels = ['Category A', 'Category B', 'Category C']
sizes = [40, 30, 30]

# Scatter Plot Data
scatter_x = np.random.rand(50)  # Random x values for scatter
scatter_y = np.random.rand(50)  # Random y values for scatter

# Create sub-plots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# First plot: Sine Wave
axs[0, 0].plot(x, y1, color='blue')
axs[0, 0].set_title('Sine Wave')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')
axs[0, 0].grid()

# Second plot: Histogram
axs[0, 1].hist(data, bins=30, color='purple', alpha=0.7)
axs[0, 1].set_title('Histogram')
axs[0, 1].set_xlabel('Value')
axs[0, 1].set_ylabel('Frequency')

# Third plot: Pie Chart
axs[1, 0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
axs[1, 0].set_title('Pie Chart')

# Fourth plot: Scatter Plot
axs[1, 1].scatter(scatter_x, scatter_y, color='red', alpha=0.5)
axs[1, 1].set_title('Scatter Plot')
axs[1, 1].set_xlabel('X-axis')
axs[1, 1].set_ylabel('Y-axis')
axs[1, 1].grid()

# Adjust layout for better appearance
plt.tight_layout()
plt.show()
