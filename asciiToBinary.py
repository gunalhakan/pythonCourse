kelime = input("Lütfen bir kelime girin: ")

binary_kelime = ""
ascii_kelime = ""
for harf in kelime:
    ascii_deger = ord(harf)
    binary_harf = ""
    ascii_kelime += str(ascii_deger) + "/"
    for i in range(8):
        binary_harf = str(ascii_deger % 2) + binary_harf
        ascii_deger //= 2
    binary_kelime += binary_harf + " "
    

print("Girilen kelimenin binary karşılığı:", binary_kelime)
print("Girilen kelimenin ascii karşılığı:", ascii_kelime)