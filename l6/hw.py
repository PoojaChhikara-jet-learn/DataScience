import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset (adjust the path as necessary)
# Example: df = pd.read_csv('path_to_titanic.csv')
df = pd.read_csv('DS/l6/titanic.csv')

# 1. Total number of men and women
gender_counts = df['Sex'].value_counts()

# 2. Average fare of men and women
average_fare = df.groupby('Sex')['Fare'].mean()

# 3. Count of passengers by class
class_counts = df['Pclass'].value_counts()

# Create bar graphs
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Bar graph for total number of men and women
axs[0].bar(gender_counts.index, gender_counts.values, color=['blue', 'pink'])
axs[0].set_title('Total Number of Men and Women on the Titanic')
axs[0].set_xlabel('Gender')
axs[0].set_ylabel('Number of Passengers')

# Bar graph for average fare of men and women
axs[1].bar(average_fare.index, average_fare.values, color=['blue', 'pink'])
axs[1].set_title('Average Fare of Men and Women on the Titanic')
axs[1].set_xlabel('Gender')
axs[1].set_ylabel('Average Fare')

plt.tight_layout()
plt.show()

# Create a pie chart for the number of people in different classes
plt.figure(figsize=(8, 8))
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Distribution of Passengers by Class')
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
plt.show()
