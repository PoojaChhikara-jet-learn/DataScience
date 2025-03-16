import pandas as pd
import numpy as np
df=pd.read_csv("DS/covid_19_clean_complete.csv")
print (df)

print(df.head())
print(df.isna())
header=df.columns
data=df.values
print(header)






