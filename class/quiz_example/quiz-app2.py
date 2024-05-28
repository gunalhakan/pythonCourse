# Her bir soruyu temsil edecek question nesnesi oluşturunuz.

# Question sınıfı
#   - text    => soru
#   - choices => cevap şıkları
#   - answer  => soru

# checkAnswer() metodu ile cevap kontrolü yapınız.

# q1.checkAnswer('cevap') => True
# q1.checkAnswer('cevap') => False

import random

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
class Quiz:
    def __init__(self,questions):
        # Soruları rastgele sırayla getirmek için sample kullanıldı.
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0

    def getQuestion(self):
        #soru listesinden bir soru al
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Soru {self.questionIndex + 1}: {question.text}")

        # print(question.choices)
        # print(type(question.choices))
        for key,choice in question.choices.items():
            print(key+") " + choice)



q1 = Question("Yerçekimi kanununu bulan bilim adamı kimdir?", 
              ["Newton","Einstein","Faraday","Bernouli"],
              "A")
q2 = Question("Sanayi devrimi hangi ülkede başlamıştır?", 
              ["Fransa","ABD","İngiltere","Almanya"],
              "C")
q3 = Question("Dünyaca ünlü piyano sanatçımız hangisidir?",
              ["Celal Şengör","Tarkan","Arda Güler","Fazıl Say"],
              "D")

#soruları liste içine at
sorular = [q1,q2,q3]
#sorular listesi ile quiz nesnesini oluştur.
quiz = Quiz(sorular)
#soruları görüntüle
quiz.displayQuestion()