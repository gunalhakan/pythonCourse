def sayma_islemi(max):
    sayi = 1
    # sayilar isimli liste kullandık ve tüm elemanları yazdırdık
    # sayilar = []
    while sayi <= 10:
        # liste kullanma işlemi büyük verilerle çalışırken oldukça fazla bellek kullanılır. 
        # liste yerine, bir kez kullanım yapılacaksa yield ile generator oluşturup kullanabiliriz 
        # sayilar.append(sayi)
        yield sayi
        sayi += 1
    
    # return sayilar
    

sayilar = sayma_islemi(10)
# generatorlar iterator oldukları için next ile birlikte kullanılabilir

# generator nesnesi içinde iterator varsayılan olarak bulunur bu sebeple 
# iter kullanmadan for döngüsü ile birlikte kullanılabilir.

# Altta ilk olarak baştaki sayıları yazıyor
print(next(sayilar))
print(next(sayilar))
print("-"*20)
for i in sayilar:
    # tekrar kullanıldığında ise kaldığı yerden devam eder
    print(i)
    
    
# generator kullanımında kullanılan değere tekrar ulaşmak mümkün değildir
# generator olan veriler aynı zamanda iteratordır, 
# bu veriler tekrar ulaşmak için kullanılacaksa ilk başta liste türüne çevirmek yeterlidir.
# örnek : list(sayilar)

# list_comprehension ile veri atama yapar gibi generator nesnesi üretilebilir
cift_sayilar = (i for i in range(2,11,2))
# generator oluşturur
print(cift_sayilar)
for i in cift_sayilar:
    print(i)