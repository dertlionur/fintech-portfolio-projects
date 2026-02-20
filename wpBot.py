"""
WhatsApp - Aynı mesajı sürekli gönderen bot
WhatsApp Web üzerinden çalışır. Bir kez QR kodu taratırsınız, sonra mesaj döngüde gönderilir.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver otomatik indirmek için (pip install webdriver-manager)
try:
    from webdriver_manager.chrome import ChromeDriverManager
    USE_MANAGER = True
except ImportError:
    USE_MANAGER = False


def main():
    print("=" * 50)
    print("  WhatsApp - Aynı Mesajı Sürekli Gönderen Bot")
    print("=" * 50)

    # Kullanıcıdan bilgileri al (ülke kodu ile numara: 905551234567)
    telefon = input("\nHedef telefon (ülke kodu ile, + olmadan, örn: 905551234567): ").strip()
    if not telefon:
        print("Telefon numarası gerekli.")
        return

    mesaj = input("Gönderilecek mesaj:").strip("😂")
    if not mesaj:
        print("Mesaj gerekli.")
        return

    try:
        aralik = float(input("Gönderim aralığı (saniye, örn: 5): ").strip() or "0")
    except ValueError:
        aralik = 0.0

    try:
        adet_str = input("Kaç kez gönderilsin? (0 = süresiz, Ctrl+C ile dur): ").strip() or "0"
        adet = int(adet_str)
    except ValueError:
        adet = 0

    # Chrome ayarları
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=./whatsapp_profile")  # Oturum saklansın
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    if USE_MANAGER:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://web.whatsapp.com/")
        print("\nLütfen WhatsApp Web için QR kodu telefonunuzla tarayın...")
        print("(İlk seferden sonra oturum kaydedilir, tekrar sormaz.)\n")

        # QR ile giriş sonrası ana panelin yüklenmesini bekle
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='chat-list']"))
        )
        print("Giriş yapıldı.\n")

        # Sohbeti aç: numaraya doğrudan link
        driver.get(f"https://web.whatsapp.com/send?phone={telefon}")
        time.sleep(2)

        # Mesaj kutusu (contenteditable)
        msg_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10']"))
        )
        print("Sohbet açıldı. Mesajlar gönderiliyor... (Durdurmak için Ctrl+C)\n")

        gonderilen = 0
        while True:
            if adet > 0 and gonderilen >= adet:
                print(f"\n{adet} mesaj gönderildi. Çıkılıyor.")
                break

            # Mesaj kutusuna tıkla ve yaz
            msg_box.click()
            time.sleep(0.3)
            msg_box.send_keys(mesaj)
            time.sleep(0.2)
            msg_box.send_keys(Keys.ENTER)
            gonderilen += 1
            print(f"  Gönderildi: {gonderilen}")

            time.sleep(aralik)
            # Element tekrar referansı (sayfa güncellenebilir)
            msg_box = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10']")

    except KeyboardInterrupt:
        print("\n\nKullanıcı tarafından durduruldu.")
    except Exception as e:
        print(f"\nHata: {e}")
    finally:
        input("\nÇıkmak için Enter'a basın (tarayıcı kapanacak)...")
        driver.quit()


if __name__ == "__main__":
    main()
