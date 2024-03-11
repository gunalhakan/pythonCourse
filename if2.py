sicaklik = float(input("Sıcaklık Değeri Girin: "))

print("-"*50)
if sicaklik <= 0:
    print("Katı")
elif sicaklik <= 100 :
    print("Sıvı")
else:
    print("Gaz")

print("-"*50)
print("Program bitti")