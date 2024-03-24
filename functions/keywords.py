def bilgi(mail,yas):
    #keyword kullanımında parametre sırası fark etmez.
    return f"mail adresiniz : {mail}, yaşınız : {yas}"

sonuc = bilgi(yas = 38, mail = "hakan@epsis.app")
print(sonuc)