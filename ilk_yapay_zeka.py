import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x_alis = np.array([[10], [20], [30], [40], [50]])
y_satis = np.array([12, 25, 32, 48, 52])

model = LinearRegression()
model.fit(x_alis, y_satis)

print("Model Başarıyla Eğitildi! Stratejin Çözüldü")

yeni_alis = np.array([[60]])
tahmin = model.predict(yeni_alis)
print(f"60 TL den aldıysan Hedef satış fiyatın: {tahmin[0]:.2f} TL olmalı")

plt.figure(figsize=(10, 6))
plt.scatter(x_alis, y_satis, color="blue", label="Gerçek İşlemler")
plt.plot(x_alis, model.predict(x_alis), color="red", linewidth=2, label="Yapay Zeka Trendi")
plt.scatter(yeni_alis, tahmin, color="green", s=150, zorder=5, label="60TL Tahmini")

plt.title("Alış - Satış Stratejisi Analizi")
plt.xlabel("Alış Fiyatı")
plt.ylabel("Satış Fiyatı")
plt.legend()
plt.grid(True)
plt.show()