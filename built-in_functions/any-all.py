# All ve Any boolean işlemlerde kullanılır. 
## All => and operatörü, Any => or operatörü

sonuclar = [True, False, True]
sonuc = all(sonuclar)
## Herhangi biri True olduğunda True döndürür
sonuc = any(sonuclar)

sayilar = [1,3,6,8,9,10]
sonuc = any([bool(sayi for sayi in sayilar)])
sonuc = all([bool(sayi for sayi in sayilar)])

sonuc = all([bool(sayi) for sayi in sayilar if sayi%2==1])
sonuc = all([sayi%2==0 for sayi in sayilar])
sonuc = any([sayi%2==0 for sayi in sayilar])

kisiler = ["ali","ahmet","çınar"]

sonuc = any([kisi[0]=='a' for kisi in kisiler])
sonuc = all([kisi[0]=='a' for kisi in kisiler if kisi[0]=='a'])
print(sonuc)