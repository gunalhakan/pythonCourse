# Dictionary 4
## İç içe dictionary
books = {
    "book1":{
        "name" : "Suç ve Ceza",
        "author" : "Fyodor Dostoyevski",
        "stock": 4,
        
    },
    "book2":{
        "name" : "Faust",
        "author" : "Johan Wolfgang Goethe",
        "stock": 9,
    },
    "book3":{
        "name" : "Hayvan Çiftliği",
        "author":"George Orwell",
        "stock": 7,
    },
    "book4":{
        "name" : "İnce Memed",
        "author":"Yaşar Kemal",
        "stock": 3,
    }
}
print(books)
book5 = {
    "name" : "Sefiller",
    "author":"Victor Hugo",
    "stock": 4,
}
books = {
    "book5" : book5
}
print(books)