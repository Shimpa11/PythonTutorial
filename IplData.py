import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Team:
    def __init__(self, year, teamName, matches, won, lost, tied, abandoned, points, netRunRate, forScore, againstScore):

        self.year = year
        self.teamName = teamName
        self.matches = matches
        self.won = won
        self.lost = lost
        self.tied = tied
        self.abandoned = abandoned
        self.points = points
        self.netRunRate = netRunRate
        self.forScore = forScore
        self.againstScore = againstScore

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{}\n".format(self.year, self.teamName, self.matches, self.won, self.lost, self.tied, self.abandoned, self.points, self.netRunRate, self.forScore, self.againstScore)



class FetchTeamsData:

    def fetchData(self, year):

        url = "https://www.espncricinfo.com/table/series/8048/season/{}/ipl".format(year)

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        teamNameTags = soup.find_all("span", class_="team-names")
        teamDataTags = soup.find_all("td", class_="")
        heads=[]
        headings=soup.find_all("th")
        for h in headings:
            heads.append(h.text.strip())
        # print(heads)

        iplTeams2019Names = []
        iplTeams2019Data = []

        for tag in teamNameTags:
            iplTeams2019Names.append(tag.text.strip())
            iplTeams2019Data.append([])
        # print(iplTeams2019Names)

        i = 0
        j = 0
        for tag in teamDataTags:

            print(tag.text.strip())
            try:
                iplTeams2019Data[j].append(int(tag.text.strip()))
            except Exception as e:
                iplTeams2019Data[j].append(tag.text.strip())
            # print(iplTeams2019Data[j])

            i += 1

            if i % 9 == 0:
                j += 1


        teams = []
        for i in range(0, len(iplTeams2019Names)):
            # h=Team(heads[0])
            team = Team(year, iplTeams2019Names[i], iplTeams2019Data[i][0], iplTeams2019Data[i][1], iplTeams2019Data[i][2],
                        iplTeams2019Data[i][3], iplTeams2019Data[i][4], iplTeams2019Data[i][5], iplTeams2019Data[i][6],
                        iplTeams2019Data[i][7], iplTeams2019Data[i][8])
            teams.append(team)

        file = open("IPL-TEAMS-DATA.csv", "a")

        for team in teams:
            data = str(team)
            file.write(data)



def main():
    print("==App Started==")

    fRef = FetchTeamsData()
    years = list(range(2008, 2020, 1))
    for year in years:
        fRef.fetchData(year)

    print("==App Finished==")




if __name__ == "__main__":
    main()

table=pd.read_csv("IPL-TEAMS-DATA.csv",header=None)
# df=pd.DataFrame(table)
# print(table)

# n=table.iloc[0:,1]
# print(table.iloc[0:,1]

# print(table.loc[0:2])
# c=table.columns
# print(c)

# 0 r all c
# print(table.loc[0,:])

# 0,1,2 inclusive 0 and 2 rows, and all c
# print(table.loc[0:2,:])

# all r and  col 0,1,2
# print(table.loc[:, 0:2])



d=table.loc[table[1]=="Mumbai Indians", :3]
df2=pd.DataFrame(d)
# print(df2)

d1=table.loc[table[1]=="Sunrisers Hyderabad", :3]
df3=pd.DataFrame(d1)
# print(df3)


# print(table[1]=="Mumbai Indians")
# print(table.loc[table[1]=="Mumbai Indians", :3])
# print(table.loc[table[1]=="Mumbai Indians", :3])

# for i,j in df2.iterrows():
#     print(i,j)
#     print()


# print(d.iloc[:, 3])
t=(d1.iloc[:,3])
t1=(d1.iloc[:,0])
# print(len(t1))
# print(len(t))
g=list(d.iloc[:,3])
# print(len(g))
h=list(d.iloc[:,0])
# print(len(h))

# print(h)
# print(t)

#
# x_indexes=np.arange(len(h))

plt.bar(h,g,label="Mumbai Indians")
plt.bar(t1+0.85,t,color="m",label="Sunrisers Hyderabad")


# plt.xticks(ticks=x_indexes,labels=h)
# plt.xlabel("Years")
# plt.ylabel("No. of matches won")
# plt.title("Team:Mumbai Indians")
plt.legend()
plt.show()