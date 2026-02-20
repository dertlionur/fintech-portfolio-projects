# Sonsuz döngü (Sen "uyu" diyene kadar program kapanmaz)
while True:
    print("\n" + "*"*40)
    print("🤖 ASİSTAN: Merhaba Onur! Şu an hangi vakitteyiz?")
    print("(Seçenekler: sabah, öğle, ikindi, akşam, gece)")
    print("*"*40)
    
    # 1. INPUT (Girdi) - Senden cevap bekler
    vakit = input("Lütfen vakti yaz: ")
    
    # Küçük/Büyük harf hatasını önlemek için hepsini küçültüyoruz
    # Yani "SABAH" da yazsan "sabah" olarak algılar.
    vakit = vakit.lower()

    # 2. KARAR MEKANİZMASI (If - Elif - Else)
    
    if vakit == "sabah":
        print("------------------------------------------------")
        print("☀️  GÜNAYDIN! Saat 08:00 Alarmı.")
        print("✅  GÖREV LİSTEN:")
        print("    1. Yüzünü yıka.")
        print("    2. Kahvaltını yap ve kahveni iç.")
        print("    3. Bilgisayarı aç -> İNGİLİZCE ÇALIŞ. 🇬🇧")
        print("------------------------------------------------")
        break

    elif vakit == "öğle":
        print("------------------------------------------------")
        print("🍔  ÖĞLE MOLASI.")
        print("✅  GÖREV LİSTEN:")
        print("    1. Yemeğini ye.")
        print("    2. Bilgisayara geç -> YAPAY ZEKA (GEMINI) ÇALIŞ. 🧠")
        print("------------------------------------------------")
        break

    elif vakit == "ikindi":
        print("------------------------------------------------")
        print("💪  SPOR VAKTİ!")
        print("✅  GÖREV LİSTEN:")
        print("    1. Bilgisayarı bırak.")
        print("    2. Kalk ve sporunu yap, hareket et.")
        print("------------------------------------------------")
        break

    elif vakit == "akşam":
        print("------------------------------------------------")
        print("🌇  AKŞAM OLDU.")
        print("✅  GÖREV LİSTEN:")
        print("    1. Akşam yemeğini ye.")
        print("    2. Gelişimini artıracak FİLM veya VİDEO izle. 🎬")
        print("------------------------------------------------")
        break

    elif vakit == "gece":
        print("------------------------------------------------")
        print("🌙  İYİ GECELER.")
        print("✅  GÖREV LİSTEN:")
        print("    1. Meditasyon yap. 🧘‍♂️")
        print("    2. Uyu ve dinlen.")
        print("------------------------------------------------")
        print("Program kapatılıyor... Yarın görüşürüz! 👋")
        break  # Döngüyü kırar ve programı sonlandırır

    else:
        # Tanımsız bir şey yazarsan (Örn: "Gece yarısı" gibi)
        print("❌  HATA: Tanımsız bir vakit girdin. Lütfen tekrar dene.")