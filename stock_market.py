import pandas as pd
import numpy as np

data = {
    "Gun": ["Pzt", "Sal", "Çar", "Per", "Cum"],
    "Acilis": [100, 105, 102, 110, 108],
    "Kapanis": [105, 100, 108, 109, 115]
}

df = pd.DataFrame(data)

df["Durum"] = np.where(df["Kapanis"] > df["Acilis"], "Yükseliş", "Düşüş")
print(df)