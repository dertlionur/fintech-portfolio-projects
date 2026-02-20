import pandas as pd
import MetaTrader5 as mt5
import matplotlib.pyplot as plt

if not mt5.initialize():
    print(f"Bağlantı Hatası: {mt5.last_error()}")
    quit()

sembol = "XAUUSD"
rates = mt5.copy_rates_from_pos(sembol, mt5.TIMEFRAME_M5, 0, 200)
mt5.shutdown()

df = pd.DataFrame(rates)
df["time"] = pd.to_datetime(df["time"], unit='s')
df['Orta_Bant'] = df['close'].rolling(window=20).mean()

# 2. Standart Sapma (Volatiliteyi ölçer)
df['Std_Dev'] = df['close'].rolling(window=20).std()

# 3. Üst ve Alt Bantları Hesapla (Matematiksel İşlem)
# Üst = Orta + (2 * Sapma)
df['Ust_Bant'] = df['Orta_Bant'] + (2 * df['Std_Dev'])

# Alt = Orta - (2 * Sapma)
df['Alt_Bant'] = df['Orta_Bant'] - (2 * df['Std_Dev'])

# Hesaplamaları görelim (Boş verileri -NaN- silerek)
print(df[['time', 'close', 'Ust_Bant', 'Alt_Bant']].tail())

# --- GRAFİK ÇİZİMİ ---
plt.figure(figsize=(12, 6))

# 1. Fiyatı Çiz
plt.plot(df['time'], df['close'], label='Fiyat', color='black', alpha=0.6)

# 2. Orta Bandı Çiz
plt.plot(df['time'], df['Orta_Bant'], label='Ortalama', color='blue', linestyle='--')

# 3. Üst ve Alt Bantları Çiz
plt.plot(df['time'], df['Ust_Bant'], label='Üst Sınır', color='green', alpha=0.3)
plt.plot(df['time'], df['Alt_Bant'], label='Alt Sınır', color='red', alpha=0.3)

# 4. SİHİRLİ DOKUNUŞ: İki bandın arasını boya (Gri Bölge)
plt.fill_between(df['time'], df['Ust_Bant'], df['Alt_Bant'], color='gray', alpha=0.1)

# Sinyal Yakalama (Basit bir AL/SAT mantığı görselleştirmesi)
# Fiyat Alt Banda değdiyse "AL" (Yeşil Ok), Üste değdiyse "SAT" (Kırmızı Ok)
# (Bu ileri seviye bir görselleştirme, sadece mantığı gör diye ekliyorum)

# --- KARAR MEKANİZMASI (Sinyal) ---

# 1. Listenin en sonundaki (yani şu anki canlı) veriyi çek
son_veri = df.iloc[-1]

# 2. Değerleri kolay okunsun diye isimlendirelim
fiyat = son_veri['close']
ust = son_veri['Ust_Bant']
alt = son_veri['Alt_Bant']

print("-" * 30)
print(f"Anlık Fiyat: {fiyat}")
print(f"Üst Sınır:   {ust:.2f}")
print(f"Alt Sınır:   {alt:.2f}")
print("-" * 30)

# 3. Sinyal Mantığı (If / Else)
if fiyat > ust:
    print("🚨 SİNYAL: SATIŞ (Short) Fırsatı! (Fiyat Üst Bandı Deldi)")
elif fiyat < alt:
    print("💎 SİNYAL: ALIŞ (Long) Fırsatı! (Fiyat Alt Bandı Deldi)")
else:
    print("✅ DURUM: NORMAL (Fiyat Bantların İçinde)")

plt.title(f"{sembol} - Bollinger Bantları Analizi")
plt.legend()
plt.grid(True)
plt.show()
