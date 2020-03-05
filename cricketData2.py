import requests
from bs4 import BeautifulSoup

url="https://www.espncricinfo.com/table/series/8048/season/2019/ipl"
response=requests.get(url)
print(response.text)

soup=BeautifulSoup(response.text,"html.parser")
print(soup.prettify())



class MatchData:
    def __init__(self,teamNames=None,totalMatches=None,matcWon=None,matchlose=None):
        self.teamNames=teamNames
        self.totalMatches=totalMatches
        self.matchWon=matcWon
        self.matchlose=matchlose



    def showData(self):
        teams = []
        team = soup.find_all("span", class_="team-names")
        for t in team:
            c = t.text.strip()
            teams.append(c)
        print(teams)
        print("{}|{}|{}|{}".format(self.teamNames,self.totalMatches,self.matchWon,self.matchlose))



    def toCSV(self):
        return "{},{},{},{}\n".format(self.teamNames, self.totalMatches, self.matchWon, self.matchlose)

    def saveData(self):
        file = open("cricData.csv", "a")
        crickData = self.toCSV()
        file.write(crickData)
        file.close()



m1=MatchData()

m1.showData()