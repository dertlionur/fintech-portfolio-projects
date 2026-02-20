import pandas as pd

# Excel dosyasını oku
df = pd.read_excel('teknolojik_urunler_zamanli.xlsx')

# Tarih sütununu datetime formatına çevirme
df['Tarih'] = pd.to_datetime(df['Tarih'])

# Zaman damgasını indeks olarak ayarlama
df.set_index('Tarih', inplace=True)

# Zaman indeksini sıralama
df = df.sort_index()

# 1. En yüksek satışın yapıldığı ay ve o ayda satılan ürünler
aylik_satis = df.resample('ME')['Satış'].sum()
max_ay = aylik_satis.idxmax()
max_satis_ay = aylik_satis.max()
max_satis_ay_urunler = df[df.index.to_series().between(max_ay - pd.offsets.MonthBegin(1), max_ay)]
print(f"En yüksek satış yapılan ay: {max_ay} - Toplam satış: {max_satis_ay}")
print("O ayda satılan ürünler:")
print(max_satis_ay_urunler[['Ürün Adı', 'Satış']])

# 2. En düşük satışın yapıldığı ay ve o ayda satılan ürünler
min_ay = aylik_satis.idxmin()
min_satis_ay = aylik_satis.min()
min_satis_ay_urunler = df[df.index.to_series().between(min_ay - pd.offsets.MonthBegin(1), min_ay)]
print(f"\nEn düşük satış yapılan ay: {min_ay} - Toplam satış: {min_satis_ay}")
print("O ayda satılan ürünler:")
print(min_satis_ay_urunler[['Ürün Adı', 'Satış']])

# 3. En fazla satış yapılan gün ve o gün satılan ürünler
gunluk_satis = df.resample('D')['Satış'].sum()
max_gun = gunluk_satis.idxmax()
max_satis_gun = gunluk_satis.max()
max_satis_gun_urunler = df.loc[max_gun]
print(f"\nEn fazla satış yapılan gün: {max_gun} - Toplam satış: {max_satis_gun}")
print("O günde satılan ürünler:")
print(max_satis_gun_urunler[['Ürün Adı', 'Satış']])

# 4. Haftalık en fazla satış yapılan hafta ve satılan ürünler
haftalik_satis = df.resample('W')['Satış'].sum()
max_hafta = haftalik_satis.idxmax()
max_satis_hafta = haftalik_satis.max()
max_satis_hafta_urunler = df[df.index.to_series().between(max_hafta - pd.offsets.Week(1), max_hafta)]
print(f"\nEn fazla satış yapılan hafta: {max_hafta} - Toplam satış: {max_satis_hafta}")
print("O haftada satılan ürünler:")
print(max_satis_hafta_urunler[['Ürün Adı', 'Satış']])

# 5. Aylık ortalama satışlar
aylik_ortalama_satis = df.resample('ME')['Satış'].mean()
print("\nAylık ortalama satışlar:")
print(aylik_ortalama_satis)

# 6. Ocak 2024 ile Mart 2024 arasındaki satışlar
belirli_aralik_urunler = df[df.index.to_series().between('2024-01-01', '2024-03-31')]
print("\nOcak 2024 ile Mart 2024 arasında satılan ürünler:")
print(belirli_aralik_urunler[['Ürün Adı', 'Satış']])

# 7. Haftalık ortalama satışlar
haftalik_ortalama_satis = df.resample('W')['Satış'].mean()
# print("\nHaftalık ortalama satışlar:")
# print(haftalik_ortalama_satis)

# 8. En yüksek toplam fiyatın olduğu ay ve o ayda satılan ürünler
aylik_toplam_fiyat = df.resample('ME')['Toplam Fiyat (TL)'].sum()
max_ay_fiyat = aylik_toplam_fiyat.idxmax()
max_fiyat_ay = aylik_toplam_fiyat.max()
max_fiyat_ay_urunler = df[df.index.to_series().between(max_ay_fiyat - pd.offsets.MonthBegin(1), max_ay_fiyat)]
# print(f"\nEn yüksek toplam fiyata sahip ay: {max_ay_fiyat} - Toplam fiyat: {max_fiyat_ay}")
# print("O ayda satılan ürünler:")
# print(max_fiyat_ay_urunler[['Ürün Adı', 'Toplam Fiyat (TL)']])
