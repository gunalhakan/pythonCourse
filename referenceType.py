# Dictionary ler = operatörü ile kopyalandığında içindeki değerler değil, 
# referansları yani adresleri kopyalanır. 
# Bu durumda iki dictionary den birinde bir değişiklik yapıldığında 
# diğer dictionary de bu değişiklikten etkilenir. Çünkü adreslerin içindeki veri değişir
book1 = {
    "name" : "Suç ve Ceza",
    "author" : "Fyodor Dostoyevski",
    "page" : 784,
    "stock": 4,
    "publishYear":[1845,1920,1938,1995,2003],
    "trade":True
}
book2 = book1
print(book1["name"])
print(book2["name"])
# book1["name"]= "Savaş ve Barış"
book2["name"]= "Savaş ve Barış"
print("-"*20)
print(book1["name"])
print(book2["name"])