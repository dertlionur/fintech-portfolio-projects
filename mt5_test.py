from sqlite3 import Time
import pandas as pd
import MetaTrader5 as mt5
import matplotlib.pyplot as plt
from datetime import datetime

if not mt5.initialize():
    print(f"MT5 başlatılamadı hata kodu = {mt5.last_error()}")
    quit()
else:
    print("MT5 bağlantısı başarılı veriler çekiliyor...")


sembol = "EURUSD"
zaman_dilimi = mt5.TIMEFRAME_H1
mum_sayisi = 100

rates = mt5.copy_rates_from_pos(sembol, zaman_dilimi, 0, mum_sayisi)
mt5.shutdown()

df = pd.DataFrame(rates)
df['time'] = pd.to_datetime(df['time'], unit='s')

print("\n-----Çekilen Veriler-----")
print(df[['time', 'open', 'high', 'low', 'close', 'tick_volume']].head())
plt.figure(figsize=(12, 6))
plt.plot(df['time'], df['close'], label=f"{sembol} Fiyatı", color="blue")

plt.title(f"{sembol} - MetaTrader 5 Verisi (Son {mum_sayisi} Saat)")
plt.xlabel("Tarih")
plt.ylabel("Fiyat")
plt.grid(True)
plt.legend()
plt.xticks(rotation=45) # Tarihleri eğik yaz
plt.tight_layout()

plt.show()

