import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df=pd.read_csv("DS/covid_19_clean_complete.csv")
print (df)

# count_null=df.isnull().sum()
# print(count_null)
# newdf=df.fillna('NOT Pre')
# print(newdf)
newdf=df.dropna()
print("all actuals :",newdf)

filtereddf=df[(df["Country/Region"]=="India") | (df["Country/Region"]=="Armenia")]
print(filtereddf)

originaldata=newdf.drop_duplicates()

print(originaldata)
print("groupby")
data=df.groupby("Country/Region")["Confirmed"]
print(data)
# india_data=df.groupby("Country/Region")["Confirmed"].sum().reset_index()
# # print("sum of groupby",india_data)

# sum of confirmed cases and group by country
top_countries=df.groupby("Country/Region")["Confirmed"].sum().nlargest(12)
print(top_countries)