import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#excel dosyalarını ekle

df = pd.read_excel('karar_agaci_veri_100.xlsx')


#Yaş ile hastalık arasındaki ilişkiyi görselleştirme

plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Yas', hue='Hastalik' , multiple='stack', kde=True)
plt.title('Yaş Dağılımı ve Hastalık Durumu')
plt.xlabel('Yaş')
plt.ylabel('Kişi Sayısı')
# plt.show()


plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Kan_Basinci', hue='Hastalik' , multiple='stack', kde=True)
plt.title('Kan Basinci ve Hastalık Durumu')
plt.xlabel('Kan Basinci')
plt.ylabel('Kişi Sayısı')
plt.show()


plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Kolesterol', hue='Hastalik' , multiple='stack', kde=True)
plt.title('Kolesteroli ve Hastalık Durumu')
plt.xlabel('Kolesterol')
plt.ylabel('Kişi Sayısı')
plt.show()