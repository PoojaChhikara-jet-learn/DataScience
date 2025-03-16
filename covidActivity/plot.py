import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df=pd.read_csv("DS/covid_19_clean_complete.csv")
print (df)

print(df.head())
print("columns")
print(df.columns)
print(df.values)
df.rename(columns={
    'Province/State': 'State',
    'Country/Region': 'Country'
}, inplace=True)
print(df.columns)

# making sure of all required columns in dataset
required_columns = ['Country', 'Date', 'Confirmed', 'Deaths', 'Recovered']

missing_columns = [col for col in required_columns if col not in df.columns]


if not missing_columns:
    print("All required columns are present.")
else:
    print("Missing columns:", missing_columns)


# india data
india_data = df[df['Country'] == 'India']
print(india_data)

daily_totals = india_data.groupby('Date').agg({
    'Confirmed': 'sum',
    'Deaths': 'sum',
    'Recovered': 'sum',
}).reset_index()
print("daily totals", daily_totals)

# grouping /filtering
daily_totals['New_Confirmed'] = daily_totals.groupby('Date')['Confirmed'].diff().fillna(0)
daily_totals['New_Deaths'] = daily_totals.groupby('Date')['Deaths'].diff().fillna(0)
daily_totals['New_Recovered'] = daily_totals.groupby('Date')['Recovered'].diff().fillna(0)

import matplotlib.pyplot as plt
plt.figure(figsize=(14, 7))

# Confirmed Cases
plt.subplot(1, 3, 1)
plt.plot(daily_totals['Date'], daily_totals['Confirmed'], color='blue', label='Confirmed')
plt.title('COVID-19 Trends in the India')
plt.ylabel('Number of Cases')


# Deaths
plt.subplot(1, 3, 2)
plt.plot(daily_totals['Date'], daily_totals['Deaths'], color='red', label='Deaths')
plt.ylabel('Number of Deaths')


# Recovered
plt.subplot(1, 3, 3)
plt.plot(daily_totals['Date'], daily_totals['Recovered'], color='green', label='Recovered')
plt.ylabel('Number of Recoveries')
plt.xticks(rotation=90)
plt.xlabel('Date',rotation=90)


plt.show()

# # top 10 countries
country_totals = df.groupby('Country').agg({'Confirmed': 'sum'}).reset_index()
print(country_totals)
top_10_countries = country_totals.sort_values(by='Confirmed', ascending=False).head(10)
print(top_10_countries)


# plt.figure(figsize=(12, 6))
# plt.bar(top_10_countries['Country'], top_10_countries['Confirmed'], color='skyblue')
# plt.title('Top 10 Countries with the Highest Confirmed COVID-19 Cases')
# plt.xlabel('Country')
# plt.ylabel('Total Confirmed Cases')
# plt.xticks(rotation=45)

# plt.show()


# # #country_data=daily_totals[daily_totals['Country'] == "India"]
# plt.figure(figsize=(14, 7))

# plt.plot(daily_totals['Date'], daily_totals['New_Confirmed'], label='Daily New Confirmed', color='blue')
# plt.plot(daily_totals['Date'], daily_totals['New_Deaths'], label='Daily New Deaths', color='red')
# plt.plot(daily_totals['Date'], daily_totals['New_Recovered'], label='Daily New Recovered', color='green')

# plt.title(f'Daily New COVID-19 Cases, Deaths, and Recoveries in india')
# plt.xlabel('Date')
# plt.ylabel('Count')
# plt.xticks(rotation=45)
# plt.show()