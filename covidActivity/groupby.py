import pandas as pd

# Sample data for India and USA
data = {
    'Date': ['2020-10-01', '2020-10-01', '2020-10-02', '2020-10-02'],
    'Confirmed': [100, 200, 150, 300],
    'Deaths': [5, 10, 8, 12],
    'Country': ['India', 'India', 'USA', 'USA'],
    'Recovered': [50, 75, 70, 100],
}
india_data = pd.DataFrame(data)

# Convert 'Date' to datetime
india_data['Date'] = pd.to_datetime(india_data['Date'])

# Calculate new confirmed cases before aggregation
india_data['New_Confirmed'] = india_data.groupby('Country')['Confirmed'].diff().fillna(0)

# Group by date and country and aggregate totals
daily_totals = india_data.groupby(['Date', 'Country']).agg({
    'Confirmed': 'sum',
    'Deaths': 'sum',
    'Recovered': 'sum',
    'New_Confirmed': 'sum'  # Include new confirmed cases in the aggregation
}).reset_index()

# Display the resulting DataFrame
print(daily_totals)


