import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

# Multiple plots
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='Sine Wave', color='blue')
plt.plot(x, y2, label='Cosine Wave', color='orange')

plt.title('Sine and Cosine Waves')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
