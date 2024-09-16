def dosya_kopyala(dosya_ismi,yeni_dosya_ismi):
    dosya_ismi = "file-operations/files/"+dosya_ismi
    with open(dosya_ismi,"r",encoding="utf-8") as file:
        veriler = file.read()
        # print(veriler)
    yeni_dosya_ismi = "file-operations/files/"+yeni_dosya_ismi
    with open(yeni_dosya_ismi,"w",encoding="utf-8") as file:
        file.write(veriler)

def dosya_terscevir(dosya_ismi,ters_dosya_ismi):
    dosya_ismi = "file-operations/files/"+dosya_ismi
    with open(dosya_ismi,"r",encoding="utf-8") as file:
        veriler = file.readlines()
        # print(veriler)
        veriler.reverse()
        # print(veriler)

    ters_dosya_ismi = "file-operations/files/"+ters_dosya_ismi
    with open(ters_dosya_ismi,"r+",encoding="utf-8") as file:
        
        # file.writelines(veriler)
        # Karakter karakter ters yazdırır.
        icerik = file.read()
        file.write(icerik[::-1])
# {satır sayisi : 4, kelime sayisi:6, karakter sayısı : 24} gibi
def dosya_bilgileri(dosya_ismi):
    dosya_ismi = "file-operations/files/"+dosya_ismi
    with open(dosya_ismi,"r",encoding="utf-8") as file:
        satirlar = file.readlines()
        # kelime sayısı
        # kelime_sayisi = 0
        # for satir in satirlar:
        #     satir_kelime_sayisi = len(satir.split(' '))
        #     kelime_sayisi = kelime_sayisi + satir_kelime_sayisi

        # list comprehensive
        kelime_sayisi = sum(len(satir.split(' ')) for satir in satirlar)

        #karakter sayısı
        # file.seek(0)
        # file.read()
        # karakter_sayisi = file.tell()

        # karakter sayısı 
        # list comprehensive
        karakter_sayisi = sum(len(satir) for satir in satirlar)
        
        sonuc = {
            "satir_sayisi": len(satirlar),
            "kelime_sayisi": kelime_sayisi,
            "karakter_sayisi": karakter_sayisi

        }
        print(sonuc)
        # return sonuc

# dosya_kopyala("arabalar.txt","arabalar2.txt")
# dosya_terscevir("arabalar.txt","arabalar-ters.txt")
dosya_bilgileri("newFile.txt")