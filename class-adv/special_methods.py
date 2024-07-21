liste = [1,2,3]
print(len(liste))

s = "hello world"
print(len(s))

class Film:
    def __init__(self,baslik,yonetmen,sure):
        self.baslik = baslik
        self.yonetmen = yonetmen
        self.sure = sure
    # Diğer class larda kullanılabilen str ve len gibi metodları kendi class ımızda kullanmak için 
    # aşağıdaki gibi str ve len metodları hazırlanıp kullanılır.
    def __str__(self):
        return f"{self.baslik} filmi {self.yonetmen} tarafından yönetildi"
    
    def __repr__(self):
        return f"{self.baslik} filmi {self.yonetmen} tarafından yönetildi" 
    
    def __len__(self):
        return self.sure
    
    def __del__(self):
        print("isimli film silindi")
    

    

f = Film("mayıs sıkıntısı","nuri bilge ceylan",168)

# print(f.baslik)
print(str(f))
print(len(f))
del f
print(f)
