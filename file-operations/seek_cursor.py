f = open("file-operations/files/m.txt")

# seek cursor un konumunu(karakter sayısı) belirlemek için kullanılır.
print(f.seek(80))
# readLine cursor ün bulunduğu konumdan itibaren sadece bulunulan satırı okur.
# readLines cursor ün bulunduğu konumdan itibaren tüm satırları okur ve dizi olarak döndürür.
## Okunacak satır kalmadığında read readLine ve readLines boş sonuç döndürürler.
## ilk çalıştırılan read tüm dökümanı okur, 2.kez çalıştığında okuyacak data bulamaz.
# print(f.read())
# print(f.readline())
f.seek(0)
# print(f.readlines())
satirlar = f.readlines()
print(satirlar)
for satir in satirlar:
    print(satir)

print(f.closed)
# Dosya close ile kapanır, closed ile kontrol edilir.
f.close()
print(f.closed)