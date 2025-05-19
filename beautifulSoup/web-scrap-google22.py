import requests
from bs4 import BeautifulSoup

# search_input = input('aramak istediğiniz kelime: ').replace(' ','+')
# link = "https://www.google.com/search?q=" + search_input
link = "https://www.google.com/search?q=python" 

# headerParams = {"user-agent":"Mozilla/,5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
headerParams = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0"}

response = requests.get(link, headers = headerParams)
print(response)

soup = BeautifulSoup(response.content,"html.parser")
# print(soup)

results = soup.find_all('div', class_="MjjYud")
# say = 0
for div in results:
    # say +=1
    anchor = div.find('a')

    link = anchor['href']
    text = anchor.find('h3').string
    description = anchor.parent.next_sibling.find('span').text

    print( link + "*** " + text + "*** " + description)
    print('*******************')