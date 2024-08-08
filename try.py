import pandas as pd

df = pd.read_csv('planet_data.csv')

print(df['x'][2])