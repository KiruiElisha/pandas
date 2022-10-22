import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()////removes empty rows 

// dropna() method returns a new DataFrame, and will not change the original.

print(new_df.to_string())




import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)// If you want to change the original DataFrame, use the inplace = True argument

print(df.to_string())


// Replace Empty Values


import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True) 



//Replacing Empty fields using Mean

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)