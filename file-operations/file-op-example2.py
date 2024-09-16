# Verileri dosyaya ekleyen fonksiyonu yazın
def veri_ekle(dosya_ismi,urun_adi,urun_fiyati):
    dosya_ismi = "file-operations/files/"+dosya_ismi
    with open(dosya_ismi,"a",encoding="utf-8") as file:
        file.write(f"ad : {urun_adi} - fiyat : {urun_fiyati}\n")    
    

def bul_degistir(dosya_ismi,aranan_kelime,yeni_kelime):
    dosya_ismi = "file-operations/files/"+dosya_ismi
    with open(dosya_ismi,"r+",encoding="utf-8") as file:
        text = file.read()
        yeni_text = text.replace(aranan_kelime,yeni_kelime)
        file.seek(0)
        file.write(yeni_text)
        # Yeni girilen kelime ile eski kelime arasındaki karakter sayısı farklı ise 
        # arada boşluk oluşuyor.
        # Bunu engellemek ve son kalan boşlukları atmak için truncate metodu kullanıldı
        # file.truncate()


# Dosya ismi eski kelime yeni kelime parametrelerini alarak 
# dosyadaki aranan kelimeyi yeni kelime ile değiştiren programı yazın.
# veri_ekle("cihazlar.txt","iphone 16",80000)
bul_degistir("cihazlar.txt","80000","88")
