import pandas as pd

titanic_data = pd.read_csv('DS/l4/titanic.csv')
print(titanic_data.head())  # Display the first few rows
print(titanic_data.info())  # Display information about the DataFrame
# Select specific columns
subset = titanic_data[['Name', 'Pclass', 'Survived']]
print(subset.head())

# Select rows based on a condition (e.g., first-class passengers)
first_class_passengers = titanic_data[titanic_data['Pclass'] == 1]
print(first_class_passengers.head())
# Group by 'Pclass' and calculate the mean age
mean_age_by_class = titanic_data.groupby('Pclass')['Age'].mean()
print("\nMean Age by Class:")
print(mean_age_by_class)

# Count the number of survivors by class
survivor_count = titanic_data.groupby('Pclass')['Survived'].value_counts()
print("\nSurvivor Count by Class:")
print(survivor_count)
# Count the number of passengers in each Pclass
pclass_counts = titanic_data['Pclass'].value_counts()
print("\nPassenger Count by Pclass:")
print(pclass_counts)

# Count the number of survivors by gender
gender_survivor_count = titanic_data.groupby('Sex')['Survived'].value_counts()
print("\nSurvivor Count by Gender:")
print(gender_survivor_count)
# Add a new column for family size
titanic_data['FamilySize'] = titanic_data['SibSp'] + titanic_data['Parch'] + 1

# Create a new column indicating whether the passenger is a child (Age < 18)
titanic_data['IsChild'] = titanic_data['Age'] < 18

print("\nUpdated DataFrame with New Columns:")
print(titanic_data[['Name', 'FamilySize', 'IsChild']].head())
# Sort by Age in ascending order
sorted_data = titanic_data.sort_values(by='Age')
print("\nSorted DataFrame by Age:")
print(sorted_data[['Name', 'Age']].head())

# Sort by Survival status and then by Age
sorted_data = titanic_data.sort_values(by=['Survived', 'Age'], ascending=[False, True])
print("\nSorted DataFrame by Survival Status and Age:")
print(sorted_data[['Name', 'Survived', 'Age']].head())

# Group by Pclass and calculate the mean fare and count of survivors
class_summary = titanic_data.groupby('Pclass').agg(
    MeanFare=('Fare', 'mean'),
    SurvivorCount=('Survived', 'sum')
)
print("\nClass Summary with Mean Fare and Survivor Count:")
print(class_summary)
