import requests
import matplotlib.pyplot as plt
import re
from bs4 import BeautifulSoup

url="https://www.imdb.com/india/top-rated-indian-movies/"
response=requests.get(url)
# print(response.text)

soup=BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())

movies=[]
years=[]

tags=soup.find_all("td",class_="titleColumn")
for tag in tags:
    # listToStr = ' '.join(map(str, tag.text))
    # print(tag.text)
    # s1 = (re.findall(r"[A-Za-z]+", tag.text.strip()))
    # s2 = (re.findall(r"[0-9]{4}", tag.text.strip()))
    # print(tag)
    movieTitle=tag.text.strip()
    movies.append(movieTitle)
    movieYear=movieTitle[-5:-1]
    years.append(movieYear)

    # print(years)
    r=str(movies)
    r1=r[:-7:1][: :1]
print(r1)


# for movies in r:
#
#     moviesSt.append(r[11:17])
# print(moviesSt)

    # movies.append(s1)
    # year.append(s2)
# print(year)



    # [:-7:1][9::1]




rating=[]
rate=soup.find_all("td",class_="ratingColumn imdbRating")
for r in rate:
    ratingN=float(r.text.strip())
    rating.append(ratingN)
print(rating)
#
# for rt in rating:
#     print(rt)
#
# year=[]
# yr=soup.find_all("td",class_="titleColumn")
# for y in yr:
#     y1=y.text.strip()
#
#     # y2=y1[:-7:1][9: :1]
#
#
#     year.append(y1)
#     print(year)




plt.barh(years,rating)
plt.show()





