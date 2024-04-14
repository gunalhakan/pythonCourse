'''
"player 1" 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
'''

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.

books = {
    "1": {
        "name" : "Savaş ve Barış",
        "author" : "Lev Tolstoy",
        "page" : 984,
        "stock" : 15
    },
    "2":{
        "name" : "Suç ve Ceza",
        "author" : "Fyodor Dostoyevski",
        "page" : 756,
        "stock" : 24,
    },
    "3":{
        "name" : "1984",
        "author" : "George Orwell",
        "page" : 323,
        "stock" : 6,
    },
    "4":{
        "name" : "Suskunlar",
        "author" : "İhsan Oktay Anar",
        "page" : 383,
        "stock" : 9,
    }
}
# print(books)
# print(books["1"]["name"])
# print(books["1"])
# for i,k in books["1"].items():
#     print(i,k)

# for book in books.values():
#     # print(book)
#     for key,value in book.items():
#         print (key,value, sep=":", end=" ")
#     print()

# 2- id' e göre arama yapınız.
id = input("Bulmak istediğiniz kitaba ait id yi giriniz: ")
arananKitap = books.get(id)
# print(arananKitap["name"])
# print(arananKitap.get("name"))
print(f"Aradığınız kitap : { arananKitap.get('name') } ")


# 3- id' e göre bilgi kayıt siliniz.
id = input("Silmek istediğiniz kitaba ait id yi giriniz: ")
silinenKitap = books.pop(id)
print(silinenKitap)
print(books)