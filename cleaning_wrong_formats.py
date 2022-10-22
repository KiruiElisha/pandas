#Cleaning date formats 
import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())


# Removing NULL values

df.dropna(subset=['Date'], inplace = True)


for x in df.index:
  if df.loc[x, "Duration"] > 120:#Loop through all values in the "Duration" column.
    df.loc[x, "Duration"] = 120 #If the value is higher than 120, set it to 120:


# Removing Rows


for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
