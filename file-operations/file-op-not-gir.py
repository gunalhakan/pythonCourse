def ortalama_hesapla(satir):
    satir= satir[:-1]
    # print(satir)
    liste = satir.split(":")
    # print(liste)
    
    # print("Öğrenci Notları: ", liste[1])
    ogrenci_adi = liste[0]
    notlar = liste[1].split("-")
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1 + not2 + not3)/3
    # print(ortalama)
    # print("Öğrenci Adı:", liste[0],"ortalaması",ortalama )

    if ortalama>=90 and ortalama<=100:
        harf = "AA"
    elif ortalama>=85 and ortalama<=89:
        harf = "BA"
    elif ortalama>=80 and ortalama<=84:
        harf = "BB"
    elif ortalama>=75 and ortalama<=79:
        harf = "CB"
    elif ortalama>=70 and ortalama<=74:
        harf = "CC"
    elif ortalama>=65 and ortalama<=69:
        harf = "DC"
    elif ortalama>=60 and ortalama<=64:
        harf = "DD"
    elif ortalama>=50 and ortalama<=59:
        harf = "FD"
    else:
        harf = "FF"

    return ogrenci_adi + ": " + harf + "\n"

def notlariGor():
    with open("file-operations/files/notlar.txt","r",encoding="utf-8") as file:
        bilgiler = file.readlines()
        # print(bilgiler)
        for bilgi in bilgiler:
            print(ortalama_hesapla(bilgi))

def notGirisiYap():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = input("Not1 girin: ")
    not2 = input("Not2 girin: ")
    not3 = input("Not3 girin: ")
    with open("file-operations/files/notlar.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+":"+not1+"-"+not2+"-"+not3+"\n") 

def notlariKaydet():
    pass
while True:
    islem = input("1- Notları Görüntüle\n2-Not Giriş Yap\n3-Notları Kaydet\n4-Çıkış Yap")
    if islem == "1":
        notlariGor()
    elif islem == "2": 
        notGirisiYap()
    elif islem == "3":
        notlariKaydet()
    else:
        break