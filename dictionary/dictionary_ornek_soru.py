# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.

urunler= {}
# for i in range(3):

#     id = input("id girin: ")
#     ad = input("ad girin: ")
#     fiyat = float(input("fiyat girin: "))

#     urunler[id] = {
#         "ad" : ad,
#         "fiyat" : fiyat
#     }
# print(urunler)
urunler = {
    '11': {'ad': 'aaa', 'fiyat': 1099.0}, 
    '12': {'ad': 'bbb', 'fiyat': 1200.0}, 
    '13': {'ad': 'ccc', 'fiyat': 2321.0}
}

arananId = input("Aradığınız ürünün id bilgisini girin : ")
arananUrun = urunler[arananId]
print(arananUrun)

