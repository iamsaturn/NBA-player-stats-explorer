import pandas as pd

df = pd.read_csv('./data/nbadata.csv')

print(df.info())
print(df.columns.tolist())

print('FG% Null:')

print(df.loc[:, 'FG%'].isna().sum())

print('3P% Null: ')

print(df.loc[:, '3P%'].isna().sum())

print('FT Null:')

print(df.loc[:, 'FT%'].isna().sum())

print('+/-% Null:')

print(df.loc[:, '+/-'].isna().sum())


print(df.loc[:, 'Player'].nunique())
