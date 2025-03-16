import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Create a bar plot
plt.bar(categories, values, color='orange')
plt.title('Simple Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
