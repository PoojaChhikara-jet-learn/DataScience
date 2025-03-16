import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)

plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
