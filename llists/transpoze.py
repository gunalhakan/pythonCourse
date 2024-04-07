liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[17, 18, 19]]
transpoze = []
for i in range(len(liste[0])):
    transpozeSatir = []
    for k in range(len(liste)):
        transpozeSatir.append(liste[k][i])
        print("T satir=>",transpozeSatir)
    print("transpoze",transpoze)
    transpoze.append(transpozeSatir)
print("-"*50)
print("transpoze => ", transpoze)