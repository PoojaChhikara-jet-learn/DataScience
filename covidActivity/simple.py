import pandas as pd

# Sample data for different countries
data = {
    'Date': ['2020-10-01', '2020-10-02', '2020-10-01', '2020-10-02'],
    'Country': ['India', 'India', 'USA', 'USA'],
    'Confirmed': [100, 150, 200, 250]
}
daily_totals = pd.DataFrame(data)

# Convert 'Date' to datetime
daily_totals['Date'] = pd.to_datetime(daily_totals['Date'])

# Calculate new confirmed cases
daily_totals['New_Confirmed'] = daily_totals.groupby('Country')['Confirmed'].diff().fillna(0)

print(daily_totals)
