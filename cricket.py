import requests
from bs4 import BeautifulSoup

url="https://www.espncricinfo.com/table/series/8048/season/2019/ipl"
response=requests.get(url)
print(response.text)

soup=BeautifulSoup(response.text,"html.parser")
print(soup.prettify())

teams=[]
team=soup.find_all("span",class_="team-names")
for t in team:
    c=t.text.strip()
    teams.append(c)
print(teams)





match=soup.find_all("td",class_="")
for m in match:
    print(m.text)


# print(matches)

for t1 in teams:

    file=open("data.csv",'a',)
    file.write(t1)
    file.close()

