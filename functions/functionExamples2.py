# 1- Kendisine gönderilen 2 sayıdan hangisinin büyük olduğunu bulan fonksiyonu yazın
# def findBigger(sayi1, sayi2):
#     if sayi1 > sayi2 :
#         return sayi1
#     elif sayi2 > sayi1:
#         return sayi2
#     else:
#         return "sayılar eşit"
    
# findBigger(2,6)

# 2- Kendisine gönderilen bir kelime içinde her harften kaç adet var bulan fonksiyonu yazın

# def findCharInWord(word):
#     # print(word.count("a"))
#     # for char in word:
#     #     print(char)

#     return { char: word.count(char) for char in word }

# print(findCharInWord("Hakan"))

# 3- Kendisine gönderilen list, command, position ve value bilgilerine göre liste üzerinde güncelleme yapınız.
  # [1,2,3], ("add, remove"), ("beginning | end"), value 
  # list_operation([1,2,3],"add","end","4") => [1,2,3,4]
  # list_operation([1,2,3],"remove","beginning") => [2,3]

# def update_list(liste, command, position, value=None):
#     if (command == "remove" and position == "end"):
#         return liste.pop()
#     elif (command=="remove" and position=="beginning"):
#         return liste.pop(0)
#     elif (command=="add" and position=="end"):
#         liste.append(value)
#         return liste
#     elif (command =="add" and position=="beginning"):
#         liste.insert(0,value)
#         return liste

# sonuc = update_list([1,2,3], "add", "end", 4)
# print(sonuc)
# sonuc = update_list([1,2,3], "add", "beginning", 4)
# print(sonuc)
# sonuc = update_list([1,2,3], "remove", "beginning")
# print(sonuc)
# sonuc = update_list([1,2,3], "remove", "end")
# print(sonuc)

# 4- Kendisine gönderilen renk isimlerinden içinde "blue" rengi varsa True döndüren fonksiyonu yazınız.

def contains_blue(*args):
    if "blue" in args: 
        return True
    return False

sonuc = contains_blue("blue","yellow","red")
print(sonuc)
sonuc = contains_blue("green","yellow","red","black")
print(sonuc)