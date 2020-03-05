import requests

import json
# url="http://newsapi.org/v2/everything?q=bitcoin&from=2020-01-16&sortBy=publishedAt&apiKey=e10276558dc244e5a807c72a19d51c59"
url="http://newsapi.org/v2/top-headlines?country=in&apiKey=e10276558dc244e5a807c72a19d51c59"
response=requests.get(url)
print(response,type(response))
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

jsonData=response.text
print(jsonData)
print("!!!!!!!!!!!!!!!!!!!!!!!!")

newsDictionary=json.loads(jsonData)
print(newsDictionary,type(newsDictionary))

print("!!!!!!!!!!!JSON PARSING!!!!!!!!!!!!!")

print("TOTAL NEWS:",newsDictionary["totalResults"])

articles=newsDictionary["articles"]
print(len(articles))
for article in articles:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(article["author"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(article["title"])
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(article["description"])
    print()
    print(article["content"])