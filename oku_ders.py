#Try - Except Hata Yakalama
# try:
    # x = int("abc")
# 
# except Exception as hataMesaj:
    # print(f"Hata Oluştu: {hataMesaj}")

# Sıfıra Bölünme Hatası
# try:
    # sayi = int(input("Bir Sayı Giriniz: "))
    # sonuc = 10 / sayi
    # print(f"Sonuç: {sonuc}")
# except ZeroDivisionError as bolme_hata:
    # print(f"Hata bir sayı sıfıra bölünemez: {bolme_hata}")

# Tanımlanmamış değişken hatası

# try:
    # a = 5
    # print(x)
# except NameError:
    # print("Tanımlanmamış Bir Değişken Kullanıldı")

#Geçersiz değer hatası

# try:
    # sayi = int(input("Bir Sayı Giriniz: "))
    # print(f"Girilen Sayi: {sayi}")
# except ValueError:
    # print("Hata: Geçersiz Değer Girişi")

try:
     sayi = int(input("Bir Sayı Giriniz: "))
     print(f"Girilen Sayi: {sayi}")
except ValueError:
     print("Hata: Geçersiz Değer Girişi")

else:
    print("Program Sorunsuz Çalıştı")
finally:
    print("Program Sonlandı")