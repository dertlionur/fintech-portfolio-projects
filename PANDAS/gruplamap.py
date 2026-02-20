import pandas as pd
#excel dosyasını oku
df = pd.read_excel('teknolojik_urunler.xlsx')

gruplar = df.groupby('Kategori')

# toplam_satis = df.groupby('Kategori')['Satış'].sum()
# toplam_satis_fiyat = df.groupby('Kategori')['Fiyat (TL)'].sum()
# ortalama_satis_fiyati = df.groupby('Kategori')['Fiyat (TL)'].mean()

# toplam_ve_ortalama = df.groupby('Kategori').agg(
#     {
#         'Satış':'mean',
#         'Fiyat (TL)': 'mean'
#     })
# print(toplam_ve_ortalama)

# en_pahali_urun = df.loc[df.groupby('Kategori')['Fiyat (TL)'].idxmax()]
# print(en_pahali_urun)

satis_ust_gruplar = df.groupby('Kategori').filter(lambda x: x['Satış'].sum() > 50)
print(satis_ust_gruplar[['Kategori','Ürün Adı','Satış','Fiyat (TL)']])