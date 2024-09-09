def selam(name):
    print("selam", name)

print(selam("Albert"))
selamlama = selam
print(selamlama("Albert"))
# Fonksiyonlar da bir object gibi değişkene atanabilir.
print(selam)
