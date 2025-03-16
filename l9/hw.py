import pandas as pd
import matplotlib.pyplot as plt

# Load the COVID-19 data from the CSV file
data = pd.read_csv('datasets/covid.csv')  # Replace 'covid_data.csv' with your file path

# Filter data for the USA and India

usa_data = data[data['Country_Region'] == 'US']  # Replace 'Country_Region' with the appropriate column name for country in your dataset
india_data = data[data['Country_Region'] == 'India']  # Replace 'Country_Region' with the appropriate column name for country in your dataset


# Get top states in terms of total cases and deaths for USA
top_usa_cases = usa_data.groupby('Province_State')['Confirmed'].max().nlargest(5)
top_usa_deaths = usa_data.groupby('Province_State')['Deaths'].max().nlargest(5)

# Get top states in terms of total cases and deaths for India
top_india_cases = india_data.groupby('Province_State')['Confirmed'].max().nlargest(5)
top_india_deaths = india_data.groupby('Province_State')['Deaths'].max().nlargest(5)
print(top_usa_cases)
print(top_usa_deaths)
print(top_india_cases)
print(top_india_deaths)

# Plotting the data for the USA
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
top_usa_cases.plot(kind='bar', color='skyblue')
plt.title('Top States in USA (Total Cases)')
plt.xlabel('State')
plt.ylabel('Total Cases')

plt.subplot(1, 2, 2)
top_usa_deaths.plot(kind='bar', color='salmon')
plt.title('Top States in USA (Total Deaths)')
plt.xlabel('State')
plt.ylabel('Total Deaths')

plt.tight_layout()
plt.show()

# Plotting the data for India
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
top_india_cases.plot(kind='bar', color='lightgreen')
plt.title('Top States in India (Total Cases)')
plt.xlabel('State')
plt.ylabel('Total Cases')

plt.subplot(1, 2, 2)
top_india_deaths.plot(kind='bar', color='coral')
plt.title('Top States in India (Total Deaths)')
plt.xlabel('State')
plt.ylabel('Total Deaths')

plt.tight_layout()
plt.show()