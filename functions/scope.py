from os import system
system("clear")

# ana programda değişkenler fonksiyonlarda kullanılabilir, 
# ancak fonksiyonlarda ana programda tanımlanan değişkenlere yeni değer atanamaz.
# global değişkeni ana programda yeniden kullanırsak hangi değeri alacak sorununa cevap :)
'''
sayi = 11

def yaz(): 
    sayi = sayi * 2 # bu satır hata verecektir
    sayiYeni = sayi * 2
    print("fonksiyon = ", sayiYeni)

yaz()
'''
# ana programda tanımlanan değişkenler ile fonksiyonda kullanılan değişkenler aynı isimde olduklarında 
# bulundukları konuma göre değer alırlar.
'''
sayi = 11

def yaz(): 
    sayi = 21
    print("fonksiyon = ", sayi)

yaz()
print("ana program = ", sayi)
'''
#fonksiyonda tanımlanan bir değişkenin ana programda çalışması istenirse
# bu değişken global anahtar kelimesi ile birlikte tanımlanmalıdır.
'''
sayi = 11

def yaz(): 
    global sayi 
    sayi = 21
    print("fonksiyon = ", sayi)

yaz()
print("ana program = ", sayi)
'''