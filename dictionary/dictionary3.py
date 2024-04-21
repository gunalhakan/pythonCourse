# Dictionary
## Dictionary lerin döngüler ile birlikte kullanımı
## Dictionary de key lere erişim
## Dictionary de value lara erişim
## Dictionary de elemanlara (hem key hem de value) erişim
book1 = {
    "name" : "Suç ve Ceza",
    "author" : "Fyodor Dostoyevski",
    "page" : 784,
    "stock": 4,
    "publishYear":[1845,1920,1938,1995,2003],
    "trade":True
}
# for ile basit kullanımda sadece keys kullanılır
for x in book1:
    print(x)
# for ile basit kullanımda değerleri yazdırma işlemi
for x in book1:
    print(book1[x])
# for ile values() metodu kullanılarak değerlere ulaşılır
for x in book1.values():
    print(x)
# for ile keys() metodu kullanılarak değerlere ulaşılır
for x in book1.keys():
    print(x)
# for ile items() metodu kullanılarak hem key hem de value değerlerine ulaşılır
for x,y in book1.items():
    print(x,y, sep= " : ")