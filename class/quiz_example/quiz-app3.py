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
        # Gelen soru listesinden quiz i üret
        # Soruları rastgele sırayla üretmek için sample kullanıldı.
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        #soru listesinden bir soru al
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Soru {self.questionIndex + 1}: {question.text}")


        for key,choice in question.choices.items():
            print(key+") " + choice)

        userAnswer = input('cevap: ')
        if (question.checkAnswer(userAnswer)):
            self.score += 1

        self.questionIndex += 1

        if (len(self.questions) == self.questionIndex) :
            print(self.score)
        else:
            self.displayQuestion()


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