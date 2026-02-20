import yfinance as yf
import pandas as pd
import warnings

# Terminali gereksiz uyarılarla kirletmemek için:
warnings.filterwarnings('ignore')

# 1. TARANACAK HİSSELER LİSTESİ
hisseler = ["THYAO.IS", "TUPRS.IS", "ASELS.IS", "KCHOL.IS", "AKBNK.IS"]

print("="*60)
print("🚀 BİST ORTA VADE OTOMATİK TARAMA BOTU BAŞLATILIYOR...")
print("="*60)

# 2. FOR DÖNGÜSÜ: Listedeki her bir hisse için aşağıdaki işlemleri tekrarla
for hisse in hisseler:
    try:
        # Veriyi çek
        veri = yf.download(hisse, period="1y", interval="1d", progress=False)
        
        # Sütunları düzelt
        if isinstance(veri.columns, pd.MultiIndex):
            kapanis = veri['Close', hisse]
        else:
            kapanis = veri['Close']
            
        df = pd.DataFrame({"Kapanis": kapanis})
        
        # Hareketli Ortalamaları Hesapla
        df["SMA_50"] = df["Kapanis"].rolling(window=50).mean()
        df["SMA_200"] = df["Kapanis"].rolling(window=200).mean()
        
        # Sadece en son günün verisini al
        son_durum = df.dropna().tail(1)
        son_kapanis = son_durum["Kapanis"].iloc[-1]
        son_sma50 = son_durum["SMA_50"].iloc[-1]
        son_sma200 = son_durum["SMA_200"].iloc[-1]
        
        # Algoritma Kararı
        if son_sma50 > son_sma200:
            karar = "🟢 AL / TUT (Trend Pozitif)"
        else:
            karar = "🔴 SAT / UZAK DUR (Trend Negatif)"
            
        # Sonucu Ekrana Bas
        print(f"📌 {hisse: <10} | Fiyat: {son_kapanis:>7.2f} TL | Durum: {karar}")
        
    except Exception as e:
        print(f"⚠️ {hisse} verisi çekilirken hata oluştu.")

print("="*60)
print("✅ Tarama Tamamlandı!")