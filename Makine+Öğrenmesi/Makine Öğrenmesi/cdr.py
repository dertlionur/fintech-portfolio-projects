import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#veriyi hazırlama

data = {
    'Ev_Buyuklugu':[120, 250, 175, 300, 220],
    'Oda_Sayisi': [3,5,4,6,4],
    'Fiyat':[2400000, 5000000, 3500000, 6000000, 4400000]
}


df = pd.DataFrame(data) # veriyi df çevirme

X = df[['Ev_Buyuklugu','Oda_Sayisi']] #girdi
y = df['Fiyat'] # cıktı
#modeli eğitme
X_train, X_test, y_train, y_test = train_test_split(X,y , test_size=0.2, random_state=42)

#modeli oluştur

model = LinearRegression()
model.fit(X_train,  y_train)

# y_pred = model.predict(X_test)
# #hata ne kadar küçükse tahmin o kadar iyidir.
# mse = mean_squared_error(y_test , y_pred)
# rmse = np.sqrt(mse)
# print(f"Ortalama Kare Hatası (MSE){rmse}")

# ev_buyuklugu = float(input("Lütfen evin büyüklüğünü (m²) girin :"))

# tahmini_fiyat = model.predict([[ev_buyuklugu]])

# print(f"Bu evin tahmini fiyatı : {tahmini_fiyat[0]:.2f} TL")

ev_buyuklugu = float(input("Lütfen evin büyüklüğünü (m²) girin: "))
oda_sayisi = int(input("Lütfen oda sayısını girin: "))

tahmini_fiyat = model.predict([[ev_buyuklugu, oda_sayisi]])
print(f'Bu evin tahmini fiyatı : {tahmini_fiyat[0]:.3f} TL')
