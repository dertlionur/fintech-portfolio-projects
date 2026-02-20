import pandas as pd

# s = pd.Series([10,20,30,40], index=["a","b","c","d"])

# print(s)

data = {
    'Fiyat':[45,85,45,25],
    'Satış Adedi': [5,6,7,2],
    'Kategori': ['Roman','Bilim','Çocuk','Tarih']
}

df = pd.DataFrame(data)
# print(df)
# print(df.head())
# print(df.info())
# print(df.describe())

# print(df[['Fiyat','Kategori']])
# filtre = df[df['Fiyat'] > 50]
# print(filtre)

df['Toplam Gelir'] = df['Fiyat'] * df['Satış Adedi']

df = df.drop('Kategori', axis=1)

print(df)
