import pandas as pd

# Load the dataset
columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
car_data = pd.read_csv("datasets/car.data", header=None, names=columns)

# Display the first few rows
print("First few rows of the Car Evaluation dataset:")
print(car_data.head())

# Check for null values and basic information
print("\nDataset Info:")
print(car_data.info())

print("\nSummary Statistics:")
print(car_data.describe(include='all'))

import matplotlib.pyplot as plt
import seaborn as sns

# Encode categorical variables for analysis
car_data["buying"] = car_data["buying"].map({"vhigh": 3, "high": 2, "med": 1, "low": 0})
car_data["maint"] = car_data["maint"].map({"vhigh": 3, "high": 2, "med": 1, "low": 0})
car_data["doors"] = car_data["doors"].map({"2": 2, "3": 3, "4": 4, "5more": 5})
car_data["persons"] = car_data["persons"].map({"2": 2, "4": 4, "more": 5})
car_data["lug_boot"] = car_data["lug_boot"].map({"small": 0, "med": 1, "big": 2})
car_data["safety"] = car_data["safety"].map({"low": 0, "med": 1, "high": 2})

# Distribution of car evaluations
plt.figure(figsize=(8, 5))
sns.countplot(x='class', data=car_data, palette="viridis")
plt.title("Distribution of Car Evaluations")
plt.show()

# Analyze relationship between safety and car evaluation
plt.figure(figsize=(10, 6))
sns.boxplot(x='class', y='safety', data=car_data, palette="pastel")
plt.title("Car Evaluation vs. Safety Level")
plt.show()

# Heatmap for correlation between features
plt.figure(figsize=(10, 8))
sns.heatmap(car_data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Car Features")
plt.show()

