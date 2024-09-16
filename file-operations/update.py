# Alttaki durumdaki dosyaya 1- toyota eklenecektir.
"""
2-Opel
4-BMW
5-Mercedes
"""
# with open("file-operations/files/arabalar.txt","r+",encoding="utf-8") as file:

#     # print(file.read())
    
#     markalar = file.read()
#     # print(markalar)
#     markalar = "1- Toyota\n" + markalar
#     file.seek(0)
#     file.write(markalar)

# Alttaki durumdaki dosyaya 3- Ford eklenecektir.
"""
1-Toyota
2-Opel
4-BMW
5-Mercedes
"""
with open("file-operations/files/arabalar.txt","r+",encoding="utf-8") as file:
    markalar = file.readlines()
    print(markalar)
    markalar.insert(2,"3- Ford\n")
    file.seek(0)
    # write string olarak çalışır, writelines liste halinde verileri satır satır ekler.
    file.writelines(markalar)
    
        