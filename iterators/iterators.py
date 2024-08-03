# itarable

sayilar = [1,2,3,4,5]
# print(dir(sayilar))
isim = "Hakan"
# dir bir nesnenin(burda string veya list object i kullanılmış) kullanılabileceği hazır metodları listler
# Örneğin strin için islower metodu kullanılabilir 
# print(dir(isim))

# iterator nedir?
# iter(iterator) metodu ile bir object in elemanları iterable hale getirilir.
# For döngüsü iter işlemini otomatik olarak yapar

# Kendi ürettiğimiz nesnelerdeki elemanlara tek tek ulaşmak için iterator ve iterable kullanılmak zorundadır.

sayilar2 = iter(sayilar)
# next metodu ile iterable nesne içindeki elemanlara sıra ile ulaşılır. 
# print(next(sayilar2))
# print(next(sayilar2))
# print(next(sayilar2))
# print(next(sayilar2))
# print(next(sayilar2))
# nesne içindeki son elemandan sonra yazdırmaya çalışırsak stopIteration hatası alırız.
# print(next(sayilar2))

# Manuel for döngüsü
while True:
    try:
        sayi = next(sayilar2)
        print(sayi)
    except StopIteration:
        break

