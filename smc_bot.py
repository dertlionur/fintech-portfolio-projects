import MetaTrader5 as mt5
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

print("="*65)
print("🛡️ DİJİTAL DENETMEN PRO - ÇİFT YÖNLÜ SMC AL-SAT BOTU 🛡️")
print("="*65)

# 1. MT5 BAĞLANTISI VE HEDEF BELİRLEME
if not mt5.initialize():
    print("❌ MT5 başlatılamadı! Lütfen MT5 terminalinin açık olduğundan emin ol.")
    mt5.shutdown()
    quit()

# İşlem yapılacak sembol (Aracı kurumuna göre EURUSD, BTCUSD, XAUUSD vb. olarak değiştir)
sembol = "EURUSD"

if not mt5.symbol_select(sembol, True):
    print(f"❌ {sembol} bulunamadı! MT5 'Piyasa Gözlemi' penceresindeki tam adı yaz.")
    mt5.shutdown()
    quit()

print(f"📡 {sembol} canlı piyasa verileri analiz ediliyor...")

# Veriyi çek (Son 250 günlük mum)
veriler = mt5.copy_rates_from_pos(sembol, mt5.TIMEFRAME_D1, 0, 250)
mt5.shutdown()

if veriler is None or len(veriler) == 0:
    print("❌ Veri çekilemedi. Bağlantıyı kontrol et.")
    quit()

# 2. VERİ BİLİMİ (PANDAS DATAFRAME)
df = pd.DataFrame(veriler)
df['time'] = pd.to_datetime(df['time'], unit='s')

# --- İNDİKATÖRLER VE SMC MATEMATİĞİ ---

# A. Trend (Golden/Death Cross)
df["SMA_50"] = df["close"].rolling(window=50).mean()
df["SMA_200"] = df["close"].rolling(window=200).mean()

# B. Yükseliş Senaryoları (Bullish)
df['Bullish_FVG'] = df['low'] > df['high'].shift(2)
df['Son_Dip'] = df['low'].rolling(window=20).min().shift(1)
df['Turtle_Soup_Bullish'] = (df['low'] < df['Son_Dip']) & (df['close'] > df['Son_Dip'])

# C. DÜŞÜŞ Senaryoları (Bearish - YENİ EKLENDİ)
# Düşüş FVG'si: 3. mumun en yükseği, 1. mumun en düşüğünün altında kalmışsa boşluk vardır.
df['Bearish_FVG'] = df['high'] < df['low'].shift(2)
# Tepeden Likidite Avı: Fiyat son 20 günün zirvesini kırıp (iğne atıp), altında kapatırsa tuzaktır.
df['Son_Zirve'] = df['high'].rolling(window=20).max().shift(1)
df['Turtle_Soup_Bearish'] = (df['high'] > df['Son_Zirve']) & (df['close'] < df['Son_Zirve'])

# 3. KARAR MOTORU (ALGORİTMA BEYNİ)
son_durum = df.dropna().tail(1).iloc[0]

fiyat = son_durum["close"]
sma50, sma200 = son_durum["SMA_50"], son_durum["SMA_200"]
bull_fvg, bear_fvg = son_durum["Bullish_FVG"], son_durum["Bearish_FVG"]
bull_ts, bear_ts = son_durum["Turtle_Soup_Bullish"], son_durum["Turtle_Soup_Bearish"]
son_dip, son_zirve = son_durum["Son_Dip"], son_durum["Son_Zirve"]

# --- SİNYAL VE RİSK YÖNETİMİ HESAPLAMA ---
sinyal = "BEKLE"
renk = "⚪"
gerekce = "Piyasa yatay veya kararsız. Net bir SMC onayı yok."
stop_loss = 0.0
take_profit = 0.0

# AL (LONG) KOŞULLARI
if sma50 > sma200:
    if bull_ts:
        sinyal, renk = "GÜÇLÜ AL", "🟢"
        gerekce = "Trend YUKARI + Dipten Likidite Avı (Turtle Soup) gerçekleşti. Fiyat roketlemeye hazır."
        stop_loss = son_dip * 0.998 # Dibe çok yakın koruma
        take_profit = fiyat + (fiyat - stop_loss) * 2 # 1:2 Risk Ödül Oranı
    elif bull_fvg:
        sinyal, renk = "DİKKAT (RETEST BEKLE)", "🟡"
        gerekce = "Trend YUKARI ama aşağıda dolması gereken FVG var. Şimdilik alma, fiyata düzeltme gelebilir."

# SAT (SHORT) KOŞULLARI
elif sma50 < sma200:
    if bear_ts:
        sinyal, renk = "GÜÇLÜ SAT", "🔴"
        gerekce = "Trend AŞAĞI + Tepeden Likidite Avı (Tuzak) gerçekleşti. Düşüş derinleşecek."
        stop_loss = son_zirve * 1.002 # Zirvenin hemen üstüne koruma
        take_profit = fiyat - (stop_loss - fiyat) * 2 # 1:2 Risk Ödül Oranı
    elif bear_fvg:
        sinyal, renk = "DİKKAT (RETEST BEKLE)", "🟠"
        gerekce = "Trend AŞAĞI ama yukarıda dolması gereken FVG var. Açığa satmak için fiyatın oraya çarpmasını bekle."

# 4. PROFESYONEL ÇIKTI EKRANI
print("\n" + "="*65)
print(f"[{sembol}] GÜNCEL DURUM RAPORU | Fiyat: {fiyat:.5f}")
print("="*65)
print(f"📉 Trend Durumu   : {'YÜKSELİŞ (Boğa)' if sma50 > sma200 else 'DÜŞÜŞ (Ayı)'}")
print(f"🧠 Akıllı Para    : Likidite Avı (Boğa: {bull_ts} | Ayı: {bear_ts})")
print(f"🕳️ FVG Boşlukları : (Boğa: {bull_fvg} | Ayı: {bear_fvg})")
print("-"*65)
print(f"🚀 KESİN SİNYAL   : {renk} {sinyal} {renk}")
print(f"📝 Gerekçe        : {gerekce}")

# Eğer işlem açılacaksa seviyeleri göster
if sinyal in ["GÜÇLÜ AL", "GÜÇLÜ SAT"]:
    print("-"*65)
    print("🛡️ RİSK YÖNETİMİ (1:2 R/R Oranı)")
    print(f"❌ Zarar Kes (SL) : {stop_loss:.5f}")
    print(f"✅ Kâr Al (TP)    : {take_profit:.5f}")

print("="*65 + "\n")