import pandas as pd

veri = {"Islemler": [-100, -20, 50, -30, 10]}
df = pd.DataFrame(veri)

toplam = df["Islemler"].sum()
en_buyuk = df["Islemler"].max()
adet = df["Islemler"].count()

print(f"Toplam Kar: {toplam}")
print(f"En Büyük Kazanç: {en_buyuk}")
print(f"İşlem Sayısı: {adet}")

