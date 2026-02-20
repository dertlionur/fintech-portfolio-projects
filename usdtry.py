import pandas as pd 
import numpy as np
import MetaTrader5 as mt5
import matplotlib.pyplot as plt

# MT5 BAĞLAN
if not mt5.initialize():
    print("MT5 Başlatılamadı...")
    quit()

# VERİ ÇEKME ORTALAMA HESAPLAYACAĞIMIZ İÇİN EN AZ 50-100 MUM
sembol = "USDTRY"
rates = mt5.copy_rates_from_pos(sembol, mt5.TIMEFRAME_M15, 0, 10)
mt5.shutdown()

#VERİYİ HAZIRLAMA
df = pd.DataFrame(rates)
df['time'] = pd.to_datetime(df["time"], unit='s')

#STRATEJİ HESAPLAMALARI

#HIZLI OLAN
df['SMA_Hizli'] = df['close'].rolling(window=5).mean()

#YAVAŞ OLAN
df["SMA_Yavas"] = df['close'].rolling(window=20).mean()

#SİNYAL OLUŞTURMA
df['Sinyal'] = np.where(df['SMA_Hizli'] > df['SMA_Yavas'], "AL 🟢", "SAT 🔴")

#SONUCU GÖRECEĞİMİZ YER
#50 MUMA BAKTIK
print("-"*40)
print(f"{sembol} - GOLDEN CROSS STRATEJİSİ")
print("-"*40)
print(df[['time','close','SMA_Hizli','SMA_Yavas',"Sinyal"]].tail(50))
