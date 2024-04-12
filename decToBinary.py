dec = int(input("Lütfen bir sayı girin: "))

binary = ""
while dec > 0:
    binary = str(dec % 2) + binary
    dec = dec // 2

print(f"Girinlen sayının binary karşılığı : {binary}")