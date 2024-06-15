import requests

headlineURL = "https://newsapi.org/v2/top-headlines"
everythingURL = "https://newsapi.org/v2/everything"
apiKey = "<API_KEY>"
country = "tr"


# response = requests.get(headlineURL,params={
#     "apiKey" : apiKey,
#     "country": country
# })

response = requests.get(everythingURL,params={
    "apiKey" : apiKey,
    "q" : "kripto",
    "language" : "tr",
    "sortBy":"publishedAt"
})


haberler = response.json()["articles"]
# print(haberler.status)

# print(haberler[0])
# print(haberler[1])
# print(haberler[0]["source"]["name"])
# print(haberler[0]["title"])

print()


for haber in haberler:
    print(haber["source"]["name"],"-",haber["title"])
