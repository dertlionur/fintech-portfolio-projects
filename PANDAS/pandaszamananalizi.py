import pandas as pd
import matplotlib.pyplot as plt

#excel dosyasının yolu
df = pd.read_excel('teknolojik_urunler_zamanli.xlsx')

#tarih sütununu datetime formatına çevirme
df['Tarih'] = pd.to_datetime(df['Tarih'])
#indeksleme ( çok önemli )
df.set_index('Tarih', inplace=True)
df = df.sort_index()
# print(df)
# 1. En yüksek satışın yapıldığı ay ve o ayda satılan ürünler
aylik_satis = df.resample('ME')['Satış'].sum()
max_ay = aylik_satis.idxmax()
max_satis_ay = aylik_satis.max()
max_satis_ay_urunler = df[df.index.to_series().between(max_ay - pd.offsets.MonthBegin(1), max_ay)]
# print(f"En yüksek satış yapılan ay: {max_ay} - Toplam satış: {max_satis_ay}")
# print("O ayda satılan ürünler:")
# print(max_satis_ay_urunler[['Ürün Adı', 'Satış']])
#2. En düşük satışın yapıldığı ay ve o ayda satılan ürünler
min_ay = aylik_satis.idxmin()
min_satis_ay = aylik_satis.min()
min_satis_ay_urunler = df[df.index.to_series().between(min_ay - pd.offsets.MonthBegin(1), min_ay)]
# print(f"En Düşük satış yapılan ay: {min_ay} - Toplam satış: {min_satis_ay}")
# print("O ayda satılan ürünler:")
# print(min_satis_ay_urunler[['Ürün Adı', 'Satış']])
# 3. en fazla satış yapılan gün ve o gün satılan ürünler
gunluk_satis = df.resample('D')['Satış'].sum()
max_gun = gunluk_satis.idxmax()
max_satis_gun = gunluk_satis.max()
max_satis_gun_urunler = df.loc[max_gun]
# print(f"\nEn Fazla Satış Yapılan Gün: {max_gun} - Toplam Satış : {max_satis_gun}")
# print('O günde Satılan Ürünler:')
# print(max_satis_gun_urunler[['Ürün Adı', 'Satış']])

#4.Haftalık en fazla satış yapılan ürünler
haftalik_satis = df.resample('W')['Satış'].sum()
max_hafta = haftalik_satis.idxmax()
max_satis_hafta = haftalik_satis.max()
max_satis_hafta_urunler = df[df.index.to_series().between(max_hafta - pd.offsets.Week(1), max_hafta)]
# print(f"\nEn Fazla Satış Yapılan Hafta :{max_hafta}- Toplam Satış : {max_satis_hafta}")
# print("O Hafta Satılan Ürünler :")
# print(max_satis_hafta_urunler[['Ürün Adı', 'Satış']])

aylik_ortalama_satis = df.resample('ME')['Satış'].mean()
# print('Aylık Ortalama Satışlar:')
# print(aylik_ortalama_satis)
belirli_aralik_urunler = df[df.index.to_series().between('2024-01-01','2024-03-31')]
# print("Ocak 2024 ile Mart 2024 arasında satılan ürünler :")
# print(belirli_aralik_urunler[['Ürün Adı', 'Satış','Fiyat (TL)','Toplam Fiyat (TL)']])


#8.En yüksek toplam fiyatın olduğu ay ve o ayda satılan ürünler

aylik_toplam_fiyat = df.resample('ME')['Toplam Fiyat (TL)'].sum()
max_ay_fiyat = aylik_toplam_fiyat.idxmax()
max_fiyat_ay = aylik_toplam_fiyat.max()
max_fiyat_ay_urunler = df[df.index.to_series().between(max_ay_fiyat - pd.offsets.MonthBegin(1), max_ay_fiyat)]
# print(f"En Yüksek toplam fiyata sahip ay : {max_ay_fiyat} - Toplam Fiyat : {max_fiyat_ay}")
# print("O Ayda satılan ürünler : ")
# print(max_fiyat_ay_urunler[[ 'Satış','Ürün Adı', 'Toplam Fiyat (TL)']])
df['Satış'].plot(title='Satışların Zaman İçindeki Değişimi', xlabel='Tarih', ylabel='Satış Miktarı')
plt.show()