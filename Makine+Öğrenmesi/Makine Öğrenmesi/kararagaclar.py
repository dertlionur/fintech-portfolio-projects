import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#veriyi hazırlama : yaş, kan basınıcını , kolestrerol ve hastalık durumu verisini 

# data = {
#     'Yas': [25,50,45,30,60],
#     'Kan_Basinci': [120,140,130,110,150],
#     'Kolesterol' : [180,240,200,160,220],
#     'Hastalik': [0,1,1,0,1] # 0 hayır , 1 evet
# }

# df = pd.DataFrame(data)

df = pd.read_excel('karar_agaci_veri_100.xlsx')

X = df[['Yas', 'Kan_Basinci','Kolesterol']]
y = df['Hastalik']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
classiefier = DecisionTreeClassifier()
classiefier.fit(X_train, y_train)
y_pred = classiefier.predict(X_test)
accuracy = accuracy_score(y_test , y_pred )
# print(f"Model Doğruluk Oranı: {accuracy}")
# Kullanıcıdan veri alarak tahmin yapma
yas = int(input("Yaşınızı girin: "))
kan_basinci = int(input("Kan basıncınızı girin: "))
kolesterol = int(input("Kolesterol seviyenizi girin: "))
#tahmın oluştur
kullanici_verisi = pd.DataFrame([[yas, kan_basinci, kolesterol]], columns=['Yas', 'Kan_Basinci', 'Kolesterol'])
tahmin = classiefier.predict(kullanici_verisi)
sonuc = "Hastalık var" if tahmin[0] == 1 else "Hastalık Yok"
print(f"Tahmin : {sonuc}")
