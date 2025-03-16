import pandas as pd
import matplotlib.pyplot as plt
# Sample DataFrame (replace this with your actual DataFrame)
data = {'Pclass': [1, 1, 2, 3, 1, 2, 3, 2, 1, 3]}
df = pd.DataFrame(data)

# Count of passengers in different Pclass
pclass_counts = df['Pclass'].value_counts()

# Plotting
plt.bar(pclass_counts.index, pclass_counts.values)
plt.title("Count of Passengers in Different Pclass")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.xticks([1, 2, 3])  # Specify the x-ticks
plt.show()
