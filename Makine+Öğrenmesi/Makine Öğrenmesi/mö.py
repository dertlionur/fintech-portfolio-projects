import pandas as pd
from pandas.core.common import random_state
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#veriyi hazırlama

data = {
    "Ev_Buyuklugu":[120,250,175,300,220],
    "Oda_Sayisi":[3,5,4,6,4],
    "Fiyat":[2400000,5000000,3500000,6000000,4400000]
}

df = pd.DataFrame(data) #veriyi df çevirme

x = df[["Ev_Buyuklugu", "Oda_Sayisi"]]
y = df["Fiyat"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#modeli oluştur

model = LinearRegression()
model.fit(x_train, y_train)

# y_pred = model.predict(x_test)
# 
#hata ne kadar küçükse tahmin o kadar iyidir


# ev_buyuklugu = float(input("Lütfen Evin Büyüklüğünü (m²) Girin: "))
# tahmini_fiyat = model.predict([[ev_buyuklugu]])
# print(f"Bu Evin Tahmini Fiyatı: {tahmini_fiyat[0]:.2f}TL")

ev_buyuklugu = float(input("Lütfen Evin Büyüklüğünü (m²) Girin: "))
oda_sayisi = int(input("Lütfen Oda Sayısını Girin: "))
tahmini_fiyat = model.predict([[ev_buyuklugu, oda_sayisi]])
print(f"Bu Evin Tahmini Fiyatı: {tahmini_fiyat[0]:.2f}TL")

