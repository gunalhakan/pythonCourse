class Person():
    buYil = 2024
    # Class içindeki metodlarda self anahtar kelimesi kullanılmak zorundadır.
    # self class ı temsil eder, class içindeki metodlara erişmek için kullanılır.
    # Class içinde anımlanmış değişkenlere erişmek için Class_ismi kullanılır.
    # Örneğin burada buYil değişkenine erişmek için kullanılmış.
    # self parametresine bir argument gönderilmez.
    def yasHesapla(self,birthYear):
        yas = Person.buYil - birthYear
        print(yas)

p1 = Person()
# Metod yine nesne_adi.metod(arg) ile çağırılır, self e değer gönderilmez
p1.yasHesapla(2005)