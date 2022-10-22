import pandas as pd

df = pd.read_json('data.json')

print(df.to_string())


// to_string prints the entire dataset
