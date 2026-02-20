import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Excel dosyasını oku
df = pd.read_excel('karar_agaci_veri_100.xlsx')

# Girdi ve çıktı değişkenlerini ayırma
X = df[['Yas', 'Kan_Basinci', 'Kolesterol']]  # Girdi: Yaş, Kan Basıncı, Kolesterol
y = df['Hastalik']  # Çıktı: Hastalık durumu (0: yok, 1: var)

# Karar Ağacı sınıflandırıcısını oluşturma
classifier = DecisionTreeClassifier()

# 5 katlamalı çapraz doğrulama kullanarak modelin doğruluğunu ölçme
cross_val_skorlar = cross_val_score(classifier, X, y, cv=5)

# Çapraz doğrulama sonuçlarının ortalaması
print(f"5-Katlamalı Çapraz Doğrulama Skorları: {cross_val_skorlar}")
print(f"Ortalama Doğruluk Skoru: {cross_val_skorlar.mean():.2f}")

# Modeli eğitip test etmek için tekrar ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli eğitme ve tahmin yapma
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

# Modelin test verisi üzerindeki doğruluğunu ölçme
accuracy = accuracy_score(y_test, y_pred)
print(f"Modelin Test Setindeki Doğruluk Oranı: {accuracy:.2f}")
