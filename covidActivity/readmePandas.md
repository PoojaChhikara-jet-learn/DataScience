# for pandas we have
 df.isnull()/df.isna()/df.notna()/df.notnull()/.any()/.sum()
 df.dropna()<!--(how="all",axis=1,col_name=['colname'])  -->
 missing=["NA","n/a","N/A","null"]
 df.isnull()
 df.fillna(val)
 df['column_name'].fillna(df['column_name'].mean(), inplace=True)
 interpolate(mean of forward and backward)=df.interpolated()
forward fill-df_filled = df.fillna(method='ffill')
backward fill=df_filled = df.fillna(method='bfill')
