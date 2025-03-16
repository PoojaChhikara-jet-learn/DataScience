import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y1 = [1, 2, 3, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [3, 4, 5, 6, 7]

plt.stackplot(x, y1, y2, y3, labels=['A', 'B', 'C'], colors=['red', 'blue', 'green'])
plt.title('Stack Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc='upper left')
plt.show()