import pandas as pd
from sklearn.model_selection import cross_val_score,train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score



df = pd.read_excel('karar_agaci_veri_100.xlsx')

X = df[['Yas', 'Kan_Basinci','Kolesterol']]
y = df['Hastalik']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# classiefier = DecisionTreeClassifier()
# classiefier.fit(X_train, y_train)

# y_pred = classiefier.predict(X_test)
# accuracy = accuracy_score(y_test , y_pred )

# print(f"Model Doğruluk Oranı: {accuracy}")
classifier = DecisionTreeClassifier(max_depth=1, min_samples_split=2 , min_samples_leaf=2)
# cross_val_skorlar = cross_val_score(classifier , X ,y , cv=5)
# print(f"5-Katlamalı Çapraz Doğrulama Skoları : {cross_val_skorlar}")
# print(f"Ortalama Doğruluk Skoru: {cross_val_skorlar.mean():.2f}")
classifier.fit(X,y)

# Kullanıcıdan veri alalım
print("Lütfen tahmin için aşağıdaki bilgileri giriniz:")
yas = int(input("Yaş: "))
kan_basinci = float(input("Kan Basıncı: "))
kolesterol = float(input("Kolesterol: "))

#kullanıcıdan alınan veriyi modelin anlayacağı formata çevirelim

yeni_veri = pd.DataFrame([[yas,kan_basinci,kolesterol]], columns=['Yas','Kan_Basinci','Kolesterol'])

tahmin = classifier.predict(yeni_veri)


#tahmin sonucunu kullanıcya göster

if tahmin[0] == 1:
    print("Tahmin : Hastalık Var")
else:
    print('Tahmin : Hastalık Yok')
