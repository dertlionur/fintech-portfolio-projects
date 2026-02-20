import numpy as np

fiyatlar = np.array([0.82,0.43])
miktarlar = np.array([433,600])

toplam_deger = np.dot(fiyatlar,miktarlar)

print(toplam_deger)