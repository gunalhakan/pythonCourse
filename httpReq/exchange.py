import requests
import os
apiKey = "09670e10c0d829c096e7784b"

url = f"https://v6.exchangerate-api.com/v6/{apiKey}/latest/"

os.system("clear")

bozulanDoviz = input("Bozdurulacak döviz türü: ") #USD
alinanDoviz = input("Alınacak döviz türü: ") #TRY

miktar = float(input(f"Ne kadar {bozulanDoviz} bozdurmak istiyorsunuz : "))

response = requests.get(url+bozulanDoviz)
sonuc_json = response.json()
# print(response.text)
# print("-"*50)
# print(sonuc_json)

# print(sonuc_json["conversion_rates"][alinanDoviz])
parite = sonuc_json["conversion_rates"][alinanDoviz]
print("1 {0} = {1} {2}".format(bozulanDoviz,parite,alinanDoviz))
print("{0} {1} = {2} {3}".format(miktar, bozulanDoviz, parite*miktar, alinanDoviz))

