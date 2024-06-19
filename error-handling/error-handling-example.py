liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulup liste2 ye ekleyiniz.

# liste2=[]
# for v in liste:
#     try:
#         sonuc = int(v)
#         # print(sonuc)
#         liste2.append(sonuc)
#     except Exception as e:
#         # print(e)
#         continue
# print(liste2)

# 2: Kullanıcı 'quit (q)' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazın.

# while True:
#     value = input("Değer girin: ")
#     if value == "q":
#         break
#     # Alttaki else i yazsak da yazmasak da olur. Önemli !!!
#     else:
#         try:
#             value = int(value)
#             print(value)
#         except ValueError as e:
#             print(e)
#             continue


# 3: Dictionary ve key bilgilerini parametre olarak alan ve 
# alttaki dictionary ile karşılaştıran bir  get(d, key) fonksiyonu hazırlayınız.

urun = {"ad":"Yumurta","fiyat":6}
def get(d, key):
    try:
        return d[key]
    except KeyError as e:
        return e, None

print(get(urun,"ad"))
print(get(urun,"yas"))