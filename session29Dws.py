import requests
from bs4 import BeautifulSoup
url="https://twitter.com/dna"
# webpage is html program


# we have extracted HTML response from the URL
response=requests.get(url)

# print(response.text)

# HTML parsing
# need to extract only meaningful data  from HTML response
# Beautiful Soup external library installed in our project  used for HTML Parsing

# soup is an object of Beautifulsoup

soup=BeautifulSoup(response.text,"html.parser")

# print(soup)
# print(soup.prettify())
print("------------")
print("Title")
print(soup.title.text)

print("CHILDREN")
children=soup.children
for child in children:
    print(child)
    print("--------------")
print("pTags")
pTags=soup.find_all("p")
for tag in pTags:
    print(tag)
    print("=====================")

print("Div Tags")

divTags=soup.find_all("div",class_="js-tweet-text-container")
for tag in divTags:
    print(tag.text)
    print("=====================")


