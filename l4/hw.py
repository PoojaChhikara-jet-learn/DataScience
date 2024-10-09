import pandas as pd

titanic_data = pd.read_csv('DS/l4/titanic.csv')
# Mean fare of passengers with respect to sex and Pclass
# unstack is put data into columns
mean_fare = titanic_data.groupby(['Sex', 'Pclass'])['Fare'].mean().unstack()
print("Mean Fare of Passengers with respect to Sex and Pclass:")
print(mean_fare)

# Filter the dataset for passengers who died
deceased_passengers = titanic_data[titanic_data['Survived'] == 0]

# Calculate the mean age of deceased passengers by sex
mean_age_deceased = deceased_passengers.groupby('Sex')['Age'].mean()
median_age_deceased = deceased_passengers.groupby('Sex')['Age'].median()

print("\nMean Age of Deceased Passengers by Sex:")
print(mean_age_deceased)

print("\nMedian Age of Deceased Passengers by Sex:")
print(median_age_deceased)


