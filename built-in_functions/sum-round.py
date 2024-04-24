# sum toplamak için kullanılır, round >5  üste yuvarlama,  <=5 alta yuvarlama için kullanılır
sayilar = [2,6,9,11,4,5]

sonuc = sum(sayilar)
# sayılar ve 10 u toplar
sonuc = sum(sayilar,10)

users = [
    {"username": "Hakan", "yas" : 42, "meslek" : "öğretmen"},
    {"username": "Seda", "yas" : 40, "meslek" : "öğretmen"},
    {"username": "Nİl", "yas" : 9, "meslek" : "öğrenci"},
    {"username": "Derya", "yas" : 44, "meslek" : "mühendis"},
    {"username": "Metin", "yas" : 46, "meslek" : "Bankacı"},
    {"username": "Kerem Poyraz", "yas" : 13, "meslek" : "öğrenci"},
]
sonuc = sum(user["yas"] for user in users) # list comprehensive
sonuc = sum(map(lambda user : user["yas"],users)) # lambda function
userCount = len([user for user in users if user["meslek"] == "öğretmen"])
print(userCount)

sonuc = round(10.2)
sonuc = round(10.5)
sonuc = round(10.6)
sonuc = round(10.424242)
sonuc = round(10.424242,2)
sonuc = round(10.426242,2)
sonuc = round(10.426242,2)
print(sonuc)