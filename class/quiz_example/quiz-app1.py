# Her bir soruyu temsil edecek question nesnesi oluşturunuz.

# Question sınıfı
#   - text    => soru
#   - choices => cevap şıkları
#   - answer  => soru

# checkAnswer() metodu ile cevap kontrolü yapınız.

# q1.checkAnswer('cevap') => True
# q1.checkAnswer('cevap') => False

class Question:
    def __init__(self,text,choices,answer) :
        self.text = text
        self.choices = {
            "A":choices[0],
            "B":choices[1],
            "C":choices[2],
            "D":choices[3],
        }
        self.answer = answer
    def checkAnswer(self,userAnswer):
        if userAnswer not in self.choices.keys():
            raise ValueError ("hatalı cevap")
        
        return userAnswer == self.answer



q1 = Question("Yerçekimi kanununu bulan bilim adamı kimdir?", 
              ["Newton","Einstein","Faraday","Bernouli"],
              "A")
q2 = Question("Sanayi devrimi hangi ülkede başlamıştır?", 
              ["Fransa","ABD","İngiltere","Almanya"],
              "C")
q3 = Question("Dünyaca ünlü piyano sanatçımız hangisidir",
              ["Celal Şengör","Tarkan","Arda Güler","Fazıl Say"],
              "D")

print(q1.text)
# print(q1.choices)
# choices = q1.choices
for key,choice in q1.choices.items():
    print(key+" : "+choice)
print(q3.answer)
userAnswer = input("Seçiminize göre cevabınızı giriniz: ")
sonuc = q3.checkAnswer(userAnswer)
print(sonuc)