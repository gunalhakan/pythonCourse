# Comment isminde bir sınıf oluşturunuz.
# Comment sınıfı username, text, likes, dislikes isminde özelliklere sahip olsun.
# 5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız.

class Comment:
    def __init__(self, username, text, likes=0, dislikes=0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes


c1 = Comment("Hakan","güzel kurs")
c2 = Comment("Nilay","çok güzel kurs")
c3 = Comment("Akif","idare eder bir kurs", 50, 10)
c4 = Comment("Osman","kursu beğenmedim")
c5 = Comment("Neslihan","süper bir kurs olmuş",100)

# her oluşan nesneyi bir listeye at, böylece iterable olur ;)
comments = [c1,c2,c3,c4,c5]

#her elemanı sırayla c nin içine at ve tek tek yazdır.
for c in comments:
    #apple simgesi shift + alt + k :D:D :D:D
    print(f"{c.username} : {c.text} -> likes : {c.likes} dislikes : {c.dislikes}" )

# for c in comments:
#     print(f"{c.username}: {c.text}")
#     print(f"likes: {c.likes} - dislikes: {c.dislikes}")