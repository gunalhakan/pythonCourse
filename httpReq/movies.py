import requests

class theMovieDB:
    def __init__(self) :
        self.apiUrl = "https://api.themoviedb.org/3/"
        self.apiKey = "4166b10ffe6dda7a8431a59748cba3fd"
    def getPopulars(self):
        response = requests.get(f"{self.apiUrl}/movie/popular?api_key={self.apiKey}&language=en-US&page=1")
        return response.json()
    def getSearchResult(self,keyword):
        response = requests.get(f"{self.apiUrl}/search/keyword?api_key={self.apiKey}&query={keyword}&page=1")
        return response.json()


movieApi = theMovieDB()

while True:
    secim = input("1-Popular Movies\n2-Search Movies\n3-Exit\nSeçim: ")
    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            # print(movies)
            # print("-"*50)
            # print(movies['results'])
            # print("-"*50)
            # print()
            for movie in movies['results']:
                print(movie['title'])
                print("-"*50)
                
        elif secim == "2":
            keyword = input("Keyword : ")
            movies = movieApi.getSearchResult(keyword)
            for movie in movies["results"]:
                print("Results")
                print("*"*50)
                print(movie["name"])