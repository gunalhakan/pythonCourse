class Person():
    
    city = "İstanbul"
    buYil = 2024
    # yapıcı fonksiyon, ilk nesne oluştuğunda 1 kez çağırılır.
    # nesne oluştururken gereken parametreler __init__ e gönderilir.
    
    def __init__(self,name,age) :
        #Class içinde kullanılacak özellikler için self nesnesi kullanılır.
        # Gelen parametreler class içindeki name ve age değişkenlerine atandı,
        # böylece class ın her yerinde kullanılabilir hale geldi
        self.name=name
        self.age=age
        #print("init çalıştı")

        print(name)
        print(age)
        # Örneğin class içinde ama fonksiyonun dışında olan bir elemanı class_ismi.eleman
        # şeklinde çağırırız
        print(Person.city)

    def yaz(self):
        print(self.name)
        print(self.age)
    #
    def dogumYiliHesapla(self):
        # __init__ metodunda parametre olarak gelen  age self.age olarak alındığı için ve 
        # bu metoda parametre olarak self alındığı için, age ve buYil değişkenleri 
        # hatasız kullanılabildi.
        print(Person.buYil-self.age)

p1 = Person("Ali",41)
p2 = Person("Ayşe",28)
print(p1.name, p1.age)
print(p2.name, p2.age)
print("-"*50)
p2.dogumYiliHesapla()
# p1 update name - age
p1.name = "Timur"
p1.age = 28
print(p1.name, p1.age)
