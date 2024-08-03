# tanımladığımız fonksiyona parametre olarak bir fonksiyon da gönderebiliriz

def myfunc(iterable,func):
    iterator = iter(iterable)
    while True:
        try:
            sayi = next(iterator)
            func(sayi)
        except StopIteration:
            break
def kareAl(sayi):
    print(sayi * sayi)

sayilar = [1,2,3,4,5]
kelime = "Merhaba"
# myfunc un 2. parametresine print fonksiyonunu gönderdik
# böylece fonksiyon içinde gönderdiğimiz func parametresini kullandığımızda 
# print fonksiyonunun işlevi çalışır.
# myfunc(sayilar,print)
# myfunc(kelime,print)
# kareAl ın görevi gelen sayının karesini ekrana yazdırmaktır.
# myfunc da sayılar iterable olur ve her sayının karesi kareAl fonksiyonu sayesinde ekrana yazdırılır.
myfunc(sayilar,kareAl)

