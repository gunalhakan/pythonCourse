isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
# isimler.append("Cenk")

# 2-  "Sena" değerini listenin başına ekleyiniz.
# isimler.insert(0,"Sena")
# isimler.insert(-1,"Sena")
# isimler.insert(len(isimler),"Sena")

# 3-  "Yiğit" ismini listeden siliniz.
# isimler.remove("Yiğit")

# 4-  "Yiğit" isminin indeksi nedir ?
# print(isimler.index("Yiğit"))

# 5-  "Beril" listenin bir elemanı mıdır ?
# if "Beril" in isimler:
    # print("Beril listenin içindedir")
# sonuc = "Beril" in isimler
# print(sonuc)

# 6-  Liste elemanlarını ters çevirin.
# isimler.reverse()
# yaslar.reverse()
# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
# isimler.sort()

# 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.
# yaslar.sort(reverse=True)

# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.
# s = "IPhone X ,IPhone XR"
# result = s.split(",")
# print(result)

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
# print(max(yaslar))
# print(min(yaslar))

# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?
# print(yaslar.count(1998))

# 12- yaslar dizisinin tüm elemanlarını siliniz.
# yaslar.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
# markalar = []
# for i in range(3):
#     markalar.append(input("Marka girin :"))

# print(markalar)
print(isimler)
print(yaslar)
