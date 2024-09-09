def toplam(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islemAdi):
    if islemAdi == "toplama":
        print(f1(10,2))
    elif islemAdi == "cikarma":
        print(f2(10,2))
    elif islemAdi == "carpma":
        print(f3(10,2))
    elif islemAdi == "bolme":
        print(f4(10,2))
    else:
        print("Geçersiz İşlem")

islem(toplam,cikarma,carpma,bolme,"toplama")
islem(toplam,cikarma,carpma,bolme,"cikarma")
islem(toplam,cikarma,carpma,bolme,"carpma")
islem(toplam,cikarma,carpma,bolme,"bolme")