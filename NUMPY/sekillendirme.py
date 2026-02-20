import numpy as np

dizi = np.array([1,2,3,4,5,6,7,8])
yeni_dizi = dizi.reshape((2,4))

print(yeni_dizi)

dizi1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
tek_boyut = dizi1.reshape(-1)  #2 boyutlu diziyi tek boyutlu diziye çevirme
print(tek_boyut)

yeni_dizi1 = dizi1.reshape(3,-1) #Satır sayısını verdik sütün sayısını programa hesaplatıyoruz

print(yeni_dizi1)