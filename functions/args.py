# def toplam(sayilar):
#     sonuc = 0
#     for sayi in sayilar:
#         sonuc = sonuc + sayi
#     return sonuc

# liste1 = [10,20,30,40]
# sonuc = toplam(liste1)
# print(sonuc)

def toplam (*args):
    #* tuple türünde veri göndermek için kullanılır, args değişken ismi
    print(type(args))
    print(args)
    sonuc = 0
    for sayi in args:
        sonuc = sonuc + sayi
    return sonuc

print(toplam(10,20,30))
print(toplam(10,20,30,50))
