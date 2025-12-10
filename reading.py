import pandas as pd

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('ecommerce_estatistica.csv')

print(df.head())
print("Ver as informações, se possui nulos, quantos cada possui, o tipo\n", df.info())
print("Quantos possui, min/max etc: \n", df.describe())
print(df[['Marca', 'Marca_Cod']].drop_duplicates().sort_values('Marca_Cod'))