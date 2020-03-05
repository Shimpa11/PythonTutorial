import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.espncricinfo.com/table/series/8048/season/2019/ipl"
response=requests.get(url)
print(response.text)

soup=BeautifulSoup(response.text,"html.parser")
print(soup.prettify())
# tags=[]
# tag=soup.find("div",class_="responsive-table-wrap")
# tags.append(tag.text.strip())
# print(tags)



teams=[]
team=soup.find_all("span",class_="team-names")
for t in team:
    c=t.text.strip()
    teams.append(c)

print(teams)



if teams:
    # print("team names:{}".format(','.join(teams)))
    file = open("cricdata.csv", "a")
    for t in teams:
        file.write(t)



data=[]
for tr in soup.find_all("tr"):

    for td in tr.find_all("td"):
        data.append(td.text)
#         df = pd.DataFrame(data)
#
        # t=str(data)
print(data)
#
#         row=[td for td in data]
#         df=df.append(pd.Series(row),ignore_index=True)
#         df.to_csv("cricketdata.csv",index=False)


if data:
        # print("inserting headings{}".format(','.join(t)))
        file=open("cricdata.csv","a")
        for d in data:
            file.write(str(data))


