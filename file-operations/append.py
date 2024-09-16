# a : append modu, dosyanın sonuna ekleme yapar
# with open("file-operations/files/newFile.txt","a",encoding="utf-8") as file:
#     file.write("Nil\n")
#     print(file)

# r+ : read, write modu, dosyanın başına ekleme yapar, ilk satırdaki karakterleri silip ekler.
with open("file-operations/files/newFile.txt","r+",encoding="utf-8") as file:
    # file.seek(5)
    # read imleci sona konumlandırır, böylece sona ekleyebiliriz.
    file.read()
    file.write("Nil\n")
    print(file)