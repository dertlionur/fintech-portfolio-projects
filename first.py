class varlik:
    def __init__(self,ad,fiyat):
        self.ad = ad
        self.fiyat = fiyat
    
    def bilgiver(self):
        print(f"{self.ad} şuan ki fiyatı: {self.fiyat}")


class KriptoPara(varlik):
    def __init__(self, ad, fiyat,blokzincir):
        super().__init__(ad, fiyat)
        self.blokzincir = blokzincir

    def madencilik_notu(self):
        return f"{self.ad}, {self.blokzincir} ağında işlem görüyor"

class HisseSenedi(varlik):
    def __init__(self, ad, fiyat,borsa):
        super().__init__(ad, fiyat)
        self.borsa = borsa

class portföy:
    def __init__(self):
        self.varliklar = []
    
    def varlik_ekle(self,varlik):
        self.varliklar.append(varlik)
        print(f"{varlik.ad} portföye eklendi")
    
    def toplam_deger(self):
        toplam = sum(v.fiyat for v in self.varliklar)
        return f"Portföyün toplam değeri: {toplam}"
    

eth = KriptoPara("Etherum",5000,"ETH Network")
thy = HisseSenedi("THYAO",312,"BIST")

benim_portföyüm = portföy()
benim_portföyüm.varlik_ekle(eth)
benim_portföyüm.varlik_ekle(thy)

print(benim_portföyüm.toplam_deger())
print(eth.madencilik_notu())


finans = varlik("Altın","6000TL")
finans.bilgiver()
