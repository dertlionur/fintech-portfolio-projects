import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import MetaTrader5 as mt5

data = {
    "Metrekare":[80, 120, 100, 150, 200, 90, 85, 130, 160, 110],
    "Oda_Sayisi": [2, 3, 2, 4, 5, 2, 2, 3, 4, 3],
    "Bina_Yasi": [10, 5, 20, 2, 1, 15, 8, 4, 3, 12],
    "Fiyat": [1500, 2800, 1400, 4000, 6000, 1600, 1550, 3000, 4500, 2200]
}

df = pd.DataFrame(data)
print("----Veri Setimiz----")
print(df.head())

x = df.drop("Fiyat", axis=1)
y = df["Fiyat"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)
ornek_ev = pd.DataFrame([[170,5,0]], columns=["Metrekare", "Oda_Sayisi", "Bina_Yasi"])
tahmin = model.predict(ornek_ev)
print("-"*30)
print(f"Tahmini Fiyat: {tahmin[0]:.2f} Bin TL")
print("-"*30)
basari = model.score(x_test, y_test)
print(f"Modelin Güvenilirliği %{basari*100:.1f}")

print(f"MetaTrader5 kütüphanesi başarıyla yüklü sürüm: {mt5.__version__}")
