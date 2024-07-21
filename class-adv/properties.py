class Product:
    def __init__(self,name,price,descripion):
        self.name = name
        self.description = descripion
        if price >= 0:
            # _ işareti class dışından erişilen nesneleri belirtmek için kullanılır,
            # özel bir anlamı yok
            self._price = price
        else:
            raise ValueError("Fiyat negatif olamaz")
    #class dışından erişmek için property kullanılır 
    @property
    def price(self):
        return self._price
    #class dışından değeri set etmek için değerin adı ve setter birlikte kullanılır
    @price.setter
    def price(self,value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Fiyat negatif olamaz")
      
    @property
    def short_description(self):
        return self.description[:10]
        
p1 = Product("macbook 14 M2",52000,"Yeni Macbook M2 çipiyle çok daha yüksek performans sunuyor")
print(p1.name)
# propert olarak tanımlandığı için class dışından erişilebilir
print(p1.price)
# property setter olarak tanımlandığı için class dışından erişilebilir
p1.price =-3000
print(p1.price)
# print(p1.description)
# print(p1.short_description)