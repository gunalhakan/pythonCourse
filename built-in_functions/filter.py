#fonksiyona gönderilen veriler şarta göre filtrelenir ve geri döndürülür
# filter iterable dır. For ile kullanılabilir
yaslar = [9,16,21,43,51,4]

def yetiskin(x):
    if x < 18 :
        return False
    else:
        return True
    
sonuc = list(filter(yetiskin, yaslar))
sonuc = list(filter(lambda x : x >= 18, yaslar))
sonuc = list(filter(lambda x : x % 2 == 1, yaslar))

isimler = ["Hakan","Seda", "Tolga", "Metin","Nil", "Derya"]
# ilk harfleri H veya N olanları filter ile al
filteredResults = filter(lambda x : x[0] == "H" or x[0]== "N", isimler)
# filtrelenmiş sonuçları upper yap ;)
sonuc = list(map(str.upper, filteredResults))

users = [
    {"username": "Hakan", "yas" : 42, "meslek" : "öğretmen"},
    {"username": "Seda", "yas" : 40, "meslek" : "öğretmen"},
    {"username": "Nİl", "yas" : 9, "meslek" : "öğrenci"},
    {"username": "Derya", "yas" : 44, "meslek" : "mühendis"},
    {"username": "Metin", "yas" : 46, "meslek" : "Bankacı"},
    {"username": "Kerem Poyraz", "yas" : 13, "meslek" : "öğrenci"},
]
sonuc = list(filter(lambda x : x["yas"]<18,users))
sonuc = list(map(lambda x : x["username"].upper(),filter(lambda x : x["yas"]>18,users)))
print(sonuc)
