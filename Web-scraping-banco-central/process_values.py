import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 
print('\n')
print('min value:', df['price'].min()) 
print('max value:', df['price'].max()) 
print('mean value:', df['price'].mean()) 