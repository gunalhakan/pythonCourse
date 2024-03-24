# 1- Kendisine gönderilen bir kelimeyi ekranda istenilen sayıda yazan fonksiyonu yazın

# def yaz(kelime="", adet=0):
#     for i in range(adet):
#         print(kelime)
# yaz("deneme", 5)

# 2- Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazın

# def alanCevre(a=0,b=0):
#     alan = a*b
#     cevre = 2*(a+b)
#     print(f"Çevre = {cevre}, Alan = {alan}")

# alanCevre(4,6)

# 3- Yazı Tura uygulamasını fonksiyon kullanarak yapınız.(import modülü kullan)

# def yaziTura():
#     import random
#     yt = ["yazi","tura"]
#     return random.choice(yt)

# sonuc = yaziTura()
# print(sonuc)


# 4- Kendisine gönderilen 2 sayı arasındaki asal sayıları bulan fonksiyonu yazın

# def asalSayiBul(sayi1,sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1 :
#             for i in range(2,sayi):
#                 if sayi % i == 0:
#                     #eğer tam bölünüyorsa döngüden çık
#                     break
#             else :
#                 print(f"{sayi} sayısı asaldır")
#                 # print(sayi)
#         else:
#             print("1 den büyük sayı girin:")

# asalSayiBul(120,155)
# 5- Kendisine gönderilen 1 sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazın

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if sayi % i == 0:
            tamBolenler.append(i)
        
    return tamBolenler

print(tamBolenleriBul(120))

