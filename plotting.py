import pandas as pandas
import matplotlib.pyplot as plt
 df = pd.read_csv('data.csv')

df.plot()

 plt.show()

 #Scatter Plot

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show() 

#Histogram 
df["Duration"].plot(kind = 'hist')