class Pet:

    cinsler = ["kedi","köpek","kuş"]

    def __init__(self,isim,cins):
        # init içinde olan bir elemana nesne tarafından erişim için self anahtar kelimesi
        # kullanılması zorunludur.
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değildir.")
        self.isim = isim
        self.cins = cins

    def set_cins(self,cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değildir.")
        self.cins = cins

boncuk = Pet("Boncuk","kedi")
pasa = Pet("Paşa","köpek")
mavis = Pet("Maviş","kuş")

mavis.set_cins("aslan")

# Nesne üzerinden bir elemana __init__ metodu üzerinden ulaşırsan append gibi metodlar
# SADECE OLUŞTURDUĞUN NESNE İÇİN GEÇERLİ OLUR.
# boncuk.cinsler.append("balık")
# pasa.cinsler.append("balık")

# print(Pet.cinsler)
# print(boncuk.cinsler)
# print(pasa.cinsler)