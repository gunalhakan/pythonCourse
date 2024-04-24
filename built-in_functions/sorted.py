# sıralama yapmak için kullanılır. 
sayilar = [1,53,45,67,97,5,7]

# sayilar.sort()
sonuc = sorted(sayilar)
sonuc = sorted(sayilar, reverse=True)
sonuc = sorted((1,53,45,67,97,5,7))

users = [
    {"username": "Hakan", "yas" : 42, "meslek" : "öğretmen"},
    {"username": "Seda", "yas" : 40, "meslek" : "öğretmen"},
    {"username": "Nİl", "yas" : 9, "meslek" : "öğrenci"},
    {"username": "Derya", "yas" : 44, "meslek" : "mühendis"},
    {"username": "Metin", "yas" : 46, "meslek" : "Bankacı"},
    {"username": "Kerem Poyraz", "yas" : 13, "meslek" : "öğrenci"},
]
# eleman uzunluklarına göre listeler
sonuc = sorted(users,key=len)
# user ın yas bilgisine göre sıralar
sonuc = sorted(users, key= lambda user : user["yas"], reverse= True)
# user ın yas bilgisine göre sıralar, sadece meslekleri  yazdırır.
sonuc = list(map(lambda user : user["meslek"],sorted(users,key=lambda user : user["yas"])))
print(sonuc)
# users a ait username in uzunluklarına göre users ı sıralar, tüm elemanlarını gösterir
sonuc = sorted(users,key= lambda user : len(user["username"]))
# users a ait username in uzunluklarına göre users ı sıralar, sadece username i gösterir
sonuc = list(map(lambda user : user["username"],sorted(users, key= lambda user : len(user["username"])) ))
print(sonuc)