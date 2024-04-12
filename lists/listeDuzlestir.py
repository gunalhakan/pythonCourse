# 2 boyutlu bir liste oluşturun ve bu listeyi tek boyutlu bir listeye dönüştürün
liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
duzListe = []
gecici = [liste]

while gecici:
    print("geçici =>", gecici)
    #gecici liste içindeki son elemanı listeIc e aktar
    listeIc = gecici.pop()
    #listeIc in içindeki elemanları dolaş
    for eleman in listeIc:
        #eğer eleman yeni bir liste ise 
        if isinstance(eleman,list):
            #gecici nin içine listeyi aktar
            gecici.append(eleman)
        #eğer eleman liste değilse
        else:
            #duz listeye elemanı aktar
            duzListe.append(eleman)
            print(duzListe)

print(liste)
print("-"*10)
print(duzListe)