# Kart sınıfı

# Kart sınıfından türetilen her bir nesne bir kart türünü temsil edecek. (sinek 5)
# Kart sınıfının tip ve deger isminde 2 instance özelliği olsun. (tip:sinek deger:5)
# Kart sınıfının kartıGetir() ismindeki instance metodu kart bilgilerini yazdırsın.
# Kart bilgilerini yazdırmak için __repr__ metodunu kullanın. (Araştırma...)

class Kart:
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger

    # def kartiGetir(self):
    #     return f"{self.tip} {self.deger}"

    
    # representation -> nesneyi temsil eder.
    # object i yazdırdığımızda bu metod ekrana basılır, 
    # yeni bir fonksiyon tanımlayıp kullanma işlemini kısaltır
    def __repr__(self):
        return f"{self.tip} {self.deger}"
        
    

sinek5 = Kart("sinek","5")
# print(sinek5.kartiGetir())
print(sinek5)