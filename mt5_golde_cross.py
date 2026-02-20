import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. BAĞLAN
if not mt5.initialize():
    print("MT5 Başlatılamadı!")
    quit()

# 2. VERİ ÇEK (Ortalama hesaplayacağımız için en az 50-100 mum lazım)
sembol = "EURUSD"
rates = mt5.copy_rates_from_pos(sembol, mt5.TIMEFRAME_M15, 0, 100)
mt5.shutdown()

df = pd.DataFrame(rates)
df['time'] = pd.to_datetime(df['time'], unit='s')

# --- STRATEJİ HESAPLAMALARI ---
# SMA (Simple Moving Average) - Basit Hareketli Ortalama

# Hızlı Olan (5 Mum)
df['SMA_Hizli'] = df['close'].rolling(window=5).mean()

# Yavaş Olan (20 Mum)
df['SMA_Yavas'] = df['close'].rolling(window=20).mean()

# --- SİNYAL OLUŞTURMA (GÖREVİN BURADA) ---
# Mantık: 
# Eğer Hızlı (SMA_Hizli) > Yavaş (SMA_Yavas) ise "AL 🟢"
# Değilse "SAT 🔴" (veya Bekle)

df['Sinyal'] = np.where(df['SMA_Hizli'] > df['SMA_Yavas'], "AL 🟢", "SAT 🔴")


# --- SONUCU GÖRELİM ---
# Sadece son 10 muma bakalım, trend ne durumda?
print("-" * 40)
print(f"{sembol} - GOLDEN CROSS STRATEJİSİ")
print("-" * 40)
print(df[['time', 'close', 'SMA_Hizli', 'SMA_Yavas', 'Sinyal']].tail(10))


# --- GÖRSELLEŞTİRME (Visual Backtest) ---
plt.figure(figsize=(12, 6))

# 1. Fiyatı Çiz (Arka planda silik görünsün)
plt.plot(df['time'], df['close'], label='Fiyat', color='gray', alpha=0.3)

# 2. Ortalamaları Çiz
plt.plot(df['time'], df['SMA_Hizli'], label='Hızlı (5) - Mavi', color='blue', linewidth=2)
plt.plot(df['time'], df['SMA_Yavas'], label='Yavaş (20) - Kırmızı', color='red', linewidth=2)

# 3. SİNYAL BÖLGELERİNİ BOYAMA (İşte Sihir Burada!)
# where argümanı: Hangi koşulda boyayayım?
# interpolate=True: Kesişim noktalarını yumuşak geçişli yapar

# AL BÖLGESİ (Hızlı > Yavaş) -> Yeşil
plt.fill_between(df['time'], df['SMA_Hizli'], df['SMA_Yavas'], 
                 where=(df['SMA_Hizli'] > df['SMA_Yavas']), 
                 facecolor='green', alpha=0.2, label='AL Bölgesi')

# SAT BÖLGESİ (Hızlı < Yavaş) -> Kırmızı
plt.fill_between(df['time'], df['SMA_Hizli'], df['SMA_Yavas'], 
                 where=(df['SMA_Hizli'] < df['SMA_Yavas']), 
                 facecolor='red', alpha=0.2, label='SAT Bölgesi')



son_fiyat = df['close'].iloc[-1]
son_sma_hizli = df['SMA_Hizli'].iloc[-1]

print("\n" + "*"*30)
print("🛡️ KÂR KORUMA ANALİZİ")
print("*"*30)
print(f"Anlık Fiyat:      {son_fiyat}")
print(f"Destek (SMA 5):   {son_sma_hizli:.5f}")

# Mantık: Fiyat, Hızlı Ortalamanın altına düştü mü?
if son_fiyat < son_sma_hizli:
    print("🚨 UYARI: Fiyat, Hızlı Ortalamanın (Mavi Çizgi) altına indi!")
    print("💡 TAVSİYE: Kârı realize etmeyi (Satış) düşünebilirsin. Momentum zayıflıyor.")
else:
    print("✅ DURUM: Trend hala ÇOK GÜÇLÜ.")
    print(f"💡 TAVSİYE: Pozisyonu tutmaya devam et. Stop seviyen: {son_sma_hizli:.5f}")
    print("   (Fiyat bu değerin altına düşerse çıkış yaparsın.)")

plt.title(f"{sembol} - Golden Cross Stratejisi (Yeşil=AL, Kırmızı=SAT)")
plt.xlabel("Zaman")
plt.ylabel("Fiyat")
plt.legend()
plt.grid(True)
plt.show()

# --- ÇIKIŞ STRATEJİSİ (Trailing Stop) ---

# Son kapanış fiyatı ve son ortalama değeri
