#Klavyeden 10 basamağa kadar girilen sayıyı basamaklarına ayıran program

sayi = int(input("Bir sayı girin: "))
sayac = 10
while sayac > -1 or bolum < 1:
    bolum = sayi // (10 ** sayac) 
    print(f"10 üzeri {sayac} basamağı = {bolum}")
    sayi = sayi % (10**sayac)
    sayac -= 1