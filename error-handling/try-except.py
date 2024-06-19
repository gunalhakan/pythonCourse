# Olası hataların alınacağı bölüm try içine
try:
    sayi1 = int(input("1. sayıyı giriniz: "))
    sayi2 = int(input("2. sayıyı giriniz: "))
    print(sayi1 + sayi2)
# Hata yakalandığında yapılacak işler except bölümüne yazılır.
except:
    print("Bir hata oluştu")