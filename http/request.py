import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

#Response ve 200 kodunu döndürür
sonuc = response
# Dönen response objectinin tipini döndürür
sonuc = type(response)
# durum kodunu döndürür
sonuc = response.status_code
# header bilgilerini döndürür
sonuc = response.headers
# dönen verinin content-type ini gösterir
sonuc = response.headers["Content-Type"]
sonuc = response.url
# dönen verinin dil kodlamasını döndürür
sonuc = response.encoding
# Dönen verinin içeriği (body)
sonuc = response.text
# response.text ile gelen veriyi dictionary e dönüştürür
todos = json.loads(response.text)
# Dönen veri bir liste içindeki dictionary verisi olduğu için ilk elemanın title bilgisini yazar
sonuc = todos[0]["title"]

# userId 1 olan todo ların başlıklarını yazar.
for item in todos:
    if (item["userId"]==1):
        print(item["title"])

print(sonuc)