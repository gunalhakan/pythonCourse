# BankaHesap isminde bir sınıf tanımlayınız.
# Üretilen her bir nesne owner isminde biz özelliğe sahip olmalıdır. BankaHesap("Hakan Günal")
# Üretilen her bir nesne balance isminde bir özelliğe sahip olup başlangıçta gönderilen miktarda değere olmalıdır.
# Üretilen her bir nesne için paraYatir metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp balance
# üzerine ekleyin ve balance miktarını geriye döndürün.
# Üretilen her bir nesne için paraCek metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp balance
# değerinden çıkarıp geriye döndürün.

# hesap = BankaHesap("Hakan Günal")
# hesap.owner => Hakan Günal
# hesap.balance => 0.0
# hesap.paraYatir(1000) => 1000.0
# hesap.paraCek(500) => 500.0

class BankaHesap:
    activeUser = 0
    def __init__(self,name,balance):
        self.owner = name
        self.balance = balance
        #Bir class içindeki attribute lere ulaşmak için class_ismi.attribute kullanılır.
        BankaHesap.activeUser += 1
        print(BankaHesap.activeUser)
        

    def bakiyeGoster(self):
        return self.balance

    def paraYatir(self,amount):
        self.balance += amount
        return self.balance

    def paraCek(self,amount):
        self.balance -= amount
        return self.balance
    
    def cikis(self):
        BankaHesap.activeUser -= 1
        

hesap = BankaHesap("Hakan Günal",5000)
hesap2 = BankaHesap("Zeynep Yılmaz",10000)
hesap3 = BankaHesap("Koray Candemir ",12000)

print(hesap.bakiyeGoster())
hesap.paraYatir(1000)
print(hesap.bakiyeGoster())
hesap.paraCek(500)
print(hesap.bakiyeGoster())
print(hesap.activeUser)
print(hesap2.activeUser)
hesap3.cikis()
print(hesap.activeUser)