def usAlma(taban):
    def inner(us):
        return taban ** us
        # Dönen değer bir değişkene atanacaksa mutlaka fonksiyonla aynı isimde olmalı
        # inner = taban ** us
        # return inner
    # Fonksiyonu geri döndürür
    return inner
# # içteki fonksiyona ulaşmak için 2 parantez ve parametre kullanılır.
# print(usAlma(2)(3))
# # İçteki fonksiyona ulaşmak için ilk fonksiyon bir değişkene atanır, 
# # değişken olan fonksiyona yeni parametre eklenerek yeniden çağırma işlemi uygulanır.
iki = usAlma(2)
print(iki(3))

def islem(islemAdi):
    def toplam(*args):
        toplam = 0
        for deger in args:
            
            toplam = toplam + deger
        # Dönen değişken isminin fonksiyon ile aynı olması şarttır.
        return toplam
    
    def carpim(*args):
        sonuc = 1
        for deger in args:
            carpim = carpim * deger
        # Dönen değişken adı fonksiyon adı ile aynı olmak zorunda
        return carpim
    
    if islemAdi == "toplam":
        return toplam
    elif islemAdi == "carpim":
        return carpim
    
toplama = islem("toplam")
print(toplama(3,4,5))