# sermaye = 1000
# kar_zarar = -50
# güncel_sermaye = sermaye + kar_zarar
# print(f"Güncel Bakiyeniz: {güncel_sermaye}")

# islemler = [120,-50,30,-10,200]
# gunluk_sonuc = sum(islemler)
# print(f"Günlük İşlemlerin Sonucu Kalan Bakiye: {gunluk_sonuc}")

# if gunluk_sonuc > 0:
    # print("Tebrikler Bugün Kar Yaptınız...")
# elif gunluk_sonuc < 0:
    # print("Maalesef Bugün Zarar Ettiniz...")
# else:
    # print("Bugün İşleminiz Başa Baş...")


# kazanan_sayi = 0
# kaybeden_sayi = 0
# for islem in islemler:
    # if islem > 0:
        # kazanan_sayi+=1
    # else:
        # kaybeden_sayi+=1

# print(f"Başarılı İşlem Sayısı: {kazanan_sayi}")
# print(f"Başarısız İşlem Sayısı: {kaybeden_sayi}")

# toplam_islem = len(islemler)
# basari_orani = (kazanan_sayi / toplam_islem)*100
# print(f"Başarı Oranı: {basari_orani}")

def strateji_test(gelen_islemler):
    toplam_kar = sum(sali)
    print(f"Toplam Karınız: {toplam_kar}")

    kazanan_sayi = 0
    kaybeden_sayi = 0
    for islem in sali:
        if islem > 0:
            kazanan_sayi+=1
        else:
            kaybeden_sayi+=1
    
    print(f"Başarılı İşlem Sayısı: {kazanan_sayi}")
    print(f"Başarısız İşlem Sayısı: {kaybeden_sayi}")

    toplam_islem = len(sali)
    basari_orani = (kazanan_sayi / toplam_islem)*100
    print(f"Başarı Oranı: {basari_orani}")

sali = [-100, -20, 50, -30, 10]
print("---------Sali Raporu----------")
strateji_test(sali)
