# Dictionary 2
## Dictionary değerlerini güncelleme
## Dictionary e yeni değerler ekleme
## Dictionary kopyalama
## Dictionary de bulunan elemanları silme
book1 = {
    "name" : "Suç ve Ceza",
    "author" : "Fyodor Dostoyevski",
    "page" : 784,
    "stock": 4,
    "publishYear":[1845,1920,1938,1995,2003],
    "trade":True
}
print(book1)
book1["stock"] = 1
print(book1)
book1.update({"trade":False})
print(book1)
book1["publishCo"] = "İş Bankası Yayınları"
print(book1)
book1.update({"price":145.6})
print(book1)
# Bir dictionary i kopyalamak için copy metodu kullanılır. 
# dictionary reference type olduğu için = operatörü kullanılmaz.
book2 = book1.copy()
# pop silinen değeri döndürür
#print(book1.pop("price"))
# popitem silinen elemanı(key value) döndürür
#print(book1.popitem())
book2.clear()
print("book2 =",book2)
print("book1 =",book1)
del book1["name"]
# del book1
result = book1
print(result)
