import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
# Read the CSV file
file_path = 'datasets/WHO-COVID-19-global-data.csv'  # Replace with your file path
data = pd.read_csv(file_path)
data['DateReported'] = pd.to_datetime(data['DateReported']) 
# Function to plot daily cases and deaths for a specific country
def plot_country_data(country_name):
    country_data = data[data['Country'] == country_name]

    if country_data.empty:
        print("Data for the specified country not found.")
        return

    country_data = country_data.iloc[::-1]  # Reverse the DataFrame to have earliest dates first
    dates = country_data['DateReported']
    daily_cases = country_data['New_cases']
    daily_deaths = country_data['New_deaths']

    # Plotting daily cases
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(dates, daily_cases, marker='o', linestyle='-', color='b')
    plt.title(f'Daily COVID-19 Cases in {country_name}')
    plt.xlabel('Date')
    plt.ylabel('Daily Cases')
    plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)
    plt.grid(True)

    # Plotting daily deaths
    plt.subplot(2, 1, 2)
    plt.plot(dates, daily_deaths, marker='o', linestyle='-', color='r')
    plt.title(f'Daily COVID-19 Deaths in {country_name}')
    plt.xlabel('Date')
    plt.ylabel('Daily Deaths')
    plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Input the country name
country_input = input("Enter the country name: ")

# Plot the data for the specified country
plot_country_data(country_input)