import MetaTrader5 as mt5
import pandas as pd
import numpy as np

# 1. BAĞLANTI
if not mt5.initialize():
    print("MT5 Başlatılamadı!")
    quit()

# 2. VERİ ÇEK (Son 10 mum)
sembol = "EURUSD"
rates = mt5.copy_rates_from_pos(sembol, mt5.TIMEFRAME_M15, 0, 10)
mt5.shutdown()

df = pd.DataFrame(rates)
df['time'] = pd.to_datetime(df['time'], unit='s')

#--- GÖREV TAMAMLANDI ---
#Mantık: Kapanış (close) > Açılış (open)  "Yükseliş", "Düşüş"
df["Durum"] = np.where(df["close"] > df["open"], "Yükseliş 🟢", "Düşüş 🔴")

# --- SONUCU GÖRELİM ---
print(df[['time', 'open', 'close', 'Durum']])

df['Degisim_Yuzde'] = (df["close"] - df["open"])/df['open']*100


# --- SONUCU GÖRELİM ---
# Sadece Zaman, Fiyat ve Yüzdeyi yazdıralım
print("-" * 30)
print(f"{sembol} SON 10 MUM ANALİZİ")
print("-" * 30)
print(df[['time', 'close', 'Degisim_Yuzde']])

buyuk_hareketler = df[df['Degisim_Yuzde'].abs() > 0.05]

print("\n" + "="*30)
print("🚨 DİKKAT ÇEKEN HAREKETLER (Volatilite) 🚨")
print("="*30)

if not buyuk_hareketler.empty:
    print(buyuk_hareketler[['time', 'close', 'Degisim_Yuzde', 'Durum']])
else:
    print("Piyasa şu an sakin, büyük bir hareket yok.")