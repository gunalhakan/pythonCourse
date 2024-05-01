import db

# print(db.urunler)
def selectUrunler():
    for urun in db.urunler:
        print(f"{urun['id']} : {urun['ad']} => {urun['fiyat']}")

def insertUrun(ad, fiyat):
    db.urunler.append({
        "id" : "100" + str(len(db.urunler) + 1),
        "ad" : ad,
        "fiyat" : fiyat
    })
def updateUrun(id,ad,fiyat):
    for urun in db.urunler:
        if str(id) == urun["id"]:
            urun["ad"] = ad
            urun["fiyat"] = fiyat
            break

def deleteUrun(id):
    print()
    for urun in db.urunler:
        if str(id) == urun["id"]:
            index = (int(id) % 1000) -1
            del db.urunler[index]
            print()
            break

# id= input("Silmek isteiğidiniz ürün id yi girin : ")
# # id = input("Ürün id girin : ")
# # ad = input("Ürün adı girin : ")
# # fiyat = float(input("Ürün fiyatı girin : "))
# deleteUrun(id)
# selectUrunler()