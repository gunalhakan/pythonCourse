import requests

response = requests.post("https://jsonplaceholder.typicode.com/posts", data = {
        "title": 'deneme',
        "body": 'deneme',
        "userId": 1,
    }
)
# 201 Created Döner
sonuc = response
# Post ile eklenen veri döner, id = 101 otomatik atandı
sonuc = response.text
#sonucu json a dönüştürür
sonuc = response.json()

print(sonuc)