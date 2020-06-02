import pandas as pd
import matplotlib.pyplot as plt
movies=pd.read_csv("movies.csv")
# print(movies)
# print(movies.head(10))
# print(movies.title.sort_values())
ttle=movies['title']
# ttle=movies['title'].sort_values(ascending=False)
# print(ttle)

ttle2=movies.sort_values('title')
print(ttle2)
ttle3=movies.sort_values(['content_rating','duration'])
print(ttle3)

print(movies.keys())

title=movies['title']
rating=movies['star_rating']
content=movies['content_rating']
dur=movies['duration']
genre=movies['genre']


print(movies.isnull().sum())
movies['content_rating'].fillna('0',inplace=True)

print(movies.isnull().sum())
# plt.figure(figsize=(16,16))
# # plt.subplot(2,2,1)
# plt.bar(title,rating)
# plt.xlabel('title')
# plt.ylabel('star-Rating')
# plt.xticks(title,labels=title,rotation=90)
# plt.margins(0.2)
# plt.show()
#
# # plt.subplot(2,2,2)
# plt.bar(title,genre)
# plt.xlabel('title')
# plt.ylabel('Genre')
# plt.show()

# # plt.subplot(2,2,3)
# plt.bar(title,rating)
# plt.xlabel('title')
# plt.ylabel('duration')

# plt.subplot(2,2,4)
# plt.bar(title,content)
# plt.xlabel('title')
# plt.ylabel('Content-Rating')

plt.figure(figsize=(32,32))

plt.bar(title,dur,color='r',align='edge',width=0.2)
plt.bar(title,rating+0.1,color='g',align='edge',width=0.1)
# plt.pie(title,genre)
#plot data
# fig, ax = plt.subplots(figsize=(15,7))
# movies.groupby(['title','genre']).count()['duration'].unstack().plot(kind='bar',ax=ax)

plt.show()
