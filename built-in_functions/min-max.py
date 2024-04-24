# En büyük ve En küçük değerleri bulmak için kullanılır.
yaslar = [42, 40, 9, 44, 46, 13]

sonuc = min(yaslar)
sonuc = max(yaslar)

harfler = ['h', 's', 'n', 'd', 'm', 'k']
sonuc = min(harfler)
sonuc = max(harfler)

isimler = ['hakan', 'seda', 'ni̇l', 'derya', 'metin', 'kerem poyraz']
sonuc = min(isimler)
sonuc = max(isimler)

sonuc = min(isimler, key= lambda isim : len(isim))
sonuc = max(isimler, key= lambda isim : len(isim))

users = [
    {"username": "Hakan", "yas" : 42, "meslek" : "öğretmen"},
    {"username": "Seda", "yas" : 40, "meslek" : "öğretmen"},
    {"username": "Nİl", "yas" : 9, "meslek" : "öğrenci"},
    {"username": "Derya", "yas" : 44, "meslek" : "mühendis"},
    {"username": "Metin", "yas" : 46, "meslek" : "Bankacı"},
    {"username": "Kerem Poyraz", "yas" : 13, "meslek" : "öğrenci"},
]
sonuc = min(users, key= lambda user : user["yas"])
sonuc = max(users, key= lambda user : user["yas"])

sonuc = min(users, key= lambda user : user["yas"])["username"]
sonuc = max(users, key= lambda user : user["yas"])["username"]
print(sonuc)


# sonuc = list(map(lambda user : user["username"].lower(), users))
# print(sonuc)
# sonuc = list(map(lambda user : user["yas"], users))