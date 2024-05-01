# 1-  "Samsung S5,Samsung S6,Samsung S7,Samsung S8" elemanlarına sahip bir liste oluşturunuz.
telefonlar = ["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]
if "Samsung S5" in telefonlar:
    print("var")
else :
    print("yok")
# 2-  Liste Kaç elemanlıdır ?
# print(len(telefonlar))

# 3-  Listenin ilk ve son elemanı nedir ?
# print(telefonlar[0])
# print(telefonlar[-1])
# print(telefonlar[len(telefonlar)-1])
# 4-  "Samsung S5" değerini "Samsung S9" ile değiştirin.
# telefonlar[0]="Samsung S9"


# 5-  "Samsung S6" listenin bir elemanı mıdır ?
# if "Samsung S6" in telefonlar:
#     print("Evet listenin elemanıdır")

# 6-  Listenin -3 indeksindeki değer nedir ?
# print(telefonlar[-3])
# 7-  Listenin ilk 2 elemanını alın.
# print(telefonlar[:2])
# 8-  Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.
# telefonlar[-1] = "Samsung S10"
# telefonlar[-2] = "Samsung S9"
#-- telefonlar[-2:] = ["Samsung S9","Samsung S10"]

# 9-  Listenin üzerine "IPhone X" ve "IPhone XR" değerlerini ekleyin.
# telefonlar = telefonlar + ["IPhone X", "IPhone XR"]

# 10- Listenin son elemanını silin.
# telefonlar.pop()
# del telefonlar[-1]
# 11- Liste elemanlarını tersten yazdırınız.
# print(telefonlar[::-1])

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 
    # kullaniciA: Yiğit Bilgi 2010, (70,60,70)
    # kullaniciB: Sena Turan  1999, (80,80,70)
    # kullaniciC: Ahmet Turan 1998, (80,70,90) 
# kullaniciA = ["Yiğit", "Bilgi", 2010, [50,60,70]]
# kullaniciB = ["Sena", "Turan", 1999, [80,90,100]]
# kullaniciC = ["Ahmet", "Turan", 1998, [80,70,90]]

# kullanicilar = [kullaniciA,kullaniciB,kullaniciC]
# print(kullanicilar)
# 13- Yukarıdaki Liste elemanlarını ekrana yazdırınız.

# for kullanici in kullanicilar:
#     for bilgi in kullanici:
#         print(bilgi, end=" /")
#     print()
# ortalama = 0
# for kullanici in kullanicilar :
#     ortalama = (kullanici[3][0] + kullanici[3][1] + kullanici[3][2] ) /3
#     print(f"ad : {kullanici[0]} - soyad : {kullanici[1]} - yaş : {2024-kullanici[2]} - notlar : {ortalama}"
#     )

# print(telefonlar)