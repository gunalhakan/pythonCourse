# Dictionary 1
## Dictionary tanımlama
## Dictionary değerlerine erişme
## Dictionary elemanlarına(hem key hem value), sadece key lere ve sadece değerlere erişme
## Dictionary key leri içinde bir değer arama
book1 = {
    "name" : "Suç ve Ceza",
    "author" : "Fyodor Dostoyevski",
    "page" : 784,
    "stock": 4,
    "publishYear":[1845,1920,1938,1995,2003],
    "trade":True
}
result = book1
result = book1["author"]
result = len(book1)
result = book1.get("publishYear")
result = book1.keys()
result = book1.values()
result = book1.items()
# in operatörü key lerin içinde arama yapar
if "page" in book1 :
    result = "page key lerin içinde var"
else:
    result = "page key lerin içinde yok"
print(result)
