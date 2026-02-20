import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
gun_sayisi = 365
baslangic_fiyat = 100

gunluk_degisimler = np.random.normal(loc=0.0005, scale=0.02, size=gun_sayisi)
fiyatlar = baslangic_fiyat * (1 + gunluk_degisimler).cumprod()
print(f"İlk Fiyat: {fiyatlar[5]}")

tarihler = pd.date_range(start="2026-02-14", periods=gun_sayisi)
df = pd.DataFrame(data={"Fiyat":fiyatlar}, index=tarihler)

df["SMA_20"] = df["Fiyat"].rolling(window=20).mean()
df["SMA_50"] = df["Fiyat"].rolling(window=50).mean()

# print(df.tail())

plt.figure(figsize=(12,6))
plt.plot(df.index, df["Fiyat"], label="Hisse Fiyatı", color="black", alpha=0.5)
plt.plot(df.index, df["SMA_20"], label="SMA 20 (Hızlı)", color="green", linewidth=2)
plt.plot(df.index, df["SMA_50"], label="SMA 50 (Yavaş)", color="red", linewidth=2, linestyle="--")

plt.title("Sanal Hisse Analizi Ve Golden Cross Analizi")
plt.xlabel("Tarih")
plt.ylabel("Fiyat (TL)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()