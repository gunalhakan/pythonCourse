import requests

url = "http://api.weatherapi.com/v1/current.json"
apiKey = "<API_KEY>"
sehir = input("Durumunu görmek için şehir ismi girin: ")

response = requests.get(url, params={
    "key" : apiKey,
    "q" : sehir,
    "lang" : "tr"
})

havaDurumu = response.json()

sehir = havaDurumu["location"]["name"]
sicaklik = havaDurumu["current"]["temp_c"]
durum = havaDurumu["current"]["condition"]["text"]
print(f"{sehir}, şu anda {sicaklik} derece ve {durum}.")
