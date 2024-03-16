import requests
import os

class Github :
    def __init__(self):
        self.apiURL = "https://api.github.com"
        self.tok = ""
        self.headers = {"Authorization": "tok "+self.tok}
    def githubUser(self,username):
        response = requests.get(self.apiURL+"/users/"+username)
        return response.json()
    def githubRepository(self, username):
        response = requests.get(self.apiURL+"/users/"+username+"/repos")
        return response.json()
    def createRepository(self,repoName):
        # response = requests.post(self.apiURL + "/user/repos?access_token=" + self.tok, json={
        response = requests.post(self.apiURL +"/user/repos", headers=self.headers, json={
            "name" : repoName,
            "description" : "first try for api",
            "homepage": "https://epsis.app",
            "private" : False,
            "has_issues" : True,
            "has_projects" : True,
            "has_wiki" : True
        })
        return response.json()
github = Github()
os.system("clear")
# secim = input("1-Find User\n2-Get Repositories\n3-Create Repository\n4-Exit\nSeçim :")
while True:
    secim = input("1-Find User\n2-Get Repositories\n3-Create Repository\n4-Exit\nSeçim :")
    if secim == "4":
        break
    else:
        if secim == "1":
            username = input("Username : ")
            result = github.githubUser(username)
            # print(result)
            print("name: ", result["name"])
            print("public repos: ", result["public_repos"])
            print("following: ", result["following"])
            # pass
        elif secim == "2":
            username = input("Username : ")
            result = github.githubRepository(username)
            # print(result)
            # pass
            for repo in result:
                print(repo["name"])
        elif secim == "3":
            name = input("Repository name : ")
            result = github.createRepository(name)
            print(result)
        else:
            print("Hatalı giriş yaptınız")
