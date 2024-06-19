# İsteğe bağlı olarak hata oluşturmak için raise kullanılır. 
# Örneğin girilen sayı 100 den büyük olduğunda hata oluşturmak için raise kullanılır.
def colorize(text, color):
    colors = ("blue","red","white","black","orange")
    if type(text) is not str:
        # raise kullanımında hata tipini seçip, parantez içine hata mesajını yazdırılabilir.
        raise TypeError("text str tipinde olmalıdır.")

    if type(color) is not str:
        raise TypeError("renk str tipinde olmalıdır.")
    # Renklerin içinde olmadığında ValueError fırlatılmış
    if color not in colors:
        raise ValueError("geçersiz bir renk ismi.")

    print(f"{text} {color} olarak yazdırıldı.")

# try:
#     colorize("selam","yellow")
# except Exception as ex:
#     print(ex)

try:
    # Fonksiyon içinde bir hata varsa otomatik olarak geri döndürülür. Önemli!!!
    colorize("selam","red")
    colorize("selam","yellow")
except (TypeError,ValueError) as ex:
    print(ex)