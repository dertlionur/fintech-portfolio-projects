import random
from shlex import join

# KULLANILACAK KARAKTERLER
harfler_ve_sayilar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
print("\n" + "="*40)
print("Şifre Üretme")

# KULLANICIDAN VERİ ALMA
metin_uzunluk = input("Kaç Karakterli Şifre İstersin(Güvenlik İçin En Az 8 Karakter): ")
uzunluk = int(metin_uzunluk)

# RASTGELE SEÇİM VE BİRŞELTİRME İŞLEMİ
guvenli_sifre = "".join(random.sample(harfler_ve_sayilar,uzunluk))

# KARAKTER SAYISINI KONTROL ETME
if uzunluk < 8:
    print("Şifreniz 8 Veya Daha Fazla Karakterden Oluşmalıdır...")
else:
    print("\n✅ Şifre Oluşturuldu:")
    print(f"👉{guvenli_sifre}👈")
    print("\n" + "="*40)