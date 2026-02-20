import numpy as np

dizi = np.array([1,3,4,5,6])

# maks = np.max(dizi)
# min = np.min(dizi)
# 
# print(maks)
# print(min)

toplam = sum(dizi)
kume_toplam = np.cumsum(dizi)

print(toplam)
print(kume_toplam)