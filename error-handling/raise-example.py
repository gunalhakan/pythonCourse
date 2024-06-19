# 1- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.
# negatif, harf hataları

# def faktoriyel(sayi):
#     sayi = int(sayi)

#     if sayi < 0 :
#         raise ValueError("Sayı negatif olamaz")
    
#     sonuc = 1
#     for i in range(1,sayi+1):
#         sonuc = sonuc * i
    
#     return sonuc

# for i in [4,6,-3,"5a",5,"c3"]:
#     try:
#         x =faktoriyel(i)
#     except ValueError as e:
#         print(e)
#         continue
#     else:
#         print(x)

# 2- Girilen parola içinde türkçe karakter hatası veriniz.
def parolaKontrol(parola):
    turkce_karakterler = "ıİŞşÇçÖöÜüĞğ"
    for i in parola:
        if i in turkce_karakterler:
            raise ValueError("Parola Türkçe karakter içeremez")
        
    print(f"parolanız => <{parola}> geçerlidir")

parola = input("Parolanızı giriniz: ")
try:
    parolaKontrol(parola)
except Exception as e:
    print(e)
