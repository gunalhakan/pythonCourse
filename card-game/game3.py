# Destede kalan kart sayısı için kartSayisi() isminde bir metot.
# Destedeki kartları karıştırmak için KartlariKaristir() isminde bir metot.
# kartDagit() ismindeki metot belirtilen adet kadar kartı dağıtmalıdır. Destedeki kalan kart sayısına dikkat.
# kartAt() ismindeki metot elden bir kart atmak için kullanılsın.

from random import shuffle

class Kart:
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger

    def __repr__(self):
        return f"{self.tip} {self.deger}"
    
class Deste:
    tipler = ["karo","sinek","kupa","maça"]
    degerler = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        # list comprehension
        self.kartlar = [Kart(tip,deger) for tip in Deste.tipler for deger in Deste.degerler]
        # print(self.kartlar)
    
    def kartSayisi(self):
        return len(self.kartlar)
    
    def karistir(self):
        # Kartlar dağıtıldığında destedeki kart sayısı 52 den düşer ve bir daha karıştırılamaz
        if self.kartSayisi() < 52:
            raise ValueError("Kartlar dağıtıldıktan sonra karıştırılamaz")
        # Kartlar listesini karıştırdık
        shuffle(self.kartlar)

    def kartDagit(self,adet):
        kartSayisi = self.kartSayisi()
        if kartSayisi == 0 :
            raise ValueError("Tüm kartlar dağıtıldı, yeni kart dağıtılamaz")
        # Dağıtılacak adet kart sayısı, destede kalan kart sayısından küçükse,
        # destedeki kadar kart dağıtması için küçük olanı adet değişkenine atadık
        adet = min([kartSayisi,adet])
        # Dağıtılacak kartları kartlar listesinin sonundan itibaren adet kadar dağıtılması 
        # için kartlar değişkenine aktarıldı.
        kartlar = self.kartlar[-adet:]
        # Dağıtılan kartlar sondan dağıtıldıktan sonra destede kalan kartlar baştan itibaren
        # desteye(self.kartlar) yeniden tanımlandı. (Bir nevi dağıtılanlar çıkarıldı)
        self.kartlar = self.kartlar[:-adet]
        # Dağıtılan kartlar döndürüldü.
        return kartlar

deste1 = Deste()
deste1.kartSayisi()
deste1.karistir()
# Karıştırılmış dağıtılmadan önce kartlar (52 adet)
print(deste1.kartlar)
# adet kadar kart dağıt(dağıtılan kartları yazar)
print("-"*20)
print(deste1.kartDagit(4))
# Deste de kalan kart sayısını göster
print("kalan kart sayısı")
print(deste1.kartSayisi())
# Destede kalan kartları göster
print("-"*20)
print(deste1.kartlar)
