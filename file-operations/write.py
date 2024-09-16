# file = open("file-operations/files/newFile.txt","w",encoding="utf-8")
# Eğer var olan dosyayı açarsak olan silinir yerine yenisi oluşturulur.
with open("file-operations/files/newFile.txt","w",encoding="utf-8") as file:
    file.write("Hakan\n")
    file.write("Seda\n")
    print(file)
    