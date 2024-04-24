# map fonksiyonu bir fonksiyon ve bir iterable değer alır. 
## gelen iterable daki elemanları sırayla fonksiyona gönderip dönenleri bir map class ı içine alır
## map i list e dönüştürerek sonucu düzenli alabiliriz.
# bir fonksiyona sırayla liste gönderme işleminin kısaltılmışı 
def kareAl(sayi):
    return sayi ** 2
sayilar = [1,2,3,4,5]
sonuc = list(map(kareAl,sayilar))
## map in lambda ile birlikte kullanımı gelen sayıları 2yle çarpar
## map iterable dır, for ile kullanılır.
sonuc = list(map(lambda sayi : sayi * 2, sayilar))
sayilar_str = ["1","2","3","4","5"]
sonuc = list(map(int,sayilar_str))
sayilar_neg = [-4,3,-9,-11,5]
sonuc = list(map(abs,sayilar_neg))
isimler =["Hakan","Seda","Nil","Ahmetcan"]
sonuc = list(map(len,isimler))
sonuc = list(map(str.upper,isimler))
users = [
    {"ad" : "Seda", "soyad":"Günal"},
    {"ad" : "Hakan", "soyad":"Günal"},
    {"ad" : "Nil", "soyad":"Günal"},
    {"ad" : "Metin", "soyad":"Demir"},
    {"ad" : "Kerem Poyraz", "soyad":"Demir"},
    {"ad" : "Derya", "soyad":"Demir"},
]
sonuc = list(map(lambda x : x["ad"],users))
sonuc = list(map(lambda x : len(x["ad"]),users))
print(sonuc)