import pandas as pd


data = {

    "Fiyat":[45,564,34,22,11],
    "Satılan Hisse Adedi":[100,50,200,300,1000],
    "Kategori":["IHLAS","THY","FORD","SAHOL","KOÇ"]
}

df = pd.DataFrame(data)

# print(df)
# print(df.info())

filtre = df[df["Fiyat"]>30]
print(filtre)