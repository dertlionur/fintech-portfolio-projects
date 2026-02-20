import numpy as np


# dizi1 = np.array([1,2,3,4])
# dizi2 = np.array([5,6,7,8])
# 
# birlesik_dizi = np.concatenate((dizi1,dizi2))
# 
# print(birlesik_dizi)

dizi1 = np.array([[1,2,3,4],[5,6,7,8]])
dizi2 = np.array([[9,10,11,12],[13,14,15,16]])

birlestir = np.hstack((dizi1,dizi2))
birlestir1 = np.vstack((dizi1,dizi2))
print(birlestir)
print("----------------------------------")
print(birlestir1)